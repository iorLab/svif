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
- Canonical Agnir activation route for this Agent-operable Project: `Project root -> AGENTS.md -> README.md / Agnir Project Instructions -> AGNIR.yaml -> declared durable memory`.
- Canonical Svif repository/ref: `iorLab/svif` / `main`.

## Runtime baseline

- Externally driven execution uses `Orchestrator.begin()` / `Orchestrator.complete()`.
- Untrusted model/result payloads cannot self-grant protected authority.
- External actuation requires successful verification for the exact subject plus applicable trusted authority.
- External success requires independent observation before checkpoint.
- Agnir durable continuity remains Project-owned and execution-surface-neutral.
- Detached commits, PR checkouts, temporary branches, forks, mirrors, or other non-authoritative copies do not silently become canonical checkpoint targets.

`tests/test_founding_e2e.py` proves the credential-free orchestration loop through Agnir continuity load -> Orchestrator -> ChatGPT bridge -> trusted authority -> exact-subject Cloudflare actuation through injected fake transport -> independent observation -> Agnir checkpoint -> continuity reload/resume. This is not live Cloudflare production-delivery evidence.

## Plugin and distribution baseline

Svif has an active **Skill-first Plugin MVP** under `plugin/`:

- `plugin/plugin.json` — portable Agent Plugins `1.0.0` manifest;
- `plugin/skills/svif/SKILL.md` — shared Svif Project-orchestration Skill;
- `plugin/.codex-plugin/plugin.json` — OpenAI/Codex manifest that reuses the shared Skill and carries public-listing metadata;
- `.agents/plugins/marketplace.json` — auxiliary repository-backed OpenAI/Codex marketplace catalog mapping to `./plugin`;
- `plugin/README.md` — public submission, package/distribution, installation, review-case, and evidence-boundary guidance.

Repository CI proves package/conformance, runtime, repository integrity, Agnir discovery guardrails, distribution metadata consistency, and documentation claim boundaries. It does **not** prove OpenAI review, publication, directory appearance, installation, or invocation on a consumer surface.

## Personal ChatGPT public distribution status

The Principal's primary ChatGPT audience is **individual/personal ChatGPT users**. The mature consumer path is:

`individual ChatGPT user -> universal Plugins Directory -> install -> invoke Svif in normal ChatGPT use`

The exact current OpenAI publication path has now been verified against current OpenAI developer documentation:

- public Plugin submission may be **Skills only**;
- Skills-only publication uses the OpenAI Plugin manifest plus the bundled `skills/` tree and does not require MCP/App packaging;
- submission requires an OpenAI Platform organization where the submitter has **Apps Management: Write** and a verified individual developer or business identity;
- the developer creates a **Skills only** submission, uploads the final tested bundle, supplies listing metadata/review cases/availability/release notes/attestations, and submits for review;
- approval does not publish automatically; the approved version must be explicitly published;
- after publication the Plugin can appear in the universal Plugins Directory shared by ChatGPT and Codex.

The repository has been aligned to this route:

- `.codex-plugin/plugin.json` listing metadata was tightened to current public-directory limits;
- the starter prompt and short description were shortened to submission-safe lengths;
- `plugin/README.md` now contains public submission prerequisites, proposed listing metadata, five positive and three negative review cases, and evidence boundaries;
- `README.md` and `README.zh-CN.md` now make personal ChatGPT / universal Plugins Directory the primary consumer onboarding model and clearly state that Svif is not publicly listed yet;
- repository marketplace import remains auxiliary for development, Codex, managed workspaces, and secondary validation.

ChatGPT Web remains a first-class target. MCP/App packaging is a later capability increment, not a release gate. No public/personal ChatGPT installation claim has yet been established.

Evidence and rationale are recorded in `.agnir/evidence/2026-08-31-personal-chatgpt-distribution-checkpoint.md`.

## Current implementation gap / resume point

1. Use a publisher OpenAI Platform organization with **Apps Management: Write** plus verified individual/business identity to create a `Skills only` Plugin submission using the exact tested Svif package.
2. Record automated skill-scan and review evidence; repair only observed submission friction.
3. After approval, explicitly Publish and verify the exact Svif listing in the universal Plugins Directory.
4. Run the first real **personal ChatGPT Web** installation/invocation exercise on a real Agnir-initialized Project and record installation, invocation, activation/discovery, verification, authority, observation, checkpoint, and fresh-context resume evidence.
5. Repair observed personal-user friction, then expand evidence to ChatGPT Desktop, Codex, and Cursor while keeping the shared Skill/runtime single-sourced.
6. Add broader execution/storage neutrality evidence without turning any current platform/provider into a universal kernel dependency.
7. Keep live Cloudflare delivery disabled unless explicitly authorized.

## Evidence checkpoints

- Personal ChatGPT distribution checkpoint: `.agnir/evidence/2026-08-31-personal-chatgpt-distribution-checkpoint.md`.
- Plugin MVP hardening checkpoint: `.agnir/evidence/2026-08-31-plugin-mvp-hardening-checkpoint.md`.
  - Validated implementation baseline before checkpoint persistence: `fc90263010ead4e40eb3e22c64584f5ce26f9b7d`.
  - `Svif product checks` run `33318607243`: `completed / success`.
- README/localization: `.agnir/evidence/2026-08-28-readme-diagram-localization-checkpoint.md`.
- Founding E2E: `.agnir/evidence/2026-08-28-founding-e2e.md`, run `33143308949` success.
- Main-only branch cleanup: `.agnir/evidence/2026-08-28-main-only-branch-cleanup-checkpoint.md`.

`.agnir/decisions.md` is authoritative for architecture and distribution decisions; `.agnir/next-actions.md` is the canonical ordered resume plan.
