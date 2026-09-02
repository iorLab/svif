from __future__ import annotations

import re
import unittest
from pathlib import Path

from svif.continuity.agnir import AgnirFilesystemContinuityProvider


ROOT = Path(__file__).resolve().parents[1]
PROJECT = "urn:svif:project:svif-core"


def _quoted_scalar(text: str, key: str) -> str:
    match = re.search(rf'^\s+{re.escape(key)}:\s+"([^"]+)"\s*$', text, re.MULTILINE)
    if match is None:
        raise AssertionError(f"missing quoted scalar {key!r}")
    return match.group(1)


class SelfHostedAgnirCore02Tests(unittest.TestCase):
    def test_real_svif_project_fresh_resolves_selected_core_0_2_lineage(self) -> None:
        svif = (ROOT / "SVIF.yaml").read_text(encoding="utf-8")
        expected_lineage = _quoted_scalar(svif, "lineage")
        expected_selector = _quoted_scalar(svif, "vcs_selector")

        provider = AgnirFilesystemContinuityProvider(
            ROOT,
            expected_core_version="0.2",
            expected_profile="repository-filesystem/0.2",
            selected_vcs_selector=expected_selector,
        )

        snapshot = provider.load(PROJECT)

        self.assertEqual(snapshot.project_identity, PROJECT)
        self.assertEqual(provider.resolve_lineage(PROJECT), expected_lineage)
        self.assertIn("Project orchestration product", snapshot.state)
        self.assertIn("Agnir Core 0.2", snapshot.next_actions)
        self.assertIn(expected_lineage, snapshot.next_actions)
        self.assertTrue(
            any("agnir-core-0.2" in name for name in snapshot.evidence),
            "fresh resume should recover inspectable Core 0.2 evidence",
        )


if __name__ == "__main__":
    unittest.main()
