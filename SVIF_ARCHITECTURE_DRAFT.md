# Svif v0.2 Architecture Transition Draft

**Status:** Architecture transition draft; not a released conformance specification  
**Predecessor:** ZeroLocal Specification v0.1  
**Durable-continuity dependency:** Agnir Core 0.1 line (draft target)

## 1. Purpose

Svif is an execution-environment-independent protocol for carrying Project operations from intent through change, verification, delivery, observation, repair, and durable continuation.

Svif is built around one stable rule:

> The Project persists; Executors and execution environments may change.

A Svif-conforming Core MUST NOT require ChatGPT, GitHub, Git, a particular AI agent, a conversational interface, a local-or-remote execution distinction, or ChatGPT Skill packaging.

ZeroLocal v0.1 remains the historical predecessor specification. Existing ZeroLocal validation evidence remains valid as predecessor evidence and MUST NOT be silently relabeled as Svif conformance.

## 2. Relationship to Agnir

Svif requires durable Project continuity through **Agnir Core**.

The dependency is normative at the protocol layer and implementation-neutral:

- Svif depends on a declared compatible Agnir Core version line.
- Svif MUST NOT require the Agnir reference implementation, a repository backend, Git, GitHub, ChatGPT, or any particular Agnir adapter.
- Any Agnir implementation MAY satisfy Svif's continuity dependency if it conforms to the required Agnir Core contract.
- Agnir remains independently useful without Svif.

For the current transition draft, Svif targets the **Agnir Core 0.1** line. The exact release compatibility expression is frozen only when both draft contracts are stable enough for conformance testing.

Svif delegates durable continuity semantics to Agnir rather than redefining Project Memory, discovery, or checkpoint persistence.

## 3. Core concepts and roles

### 3.1 Project

A **Project** is the stable unit whose intent, artifacts, state, policy, evidence, and durable continuity survive changes in execution environment.

A repository MAY be a Project substrate or an important Project resource, but repository identity is not Svif Core identity.

### 3.2 Principal

A **Principal** is an authority that supplies or owns intent, policy, approval, account authority, or risk acceptance for Project operations.

A Principal MAY be a person, organization, policy system, or composed authority model.

### 3.3 Executor

An **Executor** performs Project operations.

An Executor MAY be a human, AI agent, CLI, IDE, automation, CI runner, service, or composed system. Svif Core MUST NOT depend on the Executor being conversational or AI-based.

### 3.4 Execution Environment

An **Execution Environment** is the surface in which an Executor operates, such as a local workspace, hosted development environment, ChatGPT Project, IDE, CI system, cloud runner, or automation service.

No Execution Environment becomes authoritative merely because work occurred there.

### 3.5 Capability Adapter

A **Capability Adapter** connects Svif Core to an external capability without making the capability's implementation details normative Core semantics.

Examples include SCM, verification, delivery, provider, observation, workspace, and execution-surface adapters.

### 3.6 Trust Boundary

A **Trust Boundary** is a point where authority, secrets, billing, protected resources, production risk, or external consent require a different authorization context or explicit Principal action.

Trust-boundary behavior MUST be modeled explicitly rather than misclassified as implementation failure.

## 4. Architecture

Svif v0.2 uses six logical layers:

1. **Authority & Intent** — Principal intent, policy, approvals, and trust boundaries.
2. **Project Continuity** — Agnir Core discovery, current state, decisions, next actions, and checkpoint continuity.
3. **Operation Core** — lifecycle orchestration, candidate identity, failure routing, and operation invariants.
4. **Verification & Evidence** — evidence-producing checks attributable to a stable candidate or target state.
5. **Capability Adapters** — SCM, provider, delivery, observation, workspace, and other environment-specific behavior.
6. **External Observation** — independent observation of the intended resulting state when an externally observable effect is claimed.

This replaces the predecessor architecture that made Human, Agent, Repository Control Plane, and remote delivery surfaces first-class Core assumptions.

## 5. Lifecycle

The generalized Svif lifecycle is:

`DISCOVER -> PLAN -> CHANGE -> VERIFY -> DELIVER -> OBSERVE -> CHECKPOINT`

`REPAIR` is a recovery state reachable after failure evidence is available. It returns to the earliest state whose invariant was violated.

States MAY be skipped only when their semantic effect is not required for the current operation. Skipping MUST NOT erase an applicable invariant.

### 5.1 DISCOVER

Entry: an authorized Project Entry Point is available.

The Executor MUST:

- identify the Project boundary and current operation intent;
- load the Project's Agnir state through the required Agnir cold-start discovery path;
- inspect relevant Project artifacts, policies, automation, adapters, external state, and known blockers;
- identify applicable trust boundaries without requesting protected values through an unauthorized channel;
- determine which capabilities are required for the operation.

Exit evidence: Project identity, current durable state, applicable policy, required capabilities, known blockers, and a working Agnir continuity path are known.

### 5.2 PLAN

The Executor MUST translate intent and current Project state into a bounded operation plan that identifies expected changes, verification evidence, delivery/observation requirements, trust boundaries, and rollback or repair considerations when material.

A plan MAY be lightweight for trivial operations. Svif does not require a separate planning artifact for every change.

### 5.3 CHANGE

The Executor performs the authorized Project change through available capability adapters or direct Project mechanisms.

Material changes MUST produce a stable candidate identity sufficient for later evidence attribution. A stable candidate MAY be an immutable revision, content digest, versioned document/object, transaction identity, or another project-appropriate immutable or unambiguous reference.

Svif Core does not require Git or a repository commit as the candidate identity.

### 5.4 VERIFY

Required checks MUST produce inspectable evidence attributable to the stable candidate or target state being verified.

A claim MUST NOT advance from completed change to verified change without independent evidence appropriate to the Project.

Untrusted validation contexts MUST NOT implicitly acquire protected delivery authority merely because they can verify a candidate.

Failure exits to `REPAIR` or a documented Trust Boundary.

### 5.5 DELIVER

`DELIVER` applies when the operation must actuate a change into an external or authoritative target state.

Delivery MUST identify the candidate or state being actuated. When delivery is validation-gated, the delivered candidate MUST be the verified candidate unless a replacement candidate is separately verified.

Preparation, provisioning, migration, publication, deployment, release, or other domain-specific delivery steps MAY be expanded by profiles/adapters beneath this state.

Operations that do not require external actuation MAY skip `DELIVER`.

### 5.6 OBSERVE

When an operation claims an externally observable effect, success MUST include observation appropriate to that effect. A successful actuation command alone is insufficient evidence of the resulting state.

Observation MAY use health checks, endpoint assertions, state reads, provider evidence, rendered artifacts, transaction status, or another independent Project-appropriate signal.

Operations with no externally observable effect MAY skip this state.

### 5.7 REPAIR

Failures MUST be classified according to the violated invariant or capability boundary rather than the identity of the Executor.

At minimum, a Svif implementation SHOULD distinguish:

- Project artifact / logic failure;
- dependency or toolchain failure;
- capability-adapter failure;
- authorization / permission failure;
- protected-secret or credential availability failure;
- provider / external-account state failure;
- state-transition / migration failure;
- delivery / routing / external-integration failure;
- observation / readiness failure;
- Agnir discovery / continuity failure;
- Principal trust-boundary action required.

Repair MUST occur at the earliest responsible layer. Agnir discovery failures are repaired in the continuity/discovery layer, not by replaying private Executor history.

### 5.8 CHECKPOINT

At a meaningful work boundary, the Executor SHOULD reconcile durable Project truth through Agnir.

Svif CHECKPOINT MUST delegate persistence and resumability semantics to the applicable Agnir Core contract. Svif MAY require additional operation evidence to be stored, but MUST NOT create a second competing durable-memory model.

A Svif operation MUST NOT claim resumability when the Agnir discovery path cannot resolve the authoritative resulting state.

## 6. Core invariants retained from ZeroLocal

The following predecessor ideas survive the architecture generalization, but with platform-neutral semantics:

### 6.1 Evidence-driven transitions

Lifecycle progress is determined by evidence, not by conversational completion or Executor assertion.

### 6.2 Candidate provenance

Verification and delivery MUST be attributable to a stable candidate identity. The ZeroLocal requirement for an exact Git SHA becomes one strong software/SCM realization of this more general invariant.

### 6.3 Verification/delivery authority separation

Ability to validate a candidate MUST NOT automatically imply authority to actuate protected external state.

### 6.4 Observable success

When external state change is claimed, successful actuation alone is insufficient; resulting state must be observed.

### 6.5 Explicit trust boundaries

Account authority, billing, protected credentials, external consent, destructive operations, and production-risk approval MAY require explicit Principal action. These are not automatically Project defects.

Protected secret values MUST remain inside authorized protected channels/stores. Svif Core MUST NOT require secret values to be passed through an unprotected conversational or execution surface.

### 6.6 Adapter isolation

Provider- or environment-specific behavior MUST remain outside provider/environment-neutral Core unless repeated evidence demonstrates a genuinely general invariant.

### 6.7 Durable continuity

Executor replacement, context loss, or workspace changes MUST NOT destroy Project resumability when Svif continuity is claimed. This invariant is satisfied through Agnir rather than a Svif-specific RPM contract.

## 7. What moves out of Core

The following ZeroLocal v0.1 concepts are no longer Svif Core requirements:

- a canonical Git repository as the Project itself;
- repository-native interfaces as the only valid mutation path;
- remote execution as intrinsically preferable to local execution;
- a required human-local-checkout prohibition as the defining conformance property;
- ChatGPT Projects or fresh conversations as normative concepts;
- Agent Operator / Human Operator role identities;
- ChatGPT Core Skill / Provider Skill packaging;
- `.chatgpt/project-memory.yaml` or any specific Agnir serialization;
- Git SHA as the only possible immutable candidate identity;
- Cloudflare or any provider-specific provisioning model.

These MAY remain valid profiles, adapters, implementation choices, or historical validation fixtures.

## 8. Capability model

Svif Core MAY use these capability classes without requiring any specific implementation:

- **Continuity** — Agnir Core;
- **Artifact / Workspace** — read and modify Project artifacts;
- **SCM / Versioning** — optional version-control capabilities;
- **Verification** — tests, builds, checks, inspections, or policy evaluation;
- **Delivery** — publication, deployment, release, migration, transaction, or other actuation;
- **Provider** — external infrastructure/service-specific capability;
- **Observation** — externally verify resulting state;
- **Authority** — approvals, credentials, consent, protected actions.

Adapters SHOULD declare capabilities, required authority, supported evidence, and failure semantics in machine-readable form where practical.

## 9. Software delivery profile mapping

The ZeroLocal lifecycle remains a valid software-delivery specialization of Svif:

| ZeroLocal v0.1 | Svif v0.2 Core |
|---|---|
| `BOOTSTRAP` | `DISCOVER` |
| implicit planning | `PLAN` |
| `IMPLEMENT` | `CHANGE` |
| `VERIFY` | `VERIFY` |
| `PROVISION` + `DEPLOY` | `DELIVER` |
| `OBSERVE` | `OBSERVE` |
| `REPAIR/ITERATE` | `REPAIR` |
| `CHECKPOINT` | `CHECKPOINT` via Agnir |

A future **Svif Software Delivery Profile** MAY preserve explicit `PROVISION` and `DEPLOY` substates, SCM revision semantics, CI policy, provider descriptors, and exact-tested-revision delivery rules without making those requirements universal Svif Core.

## 10. Packaging and integrations

`Skill`, `Plugin`, CLI, SDK, IDE extension, CI automation, and other product forms are integrations of Svif rather than Svif protocol layers.

The predecessor `ZeroLocal Core Skill` should evolve into a **ChatGPT Svif integration** only after the new Core contract is stable enough to implement. Provider Skills become provider adapters and, where useful, execution-surface-specific integration wrappers.

Packaging remains gated during the architecture transition.

## 11. Conformance and evidence lineage

ZeroLocal v0.1 conformance and clean-room validation evidence remain historical evidence for requirements discovery.

They do not prove Svif v0.2 conformance because the new protocol changes the Project, Executor, continuity, lifecycle, and capability boundaries.

Future Svif conformance MUST test at least:

- Agnir cold-start discovery from a fresh Executor;
- operation execution across a declared execution environment without relying on predecessor-private context;
- evidence attribution to stable candidate identity;
- explicit trust-boundary handling;
- adapter isolation;
- observable external success when external effects are claimed;
- durable checkpoint/resume through Agnir;
- at least one execution/storage arrangement materially different from the founding ChatGPT + GitHub + Cloudflare path.

## 12. Migration order

The migration should proceed in this order:

1. stabilize Agnir Core 0.1 discovery/continuity semantics;
2. freeze Svif's Agnir compatibility declaration;
3. convert this architecture draft into a normative Svif specification draft;
4. define the Svif Software Delivery Profile from retained ZeroLocal invariants;
5. replace RPM-specific Svif conformance requirements with Agnir conformance requirements;
6. rename manifests, skills/integrations, conformance identifiers, and repository/public branding only after compatibility rules are explicit;
7. update the Cloudflare reference as a provider/software-delivery profile implementation rather than Svif Core;
8. resume Validation Project #2 against the Svif + Agnir contracts.
