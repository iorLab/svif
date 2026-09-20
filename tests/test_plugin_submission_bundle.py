from __future__ import annotations

import hashlib
import importlib.util
import json
import os
import shutil
from unittest.mock import patch
import tempfile
import unittest
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN_ROOT = ROOT / "plugin"
BUILDER = ROOT / "checks" / "build_submission_bundle.py"


def load_builder():
    spec = importlib.util.spec_from_file_location("svif_submission_bundle", BUILDER)
    if spec is None or spec.loader is None:
        raise RuntimeError("unable to load submission bundle builder")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class PluginSubmissionBundleTests(unittest.TestCase):
    def test_builder_is_deterministic_and_exactly_mirrors_plugin_tree(self) -> None:
        builder = load_builder()
        with tempfile.TemporaryDirectory() as temporary:
            first = Path(temporary) / "svif-a.zip"
            second = Path(temporary) / "svif-b.zip"

            first_digest = builder.build_submission_bundle(first)
            second_digest = builder.build_submission_bundle(second)

            self.assertEqual(first_digest, second_digest)
            self.assertEqual(hashlib.sha256(first.read_bytes()).hexdigest(), first_digest)

            source_files = {
                path.relative_to(PLUGIN_ROOT).as_posix(): path.read_bytes()
                for path in PLUGIN_ROOT.rglob("*")
                if path.is_file() and not path.is_symlink()
            }

            with zipfile.ZipFile(first) as archive:
                archive_files = {
                    info.filename: archive.read(info)
                    for info in archive.infolist()
                    if not info.is_dir()
                }

            self.assertEqual(archive_files, source_files)

    def test_archive_has_one_root_safe_paths_and_required_skill_only_contents(self) -> None:
        builder = load_builder()
        with tempfile.TemporaryDirectory() as temporary:
            archive_path = Path(temporary) / "svif.zip"
            builder.build_submission_bundle(archive_path)

            self.assertLessEqual(archive_path.stat().st_size, 100 * 1024 * 1024)

            with zipfile.ZipFile(archive_path) as archive:
                names = [info.filename for info in archive.infolist() if not info.is_dir()]

            self.assertIn("plugin.json", names)
            self.assertIn("skills/svif/SKILL.md", names)
            self.assertIn("assets/svif-directory-icon.png", names)
            self.assertNotIn("mcp.json", names)
            self.assertNotIn(".mcp.json", names)
            self.assertNotIn(".app.json", names)

            for name in names:
                self.assertFalse(name.startswith("/"), name)
                self.assertNotIn("\\", name)
                self.assertEqual(name, name.strip())
                self.assertNotIn("", name.split("/"))
                self.assertNotIn(".", name.split("/"))
                self.assertNotIn("..", name.split("/"))

    def test_rejects_destination_inside_source_without_mutation(self) -> None:
        builder = load_builder()
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary) / "plugin"
            shutil.copytree(PLUGIN_ROOT, root)
            before = {p.relative_to(root): p.read_bytes() for p in root.rglob("*") if p.is_file()}
            with patch.object(builder, "PLUGIN_ROOT", root):
                with self.assertRaises(ValueError):
                    builder.build_submission_bundle(root / "plugin.json")
                with self.assertRaises(ValueError):
                    builder.build_submission_bundle(root / "self.zip")
            self.assertEqual(before, {p.relative_to(root): p.read_bytes() for p in root.rglob("*") if p.is_file()})

    def test_size_entry_and_depth_limits_fail_without_destroying_prior_archive(self) -> None:
        builder = load_builder()
        for limit in ("MAX_ARCHIVE_BYTES", "MAX_MEMBER_BYTES", "MAX_UNCOMPRESSED_BYTES", "MAX_ENTRIES", "MAX_PATH_SEGMENTS"):
            with self.subTest(limit=limit), tempfile.TemporaryDirectory() as temporary:
                output = Path(temporary) / "prior.zip"
                output.write_bytes(b"prior accepted archive")
                with patch.object(builder, limit, 1), self.assertRaises(ValueError):
                    builder.build_submission_bundle(output)
                self.assertEqual(output.read_bytes(), b"prior accepted archive")
                self.assertEqual(list(Path(temporary).glob(".svif-bundle-*")), [])

    def test_missing_required_file_and_invalid_member_names_fail(self) -> None:
        builder = load_builder()
        for bad in ("missing", "space ", "drive:name", "PLUGIN.json"):
            with self.subTest(bad=bad), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary) / "plugin"
                shutil.copytree(PLUGIN_ROOT, root)
                if bad == "missing":
                    (root / "skills/svif/SKILL.md").unlink()
                else:
                    if os.name == "nt" and bad in {"space ", "drive:name", "PLUGIN.json"}:
                        continue  # These spellings cannot be created as distinct NTFS files.
                    (root / bad).write_text("invalid", encoding="utf-8")
                with patch.object(builder, "PLUGIN_ROOT", root), self.assertRaises(ValueError):
                    builder.build_submission_bundle(Path(temporary) / "bad.zip")

    def test_io_failure_leaves_existing_output_untouched(self) -> None:
        builder = load_builder()
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary) / "prior.zip"
            output.write_bytes(b"prior accepted archive")
            with patch.object(builder.zipfile.ZipFile, "writestr", side_effect=OSError("injected")), self.assertRaises(OSError):
                builder.build_submission_bundle(output)
            self.assertEqual(output.read_bytes(), b"prior accepted archive")
            self.assertEqual(list(Path(temporary).glob(".svif-bundle-*")), [])

    def test_symlink_source_and_output_are_rejected(self) -> None:
        builder = load_builder()
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary) / "plugin"
            shutil.copytree(PLUGIN_ROOT, root)
            outside = Path(temporary) / "outside"
            outside.write_text("unchanged", encoding="utf-8")
            try:
                (root / "linked").symlink_to(outside)
            except OSError:
                self.skipTest("symlinks unavailable")
            with patch.object(builder, "PLUGIN_ROOT", root), self.assertRaises(ValueError):
                builder.build_submission_bundle(Path(temporary) / "bad.zip")
            output = Path(temporary) / "output.zip"
            output.symlink_to(outside)
            with self.assertRaises(ValueError):
                builder.build_submission_bundle(output)
            self.assertEqual(outside.read_text(), "unchanged")

    def test_manifest_remains_skills_only_for_zip_submission(self) -> None:
        manifest = json.loads((PLUGIN_ROOT / "plugin.json").read_text(encoding="utf-8"))
        interface = manifest["extensions"]["com.openai"]["interface"]

        self.assertEqual(manifest["name"], "svif")
        self.assertEqual(manifest["version"], (ROOT / "VERSION").read_text(encoding="utf-8").strip())
        self.assertNotIn("mcpServers", manifest)
        self.assertNotIn("apps", manifest["extensions"]["com.openai"])
        self.assertNotIn("screenshots", interface)


if __name__ == "__main__":
    unittest.main()
