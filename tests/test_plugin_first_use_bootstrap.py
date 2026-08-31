from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "plugin" / "skills" / "svif" / "SKILL.md"


class PluginFirstUseBootstrapTests(unittest.TestCase):
    def test_uninitialized_project_bootstraps_before_not_found(self) -> None:
        text = SKILL.read_text(encoding="utf-8")

        bootstrap = text.index("### Bootstrap a Project that has no continuity binding")
        first_use = text.index("classify it as a **first-use bootstrap**")
        no_separate_prompt = text.index("Do not make the user issue a separate Agnir initialization prompt")
        not_found = text.index("surface `AGNIR_DISCOVERY_NOT_FOUND`")

        self.assertLess(bootstrap, first_use)
        self.assertLess(first_use, no_separate_prompt)
        self.assertLess(no_separate_prompt, not_found)

        for marker in (
            "Do not require the user to initialize Agnir separately",
            "no `SVIF.yaml` continuity binding",
            "no `AGNIR.yaml`",
            "no Project instruction or durable configuration selecting another Continuity Provider",
            "first-use bootstrap",
            "same stable Project identity",
            "Agnir Core `0.1`",
            "repository-filesystem/0.1",
            "create top-level `AGNIR.yaml`",
            "`.agnir/state.md`",
            "`.agnir/next-actions.md`",
            "`.agnir/decisions.md`",
            "`.agnir/evidence/`",
            "minimal Agnir locator",
            "minimal repository/filesystem `SVIF.yaml`",
            "project-binding/0.2",
            'continuity.provider: "agnir"',
            'compatibility `"0.1"`',
            'discovery `"AGNIR.yaml"`',
            "continue the user's original Project task in the same operation",
        ):
            self.assertIn(marker, text)

    def test_bootstrap_does_not_overwrite_existing_or_conflicting_continuity(self) -> None:
        text = SKILL.read_text(encoding="utf-8")

        for marker in (
            "Preserve unrelated Project documentation and instructions",
            "merge only the minimal locator",
            "If a material existing instruction conflicts with Agnir activation",
            "surface the conflict to the Principal",
            "Do not treat partial or contradictory Agnir/Svif artifacts as a clean first-use bootstrap",
            "enter repair and preserve the applicable Agnir failure class",
            "intentionally selects a different Continuity Provider",
            "do not overwrite it with Agnir",
        ):
            self.assertIn(marker, text)

    def test_bootstrap_is_self_contained_and_does_not_create_external_effect_authority(self) -> None:
        text = SKILL.read_text(encoding="utf-8")

        for marker in (
            "does not grant authority for protected external effects",
            "MUST NOT require the Agnir Skill repository",
            "previous Agnir installation conversation",
            "successful first use must remain possible from the Svif Plugin procedure itself",
            "bootstrap capability blocker",
        ):
            self.assertIn(marker, text)


if __name__ == "__main__":
    unittest.main()
