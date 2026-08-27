# Svif Capability Adapter Contract Draft

**Status:** Architecture transition draft; not released conformance text  
**Parent:** `SVIF_ARCHITECTURE_DRAFT.md`

## 1. Purpose

A Capability Adapter connects Svif Core to a concrete capability or external system without making that capability's technology, execution location, or provider semantics part of Core.

Examples include SCM/versioning, artifact/workspace mutation, verification, delivery, provider, observation, authority, and execution-surface integrations.

The contract is semantic. A YAML descriptor is shown as a reference serialization, not a mandatory Core file format.

## 2. Adapter identity

A conforming adapter descriptor MUST identify semantics equivalent to:

```yaml
svif_adapter:
  version: 0.1
adapter:
  id: <stable-adapter-id>
  kind: <adapter-kind>
  implementation: <implementation-id-or-null>
capabilities: {}
authority: {}
evidence: {}
failures: []
```

The adapter ID MUST be stable enough for Project configuration and evidence to identify the adapter being used.

## 3. Adapter kinds

Svif defines these initial semantic adapter kinds:

- `workspace` — read/change Project artifacts;
- `scm` — versioning and candidate identity;
- `verification` — tests/checks/inspection/policy evaluation;
- `delivery` — actuation/publication/deployment/release;
- `provider` — provider-specific resources and operations;
- `observation` — external resulting-state evidence;
- `authority` — protected approval/credential/consent surfaces;
- `execution_surface` — integration with a workspace/agent/IDE/CLI/automation environment.

An adapter MAY implement more than one kind when the boundaries remain explicit. A monolithic implementation MUST still expose the semantic capability/authority/evidence/failure boundaries expected by Svif.

## 4. Capability declarations

`capabilities` MUST declare the operations the adapter can perform or support.

Capability names SHOULD be verbs or verb phrases with stable semantics. The first draft vocabulary includes:

- `detect` — determine whether the capability/system applies to the Project;
- `inspect` — read current configuration/state;
- `change` — modify Project or external state;
- `identify_candidate` — resolve a stable candidate identity;
- `verify` — produce verification evidence;
- `prepare` — prepare prerequisites;
- `provision` — discover/create/update resources;
- `migrate` — perform ordered durable state transitions;
- `deliver` — actuate a candidate or target state;
- `discover_target` — resolve delivery/observation target;
- `observe` — produce resulting-state evidence;
- `recover` — classify and route repair/recovery;
- `checkpoint` — adapter-specific persistence action when relevant, without replacing Agnir continuity.

Adapters MUST NOT claim unsupported capabilities merely because an underlying provider product offers them in some configuration.

## 5. Authority declaration

An adapter MUST declare the authority required for protected operations.

The semantic model SHOULD distinguish:

- unprivileged inspection/read authority;
- mutation authority;
- verification authority;
- protected delivery/production authority;
- destructive-operation authority;
- billing/account/domain/consent authority;
- required credential references and minimum scope descriptions.

Reference shape:

```yaml
authority:
  operations:
    verify:
      level: untrusted-or-project-policy
    deliver:
      level: protected
  credentials:
    - name: <credential-reference-name>
      purpose: <purpose>
      minimum_scope: <scope-description>
      value_transport: protected-store-only
  trust_boundaries:
    - id: <boundary-id>
      operation: <operation>
      principal_action: <required-action>
```

Secret values MUST NOT be required in the descriptor. An adapter MAY reference a protected secret store or identity binding.

## 6. Evidence contract

An adapter that supports `verify`, `deliver`, or `observe` MUST declare what evidence it can produce and how that evidence is bound to a Project candidate or target state.

Evidence semantics SHOULD include:

- `candidate_identity` — accepted input identity form(s);
- `result_identity` — identity of the object/state actually verified or actuated;
- `target_identity` — environment/resource/endpoint identity when applicable;
- `status` — success/failure/blocked/unknown semantics;
- `evidence_locator` — durable or inspectable location/reference when available;
- `observed_at` — timestamp when material;
- `provenance` — relation between candidate, produced artifact, delivery, and observed state.

An adapter MUST NOT report a verified/delivered/observed success for candidate `A` using evidence that only identifies candidate `B`, unless it can prove the two are equivalent under Project policy.

## 7. Failure contract

Adapters MUST surface failures in semantic classes that let Svif route `REPAIR` to the responsible layer.

The initial cross-adapter failure classes are:

- `ADAPTER_UNAVAILABLE`;
- `ADAPTER_UNSUPPORTED_CAPABILITY`;
- `ADAPTER_CONFIGURATION_INVALID`;
- `AUTHORITY_REQUIRED`;
- `AUTHORITY_DENIED`;
- `CREDENTIAL_UNAVAILABLE`;
- `EXTERNAL_ACCOUNT_STATE`;
- `DEPENDENCY_TOOLCHAIN`;
- `PROVISIONING_FAILURE`;
- `MIGRATION_FAILURE`;
- `DELIVERY_FAILURE`;
- `OBSERVATION_FAILURE`;
- `CANDIDATE_IDENTITY_FAILURE`;
- `PROVENANCE_MISMATCH`;
- `EXTERNAL_INTEGRATION_FAILURE`;
- `TRANSIENT_EXTERNAL_FAILURE`;
- `DESTRUCTIVE_ACTION_REQUIRES_PRINCIPAL`.

Adapters MAY define provider/domain-specific subcodes, but MUST map them to a Svif semantic class when a Core/profile implementation depends on portable recovery behavior.

## 8. Idempotency and retry declaration

For state-changing capabilities, an adapter SHOULD declare retry semantics:

```yaml
retry:
  provision: idempotent | guarded | unsafe | unknown
  migrate: idempotent | guarded | unsafe | unknown
  deliver: idempotent | guarded | unsafe | unknown
```

`idempotent` means the same intended operation can be repeated safely.

`guarded` means the adapter can detect prior completion/current state and avoid unsafe duplication.

`unsafe` means repeat execution may cause duplicate/destructive effects and requires explicit coordination or Principal approval.

`unknown` MUST be treated conservatively until the behavior is established.

## 9. Observation declaration

Adapters that can produce external observation SHOULD declare:

- target discovery mechanism;
- observation methods;
- readiness/health semantics;
- candidate/version visibility if available;
- bounded retry/timeout behavior;
- distinction between provider control-plane success and externally observed application/service success.

Observation MUST NOT be synthesized from a delivery command's success when an independent resulting-state check is required by Svif or an active profile.

## 10. Adapter composition

Multiple adapters MAY compose one Svif operation.

Example software delivery path:

```text
workspace adapter
      -> scm adapter
      -> verification adapter
      -> provider/delivery adapter
      -> observation adapter
```

Composition MUST preserve candidate identity and evidence relationships across boundaries.

If one adapter transforms candidate `A` into artifact `B`, the evidence chain MUST record enough provenance to determine that verified `A` produced delivered `B`.

## 11. Execution-surface adapters

ChatGPT Skills, local CLIs, IDE extensions, CI orchestration, and other user/executor surfaces are `execution_surface` integrations.

They MAY orchestrate other adapters but MUST NOT redefine Svif Core semantics.

An execution-surface adapter SHOULD:

- load the Project's Agnir continuity before material operation;
- expose Principal trust-boundary requirements without requesting secret values through unauthorized channels;
- preserve candidate/evidence provenance across delegated tools;
- checkpoint durable Project truth through Agnir at meaningful boundaries;
- make environment-specific limitations explicit.

## 12. Provider adapter specialization

A provider adapter is a Capability Adapter with provider-specific resource and delivery semantics.

The ZeroLocal v0.1 hooks map as follows:

| ZeroLocal provider hook | Svif capability |
|---|---|
| `detect` | `detect` |
| `capabilities` | descriptor `capabilities` |
| `credentials` | descriptor `authority.credentials` |
| `scaffold` | `change` / `prepare` |
| `validate` | `verify` or verification requirements |
| `provision` | `provision` |
| `migrate` | `migrate` |
| `deploy` | `deliver` |
| `endpoint` | `discover_target` |
| `verify` | `observe` when proving resulting external state |
| `recover` | `recover` + failure taxonomy |

This mapping preserves predecessor implementation knowledge while removing Cloudflare/Skill assumptions from the generic contract.

## 13. Minimal conformance expectations

A Capability Adapter draft implementation is testable when it can demonstrate:

1. stable adapter identity and kind;
2. truthful capability declaration;
3. authority/credential requirements without secret values;
4. candidate/evidence input/output semantics where relevant;
5. portable failure mapping;
6. retry/idempotency semantics for state-changing operations;
7. target/observation semantics when external effects are claimed;
8. evidence-preserving composition with at least one other adapter when composition is required.

## 14. Open items before normative freeze

- final adapter kind vocabulary;
- whether capability operation names are Core-normative or profile-extensible;
- exact machine-readable schema and versioning rules;
- standard evidence envelope shape;
- standard adapter invocation/result envelope versus implementation-specific APIs;
- whether authority semantics belong entirely in adapter descriptors or partly in a separate Svif authority contract;
- conformance rules for adapters that wrap third-party tools whose behavior/version changes independently.
