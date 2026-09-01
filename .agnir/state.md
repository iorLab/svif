# Svif Current State

Svif is the authoritative active **Project orchestration product** in `iorLab/svif` on `main`. Agnir is the independent founding Continuity Provider in `iorLab/agnir`. The former `iorLab/svif-cloudflare-reference` project is retired. Historical ZeroLocal material, retired branches, and the retired Cloudflare reference are evidence only and are not active dependencies or release gates.

## Product architecture

Svif coordinates four first-class components:

1. **Orchestrator** — `src/svif/runtime.py`;
2. **Continuity Provider** — founding Agnir implementation at `src/svif/continuity/agnir.py`;
3. **Execution Surface** — founding ChatGPT bridge at `src/svif/execution/chatgpt.py`;
4. **Capability Provider** — founding Cloudflare Workers provider at `src/svif/capabilities/cloudflare.py`.

Stable rule:

> The Project persists; Executors and execution environments may change.

No execution surface becomes canonical Project truth merely because execution occurred there.

## Active contracts and bindings

- Svif product line: `0.2` development (`0.2.0-dev`).
- Project Binding: `project-binding/0.2`.
- Software Delivery profile: `software-delivery/0.2`.
- Capability Adapter: `capability-adapter/0.2`.
- Evidence record: `evidence-record/0.2`.
- Repository/filesystem binding serialization: `SVIF.yaml`.
- Agnir Core compatibility: `0.1`.
- Agnir discovery profile: `repository-filesystem/0.1`.
- Agnir operational distribution applied to this Project: stable repository release `0.1.0` from `iorLab/agnir`, immutable applied revision `2a0cb7bf2068b11f361e315670b2f2dc497b2588`, recorded in `AGNIR.yaml` under `extensions.agnir/operations`.
- Canonical Agnir activation route: `Project root -> AGENTS.md -> README.md / Agnir Project Instructions -> AGNIR.yaml -> declared durable memory`.
- Canonical Svif repository/ref: `iorLab/svif` / `main`.

The Agnir `v0.1.0` application was a **compatible operational upgrade**, not a migration. Upgrade revision `c7cd42b6e94556a630570a54e22c72acc97f3ecf` preserved Core/profile compatibility, Project identity, memory locators/content, and `SVIF.yaml`; `Svif product checks` run `33466389590` passed.

## README entry architecture

The README front section is now deliberately layered before architecture material:

1. `Start Here` / `从这里开始` — minimal user actions for personal-ChatGPT availability, installation in compatible Agent environments, normal continuation, and upgrading the Agnir used by the Project;
2. `Agnir Project Instructions` — canonical Agent activation/operation guidance for this repository;
3. `What Svif Adds to a Project` / `Svif 会给 Project 增加什么` — concrete first-use Project surface, with `AGENTS.md` / `README.md` visibly marked as non-destructive EDIT/add-entry-only and `AGNIR.yaml` / `.agnir/` / `SVIF.yaml` as founding ADD surfaces;
4. `Architecture Diagram` / `架构图` — static product architecture plus the first-use boundary;
5. `Runtime / Operation Flow` / `运行流程` — post-bootstrap runtime behavior, intentionally free of install-mutation labels.

A genuinely uninitialized Project does **not** require manual Agnir pre-initialization. The active Svif first-use contract remains that the shared Skill establishes founding Agnir continuity plus a matching minimal Svif Project Binding on the repository/filesystem path. Compatible existing artifacts are reused; partial/contradictory artifacts are repair cases; an intentional other Continuity Provider binding is preserved.

Repository-integrity checks enforce the entry ordering, first-use ADD/EDIT distinction, architecture/runtime separation, and canonical user intents. Durable rationale is recorded in `.agnir/evidence/2026-09-01-readme-information-architecture.md` and `.agnir/decisions.md`. `README.md` and `README.zh-CN.md` remain synchronized entry points.

## Runtime baseline

- Externally driven execution uses `Orchestrator.begin()` / `Orchestrator.complete()`.
- Untrusted model/result payloads cannot self-grant protected authority.
- External actuation requires successful verification for the exact subject plus applicable trusted authority.
- External success requires independent observation before checkpoint.
- Agnir durable continuity remains Project-owned and execution-surface-neutral.
- Detached commits, PR checkouts, temporary branches, forks, mirrors, or other non-authoritative copies do not silently become canonical checkpoint targets.

`tests/test_founding_e2e.py` proves the credential-free orchestration loop through Agnir continuity load -> Orchestrator -> ChatGPT bridge -> trusted authority -> exact-subject Cloudflare actuation through injected fake transport -> independent observation -> Agnir checkpoint -> continuity reload/resume. This is not live Cloudflare production-delivery evidence.

## Plugin MVP and first-use onboarding

Svif has an active **Plugin MVP** under `plugin/`:

- `plugin/plugin.json` — portable Agent Plugins `1.0.0` manifest;
- `plugin/skills/svif/SKILL.md` — shared Svif Project-orchestration Skill;
- `plugin/.codex-plugin/plugin.json` — OpenAI/Codex manifest reusing the same Skill and carrying public-listing metadata;
- `.agents/plugins/marketplace.json` — auxiliary repository-backed OpenAI/Codex catalog;
- `plugin/README.md` — submission, installation, review-case, and evidence-boundary guidance.

First-use onboarding is a Svif product responsibility. For a genuinely uninitialized ordinary Project, the shared Skill establishes one stable Project identity, Agnir Core `0.1` / `repository-filesystem/0.1` continuity, a matching minimal `project-binding/0.2` `SVIF.yaml`, then fresh-activates and continues the original task. Partial/broken Agnir/Svif artifacts remain repair cases, and a Project intentionally bound to another Continuity Provider is not overwritten with Agnir.

Repository CI proves package/conformance, runtime, repository integrity, Agnir discovery guardrails, distribution metadata consistency, documentation claim boundaries, and first-use bootstrap regression behavior. It does **not** prove OpenAI review, publication, directory appearance, installation, or invocation on a consumer surface.

## Personal ChatGPT public distribution status

The primary ChatGPT audience is individual/personal users. The mature consumer path is:

`individual ChatGPT user -> universal Plugins Directory -> install -> invoke Svif in normal ChatGPT use`

Svif is not publicly listed yet. The repository-side Skills-only package is aligned to the current OpenAI public-submission route, but the real publisher flow is externally blocked before individual developer verification because the Platform requires an accepted default payment method. This is an account/publisher eligibility blocker, not evidence of a Svif package, Skill, Orchestrator, or runtime defect.

Do not weaken the Skills-only package, add MCP merely to escape this gate, invent billing identity, or claim review/publication/install success while publisher verification is blocked. ChatGPT Web remains a first-class target. MCP/App packaging is a later capability increment, not a release gate.

## Current resume point

1. Resolve or formally clarify the OpenAI publisher-verification payment-method gate through an official supported path.
2. While that external gate is unresolved, run the first real Codex installation/invocation from an ordinary non-Agnir Project. Do not pre-initialize Agnir or pre-create `SVIF.yaml`; validate the actual Svif first-use bootstrap path and then fresh-context resume.
3. When publisher verification becomes available, submit the exact tested Skills-only package, record scan/review evidence, explicitly Publish after approval, and then validate the first personal ChatGPT Web installation/invocation from the universal Plugins Directory.
4. Repair only friction observed from real supported-surface use, then expand surface evidence while keeping the shared Skill and Orchestrator behavior single-sourced.
5. Keep live Cloudflare delivery disabled unless explicitly authorized.

## Evidence checkpoints

- README audience split / first-use Project surface: `.agnir/evidence/2026-09-01-readme-information-architecture.md`.
- Agnir `v0.1.0` compatible operational upgrade: `.agnir/evidence/2026-09-01-agnir-v0.1.0-compatible-upgrade.md`; upgrade revision `c7cd42b6e94556a630570a54e22c72acc97f3ecf`, run `33466389590` success.
- Plugin first-use bootstrap fix: `.agnir/evidence/2026-08-31-plugin-first-use-bootstrap-fix.md`; final behavior baseline `b90d1f8976b0e03d2c5a3b70c9bbb4b032c37724`, run `33384858568` success.
- Personal ChatGPT distribution / publisher-gate checkpoint: `.agnir/evidence/2026-08-31-personal-chatgpt-distribution-checkpoint.md`.
- Plugin MVP hardening checkpoint: `.agnir/evidence/2026-08-31-plugin-mvp-hardening-checkpoint.md`.
- README/localization baseline: `.agnir/evidence/2026-08-28-readme-diagram-localization-checkpoint.md`.
- Founding E2E: `.agnir/evidence/2026-08-28-founding-e2e.md`, run `33143308949` success.

`.agnir/decisions.md` is authoritative for architecture and distribution decisions; `.agnir/next-actions.md` is the canonical ordered resume plan.
