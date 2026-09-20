#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import os
import tempfile
import stat
import unicodedata
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUGIN_ROOT = ROOT / "plugin"
DOS_EPOCH = (1980, 1, 1, 0, 0, 0)
MAX_ARCHIVE_BYTES = 100 * 1024 * 1024
MAX_MEMBER_BYTES = 100 * 1024 * 1024
MAX_UNCOMPRESSED_BYTES = 512 * 1024 * 1024
MAX_ENTRIES = 5000
MAX_PATH_SEGMENTS = 20


def iter_plugin_files() -> list[Path]:
    if PLUGIN_ROOT.is_symlink() or not PLUGIN_ROOT.is_dir():
        raise ValueError("plugin root must be a real directory")
    files: list[Path] = []
    for path in sorted(PLUGIN_ROOT.rglob("*"), key=lambda item: item.as_posix()):
        if path.is_symlink():
            raise ValueError(f"submission package must not contain symlinks: {path.relative_to(PLUGIN_ROOT)}")
        if path.is_file():
            if path.stat().st_nlink != 1:
                raise ValueError("submission source contains a hardlinked file")
            files.append(path)
        elif not path.is_dir():
            raise ValueError("submission source contains a non-regular object")
    if not files:
        raise ValueError("submission package is empty")
    if len(files) > MAX_ENTRIES:
        raise ValueError(f"submission package exceeds {MAX_ENTRIES} entries")

    total_bytes = 0
    normalized_paths: set[str] = set()
    for path in files:
        relative = path.relative_to(PLUGIN_ROOT).as_posix()
        parts = relative.split("/")
        if relative != relative.strip() or relative.startswith("/") or "\\" in relative:
            raise ValueError(f"unsafe submission member path: {relative!r}")
        if any(part in {"", ".", ".."} or part != part.strip() or ":" in part for part in parts):
            raise ValueError(f"unsafe submission member segment: {relative!r}")
        if len(parts) > MAX_PATH_SEGMENTS:
            raise ValueError(f"submission member path exceeds {MAX_PATH_SEGMENTS} segments: {relative}")
        normalized = unicodedata.normalize("NFC", relative).casefold()
        if normalized in normalized_paths:
            raise ValueError(f"submission member normalization collision: {relative}")
        normalized_paths.add(normalized)

        size = path.stat().st_size
        if size > MAX_MEMBER_BYTES:
            raise ValueError(f"submission member exceeds 100 MiB: {relative}")
        total_bytes += size

    if total_bytes > MAX_UNCOMPRESSED_BYTES:
        raise ValueError("submission package exceeds 512 MiB uncompressed limit")
    return files


def build_submission_bundle(output: Path) -> str:
    if output.is_symlink():
        raise ValueError("destination must not be a symlink")
    output = output.resolve()
    if output.is_relative_to(PLUGIN_ROOT.resolve()) or output.suffix.lower() != ".zip":
        raise ValueError("destination must be a ZIP outside the source plugin tree")
    files = iter_plugin_files()
    members = {path.relative_to(PLUGIN_ROOT).as_posix() for path in files}
    required = {"plugin.json", "skills/svif/SKILL.md", "assets/svif-directory-icon.png"}
    if missing := sorted(required - members):
        raise ValueError(f"submission package missing required files: {missing}")
    output.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary_name = tempfile.mkstemp(prefix=".svif-bundle-", suffix=".zip", dir=output.parent)
    os.close(fd)
    temporary = Path(temporary_name)
    try:
        with zipfile.ZipFile(temporary, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
            for path in files:
                relative = path.relative_to(PLUGIN_ROOT).as_posix()
                if path.is_symlink() or path.stat().st_nlink != 1:
                    raise ValueError("submission source changed during packaging")
                info = zipfile.ZipInfo(relative, DOS_EPOCH)
                info.compress_type = zipfile.ZIP_DEFLATED
                info.create_system = 3
                info.external_attr = (stat.S_IFREG | 0o644) << 16
                archive.writestr(info, path.read_bytes(), compresslevel=9)
        if temporary.stat().st_size > MAX_ARCHIVE_BYTES:
            raise ValueError("submission archive exceeds 100 MiB compressed limit")
        digest = hashlib.sha256(temporary.read_bytes()).hexdigest()
        os.replace(temporary, output)
        return digest
    finally:
        temporary.unlink(missing_ok=True)


def main() -> None:
    parser = argparse.ArgumentParser(description="Build deterministic Svif Skills-only submission ZIP")
    parser.add_argument("--output", type=Path, required=True, help="destination ZIP path")
    args = parser.parse_args()
    digest = build_submission_bundle(args.output)
    print(f"{args.output.resolve()} sha256:{digest}")


if __name__ == "__main__":
    main()
