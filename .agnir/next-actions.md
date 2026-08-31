# Svif Next Actions

1. **Establish the actual current public/personal ChatGPT publication path for Svif.** The primary audience is individual ChatGPT users, so do not use managed-workspace GitHub marketplace import as the default consumer path. Re-verify the current OpenAI developer requirements that lead to a public Plugins Directory listing, identify the required package/app/submission artifacts, and preserve ChatGPT Web as a first-class supported surface.
2. **Align the bilingual README onboarding and package guidance with that personal-user path.** Keep the Agnir-style minimal user intent, but where ChatGPT provides a product-native directory installation flow, prefer `Plugins Directory -> Svif -> Install` over administrator-oriented marketplace instructions. Keep GitHub marketplace details in advanced/development documentation.
3. **Implement only the missing OpenAI public-distribution surface needed for the personal-user product.** Reuse `integrations/chatgpt/`, `ChatGPTExecutionSurface`, and `Orchestrator.begin()` / `Orchestrator.complete()`; do not create a second execution kernel or move Project truth out of Agnir. Treat any MCP/App packaging that makes the product Desktop-only as unacceptable unless the Principal explicitly accepts that evidenced tradeoff.
4. **Run the first personal ChatGPT installation and invocation exercise on ChatGPT Web.** Use the actual published/available Svif listing, invoke it on a real Agnir-initialized Project, and record exact surface, installation state, revision/version provenance when exposed, Agnir activation/discovery, verification, any authority use, independent observation for external effects, and the resulting durable checkpoint. Package/conformance success is not installation evidence.
5. **Repair only friction observed from real personal-user use, then expand surface evidence.** After the ChatGPT Web baseline, exercise ChatGPT Desktop and Codex, then add Cursor-native distribution metadata/validation while keeping the shared Agent Plugins/Skill implementation single-sourced. Treat DSH/other harnesses as later adapter/bridge pressure unless they become an explicit product priority.
6. **Add broader neutrality evidence** using Agnir's non-repository continuity and multi-project isolation cases without making GitHub, Cloudflare, ChatGPT, Cursor, or another execution environment universal Svif dependencies.
7. Keep live Cloudflare delivery disabled unless explicitly authorized. If authorized later, preserve exact verified-subject delivery and require independent observation before success claims.

## Current Agnir compatibility reference

- Agnir Core compatibility consumed by Svif: `0.1`.
- Repository/filesystem profile: `repository-filesystem/0.1`.
- Agnir repository release SemVer: `0.1.0` (a separate version layer; currently release-ready pending publication).
- Current Agent-operable activation route: `Project root -> AGENTS.md -> README.md / Agnir Project Instructions -> AGNIR.yaml -> declared durable memory`.
- Svif depends on Agnir continuity semantics/profile compatibility, not on Agnir's repository history, GitHub, or Skill repository at runtime.

## Distribution and iteration rules

- `plugin/` is an active product surface and the portable package targets Agent Plugins `1.0.0`.
- `plugin/skills/svif/SKILL.md` remains the shared Svif Project-orchestration workflow; product-specific packaging should reuse it rather than fork behavior.
- `.agents/plugins/marketplace.json` plus `plugin/.codex-plugin/plugin.json` remain additive OpenAI/Codex repository-distribution surfaces, primarily useful for development, Codex, managed workspaces, and validation. They do not supersede portable `plugin/plugin.json` and are not the primary personal ChatGPT onboarding path.
- Repository CI validates package/conformance/distribution properties; do not call personal ChatGPT installation validated until an actual supported personal-user surface has installed and exercised Svif.
- Plugin changes SHOULD be driven by real installation/execution friction whenever possible.
- Distribution MUST NOT reimplement `src/svif/runtime.py`, move Project truth out of the Continuity Provider, or grant protected authority through model-controlled payloads.
- ChatGPT Web availability is a product requirement for the current personal-user target. Any packaging restriction that removes Web support must be surfaced as a deliberate product decision, not hidden as an implementation detail.

## Documentation maintenance rule

- Architecture/runtime/distribution changes are incomplete until affected explanatory sections and diagrams in both `README.md` and `README.zh-CN.md` are updated in the same change set.
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
- OpenAI/Codex GitHub marketplace distribution metadata maps the repository to the same Skill-first Plugin root without duplicating runtime semantics.
- Plugin manifest metadata, schema-constraint tests, deterministic Skill workflow branches, and current Agnir activation/profile references have been hardened after review.
- Bilingual README installation onboarding was simplified to an Agnir-style user-facing install intent in commits `95a95423d74c19a3fb63c027a6be8e8bcc232b5a` and `2a6829834799e4afc291ace370412bb6b9ec2cc7`; product checks run `33356222213` succeeded.
- The personal ChatGPT audience/distribution correction is recorded in `.agnir/evidence/2026-08-31-personal-chatgpt-distribution-checkpoint.md`.
- Main-only branch governance is complete.

## Repository-retirement note

`iorLab/svif-cloudflare-reference` is no longer an active Svif project or dependency. No future Svif work should target it.
