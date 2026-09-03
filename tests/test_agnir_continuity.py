from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from svif.continuity.agnir import AgnirDiscoveryError, AgnirFilesystemContinuityProvider
from svif.runtime import (
    ContinuityUpdate,
    EvidenceRecord,
    OperationRequest,
    Orchestrator,
    ProjectBinding,
    ProviderBinding,
    WorkResult,
)


PROJECT = "urn:test:svif-project"
SUBJECT = "sha256:verified-candidate"


def write_project(
    root: Path,
    *,
    version: str = "0.1",
    profile: str | None = None,
    identity: str = PROJECT,
    state_locator: str = ".agnir/state.md",
    lineage: str | None = None,
    vcs_selector: str | None = None,
) -> None:
    if profile is None:
        profile = f"repository-filesystem/{version}" if version in {"0.1", "0.2"} else "repository-filesystem/0.1"
    (root / ".agnir/evidence").mkdir(parents=True)
    (root / ".agnir/state.md").write_text("# State\nold\n", encoding="utf-8")
    (root / ".agnir/next-actions.md").write_text("# Next\nold\n", encoding="utf-8")
    (root / ".agnir/decisions.md").write_text("# Decisions\nold\n", encoding="utf-8")
    (root / ".agnir/evidence/seed.md").write_text("# Seed\n", encoding="utf-8")

    continuity = ""
    if version == "0.2" or lineage is not None:
        continuity = (
            "\ncontinuity:\n"
            f'  lineage: "{lineage or "urn:test:lineage:default"}"\n'
        )

    extensions = ""
    if vcs_selector is not None:
        extensions = (
            "\nextensions:\n"
            "  agnir/vcs:\n"
            '    branch_continuity: "lineage-bound"\n'
            '    integration_reconciliation: "required"\n'
            "    lineage_binding:\n"
            '      kind: "vcs-ref"\n'
            f'      selector: "{vcs_selector}"\n'
        )

    (root / "AGNIR.yaml").write_text(
        "agnir:\n"
        f'  version: "{version}"\n'
        f'  discovery_profile: "{profile}"\n\n'
        "project:\n"
        f'  identity: "{identity}"\n'
        + continuity
        + "\nmemory:\n"
        f'  state: "{state_locator}"\n'
        '  next_actions: ".agnir/next-actions.md"\n'
        '  decisions: ".agnir/decisions.md"\n'
        '  evidence: ".agnir/evidence/"\n'
        + extensions,
        encoding="utf-8",
    )


class UpdatingSurface:
    surface_id = "chatgpt"

    def execute(self, context, request) -> WorkResult:
        self.loaded_state = context.continuity.state
        self.loaded_next_actions = context.continuity.next_actions
        return WorkResult(
            subject_identity=SUBJECT,
            evidence=(EvidenceRecord(kind="verification", subject_identity=SUBJECT),),
            continuity_update=ContinuityUpdate(
                state="# State\nnew durable truth\n",
                next_actions="# Next\ncontinue product integration\n",
            ),
        )


class AgnirFilesystemContinuityTests(unittest.TestCase):
    def test_loads_repository_filesystem_profile_0_1(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_project(root)
            provider = AgnirFilesystemContinuityProvider(root)

            snapshot = provider.load(PROJECT)

            self.assertEqual(snapshot.project_identity, PROJECT)
            self.assertIsNone(provider.resolve_lineage(PROJECT))
            self.assertIn("old", snapshot.state)
            self.assertIn("old", snapshot.next_actions)
            self.assertIn("old", snapshot.decisions)
            self.assertIn("seed.md", snapshot.evidence)

    def test_loads_repository_filesystem_profile_0_2_and_resolves_logical_lineage(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            selector = "refs/heads/feature/parallel"
            lineage = "urn:test:lineage:parallel"
            write_project(root, version="0.2", lineage=lineage, vcs_selector=selector)
            provider = AgnirFilesystemContinuityProvider(
                root,
                expected_core_version="0.2",
                expected_profile="repository-filesystem/0.2",
                selected_vcs_selector=selector,
            )

            snapshot = provider.load(PROJECT)

            self.assertEqual(snapshot.project_identity, PROJECT)
            self.assertEqual(provider.resolve_lineage(PROJECT), lineage)
            self.assertIn("old", snapshot.state)
            self.assertIn("seed.md", snapshot.evidence)

    def test_project_mismatch_preserves_agnir_failure_class(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_project(root, identity="urn:test:other-project")
            provider = AgnirFilesystemContinuityProvider(root)

            with self.assertRaises(AgnirDiscoveryError) as raised:
                provider.load(PROJECT)

            self.assertEqual(raised.exception.code, "AGNIR_DISCOVERY_PROJECT_MISMATCH")

    def test_unsupported_version_preserves_agnir_failure_class(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_project(root, version="9.9")
            provider = AgnirFilesystemContinuityProvider(root)

            with self.assertRaises(AgnirDiscoveryError) as raised:
                provider.load(PROJECT)

            self.assertEqual(raised.exception.code, "AGNIR_DISCOVERY_UNSUPPORTED_VERSION")

    def test_svif_binding_can_require_core_0_2(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_project(root, version="0.1")
            provider = AgnirFilesystemContinuityProvider(
                root,
                expected_core_version="0.2",
                expected_profile="repository-filesystem/0.2",
            )

            with self.assertRaises(AgnirDiscoveryError) as raised:
                provider.load(PROJECT)

            self.assertEqual(raised.exception.code, "AGNIR_DISCOVERY_UNSUPPORTED_VERSION")

    def test_core_0_2_requires_logical_lineage(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_project(root, version="0.2", lineage="urn:test:lineage:temporary")
            text = (root / "AGNIR.yaml").read_text(encoding="utf-8")
            text = text.replace('\ncontinuity:\n  lineage: "urn:test:lineage:temporary"\n', "")
            (root / "AGNIR.yaml").write_text(text, encoding="utf-8")
            provider = AgnirFilesystemContinuityProvider(root)

            with self.assertRaises(AgnirDiscoveryError) as raised:
                provider.load(PROJECT)

            self.assertEqual(raised.exception.code, "AGNIR_LINEAGE_REQUIRED")

    def test_selected_vcs_selector_must_match_durable_binding(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_project(
                root,
                version="0.2",
                lineage="urn:test:lineage:parallel",
                vcs_selector="refs/heads/feature/a",
            )
            provider = AgnirFilesystemContinuityProvider(
                root,
                selected_vcs_selector="refs/heads/feature/b",
            )

            with self.assertRaises(AgnirDiscoveryError) as raised:
                provider.load(PROJECT)

            self.assertEqual(raised.exception.code, "AGNIR_VCS_LINEAGE_BINDING_MISMATCH")

    def test_selected_vcs_selector_requires_durable_binding(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_project(root, version="0.2", lineage="urn:test:lineage:parallel")
            provider = AgnirFilesystemContinuityProvider(
                root,
                selected_vcs_selector="refs/heads/feature/a",
            )

            with self.assertRaises(AgnirDiscoveryError) as raised:
                provider.load(PROJECT)

            self.assertEqual(raised.exception.code, "AGNIR_VCS_LINEAGE_BINDING_REQUIRED")

    def test_locator_cannot_escape_project_root(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_project(root, state_locator="../outside.md")
            (root.parent / "outside.md").write_text("outside", encoding="utf-8")
            provider = AgnirFilesystemContinuityProvider(root)

            with self.assertRaises(AgnirDiscoveryError) as raised:
                provider.load(PROJECT)

            self.assertEqual(raised.exception.code, "AGNIR_DISCOVERY_UNRESOLVABLE")

    def test_orchestrator_checkpoints_explicit_update_through_agnir_0_1(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_project(root)
            provider = AgnirFilesystemContinuityProvider(root)
            surface = UpdatingSurface()
            orchestrator = Orchestrator(
                continuity_providers=(provider,),
                execution_surfaces=(surface,),
            )
            binding = ProjectBinding(
                project_identity=PROJECT,
                continuity=ProviderBinding("agnir"),
                execution_surface="chatgpt",
            )

            orchestrator.run(
                binding,
                OperationRequest(operation_id="op-agnir-1", intent="update durable truth"),
            )

            self.assertIn("old", surface.loaded_state)
            self.assertIn("old", surface.loaded_next_actions)
            self.assertEqual(
                (root / ".agnir/state.md").read_text(encoding="utf-8"),
                "# State\nnew durable truth\n",
            )
            evidence_files = list((root / ".agnir/evidence").glob("svif-operation-*.json"))
            self.assertEqual(len(evidence_files), 1)
            payload = json.loads(evidence_files[0].read_text(encoding="utf-8"))
            self.assertEqual(payload["operation_id"], "op-agnir-1")
            self.assertIsNone(payload["agnir_lineage"])

    def test_orchestrator_checkpoint_preserves_core_0_2_lineage_and_binding(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            selector = "refs/heads/feature/parallel"
            lineage = "urn:test:lineage:parallel"
            write_project(root, version="0.2", lineage=lineage, vcs_selector=selector)
            provider = AgnirFilesystemContinuityProvider(
                root,
                expected_core_version="0.2",
                expected_profile="repository-filesystem/0.2",
                selected_vcs_selector=selector,
            )
            surface = UpdatingSurface()
            orchestrator = Orchestrator(
                continuity_providers=(provider,),
                execution_surfaces=(surface,),
            )
            binding = ProjectBinding(
                project_identity=PROJECT,
                continuity=ProviderBinding("agnir"),
                execution_surface="chatgpt",
            )

            orchestrator.run(
                binding,
                OperationRequest(operation_id="op-agnir-lineage", intent="advance selected lineage"),
            )

            self.assertEqual(provider.resolve_lineage(PROJECT), lineage)
            evidence_files = list((root / ".agnir/evidence").glob("svif-operation-*.json"))
            self.assertEqual(len(evidence_files), 1)
            payload = json.loads(evidence_files[0].read_text(encoding="utf-8"))
            self.assertEqual(payload["agnir_lineage"], lineage)
            self.assertEqual(payload["operation_id"], "op-agnir-lineage")


if __name__ == "__main__":
    unittest.main()
