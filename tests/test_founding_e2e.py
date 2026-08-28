from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from svif.capabilities.cloudflare import CloudflareWorkersCapabilityProvider
from svif.continuity.agnir import AgnirFilesystemContinuityProvider
from svif.execution.chatgpt import ChatGPTExecutionSurface
from svif.runtime import OperationRequest, Orchestrator, ProjectBinding, ProviderBinding


PROJECT = "urn:test:svif-founding-e2e"
SUBJECT = "sha256:founding-verified-candidate"
TARGET = "cloudflare://workers/founding-e2e"
AUTHORITY = "protected-delivery"


def write_agnir_project(root: Path) -> None:
    (root / ".agnir/evidence").mkdir(parents=True)
    (root / ".agnir/state.md").write_text("# State\nready for founding E2E\n", encoding="utf-8")
    (root / ".agnir/next-actions.md").write_text("# Next\nrun founding E2E\n", encoding="utf-8")
    (root / ".agnir/decisions.md").write_text("# Decisions\nuse fake provider transport\n", encoding="utf-8")
    (root / "AGNIR.yaml").write_text(
        "agnir:\n"
        '  version: "0.1"\n'
        '  discovery_profile: "repository-filesystem/0.1"\n\n'
        "project:\n"
        f'  identity: "{PROJECT}"\n\n'
        "memory:\n"
        '  state: ".agnir/state.md"\n'
        '  next_actions: ".agnir/next-actions.md"\n'
        '  decisions: ".agnir/decisions.md"\n'
        '  evidence: ".agnir/evidence/"\n',
        encoding="utf-8",
    )


class FakeCloudflareTransport:
    def __init__(self) -> None:
        self.events: list[tuple[str, str, str]] = []
        self.deployed: set[tuple[str, str]] = set()

    def deploy_worker(self, *, subject_identity: str, target_identity: str) -> None:
        self.events.append(("deploy", subject_identity, target_identity))
        self.deployed.add((subject_identity, target_identity))

    def observe_worker(self, *, subject_identity: str, target_identity: str) -> bool:
        self.events.append(("observe", subject_identity, target_identity))
        return (subject_identity, target_identity) in self.deployed


class FoundingEndToEndTests(unittest.TestCase):
    def test_agnir_chatgpt_cloudflare_closes_the_full_product_loop(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_agnir_project(root)

            continuity = AgnirFilesystemContinuityProvider(root)
            chatgpt = ChatGPTExecutionSurface()
            transport = FakeCloudflareTransport()
            cloudflare = CloudflareWorkersCapabilityProvider(transport)
            orchestrator = Orchestrator(
                continuity_providers=(continuity,),
                execution_surfaces=(chatgpt,),
                capability_providers=(cloudflare,),
            )
            binding = ProjectBinding(
                project_identity=PROJECT,
                continuity=ProviderBinding("agnir"),
                execution_surface="chatgpt",
                capabilities=frozenset({"cloudflare.workers"}),
            )
            request = OperationRequest(
                operation_id="founding-e2e-1",
                intent="deploy the exact verified candidate and persist the observed result",
            )

            session = orchestrator.begin(binding, request)
            context = chatgpt.materialize(session)

            self.assertEqual(context["project_identity"], PROJECT)
            self.assertEqual(context["operation_id"], "founding-e2e-1")
            self.assertIn("ready for founding E2E", context["continuity"]["state"])
            self.assertEqual(context["bound_capabilities"], ["cloudflare.workers"])
            self.assertEqual(context["authority_grants"], [])

            work = chatgpt.parse_result(
                session,
                {
                    "project_identity": PROJECT,
                    "operation_id": "founding-e2e-1",
                    "subject_identity": SUBJECT,
                    "evidence": [
                        {
                            "kind": "verification",
                            "subject_identity": SUBJECT,
                            "status": "succeeded",
                            "producer": "founding-e2e-verifier",
                        }
                    ],
                    "capability_request": {
                        "provider": "cloudflare.workers",
                        "operation": "deploy_verified_worker",
                        "effect": "actuate",
                        "subject_identity": SUBJECT,
                        "target_identity": TARGET,
                        "authority_class": AUTHORITY,
                    },
                    "continuity_update": {
                        "state": "# State\nfounding E2E observed successfully\n",
                        "next_actions": "# Next\nharden ChatGPT app/MCP packaging\n",
                        "decisions": "# Decisions\nfounding product loop is executable with injected provider transport\n",
                    },
                },
            )

            outcome = orchestrator.complete(
                session,
                work,
                authority_grants=frozenset({AUTHORITY}),
            )

            self.assertTrue(outcome.externally_effectful)
            self.assertEqual(
                [record.kind for record in outcome.evidence],
                ["verification", "delivery", "observation"],
            )
            self.assertEqual({record.subject_identity for record in outcome.evidence}, {SUBJECT})
            self.assertEqual(
                transport.events,
                [
                    ("deploy", SUBJECT, TARGET),
                    ("observe", SUBJECT, TARGET),
                ],
            )

            resumed = continuity.load(PROJECT)
            self.assertIn("founding E2E observed successfully", resumed.state)
            self.assertIn("harden ChatGPT app/MCP packaging", resumed.next_actions)
            self.assertIn("founding product loop is executable", resumed.decisions)

            evidence_files = list((root / ".agnir/evidence").glob("svif-operation-*.json"))
            self.assertEqual(len(evidence_files), 1)
            checkpoint = json.loads(evidence_files[0].read_text(encoding="utf-8"))
            self.assertEqual(checkpoint["operation_id"], "founding-e2e-1")
            self.assertEqual(checkpoint["subject_identity"], SUBJECT)
            self.assertTrue(checkpoint["externally_effectful"])
            self.assertEqual(
                [record["kind"] for record in checkpoint["evidence"]],
                ["verification", "delivery", "observation"],
            )


if __name__ == "__main__":
    unittest.main()
