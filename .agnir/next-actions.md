# Svif Next Actions

1. **Perform the first real supported-client/workspace installation exercise through the repository-backed OpenAI GitHub marketplace path.** Package/conformance/distribution CI is not installation evidence. Import `https://github.com/iorLab/svif` from an eligible workspace, pin or record the exact commit, capture the marketplace import report, then invoke the installed Plugin on a real Agnir-initialized Project and record the exact surface, Agnir activation/discovery path, verification performed, and resulting durable checkpoint.
2. **Repair Plugin workflow or distribution friction from that real exercise.** The repository now carries `.agents/plugins/marketplace.json`, `plugin/.codex-plugin/plugin.json`, and the portable Agent Plugins manifest; tighten them only from observed import errors, bad discovery, missed activation, bad tool selection, weak verification, or resume failures.
3. **Harden the concrete ChatGPT Apps SDK / MCP packaging** as the next additive Plugin component around `integrations/chatgpt/` and the existing `ChatGPTExecutionSurface` bridge. Preserve the externally driven `Orchestrator.begin()` / `Orchestrator.complete()` control direction, keep protected authority outside untrusted model/result payloads, and do not duplicate kernel semantics in the packaging layer.
4. **Add broader neutrality evidence** using Agnir's proven non-repository continuity and multi-project isolation cases as pressure inputs. Do not make GitHub, Cloudflare, or ChatGPT universal Svif dependencies.
5. Keep live Cloudflare delivery disabled unless explicitly authorized. If authorized later, preserve exact verified-subject delivery and require independent observation before success claims.

## Current Agnir compatibility reference

- Agnir Core compatibility consumed by Svif: `0.1`.
- Repository/filesystem profile: `repository-filesystem/0.1`.
- Agnir repository release SemVer: `0.1.0` (a separate version layer; currently release-ready pending publication).
- Current Agent-operable activation route: `Project root -> AGENTS.md -> README.md / Agnir Project Instructions -> AGNIR.yaml -> declared durable memory`.
- Svif depends on Agnir continuity semantics/profile compatibility, not on Agnir's repository history, GitHub, or Skill repository at runtime.

## Plugin-first iteration rule

- `plugin/` is an active product surface.
- The portable package targets Agent Plugins `1.0.0` and is intentionally Skill-first.
- `.agents/plugins/marketplace.json` plus `plugin/.codex-plugin/plugin.json` are additive OpenAI/Codex distribution surfaces; they do not supersede portable `plugin/plugin.json` and do not move runtime or continuity authority into distribution metadata.
- Repository CI validates package/conformance/distribution properties; do not call client installation validated until an actual supported client/workspace has imported and exercised the exact revision.
- Plugin changes SHOULD be driven by real execution or import failures and usability pressure whenever possible.
- Distribution MUST NOT reimplement `src/svif/runtime.py`, move Project truth out of the Continuity Provider, or grant protected authority through model-controlled payloads.
- The future `mcp.json` component is additive and becomes part of the Plugin only when it can reuse existing Svif boundaries cleanly.

## Documentation maintenance rule

- Architecture/runtime/distribution changes are incomplete until the corresponding diagrams and affected explanatory sections in both `README.md` and `README.zh-CN.md` are updated in the same change set.
- Localized diagrams are comprehension-first rather than literal translations; important Simplified Chinese nodes explain both role and responsibility.
- README repository trees remain compact navigation views.
- `REPOSITORY_TREE.md` is the exhaustive file-level map. Tracked file additions/removals/moves or material responsibility changes must update it in the same change set; if the compact tree is also affected, both README language versions must update as well.

## Branch governance

- `main` is the only long-lived branch.
- Historical predecessor and retired work is indexed by immutable commit SHA in `history/BRANCH_ARCHIVE.md`; live legacy/feature/fix/tmp branch refs are not retained.

## Completed in the current implementation sequence

- Product Architecture `0.2` frozen around Orchestrator + Continuity Provider + Execution Surface + Capability Provider.
- Minimal executable Orchestrator implemented and CI-proven.
- Concrete Agnir repository/filesystem Continuity Provider implemented.
- ChatGPT structured Execution Surface bridge implemented with `begin()` / `complete()` handoff.
- Cloudflare provider ownership consolidated into `src/svif/capabilities/cloudflare.py` and `integrations/cloudflare/`.
- English and Simplified Chinese README entry points include synchronized Architecture and Runtime / Operation Flow diagrams.
- Founding credential-free E2E implemented at `tests/test_founding_e2e.py`.
- Skill-first Plugin MVP exists under `plugin/` using Agent Plugins `1.0.0` packaging.
- OpenAI/Codex GitHub marketplace distribution metadata now maps the repository to the same Skill-first Plugin root without duplicating runtime semantics.
- Plugin manifest metadata, schema-constraint tests, deterministic Skill workflow branches, and current Agnir activation/profile references have been hardened after review.
- Main-only branch governance is complete.

## Repository-retirement note

`iorLab/svif-cloudflare-reference` is no longer an active Svif project or dependency. No future Svif work should target it.
