from __future__ import annotations

from dataclasses import replace
import json
import tempfile
import unittest
from pathlib import Path

from svif.capabilities.cloudflare import CloudflareWorkersCapabilityProvider
from svif.continuity.agnir import AgnirDiscoveryError, AgnirFilesystemContinuityProvider
from svif.execution.chatgpt import ChatGPTExecutionSurface
from svif.runtime import (
    AuthorityRequired, BindingError, ContinuitySnapshot, ContinuityUpdate,
    EvidenceRecord, OperationRequest, Orchestrator, ProjectBinding, ProviderBinding,
    SessionError, VerificationFailed, WorkResult,
)
from test_agnir_continuity import write_project, PROJECT, SUBJECT

TARGET = "urn:test:non-production-worker"


class Memory:
    provider_id = "memory"
    def __init__(self):
        self.saved = []
    def load(self, project_identity):
        return ContinuitySnapshot(project_identity)
    def checkpoint(self, outcome):
        self.saved.append(outcome)


class Transport:
    def __init__(self, observed=True):
        self.calls = []
        self.observed = observed
    def deploy_worker(self, **kwargs):
        self.calls.append(("deploy", kwargs))
    def observe_worker(self, **kwargs):
        self.calls.append(("observe", kwargs))
        return self.observed


def rig(*, memory=None, required=True, verifiers=frozenset()):
    memory = Memory() if memory is None else memory
    surface = ChatGPTExecutionSurface()
    transport = Transport()
    capability = CloudflareWorkersCapabilityProvider(transport)
    runtime = Orchestrator(continuity_providers=(memory,), execution_surfaces=(surface,),
                           capability_providers=(capability,))
    binding = ProjectBinding(PROJECT, ProviderBinding(memory.provider_id), surface.surface_id,
                             frozenset({capability.provider_id}))
    session = runtime.begin(binding, OperationRequest("safety-op", "verify and checkpoint fixture",
                              verification_required=required, required_verifiers=verifiers))
    payload = {"project_identity": PROJECT, "operation_id": "safety-op", "subject_identity": SUBJECT,
               "evidence": [{"kind": "verification", "subject_identity": SUBJECT, "status": "succeeded"}],
               "continuity_update": {"state": "new state\n", "next_actions": "new next\n"},
               "capability_request": {"provider": capability.provider_id, "operation": "deploy_verified_worker",
                                      "effect": "actuate", "subject_identity": SUBJECT, "target_identity": TARGET}}
    return runtime, session, surface, transport, memory, payload


def attestation(producer="trusted-fixture-verifier", status="succeeded", subject=SUBJECT):
    return (EvidenceRecord("verification", subject, status=status, producer=producer),)


class ReleaseSafetyTests(unittest.TestCase):
    def test_authority_omission_null_empty_and_downgrade_cannot_bypass_provider_policy(self):
        for value in ("ABSENT", None, "", "read", "none", "verification"):
            with self.subTest(authority=value):
                rt, session, surface, transport, memory, payload = rig()
                if value != "ABSENT":
                    payload["capability_request"]["authority_class"] = value
                payload["authority_grants"] = ["protected-delivery"]
                with self.assertRaises(AuthorityRequired):
                    rt.complete(session, surface.parse_result(session, payload), verification_evidence=attestation())
                self.assertEqual(transport.calls, [])
                self.assertEqual(memory.saved, [])

    def test_trusted_authority_allows_omitted_advisory_class(self):
        rt, session, surface, transport, memory, payload = rig()
        result = rt.complete(session, surface.parse_result(session, payload), verification_evidence=attestation(),
                             authority_grants=frozenset({"protected-delivery"}))
        self.assertTrue(result.externally_effectful)
        self.assertEqual([v[0] for v in transport.calls], ["deploy", "observe"])
        self.assertEqual(len(memory.saved), 1)

    def test_model_verification_success_is_not_its_own_attestation(self):
        rt, session, surface, transport, memory, payload = rig()
        with self.assertRaises(VerificationFailed):
            rt.complete(session, surface.parse_result(session, payload), authority_grants=frozenset({"protected-delivery"}))
        self.assertEqual(transport.calls, [])
        self.assertEqual(memory.saved, [])

    def test_required_non_effectful_verification_blocks_missing_wrong_failed_unknown(self):
        for receipt in ((), attestation(subject="sha256:other"), attestation(status="failed"),
                        attestation(status="unknown"), attestation(status="blocked")):
            with self.subTest(receipt=receipt):
                rt, session, surface, transport, memory, payload = rig()
                del payload["capability_request"]
                with self.assertRaises(VerificationFailed):
                    rt.complete(session, surface.parse_result(session, payload), verification_evidence=receipt)
                self.assertFalse(memory.saved)

    def test_failed_declared_verification_never_checkpoints_completion_even_when_not_required(self):
        for required in (True, False):
            rt, session, surface, transport, memory, payload = rig(required=required)
            del payload["capability_request"]
            payload["evidence"][0]["status"] = "failed"
            with self.assertRaises(VerificationFailed):
                rt.complete(session, surface.parse_result(session, payload), verification_evidence=attestation())
            self.assertFalse(memory.saved)

    def test_trusted_non_applicable_case_does_not_require_invented_verification(self):
        rt, session, surface, transport, memory, payload = rig(required=False)
        del payload["capability_request"]
        payload["evidence"] = []
        result = rt.complete(session, surface.parse_result(session, payload))
        self.assertFalse(result.externally_effectful)
        self.assertEqual(transport.calls, [])
        self.assertEqual(len(memory.saved), 1)

    def test_result_cannot_disable_trusted_verification_requirement(self):
        rt, session, surface, transport, memory, payload = rig()
        del payload["capability_request"]
        payload["verification_required"] = False
        payload["verification_needs_attestation"] = False
        with self.assertRaises(VerificationFailed):
            rt.complete(session, surface.parse_result(session, payload))
        self.assertFalse(memory.saved)

    def test_every_required_verifier_must_succeed(self):
        rt, session, surface, transport, memory, payload = rig(verifiers=frozenset({"lint", "unit"}))
        del payload["capability_request"]
        with self.assertRaises(VerificationFailed):
            rt.complete(session, surface.parse_result(session, payload), verification_evidence=attestation("lint"))
        rt.complete(session, surface.parse_result(session, payload),
                    verification_evidence=attestation("lint") + attestation("unit"))
        self.assertEqual(len(memory.saved), 1)

    def test_model_cannot_forge_delivery_observation_or_checkpoint_receipts(self):
        for kind in ("delivery", "observation", "checkpoint"):
            rt, session, surface, transport, memory, payload = rig()
            payload["evidence"][0]["kind"] = kind
            with self.assertRaises(BindingError):
                surface.parse_result(session, payload)
            self.assertFalse(transport.calls)

    def test_unknown_operation_fails_before_transport(self):
        rt, session, surface, transport, memory, payload = rig()
        payload["capability_request"]["operation"] = "delete_everything"
        with self.assertRaises(BindingError):
            rt.complete(session, surface.parse_result(session, payload), verification_evidence=attestation(),
                        authority_grants=frozenset({"protected-delivery"}))
        self.assertFalse(transport.calls)

    def test_completed_session_cannot_replay_or_be_forged(self):
        rt, session, surface, transport, memory, payload = rig()
        work = surface.parse_result(session, payload)
        with self.assertRaises(SessionError):
            rt.complete(replace(session), work, verification_evidence=attestation())
        rt.complete(session, work, verification_evidence=attestation(), authority_grants=frozenset({"protected-delivery"}))
        with self.assertRaises(SessionError):
            rt.complete(session, work, verification_evidence=attestation(), authority_grants=frozenset({"protected-delivery"}))
        self.assertEqual(len(transport.calls), 2)

    def test_failed_observation_is_uncertain_and_cannot_blindly_replay(self):
        rt, session, surface, transport, memory, payload = rig()
        transport.observed = False
        work = surface.parse_result(session, payload)
        from svif.runtime import ObservationMismatch
        with self.assertRaises(ObservationMismatch):
            rt.complete(session, work, verification_evidence=attestation(), authority_grants=frozenset({"protected-delivery"}))
        with self.assertRaises(SessionError):
            rt.complete(session, work, verification_evidence=attestation(), authority_grants=frozenset({"protected-delivery"}))
        self.assertFalse(memory.saved)
        self.assertEqual(len(transport.calls), 2)

    def test_stale_snapshot_is_rejected_before_external_effect(self):
        for version in ("0.1", "0.2", "1.0"):
            with self.subTest(version=version), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                write_project(root, version=version)
                memory = AgnirFilesystemContinuityProvider(root)
                rt, session, surface, transport, _, payload = rig(memory=memory)
                (root / ".agnir/state.md").write_text("newer concurrent truth\n")
                with self.assertRaises(AgnirDiscoveryError) as raised:
                    rt.complete(session, surface.parse_result(session, payload), verification_evidence=attestation(),
                                authority_grants=frozenset({"protected-delivery"}))
                self.assertEqual(raised.exception.code, "AGNIR_DISCOVERY_STALE")
                self.assertFalse(transport.calls)

    def test_invalid_checkpoint_is_rejected_before_external_effect(self):
        for version in ("0.1", "0.2", "1.0"):
            with self.subTest(version=version), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                write_project(root, version=version)
                anchor = root / "AGNIR.yaml"
                anchor.write_text(anchor.read_text().replace('decisions: ".agnir/decisions.md"', 'decisions: null'))
                memory = AgnirFilesystemContinuityProvider(root)
                rt, session, surface, transport, _, payload = rig(memory=memory)
                payload["continuity_update"]["decisions"] = "cannot be stored"
                with self.assertRaises(AgnirDiscoveryError):
                    rt.complete(session, surface.parse_result(session, payload), verification_evidence=attestation(),
                                authority_grants=frozenset({"protected-delivery"}))
                self.assertFalse(transport.calls)
                self.assertIn("old", (root / ".agnir/state.md").read_text())

    def test_provider_policy_matches_registered_descriptor(self):
        root = Path(__file__).resolve().parents[1]
        descriptor = json.loads((root / "integrations/cloudflare/adapter.json").read_text())
        operation = next(op for op in descriptor["operations"] if op["name"] == "deploy_verified_worker")
        policy = CloudflareWorkersCapabilityProvider(Transport()).policy_for(operation["name"])
        self.assertEqual(policy.effect, operation["effect"])
        self.assertEqual(policy.required_authorities, frozenset({operation["authority"]}))

    def test_uncertain_effect_survives_restart_and_only_observation_can_resolve_it(self):
        from svif.runtime import ObservationMismatch
        for version in ("0.1", "0.2", "1.0"):
            with self.subTest(version=version), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                write_project(root, version=version)
                memory = AgnirFilesystemContinuityProvider(root)
                rt, session, surface, transport, _, payload = rig(memory=memory)
                transport.observed = False
                with self.assertRaises(ObservationMismatch):
                    rt.complete(session, surface.parse_result(session, payload), verification_evidence=attestation(),
                                authority_grants=frozenset({"protected-delivery"}))
                fresh = AgnirFilesystemContinuityProvider(root)
                with self.assertRaises(AgnirDiscoveryError) as error:
                    fresh.load(PROJECT)
                self.assertEqual(error.exception.code, "AGNIR_EFFECT_RECONCILIATION_REQUIRED")
                pending = fresh.pending_effect(PROJECT)
                self.assertEqual(pending["subject_identity"], SUBJECT)
                self.assertEqual(pending["target_identity"], TARGET)
                delivery = EvidenceRecord("delivery", SUBJECT, target_identity=TARGET, producer="cloudflare.workers")
                wrong = EvidenceRecord("observation", "wrong", target_identity=TARGET, producer="cloudflare.workers")
                with self.assertRaises(AgnirDiscoveryError):
                    fresh.reconcile_effect(PROJECT, delivery=delivery, observation=wrong)
                # Trusted independent transport read, not another actuation.
                transport.observed = True
                observed = CloudflareWorkersCapabilityProvider(transport).observe(delivery)
                fresh.reconcile_effect(PROJECT, delivery=delivery, observation=observed)
                self.assertEqual(fresh.load(PROJECT).state, "new state\n")
                self.assertIsNone(fresh.pending_effect(PROJECT))
                self.assertEqual(sum(call[0] == "deploy" for call in transport.calls), 1)

    def test_completed_durable_operation_cannot_redeploy_after_restart(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_project(root)
            memory = AgnirFilesystemContinuityProvider(root)
            rt, session, surface, transport, _, payload = rig(memory=memory)
            rt.complete(session, surface.parse_result(session, payload), verification_evidence=attestation(),
                        authority_grants=frozenset({"protected-delivery"}))
            second, new_session, new_surface, new_transport, _, new_payload = rig(memory=AgnirFilesystemContinuityProvider(root))
            with self.assertRaises(AgnirDiscoveryError) as error:
                second.complete(new_session, new_surface.parse_result(new_session, new_payload),
                                verification_evidence=attestation(), authority_grants=frozenset({"protected-delivery"}))
            self.assertEqual(error.exception.code, "AGNIR_OPERATION_REPLAY")
            self.assertFalse(new_transport.calls)


if __name__ == "__main__":
    unittest.main()
