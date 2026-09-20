from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "plugin" / "skills" / "svif" / "SKILL.md"


class PluginFirstUseBootstrapTests(unittest.TestCase):
    def test_existing_agnir_project_preserves_declared_compatibility(self) -> None:
        text = SKILL.read_text(encoding="utf-8")

        for marker in (
            "Existing Agnir Project: preserve the declared compatibility line",
            "Dispatch according to the compatibility identifiers the Project actually declares",
            "A valid Core/profile `0.1` Project remains `0.1`",
            "a valid `0.2` Project remains `0.2`",
            "a valid `1.0` Project remains `1.0`",
            "authorization to migrate or relabel compatibility",
            "`compatibility` equal to the existing `agnir.version`",
            "`profile` equal to the existing `agnir.discovery_profile`",
            "An operational Agnir package upgrade and a Core/profile compatibility migration are different operations",
        ):
            self.assertIn(marker, text)

    def test_genuinely_new_project_resolves_latest_published_stable(self) -> None:
        text = SKILL.read_text(encoding="utf-8")

        first_use = text.index("classify it as a **first-use bootstrap**")
        no_separate_prompt = text.index("Do not make the user issue a separate Agnir initialization prompt")
        not_found = text.index("surface `AGNIR_DISCOVERY_NOT_FOUND`")
        self.assertLess(first_use, no_separate_prompt)
        self.assertLess(no_separate_prompt, not_found)

        for marker in (
            "latest published stable release",
            "published non-prerelease tag/Release",
            "never substitute moving `main`",
            "Package SemVer and Core/profile compatibility are distinct version layers",
            "use the Core/profile declared by the resolved stable release",
            "Do not fall back to Core/profile `0.1`",
            "record immutable Agnir operational provenance",
            "`compatibility` equal to the newly created `AGNIR.yaml -> agnir.version`",
            "`profile` equal to `AGNIR.yaml -> agnir.discovery_profile`",
            "continue the user's original Project task in the same operation",
        ):
            self.assertIn(marker, text)

    def test_existing_broken_or_other_provider_is_not_clean_bootstrap(self) -> None:
        text = SKILL.read_text(encoding="utf-8")
        for marker in (
            "partial or contradictory Agnir/Svif artifacts",
            "enter repair and preserve the applicable Agnir failure class",
            "Do not silently replace that Project",
            "intentionally selects a different Continuity Provider",
            "do not overwrite it with Agnir",
            "A mismatch is a repair/binding case",
        ):
            self.assertIn(marker, text)

    def test_activation_dispatch_preserves_installed_contract(self) -> None:
        text = SKILL.read_text(encoding="utf-8")
        for marker in (
            "Activate according to the Project's installed Agnir contract",
            "Do not infer the activation route from the newest available version",
            "AGENTS.md -> README.md / Agnir Project Instructions -> AGNIR.yaml",
            "AGENTS.md -> AGNIR.md -> AGNIR.yaml",
            "Preserve a valid existing route unless an explicit compatible operational upgrade or repair authorizes changing it",
            "`AGENTS.md` remains locator-only",
        ):
            self.assertIn(marker, text)

    def test_existing_resume_is_offline_and_new_unsupported_latest_does_not_downgrade(self) -> None:
        text = SKILL.read_text(encoding="utf-8")
        for marker in (
            "does not require a latest-release lookup",
            "Preserve its recorded operational release/provenance",
            "absent optional package provenance is not evidence of an uninitialized Project",
            "fresh, same-operation canonical release-resolution receipt",
            "Before writing any Project files",
            "If unsupported, stop without initializing or selecting an older release",
        ):
            self.assertIn(marker, text)

    def test_preview_history_does_not_pin_current_bootstrap(self) -> None:
        text = SKILL.read_text(encoding="utf-8")
        self.assertIn("released `v0.2.0-preview.1` artifact is immutable historical evidence", text)
        self.assertIn("current unpublished `0.2.0` line deliberately supersedes that historical bootstrap rule", text)
        self.assertNotIn("Initialize the Agnir `repository-filesystem/0.1` continuity contract", text)

    def test_bootstrap_does_not_create_external_effect_authority_or_require_prior_install(self) -> None:
        text = SKILL.read_text(encoding="utf-8")
        for marker in (
            "does not grant authority for protected external effects",
            "MUST NOT require a preinstalled Agnir Skill",
            "previous Agnir installation conversation",
            "If that resolution is unavailable, surface the blocker instead of inventing a version",
            "bootstrap capability blocker",
        ):
            self.assertIn(marker, text)


if __name__ == "__main__":
    unittest.main()
