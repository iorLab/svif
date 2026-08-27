# Validation Project #1 — `mattamior/agent-skills`

## Result

**PASS — 2026-08-27**

Validation Project #1 completed the required clean-room lifecycle and fresh-context recovery test without relying on founding-chat history or a human-operated local checkout/toolchain.

Final production endpoint: `https://agent-skills.mattamior.workers.dev`

Final observed revision: `b72b103fa1aeebe0f733b8f4ed57ce01f0385ce4`

## Setup

- Fresh ChatGPT Project with Project-only memory.
- Project Instructions intentionally blank at initialization.
- ZeroLocal source supplied as `iorLab/zerolocal`.
- Target repository supplied as `mattamior/agent-skills`.
- Business goal: build a repository-derived Agent Skills showcase website and deploy it to Cloudflare.

## Failure 1 — fresh-conversation RPM discovery

### Evidence

- First run created repository RPM on `feat/skill-gallery-cloudflare`, implemented the gallery, opened PR #1, and checkpointed state.
- RPM was not on the default branch at the time of the first resume test.
- A new conversation in the same ChatGPT Project could not recover the target repository/working ref/RPM automatically and behaved as if project history were absent.

### Classification

`RPM/bootstrap discovery`

RPM persistence succeeded, but fresh-context discovery failed because no durable conversational bootstrap pointer identified the canonical repository, RPM manifest, and non-default authoritative RPM ref.

### Durable repair

- `SPECIFICATION.md`: added `ZL-RPM-006` through `ZL-RPM-009` for durable bootstrap discovery, non-default RPM ref resolution, locator-only instructions, and checkpoint resumability gating.
- Core Skill: Initialize now establishes/proposes a minimal locator-only bootstrap after RPM creation/adoption; Checkpoint verifies the pointer before claiming resumability.
- Failure taxonomy: added `RPM/bootstrap discovery`.
- Conformance: added structural checks for the new requirements.
- ZeroLocal PR #1 (`fix: make RPM resumable from fresh conversations`) passed Conformance and was merged to `main`.

### Retest

The Validation #1 ChatGPT Project then received only the minimal locator instructions:

- ZeroLocal activation;
- canonical repository `mattamior/agent-skills`;
- RPM manifest `.chatgpt/project-memory.yaml`;
- RPM ref `feat/skill-gallery-cloudflare`.

A brand-new conversation received only the user message equivalent of “继续吧，接下来做什么？”. It independently loaded repository/RPM state, reconciled newer GitHub evidence, continued the lifecycle, and stopped at the correct protected-secret trust boundary.

**Fresh-conversation resumability retest: PASS.**

## Production delivery and repair loop

### Initial implementation / PR #1

PR #1 implemented:

- repository-derived gallery content from `skills/*/SKILL.md`;
- remote build/validation;
- `ZEROLOCAL.yaml` Cloudflare provider declaration;
- trusted `.github/workflows/deploy.yml` with exact validated-SHA checkout;
- serialized production deployment;
- external `/health.json` revision verification;
- repository RPM.

The user configured the required protected GitHub `production` environment secrets without exposing values in chat or repository plaintext:

- `CLOUDFLARE_API_TOKEN`;
- `CLOUDFLARE_ACCOUNT_ID`.

PR #1 merged as `bad5f7787b7aeb2e2e792da93346ff9f39516272`.

### Failure 2 — deployment toolchain mismatch

The first production deploy failed after checkout/build because `cloudflare/wrangler-action@v3` installed Wrangler 3.90.0, which rejected the repository's assets-only configuration with `Missing entry-point`.

**Classification:** `dependency/toolchain`.

PR #2 repaired the repository automation by upgrading `cloudflare/wrangler-action` to v4 and explicitly selecting Wrangler major version 4. The repair preserved the exact-SHA validation/deployment gate.

### Endpoint normalization / PR #3

PR #3 renamed the Worker from `mattamior-agent-skills` to `agent-skills` to produce the concise canonical endpoint. The previous Worker remained provisioned; this was surfaced explicitly as non-blocking provider-resource cleanup rather than silently deleted.

PR #3 merged to final `main` revision:

`b72b103fa1aeebe0f733b8f4ed57ce01f0385ce4`

## Final verification and observation evidence

For `b72b103fa1aeebe0f733b8f4ed57ce01f0385ce4`:

- `Validate skills` push workflow run `33047199204`: **success**.
- `Deploy gallery` workflow run `33047220371`: **success**.
- Deployment job completed exact revision resolution, checkout, build, deploy, and production health verification successfully.
- External health endpoint: `https://agent-skills.mattamior.workers.dev/health.json`.
- Health verification reported `status: ok` and the exact deployed revision after one transient propagation 404.
- Target RPM recorded provider status `observed`, delivery status `observed`, endpoint, exact revision, workflow evidence, and the Wrangler repair history.

## Lifecycle coverage

Validation #1 demonstrated the relevant end-to-end path:

`BOOTSTRAP -> IMPLEMENT -> VERIFY -> trust boundary -> DEPLOY -> OBSERVE -> REPAIR/ITERATE -> CHECKPOINT`

It also demonstrated a required fresh-context resume after checkpoint.

## Failure/recovery evidence promoted from this run

1. `RPM/bootstrap discovery` -> durable locator-only Project bootstrap + branch-aware RPM discovery + fresh-context retest.
2. `dependency/toolchain` -> inspect remote tool selection, pin compatible provider CLI/action version, create a new immutable revision, revalidate, redeploy.
3. protected-secret trust boundary -> name protected secret requirements and minimum scope without requesting values in chat.
4. production propagation/readiness -> bounded external retry plus exact-revision health assertion.
5. provider resource rename -> surface retained legacy resources; avoid destructive cleanup without explicit authorization.

Reusable rules are maintained in `.chatgpt/recovery-playbook.md`.

## Residual hygiene

The final observed target RPM remains authoritative on `feat/skill-gallery-cloudflare`, and the ChatGPT Project locator points to that ref. This satisfies the repaired v0.1 resumability contract while the branch exists. A later repository-hygiene pass may consolidate final RPM state onto `main`, remove the non-default `RPM ref` locator, verify fresh-context resume again, and only then delete the feature branch. This is not a Validation #1 pass blocker.

## Conclusion

Validation #1 satisfies the clean-room success criteria: repository-driven implementation, remote verification, protected trust-boundary handling, exact-revision Cloudflare production delivery, observable production verification, real failure diagnosis/repair, durable RPM, and fresh-conversation resumability.
