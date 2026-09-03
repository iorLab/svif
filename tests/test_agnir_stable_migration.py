from __future__ import annotations

import re
import unittest
from pathlib import Path

from svif.continuity.agnir import AgnirFilesystemContinuityProvider


ROOT = Path(__file__).resolve().parents[1]
PROJECT = "urn:svif:project:svif-core"


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


if __name__ == "__main__":
    unittest.main()
