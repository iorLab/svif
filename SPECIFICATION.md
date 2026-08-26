# ZeroLocal Specification v0.1

**Status:** Working Draft  
**Canonical repository:** `iorLab/zerolocal`  
**Current delivery form:** Skills  
**Long-term product form:** Installable plugin after stabilization  
**First provider reference:** `iorLab/zerolocal-cloudflare-starter`

## 1. Purpose

ZeroLocal is a repository-first, AI-operated software-delivery protocol. A conforming project provides a complete normal path for implementation, validation, delivery, observation, repair, and durable project-state recovery without requiring the human operator to maintain a local checkout, local project toolchain, local git workflow, or local deployment CLI.

Local development MAY exist, but it MUST NOT be the only supported path for any lifecycle step claimed as ZeroLocal.

ZeroLocal v0.1 consists of three separable layers:

1. **Protocol** — provider-neutral roles, lifecycle, contracts, trust boundaries, and conformance rules defined here.
2. **Core Skill** — procedural orchestration that translates user intent into protocol-compliant repository operations.
3. **Provider Skill** — provider-specific implementation of the Provider Adapter Contract. Cloudflare is the first reference provider.

The plugin is not part of the v0.1 delivery target. It is a later distribution shell gated on skill stabilization.

## 2. Normative language and roles

`MUST`, `MUST NOT`, `SHOULD`, `SHOULD NOT`, and `MAY` are normative requirement levels.

Roles:

- **Human Operator** — owns intent, judgment, account authority, secrets, billing, and explicit production-risk approvals.
- **Agent Operator** — inspects and changes repository state, runs remote verification/delivery paths, diagnoses failures, repairs repository-owned causes, and checkpoints durable state.
- **Canonical Repository** — authoritative source for code, configuration, automation, durable history, and Repository Project Memory (RPM) when used.
- **Verification Environment** — remote environment that validates an immutable repository revision.
- **Delivery Environment** — remote environment that actuates a release of an immutable repository revision.
- **Provider Adapter** — provider-specific behavior invoked by Core only when provider work is required.

## 3. Architecture and authority

The six logical layers are:

`Human Governance -> Agent -> Repository Control Plane -> Verification & Delivery -> Provider Adapter -> Production Observation`.

Authority rules:

- The repository **MUST** be the canonical project filesystem and durable operating record.
- Secret values **MUST NOT** be committed to the repository, RPM, chat, or other transient prompt context.
- Human account-owner actions at explicit trust boundaries do not violate ZeroLocal.
- Repository write authority and production authority **SHOULD** be separable.
- CI verifies; deployment actuates. A successful deployment command by itself is not production-success evidence.

## 4. Protocol lifecycle

The normative lifecycle is:

`BOOTSTRAP -> IMPLEMENT -> VERIFY -> PROVISION -> DEPLOY -> OBSERVE -> CHECKPOINT`

`REPAIR/ITERATE` is a recovery state reachable from any executable state after failure evidence is available. It returns to the earliest state whose invariant was violated.

### 4.1 BOOTSTRAP

Entry: repository intent is known or can be resolved.

The Agent Operator MUST:

- resolve the canonical repository;
- read repository instructions and RPM manifest when present;
- load referenced state, next steps, and decisions;
- inspect project structure, validation/delivery automation, provider declarations, and outstanding failures;
- identify trust-boundary prerequisites without requesting secret values.

Exit evidence: repository identity, current immutable revision, operating state, required remote checks, and provider status are known.

### 4.2 IMPLEMENT

Entry: the requested change and repository authority are understood.

The Agent Operator MUST make material source/configuration/automation changes through repository-native interfaces and MUST preserve durable repository history.

Exit evidence: an immutable candidate revision exists.

### 4.3 VERIFY

Entry: candidate revision exists.

Required project checks MUST run remotely. Results MUST be attributable to the immutable candidate revision. Failure evidence MUST be remotely inspectable.

Exit: successful required checks, or `REPAIR/ITERATE`.

### 4.4 PROVISION

Entry: verified revision requires provider resources or state transitions.

Provisioning MUST be provider-adapter-owned, SHOULD be idempotent, and MUST surface human trust-boundary requirements separately from repository defects.

This state MAY be skipped when no provisioning is required.

### 4.5 DEPLOY

Entry: required verification and provisioning gates are satisfied.

A production deployment MUST identify the immutable revision being released. If delivery is validation-gated, the deployed revision MUST equal the validated revision unless the replacement revision is separately validated. Untrusted validation contexts MUST NOT gain production credentials or authority.

Concurrent production operations MUST be serialized or otherwise coordinated when concurrency could corrupt state, race migrations, or make provenance ambiguous.

### 4.6 OBSERVE

Entry: a deployment or externally observable state change occurred.

Production success requires observable verification appropriate to the system, such as health/readiness checks, endpoint assertions, or equivalent provider evidence. A successful deploy command alone is insufficient.

Exit: observable success, or `REPAIR/ITERATE`.

### 4.7 REPAIR/ITERATE

Failures MUST be classified at least as one of:

- code/build/test;
- dependency/toolchain;
- repository permissions;
- missing/invalid protected secret;
- provider permissions/account state;
- infrastructure provisioning;
- migration/state transition;
- routing/DNS/external integration;
- production health/readiness.

Repository-owned failures MUST be repaired through the repository-native path. Trust-boundary failures MUST produce precise human action requirements without requesting secret values in chat and without defaulting to local debugging.

### 4.8 CHECKPOINT

Entry: a meaningful work boundary is reached.

The Agent Operator SHOULD persist changed project status, completed work, unresolved blockers, next steps, and durable decisions to RPM or an explicitly declared equivalent. The next fresh context SHOULD be able to resume from repository state alone.

## 5. Core Contract families

### 5.1 Lifecycle Contract

**ZL-LIFECYCLE-001** A conforming workflow MUST implement the lifecycle and evidence rules in section 4.  
**ZL-LIFECYCLE-002** State transitions MUST be evidence-driven rather than inferred from conversational completion.  
**ZL-LIFECYCLE-003** Failures MUST transition to `REPAIR/ITERATE` or a documented human trust boundary.

### 5.2 Repository Contract

**ZL-REPO-001** The project MUST designate a canonical repository.  
**ZL-REPO-002** Normal implementation and repository repair MUST be possible through repository-native interfaces without human local checkout.  
**ZL-REPO-003** Material implementation and operating changes MUST have durable history.  
**ZL-REPO-004** Required validation/delivery automation MUST be versioned in the repository unless an external policy object is explicitly referenced.

### 5.3 RPM Contract

RPM is the standard durable-memory profile for the official skills.

**ZL-RPM-001** `.chatgpt/project-memory.yaml` or an explicitly declared equivalent MUST identify the project, canonical repository, and durable state files.  
**ZL-RPM-002** The manifest MUST reference current state and next steps and SHOULD reference durable decisions.  
**ZL-RPM-003** A fresh Agent context SHOULD load RPM at the first substantive project turn.  
**ZL-RPM-004** Checkpoint MUST NOT persist secret values.  
**ZL-RPM-005** RPM content MUST be sufficient to resume without founding-chat context.

Minimum official layout:

```text
.chatgpt/
  project-memory.yaml
  state.yaml
  next-steps.md
  decisions.md
```

### 5.4 CI Contract

**ZL-CI-001** Project-relevant changes MUST have a remote validation path.  
**ZL-CI-002** Validation results MUST identify the immutable revision tested.  
**ZL-CI-003** Failed checks MUST expose remotely inspectable status/log evidence.  
**ZL-CI-004** Untrusted change validation MUST be isolated from production secrets and production authority.  
**ZL-CI-005** A retry/recovery path SHOULD remain remotely invokable.

### 5.5 Deployment Contract

**ZL-DEPLOY-001** Production delivery MUST be remotely executable without human local deployment tooling.  
**ZL-DEPLOY-002** Every production deployment MUST identify an immutable repository revision.  
**ZL-DEPLOY-003** Validation-gated production MUST deploy the exact validated revision.  
**ZL-DEPLOY-004** Provisioning/delivery SHOULD be safe to retry for the same intended state.  
**ZL-DEPLOY-005** State-sensitive production operations MUST be coordinated when concurrent execution could make state or provenance unsafe.  
**ZL-DEPLOY-006** Production success MUST include observable post-deploy verification.  
**ZL-DEPLOY-007** Human production approval MAY be required as a trust boundary.

### 5.6 Trust Boundary Contract

**ZL-TRUST-001** Secret values MUST remain in protected repository/provider secret stores.  
**ZL-TRUST-002** The workflow MUST NOT request secret values in chat.  
**ZL-TRUST-003** Credential names, minimum scopes, and setup actions MAY be communicated.  
**ZL-TRUST-004** Credentials SHOULD use least privilege.  
**ZL-TRUST-005** Account ownership, billing, consent, provider authorization, domain ownership, and protected-environment approval MAY remain explicit human actions.  
**ZL-TRUST-006** Provider/account failures MUST be distinguishable from repository/code failures.

### 5.7 Provider Adapter Contract

Each provider implementation MUST declare a machine-readable provider descriptor and procedural skill capable of satisfying these hooks:

1. `detect` — recognize provider configuration and readiness;
2. `capabilities` — declare supported runtimes/resources/features;
3. `credentials` — name required credentials and minimum scopes without values;
4. `scaffold` — create provider-owned repository configuration/automation;
5. `validate` — state provider-relevant validation requirements;
6. `provision` — discover/create/update provider resources idempotently where practical;
7. `migrate` — apply ordered durable state transitions when applicable;
8. `deploy` — release a specific immutable revision;
9. `endpoint` — discover the externally observable deployment endpoint or equivalent target;
10. `verify` — prove production readiness/health;
11. `recover` — classify provider failures and prescribe repository repair or precise trust-boundary action.

A provider descriptor MUST include at least:

```yaml
version: 1
provider:
  id: provider-id
  capabilities: {}
  credentials: []
  delivery:
    validation_workflow: path-or-reference
    deployment_workflow: path-or-reference
    revision_source: immutable-revision-expression
    verification_path: path-or-equivalent
trust_boundaries: []
```

Provider-specific implementation details MUST NOT become Core invariants merely because the first reference provider uses them.

## 6. Core Skill procedural interface

The official ZeroLocal Core Skill implements this agent-facing procedure:

`Initialize -> Plan -> Implement -> Verify -> Deliver -> Observe -> Checkpoint`

This is not a second protocol lifecycle. It is the procedural interface that maps user intent onto lifecycle states:

| Skill procedure | Protocol states |
|---|---|
| Initialize | BOOTSTRAP |
| Plan | BOOTSTRAP / IMPLEMENT preparation |
| Implement | IMPLEMENT |
| Verify | VERIFY / REPAIR/ITERATE |
| Deliver | PROVISION / DEPLOY / REPAIR/ITERATE |
| Observe | OBSERVE / REPAIR/ITERATE |
| Checkpoint | CHECKPOINT |

Core MUST delegate provider-specific work through a compatible Provider Skill and MUST preserve protocol invariants across that delegation.

## 7. Cloudflare reference profile

`iorLab/zerolocal-cloudflare-starter` is the executable Cloudflare reference/golden fixture. It MUST demonstrate at minimum:

- repository-backed RPM;
- remote CI for pull requests and release-branch pushes;
- separation of untrusted validation from production authority;
- `CLOUDFLARE_API_TOKEN` and `CLOUDFLARE_ACCOUNT_ID` in protected repository secrets;
- trusted production delivery after successful validation;
- checkout/deployment of the exact validated SHA;
- serialized production runs;
- Worker endpoint discovery;
- automated `/health` or equivalent post-deploy verification;
- manual remote recovery for an explicitly identified immutable revision.

D1 is an optional v0.1 capability. When used, creation/migration behavior MUST be idempotent or safely replayable and production migration ordering MUST be explicit.

## 8. Conformance evidence

Conformance is evidence-based.

**Repository-static evidence** includes protocol/RPM/provider manifests, workflow definitions, secret-name declarations, source/configuration, validation commands, and documented trust boundaries.

**Live operational evidence** includes CI results attributed to a SHA, deployment logs, deployed revision identity, provider resource status, endpoint discovery, and health/readiness results.

A repository cannot claim live deployment conformance solely from static workflow files. Conversely, provider credentials or live access are not required to inspect static contract conformance.

## 9. Skill v0.1 Definition of Done

Skill v0.1 is complete when:

1. this specification defines lifecycle, seven contracts, provider adapter hooks, trust boundaries, evidence, and the Core procedural mapping;
2. the Cloudflare reference repository implements the provider descriptor, remote validation, exact-tested-revision deployment, and production verification path;
3. `skills/zerolocal-core/SKILL.md` can bootstrap/resume a project from repository/RPM state and execute the complete procedural interface without founding-chat knowledge;
4. `skills/cloudflare-provider/SKILL.md` implements the Provider Adapter Contract without leaking Cloudflare semantics into Core;
5. repository/project and provider conformance checklists exist;
6. remaining failures that require account ownership or secrets are documented as trust-boundary prerequisites rather than hidden implementation work.

This Definition of Done establishes **Skill v0.1 implementation completeness**, not stabilization. Plugin work remains gated until clean-room validation succeeds on at least two new non-founding real projects, preferably 2-3, and recurring failure modes have reusable recovery strategies.

## 10. Non-goals for v0.1

- broad multi-provider support;
- Plugin packaging, marketplace distribution, or onboarding UX;
- requiring projects to fork the Cloudflare reference fixture;
- standardizing a specific application framework or language;
- moving secrets into chat or repository plaintext;
- eliminating optional local development.

## 11. Compatibility and evolution

Cloudflare is the sole reference provider for v0.1. Provider neutrality is an architectural boundary, not a claim that multiple providers have already passed conformance.

Changes to lifecycle semantics, trust-boundary invariants, provider hooks, or exact-revision delivery semantics require a durable RPM decision and specification revision. Skills MUST identify the specification version they implement.
