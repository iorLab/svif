from __future__ import annotations

import hashlib
import json
import re
import threading
from contextlib import contextmanager
from dataclasses import asdict, dataclass
from pathlib import Path

from svif.runtime import AuthorityRequired, BindingError, ContinuitySnapshot, OperationOutcome
from ._filesystem import ProjectFiles, StorageError


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
        self.expected_core_version = expected_core_version
        self.expected_profile = expected_profile
        self.selected_vcs_selector = selected_vcs_selector
        self._files = ProjectFiles(self.project_root)
        self._effect_context = threading.local()

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
        for raw in text.splitlines():
            if not raw.strip() or raw.lstrip().startswith("#"):
                continue
            if raw.lstrip().startswith("-"):
                continue
            indent = len(raw) - len(raw.lstrip(" "))
            match = re.match(r"^\s*([A-Za-z0-9_./-]+):\s*(.*?)\s*$", raw)
            if not match:
                continue
            key, scalar_text = match.groups()
            while stack and indent <= stack[-1][0]:
                stack.pop()
            if scalar_text == "":
                stack.append((indent, key))
                continue
            path = tuple([item[1] for item in stack] + [key])
            if path in values:
                raise AgnirDiscoveryError("AGNIR_DISCOVERY_INCONSISTENT", "duplicate discovery key")
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

        candidate = self._files.path(locator)
        if not candidate.is_relative_to(self.project_root):
            raise self._fail(
                "AGNIR_DISCOVERY_UNRESOLVABLE",
                f"{kind} locator escapes the authorized Project root",
            )
        if not candidate.exists():
            raise self._fail(
                "AGNIR_DISCOVERY_UNRESOLVABLE",
                f"{kind} locator does not resolve: {locator}",
            )
        return candidate

    def _discover(self, project_identity: str) -> _ResolvedAgnir:
        discovery = self._files.path("AGNIR.yaml")
        if not discovery.is_file():
            raise self._fail(
                "AGNIR_DISCOVERY_NOT_FOUND",
                "repository/filesystem profile could not resolve AGNIR.yaml at the Project Entry Point",
            )

        values = self._parse_discovery(self._files.read(discovery))
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
            if path is not None and not path.is_file():
                raise self._fail(
                    "AGNIR_DISCOVERY_UNRESOLVABLE",
                    f"{kind} locator is not a file",
                )

        memory_paths = [p for p in paths.values() if p is not None]
        if len(set(memory_paths)) != len(memory_paths) or discovery in memory_paths:
            raise self._fail("AGNIR_DISCOVERY_INCONSISTENT", "memory locators alias each other or discovery")
        # Each memory file is distinct and must not become an evidence receipt.
        evidence = paths["evidence"]
        if evidence is not None and any(p.parent == evidence for p in memory_paths if p != evidence):
            raise self._fail("AGNIR_DISCOVERY_INCONSISTENT", "memory files cannot be evidence children")
        if evidence is not None and not evidence.is_dir():
            raise self._fail(
                "AGNIR_DISCOVERY_UNRESOLVABLE",
                "Evidence locator is not a directory",
            )

        return _ResolvedAgnir(
            version=version,
            profile=profile,
            lineage_identity=lineage_identity,
            vcs_selector=binding_selector if isinstance(binding_selector, str) else None,
            state=paths["state"],
            next_actions=paths["next_actions"],
            decisions=paths["decisions"],
            evidence=paths["evidence"],
        )

    @contextmanager
    def _locked(self):
        try:
            with self._files.locked():
                yield
        except StorageError as exc:
            raise self._fail(exc.code, str(exc)) from exc
        except (OSError, UnicodeError) as exc:
            raise self._fail("AGNIR_DISCOVERY_UNRESOLVABLE", "continuity I/O failed") from exc

    def _read_optional(self, path: Path | None) -> str | None:
        return None if path is None else self._files.read(path)

    def _read_evidence(self, path: Path | None) -> dict[str, str]:
        if path is None:
            return {}
        result = {}
        for item in sorted(path.iterdir()):
            # Validate before is_file(): is_file itself follows links.
            item = self._files.path(item)
            if item.is_file():
                result[item.name] = self._files.read(item)
        return result

    def _evidence_path(self, resolved: _ResolvedAgnir, project: str, operation: str) -> Path | None:
        if resolved.evidence is None:
            return None
        digest = hashlib.sha256(
            f"{project}\0{resolved.lineage_identity or ''}\0{operation}".encode("utf-8")
        ).hexdigest()[:16]
        return self._files.path(resolved.evidence / f"svif-operation-{digest}.json")

    def _context(self, resolved: _ResolvedAgnir, project: str, operation: str) -> dict:
        return {
            "project_identity": project, "lineage": resolved.lineage_identity,
            "operation_id": operation,
            "discovery_sha256": hashlib.sha256(self._files.read(self.project_root / "AGNIR.yaml").encode("utf-8")).hexdigest(),
        }

    def _authorize(self, resolved: _ResolvedAgnir, project: str, context: dict) -> set[Path]:
        if not isinstance(context, dict) or not isinstance(context.get("operation_id"), str) or not context["operation_id"]:
            raise ValueError("invalid checkpoint context")
        if context != self._context(resolved, project, context["operation_id"]):
            raise ValueError("checkpoint context/binding changed")
        paths = {resolved.state, resolved.next_actions}
        if resolved.decisions is not None:
            paths.add(resolved.decisions)
        receipt = self._evidence_path(resolved, project, context["operation_id"])
        if receipt is not None:
            paths.add(receipt)
        return paths

    def _recover(self, project: str) -> _ResolvedAgnir:
        resolved = self._discover(project)
        self._files.recover(lambda context: self._authorize(resolved, project, context))
        pending = self._files.read(self.project_root / ProjectFiles.PENDING_EFFECT, missing=True)
        if pending is not None:
            try:
                data = json.loads(pending)
                self._authorize(resolved, project, data["context"])
                receipt = self._evidence_path(resolved, project, data["context"]["operation_id"])
                saved = self._files.read(receipt, missing=True) if receipt is not None else None
                if saved is not None:
                    recorded = json.loads(saved)
                    if (recorded.get("operation_id") != data["context"]["operation_id"]
                        or recorded.get("project_identity") != project
                        or recorded.get("subject_identity") != data["subject_identity"]
                        or recorded.get("target_identity") != data["target_identity"]
                        or recorded.get("externally_effectful") is not True
                        or recorded.get("agnir_lineage") != resolved.lineage_identity
                        or not any(isinstance(r, dict) and r.get("kind") == "observation"
                                   and r.get("status") == "succeeded"
                                   and r.get("subject_identity") == data["subject_identity"]
                                   and r.get("target_identity") == data["target_identity"]
                                   for r in recorded.get("evidence", []))):
                        raise ValueError("pending effect and completion receipt disagree")
                    self._files.remove(self.project_root / ProjectFiles.PENDING_EFFECT)
            except (ValueError, TypeError, KeyError) as exc:
                raise self._fail("AGNIR_EXTERNAL_EFFECT_UNCONFIRMED", "pending effect requires explicit reconciliation") from exc
        return self._discover(project)

    def _snapshot(self, project: str, resolved: _ResolvedAgnir) -> ContinuitySnapshot:
        values = {
            "state": self._read_optional(resolved.state),
            "next_actions": self._read_optional(resolved.next_actions),
            "decisions": self._read_optional(resolved.decisions),
            "evidence": self._read_evidence(resolved.evidence),
        }
        revision = hashlib.sha256(json.dumps(
            {"discovery": self._files.read(self.project_root / "AGNIR.yaml"), **values},
            sort_keys=True, ensure_ascii=False,
        ).encode("utf-8")).hexdigest()
        pending = self._files.read(self.project_root / ProjectFiles.PENDING_EFFECT, missing=True)
        return ContinuitySnapshot(project_identity=project, revision=revision, pending_effect=pending, **values)

    def resolve_lineage(self, project_identity: str) -> str | None:
        with self._locked():
            return self._recover(project_identity).lineage_identity

    def load(self, project_identity: str) -> ContinuitySnapshot:
        with self._locked():
            return self._snapshot(project_identity, self._recover(project_identity))

    @staticmethod
    def _require_text_update(value: object | None, label: str) -> str | None:
        if value is None:
            return None
        if not isinstance(value, str):
            raise BindingError(f"Agnir filesystem {label} update must be text")
        return value

    def _preflight(self, outcome: OperationOutcome) -> tuple[_ResolvedAgnir, dict[Path, str]]:
        resolved = self._recover(outcome.project_identity)
        snapshot = self._snapshot(outcome.project_identity, resolved)
        if snapshot.pending_effect is not None and snapshot.pending_effect != getattr(self._effect_context, "active", None):
            raise self._fail("AGNIR_EXTERNAL_EFFECT_UNCONFIRMED", "an earlier external effect is unresolved; observe and reconcile before retry")
        if outcome.externally_effectful and resolved.evidence is None:
            raise self._fail("AGNIR_DISCOVERY_UNRESOLVABLE", "external effects require a durable evidence locator")
        if outcome.expected_revision is not None and snapshot.revision != outcome.expected_revision:
            raise self._fail("AGNIR_CHECKPOINT_STALE", "Project changed after DISCOVER; reload and reconcile")
        if not isinstance(outcome.operation_id, str) or not outcome.operation_id.strip():
            raise BindingError("checkpoint requires a stable operation id")
        writes = {}
        update = outcome.continuity_update
        # Validate every update and locator before mutating ANY memory file.
        for label, value, path in (
            ("Current State", update.state, resolved.state),
            ("Next Actions", update.next_actions, resolved.next_actions),
            ("Decisions", update.decisions, resolved.decisions),
        ):
            text = self._require_text_update(value, label)
            if text is not None:
                if path is None:
                    raise self._fail("AGNIR_DISCOVERY_UNRESOLVABLE", f"cannot persist {label}: locator missing")
                writes[path] = text
        receipt = self._evidence_path(resolved, outcome.project_identity, outcome.operation_id)
        if receipt is not None:
            if self._files.read(receipt, missing=True) is not None:
                raise self._fail("AGNIR_CHECKPOINT_DUPLICATE_OPERATION", "operation already checkpointed; do not replay")
            payload = {
                "svif_runtime_checkpoint": "0.1",
                "project_identity": outcome.project_identity,
                "agnir_lineage": resolved.lineage_identity,
                "operation_id": outcome.operation_id,
                "subject_identity": outcome.subject_identity,
                "externally_effectful": outcome.externally_effectful,
                "target_identity": outcome.target_identity,
                "evidence": [asdict(record) for record in outcome.evidence],
            }
            writes[receipt] = json.dumps(payload, indent=2, sort_keys=True) + "\n"
        return resolved, writes

    @contextmanager
    def operation_guard(self, outcome: OperationOutcome):
        """Serialize this Project's complete boundary, including external effects."""
        with self._locked():
            resolved, _ = self._preflight(outcome)
            if outcome.externally_effectful:
                pending = json.dumps({
                    "context": self._context(resolved, outcome.project_identity, outcome.operation_id),
                    "subject_identity": outcome.subject_identity, "target_identity": outcome.target_identity,
                    "status": "attempted-unconfirmed",
                }, sort_keys=True)
                self._files.write(self.project_root / ProjectFiles.PENDING_EFFECT, pending)
                self._effect_context.active = pending
            try:
                yield
            finally:
                self._effect_context.active = None
                # Successful checkpoint recovery removes the marker. Failure keeps it
                # so a restarted process cannot blindly replay an uncertain effect.

    def checkpoint(self, outcome: OperationOutcome) -> None:
        with self._locked():
            resolved, writes = self._preflight(outcome)
            self._files.publish(
                writes, self._context(resolved, outcome.project_identity, outcome.operation_id),
                lambda context: self._authorize(resolved, outcome.project_identity, context),
            )
            # A complete reload must succeed before resumability is claimed.
            self._snapshot(outcome.project_identity, self._recover(outcome.project_identity))

    def reconcile_effect(self, outcome: OperationOutcome, *, authority_grants: frozenset[str]) -> None:
        """Trusted integration entry point for an independently confirmed effect.

        This does not retry delivery. Unknown/absent effects remain blocked until
        a Principal reconciles the provider/account and selected Project state.
        """
        if "effect-reconciliation" not in authority_grants:
            raise AuthorityRequired("pending-effect reconciliation requires trusted authority")
        with self._locked():
            resolved = self._recover(outcome.project_identity)
            pending = self._files.read(self.project_root / ProjectFiles.PENDING_EFFECT, missing=True)
            if pending is None:
                raise BindingError("no pending effect to reconcile")
            data = json.loads(pending)
            if (not outcome.externally_effectful
                or outcome.operation_id != data["context"]["operation_id"]
                or outcome.subject_identity != data["subject_identity"]
                or outcome.target_identity != data["target_identity"]
                or not any(r.kind == "observation" and r.status == "succeeded"
                           and r.subject_identity == outcome.subject_identity
                           and r.target_identity == outcome.target_identity for r in outcome.evidence)):
                raise BindingError("reconciliation requires matching independent successful observation")
            self._effect_context.active = pending
            try:
                self.checkpoint(outcome)
            finally:
                self._effect_context.active = None
