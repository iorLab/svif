from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "plugin" / "skills" / "svif" / "SKILL.md"


class PluginAgnirDiscoveryTests(unittest.TestCase):
    def test_skill_requires_authority_to_select_one_project_root_before_discovery(self) -> None:
        text = SKILL.read_text(encoding="utf-8")

        root_selection = text.index("select exactly one Project root")
        ambiguity = text.index("AGNIR_DISCOVERY_AMBIGUOUS")
        manifest = text.index("When `AGNIR.yaml` is available")

        self.assertLess(root_selection, ambiguity)
        self.assertLess(ambiguity, manifest)
        self.assertIn(
            "a parent or child Project with its own `AGNIR.yaml` does not make that selected root ambiguous",
            text,
        )
        self.assertIn(
            "MUST NOT be searched as a replacement",
            text,
        )

    def test_skill_resolves_one_record_and_detects_chain_conflicts_before_compatibility(self) -> None:
        text = SKILL.read_text(encoding="utf-8")

        record = text.index("resolve exactly one authoritative Discovery Record")
        not_found = text.index("AGNIR_DISCOVERY_NOT_FOUND")
        chain_checks = text.index("Detect Locator Chain cycles and conflicting candidate records")
        compatibility = text.index("validate `agnir.version`")

        self.assertLess(record, not_found)
        self.assertLess(not_found, chain_checks)
        self.assertLess(chain_checks, compatibility)

    def test_skill_validates_compatibility_and_identity_before_loading_memory(self) -> None:
        text = SKILL.read_text(encoding="utf-8")

        compatibility = text.index("validate `agnir.version`")
        profile = text.index("validate `agnir.discovery_profile`")
        identity = text.index("verify that `project.identity`")
        locator = text.index("resolve the required memory locators")
        load = text.index("After validation, treat the Project-managed Agnir state")

        self.assertLess(compatibility, profile)
        self.assertLess(profile, identity)
        self.assertLess(identity, locator)
        self.assertLess(locator, load)

    def test_skill_surfaces_all_named_agnir_discovery_failures_without_fallback_search(self) -> None:
        text = SKILL.read_text(encoding="utf-8")

        for marker in (
            "AGNIR_DISCOVERY_NOT_FOUND",
            "AGNIR_DISCOVERY_AMBIGUOUS",
            "AGNIR_DISCOVERY_UNSUPPORTED_VERSION",
            "AGNIR_DISCOVERY_PROJECT_MISMATCH",
            "AGNIR_DISCOVERY_UNRESOLVABLE",
            "AGNIR_DISCOVERY_UNAUTHORIZED",
            "AGNIR_DISCOVERY_CYCLE",
            "AGNIR_DISCOVERY_STALE",
            "AGNIR_DISCOVERY_INCONSISTENT",
            "sibling repositories",
            "parent/child Projects",
            "chat history",
            "retired layouts",
        ):
            self.assertIn(marker, text)

        self.assertIn("repair the earliest violated discovery invariant", text)
        self.assertIn("original authorized Project Entry Point", text)

    def test_svif_binding_and_skill_agree_on_current_agnir_identity_and_compatibility(self) -> None:
        skill = SKILL.read_text(encoding="utf-8")
        agnir = (ROOT / "AGNIR.yaml").read_text(encoding="utf-8")
        svif = (ROOT / "SVIF.yaml").read_text(encoding="utf-8")

        self.assertIn('version: "0.1"', agnir)
        self.assertIn('discovery_profile: "repository-filesystem/0.1"', agnir)
        self.assertIn('identity: "urn:svif:project:svif-core"', agnir)
        self.assertIn('compatibility: "0.1"', svif)
        self.assertIn('profile: "repository-filesystem/0.1"', svif)

        for marker in (
            "Agnir Core `0.1`",
            "profile `repository-filesystem/0.1`",
            "Project identity `urn:svif:project:svif-core`",
        ):
            self.assertIn(marker, skill)

    def test_discovery_guard_test_is_registered_in_project_binding(self) -> None:
        svif = (ROOT / "SVIF.yaml").read_text(encoding="utf-8")
        self.assertIn(
            'plugin_agnir_discovery: "tests/test_plugin_agnir_discovery.py"',
            svif,
        )


if __name__ == "__main__":
    unittest.main()
