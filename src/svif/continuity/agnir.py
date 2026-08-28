from __future__ import annotations

import hashlib
import json
import os
import re
from dataclasses import asdict
from pathlib import Path

from svif.runtime import BindingError, ContinuitySnapshot, OperationOutcome


class AgnirDiscoveryError(BindingError):
    """Agnir discovery/profile failure preserving the Agnir semantic failure code."""

    def __init__(self, code: str, message: str) -> None:
        super().__init__(f"{code}: {message}")
        self.code = code


class AgnirFilesystemContinuityProvider:
    """Agnir `repository-filesystem/0.1` Continuity Provider for Svif.

    The Project root is the authorized Project Entry Point. This adapter
    intentionally implements only Agnir's current repository/filesystem profile;
    that profile is not part of the generic Svif Orchestrator contract.
    """

    provider_id = "agnir"
    _CORE_VERSION = "0.1"
    _PROFILE = "repository-filesystem/0.1"

    def __init__(self, project_root: str | Path) -> None:
        self.project_root = Path(project_root).resolve()

    @staticmethod
    def _strip_scalar(value: str) -> str | None:
        value = value.strip()
        if value in {"null", "Null", "NULL", "~"}:
            return None
        if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
            return value[1:-1]
        return value

    @classmethod
    def _parse_discovery(cls, text: str) -> dict[tuple[str, str], str | None]:
        """Parse only the scalar subset required by repository-filesystem/0.1.

        This is deliberately not a general YAML parser. Unsupported YAML forms
        fail later as missing/inconsistent required semantics rather than being
        guessed by the adapter.
        """

        values: dict[tuple[str, str], str | None] = {}
        section: str | None = None
        for raw in text.splitlines():
            if not raw.strip() or raw.lstrip().startswith("#"):
                continue
            top = re.match(r"^([A-Za-z0-9_/-]+):\s*$", raw)
            if top:
                section = top.group(1)
                continue
            if section is None:
                continue
            scalar = re.match(r"^\s{2}([A-Za-z0-9_/-]+):\s*(.*?)\s*$", raw)
            if scalar:
                values[(section, scalar.group(1))] = cls._strip_scalar(scalar.group(2))
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

    def _discover(self, project_identity: str) -> dict[str, Path | None]:
        discovery = self.project_root / "AGNIR.yaml"
        if not discovery.is_file():
            raise self._fail(
                "AGNIR_DISCOVERY_NOT_FOUND",
                "repository/filesystem profile could not resolve AGNIR.yaml at the Project Entry Point",
            )

        values = self._parse_discovery(discovery.read_text(encoding="utf-8"))

        if values.get(("agnir", "version")) != self._CORE_VERSION:
            raise self._fail(
                "AGNIR_DISCOVERY_UNSUPPORTED_VERSION",
                f"expected Agnir Core {self._CORE_VERSION}",
            )
        if values.get(("agnir", "discovery_profile")) != self._PROFILE:
            raise self._fail(
                "AGNIR_DISCOVERY_INCONSISTENT",
                f"expected discovery profile {self._PROFILE}",
            )

        discovered_identity = values.get(("project", "identity"))
        if discovered_identity != project_identity:
            raise self._fail(
                "AGNIR_DISCOVERY_PROJECT_MISMATCH",
                f"expected {project_identity!r}, discovered {discovered_identity!r}",
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

        return paths

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

    def load(self, project_identity: str) -> ContinuitySnapshot:
        paths = self._discover(project_identity)
        return ContinuitySnapshot(
            project_identity=project_identity,
            state=self._read_optional(paths["state"]),
            next_actions=self._read_optional(paths["next_actions"]),
            decisions=self._read_optional(paths["decisions"]),
            evidence=self._read_evidence(paths["evidence"]),
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
        paths = self._discover(outcome.project_identity)
        update = outcome.continuity_update

        state = self._require_text_update(update.state, "Current State")
        next_actions = self._require_text_update(update.next_actions, "Next Actions")
        decisions = self._require_text_update(update.decisions, "Decisions")

        if state is not None:
            self._atomic_write(paths["state"], state)
        if next_actions is not None:
            self._atomic_write(paths["next_actions"], next_actions)
        if decisions is not None:
            if paths["decisions"] is None:
                raise self._fail(
                    "AGNIR_DISCOVERY_UNRESOLVABLE",
                    "cannot persist Decisions because the Discovery Record has no Decisions locator",
                )
            self._atomic_write(paths["decisions"], decisions)

        evidence_dir = paths["evidence"]
        if evidence_dir is not None:
            digest = hashlib.sha256(
                f"{outcome.project_identity}\0{outcome.operation_id}".encode("utf-8")
            ).hexdigest()[:16]
            evidence_path = evidence_dir / f"svif-operation-{digest}.json"
            payload = {
                "svif_runtime_checkpoint": "0.1",
                "project_identity": outcome.project_identity,
                "operation_id": outcome.operation_id,
                "subject_identity": outcome.subject_identity,
                "externally_effectful": outcome.externally_effectful,
                "evidence": [asdict(record) for record in outcome.evidence],
            }
            self._atomic_write(
                evidence_path,
                json.dumps(payload, indent=2, sort_keys=True) + "\n",
            )

        # Do not claim resumability until the resulting locator chain resolves.
        self._discover(outcome.project_identity)
