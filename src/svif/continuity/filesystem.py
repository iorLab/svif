"""Contained filesystem I/O and process locking for Agnir checkpoint transactions.

These are private recovery mechanics, not a second continuity format. On POSIX,
component-relative no-follow opens also prevent ancestor-symlink replacement.
The selected Project root and its parent are a trusted local filesystem boundary.
"""
from __future__ import annotations

import os
import stat
import threading
import time
import uuid
from contextlib import contextmanager
from pathlib import Path
from typing import Iterator


class FilesystemSafetyError(RuntimeError):
    pass


class ProjectFilesystem:
    RUNTIME = ".svif-runtime"
    _registry_lock = threading.Lock()
    _locks: dict[str, threading.RLock] = {}
    _local = threading.local()

    def __init__(self, root: Path) -> None:
        self.root = root.resolve(strict=True)
        if not self.root.is_dir():
            raise FilesystemSafetyError("Project root is not a directory")
        self.relative_io = os.name == "posix" and os.open in os.supports_dir_fd

    def path(self, locator: str | Path) -> Path:
        value = Path(locator)
        if value.is_absolute():
            try:
                value = value.relative_to(self.root)
            except ValueError as exc:
                raise FilesystemSafetyError("locator escapes authorized Project root") from exc
        # Path renders native separators on Windows. Reject a POSIX filename
        # containing backslashes, not normal Windows path separators. Colons
        # in relative components remain forbidden (including NTFS ADS names).
        if (not value.parts or value.drive or value.root
                or any(p in {"..", ""} or ":" in p for p in value.parts)
                or (os.name != "nt" and "\\" in str(value))):
            raise FilesystemSafetyError("unsafe Project-relative path")
        return self.root / value

    @contextmanager
    def _parent(self, path: Path) -> Iterator[tuple[int | None, str | Path]]:
        path = self.path(path)
        parts = path.relative_to(self.root).parts
        if self.relative_io:
            fd = os.open(self.root, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
            try:
                for part in parts[:-1]:
                    child = os.open(part, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=fd)
                    os.close(fd)
                    fd = child
                yield fd, parts[-1]
            finally:
                os.close(fd)
        else:
            current = self.root
            for part in parts[:-1]:
                current /= part
                metadata = current.lstat()
                if (not stat.S_ISDIR(metadata.st_mode) or current.is_symlink()
                        or getattr(current, "is_junction", lambda: False)()):
                    raise FilesystemSafetyError("unsafe ancestor in Project path")
            yield None, path

    def metadata(self, path: Path) -> os.stat_result | None:
        try:
            with self._parent(path) as (fd, leaf):
                result = os.stat(leaf, dir_fd=fd, follow_symlinks=False)
                if stat.S_ISLNK(result.st_mode) or getattr(self.path(path), "is_junction", lambda: False)():
                    raise FilesystemSafetyError("symlinks/reparse points are not authorized continuity locators")
                return result
        except FileNotFoundError:
            return None
        except OSError as exc:
            raise FilesystemSafetyError("cannot safely inspect Project path") from exc

    @staticmethod
    def _regular(metadata: os.stat_result) -> None:
        if not stat.S_ISREG(metadata.st_mode) or metadata.st_nlink != 1:
            raise FilesystemSafetyError("continuity object is not a private regular file")

    def read(self, path: Path, *, missing_ok: bool = False) -> bytes | None:
        try:
            with self._parent(path) as (fd, leaf):
                # O_NONBLOCK prevents a replaced FIFO from hanging before fstat.
                flags = os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0) | getattr(os, "O_NONBLOCK", 0)
                if fd is None:
                    metadata = self.metadata(path)
                    if metadata is None:
                        raise FileNotFoundError(str(path))
                    self._regular(metadata)
                opened = os.open(leaf, flags, dir_fd=fd)
                with os.fdopen(opened, "rb") as stream:
                    self._regular(os.fstat(stream.fileno()))
                    return stream.read()
        except FileNotFoundError:
            if missing_ok:
                return None
            raise FilesystemSafetyError("required continuity file is missing") from None
        except OSError as exc:
            raise FilesystemSafetyError("cannot safely read Project file") from exc

    def files(self, directory: Path) -> list[Path]:
        directory = self.path(directory)
        try:
            with self._parent(directory) as (fd, leaf):
                if self.relative_io:
                    opened = os.open(leaf, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=fd)
                    try:
                        names = os.listdir(opened)
                    finally:
                        os.close(opened)
                else:
                    metadata = self.metadata(directory)
                    if metadata is None or not stat.S_ISDIR(metadata.st_mode):
                        raise FilesystemSafetyError("evidence collection is not a safe directory")
                    names = os.listdir(directory)
            result = []
            for name in sorted(names):
                child = directory / name
                metadata = self.metadata(child)
                if metadata is None:
                    raise FilesystemSafetyError("evidence changed during discovery")
                if stat.S_ISDIR(metadata.st_mode):
                    continue  # The filesystem profile reads immediate evidence files only.
                self._regular(metadata)
                result.append(child)
            return result
        except OSError as exc:
            raise FilesystemSafetyError("cannot safely list evidence collection") from exc

    def write(self, path: Path, content: bytes, *, mode: int = 0o600) -> None:
        """Replace one regular file, fsyncing bytes and the directory on POSIX."""
        path = self.path(path)
        current = self.metadata(path)
        if current is not None:
            self._regular(current)
            mode = stat.S_IMODE(current.st_mode)
        temporary = ".svif-write-" + uuid.uuid4().hex
        try:
            with self._parent(path) as (fd, leaf):
                temp = temporary if fd is not None else path.parent / temporary
                opened = os.open(temp, os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_NOFOLLOW", 0),
                                 mode, dir_fd=fd)
                try:
                    with os.fdopen(opened, "wb") as stream:
                        stream.write(content)
                        stream.flush()
                        os.fsync(stream.fileno())
                    # A no-follow recheck rejects an already-present unsafe leaf;
                    # rename itself does not follow a subsequently swapped leaf.
                    current = self.metadata(path)
                    if current is not None:
                        self._regular(current)
                    os.replace(temp, leaf, src_dir_fd=fd, dst_dir_fd=fd)
                    if fd is not None:
                        os.fsync(fd)
                finally:
                    try:
                        os.unlink(temp, dir_fd=fd)
                    except FileNotFoundError:
                        pass
        except OSError as exc:
            raise FilesystemSafetyError("atomic continuity write failed") from exc

    def remove(self, path: Path) -> None:
        current = self.metadata(path)
        if current is None:
            return
        self._regular(current)
        with self._parent(path) as (fd, leaf):
            os.unlink(leaf, dir_fd=fd)
            if fd is not None:
                os.fsync(fd)

    @contextmanager
    def guard(self, *, timeout: float = 10.0) -> Iterator[None]:
        """Reentrant, cross-process lock; OS releases it on process termination."""
        key = str(self.root)
        with self._registry_lock:
            lock = self._locks.setdefault(key, threading.RLock())
        with lock:
            held = getattr(self._local, "held", None)
            if held is None:
                held = self._local.held = {}
            if key in held:
                yield
                return
            runtime = self.root / self.RUNTIME
            try:
                runtime.mkdir(mode=0o700)
            except FileExistsError:
                pass
            metadata = self.metadata(runtime)
            if metadata is None or not stat.S_ISDIR(metadata.st_mode):
                raise FilesystemSafetyError("unsafe runtime lock directory")
            path = runtime / "agnir.lock"
            with self._parent(path) as (parent, leaf):
                flags = os.O_RDWR | os.O_CREAT | getattr(os, "O_NOFOLLOW", 0)
                fd = os.open(leaf, flags, 0o600, dir_fd=parent)
            try:
                self._regular(os.fstat(fd))
                if os.name == "nt" and os.fstat(fd).st_size == 0:
                    os.write(fd, b"0")
                deadline = time.monotonic() + timeout
                while True:
                    try:
                        if os.name == "nt":
                            import msvcrt
                            os.lseek(fd, 0, os.SEEK_SET)
                            msvcrt.locking(fd, msvcrt.LK_NBLCK, 1)
                        else:
                            import fcntl
                            fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
                        break
                    except (BlockingIOError, OSError):
                        if time.monotonic() >= deadline:
                            raise FilesystemSafetyError("continuity lock is busy; retry after reconciliation")
                        time.sleep(0.01)
                held[key] = fd
                try:
                    yield
                finally:
                    del held[key]
                    if os.name == "nt":
                        import msvcrt
                        os.lseek(fd, 0, os.SEEK_SET)
                        msvcrt.locking(fd, msvcrt.LK_UNLCK, 1)
                    else:
                        import fcntl
                        fcntl.flock(fd, fcntl.LOCK_UN)
            finally:
                os.close(fd)
