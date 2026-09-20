"""Executable acceptance of the four 2026-09-20 functional findings.

All transports are fake. Crash tests really terminate a child interpreter; they
are not native Codex, LLM-session, or production-delivery acceptance.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import unittest
from dataclasses import replace
from pathlib import Path
from unittest.mock import patch

from svif.capabilities.cloudflare import CloudflareWorkersCapabilityProvider
from svif.continuity.agnir import AgnirDiscoveryError, AgnirFilesystemContinuityProvider
from svif.continuity._filesystem import ProjectFiles
from svif.execution.chatgpt import ChatGPTExecutionSurface
from svif.runtime import (
    AuthorityRequired, BindingError, CapabilityPolicy, ContinuitySnapshot,
    ContinuityUpdate, EvidenceRecord, OperationOutcome, OperationRequest,
    Orchestrator, ProjectBinding, ProviderBinding, SessionConsumed, ObservationFailed,
    VerificationFailed, WorkResult,
)
from test_agnir_continuity import write_project, PROJECT

SUBJECT = "sha256:readiness-candidate"
TARGET = "fixture://worker"
VERSIONS = ("0.1", "0.2", "1.0")
ROOT = Path(__file__).resolve().parents[1]


class Memory:
    provider_id = "fixture"
    def __init__(self): self.saved = []
    def load(self, identity): return ContinuitySnapshot(identity)
    def checkpoint(self, outcome): self.saved.append(outcome)


class Transport:
    def __init__(self): self.calls = []
    def deploy_worker(self, **kwargs): self.calls.append("deploy")
    def observe_worker(self, **kwargs): self.calls.append("observe"); return True


def payload(operation="op", authority="omitted"):
    value = {
        "project_identity": PROJECT, "operation_id": operation,
        "subject_identity": SUBJECT,
        "evidence": [{"kind": "verification", "subject_identity": SUBJECT, "status": "succeeded"}],
        "capability_request": {"provider": "cloudflare.workers", "operation": "deploy_verified_worker",
                               "effect": "actuate", "subject_identity": SUBJECT, "target_identity": TARGET},
    }
    if authority != "omitted": value["capability_request"]["authority_class"] = authority
    return value


def setup_engine(memory=None):
    memory = memory or Memory()
    transport, surface = Transport(), ChatGPTExecutionSurface()
    engine = Orchestrator(continuity_providers=(memory,), execution_surfaces=(surface,),
                          capability_providers=(CloudflareWorkersCapabilityProvider(transport),))
    binding = ProjectBinding(PROJECT, ProviderBinding(memory.provider_id), "chatgpt", frozenset({"cloudflare.workers"}))
    return engine, binding, memory, transport, surface


def outcome(operation="update", expected_revision=None, decisions="new decision"):
    return OperationOutcome(PROJECT, operation, SUBJECT, (), False,
                            ContinuityUpdate("new state", "new next", decisions), expected_revision)


class RuntimeReadinessTests(unittest.TestCase):
    def test_missing_null_empty_and_weakened_authority_cannot_bypass_provider(self):
        for authority in ("omitted", None, "", "read", "none", "protected-delivery"):
            with self.subTest(authority=authority):
                engine, binding, memory, transport, surface = setup_engine()
                session = engine.begin(binding, OperationRequest("op", "test"))
                data = payload(authority=authority)
                data["authority_grants"] = ["protected-delivery"]  # never accepted from result
                with self.assertRaises(AuthorityRequired):
                    engine.complete(session, surface.parse_result(session, data))
                self.assertEqual(transport.calls, [])
                self.assertEqual(memory.saved, [])

    def test_trusted_grant_satisfies_provider_policy_with_omitted_class(self):
        engine, binding, memory, transport, surface = setup_engine()
        session = engine.begin(binding, OperationRequest("op", "test"))
        engine.complete(session, surface.parse_result(session, payload()), authority_grants=frozenset({"protected-delivery"}))
        self.assertEqual(transport.calls, ["deploy", "observe"])
        self.assertEqual(len(memory.saved), 1)

    def test_requested_additional_class_can_only_strengthen_policy(self):
        engine, binding, memory, transport, surface = setup_engine()
        session = engine.begin(binding, OperationRequest("op", "test"))
        with self.assertRaises(AuthorityRequired):
            engine.complete(session, surface.parse_result(session, payload(authority="principal-action")),
                            authority_grants=frozenset({"protected-delivery"}))
        self.assertEqual(transport.calls, [])

    def test_unknown_operation_and_absent_provider_policy_fail_closed(self):
        for absent in (False, True):
            with self.subTest(absent=absent):
                engine, binding, memory, transport, surface = setup_engine()
                if absent: engine._capabilities["cloudflare.workers"].operation_policy = None
                data = payload()
                if not absent: data["capability_request"]["operation"] = "unregistered"
                session = engine.begin(binding, OperationRequest("op", "test"))
                with self.assertRaises(BindingError):
                    engine.complete(session, surface.parse_result(session, data), authority_grants=frozenset({"protected-delivery"}))
                self.assertEqual(transport.calls, [])

    def test_provider_policy_matches_descriptor(self):
        descriptor = json.loads((ROOT / "integrations/cloudflare/adapter.json").read_text())
        operation = next(x for x in descriptor["operations"] if x["effect"] == "actuate")
        policy = CloudflareWorkersCapabilityProvider.operation_policy(operation["name"])
        self.assertEqual(policy, CapabilityPolicy(operation["name"], "actuate", frozenset({operation["authority"]})))

    def test_failed_blocked_unknown_or_missing_checks_prevent_completion(self):
        for status in ("failed", "blocked", "unknown", "missing", "foreign"):
            with self.subTest(status=status):
                engine, binding, memory, _, _ = setup_engine()
                evidence = () if status == "missing" else (EvidenceRecord("verification", "foreign" if status == "foreign" else SUBJECT,
                                                                           "succeeded" if status == "foreign" else status),)
                work = WorkResult(SUBJECT, evidence, continuity_update=ContinuityUpdate("complete", "none"))
                session = engine.begin(binding, OperationRequest("op", "test"))
                with self.assertRaises(VerificationFailed): engine.complete(session, work)
                self.assertEqual(memory.saved, [])

    def test_required_check_set_is_trusted_not_overridden_by_payload(self):
        engine, binding, memory, _, surface = setup_engine()
        session = engine.begin(binding, OperationRequest("op", "test", required_checks=frozenset({"unit", "integration"})))
        data = payload(); data.pop("capability_request")
        data["verification_required"] = False
        data["required_checks"] = []
        data["evidence"][0]["check_id"] = "unit"
        with self.assertRaises(VerificationFailed): engine.complete(session, surface.parse_result(session, data))
        self.assertEqual(memory.saved, [])
        session = engine.begin(binding, OperationRequest("op-2", "test", required_checks=frozenset({"unit", "integration"})))
        work = WorkResult(SUBJECT, tuple(EvidenceRecord("verification", SUBJECT, check_id=c) for c in ("unit", "integration")))
        engine.complete(session, work)
        self.assertEqual(len(memory.saved), 1)

    def test_no_check_exemption_is_explicit_and_does_not_override_failed_check(self):
        with self.assertRaises(BindingError): OperationRequest("op", "test", verification_required=False)
        for failed in (False, True):
            engine, binding, memory, _, _ = setup_engine()
            session = engine.begin(binding, OperationRequest("op", "inspection only", verification_required=False,
                                                           verification_not_applicable_reason="no artifact change"))
            work = WorkResult(SUBJECT, (EvidenceRecord("verification", SUBJECT, "failed"),) if failed else ())
            if failed:
                with self.assertRaises(VerificationFailed): engine.complete(session, work)
                self.assertEqual(memory.saved, [])
            else:
                engine.complete(session, work)
                self.assertEqual(len(memory.saved), 1)

    def test_sessions_are_single_use_and_cannot_be_forged(self):
        engine, binding, memory, transport, surface = setup_engine()
        session = engine.begin(binding, OperationRequest("op", "test"))
        work = surface.parse_result(session, payload())
        with self.assertRaises(SessionConsumed): engine.complete(replace(session), work)
        engine.complete(session, work, authority_grants=frozenset({"protected-delivery"}))
        with self.assertRaises(SessionConsumed): engine.complete(session, work, authority_grants=frozenset({"protected-delivery"}))
        self.assertEqual(transport.calls, ["deploy", "observe"])

    def test_conflicting_success_and_failure_is_not_verified(self):
        engine, binding, memory, _, _ = setup_engine()
        session = engine.begin(binding, OperationRequest("op", "test"))
        evidence = (EvidenceRecord("verification", SUBJECT), EvidenceRecord("verification", SUBJECT, "failed"))
        with self.assertRaises(VerificationFailed): engine.complete(session, WorkResult(SUBJECT, evidence))
        self.assertEqual(memory.saved, [])


class ContinuityReadinessTests(unittest.TestCase):
    def test_preflight_missing_decisions_never_writes_partial_state(self):
        for version in VERSIONS:
            with self.subTest(version=version), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary); write_project(root, version=version)
                anchor = root / "AGNIR.yaml"
                anchor.write_text(anchor.read_text().replace('decisions: ".agnir/decisions.md"', 'decisions: null'))
                provider = AgnirFilesystemContinuityProvider(root)
                before = provider.load(PROJECT)
                with self.assertRaises(AgnirDiscoveryError): provider.checkpoint(outcome())
                self.assertEqual(provider.load(PROJECT), before)
                self.assertFalse((root / ProjectFiles.JOURNAL).exists())

    def test_each_write_failure_rolls_back_the_whole_checkpoint(self):
        for version in VERSIONS:
            for failure_at in range(2, 7):  # state, next, decisions, receipt, commit decision
                with self.subTest(version=version, failure_at=failure_at), tempfile.TemporaryDirectory() as temporary:
                    root = Path(temporary); write_project(root, version=version)
                    provider = AgnirFilesystemContinuityProvider(root); before = provider.load(PROJECT)
                    original = provider._files.write
                    calls = 0
                    def failing(path, content):
                        nonlocal calls
                        calls += 1
                        if calls == failure_at: raise OSError("injected write failure")
                        return original(path, content)
                    with patch.object(provider._files, "write", failing):
                        with self.assertRaises(AgnirDiscoveryError): provider.checkpoint(outcome())
                    self.assertEqual(AgnirFilesystemContinuityProvider(root).load(PROJECT), before)
                    self.assertFalse((root / ProjectFiles.JOURNAL).exists())

    def test_actual_process_death_recovers_old_or_committed_snapshot(self):
        script = '''
import os, sys
from pathlib import Path
from svif.continuity.agnir import AgnirFilesystemContinuityProvider
from svif.runtime import OperationOutcome, ContinuityUpdate
p=AgnirFilesystemContinuityProvider(Path(sys.argv[1]))
write=p._files.write
count=0
limit=int(sys.argv[2])
def crash(path, content):
    global count
    write(path, content)
    count+=1
    if count==limit: os._exit(73)
p._files.write=crash
p.checkpoint(OperationOutcome(sys.argv[3], "crash", "sha256:readiness-candidate", (), False, ContinuityUpdate("new state", "new next", "new decision")))
'''
        for version in VERSIONS:
            for crash_after in (1, 2, 3, 4, 5, 6):
                with self.subTest(version=version, crash_after=crash_after), tempfile.TemporaryDirectory() as temporary:
                    root = Path(temporary); write_project(root, version=version)
                    before = AgnirFilesystemContinuityProvider(root).load(PROJECT)
                    env = {**os.environ, "PYTHONPATH": str(ROOT / "src")}
                    result = subprocess.run([sys.executable, "-c", script, str(root), str(crash_after), PROJECT], env=env, capture_output=True, timeout=15)
                    self.assertEqual(result.returncode, 73, result.stderr)
                    after = AgnirFilesystemContinuityProvider(root).load(PROJECT)
                    if crash_after < 6:
                        self.assertEqual(after, before)
                    else:
                        self.assertEqual((after.state, after.next_actions, after.decisions), ("new state", "new next", "new decision"))
                        self.assertEqual(len(after.evidence), 2)
                    self.assertFalse((root / ProjectFiles.JOURNAL).exists())

    def test_child_symlink_anchor_symlink_and_write_symlink_are_rejected(self):
        for version in VERSIONS:
            for surface in ("evidence", "anchor", "lock", "receipt"):
                with self.subTest(version=version, surface=surface), tempfile.TemporaryDirectory() as temporary:
                    base = Path(temporary); root=base / "project"; root.mkdir(); write_project(root, version=version)
                    outside = base / "dummy.txt"; outside.write_text("DUMMY OUTSIDE")
                    provider = AgnirFilesystemContinuityProvider(root)
                    if surface == "evidence": target = root / ".agnir/evidence/escape.md"
                    elif surface == "anchor": target = root / "AGNIR.yaml"; target.unlink()
                    elif surface == "lock": target = root / ProjectFiles.LOCK
                    else:
                        resolved = provider._discover(PROJECT)
                        target = provider._evidence_path(resolved, PROJECT, "update")
                    target.symlink_to(outside)
                    with self.assertRaises(AgnirDiscoveryError):
                        if surface == "receipt": provider.checkpoint(outcome())
                        else: provider.load(PROJECT)
                    self.assertEqual(outside.read_text(), "DUMMY OUTSIDE")

    def test_predictable_legacy_temp_symlink_is_not_followed(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary) / "project"; root.mkdir(); write_project(root)
            outside = root.parent / "dummy"; outside.write_text("DUMMY")
            (root / ".agnir/.state.md.svif-tmp").symlink_to(outside)
            AgnirFilesystemContinuityProvider(root).checkpoint(outcome())
            self.assertEqual(outside.read_text(), "DUMMY")

    def test_stale_snapshot_is_rejected_and_newer_state_preserved(self):
        for version in VERSIONS:
            with self.subTest(version=version), tempfile.TemporaryDirectory() as temporary:
                root=Path(temporary); write_project(root, version=version)
                provider=AgnirFilesystemContinuityProvider(root)
                before=provider.load(PROJECT)
                provider.checkpoint(outcome("first", before.revision))
                current=provider.load(PROJECT)
                with self.assertRaises(AgnirDiscoveryError) as raised:
                    provider.checkpoint(outcome("stale", before.revision))
                self.assertEqual(raised.exception.code, "AGNIR_CHECKPOINT_STALE")
                self.assertEqual(provider.load(PROJECT), current)

    def test_stale_context_blocks_external_effect_before_transport(self):
        with tempfile.TemporaryDirectory() as temporary:
            root=Path(temporary); write_project(root, version="1.0")
            provider=AgnirFilesystemContinuityProvider(root)
            engine, binding, _, transport, surface=setup_engine(provider)
            session=engine.begin(binding, OperationRequest("op", "test"))
            provider.checkpoint(outcome("other"))
            with self.assertRaises(AgnirDiscoveryError):
                engine.complete(session, surface.parse_result(session, payload()), authority_grants=frozenset({"protected-delivery"}))
            self.assertEqual(transport.calls, [])

    def test_cross_process_reader_is_busy_not_mixed(self):
        script='''
from svif.continuity.agnir import AgnirFilesystemContinuityProvider, AgnirDiscoveryError
import sys
try: AgnirFilesystemContinuityProvider(sys.argv[1]).load(sys.argv[2])
except AgnirDiscoveryError as e:
    print(e.code); sys.exit(0 if e.code=="AGNIR_CHECKPOINT_BUSY" else 2)
sys.exit(3)
'''
        with tempfile.TemporaryDirectory() as temporary:
            root=Path(temporary); write_project(root)
            provider=AgnirFilesystemContinuityProvider(root)
            with provider._locked():
                result=subprocess.run([sys.executable, "-c", script, str(root), PROJECT], env={**os.environ,"PYTHONPATH":str(ROOT/"src")}, capture_output=True, text=True, timeout=15)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertIn("AGNIR_CHECKPOINT_BUSY", result.stdout)
            self.assertIsNotNone(AgnirFilesystemContinuityProvider(root).load(PROJECT))

    def test_recovery_does_not_overwrite_conflicting_external_edits(self):
        with tempfile.TemporaryDirectory() as temporary:
            root=Path(temporary); write_project(root)
            provider=AgnirFilesystemContinuityProvider(root)
            original=provider._files.write; count=0
            def interrupt(path, content):
                nonlocal count
                original(path, content); count+=1
                if count==2: raise KeyboardInterrupt()
            with patch.object(provider._files, "write", interrupt):
                with self.assertRaises(KeyboardInterrupt): provider.checkpoint(outcome())
            (root/".agnir/state.md").write_text("external concurrent edit")
            with self.assertRaises(AgnirDiscoveryError) as raised: provider.load(PROJECT)
            self.assertEqual(raised.exception.code, "AGNIR_CHECKPOINT_RECOVERY_REQUIRED")
            self.assertEqual((root/".agnir/state.md").read_text(), "external concurrent edit")
            self.assertTrue((root/ProjectFiles.JOURNAL).exists())

    def test_duplicate_operation_receipt_is_not_overwritten(self):
        with tempfile.TemporaryDirectory() as temporary:
            root=Path(temporary); write_project(root)
            provider=AgnirFilesystemContinuityProvider(root); provider.checkpoint(outcome())
            before=provider.load(PROJECT)
            with self.assertRaises(AgnirDiscoveryError) as raised: provider.checkpoint(outcome())
            self.assertEqual(raised.exception.code, "AGNIR_CHECKPOINT_DUPLICATE_OPERATION")
            self.assertEqual(provider.load(PROJECT), before)

    def test_uncertain_effect_survives_restart_and_requires_authorized_reconciliation(self):
        with tempfile.TemporaryDirectory() as temporary:
            root=Path(temporary); write_project(root, version="1.0")
            provider=AgnirFilesystemContinuityProvider(root)
            engine, binding, _, transport, surface=setup_engine(provider)
            def unavailable(**kwargs): raise OSError("observation unavailable")
            transport.observe_worker=unavailable
            session=engine.begin(binding, OperationRequest("op", "test"))
            with self.assertRaises(ObservationFailed):
                engine.complete(session, surface.parse_result(session, payload()), authority_grants=frozenset({"protected-delivery"}))
            self.assertEqual(transport.calls, ["deploy"])
            restarted=AgnirFilesystemContinuityProvider(root)
            snapshot=restarted.load(PROJECT)
            self.assertIsNotNone(snapshot.pending_effect)
            engine2, binding2, _, transport2, surface2=setup_engine(restarted)
            session2=engine2.begin(binding2, OperationRequest("op", "retry"))
            with self.assertRaises(AgnirDiscoveryError) as raised:
                engine2.complete(session2, surface2.parse_result(session2, payload()), authority_grants=frozenset({"protected-delivery"}))
            self.assertEqual(raised.exception.code, "AGNIR_EXTERNAL_EFFECT_UNCONFIRMED")
            self.assertEqual(transport2.calls, [])
            recovered=OperationOutcome(PROJECT, "op", SUBJECT,
                (EvidenceRecord("observation", SUBJECT, target_identity=TARGET),), True,
                ContinuityUpdate("independently observed", "continue"), snapshot.revision, TARGET)
            with self.assertRaises(AuthorityRequired): restarted.reconcile_effect(recovered, authority_grants=frozenset())
            with self.assertRaises(BindingError):
                restarted.reconcile_effect(replace(recovered, target_identity="wrong"), authority_grants=frozenset({"effect-reconciliation"}))
            restarted.reconcile_effect(recovered, authority_grants=frozenset({"effect-reconciliation"}))
            self.assertIsNone(restarted.load(PROJECT).pending_effect)
            self.assertEqual(restarted.load(PROJECT).state, "independently observed")
            self.assertEqual(transport2.calls, [])

    def test_duplicate_discovery_keys_and_locator_aliases_fail(self):
        for change in ("duplicate", "alias", "discovery"):
            with self.subTest(change=change), tempfile.TemporaryDirectory() as temporary:
                root=Path(temporary); write_project(root)
                anchor=root/"AGNIR.yaml"; text=anchor.read_text()
                if change=="duplicate": text += '\nproject:\n  identity: "other"\n'
                elif change=="alias": text=text.replace('next_actions: ".agnir/next-actions.md"','next_actions: ".agnir/state.md"')
                else: text=text.replace('state: ".agnir/state.md"','state: "AGNIR.yaml"')
                anchor.write_text(text)
                with self.assertRaises(AgnirDiscoveryError): AgnirFilesystemContinuityProvider(root).load(PROJECT)


if __name__ == "__main__": unittest.main()
