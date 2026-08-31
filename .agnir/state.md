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
- `.agents/plugins/marketplace.json` — repository-backed OpenAI/Codex GitHub marketplace catalog mapping to `./plugin`;
- `plugin/.codex-plugin/plugin.json` — additive OpenAI/Codex metadata that reuses the shared Skill;
- `plugin/README.md` — package/distribution/install-validation guidance.

Repository CI proves package/conformance, runtime, repository integrity, Agnir discovery guardrails, distribution metadata consistency, and documentation claim boundaries. It does **not** prove installation or invocation on a particular consumer surface.

The bilingual root READMEs were simplified to an Agnir-style one-line installation intent in commits `95a95423d74c19a3fb63c027a6be8e8bcc232b5a` and `2a6829834799e4afc291ace370412bb6b9ec2cc7`; `Svif product checks` run `33356222213` completed successfully.

## Primary ChatGPT audience and corrected distribution direction

The Principal has clarified that Svif is being built primarily for **individual/personal ChatGPT users**, not managed-workspace administrators.

Therefore the mature ChatGPT consumer path is now targeted as:

`individual ChatGPT user -> public Plugins Directory listing -> install -> invoke Svif in normal ChatGPT use`

The repository-backed GitHub marketplace path remains useful for development, Codex, managed-workspace administration, and validation, but it is **auxiliary rather than the primary consumer onboarding route**.

ChatGPT Web is a first-class target. Packaging that makes Svif Desktop-only is a material regression unless explicitly accepted by the Principal after observed evidence. The exact current OpenAI publication/submission mechanism needed to obtain a public Plugins Directory listing still requires verification against current OpenAI developer documentation; no public/personal ChatGPT installability claim has yet been established.

Evidence and rationale are recorded in `.agnir/evidence/2026-08-31-personal-chatgpt-distribution-checkpoint.md`.

## Current implementation gap / resume point

1. Verify the exact current OpenAI developer publication path that results in a public/personal Plugins Directory listing and identify the required Svif artifacts without assuming managed-workspace import is sufficient.
2. Align `README.md`, `README.zh-CN.md`, and advanced package guidance with that personal-user route while preserving the minimal one-line user-intent philosophy.
3. Implement only the missing public ChatGPT distribution surface, reusing `ChatGPTExecutionSurface` and the existing Orchestrator lifecycle; preserve ChatGPT Web availability.
4. Run the first real **personal ChatGPT Web** installation/invocation exercise on a real Agnir-initialized Project and record installation, invocation, activation/discovery, verification, authority, observation, and checkpoint evidence.
5. Repair observed friction, then expand evidence to ChatGPT Desktop, Codex, and Cursor while keeping the shared Skill/runtime single-sourced.
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
