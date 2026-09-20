from __future__ import annotations

import base64
import hashlib
import json
import os
import subprocess
import sys
import tempfile
import threading
import unittest
from pathlib import Path
from unittest.mock import patch

from svif.continuity.agnir import AgnirDiscoveryError, AgnirFilesystemContinuityProvider
from svif.runtime import ContinuityUpdate, OperationOutcome
from test_agnir_continuity import write_project, PROJECT, SUBJECT

VERSIONS = ("0.1", "0.2", "1.0")
ROOT = Path(__file__).resolve().parents[1]


def outcome(operation="transaction", *, decisions="new decisions\n"):
    return OperationOutcome(PROJECT, operation, SUBJECT, (), False,
                            ContinuityUpdate("new state\n", "new next\n", decisions))


def memory_files(root):
    return {p.relative_to(root).as_posix(): p.read_bytes() for p in (root / ".agnir").rglob("*") if p.is_file()}


class Crash(BaseException):
    """Simulates termination without ordinary exception rollback."""


def interrupted(root, number, exception=Crash):
    provider = AgnirFilesystemContinuityProvider(root)
    publish = provider._publish_file
    calls = 0
    def injected(path, content):
        nonlocal calls
        calls += 1
        publish(path, content)
        if calls == number:
            raise exception("injected after write")
    with patch.object(provider, "_publish_file", side_effect=injected):
        provider.checkpoint(outcome())


class AgnirTransactionTests(unittest.TestCase):
    def test_all_updates_are_preflighted_before_any_mutation(self):
        for version in VERSIONS:
            for decision in ("requested but no locator", 42):
                with self.subTest(version=version, decision=decision), tempfile.TemporaryDirectory() as directory:
                    root = Path(directory)
                    write_project(root, version=version)
                    anchor = root / "AGNIR.yaml"
                    anchor.write_text(anchor.read_text().replace('decisions: ".agnir/decisions.md"', 'decisions: null'))
                    before = memory_files(root)
                    with self.assertRaises(Exception):
                        AgnirFilesystemContinuityProvider(root).checkpoint(outcome(decisions=decision))
                    self.assertEqual(memory_files(root), before)
                    self.assertFalse((root / ".svif-runtime/agnir-pending.json").exists())

    def test_normal_io_failure_restores_all_preimages_at_every_write_boundary(self):
        for version in VERSIONS:
            for split in range(1, 5):
                with self.subTest(version=version, split=split), tempfile.TemporaryDirectory() as directory:
                    root = Path(directory)
                    write_project(root, version=version)
                    before = memory_files(root)
                    with self.assertRaises(AgnirDiscoveryError) as error:
                        interrupted(root, split, OSError)
                    self.assertEqual(error.exception.code, "AGNIR_CHECKPOINT_FAILED")
                    self.assertEqual(memory_files(root), before)
                    self.assertFalse((root / ".svif-runtime/agnir-pending.json").exists())

    def test_interruption_rolls_forward_coherently_at_every_write_boundary(self):
        for version in VERSIONS:
            for split in range(1, 5):
                with self.subTest(version=version, split=split), tempfile.TemporaryDirectory() as directory:
                    root = Path(directory)
                    write_project(root, version=version)
                    anchor = (root / "AGNIR.yaml").read_bytes()
                    with self.assertRaises(Crash):
                        interrupted(root, split)
                    self.assertTrue((root / ".svif-runtime/agnir-pending.json").exists())
                    recovered = AgnirFilesystemContinuityProvider(root).load(PROJECT)
                    self.assertEqual((recovered.state, recovered.next_actions, recovered.decisions),
                                     ("new state\n", "new next\n", "new decisions\n"))
                    self.assertEqual((root / "AGNIR.yaml").read_bytes(), anchor)
                    self.assertEqual(len(list((root / ".agnir/evidence").glob("svif-operation-*.json"))), 1)
                    self.assertFalse((root / ".svif-runtime/agnir-pending.json").exists())

    def test_real_process_death_recovers_in_another_process(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_project(root, version="1.0")
            env = {**os.environ, "PYTHONPATH": str(ROOT / "src")}
            code = '''import os,sys
from svif.continuity.agnir import AgnirFilesystemContinuityProvider
from svif.runtime import ContinuityUpdate,OperationOutcome
p=AgnirFilesystemContinuityProvider(sys.argv[1])
f=p._publish_file
count=0
def stop(path,content):
 global count
 f(path,content); count+=1
 if count==2: os._exit(71)
p._publish_file=stop
p.checkpoint(OperationOutcome(sys.argv[2],"process-death","sha256:fixture",(),False,ContinuityUpdate("new state\\n","new next\\n","new decisions\\n")))
'''
            process = subprocess.run([sys.executable, "-c", code, str(root), PROJECT], env=env, capture_output=True, timeout=10)
            self.assertEqual(process.returncode, 71, process.stderr)
            recover = '''import sys,json
from dataclasses import asdict
from svif.continuity.agnir import AgnirFilesystemContinuityProvider
print(json.dumps(asdict(AgnirFilesystemContinuityProvider(sys.argv[1]).load(sys.argv[2]))))
'''
            process = subprocess.run([sys.executable, "-c", recover, str(root), PROJECT], env=env, capture_output=True, timeout=10)
            self.assertEqual(process.returncode, 0, process.stderr)
            snapshot = json.loads(process.stdout)
            self.assertEqual(snapshot["state"], "new state\n")
            self.assertEqual(snapshot["next_actions"], "new next\n")
            self.assertEqual(snapshot["decisions"], "new decisions\n")

    def test_recovery_refuses_to_overwrite_unrelated_post_crash_edit(self):
        for version in VERSIONS:
            with self.subTest(version=version), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                write_project(root, version=version)
                with self.assertRaises(Crash):
                    interrupted(root, 1)
                (root / ".agnir/next-actions.md").write_text("independent newer edit\n")
                before = memory_files(root)
                with self.assertRaises(AgnirDiscoveryError) as error:
                    AgnirFilesystemContinuityProvider(root).load(PROJECT)
                self.assertEqual(error.exception.code, "AGNIR_CHECKPOINT_RECOVERY_REQUIRED")
                self.assertEqual(memory_files(root), before)

    def test_rollback_failure_retains_recoverable_intent(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_project(root)
            provider = AgnirFilesystemContinuityProvider(root)
            publish = provider._publish_file
            calls = 0
            def fail(path, content):
                nonlocal calls
                calls += 1
                if calls >= 2:
                    raise OSError("simulated disk unavailable")
                publish(path, content)
            with patch.object(provider, "_publish_file", side_effect=fail):
                with self.assertRaises(AgnirDiscoveryError) as error:
                    provider.checkpoint(outcome())
            self.assertEqual(error.exception.code, "AGNIR_CHECKPOINT_RECOVERY_REQUIRED")
            self.assertTrue((root / ".svif-runtime/agnir-pending.json").exists())
            self.assertEqual(AgnirFilesystemContinuityProvider(root).load(PROJECT).next_actions, "new next\n")

    def test_stale_checkpoint_does_not_overwrite_newer_truth(self):
        for version in VERSIONS:
            with self.subTest(version=version), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                write_project(root, version=version)
                provider = AgnirFilesystemContinuityProvider(root)
                prior = provider.load(PROJECT)
                provider.checkpoint(outcome("first"), expected_revision=prior.revision)
                saved = memory_files(root)
                with self.assertRaises(AgnirDiscoveryError) as error:
                    provider.checkpoint(outcome("second"), expected_revision=prior.revision)
                self.assertEqual(error.exception.code, "AGNIR_DISCOVERY_STALE")
                self.assertEqual(memory_files(root), saved)

    def test_exact_retry_is_noop_and_operation_identity_cannot_be_reused(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_project(root)
            provider = AgnirFilesystemContinuityProvider(root)
            prior = provider.load(PROJECT)
            provider.checkpoint(outcome(), expected_revision=prior.revision)
            before = memory_files(root)
            times = {p: p.stat().st_mtime_ns for p in (root / ".agnir").rglob("*") if p.is_file()}
            provider.checkpoint(outcome(), expected_revision=prior.revision)
            self.assertEqual({p: p.stat().st_mtime_ns for p in times}, times)
            with self.assertRaises(AgnirDiscoveryError):
                provider.checkpoint(outcome(decisions="different result"))
            self.assertEqual(memory_files(root), before)

    def test_journal_target_escape_or_corruption_is_rejected_without_writes(self):
        for mutation in ("path", "sha256", "discovery_digest", "duplicate"):
            with self.subTest(mutation=mutation), tempfile.TemporaryDirectory() as directory:
                root = Path(directory) / "project"
                root.mkdir()
                write_project(root)
                outside = root.parent / "outside.txt"
                outside.write_text("outside dummy\n")
                with self.assertRaises(Crash):
                    interrupted(root, 1)
                path = root / ".svif-runtime/agnir-pending.json"
                journal = json.loads(path.read_text())
                if mutation == "path": journal["changes"][0]["path"] = "../outside.txt"
                elif mutation == "sha256": journal["changes"][0]["sha256"] = "wrong"
                elif mutation == "duplicate": journal["changes"][1] = journal["changes"][0]
                else: journal[mutation] = "wrong"
                path.write_text(json.dumps(journal))
                before = memory_files(root)
                with self.assertRaises(AgnirDiscoveryError):
                    AgnirFilesystemContinuityProvider(root).load(PROJECT)
                self.assertEqual(memory_files(root), before)
                self.assertEqual(outside.read_text(), "outside dummy\n")

    def test_reader_waits_for_multi_file_publication(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_project(root)
            writer = AgnirFilesystemContinuityProvider(root)
            reader = AgnirFilesystemContinuityProvider(root)
            written, proceed, returned = threading.Event(), threading.Event(), threading.Event()
            publish = writer._publish_file
            results, errors = [], []
            def pause(path, content):
                publish(path, content)
                if path.name == "state.md":
                    written.set()
                    if not proceed.wait(5): raise RuntimeError("reader coordination timeout")
            def write():
                try:
                    with patch.object(writer, "_publish_file", side_effect=pause): writer.checkpoint(outcome())
                except BaseException as error: errors.append(error)
            def read():
                try: results.append(reader.load(PROJECT))
                except BaseException as error: errors.append(error)
                finally: returned.set()
            first = threading.Thread(target=write)
            first.start()
            self.assertTrue(written.wait(5))
            second = threading.Thread(target=read)
            second.start()
            self.assertFalse(returned.wait(0.05))
            proceed.set()
            first.join(5); second.join(5)
            self.assertFalse(first.is_alive() or second.is_alive())
            self.assertFalse(errors, errors)
            self.assertEqual((results[0].state, results[0].next_actions), ("new state\n", "new next\n"))

    def test_symlink_reads_and_writes_never_escape_selected_project(self):
        for version in VERSIONS:
            for target in ("anchor", "state", "evidence", "runtime"):
                with self.subTest(version=version, target=target), tempfile.TemporaryDirectory() as directory:
                    root = Path(directory) / "project"
                    root.mkdir(); write_project(root, version=version)
                    dummy = root.parent / "outside"
                    dummy.write_text("not a secret, must not be accessed\n")
                    if target == "anchor": link = root / "AGNIR.yaml"
                    elif target == "state": link = root / ".agnir/state.md"
                    elif target == "evidence": link = root / ".agnir/evidence/outside.txt"
                    else:
                        dummy.unlink(); dummy.mkdir()
                        link = root / ".svif-runtime"
                    if link.exists(): link.unlink()
                    try: link.symlink_to(dummy, target_is_directory=target == "runtime")
                    except OSError: self.skipTest("symlink creation unavailable on this host")
                    with self.assertRaises(AgnirDiscoveryError):
                        AgnirFilesystemContinuityProvider(root).load(PROJECT)
                    if target != "runtime": self.assertEqual(dummy.read_text(), "not a secret, must not be accessed\n")

    def test_output_receipt_symlink_is_rejected_before_state_write(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "project"
            root.mkdir(); write_project(root)
            provider = AgnirFilesystemContinuityProvider(root)
            receipt = provider._receipt(provider._discover(PROJECT), PROJECT, "transaction")
            outside = root.parent / "outside"
            outside.write_text("dummy")
            try: receipt.symlink_to(outside)
            except OSError: self.skipTest("symlink creation unavailable")
            with self.assertRaises(AgnirDiscoveryError): provider.checkpoint(outcome())
            self.assertIn("old", (root / ".agnir/state.md").read_text())
            self.assertEqual(outside.read_text(), "dummy")

    def test_hardlinked_evidence_is_not_read(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "project"
            root.mkdir(); write_project(root)
            outside = root.parent / "outside"
            outside.write_text("dummy")
            try: os.link(outside, root / ".agnir/evidence/link")
            except OSError: self.skipTest("hardlinks unavailable")
            with self.assertRaises(AgnirDiscoveryError): AgnirFilesystemContinuityProvider(root).load(PROJECT)

    def test_predictable_old_temp_symlink_cannot_redirect_write(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "project"
            root.mkdir(); write_project(root)
            outside = root.parent / "outside"
            outside.write_text("dummy")
            try: (root / ".agnir/.state.md.svif-tmp").symlink_to(outside)
            except OSError: self.skipTest("symlinks unavailable")
            AgnirFilesystemContinuityProvider(root).checkpoint(outcome())
            self.assertEqual(outside.read_text(), "dummy")

    def test_duplicate_keys_and_aliased_memory_roles_are_rejected(self):
        for mutation in ("duplicate", "alias"):
            with self.subTest(mutation=mutation), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                write_project(root)
                path = root / "AGNIR.yaml"
                text = path.read_text()
                if mutation == "duplicate": text = text.replace('  version: "0.1"', '  version: "0.1"\n  version: "0.2"')
                else: text = text.replace('next_actions: ".agnir/next-actions.md"', 'next_actions: ".agnir/state.md"')
                path.write_text(text)
                with self.assertRaises(AgnirDiscoveryError) as error: AgnirFilesystemContinuityProvider(root).load(PROJECT)
                self.assertEqual(error.exception.code, "AGNIR_DISCOVERY_INCONSISTENT")


if __name__ == "__main__":
    unittest.main()
