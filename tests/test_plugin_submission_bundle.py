from __future__ import annotations

import hashlib
import importlib.util
import json
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
