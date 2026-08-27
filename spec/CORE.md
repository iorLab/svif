# Svif Core 0.2

**Status:** Working normative specification on the active `0.2` line.

## 1. Purpose

Svif is an execution-environment-independent Project operation protocol. It carries authorized Project work from discovery and planning through change, verification, optional actuation, observation, repair, and durable continuation.

> The Project persists; Executors and execution environments may change.

Svif Core MUST NOT require ChatGPT, an AI agent, Git, GitHub, a repository, local-only or remote-only execution, a specific CI product, Skill packaging, or any provider such as Cloudflare.

ZeroLocal v0.1 remains predecessor evidence on the dedicated legacy branch and MUST NOT be silently relabeled as Svif conformance.

## 2. Core concepts

### Project
The stable unit whose intent, artifacts, policy, evidence, state, and durable continuity survive changes in execution environment.

### Principal
An authority that supplies or owns intent, policy, authorization, approval, external consent, or risk acceptance.

### Executor
An entity that performs Project operations. It MAY be human, AI, CLI, IDE, CI, automation, service, or a composed system.

### Execution Environment
The replaceable surface in which an Executor operates. No Execution Environment becomes authoritative merely because work occurred there.

### Capability Adapter
A semantic boundary connecting Svif to workspace, SCM, verification, delivery, provider, observation, authority, or execution-surface capabilities.

### Trust Boundary
A boundary where authority, protected credentials, billing, destructive effect, production risk, domain/account ownership, or external consent requires a different authorization context or explicit Principal action.

## 3. Agnir continuity dependency

Svif Core requires durable continuity through a declared compatible Agnir Core line.

- Svif MUST depend on Agnir at the protocol layer only.
- Svif MUST NOT require a particular Agnir implementation, backend, adapter, repository layout, VCS, host, or execution-surface integration.
- CHECKPOINT delegates persistence, discovery, and resumability semantics to Agnir.
- Svif MUST NOT define a competing durable Project Memory contract.

The active development target is Agnir Core `0.1`; final release compatibility notation remains subject to Agnir release freeze.

## 4. Lifecycle

The Core lifecycle is:

`DISCOVER -> PLAN -> CHANGE -> VERIFY -> DELIVER -> OBSERVE -> CHECKPOINT`

`REPAIR` returns to the earliest state whose invariant was violated.

A state MAY be skipped only when its semantic effect is not applicable. Skipping a label does not erase an applicable invariant.

### DISCOVER

The Executor MUST identify the Project boundary and intent, load Agnir continuity through normal cold-start discovery, inspect relevant artifacts/policy/external state, identify required capabilities, and surface trust boundaries without requesting protected secret values through unauthorized channels.

Exit evidence: Project identity, current durable state, applicable policy, required capabilities, known blockers, and a working Agnir continuity path are known.

### PLAN

Planning semantics are mandatory before material mutation. The Executor MUST establish:

- bounded intended changes;
- required verification;
- whether DELIVER and OBSERVE apply;
- material trust/authority boundaries;
- candidate/provenance expectations when identity matters;
- repair/rollback considerations when material.

For trivial operations, an implementation MAY coalesce PLAN into its operation trace and MAY omit a separately durable plan artifact when no independent plan evidence is material. It MUST NOT mutate first and retroactively infer the plan.

### CHANGE

The Executor performs authorized change through Project mechanisms or Capability Adapters.

When later verification, delivery, or observation claims depend on material change identity, CHANGE MUST establish a stable, unambiguous candidate identity. The identity MAY be an immutable revision, content digest, versioned object, transaction identity, or another Project-appropriate reference.

### VERIFY

Required checks MUST produce inspectable evidence attributable to the subject actually verified. Verification authority MUST NOT automatically imply protected delivery authority.

A successful claim for subject `A` MUST NOT be used as verification for `B` unless equivalence is independently established under Project policy.

Failure exits to REPAIR or an explicit Trust Boundary.

### DELIVER

DELIVER applies when the operation must actuate change into an external or authoritative target state. It MAY be skipped otherwise.

Delivery MUST identify the subject/candidate actuated and target identity when material. If delivery is verification-gated, the delivered candidate MUST be the verified candidate or a replacement with independent verification evidence.

Profiles MAY expand DELIVER into preparation/provisioning, migration, deploy/publish, release, transaction, or other domain-specific steps.

### OBSERVE

When an externally observable effect is claimed, OBSERVE is mandatory. Successful actuation alone is insufficient evidence of resulting state.

Observation MUST use a Project-appropriate independent signal and SHOULD identify the target and subject/candidate when feasible.

OBSERVE MAY be skipped only when no externally observable effect is claimed.

### REPAIR

Failure MUST be classified by violated invariant/capability boundary rather than Executor identity. Repair MUST return to the earliest responsible layer and MUST use evidence rather than private recollection where durable/inspectable evidence exists.

### CHECKPOINT

At a meaningful work boundary, the Executor SHOULD reconcile durable Project truth through Agnir. Svif MUST NOT claim resumability when Agnir discovery cannot resolve the authoritative resulting state.

## 5. Core invariants

### Evidence-driven transitions
Lifecycle progress is justified by evidence appropriate to the claim, not conversational completion or Executor assertion.

### Stable provenance
Material verification, transformation, delivery, and observation claims MUST reference stable/unambiguous subject identities and preserve derivation when one subject produces another.

### Authority separation
Ability to inspect or verify MUST NOT implicitly grant protected actuation/destructive authority.

### Observable success
Externally claimed effects require resulting-state observation.

### Explicit trust boundaries
Principal action/authority boundaries are modeled explicitly and MUST NOT be misreported as ordinary Project defects.

### Protected secret transport
Svif Core MUST NOT require secret values to be transmitted through unprotected conversational or execution surfaces. References, names, and required scopes MAY be carried.

### Adapter isolation
Provider/tool/environment-specific behavior remains behind adapters/profiles unless independently justified as universal Core semantics.

### Durable continuation
Executor/context replacement MUST NOT destroy resumability when Svif continuity is claimed; this invariant is satisfied through Agnir.

## 6. Standard semantic evidence

Svif defines `evidence-record/0.2` as the machine-readable reference envelope for portable evidence/provenance semantics.

A record identifies:

- Project and operation;
- record kind;
- stable subject identity;
- derivation inputs when applicable;
- target identity when applicable;
- result status;
- producer/adapter identity when available;
- authority reference/class when material;
- evidence locator when inspectable evidence exists;
- timestamp when material.

Serialization is not a Core file-layout requirement. Implementations MAY expose equivalent semantics in APIs, databases, logs, attestations, or other durable evidence systems.

## 7. Capability Adapter semantics

Adapter operation names are extensible. Each operation MUST declare one portable semantic effect from:

`resolve`, `inspect`, `mutate`, `identify`, `verify`, `actuate`, `observe`, `authorize`, `recover`, `checkpoint`.

Profiles MAY require effects and may standardize operation names within their domain. Third-party/provider verbs MUST NOT become Core merely because an adapter wraps them.

## 8. Core repair classes

Implementations SHOULD preserve at least these semantic classes where applicable:

- Project artifact/logic failure;
- dependency/toolchain failure;
- adapter unavailable/unsupported/configuration failure;
- authority required/denied;
- credential unavailable;
- candidate identity/provenance mismatch;
- provider/external account state failure;
- migration/state-transition failure;
- delivery/external integration failure;
- observation/readiness failure;
- Agnir discovery/continuity failure;
- explicit Principal trust-boundary action required.

Adapters/profiles MAY add subcodes while mapping back to a portable class required for repair routing.

## 9. Packaging

Skill, Plugin, CLI, SDK, IDE extension, CI automation, and similar forms are Svif integrations, not Core layers.
