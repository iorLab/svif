---
name: zerolocal-cloudflare-provider
description: Implement the ZeroLocal v0.1 Provider Adapter Contract for Cloudflare Workers projects. Load when ZeroLocal Core dispatches provider work to Cloudflare for detection, scaffolding, validation, provisioning, deployment, endpoint discovery, verification, or recovery.
---

# ZeroLocal Cloudflare Provider Skill v0.1

Implements the ZeroLocal v0.1 Provider Adapter Contract for Cloudflare. This skill is provider-specific and MUST be invoked behind ZeroLocal Core rather than defining Core lifecycle semantics.

Reference fixture: `iorLab/zerolocal-cloudflare-starter`.

## Required delegation behavior

Cloudflare platform behavior changes over time. Before writing or reviewing Workers runtime/configuration, load the available current Cloudflare Workers/Wrangler skills and retrieve current Cloudflare documentation rather than relying on stale API/config assumptions.

Prefer mature Cloudflare tools/skills for provider mechanics. This skill supplies ZeroLocal-specific orchestration constraints around those mechanics.

## Provider descriptor

Recognize `ZEROLOCAL.yaml` with `provider.id: cloudflare`. The descriptor should declare at least:

- runtime/capabilities;
- protected credential names and minimum scopes;
- validation and deployment workflow paths;
- immutable revision source;
- production verification path/equivalent;
- human trust boundaries.

Reference credential names:

- `CLOUDFLARE_API_TOKEN` — protected secret; minimum practical scope for Workers deployment to the intended account/resources.
- `CLOUDFLARE_ACCOUNT_ID` — protected CI secret in the reference fixture.

Never ask the user to paste either value into chat.

## Adapter hooks

### detect

Inspect repository state for Cloudflare evidence, including `wrangler.jsonc`/`wrangler.toml`, Workers/Pages configuration, package dependencies, workflows, bindings, routes/domains, and `ZEROLOCAL.yaml`.

Return detected state, runtime, config paths, declared resources/bindings, credential names, delivery readiness, and missing repository requirements versus human trust boundaries.

### capabilities

Cloudflare v0.1 reference baseline:

- Workers deployment: required;
- endpoint discovery: required;
- production health/readiness verification: required;
- D1 provisioning/migrations: optional;
- other Cloudflare products: allowed only when project requirements need them and current Cloudflare guidance is loaded.

Do not generalize Cloudflare-specific capabilities into ZeroLocal Core.

### credentials

Describe names and minimum scopes only. Secret values remain in GitHub Actions/Cloudflare protected stores.

For CI deployment, current Cloudflare guidance requires an API token and account ID. Scope tokens to the target account/resources and least privileges needed.

Classify missing credentials as a `protected secret` trust-boundary failure, not a repository-code defect.

### scaffold

For a minimal Worker reference, create or align:

- `wrangler.jsonc` using a current compatibility date;
- Worker entrypoint;
- package metadata/tooling;
- remote CI workflow;
- trusted deployment workflow;
- `ZEROLOCAL.yaml` provider descriptor;
- health/readiness endpoint or equivalent observable assertion;
- RPM when the project claims the official ZeroLocal RPM profile.

New Workers configuration should follow current Cloudflare recommendations. Do not copy obsolete compatibility flags/config fields from the reference fixture without checking current docs.

### validate

Provider-relevant validation must execute remotely and be attributable to an immutable commit SHA. At minimum validate syntax/build/tests required by the project and consistency between bindings/configuration and code.

PR/untrusted validation MUST NOT receive production Cloudflare credentials.

### provision

Discover before create. Prefer declarative/idempotent behavior. If provider resources already exist, reconcile rather than duplicate them.

Provider/account actions requiring billing, account ownership, token creation, domain ownership, or protected permissions are human trust boundaries.

For optional D1, keep database identity/binding declarations in repository state while protected provider authority remains external.

### migrate

When durable provider state exists, migrations MUST be ordered and repository-versioned; production execution MUST be coordinated with deployment when race conditions could occur; retries MUST be safe or explicitly guarded; failure MUST expose remote evidence and halt production-success reporting.

If no migration/state transition applies, return `not required`.

### deploy

For CI-gated production:

1. accept the immutable SHA that passed required validation;
2. run only from a trusted release context with production credentials;
3. checkout/deploy that exact SHA rather than an ambient moving branch head;
4. serialize production operations when concurrent runs could race;
5. retain a manual remote recovery path accepting an explicit immutable SHA;
6. expose the Cloudflare deployment URL or equivalent production target.

The reference fixture uses a GitHub Actions `workflow_run` gated on successful CI from a push to `main`, then checks out `workflow_run.head_sha`. Equivalent mechanisms are conforming if they preserve the same invariants.

### endpoint

Prefer provider/tool output for the actual deployed URL/route rather than constructing a hostname from assumptions. Normalize provider output carefully because action/CLI formats can vary.

If deployment is only reachable through a custom domain, use provider-declared route/domain evidence.

### verify

After deployment, perform externally observable verification against the deployed endpoint/target. For HTTP Workers, call a health/readiness endpoint or equivalent assertion with retries appropriate to propagation.

Verification failure means deployment is not yet `observed` successfully even if Wrangler returned success.

Return deployed immutable SHA, deployment target URL/route, verification assertion/result, and remote evidence location when available.

### recover

Classify Cloudflare failures into the ZeroLocal taxonomy and choose the correct owner:

- Worker source/build/test -> repository repair;
- Wrangler/dependency/config mismatch -> repository repair after current-doc verification;
- missing token/account id -> human protected-secret action;
- insufficient token scope/account access -> human provider-authorization action;
- resource provisioning conflict -> inspect existing provider state and reconcile idempotently;
- D1 migration failure -> inspect logs/state, repair migration or sequencing, retry remotely;
- route/custom-domain/DNS ownership -> human/provider boundary or repository route correction according to evidence;
- health/readiness failure -> inspect Worker logs/config/runtime and repair before reporting success.

Never default to "run Wrangler locally" as the required recovery path.

## Reference GitHub Actions shape

The reference fixture intentionally separates:

- `CI` on pull request and `main` push with no production credentials;
- `Deploy` triggered after successful `CI` for a trusted `main` push;
- exact checkout of the tested SHA;
- `production` environment and serialized concurrency;
- `cloudflare/wrangler-action@v3` using protected token/account ID;
- post-deploy health check using deployment URL output;
- manual dispatch requiring a full immutable SHA for recovery.

Do not treat GitHub Actions itself as a Core requirement; it is the reference control-plane implementation.

## Exit contract to Core

Return one of these semantic outcomes:

- `ready` — provider requirements satisfied, no action needed;
- `repository_change_required` — identify exact files/automation/config to repair;
- `trust_boundary_required` — identify the human action, account/store, and minimum scope without secret values;
- `deployed` — include immutable SHA and deployment target;
- `observed` — include immutable SHA, target, and successful verification evidence;
- `failed` — include failure taxonomy category, evidence, owner, and next retry point.
