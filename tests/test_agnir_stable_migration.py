from __future__ import annotations

import re
import unittest
from pathlib import Path

from svif.continuity.agnir import AgnirFilesystemContinuityProvider


ROOT = Path(__file__).resolve().parents[1]
PROJECT = "urn:svif:project:svif-core"
SKILL = ROOT / "plugin" / "skills" / "svif" / "SKILL.md"


class PublishedAgnirStableMigrationTests(unittest.TestCase):
    def test_repository_self_consumes_published_core_0_2(self) -> None:
        agnir = (ROOT / "AGNIR.yaml").read_text(encoding="utf-8")
        svif = (ROOT / "SVIF.yaml").read_text(encoding="utf-8")

        self.assertIn('version: "0.2"', agnir)
        self.assertIn('discovery_profile: "repository-filesystem/0.2"', agnir)
        self.assertIn('release: "0.2.0"', agnir)
        self.assertIn(
            'applied_revision: "fc84095ed5d500be9e1b43a4af0e93356571bbd4"',
            agnir,
        )
        self.assertIn('compatibility: "0.2"', svif)
        self.assertIn('profile: "repository-filesystem/0.2"', svif)

        provider = AgnirFilesystemContinuityProvider(
            ROOT,
            expected_core_version="0.2",
            expected_profile="repository-filesystem/0.2",
        )
        snapshot = provider.load(PROJECT)
        lineage = provider.resolve_lineage(PROJECT)

        self.assertEqual(snapshot.project_identity, PROJECT)
        self.assertTrue(lineage)
        self.assertIn("Svif", snapshot.state or "")
        self.assertIn("Svif", snapshot.next_actions or "")

        lineage_match = re.search(r"^\s{2}lineage:\s*\"([^\"]+)\"", agnir, re.MULTILINE)
        selector_match = re.search(r"^\s{6}selector:\s*\"([^\"]+)\"", agnir, re.MULTILINE)
        self.assertIsNotNone(lineage_match)
        self.assertIsNotNone(selector_match)
        self.assertNotEqual(lineage_match.group(1), selector_match.group(1))
        self.assertIn(f'lineage: "{lineage_match.group(1)}"', svif)
        self.assertIn(f'vcs_selector: "{selector_match.group(1)}"', svif)

    def test_migration_preserves_project_identity_and_memory_locators(self) -> None:
        agnir = (ROOT / "AGNIR.yaml").read_text(encoding="utf-8")
        for marker in (
            'identity: "urn:svif:project:svif-core"',
            'state: ".agnir/state.md"',
            'next_actions: ".agnir/next-actions.md"',
            'decisions: ".agnir/decisions.md"',
            'evidence: ".agnir/evidence/"',
        ):
            self.assertIn(marker, agnir)

    def test_skill_distinguishes_current_self_host_from_released_preview_bootstrap(self) -> None:
        text = SKILL.read_text(encoding="utf-8")

        for marker in (
            "For the current Svif repository binding, the expected values are Agnir Core `0.2`",
            "profile `repository-filesystem/0.2`",
            "one explicit logical Continuity Lineage",
            "matching durable VCS selector binding",
            "The released `v0.2.0-preview.1` first-use bootstrap remains",
            "Core/profile `0.1` baseline",
            "published Agnir repository release `v0.2.0`",
        ):
            self.assertIn(marker, text)

        self.assertIn("Initialize the Agnir `repository-filesystem/0.1` continuity contract", text)
        self.assertIn('compatibility `"0.1"`', text)
        self.assertIn("Core `0.2`, require a non-empty logical `continuity.lineage`", text)
        self.assertIn("AGNIR_LINEAGE_REQUIRED", text)


if __name__ == "__main__":
    unittest.main()
