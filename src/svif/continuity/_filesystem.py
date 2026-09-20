"""Confined file access and recoverable, cooperating-reader transactions.

POSIX access walks directory descriptors with O_NOFOLLOW. Windows uses the same
no-link validation and a process lock; hostile concurrent directory replacement
by another process with the same filesystem permissions is outside its boundary.
Readers/writers must use locked() and recover() before accessing memory. Ordinary
filesystem readers do not receive multi-file snapshot isolation.
"""
from __future__ import annotations

import json
import os
import stat
import threading
import uuid
from contextlib import contextmanager
from pathlib import Path
from typing import Callable, Iterator


class StorageError(RuntimeError):
    def __init__(self, code: str, message: str) -> None:
        super().__init__(message)
        self.code = code


class ProjectFiles:
    LOCK = ".svif-continuity.lock"
    JOURNAL = ".svif-checkpoint.json"
    PENDING_EFFECT = ".svif-effect-pending.json"
    MAX_JOURNAL_BYTES = 64 * 1024 * 1024

    def __init__(self, root: Path) -> None:
        self.root = root.resolve()
        self._mutex = threading.RLock()
        self._local = threading.local()

    def path(self, value: str | Path, *, internal: bool = False) -> Path:
        path = Path(value)
        if not path.is_absolute():
            path = self.root / path
        try:
            parts = path.relative_to(self.root).parts
        except ValueError as exc:
            raise StorageError("AGNIR_DISCOVERY_UNRESOLVABLE", "path escapes selected Project") from exc
        if not parts or ".." in parts or (not internal and parts[0] in {self.LOCK, self.JOURNAL, self.PENDING_EFFECT}):
            raise StorageError("AGNIR_DISCOVERY_UNRESOLVABLE", "invalid/reserved continuity path")
        current = self.root
        for part in parts:
            current /= part
            if current.is_symlink() or (hasattr(current, "is_junction") and current.is_junction()):
                raise StorageError("AGNIR_DISCOVERY_UNRESOLVABLE", f"continuity path contains a link: {path}")
        return path

    @contextmanager
    def _parent(self, path: Path) -> Iterator[tuple[int | None, str]]:
        path = self.path(path, internal=True)
        if os.name != "posix":
            yield None, str(path)
            return
        fd = os.open(self.root, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
        try:
            for part in path.relative_to(self.root).parts[:-1]:
                new_fd = os.open(part, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=fd)
                os.close(fd)
                fd = new_fd
            yield fd, path.name
        finally:
            os.close(fd)

    @staticmethod
    def _regular(fd: int) -> None:
        info = os.fstat(fd)
        if not stat.S_ISREG(info.st_mode) or info.st_nlink != 1:
            raise StorageError("AGNIR_DISCOVERY_UNRESOLVABLE", "continuity target must be a single-link regular file")

    def read(self, path: Path, *, missing: bool = False) -> str | None:
        with self._parent(path) as (parent, name):
            try:
                fd = os.open(name, os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0) | getattr(os, "O_NONBLOCK", 0), dir_fd=parent)
            except FileNotFoundError:
                if missing:
                    return None
                raise
            try:
                self._regular(fd)
                with os.fdopen(fd, "r", encoding="utf-8", newline="") as stream:
                    fd = -1
                    return stream.read()
            finally:
                if fd != -1:
                    os.close(fd)

    def write(self, path: Path, content: str) -> None:
        """Durably replace one file without opening a predictable temporary path."""
        with self._parent(path) as (parent, name):
            mode = 0o600
            try:
                info = os.stat(name, dir_fd=parent, follow_symlinks=False)
                if not stat.S_ISREG(info.st_mode) or info.st_nlink != 1:
                    raise StorageError("AGNIR_DISCOVERY_UNRESOLVABLE", "unsafe write target")
                mode = stat.S_IMODE(info.st_mode)
            except FileNotFoundError:
                pass
            temporary = f".{Path(name).name}.{uuid.uuid4().hex}.svif-tmp"
            if parent is None:
                temporary = str(Path(name).parent / temporary)
            fd = os.open(temporary, os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_NOFOLLOW", 0), mode, dir_fd=parent)
            try:
                with os.fdopen(fd, "w", encoding="utf-8", newline="") as stream:
                    fd = -1
                    stream.write(content)
                    stream.flush()
                    os.fsync(stream.fileno())
                os.replace(temporary, name, src_dir_fd=parent, dst_dir_fd=parent)
                if parent is not None:
                    os.fsync(parent)
            finally:
                if fd != -1:
                    os.close(fd)
                try:
                    os.unlink(temporary, dir_fd=parent)
                except FileNotFoundError:
                    pass

    def remove(self, path: Path) -> None:
        with self._parent(path) as (parent, name):
            try:
                info = os.stat(name, dir_fd=parent, follow_symlinks=False)
            except FileNotFoundError:
                return
            if not stat.S_ISREG(info.st_mode) or info.st_nlink != 1:
                raise StorageError("AGNIR_DISCOVERY_UNRESOLVABLE", "unsafe removal target")
            os.unlink(name, dir_fd=parent)
            if parent is not None:
                os.fsync(parent)

    @contextmanager
    def locked(self) -> Iterator[None]:
        """Fail busy rather than return a mixed snapshot or wait indefinitely."""
        if not self._mutex.acquire(blocking=False):
            raise StorageError("AGNIR_CHECKPOINT_BUSY", "Project continuity is busy")
        fd = None
        nested = getattr(self._local, "depth", 0) > 0
        try:
            if not nested:
                with self._parent(self.root / self.LOCK) as (parent, name):
                    fd = os.open(name, os.O_RDWR | os.O_CREAT | getattr(os, "O_NOFOLLOW", 0), 0o600, dir_fd=parent)
                self._regular(fd)
                try:
                    if os.name == "posix":
                        import fcntl
                        fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
                    elif os.name == "nt":
                        import msvcrt
                        if os.fstat(fd).st_size == 0:
                            os.write(fd, b"\0")
                        os.lseek(fd, 0, os.SEEK_SET)
                        msvcrt.locking(fd, msvcrt.LK_NBLCK, 1)
                    else:
                        raise StorageError("AGNIR_CHECKPOINT_UNSUPPORTED", "OS has no supported Project lock")
                except OSError as exc:
                    raise StorageError("AGNIR_CHECKPOINT_BUSY", "another process owns Project continuity") from exc
            self._local.depth = getattr(self._local, "depth", 0) + 1
            try:
                yield
            finally:
                self._local.depth -= 1
        finally:
            if fd is not None:
                # Closing releases the OS lock, including after abrupt process exit.
                os.close(fd)
            self._mutex.release()

    def recover(self, authorize: Callable[[dict], set[Path]]) -> None:
        journal_path = self.root / self.JOURNAL
        text = self.read(journal_path, missing=True)
        if text is None:
            return
        try:
            if len(text.encode("utf-8")) > self.MAX_JOURNAL_BYTES:
                raise ValueError("oversized journal")
            journal = json.loads(text)
            if journal["version"] != 1 or journal["phase"] not in {"prepared", "committed"}:
                raise ValueError("unsupported journal")
            allowed = authorize(journal["context"])
            entries = journal["entries"]
            if not isinstance(entries, list) or not entries:
                raise ValueError("empty journal")
            checked = []
            seen = set()
            # Validate EVERY target and before/after pair before any recovery write.
            for entry in entries:
                path = self.path(entry["path"])
                if path not in allowed or path in seen:
                    raise ValueError("journal target not authorized or duplicated")
                seen.add(path)
                before, after = entry["before"], entry["after"]
                if (before is not None and not isinstance(before, str)) or not isinstance(after, str):
                    raise ValueError("invalid journal value")
                current = self.read(path, missing=True)
                if current not in (before, after):
                    raise ValueError("external edit conflicts with incomplete checkpoint")
                checked.append((path, before if journal["phase"] == "prepared" else after))
            for path, value in checked:
                if value is None:
                    self.remove(path)
                else:
                    self.write(path, value)
            self.remove(journal_path)
        except (KeyError, TypeError, ValueError, OSError, StorageError) as exc:
            raise StorageError("AGNIR_CHECKPOINT_RECOVERY_REQUIRED", "cannot safely recover checkpoint; preserve journal and reconcile") from exc

    def publish(self, writes: dict[Path, str], context: dict, authorize: Callable[[dict], set[Path]]) -> None:
        entries = []
        for path, after in writes.items():
            path = self.path(path)
            if path not in authorize(context):
                raise StorageError("AGNIR_DISCOVERY_UNRESOLVABLE", "checkpoint target not authorized")
            entries.append({"path": path.relative_to(self.root).as_posix(), "before": self.read(path, missing=True), "after": after})
        if not entries:
            return
        journal = {"version": 1, "phase": "prepared", "context": context, "entries": entries}
        text = json.dumps(journal, ensure_ascii=False, sort_keys=True)
        if len(text.encode("utf-8")) > self.MAX_JOURNAL_BYTES:
            raise StorageError("AGNIR_CHECKPOINT_LIMIT", "checkpoint journal exceeds configured safety limit")
        journal_path = self.root / self.JOURNAL
        self.write(journal_path, text)
        try:
            for path, after in writes.items():
                self.write(path, after)
            journal["phase"] = "committed"
            self.write(journal_path, json.dumps(journal, ensure_ascii=False, sort_keys=True))
        except Exception:
            self.recover(authorize)
            raise
        # The commit marker is the durable decision. Cleanup failure is not rollback:
        # the next cooperating reader finishes the committed transaction.
        try:
            self.remove(journal_path)
        except OSError:
            pass
