from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "plugin" / "skills" / "svif" / "SKILL.md"


class PluginAgnirDiscoveryTests(unittest.TestCase):
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

    def test_skill_surfaces_current_agnir_discovery_failures_without_fallback_search(self) -> None:
        text = SKILL.read_text(encoding="utf-8")

        for marker in (
            "AGNIR_DISCOVERY_UNSUPPORTED_VERSION",
            "AGNIR_DISCOVERY_PROJECT_MISMATCH",
            "broken required locator",
            "sibling repositories",
            "parent/child Projects",
            "chat history",
            "retired layouts",
        ):
            self.assertIn(marker, text)

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
