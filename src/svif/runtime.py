from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol


class SvifRuntimeError(RuntimeError):
    """Base error for Svif orchestration failures."""


class BindingError(SvifRuntimeError):
    """A declared Project binding cannot be resolved or is inconsistent."""


class AuthorityRequired(SvifRuntimeError):
    """An effect requires authority that the current operation does not hold."""


class ProvenanceMismatch(SvifRuntimeError):
    """Evidence/candidate identity does not justify the requested transition."""


class ObservationMismatch(SvifRuntimeError):
    """Observed resulting state does not correspond to the delivered subject/target."""


@dataclass(frozen=True)
class ProviderBinding:
    provider: str


@dataclass(frozen=True)
class ProjectBinding:
    project_identity: str
    continuity: ProviderBinding
    execution_surface: str
    capabilities: frozenset[str] = frozenset()


@dataclass(frozen=True)
class EvidenceRecord:
    kind: str
    subject_identity: str
    status: str = "succeeded"
    target_identity: str | None = None
    producer: str | None = None


@dataclass(frozen=True)
class ContinuitySnapshot:
    project_identity: str
    state: object | None = None
    next_actions: object | None = None
    decisions: object | None = None
    evidence: object | None = None


@dataclass(frozen=True)
class ContinuityUpdate:
    """Provider-neutral durable-truth update returned by an Execution Surface.

    Values are intentionally opaque to the Orchestrator. A concrete Continuity
    Provider validates and serializes the values it supports.
    """

    state: object | None = None
    next_actions: object | None = None
    decisions: object | None = None


@dataclass(frozen=True)
class ExecutionContext:
    project_identity: str
    operation_id: str
    continuity: ContinuitySnapshot


@dataclass(frozen=True)
class CapabilityRequest:
    provider: str
    operation: str
    effect: str
    subject_identity: str
    target_identity: str | None = None
    authority_class: str | None = None


@dataclass(frozen=True)
class WorkResult:
    subject_identity: str
    evidence: tuple[EvidenceRecord, ...] = ()
    capability_request: CapabilityRequest | None = None
    continuity_update: ContinuityUpdate = ContinuityUpdate()


@dataclass(frozen=True)
class OperationRequest:
    operation_id: str
    intent: str
    authority_grants: frozenset[str] = frozenset()


@dataclass(frozen=True)
class OperationOutcome:
    project_identity: str
    operation_id: str
    subject_identity: str
    evidence: tuple[EvidenceRecord, ...]
    externally_effectful: bool
    continuity_update: ContinuityUpdate = ContinuityUpdate()


class ContinuityProvider(Protocol):
    provider_id: str

    def load(self, project_identity: str) -> ContinuitySnapshot: ...

    def checkpoint(self, outcome: OperationOutcome) -> None: ...


class ExecutionSurface(Protocol):
    surface_id: str

    def execute(self, context: ExecutionContext, request: OperationRequest) -> WorkResult: ...


class CapabilityProvider(Protocol):
    provider_id: str

    def actuate(self, request: CapabilityRequest) -> EvidenceRecord: ...

    def observe(self, delivery: EvidenceRecord) -> EvidenceRecord: ...


class Orchestrator:
    """Minimal executable Svif product kernel.

    The kernel coordinates replaceable Continuity Providers, Execution Surfaces,
    and Capability Providers. Concrete Agnir, ChatGPT, and Cloudflare bindings
    live outside this class.
    """

    def __init__(
        self,
        *,
        continuity_providers: tuple[ContinuityProvider, ...] = (),
        execution_surfaces: tuple[ExecutionSurface, ...] = (),
        capability_providers: tuple[CapabilityProvider, ...] = (),
    ) -> None:
        self._continuity = self._index(continuity_providers, "provider_id", "Continuity Provider")
        self._surfaces = self._index(execution_surfaces, "surface_id", "Execution Surface")
        self._capabilities = self._index(capability_providers, "provider_id", "Capability Provider")

    @staticmethod
    def _index(items: tuple[object, ...], attr: str, label: str) -> dict[str, object]:
        result: dict[str, object] = {}
        for item in items:
            identity = getattr(item, attr, None)
            if not isinstance(identity, str) or not identity:
                raise BindingError(f"{label} has no stable identity")
            if identity in result:
                raise BindingError(f"duplicate {label} identity: {identity}")
            result[identity] = item
        return result

    @staticmethod
    def _successful_verification(evidence: tuple[EvidenceRecord, ...], subject: str) -> bool:
        return any(
            record.kind == "verification"
            and record.status == "succeeded"
            and record.subject_identity == subject
            for record in evidence
        )

    @staticmethod
    def _require_delivery_match(
        delivery: EvidenceRecord,
        *,
        subject: str,
        target: str | None,
    ) -> None:
        if (
            delivery.kind != "delivery"
            or delivery.status != "succeeded"
            or delivery.subject_identity != subject
            or delivery.target_identity != target
        ):
            raise ProvenanceMismatch(
                "Capability Provider did not return successful delivery evidence "
                "for the requested subject/target"
            )

    @staticmethod
    def _require_observation_match(observation: EvidenceRecord, delivery: EvidenceRecord) -> None:
        if (
            observation.kind != "observation"
            or observation.status != "succeeded"
            or observation.subject_identity != delivery.subject_identity
            or observation.target_identity != delivery.target_identity
        ):
            raise ObservationMismatch(
                "observation does not match the successfully delivered subject/target"
            )

    def run(self, binding: ProjectBinding, request: OperationRequest) -> OperationOutcome:
        continuity = self._continuity.get(binding.continuity.provider)
        if continuity is None:
            raise BindingError(f"unavailable Continuity Provider: {binding.continuity.provider}")

        surface = self._surfaces.get(binding.execution_surface)
        if surface is None:
            raise BindingError(f"unavailable Execution Surface: {binding.execution_surface}")

        snapshot = continuity.load(binding.project_identity)
        if snapshot.project_identity != binding.project_identity:
            raise BindingError("Continuity Provider returned a different Project identity")

        context = ExecutionContext(
            project_identity=binding.project_identity,
            operation_id=request.operation_id,
            continuity=snapshot,
        )
        work = surface.execute(context, request)
        if not work.subject_identity:
            raise ProvenanceMismatch("Execution Surface returned no stable subject identity")

        evidence = list(work.evidence)
        externally_effectful = False

        capability_request = work.capability_request
        if capability_request is not None:
            externally_effectful = True

            if capability_request.provider not in binding.capabilities:
                raise BindingError(
                    f"Capability Provider is not bound to this Project: {capability_request.provider}"
                )
            provider = self._capabilities.get(capability_request.provider)
            if provider is None:
                raise BindingError(f"unavailable Capability Provider: {capability_request.provider}")

            if capability_request.effect != "actuate":
                raise BindingError(
                    "minimal Svif kernel supports only an actuate request at the external-effect boundary"
                )

            if capability_request.subject_identity != work.subject_identity:
                raise ProvenanceMismatch(
                    "Capability request subject differs from the Execution Surface result subject"
                )

            if not self._successful_verification(tuple(evidence), work.subject_identity):
                raise ProvenanceMismatch(
                    "external actuation requires successful verification evidence for the exact subject"
                )

            required_authority = capability_request.authority_class
            if required_authority and required_authority not in request.authority_grants:
                raise AuthorityRequired(
                    f"external actuation requires authority class: {required_authority}"
                )

            delivery = provider.actuate(capability_request)
            self._require_delivery_match(
                delivery,
                subject=work.subject_identity,
                target=capability_request.target_identity,
            )
            evidence.append(delivery)

            observation = provider.observe(delivery)
            self._require_observation_match(observation, delivery)
            evidence.append(observation)

        outcome = OperationOutcome(
            project_identity=binding.project_identity,
            operation_id=request.operation_id,
            subject_identity=work.subject_identity,
            evidence=tuple(evidence),
            externally_effectful=externally_effectful,
            continuity_update=work.continuity_update,
        )

        continuity.checkpoint(outcome)
        return outcome
