# Svif Software Delivery Profile Draft

**Status:** Architecture transition draft; not a released conformance profile  
**Parent:** Svif v0.2 architecture transition  
**Predecessor evidence:** ZeroLocal v0.1

## 1. Purpose

This profile specializes Svif Core for software projects that build, validate, provision, deploy, migrate, publish, or otherwise deliver executable or externally served software.

Its purpose is to preserve the strongest delivery invariants proven by ZeroLocal without making Git, GitHub, remote-only execution, ChatGPT, Skills, Cloudflare, or a particular CI/CD product universal Svif Core requirements.

A conforming implementation of this profile also conforms to the applicable Svif Core and Agnir Core contracts.

## 2. Profile concepts

### 2.1 Source / artifact authority

A Project MUST identify the authoritative source and configuration used to produce a delivery candidate.

The authority MAY be a Git repository, another VCS, a versioned workspace, a build artifact store, or another system capable of producing a stable candidate identity.

### 2.2 Candidate identity

Every delivery candidate MUST have a stable, unambiguous identity that can be attributed across verification and delivery evidence.

For Git-based projects, an immutable commit SHA is the RECOMMENDED candidate identity.

A branch name, mutable tag, working-directory description, or conversational statement alone is insufficient when it can resolve to different content over time.

### 2.3 Verification environment

A Verification Environment executes required checks against an identified candidate and produces inspectable evidence.

Verification MAY run locally, remotely, in CI, in a hosted workspace, or in another environment. The execution location is not itself a conformance property.

### 2.4 Delivery environment

A Delivery Environment actuates a verified candidate into a target environment or release state.

Verification authority and protected delivery authority SHOULD be separable. An untrusted verification context MUST NOT automatically inherit protected production authority.

### 2.5 Provider adapter

A Provider Adapter implements provider-specific resource, deployment, endpoint, observation, and recovery behavior while preserving Svif and profile invariants.

Cloudflare is the first historical reference provider, not a profile requirement.

## 3. Lifecycle specialization

The Svif Core lifecycle remains:

`DISCOVER -> PLAN -> CHANGE -> VERIFY -> DELIVER -> OBSERVE -> CHECKPOINT`

For this profile, `DELIVER` MAY expand into:

`PREPARE/PROVISION -> MIGRATE -> DEPLOY/PUBLISH`

Each substate MAY be skipped when inapplicable, but applicable invariants remain mandatory.

### 3.1 DISCOVER

In addition to Svif Core discovery, the Executor SHOULD identify:

- source/versioning system and current candidate base;
- build/test/lint/typecheck/security/policy checks required by Project policy;
- delivery automation and target environments;
- provider/resource declarations;
- migration/state-transition requirements;
- protected credentials and approval boundaries by name/scope, never by secret value through an unauthorized channel;
- production observation/readiness mechanisms;
- current known release/deployment blockers.

Durable Project continuity is loaded through Agnir rather than through a profile-specific memory system.

### 3.2 PLAN

A material delivery plan SHOULD identify:

- intended candidate changes;
- required verification checks;
- delivery target(s);
- migration/provisioning implications;
- destructive or irreversible operations;
- protected authority or Principal approval required;
- observation/readiness criteria;
- rollback or repair path when material.

### 3.3 CHANGE

Source, configuration, automation, infrastructure declarations, and migration changes MUST be made in an authoritative Project system that can produce a stable candidate identity.

For Git-based Projects, material source/configuration changes SHOULD be represented by immutable commits before verification claims are made.

### 3.4 VERIFY

Required Project checks MUST run against the candidate being evaluated.

Verification evidence MUST identify the candidate. Failed checks MUST expose enough inspectable evidence to diagnose the responsible layer when the environment permits it.

A successful build or test of candidate `A` MUST NOT be used as verification evidence for candidate `B` unless equivalence is independently proven.

### 3.5 PREPARE / PROVISION

When provider resources or delivery prerequisites are required, provider-specific preparation SHOULD be idempotent or safely replayable where practical.

Resource discovery SHOULD occur before creation to avoid unintended duplication.

Destructive replacement, deletion, account changes, billing changes, domain ownership changes, or other high-risk transitions MAY require explicit Principal authorization.

### 3.6 MIGRATE

Durable state transitions such as database/schema/data migrations MUST be ordered explicitly when ordering affects correctness.

Migrations SHOULD be replay-safe or guarded against duplicate execution where practical.

The profile MUST distinguish migration failure from application-code failure when evidence supports that distinction.

### 3.7 DEPLOY / PUBLISH

Delivery MUST identify the exact candidate being actuated.

When delivery is verification-gated, the delivered candidate MUST equal the verified candidate unless the replacement candidate is independently verified.

For Git-based workflows, exact validated SHA delivery is the RECOMMENDED strong form of this invariant.

Mutable aliases such as `main`, `latest`, or an unpinned artifact name MAY be used for discovery or triggering, but final delivery evidence MUST resolve the actual immutable/unambiguous candidate delivered when the target system supports such identity.

State-sensitive concurrent production operations MUST be serialized or otherwise coordinated when concurrency could race migrations, corrupt state, or make candidate provenance ambiguous.

### 3.8 OBSERVE

A successful deployment command or provider API response alone is insufficient to prove production success when the resulting system is externally observable.

Observation SHOULD verify the deployed target through system-appropriate evidence such as:

- health/readiness endpoints;
- externally fetched page or API assertions;
- provider deployment status tied to candidate identity;
- application/version endpoint;
- resource/state query;
- rendered artifact verification;
- smoke/integration checks.

Observation evidence SHOULD identify the target environment and candidate when feasible.

### 3.9 REPAIR

The implementation SHOULD classify failures at least into:

- source/build/test;
- dependency/toolchain;
- source/versioning authorization;
- protected credential/secret availability;
- provider/account authorization or state;
- infrastructure provisioning;
- migration/state transition;
- deployment/publication;
- routing/DNS/external integration;
- production health/readiness;
- candidate/provenance mismatch;
- Agnir discovery/continuity;
- explicit Principal trust-boundary action required.

Repair SHOULD occur at the earliest responsible layer and re-enter the lifecycle at the earliest state whose invariant was violated.

### 3.10 CHECKPOINT

Svif operation state, material release evidence, blockers, and next actions SHOULD be reconciled through Agnir at meaningful boundaries.

The profile MUST NOT introduce a second repository-specific memory contract.

## 4. Core delivery requirements

### SD-PROV-001 — Stable candidate

A candidate presented as verified or delivered MUST have a stable, unambiguous identity.

### SD-PROV-002 — Verification attribution

Verification evidence MUST be attributable to the candidate it verifies.

### SD-PROV-003 — Exact verified candidate delivery

When delivery is verification-gated, the delivered candidate MUST be the verified candidate unless a replacement is independently verified.

### SD-AUTH-001 — Verification/delivery authority separation

Untrusted or lower-trust verification contexts MUST NOT automatically receive protected production credentials or authority.

### SD-SECRET-001 — Protected secret handling

Secret values MUST remain in authorized protected stores/channels appropriate to the Project. The workflow MUST NOT require secret values to be pasted into an unprotected conversational or execution surface.

Credential names, required scopes, secret-store locations, and setup actions MAY be communicated without values.

### SD-DELIVER-001 — Safe state-sensitive concurrency

Concurrent delivery operations MUST be coordinated when they could race state changes or make provenance unsafe.

### SD-OBSERVE-001 — Observable success

When a delivery claims an externally observable effect, resulting state MUST be independently observed. Successful actuation alone is insufficient.

### SD-TRUST-001 — Explicit trust boundaries

Account ownership, billing, protected credentials, domain ownership, external consent, destructive operations, and production approval MAY remain explicit Principal actions.

A trust-boundary requirement MUST NOT be misreported as an ordinary source-code defect.

### SD-ADAPTER-001 — Provider isolation

Provider-specific behavior MUST remain behind a Provider Adapter or profile-specific implementation boundary and MUST NOT redefine generic Svif Core merely because the reference provider uses it.

### SD-RECOVER-001 — Evidence-based repair

Failure classification and repair routing MUST use available evidence and return to the earliest violated invariant.

## 5. Optional SCM profile realization

A Git-based implementation can satisfy the candidate/provenance requirements with:

```text
candidate identity = full immutable commit SHA
verification evidence -> SHA
build artifact provenance -> SHA or digest linked to SHA
delivery evidence -> exact SHA/digest
observation evidence -> deployed SHA/version where observable
```

This is a strong reference pattern, not Svif Core's only candidate model.

A future `Svif Git/SCM Profile` MAY standardize repository branch, pull request, protected-branch, commit-status, and workflow conventions separately from this software-delivery profile.

## 6. Provider adapter capability contract — draft shape

A software-delivery Provider Adapter SHOULD be able to declare semantics equivalent to:

```yaml
svif_adapter:
  version: 0.1
  kind: provider
provider:
  id: <provider-id>
capabilities:
  detect: true
  provision: true
  migrate: optional
  deliver: true
  observe: true
authority:
  required_credentials:
    - name: <credential-name>
      minimum_scope: <scope-description>
  trust_boundaries: []
evidence:
  candidate_identity: <supported-form>
  delivery_identity: <supported-form>
  observation: <supported-evidence>
failure_classes: []
```

The serialization is illustrative. The semantic fields should be refined into a separate Capability Adapter contract before Svif v0.2 conformance is frozen.

## 7. Mapping from ZeroLocal v0.1

| ZeroLocal v0.1 requirement | Svif destination |
|---|---|
| canonical repository | optional SCM/repository profile, not Core |
| no required human local checkout | historical operating-mode property; not generic Core |
| Human Operator | Principal |
| Agent Operator | Executor |
| RPM | Agnir Core |
| fresh conversation bootstrap | Agnir cold-start discovery |
| remote CI | Verification capability; location-neutral |
| exact validated Git SHA | Software Delivery Profile strong SCM realization of stable candidate provenance |
| PROVISION | DELIVER substate/profile behavior |
| DEPLOY | DELIVER substate/profile behavior |
| production observation | profile + Svif observable-success invariant |
| provider descriptor/hooks | Capability/Provider Adapter contract |
| Core Skill | execution-surface integration |
| Provider Skill | provider adapter + optional execution-surface wrapper |
| Cloudflare reference | profile/provider implementation evidence |

## 8. Historical evidence treatment

`mattamior/agent-skills` Validation Project #1 remains a passed **ZeroLocal v0.1** clean-room result.

Its evidence supports this profile's design pressure around:

- immutable candidate provenance;
- validation/delivery authority separation;
- dependency/toolchain repair;
- protected-secret trust boundaries;
- provider resource lifecycle behavior;
- externally observed readiness;
- fresh-context continuity, now delegated to Agnir cold-start discovery.

The result MUST NOT be relabeled as Svif Software Delivery Profile conformance until the new profile and Agnir dependency are finalized and exercised.

## 9. Validation Project #2 pressure

When `mattamior/cloud-mail` resumes as Validation Project #2, the test should pressure this profile with:

- adoption into an existing stateful Cloudflare-native application;
- multiple provider resource types;
- migrations/state transitions;
- non-destructive provider resource handling;
- candidate provenance across verification and delivery;
- external frontend/backend observation;
- explicit protected-provider trust boundaries;
- Agnir cold-start recovery from a fresh Executor.

The validation plan should be revised only after the Agnir 0.1 discovery contract and Svif Capability Adapter semantics are concrete enough to test.
