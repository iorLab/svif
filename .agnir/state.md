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

## Active contracts and release candidate

- Svif product line: `0.2`; the current target-main candidate is `0.2.0-preview.1`.
- Project Binding: `project-binding/0.2`.
- Software Delivery profile: `software-delivery/0.2`.
- Capability Adapter: `capability-adapter/0.2`.
- Evidence record: `evidence-record/0.2`.
- Repository/filesystem binding serialization: `SVIF.yaml`.
- Agnir Core compatibility: `0.1`.
- Agnir discovery profile: `repository-filesystem/0.1`.
- The target-main candidate applies Agnir stable repository release `0.1.1` from `iorLab/agnir`, immutable revision `e9712357ab590e5c1e5357b3cf3219d07d789aff`, as a compatible operational upgrade recorded in `AGNIR.yaml`.
- Canonical Agnir activation route: `Project root -> AGENTS.md -> README.md / Agnir Project Instructions -> AGNIR.yaml -> declared durable memory`.
- Canonical Svif repository/ref: `iorLab/svif` / `main`.

The Agnir `v0.1.1` candidate upgrade is a **compatible operational upgrade**, not a migration: Core `0.1` and `repository-filesystem/0.1` are unchanged, while Project identity, memory locators/content, unrelated manifest extensions, and `SVIF.yaml` remain preserved. Its execution-surface activation handoff repair is directly relevant to the Repository Preview installation path.

Work is staged on short-lived branch `release/svif-v0.2.0-preview.1`. That branch is a candidate for the declared authoritative `main`; it is not a second continuity authority. No Preview tag, GitHub Prerelease, supported-client installation baseline, or public-directory publication has yet been claimed by this candidate state.

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

Svif has a **Skills-only `v0.2.0-preview.1` Plugin candidate** under `plugin/`:

- `plugin/plugin.json` — portable Agent Plugins `1.0.0` manifest;
- `plugin/skills/svif/SKILL.md` — shared Svif Project-orchestration Skill;
- `plugin/.codex-plugin/plugin.json` — OpenAI/Codex manifest reusing the same Skill and carrying public-listing metadata;
- `.agents/plugins/marketplace.json` — repository-backed Preview catalog for Codex CLI and ChatGPT desktop/Codex;
- `plugin/README.md` — submission, installation, review-case, and evidence-boundary guidance.

First-use onboarding is a Svif product responsibility. For a genuinely uninitialized ordinary Project, the shared Skill establishes one stable Project identity, Agnir Core `0.1` / `repository-filesystem/0.1` continuity, a matching minimal `project-binding/0.2` `SVIF.yaml`, then fresh-activates and continues the original task. Partial/broken Agnir/Svif artifacts remain repair cases, and a Project intentionally bound to another Continuity Provider is not overwritten with Agnir.

Repository checks can prove package/conformance, runtime, repository integrity, Agnir discovery guardrails, distribution metadata consistency, documentation claim boundaries, and first-use bootstrap regression behavior. They do **not** prove supported-client installation, OpenAI review, universal-directory publication, or personal ChatGPT invocation.

## Repository Preview distribution status

The copy-ready user intent remains exactly:

`Install and enable Svif for this Project: https://github.com/iorLab/svif`

The installer owns fixed-tag resolution, marketplace registration, client-capability checks, first-use bootstrap, and evidence. The candidate Preview supports Codex CLI and ChatGPT desktop/Codex through the repository marketplace. Moving `main` is not a released Preview, and ChatGPT Web/mobile cannot install this repository Preview through the prompt alone.

## Personal ChatGPT public distribution status

The primary ChatGPT audience is individual/personal users. The mature consumer path is:

`individual ChatGPT user -> universal Plugins Directory -> install -> invoke Svif in normal ChatGPT use`

Svif is not publicly listed yet. The repository-side Skills-only package is aligned to the current OpenAI public-submission route, but the real publisher flow is externally blocked before individual developer verification because the Platform requires an accepted default payment method. This is an account/publisher eligibility blocker, not evidence of a Svif package, Skill, Orchestrator, or runtime defect.

Do not weaken the Skills-only package, add MCP merely to escape this gate, invent billing identity, or claim review/publication/install success while publisher verification is blocked. ChatGPT Web remains a first-class target. MCP/App packaging is a later capability increment, not a release gate.

## Current resume point

1. Finish static validation of the `v0.2.0-preview.1` candidate and push one coherent candidate revision from the short-lived release branch.
2. Require successful CI, then use the immutable candidate SHA to validate the one-line install intent in both Codex CLI and ChatGPT desktop/Codex from an ordinary non-Agnir Project; also validate idempotent resume on an initialized Project.
3. Only after both supported surfaces pass, reconcile the target-main checkpoint, advance authoritative `main`, create immutable tag `v0.2.0-preview.1`, publish a GitHub Prerelease, and repeat a tag-based smoke.
4. Record the observed release/tag/install evidence in a post-release target-main checkpoint. Do not move a failed tag; repair into `preview.2`.
5. Keep the later public/personal ChatGPT submission path separate: resolve the publisher gate, submit the same Skills-only package, explicitly Publish after approval, then validate the universal Plugins Directory and personal ChatGPT Web.
6. Keep live Cloudflare delivery disabled unless explicitly authorized.

## Evidence checkpoints

- Repository Preview candidate: `.agnir/evidence/2026-09-02-svif-v0.2.0-preview.1-candidate.md`; static package/contract/runtime/Skill checks pass, while supported-client installation and release remain pending.
- Agnir `v0.1.1` compatible operational upgrade candidate: `.agnir/evidence/2026-09-02-agnir-v0.1.1-compatible-upgrade.md`; stable tag `e9712357ab590e5c1e5357b3cf3219d07d789aff`, Core/profile unchanged.
- README audience split / first-use Project surface: `.agnir/evidence/2026-09-01-readme-information-architecture.md`.
- Previous Agnir `v0.1.0` compatible operational upgrade: `.agnir/evidence/2026-09-01-agnir-v0.1.0-compatible-upgrade.md`; upgrade revision `c7cd42b6e94556a630570a54e22c72acc97f3ecf`, run `33466389590` success.
- Plugin first-use bootstrap fix: `.agnir/evidence/2026-08-31-plugin-first-use-bootstrap-fix.md`; final behavior baseline `b90d1f8976b0e03d2c5a3b70c9bbb4b032c37724`, run `33384858568` success.
- Personal ChatGPT distribution / publisher-gate checkpoint: `.agnir/evidence/2026-08-31-personal-chatgpt-distribution-checkpoint.md`.
- Plugin MVP hardening checkpoint: `.agnir/evidence/2026-08-31-plugin-mvp-hardening-checkpoint.md`.
- README/localization baseline: `.agnir/evidence/2026-08-28-readme-diagram-localization-checkpoint.md`.
- Founding E2E: `.agnir/evidence/2026-08-28-founding-e2e.md`, run `33143308949` success.

`.agnir/decisions.md` is authoritative for architecture and distribution decisions; `.agnir/next-actions.md` is the canonical ordered resume plan.
