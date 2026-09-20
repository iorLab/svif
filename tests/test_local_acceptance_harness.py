"""Tests the acceptance checker itself, NOT native-host acceptance evidence."""
from __future__ import annotations
import importlib.util
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("local_acceptance", ROOT / "checks/check_local_install.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class LocalAcceptanceHarnessTests(unittest.TestCase):
    def test_discovery_requires_exact_enabled_installed_skill_path(self):
        expected = Path("/tmp/installed/skills/svif/SKILL.md")
        good = {"name": "svif", "enabled": True, "path": str(expected)}
        self.assertEqual(module.discovered_skill({"data": [{"skills": [good], "errors": []}]}, expected), good)
        for skills, errors in (([], []), ([dict(good, enabled=False)], []),
                               ([dict(good, path="/tmp/wrong/SKILL.md")], []),
                               ([good, good], []), ([good], [{"message": "invalid Skill"}])):
            with self.subTest(skills=skills), self.assertRaises(RuntimeError):
                module.discovered_skill({"data": [{"skills": skills, "errors": errors}]}, expected)

    def test_file_map_detects_changed_bytes_and_rejects_symlinks(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "item").write_text("before")
            before = module.file_map(root)
            (root / "item").write_text("after")
            self.assertNotEqual(before, module.file_map(root))
            try:
                (root / "alias").symlink_to(root / "item")
            except OSError:
                self.skipTest("symlinks unavailable")
            with self.assertRaises(RuntimeError):
                module.file_map(root)
