# ZeroLocal

**ZeroLocal** is a provider-neutral operating model and skill set for repository-first, AI-operated software development where a human can run the normal implementation, validation, release, observation, and repository-side recovery loop without requiring a local project checkout or local project/deployment toolchain.

Local development is allowed. The defining property is that it is **not required**.

The founding operating model was developed under the name **AI-Native Repository Delivery (ANRD)**. ZeroLocal is the current project/product identity.

## Productization sequence

ZeroLocal is deliberately **skill-first, plugin-later**:

```text
Specification v0.1
        ↓
Cloudflare executable reference
        ↓
ZeroLocal Core Skill v0.1
        ↓
Cloudflare Provider Skill v0.1
        ↓
Clean-room multi-project stabilization
        ↓
Stable skills + contracts
        ↓
ZeroLocal Plugin packaging
```

Plugin packaging remains gated. The protocol and procedural workflows are stabilized before a wider product surface is frozen.

## Current status

**Skill v0.1 is implementation-complete.** The current artifacts are:

- canonical protocol: [`SPECIFICATION.md`](./SPECIFICATION.md)
- ZeroLocal Core Skill: [`skills/zerolocal-core/SKILL.md`](./skills/zerolocal-core/SKILL.md)
- Cloudflare Provider Skill: [`skills/cloudflare-provider/SKILL.md`](./skills/cloudflare-provider/SKILL.md)
- conformance checklist: [`conformance/v0.1.md`](./conformance/v0.1.md)
- structural conformance runner: [`conformance/check_v0_1.py`](./conformance/check_v0_1.py)
- Cloudflare executable reference/golden fixture: `iorLab/zerolocal-cloudflare-starter`
- Repository Project Memory: [`.chatgpt/project-memory.yaml`](./.chatgpt/project-memory.yaml)

The next mandatory phase is **Skill Stabilization**: run the skills end to end on at least two new non-founding real projects, preferably 2-3, from fresh contexts and repository state. That phase is required before Plugin work.

## Architecture

ZeroLocal has six logical layers:

1. **Human Governance** — intent, judgment, account ownership, secrets, billing, approvals.
2. **Agent** — ZeroLocal Core procedural orchestration.
3. **Repository Control Plane** — canonical source, automation, RPM, durable history.
4. **Verification & Delivery** — remote CI and exact-revision release mechanics.
5. **Provider Adapter** — provider-specific skill/tool behavior.
6. **Production Observation** — endpoint/readiness/health evidence and recovery signals.

Core semantics are provider-neutral. Cloudflare is the sole v0.1 reference provider, not a Core dependency.

## Lifecycle and Skill interface

Protocol lifecycle:

```text
BOOTSTRAP → IMPLEMENT → VERIFY → PROVISION → DEPLOY → OBSERVE → CHECKPOINT
                  ↘ failures → REPAIR/ITERATE → earliest violated state
```

Core Skill procedure:

```text
Initialize → Plan → Implement → Verify → Deliver → Observe → Checkpoint
```

The procedure maps user intent onto protocol states; it is not a second lifecycle.

## Core invariants

- The canonical repository is the project filesystem and durable source of truth.
- Normal operation must not require a human local checkout, project toolchain, git commands, or deployment CLI.
- Secrets stay in GitHub/provider secret stores and are never requested in chat or persisted in RPM plaintext.
- CI verifies; deployment actuates.
- Validation-gated production deploys the exact immutable revision that passed the gate.
- Untrusted validation contexts do not gain production authority.
- Production success requires observable verification, not merely a successful deploy command.
- Provider-specific behavior remains behind Provider Skills/adapters.
- Fresh contexts must be able to resume from repository state + RPM + installed skills rather than founding-chat history.

## Cloudflare reference

`iorLab/zerolocal-cloudflare-starter` is an executable contract fixture, not the ZeroLocal user entry point. It demonstrates:

- `ZEROLOCAL.yaml` provider declaration;
- repository-backed RPM;
- PR/main remote validation;
- trusted deployment only after successful `main` CI;
- exact checkout/deployment of the tested SHA;
- serialized production runs;
- explicit manual recovery by immutable SHA;
- deployment-target discovery;
- post-deploy `/health` verification;
- Cloudflare credentials as protected-store trust boundaries.

## Mature product direction

A later installable ZeroLocal product may package stable Skills, GitHub integration, templates, onboarding, provider discovery, and versioning. It should compose already-proven workflows rather than be the place where those workflows are first discovered.

## Project state

`iorLab/zerolocal` is the canonical source of truth. Durable project state, next steps, and decisions live under `.chatgpt/`; chat conversations are working memory only.
