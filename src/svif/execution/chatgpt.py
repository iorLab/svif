from __future__ import annotations

import json
from collections.abc import Mapping
from typing import Any

from svif.runtime import (
    BindingError,
    CapabilityRequest,
    ContinuityUpdate,
    EvidenceRecord,
    OperationSession,
    WorkResult,
)


class ChatGPTExecutionSurface:
    """Structured bridge between Svif OperationSessions and ChatGPT app/MCP tools.

    This bridge contains no OpenAI network client. ChatGPT is an externally
    driven surface: an Apps SDK/MCP wrapper can materialize a session as tool
    output, then parse a later tool-call payload into a WorkResult for
    `Orchestrator.complete()`.
    """

    surface_id = "chatgpt"

    @staticmethod
    def _serializable(value: object) -> object:
        try:
            json.dumps(value)
        except TypeError as exc:
            raise BindingError("ChatGPT surface context is not JSON-serializable") from exc
        return value

    @staticmethod
    def _required_string(value: object, label: str) -> str:
        if not isinstance(value, str) or not value:
            raise BindingError(f"ChatGPT result requires non-empty {label}")
        return value

    @staticmethod
    def _optional_string(value: object, label: str) -> str | None:
        if value is None:
            return None
        if not isinstance(value, str):
            raise BindingError(f"ChatGPT result {label} must be a string or null")
        return value

    def materialize(self, session: OperationSession) -> dict[str, Any]:
        """Create the surface-neutral context payload an MCP/App wrapper may return."""

        continuity = session.context.continuity
        return {
            "surface": self.surface_id,
            "project_identity": session.binding.project_identity,
            "operation_id": session.request.operation_id,
            "intent": session.request.intent,
            "bound_capabilities": sorted(session.binding.capabilities),
            "authority_grants": sorted(session.request.authority_grants),
            "continuity": {
                "state": self._serializable(continuity.state),
                "next_actions": self._serializable(continuity.next_actions),
                "decisions": self._serializable(continuity.decisions),
                "evidence": self._serializable(continuity.evidence),
            },
        }

    def parse_result(
        self,
        session: OperationSession,
        payload: Mapping[str, Any],
    ) -> WorkResult:
        """Validate a structured ChatGPT completion payload and produce WorkResult.

        Authority grants are intentionally not accepted from this payload. They
        must come from the trusted app/integration invocation context when
        `Orchestrator.complete()` is called.
        """

        if payload.get("project_identity") != session.binding.project_identity:
            raise BindingError("ChatGPT result Project identity does not match operation session")
        if payload.get("operation_id") != session.request.operation_id:
            raise BindingError("ChatGPT result operation id does not match operation session")

        subject_identity = self._required_string(
            payload.get("subject_identity"), "subject_identity"
        )

        evidence_value = payload.get("evidence", [])
        if not isinstance(evidence_value, list):
            raise BindingError("ChatGPT result evidence must be an array")
        evidence: list[EvidenceRecord] = []
        for item in evidence_value:
            if not isinstance(item, Mapping):
                raise BindingError("ChatGPT evidence record must be an object")
            evidence.append(
                EvidenceRecord(
                    kind=self._required_string(item.get("kind"), "evidence.kind"),
                    subject_identity=self._required_string(
                        item.get("subject_identity"), "evidence.subject_identity"
                    ),
                    status=self._required_string(
                        item.get("status", "succeeded"), "evidence.status"
                    ),
                    target_identity=self._optional_string(
                        item.get("target_identity"), "evidence.target_identity"
                    ),
                    producer=self._optional_string(
                        item.get("producer"), "evidence.producer"
                    ),
                )
            )

        capability_value = payload.get("capability_request")
        capability_request: CapabilityRequest | None = None
        if capability_value is not None:
            if not isinstance(capability_value, Mapping):
                raise BindingError("ChatGPT capability_request must be an object or null")
            capability_request = CapabilityRequest(
                provider=self._required_string(
                    capability_value.get("provider"), "capability_request.provider"
                ),
                operation=self._required_string(
                    capability_value.get("operation"), "capability_request.operation"
                ),
                effect=self._required_string(
                    capability_value.get("effect"), "capability_request.effect"
                ),
                subject_identity=self._required_string(
                    capability_value.get("subject_identity"),
                    "capability_request.subject_identity",
                ),
                target_identity=self._optional_string(
                    capability_value.get("target_identity"),
                    "capability_request.target_identity",
                ),
                authority_class=self._optional_string(
                    capability_value.get("authority_class"),
                    "capability_request.authority_class",
                ),
            )

        continuity_value = payload.get("continuity_update", {})
        if not isinstance(continuity_value, Mapping):
            raise BindingError("ChatGPT continuity_update must be an object")
        continuity_update = ContinuityUpdate(
            state=continuity_value.get("state"),
            next_actions=continuity_value.get("next_actions"),
            decisions=continuity_value.get("decisions"),
        )

        return WorkResult(
            subject_identity=subject_identity,
            evidence=tuple(evidence),
            capability_request=capability_request,
            continuity_update=continuity_update,
        )
