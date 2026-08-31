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

The exact current OpenAI publication path has been verified against current OpenAI developer documentation:

- public Plugin submission may be **Skills only**;
- Skills-only publication uses the OpenAI Plugin manifest plus the bundled `skills/` tree and does not require MCP/App packaging;
- submission requires an OpenAI Platform organization where the submitter has **Apps Management: Write** and a verified individual developer or business identity;
- the developer creates a **Skills only** submission, uploads the final tested bundle, supplies listing metadata/review cases/availability/release notes/attestations, and submits for review;
- approval does not publish automatically; the approved version must be explicitly published;
- after publication the Plugin can appear in the universal Plugins Directory shared by ChatGPT and Codex.

The repository is aligned to this route:

- `.codex-plugin/plugin.json` listing metadata is within the currently tested public-directory limits;
- `plugin/README.md` contains public submission prerequisites, proposed listing metadata, five positive and three negative review cases, and evidence boundaries;
- `README.md` and `README.zh-CN.md` make personal ChatGPT / universal Plugins Directory the primary consumer onboarding model and clearly state that Svif is not publicly listed yet;
- repository marketplace import remains auxiliary for development, Codex, managed workspaces, and secondary validation.

### Current external publisher blocker

A real publisher-verification attempt has now reached the OpenAI Platform organization verification flow. The Platform exposed the individual-developer verification option, but beginning verification required a valid **default payment method** first. The currently available payment method was rejected by the Platform, so individual developer verification could not proceed and no Plugin submission was created.

This is currently treated as an **external publisher/account eligibility blocker**, not evidence of a Svif package, Skill, Orchestrator, or ChatGPT integration defect. No card number, billing address, organization identifier, or other private payment/account data is stored in repository state or evidence.

The public ChatGPT release remains submission-ready on the repository side. Do not weaken the Skills-only package, add MCP merely to escape this gate, invent billing identity, or claim review/publication/install success while publisher verification is blocked. Resolve the account gate through an official OpenAI-supported path or a legitimately accepted payment method when available.

ChatGPT Web remains a first-class target. MCP/App packaging is a later capability increment, not a release gate. No public/personal ChatGPT installation claim has yet been established.

Evidence and rationale are recorded in `.agnir/evidence/2026-08-31-personal-chatgpt-distribution-checkpoint.md`.

## Current implementation gap / resume point

1. **Resolve or formally clarify the OpenAI publisher-verification payment-method gate.** Prefer official OpenAI support guidance or a legitimately supported payment method when available. Do not use false billing identity or unsupported circumvention. Keep the exact tested Skills-only submission package unchanged unless the portal itself reports package friction.
2. **While the public ChatGPT submission is externally blocked, continue real surface validation instead of stalling the project.** Exercise the repository-backed Codex installation/invocation path on an Agnir-initialized Project with real checkpoint/resume evidence, then add/test Cursor-native distribution metadata while preserving the same shared `plugin/skills/svif/SKILL.md` implementation.
3. **When publisher verification becomes available, resume the public/personal ChatGPT path immediately.** Create the `Skills only` submission from the exact tested package, record automated scan/review evidence, repair only observed review friction, then explicitly Publish after approval.
4. Verify the exact Svif listing in the universal Plugins Directory and run the first real **personal ChatGPT Web** installation/invocation exercise, including installation state, activation/discovery, verification, authority, observation, durable checkpoint, and fresh-context resume evidence.
5. Repair observed personal-user friction, then expand evidence across ChatGPT Desktop and other compatible execution surfaces while keeping runtime and Skill behavior single-sourced.
6. Add broader execution/storage neutrality evidence without turning any current platform/provider into a universal kernel dependency.
7. Keep live Cloudflare delivery disabled unless explicitly authorized.

## Evidence checkpoints

- Personal ChatGPT distribution / publisher-gate checkpoint: `.agnir/evidence/2026-08-31-personal-chatgpt-distribution-checkpoint.md`.
- Plugin MVP hardening checkpoint: `.agnir/evidence/2026-08-31-plugin-mvp-hardening-checkpoint.md`.
  - Validated implementation baseline before checkpoint persistence: `fc90263010ead4e40eb3e22c64584f5ce26f9b7d`.
  - `Svif product checks` run `33318607243`: `completed / success`.
- README/localization: `.agnir/evidence/2026-08-28-readme-diagram-localization-checkpoint.md`.
- Founding E2E: `.agnir/evidence/2026-08-28-founding-e2e.md`, run `33143308949` success.
- Main-only branch cleanup: `.agnir/evidence/2026-08-28-main-only-branch-cleanup-checkpoint.md`.

`.agnir/decisions.md` is authoritative for architecture and distribution decisions; `.agnir/next-actions.md` is the canonical ordered resume plan.
