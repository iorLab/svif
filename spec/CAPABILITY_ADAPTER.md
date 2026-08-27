# Svif Capability Adapter 0.2

**Reference schema:** `schemas/capability-adapter.schema.json`

A Capability Adapter connects Svif semantics to a concrete capability or external system without making that system's implementation, location, product vocabulary, or provider semantics part of Core.

## 1. Adapter kinds

The initial portable kinds are:

- `workspace`
- `scm`
- `verification`
- `delivery`
- `provider`
- `observation`
- `authority`
- `execution_surface`

An adapter MAY declare more than one kind when each operation's boundary remains explicit.

## 2. Operation semantics

Adapter operation names are implementation/profile-extensible. Every operation MUST map to exactly one Core semantic effect:

- `resolve` — resolve a Project/capability/target/resource binding;
- `inspect` — read current state without intended mutation;
- `mutate` — change Project or external state;
- `identify` — establish stable candidate/artifact/target identity;
- `verify` — produce verification evidence;
- `actuate` — deliver/publish/deploy/migrate/provision or otherwise cause intended external/authoritative effect;
- `observe` — independently read resulting state;
- `authorize` — obtain/validate/route protected authority or Principal approval;
- `recover` — classify/repair capability-specific failure;
- `checkpoint` — adapter-specific persistence action that does not replace Agnir.

A profile may require a narrower named operation vocabulary while preserving these effects.

## 3. Authority

Each state-changing/protected operation SHOULD declare an authority class:

- `none`
- `read`
- `mutation`
- `verification`
- `protected-delivery`
- `destructive`
- `principal-action`

Credential declarations carry references/purpose/minimum scope, not secret values. `value_transport` is `none`, `protected-store-only`, or `adapter-managed`.

Verification capability MUST NOT imply protected delivery authority.

## 4. Evidence

Operations that `identify`, `verify`, `actuate`, or `observe` SHOULD declare the evidence-record kinds they consume/produce and the subject/target identity forms they support.

An adapter MUST NOT report success for subject `A` using evidence for `B` unless Project policy establishes equivalent identity.

## 5. Failure mapping

Portable adapter failure classes are:

- `ADAPTER_UNAVAILABLE`
- `ADAPTER_UNSUPPORTED_CAPABILITY`
- `ADAPTER_CONFIGURATION_INVALID`
- `AUTHORITY_REQUIRED`
- `AUTHORITY_DENIED`
- `CREDENTIAL_UNAVAILABLE`
- `EXTERNAL_ACCOUNT_STATE`
- `DEPENDENCY_TOOLCHAIN`
- `STATE_TRANSITION_FAILURE`
- `DELIVERY_FAILURE`
- `OBSERVATION_FAILURE`
- `CANDIDATE_IDENTITY_FAILURE`
- `PROVENANCE_MISMATCH`
- `EXTERNAL_INTEGRATION_FAILURE`
- `TRANSIENT_EXTERNAL_FAILURE`
- `DESTRUCTIVE_ACTION_REQUIRES_PRINCIPAL`

Provider/domain-specific subcodes MAY be added, but portable repair behavior MUST map to a class above when Core/profile orchestration depends on it.

## 6. Retry/idempotency

State-changing operations SHOULD declare one of:

- `idempotent`
- `guarded`
- `unsafe`
- `unknown`

`unknown` is treated conservatively. `unsafe` requires explicit coordination and may require Principal approval before replay.

## 7. Composition

When adapters compose, evidence MUST preserve subject identity and derivation across boundaries. A transformation from source `A` to artifact `B` records `B` with `derived_from: [A]`; verification/delivery/observation records then reference the actual subject they concern.

Execution-surface integrations may orchestrate adapters but MUST NOT redefine Svif Core semantics.
