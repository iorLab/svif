from __future__ import annotations

from typing import Protocol

from svif.runtime import BindingError, CapabilityRequest, EvidenceRecord


class CloudflareWorkersTransport(Protocol):
    """Provider-I/O boundary supplied by an integration/distribution layer.

    Implementations may use the Cloudflare API, Wrangler, a remote service, or
    another authorized mechanism. Secret values stay behind this boundary.
    """

    def deploy_worker(self, *, subject_identity: str, target_identity: str) -> None: ...

    def observe_worker(self, *, subject_identity: str, target_identity: str) -> bool: ...


class CloudflareWorkersCapabilityProvider:
    """Svif-facing Cloudflare Workers Capability Provider.

    Authority and exact-subject verification are enforced by the Orchestrator.
    This provider validates the Cloudflare operation boundary, delegates I/O to
    an injected transport, and returns portable delivery/observation evidence.
    """

    provider_id = "cloudflare.workers"

    def __init__(self, transport: CloudflareWorkersTransport) -> None:
        self._transport = transport

    def actuate(self, request: CapabilityRequest) -> EvidenceRecord:
        if request.provider != self.provider_id:
            raise BindingError("Cloudflare provider received a request for another provider")
        if request.operation != "deploy_verified_worker" or request.effect != "actuate":
            raise BindingError("unsupported Cloudflare Workers capability operation")
        if not request.target_identity:
            raise BindingError("Cloudflare Workers delivery requires a stable target identity")

        self._transport.deploy_worker(
            subject_identity=request.subject_identity,
            target_identity=request.target_identity,
        )
        return EvidenceRecord(
            kind="delivery",
            subject_identity=request.subject_identity,
            target_identity=request.target_identity,
            producer=self.provider_id,
        )

    def observe(self, delivery: EvidenceRecord) -> EvidenceRecord:
        if delivery.kind != "delivery" or delivery.producer != self.provider_id:
            raise BindingError("Cloudflare observation requires delivery evidence from this provider")
        if not delivery.target_identity:
            raise BindingError("Cloudflare delivery evidence has no stable target identity")

        observed = self._transport.observe_worker(
            subject_identity=delivery.subject_identity,
            target_identity=delivery.target_identity,
        )
        return EvidenceRecord(
            kind="observation",
            subject_identity=delivery.subject_identity,
            target_identity=delivery.target_identity,
            producer=self.provider_id,
            status="succeeded" if observed else "failed",
        )
