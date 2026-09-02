from __future__ import annotations

import unittest
from pathlib import Path

from svif.continuity.agnir import AgnirFilesystemContinuityProvider


ROOT = Path(__file__).resolve().parents[1]
PROJECT = "urn:svif:project:svif-core"
LINEAGE = "urn:svif:lineage:agnir-core-0.2-validation"
SELECTOR = "refs/heads/feature/agnir-core-0.2-validation"


class SelfHostedAgnirCore02Tests(unittest.TestCase):
    def test_real_svif_project_fresh_resolves_selected_core_0_2_lineage(self) -> None:
        provider = AgnirFilesystemContinuityProvider(
            ROOT,
            expected_core_version="0.2",
            expected_profile="repository-filesystem/0.2",
            selected_vcs_selector=SELECTOR,
        )

        snapshot = provider.load(PROJECT)

        self.assertEqual(snapshot.project_identity, PROJECT)
        self.assertEqual(provider.resolve_lineage(PROJECT), LINEAGE)
        self.assertIn("Project orchestration product", snapshot.state)
        self.assertIn("Active Agnir Core 0.2 real-consumer validation", snapshot.next_actions)
        self.assertIn("2026-09-02-agnir-core-0.2-real-consumer-validation.md", snapshot.evidence)


if __name__ == "__main__":
    unittest.main()
