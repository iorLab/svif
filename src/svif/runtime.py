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
    """Required verification is missing, failed, or not independently attested."""


class SessionError(SvifRuntimeError):
    """A session is foreign, already completed, or unsafe to replay."""


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
class CapabilityPolicy:
    """Trusted provider-owned policy; never selected by a result payload."""

    effect: str
    required_authorities: frozenset[str]


@dataclass(frozen=True)
class ContinuitySnapshot:
    project_identity: str
    state: object | None = None
    next_actions: object | None = None
    decisions: object | None = None
    evidence: object | None = None
    revision: str | None = None


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
class WorkResult:
    subject_identity: str
    evidence: tuple[EvidenceRecord, ...] = ()
    capability_request: CapabilityRequest | None = None
    continuity_update: ContinuityUpdate = ContinuityUpdate()
    # Set by untrusted-surface parsers, not accepted from their JSON payloads.
    verification_needs_attestation: bool = False


@dataclass(frozen=True)
class OperationRequest:
    operation_id: str
    intent: str
    authority_grants: frozenset[str] = frozenset()
    # This request is supplied by trusted integration code, not parse_result().
    verification_required: bool = True
    required_verifiers: frozenset[str] = frozenset()


@dataclass(frozen=True)
class OperationOutcome:
    project_identity: str
    operation_id: str
    subject_identity: str
    evidence: tuple[EvidenceRecord, ...]
    externally_effectful: bool
    continuity_update: ContinuityUpdate = ContinuityUpdate()


@dataclass(frozen=True)
class OperationSession:
    """Bound, continuity-loaded operation awaiting execution completion."""

    binding: ProjectBinding
    request: OperationRequest
    context: ExecutionContext


class ContinuityProvider(Protocol):
    provider_id: str

    def load(self, project_identity: str) -> ContinuitySnapshot: ...

    def checkpoint(self, outcome: OperationOutcome, *, expected_revision: str | None = None) -> None: ...


class ExecutionSurface(Protocol):
    """Stable identity for a surface integration.

    A surface may be synchronous (`execute`) or externally driven
    (`begin`/materialize/`complete`) such as a ChatGPT MCP app.
    """

    surface_id: str


class CapabilityProvider(Protocol):
    provider_id: str

    def policy_for(self, operation: str) -> CapabilityPolicy: ...

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
        self._lock = RLock()
        self._sessions: dict[tuple[str, str], tuple[OperationSession, str]] = {}
        # Serializes effects within this Orchestrator. Cross-process integration
        # must also coordinate its target (filesystem providers supply a guard).
        self._completion_lock = RLock()

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

    @staticmethod
    def _names(value: frozenset[str], label: str) -> None:
        if not isinstance(value, frozenset) or any(
            not isinstance(item, str) or not item.strip() or item != item.strip()
            for item in value
        ):
            raise BindingError(f"{label} must be a frozenset of non-empty names")

    def begin(self, binding: ProjectBinding, request: OperationRequest) -> OperationSession:
        """Load durable continuity and bind a single-use operation before execution."""
        for value in (binding.project_identity, request.operation_id, request.intent):
            if not isinstance(value, str) or not value.strip():
                raise BindingError("Project identity, operation identity, and intent are required")
        self._names(request.authority_grants, "authority_grants")
        self._names(request.required_verifiers, "required_verifiers")
        if type(request.verification_required) is not bool:
            raise BindingError("verification_required must be a trusted boolean")
        continuity = self._continuity_for(binding)
        self._surface_for(binding)
        key = (binding.project_identity, request.operation_id)
        with self._lock:
            if key in self._sessions:
                raise SessionError("operation identity already used; reconcile before starting new work")
            snapshot = continuity.load(binding.project_identity)
            if snapshot.project_identity != binding.project_identity:
                raise BindingError("Continuity Provider returned a different Project identity")
            context = ExecutionContext(binding.project_identity, request.operation_id, snapshot)
            session = OperationSession(binding=binding, request=request, context=context)
            self._sessions[key] = (session, "ready")
            return session

    def complete(
        self,
        session: OperationSession,
        work: WorkResult,
        *,
        authority_grants: frozenset[str] = frozenset(),
        verification_evidence: tuple[EvidenceRecord, ...] | None = None,
    ) -> OperationOutcome:
        """Complete only with trusted policy, exact verification and coherent state.

        Grants and verification_evidence are supplied by trusted integration code.
        For parsed ChatGPT results, verification declarations alone are not proof.
        A trusted synchronous execute() implementation may supply its own evidence.
        A pre-effect rejection permits repair on the same session. Once effect or
        checkpoint starts, any failure requires reconciliation, not blind replay.
        """
        key = (session.binding.project_identity, session.request.operation_id)
        with self._lock:
            saved = self._sessions.get(key)
            if saved is None or saved[0] is not session or saved[1] != "ready":
                raise SessionError("foreign, busy, completed, or uncertain operation session")
            self._sessions[key] = (session, "completing")
        started = False
        try:
            self._names(authority_grants, "authority_grants")
            binding, request = session.binding, session.request
            continuity = self._continuity_for(binding)
            if not isinstance(work.subject_identity, str) or not work.subject_identity.strip():
                raise ProvenanceMismatch("Execution Surface returned no stable subject identity")
            self._validate_evidence(work.evidence)
            trusted = verification_evidence
            if trusted is None:
                trusted = () if work.verification_needs_attestation else work.evidence
            self._validate_evidence(trusted)
            if verification_evidence is not None and any(r.kind != "verification" for r in trusted):
                raise BindingError("verification_evidence may contain only verification records")
            # Historical evidence for other subjects does not verify this result.
            for record in (*work.evidence, *trusted):
                if (record.kind == "verification" and record.subject_identity == work.subject_identity
                        and record.status != "succeeded"):
                    raise VerificationFailed("failed, blocked, or unknown verification cannot complete successfully")
            capability_request = work.capability_request
            required = request.verification_required or bool(request.required_verifiers) or capability_request is not None
            if required and not self._successful_verification(trusted, work.subject_identity):
                raise VerificationFailed("required verification needs trusted success evidence for the exact subject")
            producers = {r.producer for r in trusted if r.kind == "verification"
                         and r.subject_identity == work.subject_identity and r.status == "succeeded"}
            if not request.required_verifiers.issubset(producers):
                raise VerificationFailed("not all trusted operation-required verifiers have succeeded")
            evidence = [r for r in work.evidence if not (work.verification_needs_attestation and r.kind == "verification")]
            for record in trusted:
                if record not in evidence:
                    evidence.append(record)
            provider = None
            if capability_request is not None:
                if capability_request.provider not in binding.capabilities:
                    raise BindingError(f"Capability Provider is not bound to this Project: {capability_request.provider}")
                provider = self._capabilities.get(capability_request.provider)
                policy_for = getattr(provider, "policy_for", None)
                if not callable(policy_for):
                    raise BindingError("Capability Provider has no trusted operation policy")
                policy = policy_for(capability_request.operation)
                if not isinstance(policy, CapabilityPolicy) or policy.effect != "actuate":
                    raise BindingError("unsupported or invalid trusted capability policy")
                self._names(policy.required_authorities, "provider required_authorities")
                if capability_request.effect != policy.effect:
                    raise BindingError("capability effect conflicts with trusted operation policy")
                if capability_request.subject_identity != work.subject_identity:
                    raise ProvenanceMismatch("Capability request subject differs from the Execution Surface result subject")
                # Keep the exact-subject invariant explicit at the effect boundary.
                if not self._successful_verification(trusted, work.subject_identity):
                    raise ProvenanceMismatch("external actuation requires successful verification evidence for the exact subject")
                extra = capability_request.authority_class
                if extra is not None and not isinstance(extra, str):
                    raise BindingError("requested authority_class must be text or null")
                required_authorities = policy.required_authorities | (frozenset({extra}) if extra else frozenset())
                effective_authority = request.authority_grants | authority_grants
                if not required_authorities.issubset(effective_authority):
                    raise AuthorityRequired("external actuation requires trusted authority classes: "
                                            + ", ".join(sorted(required_authorities - effective_authority)))
            expected = session.context.continuity.revision
            guard_factory = getattr(continuity, "operation_guard", None)
            guard = guard_factory(binding.project_identity) if callable(guard_factory) else nullcontext()
            with self._completion_lock, guard:
                outcome = OperationOutcome(binding.project_identity, request.operation_id, work.subject_identity,
                                           tuple(evidence), capability_request is not None, work.continuity_update)
                preflight = getattr(continuity, "validate_checkpoint", None)
                if callable(preflight):
                    preflight(outcome, expected_revision=expected)
                if provider is not None:
                    prepare_effect = getattr(continuity, "prepare_effect", None)
                    if callable(prepare_effect):
                        # Persist uncertainty before crossing a non-transactional
                        # boundary. A restart must observe/reconcile, not redeploy.
                        prepare_effect(outcome, capability_request, expected_revision=expected)
                    started = True
                    delivery = provider.actuate(capability_request)
                    self._require_delivery_match(delivery, subject=work.subject_identity,
                                                 target=capability_request.target_identity)
                    evidence.append(delivery)
                    observation = provider.observe(delivery)
                    self._require_observation_match(observation, delivery)
                    evidence.append(observation)
                outcome = OperationOutcome(binding.project_identity, request.operation_id, work.subject_identity,
                                           tuple(evidence), capability_request is not None, work.continuity_update)
                started = True
                if expected is None:
                    continuity.checkpoint(outcome)
                else:
                    continuity.checkpoint(outcome, expected_revision=expected)
            with self._lock:
                self._sessions[key] = (session, "completed")
            return outcome
        except BaseException:
            with self._lock:
                self._sessions[key] = (session, "uncertain" if started else "ready")
            raise

    @staticmethod
    def _validate_evidence(records: tuple[EvidenceRecord, ...]) -> None:
        if not isinstance(records, tuple):
            raise BindingError("evidence must be a tuple of EvidenceRecord values")
        for record in records:
            if (not isinstance(record, EvidenceRecord)
                    or record.kind not in {"candidate", "transformation", "verification", "delivery", "observation", "checkpoint"}
                    or record.status not in {"succeeded", "failed", "blocked", "unknown"}
                    or not isinstance(record.subject_identity, str) or not record.subject_identity.strip()):
                raise BindingError("invalid evidence kind, status, or subject")

    def run(self, binding: ProjectBinding, request: OperationRequest) -> OperationOutcome:
        """Convenience path for an Execution Surface that supports synchronous execute()."""

        session = self.begin(binding, request)
        surface = self._surface_for(binding)
        execute = getattr(surface, "execute", None)
        if not callable(execute):
            raise BindingError(
                f"Execution Surface {binding.execution_surface!r} is externally driven; "
                "use begin()/complete() through its integration bridge"
            )
        work = execute(session.context, request)
        return self.complete(session, work)
