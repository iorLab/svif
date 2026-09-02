# Svif Next Actions

1. **Retain the release branch until cleanup is explicitly confirmed.** Record and report its final remote tip after the post-release checkpoint reaches `main`; do not delete the local or remote branch without the Principal's confirmation.
2. **Continue the separate public/personal ChatGPT path.** Resolve or formally clarify the publisher-verification gate, then submit the exact tested Skills-only package to the universal Plugins Directory. Record scan/review evidence, explicitly Publish after approval, and validate the first individual-user ChatGPT Web installation without conflating it with the Repository Preview.
3. **Use a new Preview tag for any fix.** Keep `v0.2.0-preview.1` immutable; repair observed defects into `v0.2.0-preview.2` rather than moving the released tag.
4. **Repair only observed friction, then expand neutrality/surface evidence.** Keep `plugin/skills/svif/SKILL.md` single-sourced; add no MCP merely for publication. Add broader non-repository and multi-project evidence without making GitHub, Cloudflare, ChatGPT, Cursor, or another execution environment universal dependencies.
5. Keep live Cloudflare delivery disabled unless explicitly authorized. If authorized later, preserve exact verified-subject delivery and require independent observation before success claims.

## Current Agnir compatibility reference

- Agnir Core compatibility consumed by Svif: `0.1`.
- Repository/filesystem profile: `repository-filesystem/0.1`.
- Agnir repository release SemVer: stable `0.1.1`, formally published as `v0.1.1`.
- Target-main Svif Project operational provenance: `agnir-agent-skill` release `0.1.1` from `iorLab/agnir`, immutable applied revision `e9712357ab590e5c1e5357b3cf3219d07d789aff`.
- Current Agent-operable activation route: `Project root -> AGENTS.md -> README.md / Agnir Project Instructions -> AGNIR.yaml -> declared durable memory`.
- Svif depends on Agnir continuity semantics/profile compatibility, not on Agnir's repository history, GitHub, or Skill repository at runtime.

## Distribution and iteration rules

- `plugin/` is an active product surface and the portable package targets Agent Plugins `1.0.0`.
- `plugin/skills/svif/SKILL.md` remains the shared Svif Project-orchestration workflow; product-specific packaging must reuse it rather than fork behavior.
- The initial public ChatGPT release is deliberately **Skills only**. Current OpenAI public submission accepts this shape directly; MCP/App packaging is not a publication prerequisite.
- `plugin/.codex-plugin/plugin.json` carries the current OpenAI/Codex public-listing metadata and points to the same `skills/` implementation.
- `.agents/plugins/marketplace.json` is the supported self-distributed `v0.2.0-preview.1` route for Codex CLI and ChatGPT desktop/Codex. It remains separate from universal-directory publication and personal ChatGPT Web onboarding.
- Repository CI validates package/conformance/distribution properties; do not call personal ChatGPT installation validated until an actual individual-user ChatGPT surface has installed and exercised the published Plugin.
- Publisher/account verification gates are external release constraints. They must not be mistaken for package/runtime failures or used as justification for speculative MCP/App changes.
- Plugin changes SHOULD be driven by real submission, installation, or execution friction whenever possible.
- **First-use onboarding is a Svif product responsibility.** When the selected Project is genuinely uninitialized and no durable binding chooses another Continuity Provider, Svif's founding repository/filesystem path establishes Agnir Core `0.1` / `repository-filesystem/0.1` continuity plus a matching minimal `project-binding/0.2` `SVIF.yaml` using one stable Project identity. A user MUST NOT have to pre-initialize Agnir as a prerequisite for first Svif use.
- Partial/broken Agnir/Svif artifacts are repair cases, not clean bootstrap cases. An intentionally configured different Continuity Provider must not be overwritten with Agnir.
- The first-use bootstrap consumes Agnir protocol/profile semantics through the founding Continuity Provider integration and must not make the Agnir Skill repository, prior installation chat, GitHub, or another execution surface a runtime prerequisite.
- Distribution MUST NOT reimplement `src/svif/runtime.py`, move Project truth out of the Continuity Provider, or grant protected authority through model-controlled payloads.
- ChatGPT Web availability is a product requirement for the current personal-user target. Any future packaging restriction that removes Web support must be surfaced as a deliberate product decision, not hidden as an implementation detail.

### Auxiliary repository-marketplace evidence rule

The GitHub marketplace path remains a useful secondary validation channel. **Package/conformance/distribution CI is not installation evidence.** For a revision-sensitive marketplace exercise, record the immutable commit SHA actually invoked when the client exposes enough evidence to establish it. Treat a repository ref's current SHA only as comparison evidence; when the surface cannot bind invocation to one immutable commit, preserve exact installed-revision provenance as unconfirmed.

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
- OpenAI/Codex repository marketplace metadata maps to the same Skill-first Plugin root without duplicating runtime semantics.
- The personal ChatGPT audience/distribution correction is recorded in `.agnir/evidence/2026-08-31-personal-chatgpt-distribution-checkpoint.md`.
- Current OpenAI public submission requirements have been re-verified: Skills-only public Plugins are accepted; the repository manifest, README guidance, listing metadata, and review-case preparation have been aligned to that route.
- A real publisher verification attempt reached the individual-developer verification flow but was blocked at the required accepted-default-payment-method gate before verification/submission. This is recorded as an external release blocker without storing private payment/account data.
- Svif first-use onboarding now handles an ordinary non-Agnir Project without requiring manual Agnir pre-initialization; regression pressure is `tests/test_plugin_first_use_bootstrap.py` and durable evidence is `.agnir/evidence/2026-08-31-plugin-first-use-bootstrap-fix.md`.
- The target-main candidate upgrades Svif's Agnir operational baseline compatibly to stable `v0.1.1`; `AGNIR.yaml` records immutable provenance without changing Core/profile compatibility, Project identity, memory locators, or `SVIF.yaml`.
- The immutable candidate passed Codex CLI and ChatGPT desktop/Codex installation, bootstrap, checkpoint, initialized-Project idempotency, and fresh-context recovery acceptance before release.
- Svif `v0.2.0-preview.1` is released from authoritative `main` as a GitHub Prerelease; immutable tag installation resolves to the verified release commit and exposes the Skills-only Plugin as installed/enabled.
- Main-only branch governance is complete.

## Repository-retirement note

The former `iorLab/svif-cloudflare-reference` project is retired. No future Svif work should target it.
