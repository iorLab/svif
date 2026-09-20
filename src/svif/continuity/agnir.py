from __future__ import annotations

import base64
import hashlib
import json
import os
import re
import stat
from contextlib import contextmanager
from typing import Iterator
from dataclasses import asdict, dataclass
from pathlib import Path

from svif.runtime import BindingError, CapabilityRequest, ContinuitySnapshot, ContinuityUpdate, EvidenceRecord, OperationOutcome
from svif.continuity.filesystem import FilesystemSafetyError, ProjectFilesystem


class AgnirDiscoveryError(BindingError):
    """Agnir discovery/profile failure preserving the Agnir semantic failure code."""

    def __init__(self, code: str, message: str) -> None:
        super().__init__(f"{code}: {message}")
        self.code = code


@dataclass(frozen=True)
class _ResolvedAgnir:
    version: str
    profile: str
    lineage_identity: str | None
    vcs_selector: str | None
    state: Path
    next_actions: Path
    decisions: Path | None
    evidence: Path | None
    discovery_digest: str


class AgnirFilesystemContinuityProvider:
    """Agnir repository/filesystem Continuity Provider for Svif.

    The adapter supports the published Core/profile `0.1` and `0.2`
    compatibility lines plus the stable Core/profile `1.0` line. Provider-specific
    lineage and selector semantics stay inside this adapter; the Svif
    Orchestrator remains Continuity-Provider-neutral.
    """

    provider_id = "agnir"
    _SUPPORTED_PROFILES = {
        "0.1": "repository-filesystem/0.1",
        "0.2": "repository-filesystem/0.2",
        "1.0": "repository-filesystem/1.0",
    }

    def __init__(
        self,
        project_root: str | Path,
        *,
        expected_core_version: str | None = None,
        expected_profile: str | None = None,
        selected_vcs_selector: str | None = None,
    ) -> None:
        self.project_root = Path(project_root).resolve()
        self._fs = ProjectFilesystem(self.project_root)
        self._journal = self.project_root / ProjectFilesystem.RUNTIME / "agnir-pending.json"
        self._effect = self.project_root / ProjectFilesystem.RUNTIME / "agnir-effect.json"
        self.expected_core_version = expected_core_version
        self.expected_profile = expected_profile
        self.selected_vcs_selector = selected_vcs_selector

    @staticmethod
    def _strip_scalar(value: str) -> str | None:
        value = value.strip()
        if value in {"null", "Null", "NULL", "~"}:
            return None
        if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
            return value[1:-1]
        return value

    @classmethod
    def _parse_discovery(cls, text: str) -> dict[tuple[str, ...], str | None]:
        """Parse the scalar YAML subset used by the repository profiles.

        This is deliberately not a general YAML parser. It recognizes nested
        mapping/scalar paths by indentation and ignores list items/complex YAML.
        Unsupported forms fail later as missing or inconsistent semantics.
        """

        values: dict[tuple[str, ...], str | None] = {}
        stack: list[tuple[int, str]] = []
        seen: set[tuple[str, ...]] = set()
        for raw in text.splitlines():
            if not raw.strip() or raw.lstrip().startswith("#"):
                continue
            if raw.lstrip().startswith("-"):
                continue
            if "\t" in raw[:len(raw) - len(raw.lstrip())]:
                raise AgnirDiscoveryError("AGNIR_DISCOVERY_INCONSISTENT", "tabs are not supported in discovery indentation")
            indent = len(raw) - len(raw.lstrip(" "))
            match = re.match(r"^\s*([A-Za-z0-9_./-]+):\s*(.*?)\s*$", raw)
            if not match:
                continue
            key, scalar_text = match.groups()
            while stack and indent <= stack[-1][0]:
                stack.pop()
            path = tuple([item[1] for item in stack] + [key])
            if path in seen:
                raise AgnirDiscoveryError("AGNIR_DISCOVERY_INCONSISTENT", "duplicate discovery key: " + ".".join(path))
            seen.add(path)
            if scalar_text == "":
                stack.append((indent, key))
                continue
            path = tuple([item[1] for item in stack] + [key])
            values[path] = cls._strip_scalar(scalar_text)
        return values

    @staticmethod
    def _fail(code: str, message: str) -> AgnirDiscoveryError:
        return AgnirDiscoveryError(code, message)

    def _resolve_locator(
        self,
        locator: str | None,
        *,
        required: bool,
        kind: str,
    ) -> Path | None:
        if locator is None:
            if required:
                raise self._fail(
                    "AGNIR_DISCOVERY_UNRESOLVABLE",
                    f"required {kind} locator is null",
                )
            return None

        candidate = self._fs.path(locator)
        if not candidate.is_relative_to(self.project_root):
            raise self._fail(
                "AGNIR_DISCOVERY_UNRESOLVABLE",
                f"{kind} locator escapes the authorized Project root",
            )
        if self._fs.metadata(candidate) is None:
            raise self._fail(
                "AGNIR_DISCOVERY_UNRESOLVABLE",
                f"{kind} locator does not resolve: {locator}",
            )
        return candidate

    def _discover(self, project_identity: str) -> _ResolvedAgnir:
        discovery = self.project_root / "AGNIR.yaml"
        if self._fs.metadata(discovery) is None:
            raise self._fail(
                "AGNIR_DISCOVERY_NOT_FOUND",
                "repository/filesystem profile could not resolve AGNIR.yaml at the Project Entry Point",
            )

        discovery_bytes = self._fs.read(discovery)
        values = self._parse_discovery(discovery_bytes.decode("utf-8"))
        version = values.get(("agnir", "version"))
        profile = values.get(("agnir", "discovery_profile"))

        if not isinstance(version, str) or version not in self._SUPPORTED_PROFILES:
            raise self._fail(
                "AGNIR_DISCOVERY_UNSUPPORTED_VERSION",
                f"unsupported Agnir Core version: {version!r}",
            )
        expected_profile_for_version = self._SUPPORTED_PROFILES[version]
        if profile != expected_profile_for_version:
            raise self._fail(
                "AGNIR_DISCOVERY_INCONSISTENT",
                f"Core {version} requires discovery profile {expected_profile_for_version!r}, discovered {profile!r}",
            )
        if self.expected_core_version is not None and version != self.expected_core_version:
            raise self._fail(
                "AGNIR_DISCOVERY_UNSUPPORTED_VERSION",
                f"Svif binding expects Agnir Core {self.expected_core_version}, discovered {version}",
            )
        if self.expected_profile is not None and profile != self.expected_profile:
            raise self._fail(
                "AGNIR_DISCOVERY_INCONSISTENT",
                f"Svif binding expects discovery profile {self.expected_profile!r}, discovered {profile!r}",
            )

        discovered_identity = values.get(("project", "identity"))
        if discovered_identity != project_identity:
            raise self._fail(
                "AGNIR_DISCOVERY_PROJECT_MISMATCH",
                f"expected {project_identity!r}, discovered {discovered_identity!r}",
            )

        lineage_identity = values.get(("continuity", "lineage"))
        if version in {"0.2", "1.0"}:
            if not isinstance(lineage_identity, str) or not lineage_identity:
                raise self._fail(
                    "AGNIR_LINEAGE_REQUIRED",
                    f"Core {version} repository/filesystem discovery requires continuity.lineage",
                )
        else:
            lineage_identity = None

        binding_selector = values.get(
            ("extensions", "agnir/vcs", "lineage_binding", "selector")
        )
        if self.selected_vcs_selector is not None and version in {"0.2", "1.0"}:
            if not isinstance(binding_selector, str) or not binding_selector:
                raise self._fail(
                    "AGNIR_VCS_LINEAGE_BINDING_REQUIRED",
                    "selected VCS context has no durable lineage selector binding",
                )
            if binding_selector != self.selected_vcs_selector:
                raise self._fail(
                    "AGNIR_VCS_LINEAGE_BINDING_MISMATCH",
                    f"selected VCS selector {self.selected_vcs_selector!r} conflicts with durable binding {binding_selector!r}",
                )

        paths = {
            "state": self._resolve_locator(
                values.get(("memory", "state")), required=True, kind="Current State"
            ),
            "next_actions": self._resolve_locator(
                values.get(("memory", "next_actions")), required=True, kind="Next Actions"
            ),
            "decisions": self._resolve_locator(
                values.get(("memory", "decisions")), required=False, kind="Decisions"
            ),
            "evidence": self._resolve_locator(
                values.get(("memory", "evidence")), required=False, kind="Evidence"
            ),
        }

        for kind in ("state", "next_actions", "decisions"):
            path = paths[kind]
            if path is not None and not stat.S_ISREG(self._fs.metadata(path).st_mode):
                raise self._fail(
                    "AGNIR_DISCOVERY_UNRESOLVABLE",
                    f"{kind} locator is not a file",
                )

        evidence = paths["evidence"]
        if evidence is not None and not stat.S_ISDIR(self._fs.metadata(evidence).st_mode):
            raise self._fail(
                "AGNIR_DISCOVERY_UNRESOLVABLE",
                "Evidence locator is not a directory",
            )

        concrete = [path for path in paths.values() if path is not None]
        if len(set(concrete)) != len(concrete):
            raise self._fail("AGNIR_DISCOVERY_INCONSISTENT", "memory roles must not alias each other")
        for path in concrete:
            if path == discovery or path.is_relative_to(self.project_root / ProjectFilesystem.RUNTIME):
                raise self._fail("AGNIR_DISCOVERY_INCONSISTENT", "memory locator overlaps discovery/recovery metadata")
        if evidence is not None and any(paths[k] is not None and paths[k].is_relative_to(evidence)
                                       for k in ("state", "next_actions", "decisions")):
            raise self._fail("AGNIR_DISCOVERY_INCONSISTENT", "state files must not overlap the evidence collection")
        return _ResolvedAgnir(
            version=version,
            profile=profile,
            lineage_identity=lineage_identity,
            vcs_selector=binding_selector if isinstance(binding_selector, str) else None,
            state=paths["state"],
            next_actions=paths["next_actions"],
            decisions=paths["decisions"],
            evidence=paths["evidence"],
            discovery_digest=hashlib.sha256(discovery_bytes).hexdigest(),
        )

    @contextmanager
    def operation_guard(self, project_identity: str) -> Iterator[None]:
        """Serialize cooperating readers/writers; recover before exposing memory."""
        try:
            with self._fs.guard():
                self._recover(project_identity)
                self._clear_resolved_effect(project_identity)
                yield
        except (FilesystemSafetyError, UnicodeError) as exc:
            raise self._fail("AGNIR_DISCOVERY_UNRESOLVABLE", str(exc)) from exc

    def _snapshot(self, project_identity: str) -> tuple[_ResolvedAgnir, ContinuitySnapshot]:
        resolved = self._discover(project_identity)
        raw: dict[str, bytes] = {}

        def read(path: Path | None) -> str | None:
            if path is None:
                return None
            value = self._fs.read(path)
            raw[path.relative_to(self.project_root).as_posix()] = value
            return value.decode("utf-8")

        state, next_actions, decisions = read(resolved.state), read(resolved.next_actions), read(resolved.decisions)
        evidence = {} if resolved.evidence is None else {p.name: read(p) for p in self._fs.files(resolved.evidence)}
        discovery = self._fs.read(self.project_root / "AGNIR.yaml")
        if hashlib.sha256(discovery).hexdigest() != resolved.discovery_digest:
            raise self._fail("AGNIR_DISCOVERY_STALE", "Discovery Record changed during load")
        raw["AGNIR.yaml"] = discovery
        identity = [(name, hashlib.sha256(value).hexdigest()) for name, value in sorted(raw.items())]
        revision = hashlib.sha256(json.dumps(identity, ensure_ascii=True).encode()).hexdigest()
        return resolved, ContinuitySnapshot(project_identity, state, next_actions, decisions, evidence, revision)

    def resolve_lineage(self, project_identity: str) -> str | None:
        with self.operation_guard(project_identity):
            return self._discover(project_identity).lineage_identity

    def load(self, project_identity: str) -> ContinuitySnapshot:
        with self.operation_guard(project_identity):
            if self._effect_record(project_identity) is not None:
                raise self._fail("AGNIR_EFFECT_RECONCILIATION_REQUIRED", "external effect is unresolved; inspect pending_effect before continuation")
            return self._snapshot(project_identity)[1]

    @staticmethod
    def _require_text_update(value: object | None, label: str) -> str | None:
        if value is not None and not isinstance(value, str):
            raise BindingError(f"Agnir filesystem {label} update must be text")
        return value

    def _receipt(self, resolved: _ResolvedAgnir, project: str, operation: str) -> Path | None:
        if resolved.evidence is None:
            return None
        digest = hashlib.sha256(f"{project}\0{resolved.lineage_identity or ''}\0{operation}".encode()).hexdigest()
        return resolved.evidence / f"svif-operation-{digest}.json"

    def _permitted(self, resolved: _ResolvedAgnir, project: str, operation: str) -> set[Path]:
        return {p for p in (resolved.state, resolved.next_actions, resolved.decisions,
                           self._receipt(resolved, project, operation)) if p is not None}

    def _plan(self, outcome: OperationOutcome, expected_revision: str | None,
              *, reject_replay: bool = False) -> tuple[_ResolvedAgnir, dict[Path, bytes]]:
        for value in (outcome.project_identity, outcome.operation_id, outcome.subject_identity):
            if not isinstance(value, str) or not value.strip():
                raise BindingError("checkpoint requires non-empty Project/operation/subject identity")
        # Validate every value and locator before writing even one state file.
        resolved, snapshot = self._snapshot(outcome.project_identity)
        values = {name: self._require_text_update(getattr(outcome.continuity_update, name), name)
                  for name in ("state", "next_actions", "decisions")}
        writes = {}
        for name, value in values.items():
            path = getattr(resolved, name)
            if value is not None:
                if path is None:
                    raise self._fail("AGNIR_DISCOVERY_UNRESOLVABLE", f"cannot persist {name}: no locator")
                writes[path] = value.encode("utf-8")
        receipt = self._receipt(resolved, outcome.project_identity, outcome.operation_id)
        if receipt is not None:
            payload = {
                "svif_runtime_checkpoint": "0.2",
                "project_identity": outcome.project_identity,
                "agnir_lineage": resolved.lineage_identity,
                "operation_id": outcome.operation_id,
                "subject_identity": outcome.subject_identity,
                "externally_effectful": outcome.externally_effectful,
                "evidence": [asdict(record) for record in outcome.evidence],
                "updates": {name: None if value is None else hashlib.sha256(value.encode()).hexdigest()
                            for name, value in values.items()},
            }
            writes[receipt] = (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode()
            previous = self._fs.read(receipt, missing_ok=True)
            # The old 64-bit locator remains a replay boundary, never overwritten.
            legacy = receipt.with_name(receipt.name[:len("svif-operation-") + 16] + ".json")
            if previous is not None or self._fs.read(legacy, missing_ok=True) is not None:
                same = previous == writes[receipt] and all(self._fs.read(p, missing_ok=True) == v for p, v in writes.items())
                if not reject_replay and same:
                    return resolved, {}  # Exact retry of an already committed checkpoint.
                raise self._fail("AGNIR_OPERATION_REPLAY", "operation receipt already exists; reconcile, do not replay")
        if expected_revision is not None and expected_revision != snapshot.revision:
            raise self._fail("AGNIR_DISCOVERY_STALE", "durable memory changed since operation began")
        # Preflight also detects unsafe receipt leaves, even for new operations.
        for path in writes:
            self._fs.read(path, missing_ok=True)
        return resolved, writes

    def validate_checkpoint(self, outcome: OperationOutcome, *, expected_revision: str | None = None) -> None:
        with self.operation_guard(outcome.project_identity):
            if self._effect_record(outcome.project_identity) is not None:
                raise self._fail("AGNIR_EFFECT_RECONCILIATION_REQUIRED", "prior external effect needs independent observation")
            self._plan(outcome, expected_revision, reject_replay=True)

    def _publish_file(self, path: Path, content: bytes) -> None:
        self._fs.write(path, content)

    @staticmethod
    def _encode(value: bytes | None) -> str | None:
        return None if value is None else base64.b64encode(value).decode("ascii")

    def _journal_changes(self, project_identity: str) -> list[tuple[Path, bytes | None, bytes]] | None:
        data = self._fs.read(self._journal, missing_ok=True)
        if data is None:
            return None
        try:
            record = json.loads(data)
            resolved = self._discover(project_identity)
            if (record["schema"] != "svif-agnir-transaction/1" or record["project_identity"] != project_identity
                    or record["discovery_digest"] != resolved.discovery_digest
                    or not isinstance(record["operation_id"], str) or not record["operation_id"].strip()):
                raise ValueError("journal binding mismatch")
            allowed = self._permitted(resolved, project_identity, record["operation_id"])
            if not isinstance(record["changes"], list) or not 1 <= len(record["changes"]) <= 4:
                raise ValueError("invalid transaction size")
            changes = []
            seen: set[Path] = set()
            for item in record["changes"]:
                if not isinstance(item["path"], str) or Path(item["path"]).is_absolute():
                    raise ValueError("journal path is not relative")
                path = self._fs.path(item["path"])
                if path not in allowed or path in seen:
                    raise ValueError("unauthorized or duplicate journal target")
                seen.add(path)
                before = None if item["before"] is None else base64.b64decode(item["before"], validate=True)
                after = base64.b64decode(item["after"], validate=True)
                after.decode("utf-8")
                if hashlib.sha256(after).hexdigest() != item["sha256"]:
                    raise ValueError("corrupt staged content")
                current = self._fs.read(path, missing_ok=True)
                if current != before and current != after:
                    raise ValueError("target changed outside the interrupted transaction")
                changes.append((path, before, after))
            return changes
        except (KeyError, TypeError, ValueError, FilesystemSafetyError) as exc:
            raise self._fail("AGNIR_CHECKPOINT_RECOVERY_REQUIRED", "invalid/conflicting journal; no recovery writes performed") from exc

    def _recover(self, project_identity: str) -> None:
        changes = self._journal_changes(project_identity)
        if changes is None:
            return
        # A durable intent was recorded only after complete preflight. Following
        # process death, finish it before returning any mixed state to a reader.
        try:
            for path, _, after in changes:
                self._publish_file(path, after)
            self._discover(project_identity)
            self._fs.remove(self._journal)
        except Exception as exc:
            raise self._fail("AGNIR_CHECKPOINT_RECOVERY_REQUIRED", "interrupted checkpoint could not be recovered") from exc

    def checkpoint(self, outcome: OperationOutcome, *, expected_revision: str | None = None) -> None:
        with self.operation_guard(outcome.project_identity):
            self._validate_pending_outcome(outcome)
            resolved, writes = self._plan(outcome, expected_revision)
            if not writes:
                return
            before = {path: self._fs.read(path, missing_ok=True) for path in writes}
            record = {
                "schema": "svif-agnir-transaction/1",
                "project_identity": outcome.project_identity,
                "operation_id": outcome.operation_id,
                "discovery_digest": resolved.discovery_digest,
                "changes": [{"path": path.relative_to(self.project_root).as_posix(),
                             "before": self._encode(before[path]), "after": self._encode(content),
                             "sha256": hashlib.sha256(content).hexdigest()}
                            for path, content in writes.items()],
            }
            # Journal first, fsynced and atomically replaced; no fixed-name temp.
            self._fs.write(self._journal, (json.dumps(record, sort_keys=True) + "\n").encode())
            try:
                for path, content in writes.items():
                    self._publish_file(path, content)
                if self._discover(outcome.project_identity).discovery_digest != resolved.discovery_digest:
                    raise self._fail("AGNIR_DISCOVERY_STALE", "Discovery Record changed during checkpoint")
                self._fs.remove(self._journal)
            except Exception as original:
                try:
                    # Refuse to overwrite unrelated concurrent edits on rollback.
                    self._journal_changes(outcome.project_identity)
                    for path, content in before.items():
                        if content is None:
                            self._fs.remove(path)
                        else:
                            self._publish_file(path, content)
                    self._fs.remove(self._journal)
                except Exception as recovery:
                    raise self._fail("AGNIR_CHECKPOINT_RECOVERY_REQUIRED", "checkpoint and rollback failed; recovery intent retained") from recovery
                raise self._fail("AGNIR_CHECKPOINT_FAILED", "checkpoint failed and all prior contents were restored") from original
            # BaseException (process interruption) deliberately retains the
            # journal. Next provider load rolls forward or fails closed.

            # The receipt is durable before an uncertain external-effect marker
            # can be retired. A cleanup interruption is recovered at next entry.
            self._clear_resolved_effect(outcome.project_identity)

    def _effect_record(self, project_identity: str) -> dict | None:
        data = self._fs.read(self._effect, missing_ok=True)
        if data is None:
            return None
        try:
            value = json.loads(data)
            if value["schema"] != "svif-agnir-effect/1" or value["project_identity"] != project_identity:
                raise ValueError("effect identity mismatch")
            for name in ("operation_id", "subject_identity", "target_identity", "provider", "revision"):
                if not isinstance(value[name], str) or not value[name].strip():
                    raise ValueError("effect identity missing")
            return value
        except (ValueError, KeyError, TypeError) as exc:
            raise self._fail("AGNIR_EFFECT_RECONCILIATION_REQUIRED", "invalid pending external-effect record") from exc

    def pending_effect(self, project_identity: str) -> dict | None:
        """Inspect uncertain effect identity without treating old state as success."""
        with self.operation_guard(project_identity):
            self._discover(project_identity)
            return self._effect_record(project_identity)

    def prepare_effect(self, outcome: OperationOutcome, request: CapabilityRequest,
                       *, expected_revision: str | None = None) -> None:
        with self.operation_guard(outcome.project_identity):
            if self._effect_record(outcome.project_identity) is not None:
                raise self._fail("AGNIR_EFFECT_RECONCILIATION_REQUIRED", "do not replay an unresolved external effect")
            resolved, snapshot = self._snapshot(outcome.project_identity)
            self._plan(outcome, expected_revision, reject_replay=True)
            if resolved.evidence is None or not request.target_identity:
                raise BindingError("recoverable effects require a durable evidence locator and stable target")
            record = {
                "schema": "svif-agnir-effect/1",
                "project_identity": outcome.project_identity,
                "operation_id": outcome.operation_id,
                "subject_identity": outcome.subject_identity,
                "target_identity": request.target_identity,
                "provider": request.provider,
                "revision": snapshot.revision,
                "verification": [asdict(item) for item in outcome.evidence if item.kind == "verification"],
                "continuity_update": asdict(outcome.continuity_update),
            }
            self._fs.write(self._effect, (json.dumps(record, sort_keys=True) + "\n").encode())

    def _matches_pending(self, record: dict, evidence: tuple[EvidenceRecord, ...]) -> bool:
        return all(any(item.kind == kind and item.status == "succeeded"
                       and item.subject_identity == record["subject_identity"]
                       and item.target_identity == record["target_identity"]
                       and item.producer == record["provider"] for item in evidence)
                   for kind in ("delivery", "observation"))

    def _validate_pending_outcome(self, outcome: OperationOutcome) -> None:
        record = self._effect_record(outcome.project_identity)
        if record is not None and (outcome.operation_id != record["operation_id"]
                or outcome.subject_identity != record["subject_identity"] or not outcome.externally_effectful
                or not self._matches_pending(record, outcome.evidence)):
            raise self._fail("AGNIR_EFFECT_RECONCILIATION_REQUIRED", "checkpoint does not independently resolve the pending effect")

    def _clear_resolved_effect(self, project_identity: str) -> None:
        record = self._effect_record(project_identity)
        if record is None:
            return
        resolved = self._discover(project_identity)
        receipt = self._receipt(resolved, project_identity, record["operation_id"])
        if receipt is None:
            return
        data = self._fs.read(receipt, missing_ok=True)
        if data is None:
            return
        try:
            saved = json.loads(data)
            evidence = tuple(EvidenceRecord(**item) for item in saved["evidence"])
            if (saved["project_identity"] != project_identity or saved["operation_id"] != record["operation_id"]
                    or saved["subject_identity"] != record["subject_identity"]
                    or not saved["externally_effectful"] or not self._matches_pending(record, evidence)):
                raise ValueError("pending effect receipt mismatch")
        except (ValueError, TypeError, KeyError) as exc:
            raise self._fail("AGNIR_EFFECT_RECONCILIATION_REQUIRED", "pending effect has a conflicting receipt") from exc
        self._fs.remove(self._effect)

    def reconcile_effect(self, project_identity: str, *, delivery: EvidenceRecord,
                         observation: EvidenceRecord) -> OperationOutcome:
        """Trusted integration-only recovery. No actuation is performed here.

        The caller must obtain these receipts from an independent provider read,
        never from an untrusted model assertion. Stale memory still blocks repair.
        """
        with self.operation_guard(project_identity):
            record = self._effect_record(project_identity)
            if record is None:
                raise BindingError("there is no pending effect to reconcile")
            if not self._matches_pending(record, (delivery, observation)):
                raise self._fail("AGNIR_EFFECT_RECONCILIATION_REQUIRED", "independent evidence does not resolve subject/target/provider")
            verification = tuple(EvidenceRecord(**item) for item in record["verification"])
            result = OperationOutcome(project_identity, record["operation_id"], record["subject_identity"],
                                      verification + (delivery, observation), True,
                                      ContinuityUpdate(**record["continuity_update"]))
            self.checkpoint(result, expected_revision=record["revision"])
            return result
