from __future__ import annotations

import unittest

from svif.capabilities.cloudflare import CloudflareWorkersCapabilityProvider
from svif.runtime import BindingError, CapabilityRequest, EvidenceRecord


SUBJECT = "sha256:verified-candidate"
TARGET = "cloudflare://workers/example"


class FakeTransport:
    def __init__(self, *, observed: bool = True) -> None:
        self.observed = observed
        self.deployments: list[tuple[str, str]] = []
        self.observations: list[tuple[str, str]] = []

    def deploy_worker(self, *, subject_identity: str, target_identity: str) -> None:
        self.deployments.append((subject_identity, target_identity))

    def observe_worker(self, *, subject_identity: str, target_identity: str) -> bool:
        self.observations.append((subject_identity, target_identity))
        return self.observed


def request() -> CapabilityRequest:
    return CapabilityRequest(
        provider="cloudflare.workers",
        operation="deploy_verified_worker",
        effect="actuate",
        subject_identity=SUBJECT,
        target_identity=TARGET,
        authority_class="protected-delivery",
    )


class CloudflareCapabilityTests(unittest.TestCase):
    def test_delivery_and_observation_preserve_subject_and_target(self) -> None:
        transport = FakeTransport()
        provider = CloudflareWorkersCapabilityProvider(transport)

        delivery = provider.actuate(request())
        observation = provider.observe(delivery)

        self.assertEqual(transport.deployments, [(SUBJECT, TARGET)])
        self.assertEqual(transport.observations, [(SUBJECT, TARGET)])
        self.assertEqual(delivery.kind, "delivery")
        self.assertEqual(observation.kind, "observation")
        self.assertEqual(observation.status, "succeeded")
        self.assertEqual(delivery.subject_identity, observation.subject_identity)
        self.assertEqual(delivery.target_identity, observation.target_identity)

    def test_failed_external_observation_is_not_success_evidence(self) -> None:
        provider = CloudflareWorkersCapabilityProvider(FakeTransport(observed=False))
        observation = provider.observe(provider.actuate(request()))
        self.assertEqual(observation.status, "failed")

    def test_wrong_operation_is_rejected_before_transport(self) -> None:
        transport = FakeTransport()
        provider = CloudflareWorkersCapabilityProvider(transport)
        bad = CapabilityRequest(
            provider="cloudflare.workers",
            operation="delete_everything",
            effect="actuate",
            subject_identity=SUBJECT,
            target_identity=TARGET,
        )
        with self.assertRaises(BindingError):
            provider.actuate(bad)
        self.assertEqual(transport.deployments, [])

    def test_observation_rejects_foreign_delivery_evidence(self) -> None:
        provider = CloudflareWorkersCapabilityProvider(FakeTransport())
        foreign = EvidenceRecord(
            kind="delivery",
            subject_identity=SUBJECT,
            target_identity=TARGET,
            producer="other.provider",
        )
        with self.assertRaises(BindingError):
            provider.observe(foreign)


if __name__ == "__main__":
    unittest.main()
