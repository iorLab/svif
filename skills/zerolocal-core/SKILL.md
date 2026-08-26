---
name: zerolocal-core
description: Operate software projects through the ZeroLocal v0.1 repository-first lifecycle. Load when the user asks to initialize, continue, implement, verify, deliver, recover, observe, or checkpoint a project in ZeroLocal mode. Provider-neutral; delegate provider work to a compatible provider skill.
---

# ZeroLocal Core Skill v0.1

Implements `SPECIFICATION.md` v0.1. GitHub is the canonical RPM/control-plane implementation for the reference product, but Core semantics are provider-neutral.

## Non-negotiable invariants

1. The canonical repository is the project filesystem and durable source of truth.
2. Do not require a human-operated local checkout, local toolchain, local git commands, or local deployment CLI for the normal supported lifecycle.
3. Never request or reproduce secret values in chat. Refer only to secret names, required scopes, and protected stores.
4. CI verifies; deployment actuates. If production is validation-gated, deploy the exact immutable revision that passed the gate.
5. Untrusted validation must not gain production credentials or deployment authority.
6. Production success requires observable verification, not merely a successful deploy command.
7. Provider-specific behavior belongs in a Provider Skill/adapter, never in Core.
8. Repository state + RPM + installed skills must be sufficient to resume without founding-chat history.

## Procedure

Execute the smallest necessary slice of `Initialize -> Plan -> Implement -> Verify -> Deliver -> Observe -> Checkpoint`. Do not mechanically run irrelevant phases.

### Initialize

At the first substantive project turn:

1. Resolve the canonical repository from explicit user context, project instructions, or repository metadata.
2. Prefer repository-native/connected GitHub operations over asking for a local checkout or pasted files.
3. Read `.chatgpt/project-memory.yaml` if present.
4. Load every state/next-step file named by the manifest. Load decisions when architecture, security, lifecycle, provider behavior, or prior constraints are relevant.
5. Read `ZEROLOCAL.yaml` or equivalent project/provider descriptor when present.
6. Inspect current repository revision, changed/open work, remote validation/delivery definitions, provider declaration, and current failures.
7. If RPM is absent and the user is explicitly initializing ZeroLocal, create the minimum RPM layout from the Specification; otherwise do not silently impose RPM on an unrelated project.
8. Never ask again for facts already durable in repository/RPM state.

Initialization output must establish: canonical repo, current phase/state, requested intent, required validation, provider status if relevant, and explicit blockers/trust boundaries.

### Plan

Form a repository-executable plan, not a local shell plan.

- Map work to the earliest lifecycle state that needs change.
- Identify repository-owned edits, remote checks, provider work, and trust-boundary actions separately.
- Prefer minimal, reversible repository changes.
- Treat missing secret values as protected-store prerequisites, never as chat inputs.
- When a task is executable without clarification, proceed using repository evidence instead of asking unnecessary questions.

### Implement

- Read the full relevant files before replacement edits when practical.
- Make source/configuration/automation changes through repository-native writes.
- Preserve existing project conventions unless the protocol requires correction.
- Keep provider-neutral orchestration out of provider-specific configuration.
- Ensure material changes become an immutable repository revision.
- Do not claim implementation success before remote verification when required checks exist.

### Verify

1. Identify the immutable candidate revision.
2. Inspect or trigger the repository's remote CI/validation path.
3. Attribute status and diagnostics to the exact revision.
4. If checks fail, classify the failure using the v0.1 taxonomy:
   - code/build/test
   - dependency/toolchain
   - repository permissions
   - protected secret
   - provider permissions/account state
   - provisioning
   - migration/state transition
   - routing/DNS/external integration
   - production health/readiness
5. Repository-owned failure: inspect logs, repair in repository, create a new immutable revision, repeat Verify.
6. Trust-boundary failure: state the exact human action, protected store/account location, and required scope. Do not request the secret value.
7. Do not substitute local commands for a missing remote validation path; repair or add the remote path when ZeroLocal conformance is the task.

### Deliver

Run only when production/provider delivery is requested or part of the project's documented normal lifecycle.

1. Resolve provider from durable project state. Ask for provider choice only if not already declared and provider work is now required.
2. Load a Provider Skill matching the provider descriptor.
3. Pass the immutable validated revision and required lifecycle intent to that skill.
4. Require provider execution to preserve:
   - exact validated-revision provenance;
   - untrusted-context isolation;
   - least-privilege secret handling;
   - idempotent/safe retry behavior;
   - serialization/coordination where state-sensitive;
   - remotely inspectable failure evidence.
5. If a provider skill reports a repository-owned defect, repair via Implement -> Verify before retrying delivery.
6. If it reports a human trust boundary, surface only the precise required action.

### Observe

After delivery or material provider state changes:

- discover the deployed endpoint/target via provider evidence;
- run or inspect health/readiness/external assertions;
- confirm observable result and deployed revision provenance;
- if observation fails, classify and enter Repair/Iterate;
- never report production success from deploy exit status alone.

### Checkpoint

Checkpoint when the user requests `checkpoint`, `save progress`, `收尾`, `结束`, `先到这里`, or an equivalent intentional work boundary, and also when durable state materially changed and the current work naturally concludes.

Persist, as applicable:

- current project phase/lifecycle state;
- completed implementation and verification evidence;
- deployed revision/environment and observation evidence;
- unresolved blockers and trust boundaries;
- next executable steps;
- durable decisions affecting architecture, security, delivery, product scope, or protocol interpretation;
- checkpoint timestamp/reason.

Never persist secret values. After writes, re-read or otherwise verify the durable files if write uncertainty exists.

## Provider dispatch contract

Core may delegate only to a provider skill that can satisfy the v0.1 hooks:

`detect, capabilities, credentials, scaffold, validate, provision, migrate, deploy, endpoint, verify, recover`.

Core owns lifecycle decisions and cross-provider invariants. Provider Skill owns provider API/runtime/tool semantics.

For `provider.id: cloudflare`, load the ZeroLocal Cloudflare Provider Skill. It may itself load mature Cloudflare platform skills/tools for current API/configuration behavior.

## Completion rules

A user-facing completion claim must distinguish:

- **implemented** — repository changes exist;
- **verified** — required remote checks passed for an identified immutable revision;
- **deployed** — provider delivery completed for an identified revision;
- **observed** — production verification passed;
- **blocked at trust boundary** — repository work is complete but a named human authorization/secret/account action remains.

Do not collapse these states into a generic "done".

## ZeroLocal project self-development

When operating `iorLab/zerolocal` itself, obey its `.chatgpt/project-memory.yaml`. `iorLab/zerolocal-cloudflare-starter` is the executable provider reference, not the user entry point. Plugin work remains gated until clean-room skill stabilization passes.
