from __future__ import annotations

from contextlib import nullcontext
from dataclasses import dataclass
from threading import RLock
from typing import Protocol


class SvifRuntimeError(RuntimeError):
    """Base error for Svif orchestration failures."""


class BindingError(SvifRuntimeError):
    """A declared Project binding cannot be resolved or is inconsistent."""


class AuthorityRequired(SvifRuntimeError):
    """An effect requires authority that the current operation does not hold."""


class ProvenanceMismatch(SvifRuntimeError):
    """Evidence/candidate identity does not justify the requested transition."""


class VerificationFailed(ProvenanceMismatch):
    """Required verification did not succeed for the exact completion subject."""


class SessionConsumed(BindingError):
    """A completion was replayed, forged, or belongs to another Orchestrator."""


class DeliveryFailed(SvifRuntimeError):
    """The external delivery failed or its outcome is uncertain."""


class ObservationFailed(SvifRuntimeError):
    """Independent resulting-state observation was unavailable."""


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
    check_id: str | None = None

    def __post_init__(self) -> None:
        if self.kind not in {"candidate", "transformation", "verification", "delivery", "observation", "checkpoint"}:
            raise BindingError("unsupported evidence kind")
        if self.status not in {"succeeded", "failed", "blocked", "unknown"}:
            raise BindingError("unsupported evidence status")
        if not isinstance(self.subject_identity, str) or not self.subject_identity.strip():
            raise BindingError("evidence requires a stable subject identity")


@dataclass(frozen=True)
class ContinuitySnapshot:
    project_identity: str
    state: object | None = None
    next_actions: object | None = None
    decisions: object | None = None
    evidence: object | None = None
    revision: str | None = None
    pending_effect: object | None = None


@dataclass(frozen=True)
class ContinuityUpdate:
    """Provider-neutral durable-truth update returned by an Execution Surface.

    Values are opaque to the Orchestrator. A concrete Continuity Provider
    validates and serializes the values it supports.
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
class CapabilityPolicy:
    """Trusted provider metadata, never read from a WorkResult."""

    operation: str
    effect: str
    authority_classes: frozenset[str]


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
    verification_required: bool = True
    required_checks: frozenset[str] = frozenset()
    verification_not_applicable_reason: str | None = None

    def __post_init__(self) -> None:
        if not isinstance(self.operation_id, str) or not self.operation_id.strip():
            raise BindingError("operation_id must be non-empty")
        for label, values in (("authority_grants", self.authority_grants), ("required_checks", self.required_checks)):
            if not isinstance(values, frozenset) or any(not isinstance(x, str) or not x.strip() for x in values):
                raise BindingError(f"{label} must contain non-empty trusted names")
        if type(self.verification_required) is not bool:
            raise BindingError("verification_required must be a trusted boolean")
        if not self.verification_required and (
            self.required_checks or not isinstance(self.verification_not_applicable_reason, str) or not self.verification_not_applicable_reason.strip()
        ):
            raise BindingError("verification exemption requires a reason and no required checks")


@dataclass(frozen=True)
class OperationOutcome:
    project_identity: str
    operation_id: str
    subject_identity: str
    evidence: tuple[EvidenceRecord, ...]
    externally_effectful: bool
    continuity_update: ContinuityUpdate = ContinuityUpdate()
    expected_revision: str | None = None
    target_identity: str | None = None


@dataclass(frozen=True)
class OperationSession:
    """Bound, continuity-loaded operation awaiting execution completion."""

    binding: ProjectBinding
    request: OperationRequest
    context: ExecutionContext


class ContinuityProvider(Protocol):
    provider_id: str

    def load(self, project_identity: str) -> ContinuitySnapshot: ...

    def checkpoint(self, outcome: OperationOutcome) -> None: ...


class ExecutionSurface(Protocol):
    """Stable identity for a surface integration.

    A surface may be synchronous (`execute`) or externally driven
    (`begin`/materialize/`complete`) such as a ChatGPT MCP app.
    """

    surface_id: str


class CapabilityProvider(Protocol):
    provider_id: str

    def operation_policy(self, operation: str) -> CapabilityPolicy: ...

    def actuate(self, request: CapabilityRequest) -> EvidenceRecord: ...

    def observe(self, delivery: EvidenceRecord) -> EvidenceRecord: ...


class Orchestrator:
    """Minimal executable Svif product kernel.

    `run()` supports synchronous Execution Surfaces. `begin()` + `complete()`
    support externally driven surfaces where the host (for example ChatGPT via
    an MCP/App integration) calls into Svif rather than being invoked by Svif.
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
        self._sessions: dict[int, OperationSession] = {}
        self._session_lock = RLock()

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

    def _continuity_for(self, binding: ProjectBinding) -> object:
        provider = self._continuity.get(binding.continuity.provider)
        if provider is None:
            raise BindingError(f"unavailable Continuity Provider: {binding.continuity.provider}")
        return provider

    def _surface_for(self, binding: ProjectBinding) -> object:
        surface = self._surfaces.get(binding.execution_surface)
        if surface is None:
            raise BindingError(f"unavailable Execution Surface: {binding.execution_surface}")
        return surface

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

    def begin(self, binding: ProjectBinding, request: OperationRequest) -> OperationSession:
        """Load durable continuity and bind an operation before surface execution."""

        continuity = self._continuity_for(binding)
        self._surface_for(binding)

        snapshot = continuity.load(binding.project_identity)
        if snapshot.project_identity != binding.project_identity:
            raise BindingError("Continuity Provider returned a different Project identity")

        context = ExecutionContext(
            project_identity=binding.project_identity,
            operation_id=request.operation_id,
            continuity=snapshot,
        )
        session = OperationSession(binding=binding, request=request, context=context)
        with self._session_lock:
            self._sessions[id(session)] = session
        return session

    def complete(
        self,
        session: OperationSession,
        work: WorkResult,
        *,
        authority_grants: frozenset[str] = frozenset(),
    ) -> OperationOutcome:
        """Reconcile an externally/synchronously produced WorkResult and checkpoint.

        `authority_grants` is supplied by a trusted integration layer. An
        untrusted model/result payload cannot grant itself protected authority.
        """

        # Consume once before effects. A failed/uncertain delivery must be reconciled,
        # not blindly repeated by calling complete() again.
        with self._session_lock:
            if self._sessions.pop(id(session), None) is not session:
                raise SessionConsumed("operation session is foreign or already consumed")
        binding = session.binding
        request = session.request
        continuity = self._continuity_for(binding)

        if not isinstance(work.subject_identity, str) or not work.subject_identity.strip():
            raise ProvenanceMismatch("Execution Surface returned no stable subject identity")
        evidence = list(work.evidence)
        checks = [r for r in evidence if r.kind == "verification" and r.subject_identity == work.subject_identity]
        if any(r.status != "succeeded" for r in checks):
            raise VerificationFailed("failed/blocked/unknown verification cannot checkpoint completion")
        required = request.verification_required or work.capability_request is not None
        if required and not self._successful_verification(tuple(checks), work.subject_identity):
            raise VerificationFailed("completion requires successful verification for the exact subject")
        if not request.required_checks.issubset({r.check_id for r in checks}):
            raise VerificationFailed("not all trusted required checks succeeded for the exact subject")

        capability_request = work.capability_request
        provider = None
        if capability_request is not None:
            if capability_request.provider not in binding.capabilities:
                raise BindingError(f"Capability Provider is not bound to this Project: {capability_request.provider}")
            provider = self._capabilities.get(capability_request.provider)
            if provider is None:
                raise BindingError(f"unavailable Capability Provider: {capability_request.provider}")
            resolver = getattr(provider, "operation_policy", None)
            if not callable(resolver):
                raise BindingError("Capability Provider has no trusted operation policy")
            policy = resolver(capability_request.operation)
            if not isinstance(policy, CapabilityPolicy) or (
                policy.operation != capability_request.operation
                or policy.effect != capability_request.effect or policy.effect != "actuate"
                or not isinstance(policy.authority_classes, frozenset)
                or any(not isinstance(a, str) or not a.strip() for a in policy.authority_classes)
            ):
                raise BindingError("missing/inconsistent trusted capability operation policy")
            if capability_request.subject_identity != work.subject_identity:
                raise ProvenanceMismatch("Capability request subject differs from the Execution Surface result subject")
            # external actuation requires successful verification evidence for the exact subject
            effective_authority = request.authority_grants | authority_grants
            required_authority = policy.authority_classes
            if capability_request.authority_class:
                required_authority |= frozenset({capability_request.authority_class})
            missing = required_authority - effective_authority
            if missing:
                raise AuthorityRequired(f"external actuation requires authority classes: {sorted(missing)}")

        preliminary = OperationOutcome(
            project_identity=binding.project_identity, operation_id=request.operation_id,
            subject_identity=work.subject_identity, evidence=tuple(evidence),
            externally_effectful=capability_request is not None,
            continuity_update=work.continuity_update,
            expected_revision=session.context.continuity.revision,
            target_identity=capability_request.target_identity if capability_request else None,
        )
        # A filesystem provider holds its cross-process lock from preflight through
        # delivery/observation/checkpoint, and rejects stale contexts before effects.
        guard = getattr(continuity, "operation_guard", None)
        with guard(preliminary) if callable(guard) else nullcontext():
            if capability_request is not None:
                try:
                    delivery = provider.actuate(capability_request)
                except SvifRuntimeError:
                    raise
                except Exception as exc:
                    raise DeliveryFailed("external delivery failed; reconcile before retry") from exc
                self._require_delivery_match(delivery, subject=work.subject_identity, target=capability_request.target_identity)
                evidence.append(delivery)
                try:
                    observation = provider.observe(delivery)
                except SvifRuntimeError:
                    raise
                except Exception as exc:
                    raise ObservationFailed("independent observation unavailable; effect remains unconfirmed") from exc
                self._require_observation_match(observation, delivery)
                evidence.append(observation)
            outcome = OperationOutcome(
                project_identity=binding.project_identity, operation_id=request.operation_id,
                subject_identity=work.subject_identity, evidence=tuple(evidence),
                externally_effectful=capability_request is not None,
                continuity_update=work.continuity_update,
                expected_revision=session.context.continuity.revision,
            target_identity=capability_request.target_identity if capability_request else None,
            )
            continuity.checkpoint(outcome)
            return outcome

    def run(self, binding: ProjectBinding, request: OperationRequest) -> OperationOutcome:
        """Convenience path for an Execution Surface that supports synchronous execute()."""

        surface = self._surface_for(binding)
        execute = getattr(surface, "execute", None)
        if not callable(execute):
            raise BindingError(
                f"Execution Surface {binding.execution_surface!r} is externally driven; "
                "use begin()/complete() through its integration bridge"
            )
        session = self.begin(binding, request)
        try:
            work = execute(session.context, request)
            return self.complete(session, work)
        finally:
            with self._session_lock:
                self._sessions.pop(id(session), None)
