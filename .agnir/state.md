# Svif Current State

Svif is the authoritative active **Project orchestration product** in `iorLab/svif` on `main`. Agnir is the independent founding Continuity Provider in `iorLab/agnir`. The former `iorLab/svif-cloudflare-reference` project is retired. Historical repositories, retired branches, and ZeroLocal material are evidence only; they are not active dependencies, compatibility obligations, or release gates.

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
- Canonical Agnir activation route for this Agent-operable Project:
  `Project root -> AGENTS.md -> README.md / Agnir Project Instructions -> AGNIR.yaml -> declared durable memory`.
- Canonical Svif repository/ref: `iorLab/svif` / `main`.

## Runtime invariants

- Externally driven execution uses `Orchestrator.begin()` / `Orchestrator.complete()`.
- Untrusted model/result payloads cannot self-grant protected authority.
- External actuation requires successful verification for the exact subject plus applicable trusted authority.
- External success requires independent observation before checkpoint.
- Agnir durable continuity remains Project-owned and execution-surface-neutral.
- Detached commits, PR checkouts, temporary branches, forks, mirrors, or other non-authoritative execution copies do not silently become canonical checkpoint targets.

The founding credential-free E2E at `tests/test_founding_e2e.py` proves the orchestration loop through Agnir continuity load -> Orchestrator -> ChatGPT bridge -> trusted authority -> exact-subject Cloudflare actuation through injected fake transport -> independent observation -> Agnir checkpoint -> continuity reload/resume. This is not live Cloudflare delivery evidence.

## Plugin MVP status

Svif has an active **Skill-first Plugin MVP** under `plugin/`.

Distribution surfaces:

- `plugin/plugin.json` — portable Agent Plugins `1.0.0` manifest;
- `plugin/skills/svif/SKILL.md` — shared Svif Project-orchestration Skill;
- `.agents/plugins/marketplace.json` — repository-backed OpenAI/Codex GitHub marketplace catalog mapping to `./plugin`;
- `plugin/.codex-plugin/plugin.json` — additive OpenAI/Codex product metadata that reuses the shared Skill;
- `plugin/README.md` — package, distribution, installation-exercise, and evidence-boundary guidance.

Current Plugin validation surfaces registered in `SVIF.yaml`:

- `tests/test_plugin_package.py`;
- `tests/test_plugin_component_discovery.py`;
- `tests/test_plugin_installation_docs.py`;
- `tests/test_plugin_agnir_discovery.py`;
- `tests/test_plugin_openai_distribution.py`.

The extended hardening loop now covers portable manifest/schema behavior, Agent Skills frontmatter, fixed-component discovery, filesystem containment and failure isolation, OpenAI/Codex marketplace metadata, installation-documentation evidence boundaries, and Agnir activation/discovery semantics including selected-root authority, named failure modes, profile trust, locator confinement, canonical repository/ref, durable environment bindings, checkpoint resumability, activation-contract completeness, and non-destructive `AGENTS.md` repair.

This increment intentionally remains Skill-first. Missing portable `mcp.json` is valid. Future MCP/App packaging is additive only if it reuses the existing ChatGPT Execution Surface and Orchestrator lifecycle without creating a second kernel or weakening authority/continuity boundaries. Target-surface behavior must be exercised before accepting any MCP packaging change that could make the Plugin Desktop-only or otherwise reduce web/client availability.

## Installation-validation boundary

Repository CI currently proves package/conformance, runtime, repository integrity, Agnir discovery guardrails, distribution metadata consistency, and documentation claim boundaries.

**No supported ChatGPT/Codex workspace/client installation has yet been recorded as validated evidence.** GitHub marketplace import configuration, package conformance, repository HEAD resolution, directory appearance, sync state, and CI success are not substitutes for observed client installation and invocation.

Evidence-grade real-client validation should prefer a fixed immutable commit. Record the actual workspace/client import or marketplace result, observed installation/surface status, accepted revision when exposed by the client, invocation, Agnir activation/discovery checks, exact-subject verification, authority provenance, independent observation where external effects occur, and the resulting durable checkpoint. For moving refs, repository HEAD is comparison evidence only; if the client cannot bind invocation to one immutable commit, exact installed-revision provenance remains unconfirmed.

## Documentation and repository baseline

`README.md` and `README.zh-CN.md` are synchronized entry points. Both maintain Architecture Diagram and Runtime / Operation Flow Mermaid diagrams, Agnir Project Instructions, current Plugin/distribution status, and compact plain-text repository trees. Chinese diagrams are comprehension-first rather than literal translations.

`REPOSITORY_TREE.md` is the exhaustive tracked-file map. Architecture/runtime/distribution changes update both README language versions; tracked-file additions/removals/moves or material responsibility changes update `REPOSITORY_TREE.md` in the same change set.

`main` is the only long-lived branch. Retired branch tips are recorded by immutable SHA in `history/BRANCH_ARCHIVE.md`.

## Current implementation gap / resume point

1. **Perform the first real supported OpenAI workspace/client installation through the repository-backed GitHub marketplace path.** Prefer a fixed immutable commit for the evidence run. Capture client-grounded import/sync/installation evidence and invoke `svif` on a real Agnir-initialized Project.
2. **Repair only friction observed in that real exercise.** Do not continue speculative package hardening merely to create changes.
3. **Add remote ChatGPT MCP/App packaging only after real target-surface testing.** It must reuse `ChatGPTExecutionSurface` and `Orchestrator.begin()` / `complete()`, preserve protected-authority separation, and avoid accidental loss of desired ChatGPT web/client availability.
4. **Add broader neutrality evidence** using Agnir storage-neutral and multi-project isolation cases without making GitHub, ChatGPT, or Cloudflare universal Svif kernel dependencies.
5. Keep live Cloudflare delivery disabled unless explicitly authorized; future success requires exact verified-subject delivery plus independent observation.

## Evidence checkpoints

- Plugin MVP hardening checkpoint: `.agnir/evidence/2026-08-31-plugin-mvp-hardening-checkpoint.md`.
  - Validated implementation baseline before checkpoint persistence: `fc90263010ead4e40eb3e22c64584f5ce26f9b7d`.
  - `Svif product checks` run `33318607243`: `completed / success`.
- README/localization: `.agnir/evidence/2026-08-28-readme-diagram-localization-checkpoint.md`.
- Founding E2E: `.agnir/evidence/2026-08-28-founding-e2e.md`, run `33143308949` success.
- Main-only branch cleanup: `.agnir/evidence/2026-08-28-main-only-branch-cleanup-checkpoint.md`.

No new architecture decision is introduced by the 2026-08-31 checkpoint. `.agnir/decisions.md` remains authoritative for architecture and distribution decisions; `.agnir/next-actions.md` remains the canonical ordered resume plan.