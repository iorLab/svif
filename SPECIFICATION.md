# ZeroLocal Specification v0.1

**Status:** Working Draft  
**Canonical repository:** `iorLab/zerolocal`  
**Official product direction:** installable ZeroLocal plugin/orchestrator  
**First provider reference fixture:** `iorLab/zerolocal-cloudflare-starter`  
**Founding case study:** `mattamior/awesome-fame-slider`

## 1. Abstract

ZeroLocal defines a repository-first operating model for software development in which a human operator can direct normal implementation, validation, release, and repository-side recovery without requiring a local project checkout, local package/build toolchain, local git commands, or a local deployment CLI.

ZeroLocal does not prohibit local development. It specifies the existence and integrity of a complete remote path. A maintainer may still clone a repository or run tools locally, but doing so is not a prerequisite for the normal supported workflow.

The ZeroLocal project intends to operationalize this model as an **installable, provider-neutral orchestration plugin**. A user should be able to install ZeroLocal, state that a project should use ZeroLocal mode, and enter the repository/RPM/validation/recovery workflow. Deployment provider selection is a later concern inside that workflow: Cloudflare, Vercel, AWS, or another provider is selected or resolved only when provider-specific delivery behavior is needed.

The model assumes an authorized AI/operator can work directly with the canonical repository, remote automation provides reproducible validation and delivery, durable project state is stored outside transient chat context, secrets remain inside protected secret stores, and failures can be diagnosed from remote evidence.

This document defines the provider-neutral ZeroLocal Core, provisional optional profiles, the official plugin/orchestration model, and the boundary for provider-specific flows. Provider-specific deployment behavior is not part of ZeroLocal Core.

## 2. Normative language

The key words **MUST**, **MUST NOT**, **REQUIRED**, **SHOULD**, **SHOULD NOT**, and **MAY** in this document are to be interpreted as normative requirement levels.

Each normative requirement has a stable draft identifier such as `ZL-CORE-001`. Identifiers are intended to support future automated conformance checks. Requirement text may still change while v0.1 remains a Working Draft.

## 3. Scope and product layers

ZeroLocal specifies an operating system around a software repository, not an application framework, programming language, cloud provider, AI model, or source-control vendor.

A ZeroLocal system consists of at least:

- a **Human Operator** who supplies intent, judgment, authorization, provider choices when needed, and trust-boundary approvals;
- an **AI/Repository Operator** authorized to inspect and modify project state through repository-native interfaces;
- a **Canonical Repository** containing source, configuration, automation, durable history, and project-operating state;
- a **Remote Validation Environment** that can build/test/check project-relevant revisions;
- for deployable systems, a **Remote Delivery Environment** that can release an identified repository revision without local human tooling;
- protected **Secret Stores** and provider/account control planes for credentials and account-owner actions.

The ZeroLocal project itself is split into four layers:

1. **ZeroLocal Core specification** — provider-neutral requirements and invariants.
2. **ZeroLocal plugin/orchestrator** — the installable user-facing workflow that activates ZeroLocal mode, operates the repository, maintains durable state, and dispatches provider-specific work.
3. **Provider flows/adapters** — modular behavior for a selected deployment provider.
4. **Provider reference fixtures** — repositories used to exercise and validate provider flows end to end.

A repository may conform to ZeroLocal Core without using the official ZeroLocal plugin. The official ZeroLocal product, however, is intended to make the conforming workflow installable and reusable rather than requiring each project to reconstruct the playbook manually.

`iorLab/zerolocal-cloudflare-starter` is a layer-4 Cloudflare provider reference fixture/scaffold/testbed. It is **not** the primary user entry point to ZeroLocal and users are not expected to fork it merely to activate ZeroLocal mode.

## 4. Core principle

> A local machine may be useful, but it must not be required to operate the normal project lifecycle.

For this specification, **normal lifecycle** means the documented path used for routine code/configuration changes, remote validation, release where applicable, and diagnosis/recovery of repository-side failures.

Account-owner actions at explicit trust boundaries are not considered violations of ZeroLocal. Examples include authorizing repository access, choosing or authorizing a deployment provider, creating a scoped provider token, storing a secret, approving billing, proving domain ownership, or approving a protected production deployment.

## 5. ZeroLocal Core requirements

### 5.1 Canonical repository

**ZL-CORE-001 — Canonical source of truth**  
A conforming project **MUST** designate a canonical repository as the authoritative source for project code, configuration, automation, and durable project-operating state.

**ZL-CORE-002 — Repository-native operation**  
The normal workflow **MUST** provide an authorized repository-native path that is sufficient to inspect project state and create or modify repository content without requiring a human-operated local checkout.

**ZL-CORE-003 — Durable history**  
Material implementation and operating changes **MUST** be represented in durable repository history or in another durable system explicitly referenced by the repository.

### 5.2 No local prerequisite

**ZL-CORE-004 — No mandatory local checkout**  
The documented normal workflow **MUST NOT** require the Human Operator to clone or maintain a local project checkout.

**ZL-CORE-005 — No mandatory local toolchain**  
The documented normal workflow **MUST NOT** require the Human Operator to install or run project package managers, compilers, test runners, build tools, source-control commands, infrastructure CLIs, or deployment CLIs locally.

**ZL-CORE-006 — Optional local development**  
A conforming project **MAY** support local development. Optional local workflows **MUST NOT** be the only supported path for any lifecycle step claimed as ZeroLocal.

### 5.3 Remote validation and evidence

**ZL-CORE-007 — Remote validation**  
Project-relevant changes **MUST** have a remote validation path capable of executing the checks required by the project before those checks are considered satisfied.

**ZL-CORE-008 — Revision identity**  
Remote validation results **MUST** be attributable to an immutable repository revision, such as a commit SHA.

**ZL-CORE-009 — Inspectable failure evidence**  
Validation and delivery failures **MUST** produce remotely inspectable status and diagnostic evidence sufficient to distinguish at least repository/code failures from trust-boundary or provider/account failures.

**ZL-CORE-010 — Repository-side recovery**  
A repository/code failure **MUST** be recoverable through the repository-native operating path without requiring the Human Operator to debug or patch the project locally.

### 5.4 Secrets and trust boundaries

**ZL-CORE-011 — Protected secret storage**  
Secret values used by automation **MUST** be stored in an appropriate protected secret store or provider-managed secret system and **MUST NOT** be committed to the repository.

**ZL-CORE-012 — No conversational secret dependency**  
The normal ZeroLocal workflow **MUST NOT** require secret values to be pasted into a chat conversation or other transient AI prompt context. Secret names, required scopes, and setup instructions are permitted.

**ZL-CORE-013 — Explicit human trust boundaries**  
Actions that require account ownership, credential creation, billing authority, external consent, provider authorization, or protected-environment approval **MAY** remain Human Operator actions and **SHOULD** be documented as explicit trust boundaries.

**ZL-CORE-014 — Least privilege**  
Repository automation and provider credentials **SHOULD** receive only the permissions required for their documented role.

### 5.5 Automation as project state

**ZL-CORE-015 — Versioned automation**  
Automation that defines required validation or delivery behavior **MUST** be version-controlled in the canonical repository, except where a platform requires an external policy object; such external policy **MUST** be documented or referenced from the repository.

**ZL-CORE-016 — Reproducible remote execution**  
Required validation and delivery steps **SHOULD** execute in a reproducible remote environment from repository-declared configuration and dependency metadata.

### 5.6 Deployment, when the project has production delivery

The following requirements apply to projects that claim ZeroLocal operation for a deployed environment.

**ZL-CORE-017 — Remote deploy path**  
Production delivery **MUST** be executable remotely from repository/provider automation without requiring a Human Operator to run local deployment commands.

**ZL-CORE-018 — Deploy revision provenance**  
Every production deployment **MUST** identify the immutable repository revision it intends to release.

**ZL-CORE-019 — Validated-revision integrity**  
When production delivery depends on a validation result, the deployed revision **MUST** be the same immutable revision that satisfied the required validation gate, unless an explicit additional validation of the replacement revision occurs.

**ZL-CORE-020 — Untrusted change isolation**  
Untrusted pull-request or equivalent change contexts **MUST NOT** gain a path to production secrets or production deployment solely by causing ordinary validation to run.

**ZL-CORE-021 — Idempotent provisioning and delivery**  
Deployment/provisioning automation **SHOULD** be safe to re-run for the same intended state and **SHOULD NOT** create duplicate durable resources merely because a workflow is retried.

**ZL-CORE-022 — Deployment serialization**  
Where concurrent production operations could corrupt state, race migrations, or make provenance ambiguous, production delivery **MUST** serialize or otherwise coordinate those operations.

**ZL-CORE-023 — Production verification**  
A successful deployment **SHOULD** include an automated verification of the deployed system appropriate to the project, such as health/readiness checks or equivalent externally observable assertions.

**ZL-CORE-024 — Human approval gates are allowed**  
A project **MAY** require an explicit Human Operator approval before production deployment. Such an approval gate does not violate ZeroLocal if the approval is a trust-boundary action and no local project tooling is required.

## 6. Repository Project Memory (RPM) profile

RPM is the repository-backed durable-memory convention used by this specification project and the founding case study. RPM is provisional and is an optional profile in v0.1; it is not currently required for ZeroLocal Core conformance.

A project claiming **ZeroLocal v0.1 + RPM** MUST satisfy ZeroLocal Core and the following requirements.

**ZL-RPM-001 — Manifest**  
The repository **MUST** contain `.chatgpt/project-memory.yaml` or an explicitly documented equivalent manifest.

**ZL-RPM-002 — Canonical declaration**  
The manifest **MUST** identify the project and canonical repository and **MUST** declare that durable project state is repository-backed.

**ZL-RPM-003 — State and next steps**  
The manifest **MUST** reference durable project-state and next-step files.

**ZL-RPM-004 — Durable decisions**  
The manifest **SHOULD** reference a durable decisions log containing project decisions that materially affect architecture, security, delivery, or product constraints.

**ZL-RPM-005 — Conversation bootstrap**  
The AI/Repository Operator's project instructions **SHOULD** require reading the RPM manifest and referenced state at the first substantive turn of a new working conversation.

**ZL-RPM-006 — Checkpoint**  
The operating model **SHOULD** define a checkpoint operation that persists material working-state changes before a conversation intentionally ends.

A minimal v0.1 RPM layout is:

```text
.chatgpt/
├── project-memory.yaml
├── state.yaml
├── next-steps.md
└── decisions.md
```

Example manifest:

```yaml
version: 1
project:
  name: my-project
  repository: owner/my-project
canonical_source: github
files:
  state: .chatgpt/state.yaml
  next_steps: .chatgpt/next-steps.md
  decisions: .chatgpt/decisions.md
checkpoint:
  triggers:
    - checkpoint
    - save progress
    - 收尾
    - 结束
```

## 7. Continuous Delivery profile

A project claiming **ZeroLocal v0.1 + Continuous Delivery** MUST satisfy ZeroLocal Core and the following provisional requirements.

**ZL-CD-001 — Automated change validation**  
Project-relevant changes to the release branch **MUST** automatically trigger required validation.

**ZL-CD-002 — Validation-gated production**  
Normal production delivery **MUST** require successful validation of the exact revision being released.

**ZL-CD-003 — Trusted release event**  
Automatic production delivery **MUST** originate only from a trusted event and **MUST NOT** be reachable from an untrusted pull-request validation event carrying production authority.

**ZL-CD-004 — Exact revision checkout**  
Deployment automation **MUST** explicitly resolve and deploy the immutable revision that passed the production validation gate.

**ZL-CD-005 — Recovery trigger**  
A manual or operator-invoked remote recovery/re-run mechanism **SHOULD** remain available even when normal production delivery is automatic.

**ZL-CD-006 — Non-release state churn**  
Repositories that frequently update RPM or documentation **SHOULD** avoid triggering production delivery for changes that cannot affect the deployed product.

The founding case uses CI-gated automatic delivery from a trusted push to `main`, exact-SHA deployment, serialized production runs, and a manual dispatch fallback. These mechanics are evidence for this profile, not a requirement to use GitHub Actions specifically.

## 8. Official ZeroLocal plugin/orchestration model

The official ZeroLocal product is intended to be installable and activated by user intent rather than by copying a provider-specific repository template.

A provisional lifecycle is:

```text
Install ZeroLocal
        ↓
Activate ZeroLocal mode for a project
        ↓
Resolve canonical repository
        ↓
Load or initialize RPM/project state
        ↓
Inspect project + requirements
        ↓
Implement through repository-native operations
        ↓
Remote validation
        ↓
Failure? ── yes → classify → repository repair or trust-boundary instruction → retry
        ↓ no
Deployment required?
        ↓ yes
Resolve provider (existing config or user choice)
        ↓
Dispatch provider-specific flow
        ↓
Remote deploy + verification
        ↓
Checkpoint durable project state
```

The official plugin SHOULD avoid asking the user for facts that are already durable in RPM or repository configuration.

Provider selection SHOULD occur only when provider-specific work is needed. Choosing Cloudflare is not equivalent to choosing ZeroLocal; it selects the Cloudflare branch *inside* an already active ZeroLocal workflow.

The plugin MAY delegate provider operations to another installed provider plugin or tool integration rather than reimplementing provider APIs, as long as the ZeroLocal orchestration invariants, trust boundaries, provenance, and recovery behavior remain intact.

## 9. Failure-recovery contract

A conforming ZeroLocal workflow should preserve a closed remote repair loop:

```text
Human intent or reported failure
        ↓
AI/Repository Operator
        ↓
Canonical repository
        ↓
Remote validation / delivery
        ↓
Remote status + logs + deployed verification
        ↓
AI/Repository Operator diagnoses
        ↓
repository fix OR precise trust-boundary instruction
```

Failures should be classified into at least:

- code/build/test;
- dependency/toolchain;
- repository permissions;
- missing/invalid protected secret;
- provider permissions/account state;
- infrastructure provisioning;
- migration/state transition;
- routing/DNS/external integration;
- production health/readiness.

A repository-side category should lead to a repository-side repair. A trust-boundary category may require a Human Operator action, but should not default to "clone the repo and debug locally."

## 10. Provider flow / adapter boundary

ZeroLocal Core intentionally does not standardize a cloud API, deployment CLI, database, or runtime.

A provider-specific flow SHOULD expose enough behavior for the ZeroLocal plugin to perform or coordinate:

1. provider capability/dependency discovery;
2. provider selection or recognition from existing project state;
3. required credentials and minimum scopes, without requesting secret values in chat;
4. project/repository scaffolding required for that provider;
5. remote validation and delivery integration;
6. resource discovery/provisioning behavior;
7. migration/state-transition behavior where applicable;
8. deployment command/API contract and immutable revision provenance;
9. production endpoint discovery;
10. health/readiness or equivalent verification;
11. idempotency/retry behavior;
12. remotely inspectable failure evidence and recovery classification.

A provider flow may be packaged inside ZeroLocal, implemented by a separate provider plugin/tool, or use a hybrid model. v0.1 has not yet fixed the packaging mechanism; the important boundary is behavioral and provider-neutral.

Cloudflare is the first provider path. `iorLab/zerolocal-cloudflare-starter` serves as a reference scaffold/golden fixture/conformance testbed for what the Cloudflare flow creates and how the resulting project behaves. It does not define ZeroLocal as a whole.

## 11. Security invariants

The following invariants are central to ZeroLocal and should remain stable as v0.1 evolves:

- moving work off the local machine **MUST NOT** mean moving secrets into chat;
- repository write authority and production authority **SHOULD** be separable;
- untrusted code **MUST NOT** acquire production credentials merely by participating in CI;
- production provenance **MUST** identify what immutable repository revision was deployed;
- provider credentials **SHOULD** be scoped and revocable;
- repository automation **SHOULD** fail closed when required trust material is missing;
- account-owner approvals **MAY** remain manual where risk policy requires them;
- selecting a provider **MUST NOT** weaken the provider-neutral ZeroLocal trust and provenance invariants.

## 12. Provisional conformance claims

Until v0.1 exits Working Draft, the following claims are provisional:

- **ZeroLocal v0.1 Core** — satisfies all applicable `ZL-CORE-*` MUST/MUST NOT requirements.
- **ZeroLocal v0.1 + RPM** — Core plus all `ZL-RPM-*` MUST/MUST NOT requirements.
- **ZeroLocal v0.1 + Continuous Delivery** — Core plus all `ZL-CD-*` MUST/MUST NOT requirements.

A project **SHOULD NOT** claim conformance based only on repository files. Operational requirements such as secret isolation, remote validation, deployment provenance, and production verification require observable evidence from the configured system.

The official ZeroLocal plugin is an implementation/orchestration product, not itself the definition of repository conformance. Future v0.1 work may define a separate plugin/provider-adapter compatibility claim.

## 13. Founding case study: awesome-fame-slider

The founding case demonstrated the initial ZeroLocal operating loop on a real Cloudflare application:

- the repository was initialized and maintained directly through GitHub without requiring a human local checkout;
- GitHub stored durable RPM state and project history;
- GitHub Actions provided CI and deployment execution;
- Cloudflare Workers and D1 provided production compute and state;
- deployment credentials remained in GitHub/provider secret stores;
- deployment failures were diagnosed from GitHub Actions logs and repaired through repository commits;
- production delivery evolved to CI-gated automatic deployment of the exact passing main-branch SHA;
- production runs were serialized and verified with health/readiness checks;
- pure RPM/docs changes were excluded from product deployment churn.

The reusable product lesson is broader than the Cloudflare implementation: the operating model should become an installable ZeroLocal workflow, with provider choice dispatched separately rather than requiring each new project to reconstruct the playbook manually.

Application-specific voting, X sharing, UI behavior, and product architecture are not ZeroLocal requirements.

## 14. Open v0.1 questions

The Working Draft intentionally leaves several items open:

1. What is the exact installable plugin/skill package structure for ZeroLocal Core?
2. Which responsibilities belong in the official ZeroLocal plugin versus provider adapters?
3. Should provider flows be bundled, depend on separate provider plugins/tools, or use a hybrid model?
4. What is the smallest useful machine-readable project/provider manifest so ZeroLocal can resume without repeated questions?
5. Should RPM remain optional for generic conformance even if the official plugin relies on durable repository-backed state?
6. Should Continuous Delivery remain an optional profile, or should every deployable ZeroLocal project require an automatic post-validation release path?
7. How should protected production approval environments be described without binding the specification to GitHub Environments?
8. Which provider should serve as the second provider-flow implementation to validate modular dispatch?
9. Which requirements can be checked statically from repository content, and which require live operational probes?
10. Should ZeroLocal distinguish repository/project conformance, official-plugin compatibility, and provider-adapter compatibility as separate claims?

## 15. v0.1 development method

The specification and product will be refined together by implementation pressure:

1. keep Core provider-neutral;
2. define and implement the installable ZeroLocal plugin's core orchestration flow in `iorLab/zerolocal`;
3. define a provider adapter contract;
4. implement Cloudflare as the first provider flow;
5. use `iorLab/zerolocal-cloudflare-starter` as a golden fixture/testbed for the Cloudflare flow rather than as the user entry point;
6. encode observable project and provider-flow conformance checks;
7. compare behavior with the founding case;
8. turn ambiguities and implementation-specific assumptions into explicit decisions;
9. add a second provider flow before treating provider modularity as validated.

The target user experience is intentionally simple: install ZeroLocal, ask to use ZeroLocal mode for a project, and only then choose a deployment provider when deployment-specific work is required.

The goal of v0.1 is not to standardize every AI-native development workflow. It is to define a small set of testable invariants and an installable orchestration model that make "no local environment required" a dependable engineering property rather than a project-specific demo claim.
