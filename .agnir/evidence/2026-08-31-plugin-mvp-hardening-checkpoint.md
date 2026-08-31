# Svif Plugin MVP hardening checkpoint — 2026-08-31

## Scope

This checkpoint closes the extended Plugin-MVP hardening loop and records the exact durable resume boundary. It does not claim a real ChatGPT/Codex client installation.

## Validated implementation baseline

- Repository: `iorLab/svif`
- Authoritative ref: `main`
- Validated pre-checkpoint head: `fc90263010ead4e40eb3e22c64584f5ce26f9b7d`
- GitHub Actions workflow: `Svif product checks`
- Run: `33318607243`
- Result: `completed / success`
- Jobs covered by the workflow remain the repository-integrity, runtime-kernel, and portable-contract surfaces.

## Current Plugin product state

Svif has an active Skill-first Plugin MVP under `plugin/`:

- `plugin/plugin.json` is the portable Agent Plugins `1.0.0` manifest.
- `plugin/skills/svif/SKILL.md` is the shared Svif orchestration Skill.
- `.agents/plugins/marketplace.json` is the repository-backed OpenAI/Codex GitHub marketplace catalog.
- `plugin/.codex-plugin/plugin.json` is additive OpenAI/Codex distribution metadata and reuses the shared Skill.
- No `mcp.json` is required for the current portable Skill-first MVP.
- Future MCP/App packaging is additive only and must reuse the existing ChatGPT Execution Surface and `Orchestrator.begin()` / `Orchestrator.complete()` lifecycle rather than duplicating kernel semantics.

## Hardening completed in this loop

The repository now has regression coverage for:

- Agent Plugins manifest constraints, forward-compatible diagnostics, component discovery, filesystem containment, and failure isolation;
- Agent Skills frontmatter and Skill-root rules;
- OpenAI/Codex marketplace and product-specific distribution metadata without runtime shadowing;
- installation-documentation evidence boundaries, including workspace import fields, moving-ref provenance, synchronization/display distinctions, retained last-working versions, propagation delay, and MCP surface-availability caveats;
- Agnir `0.1` / `repository-filesystem/0.1` activation and discovery semantics, including selected-root authority, full named discovery failures, trusted profile selection, locator confinement, canonical repository/ref boundaries, environment-binding durability, post-checkpoint cold-start resumability, Agent activation-contract completeness, and non-destructive `AGENTS.md` repair;
- preservation of exact-subject verification, trusted protected authority, independent post-effect observation, and Project-owned canonical continuity.

## Authority and continuity invariants

These remain non-negotiable:

1. Orchestrator semantics remain canonical in `src/svif/runtime.py`; distribution must not implement a second kernel.
2. Untrusted model/result payloads cannot self-grant protected authority.
3. An external effect requires successful verification for the exact subject and applicable trusted authority.
4. External success requires independent observation before checkpoint.
5. Agnir durable continuity remains Project-owned and execution-surface-neutral.
6. Agent-operable repository/filesystem activation is `Project root -> AGENTS.md -> README.md / Agnir Project Instructions -> AGNIR.yaml -> declared durable memory`.
7. `iorLab/svif` on `main` is the canonical repository/ref for Svif continuity; detached, fork, mirror, PR, or temporary execution copies do not silently become canonical checkpoint targets.

## Installation-validation boundary

Repository CI currently proves package/conformance, repository integrity, runtime behavior, Agnir discovery guardrails, distribution metadata consistency, and documentation claim boundaries.

It does **not** prove that a supported ChatGPT/Codex workspace/client has imported, installed, surfaced, invoked, and exercised this exact Plugin revision.

A real installation-validation record must be client-grounded. Prefer a fixed immutable commit for the evidence run. Capture the actual workspace/client import or marketplace result, installation/surface status, accepted revision when exposed by the client, invocation, Agnir activation/discovery checks, exact-subject verification, authority provenance, independent observation where an external effect occurs, and the resulting durable checkpoint. Repository branch HEAD is not a substitute for client-exposed installed/invoked revision evidence.

## Durable resume point

1. Perform the first real supported OpenAI workspace/client marketplace installation and invocation exercise, preferably pinned to an immutable commit.
2. Repair only friction actually observed in that exercise; do not manufacture speculative conformance changes.
3. Consider MCP/App packaging only after real target-surface testing confirms the product trade-off, including any Desktop-only effect.
4. Continue broader neutrality evidence later without making GitHub, ChatGPT, or Cloudflare universal kernel dependencies.
5. Keep live Cloudflare delivery disabled unless explicitly authorized and independently observed.

No new architecture decision is introduced by this checkpoint; existing `.agnir/decisions.md` remains authoritative for architecture and distribution decisions.