# Svif Software Delivery Profile 0.2

**Profile identifier:** `software-delivery/0.2`

This profile specializes Svif Core for software that is built, validated, migrated, provisioned, deployed, published, or otherwise delivered to an external/authoritative target.

It preserves the strongest ZeroLocal delivery invariants without making Git, GitHub, remote CI, ChatGPT, Skills, Cloudflare, or any other provider universal Core requirements.

## 1. Candidate identity

Every candidate presented as verified or delivered MUST have a stable, unambiguous identity. For Git-based Projects, a full immutable commit SHA is the RECOMMENDED strong realization.

Mutable branch names, mutable tags, working-directory descriptions, or conversational claims alone are insufficient when they can resolve to different content over time.

## 2. Verification attribution

Required checks MUST execute against an identified candidate/subject and produce evidence attributable to that subject.

A successful check of `A` MUST NOT verify `B` unless equivalence is independently established.

Verification MAY execute in any location; execution location alone is not conformance.

## 3. Delivery specialization

Svif Core `DELIVER` may expand into:

`PREPARE/PROVISION -> MIGRATE -> DEPLOY/PUBLISH`

Applicable substates may not be skipped merely because the implementation uses one provider command to combine them.

### Preparation/provisioning

Resource discovery SHOULD precede creation where practical. Resource changes SHOULD be idempotent or guarded when replay is plausible. Destructive replacement/deletion, billing/account/domain changes, and similar high-risk effects may require Principal authorization.

### Migration

Durable state transitions MUST be ordered when ordering affects correctness. They SHOULD be replay-safe or guarded against duplicate execution. Migration failure must be distinguishable from source/application failure when evidence supports that distinction.

### Deploy/publish

When delivery is verification-gated, the actuated candidate MUST equal the verified candidate unless the replacement is independently verified.

Mutable aliases MAY trigger delivery, but final evidence SHOULD resolve the actual immutable/unambiguous subject delivered when the target system exposes such identity.

State-sensitive concurrent delivery operations MUST be serialized or otherwise coordinated when concurrency could race migrations, corrupt state, or make provenance ambiguous.

## 4. Authority and secrets

Untrusted/lower-trust verification contexts MUST NOT automatically receive protected production authority.

Secret values MUST remain inside authorized protected stores/channels. Workflows may communicate credential names, references, required scopes, and setup/approval actions without values.

## 5. Observation

A successful deployment/provider API response alone is insufficient when production/external success is claimed. Resulting state MUST be independently observed through Project-appropriate evidence such as health/readiness checks, external fetches, version endpoints, provider deployment state, resource queries, or smoke/integration checks.

Observation SHOULD identify target and delivered subject/version when feasible.

## 6. Provider isolation

Provider behavior belongs behind Capability Adapters. Provider-specific resource names, API semantics, account behavior, and deployment verbs MUST NOT redefine Svif Core or this profile unless generalized independently.

## 7. Repair

Failure classification SHOULD distinguish source/build/test, dependency/toolchain, SCM/versioning authority, credentials, provider/account state, provisioning, migration, delivery, routing/external integration, readiness/health, provenance mismatch, Agnir continuity, and explicit Principal trust-boundary action.

Repair returns to the earliest violated invariant and re-establishes evidence before continuing.

## 8. Profile conformance identifiers

- `SVIF-SD-PROV-001` stable candidate identity
- `SVIF-SD-PROV-002` verification attribution
- `SVIF-SD-PROV-003` exact verified-candidate delivery
- `SVIF-SD-AUTH-001` verification/delivery authority separation
- `SVIF-SD-SECRET-001` protected secret transport
- `SVIF-SD-DELIVER-001` safe state-sensitive concurrency
- `SVIF-SD-OBSERVE-001` observable success
- `SVIF-SD-ADAPTER-001` provider isolation
- `SVIF-SD-REPAIR-001` evidence-based repair

These are new Svif identifiers; predecessor `ZL-*` identifiers are historical evidence only.
