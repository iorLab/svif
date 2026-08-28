from __future__ import annotations

import unittest

from svif.runtime import (
    AuthorityRequired,
    CapabilityRequest,
    ContinuitySnapshot,
    EvidenceRecord,
    ObservationMismatch,
    OperationRequest,
    Orchestrator,
    ProjectBinding,
    ProviderBinding,
    ProvenanceMismatch,
    WorkResult,
)


PROJECT = "urn:test:svif-project"
SUBJECT = "sha256:verified-candidate"
TARGET = "cloudflare://worker/example"


class MemoryContinuity:
    provider_id = "agnir"

    def __init__(self, events: list[str]) -> None:
        self.events = events
        self.checkpoints = []

    def load(self, project_identity: str) -> ContinuitySnapshot:
        self.events.append("load")
        return ContinuitySnapshot(project_identity=project_identity, state={"phase": "ready"})

    def checkpoint(self, outcome) -> None:
        self.events.append("checkpoint")
        self.checkpoints.append(outcome)


class ScriptedSurface:
    surface_id = "chatgpt"

    def __init__(self, events: list[str], result: WorkResult) -> None:
        self.events = events
        self.result = result

    def execute(self, context, request) -> WorkResult:
        self.events.append("execute")
        self.last_context = context
        self.last_request = request
        return self.result


class ScriptedCapability:
    provider_id = "cloudflare.workers"

    def __init__(self, events: list[str], *, observation_subject: str = SUBJECT) -> None:
        self.events = events
        self.observation_subject = observation_subject
        self.actuation_count = 0

    def actuate(self, request: CapabilityRequest) -> EvidenceRecord:
        self.events.append("actuate")
        self.actuation_count += 1
        return EvidenceRecord(
            kind="delivery",
            subject_identity=request.subject_identity,
            target_identity=request.target_identity,
            producer=self.provider_id,
        )

    def observe(self, delivery: EvidenceRecord) -> EvidenceRecord:
        self.events.append("observe")
        return EvidenceRecord(
            kind="observation",
            subject_identity=self.observation_subject,
            target_identity=delivery.target_identity,
            producer=self.provider_id,
        )


def binding() -> ProjectBinding:
    return ProjectBinding(
        project_identity=PROJECT,
        continuity=ProviderBinding("agnir"),
        execution_surface="chatgpt",
        capabilities=frozenset({"cloudflare.workers"}),
    )


def verified_result(*, with_capability: bool) -> WorkResult:
    capability = None
    if with_capability:
        capability = CapabilityRequest(
            provider="cloudflare.workers",
            operation="deploy_verified_worker",
            effect="actuate",
            subject_identity=SUBJECT,
            target_identity=TARGET,
            authority_class="protected-delivery",
        )
    return WorkResult(
        subject_identity=SUBJECT,
        evidence=(EvidenceRecord(kind="verification", subject_identity=SUBJECT),),
        capability_request=capability,
    )


class OrchestratorTests(unittest.TestCase):
    def test_effectful_operation_closes_the_full_loop(self) -> None:
        events: list[str] = []
        continuity = MemoryContinuity(events)
        surface = ScriptedSurface(events, verified_result(with_capability=True))
        capability = ScriptedCapability(events)
        orchestrator = Orchestrator(
            continuity_providers=(continuity,),
            execution_surfaces=(surface,),
            capability_providers=(capability,),
        )

        outcome = orchestrator.run(
            binding(),
            OperationRequest(
                operation_id="op-1",
                intent="deploy the verified candidate",
                authority_grants=frozenset({"protected-delivery"}),
            ),
        )

        self.assertEqual(events, ["load", "execute", "actuate", "observe", "checkpoint"])
        self.assertEqual(
            [record.kind for record in outcome.evidence],
            ["verification", "delivery", "observation"],
        )
        self.assertEqual({record.subject_identity for record in outcome.evidence}, {SUBJECT})
        self.assertTrue(outcome.externally_effectful)
        self.assertEqual(len(continuity.checkpoints), 1)

    def test_non_effectful_operation_skips_delivery_and_observation(self) -> None:
        events: list[str] = []
        continuity = MemoryContinuity(events)
        surface = ScriptedSurface(events, verified_result(with_capability=False))
        orchestrator = Orchestrator(
            continuity_providers=(continuity,),
            execution_surfaces=(surface,),
        )

        outcome = orchestrator.run(
            binding(),
            OperationRequest(operation_id="op-2", intent="verify only"),
        )

        self.assertEqual(events, ["load", "execute", "checkpoint"])
        self.assertFalse(outcome.externally_effectful)
        self.assertEqual(len(continuity.checkpoints), 1)

    def test_unverified_subject_cannot_be_actuated_or_checkpointed(self) -> None:
        events: list[str] = []
        continuity = MemoryContinuity(events)
        result = WorkResult(
            subject_identity=SUBJECT,
            evidence=(),
            capability_request=verified_result(with_capability=True).capability_request,
        )
        surface = ScriptedSurface(events, result)
        capability = ScriptedCapability(events)
        orchestrator = Orchestrator(
            continuity_providers=(continuity,),
            execution_surfaces=(surface,),
            capability_providers=(capability,),
        )

        with self.assertRaises(ProvenanceMismatch):
            orchestrator.run(
                binding(),
                OperationRequest(
                    operation_id="op-3",
                    intent="deploy without verification",
                    authority_grants=frozenset({"protected-delivery"}),
                ),
            )

        self.assertEqual(events, ["load", "execute"])
        self.assertEqual(capability.actuation_count, 0)
        self.assertEqual(continuity.checkpoints, [])

    def test_missing_authority_blocks_actuation_and_checkpoint(self) -> None:
        events: list[str] = []
        continuity = MemoryContinuity(events)
        surface = ScriptedSurface(events, verified_result(with_capability=True))
        capability = ScriptedCapability(events)
        orchestrator = Orchestrator(
            continuity_providers=(continuity,),
            execution_surfaces=(surface,),
            capability_providers=(capability,),
        )

        with self.assertRaises(AuthorityRequired):
            orchestrator.run(
                binding(),
                OperationRequest(operation_id="op-4", intent="deploy without authority"),
            )

        self.assertEqual(events, ["load", "execute"])
        self.assertEqual(capability.actuation_count, 0)
        self.assertEqual(continuity.checkpoints, [])

    def test_observation_mismatch_prevents_checkpoint(self) -> None:
        events: list[str] = []
        continuity = MemoryContinuity(events)
        surface = ScriptedSurface(events, verified_result(with_capability=True))
        capability = ScriptedCapability(events, observation_subject="sha256:wrong-candidate")
        orchestrator = Orchestrator(
            continuity_providers=(continuity,),
            execution_surfaces=(surface,),
            capability_providers=(capability,),
        )

        with self.assertRaises(ObservationMismatch):
            orchestrator.run(
                binding(),
                OperationRequest(
                    operation_id="op-5",
                    intent="deploy but observe wrong subject",
                    authority_grants=frozenset({"protected-delivery"}),
                ),
            )

        self.assertEqual(events, ["load", "execute", "actuate", "observe"])
        self.assertEqual(continuity.checkpoints, [])


if __name__ == "__main__":
    unittest.main()
