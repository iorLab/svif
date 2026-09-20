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


class BootstrapVersionAcceptanceTests(unittest.TestCase):
    """Executable checker regressions, not fabricated native-model observations."""
    @staticmethod
    def release_fixture(package="1.0.2", core="1.0"):
        import base64
        import hashlib
        import json
        sha = "a" * 40
        files = {
            "VERSION": package + "\n",
            "AGNIR.yaml": f'agnir:\n  version: "{core}"\n  discovery_profile: "repository-filesystem/{core}"\n',
            "SKILL.md": "# Agnir fixture installer\n",
            "RELEASE.md": "# Fixture release\n",
            "AGNIR.md": "# Fixture activation\n",
            "spec/AGNIR_CORE_1_0.md": "# Core fixture\n",
            "profiles/REPOSITORY_FILESYSTEM_1_0.md": "# Profile fixture\n",
            "schemas/agnir-manifest-1.0.schema.json": "{}\n",
        }
        replies = {
            "releases/latest": {"id": 123, "tag_name": "v" + package, "draft": False,
                                "prerelease": False, "published_at": "2026-01-01T00:00:00Z"},
            "commits/v" + package: {"sha": sha},
            "contents?ref=" + sha: [{"path": "AGNIR.md", "type": "file"}],
        }
        for name, text in files.items():
            raw = text.encode()
            replies["contents/" + name + "?ref=" + sha] = {
                "type": "file", "encoding": "base64", "content": base64.b64encode(raw).decode(),
                "sha": hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest(),
            }
        calls = []
        def fetch(path):
            calls.append(path)
            return json.loads(json.dumps(replies[path]))
        return replies, calls, fetch

    @staticmethod
    def project_fixture(root, core="1.0", provenance=True):
        from test_agnir_continuity import write_project, PROJECT
        write_project(root, version=core)
        (root / "SVIF.yaml").write_text(
            'svif:\n  manifest: "project-binding/0.2"\n'
            f'project:\n  identity: "{PROJECT}"\n'
            'bindings:\n  continuity:\n    provider: "agnir"\n'
            f'    compatibility: "{core}"\n    profile: "repository-filesystem/{core}"\n'
            '    config:\n      discovery: "AGNIR.yaml"\n', encoding="utf-8")
        (root / "AGNIR.md").write_text("# Installed activation\n", encoding="utf-8")
        (root / "AGENTS.md").write_text("Read AGNIR.md.\n", encoding="utf-8")
        if provenance:
            with (root / "AGNIR.yaml").open("a", encoding="utf-8") as file:
                file.write('extensions:\n  agnir/operations:\n    source: "iorLab/agnir"\n'
                           '    release: "1.0.2"\n    applied_revision: "' + "a" * 40 + '"\n')

    def test_latest_resolution_pins_all_contract_files_and_separates_version_layers(self):
        for package in ("1.0.2", "1.1.7"):
            with self.subTest(package=package):
                _, calls, fetch = self.release_fixture(package=package)
                receipt, files = module.resolve_latest_agnir(fetch)
                self.assertEqual((receipt["release"], receipt["core"]), (package, "1.0"))
                self.assertEqual(receipt["profile"], "repository-filesystem/1.0")
                self.assertEqual(receipt["activation"], "AGNIR.md")
                self.assertEqual(set(receipt["files_sha256"]), set(files))
                self.assertTrue(all(call.endswith("?ref=" + "a" * 40)
                                    for call in calls if call.startswith("contents")))

    def test_latest_rejects_prerelease_branch_unpublished_and_missing_metadata(self):
        for mutation in ({"prerelease": True}, {"draft": True}, {"published_at": None},
                         {"tag_name": "main"}, {"tag_name": "v1.1.0-rc.1"},
                         {"published_at": "2999-01-01T00:00:00Z"}):
            with self.subTest(mutation=mutation):
                replies, calls, fetch = self.release_fixture()
                replies["releases/latest"].update(mutation)
                with self.assertRaises((RuntimeError, ValueError)):
                    module.resolve_latest_agnir(fetch)
                self.assertEqual(calls, ["releases/latest"])

    def test_resolution_failure_never_uses_a_cached_or_older_baseline(self):
        from unittest.mock import Mock
        fetch = Mock(side_effect=OSError("no upstream access"))
        with self.assertRaises(OSError):
            module.resolve_latest_agnir(fetch)
        fetch.assert_called_once_with("releases/latest")

    def test_latest_unsupported_line_fails_before_install_contract_or_project_writes(self):
        _, calls, fetch = self.release_fixture(core="9.9")
        with self.assertRaisesRegex(RuntimeError, "unsupported"):
            module.resolve_latest_agnir(fetch)
        self.assertFalse(any("SKILL.md" in call for call in calls))

    def test_changed_tag_package_or_content_identity_cannot_pass(self):
        for kind in ("commit", "version", "blob"):
            with self.subTest(kind=kind):
                replies, _, fetch = self.release_fixture()
                if kind == "commit":
                    replies["commits/v1.0.2"]["sha"] = "main"
                elif kind == "version":
                    replies["releases/latest"]["tag_name"] = "v1.0.3"
                    replies["commits/v1.0.3"] = {"sha": "a" * 40}
                else:
                    replies["contents/SKILL.md?ref=" + "a" * 40]["sha"] = "b" * 40
                with self.assertRaises(RuntimeError):
                    module.resolve_latest_agnir(fetch)

    def test_existing_projects_preserve_all_supported_lines_without_latest_lookup(self):
        from unittest.mock import patch
        for core in ("0.1", "0.2", "1.0"):
            with self.subTest(core=core), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)
                self.project_fixture(root, core=core, provenance=False)
                before = module.file_map(root)
                with patch.object(module, "canonical_agnir_json", side_effect=AssertionError("unexpected lookup")):
                    provider, identity = module.validate_agnir_binding(root)
                self.assertEqual(module.file_map(root), before)
                self.assertEqual(provider.expected_core_version, core)
                self.assertEqual(provider.load(identity).project_identity, identity)

    def test_existing_binding_conflicts_block_without_reinitialization(self):
        for old, new in (('provider: "agnir"', 'provider: "other"'),
                         ('compatibility: "1.0"', 'compatibility: "0.1"'),
                         ('identity: "urn:test:svif-project"', 'identity: "foreign"'),
                         ('profile: "repository-filesystem/1.0"', 'profile: "repository-filesystem/0.1"')):
            with self.subTest(old=old), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)
                self.project_fixture(root)
                path = root / "SVIF.yaml"
                path.write_text(path.read_text().replace(old, new), encoding="utf-8")
                before = module.file_map(root)
                with self.assertRaises(RuntimeError):
                    module.validate_agnir_binding(root)
                self.assertEqual(module.file_map(root), before)

    def test_fresh_project_must_match_resolved_stable_and_exact_provenance(self):
        _, _, fetch = self.release_fixture()
        stable, _ = module.resolve_latest_agnir(fetch)
        for core, provenance, passed in (("1.0", True, True), ("1.0", False, False),
                                         ("0.1", True, False), ("0.2", True, False)):
            with self.subTest(core=core, provenance=provenance), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)
                self.project_fixture(root, core=core, provenance=provenance)
                before = module.file_map(root)
                if passed:
                    module.validate_agnir_binding(root, stable=stable)
                else:
                    with self.assertRaises(RuntimeError):
                        module.validate_agnir_binding(root, stable=stable)
                self.assertEqual(module.file_map(root), before)

    def test_fresh_activation_or_release_provenance_mismatch_fails(self):
        _, _, fetch = self.release_fixture()
        stable, _ = module.resolve_latest_agnir(fetch)
        for path, old, new in (("AGENTS.md", "AGNIR.md", "README.md"),
                               ("AGNIR.yaml", 'release: "1.0.2"', 'release: "1.0.1"'),
                               ("AGNIR.yaml", "a" * 40, "b" * 40)):
            with self.subTest(path=path, old=old), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)
                self.project_fixture(root)
                file = root / path
                file.write_text(file.read_text().replace(old, new), encoding="utf-8")
                with self.assertRaises(RuntimeError):
                    module.validate_agnir_binding(root, stable=stable)
