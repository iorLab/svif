from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from svif.continuity.agnir import AgnirFilesystemContinuityProvider
from svif.execution.chatgpt import ChatGPTExecutionSurface
from svif.runtime import (
    BindingError,
    OperationRequest,
    Orchestrator,
    ProjectBinding,
    ProviderBinding,
)


PROJECT = "urn:test:chatgpt-surface"
SUBJECT = "sha256:chatgpt-result"


def write_project(root: Path) -> None:
    (root / ".agnir/evidence").mkdir(parents=True)
    (root / ".agnir/state.md").write_text("# State\nloaded by ChatGPT bridge\n", encoding="utf-8")
    (root / ".agnir/next-actions.md").write_text("# Next\ncontinue\n", encoding="utf-8")
    (root / ".agnir/decisions.md").write_text("# Decisions\nnone\n", encoding="utf-8")
    (root / "AGNIR.yaml").write_text(
        'agnir:\n  version: "0.1"\n  discovery_profile: "repository-filesystem/0.1"\n\n'
        f'project:\n  identity: "{PROJECT}"\n\n'
        'memory:\n  state: ".agnir/state.md"\n  next_actions: ".agnir/next-actions.md"\n'
        '  decisions: ".agnir/decisions.md"\n  evidence: ".agnir/evidence/"\n',
        encoding="utf-8",
    )


class ChatGPTExecutionSurfaceTests(unittest.TestCase):
    def test_two_phase_bridge_materializes_agnir_and_checkpoints_result(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_project(root)
            continuity = AgnirFilesystemContinuityProvider(root)
            chatgpt = ChatGPTExecutionSurface()
            orchestrator = Orchestrator(
                continuity_providers=(continuity,),
                execution_surfaces=(chatgpt,),
            )
            binding = ProjectBinding(
                project_identity=PROJECT,
                continuity=ProviderBinding("agnir"),
                execution_surface="chatgpt",
            )
            request = OperationRequest(operation_id="chatgpt-op-1", intent="continue project")

            session = orchestrator.begin(binding, request)
            envelope = chatgpt.materialize(session)

            self.assertEqual(envelope["project_identity"], PROJECT)
            self.assertEqual(envelope["operation_id"], "chatgpt-op-1")
            self.assertIn("loaded by ChatGPT bridge", envelope["continuity"]["state"])

            work = chatgpt.parse_result(
                session,
                {
                    "project_identity": PROJECT,
                    "operation_id": "chatgpt-op-1",
                    "subject_identity": SUBJECT,
                    "evidence": [
                        {
                            "kind": "verification",
                            "subject_identity": SUBJECT,
                            "status": "succeeded",
                            "producer": "chatgpt",
                        }
                    ],
                    "continuity_update": {
                        "state": "# State\nupdated through ChatGPT bridge\n",
                        "next_actions": "# Next\nimplement capability provider\n",
                    },
                },
            )
            outcome = orchestrator.complete(session, work)

            self.assertEqual(outcome.subject_identity, SUBJECT)
            self.assertIn(
                "updated through ChatGPT bridge",
                (root / ".agnir/state.md").read_text(encoding="utf-8"),
            )
            self.assertIn(
                "implement capability provider",
                (root / ".agnir/next-actions.md").read_text(encoding="utf-8"),
            )

    def test_chatgpt_result_cannot_cross_operation_identity(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_project(root)
            continuity = AgnirFilesystemContinuityProvider(root)
            chatgpt = ChatGPTExecutionSurface()
            orchestrator = Orchestrator(
                continuity_providers=(continuity,),
                execution_surfaces=(chatgpt,),
            )
            session = orchestrator.begin(
                ProjectBinding(PROJECT, ProviderBinding("agnir"), "chatgpt"),
                OperationRequest("chatgpt-op-2", "continue"),
            )

            with self.assertRaises(BindingError):
                chatgpt.parse_result(
                    session,
                    {
                        "project_identity": PROJECT,
                        "operation_id": "different-op",
                        "subject_identity": SUBJECT,
                    },
                )

    def test_chatgpt_bridge_is_not_fake_synchronous_execution(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_project(root)
            continuity = AgnirFilesystemContinuityProvider(root)
            chatgpt = ChatGPTExecutionSurface()
            orchestrator = Orchestrator(
                continuity_providers=(continuity,),
                execution_surfaces=(chatgpt,),
            )

            with self.assertRaises(BindingError):
                orchestrator.run(
                    ProjectBinding(PROJECT, ProviderBinding("agnir"), "chatgpt"),
                    OperationRequest("chatgpt-op-3", "continue"),
                )


if __name__ == "__main__":
    unittest.main()
