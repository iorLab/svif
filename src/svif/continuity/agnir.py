from __future__ import annotations

import hashlib
import json
import os
import re
from dataclasses import asdict, dataclass
from pathlib import Path

from svif.runtime import BindingError, ContinuitySnapshot, OperationOutcome


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

    The adapter supports the published Core/profile `0.1` line and the
    experimental Core/profile `0.2` lineage-aware line. Provider-specific
    lineage and selector semantics stay inside this adapter; the Svif
    Orchestrator remains Continuity-Provider-neutral.
    """

    provider_id = "agnir"
    _SUPPORTED_PROFILES = {
        "0.1": "repository-filesystem/0.1",
        "0.2": "repository-filesystem/0.2",
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

        candidate = (self.project_root / locator).resolve()
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
        discovery = self.project_root / "AGNIR.yaml"
        if not discovery.is_file():
            raise self._fail(
                "AGNIR_DISCOVERY_NOT_FOUND",
                "repository/filesystem profile could not resolve AGNIR.yaml at the Project Entry Point",
            )

        values = self._parse_discovery(discovery.read_text(encoding="utf-8"))
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
        if version == "0.2":
            if not isinstance(lineage_identity, str) or not lineage_identity:
                raise self._fail(
                    "AGNIR_LINEAGE_REQUIRED",
                    "Core 0.2 repository/filesystem discovery requires continuity.lineage",
                )
        else:
            lineage_identity = None

        binding_selector = values.get(
            ("extensions", "agnir/vcs", "lineage_binding", "selector")
        )
        if self.selected_vcs_selector is not None and version == "0.2":
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

        evidence = paths["evidence"]
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

    @staticmethod
    def _read_optional(path: Path | None) -> str | None:
        return None if path is None else path.read_text(encoding="utf-8")

    @staticmethod
    def _read_evidence(path: Path | None) -> dict[str, str]:
        if path is None:
            return {}
        return {
            item.name: item.read_text(encoding="utf-8")
            for item in sorted(path.iterdir())
            if item.is_file()
        }

    def resolve_lineage(self, project_identity: str) -> str | None:
        """Return the selected logical Agnir lineage, if the compatibility line has one."""
        return self._discover(project_identity).lineage_identity

    def load(self, project_identity: str) -> ContinuitySnapshot:
        resolved = self._discover(project_identity)
        return ContinuitySnapshot(
            project_identity=project_identity,
            state=self._read_optional(resolved.state),
            next_actions=self._read_optional(resolved.next_actions),
            decisions=self._read_optional(resolved.decisions),
            evidence=self._read_evidence(resolved.evidence),
        )

    @staticmethod
    def _require_text_update(value: object | None, label: str) -> str | None:
        if value is None:
            return None
        if not isinstance(value, str):
            raise BindingError(f"Agnir filesystem {label} update must be text")
        return value

    @staticmethod
    def _atomic_write(path: Path, content: str) -> None:
        tmp = path.with_name(f".{path.name}.svif-tmp")
        tmp.write_text(content, encoding="utf-8")
        os.replace(tmp, path)

    def checkpoint(self, outcome: OperationOutcome) -> None:
        resolved = self._discover(outcome.project_identity)
        update = outcome.continuity_update

        state = self._require_text_update(update.state, "Current State")
        next_actions = self._require_text_update(update.next_actions, "Next Actions")
        decisions = self._require_text_update(update.decisions, "Decisions")

        if state is not None:
            self._atomic_write(resolved.state, state)
        if next_actions is not None:
            self._atomic_write(resolved.next_actions, next_actions)
        if decisions is not None:
            if resolved.decisions is None:
                raise self._fail(
                    "AGNIR_DISCOVERY_UNRESOLVABLE",
                    "cannot persist Decisions because the Discovery Record has no Decisions locator",
                )
            self._atomic_write(resolved.decisions, decisions)

        if resolved.evidence is not None:
            digest = hashlib.sha256(
                (
                    f"{outcome.project_identity}\0{resolved.lineage_identity or ''}\0"
                    f"{outcome.operation_id}"
                ).encode("utf-8")
            ).hexdigest()[:16]
            evidence_path = resolved.evidence / f"svif-operation-{digest}.json"
            payload = {
                "svif_runtime_checkpoint": "0.1",
                "project_identity": outcome.project_identity,
                "agnir_lineage": resolved.lineage_identity,
                "operation_id": outcome.operation_id,
                "subject_identity": outcome.subject_identity,
                "externally_effectful": outcome.externally_effectful,
                "evidence": [asdict(record) for record in outcome.evidence],
            }
            self._atomic_write(
                evidence_path,
                json.dumps(payload, indent=2, sort_keys=True) + "\n",
            )

        # Do not claim resumability until the resulting locator chain, Project
        # identity, logical lineage, and optional VCS selector binding resolve.
        self._discover(outcome.project_identity)
