"""Validate native receipt matching; no model calls or simulated install claims."""
from __future__ import annotations

import copy
import hashlib
import importlib.util
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("native_acceptance", ROOT / "checks/check_native_install.py")
assert spec is not None and spec.loader is not None
native = importlib.util.module_from_spec(spec)
spec.loader.exec_module(native)


class NativeInstallEvidenceTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.project = self.root / "ordinary-project"
        self.project.mkdir()
        self.installed = self.root / "installed"
        self.skill = self.installed / "skills/svif/SKILL.md"
        self.skill.parent.mkdir(parents=True)
        self.skill.write_bytes(b"fixture Skill bytes\n")
        self.digest = hashlib.sha256(self.skill.read_bytes()).hexdigest()
        self.response = {"data": [{"cwd": str(self.project), "errors": [], "skills": [
            {"name": "svif:svif", "pluginId": "svif@svif", "enabled": True,
             "path": str(self.skill)}]}]}

    def check(self, response: dict) -> dict:
        return native.validate_discovery(response, self.project, self.installed, self.digest)

    def test_namespaced_native_skill_and_explicit_legacy_origin(self) -> None:
        for name in ("svif:svif", "svif"):
            with self.subTest(name=name):
                self.response["data"][0]["skills"][0]["name"] = name
                self.assertEqual(self.check(self.response)["name"], name)

    def test_rejects_missing_or_wrong_plugin_origin_and_disabled_states(self) -> None:
        for key, value in (("pluginId", None), ("pluginId", "svif@untrusted"),
                           ("enabled", None), ("enabled", False), ("enabled", "true"),
                           ("name", "another:svif")):
            with self.subTest(key=key, value=value):
                response = copy.deepcopy(self.response)
                skill = response["data"][0]["skills"][0]
                if value is None:
                    skill.pop(key)
                else:
                    skill[key] = value
                with self.assertRaises(RuntimeError):
                    self.check(response)

    def test_rejects_other_project_duplicate_results_and_error_reports(self) -> None:
        for change in ("cwd", "duplicate_rows", "duplicate_skills", "errors", "missing_errors"):
            with self.subTest(change=change):
                response = copy.deepcopy(self.response)
                row = response["data"][0]
                if change == "cwd": row["cwd"] = str(self.root)
                elif change == "duplicate_rows": response["data"].append(copy.deepcopy(row))
                elif change == "duplicate_skills": row["skills"] *= 2
                elif change == "errors": row["errors"] = [{"message": "parse failure"}]
                else: row.pop("errors")
                with self.assertRaises(RuntimeError):
                    self.check(response)

    def test_identical_bytes_at_another_path_are_not_installation_evidence(self) -> None:
        impostor = self.root / "SKILL.md"
        impostor.write_bytes(self.skill.read_bytes())
        self.response["data"][0]["skills"][0]["path"] = str(impostor)
        with self.assertRaises(RuntimeError):
            self.check(self.response)

    def test_changed_skill_bytes_fail(self) -> None:
        self.skill.write_bytes(b"changed\n")
        with self.assertRaises(RuntimeError):
            self.check(self.response)

    def test_builtin_unrelated_skills_are_not_mistaken_for_svif(self) -> None:
        self.response["data"][0]["skills"].append({"name": "skill-creator", "enabled": True})
        self.assertEqual(self.check(self.response)["pluginId"], "svif@svif")


if __name__ == "__main__":
    unittest.main()
