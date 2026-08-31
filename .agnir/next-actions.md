# Svif Next Actions

1. **Resolve or formally clarify the OpenAI publisher-verification payment-method gate.** The public/personal ChatGPT path remains the target and the repository-side Skills-only package is submission-ready, but the real publisher flow is currently blocked before individual developer verification because the Platform requires an accepted default payment method. Prefer official OpenAI support guidance or a legitimately supported payment method when available. Do not use false billing identity or unsupported circumvention, and do not modify the Svif package merely to work around an account-level gate.
2. **While that external gate is unresolved, continue real installation evidence on supported non-publication routes instead of stalling the project.** Exercise the repository-backed Codex installation/invocation path on an Agnir-initialized Project, record the actual client/surface, accepted revision provenance when exposed, Agnir activation/discovery, verification, checkpoint, and fresh-context resume. Then add and test Cursor-native distribution metadata while keeping `plugin/skills/svif/SKILL.md` single-sourced.
3. **When publisher verification becomes available, submit the tested Skills-only Svif Plugin through the OpenAI Platform plugin submission portal.** The public/personal ChatGPT path uses the universal Plugins Directory shared by ChatGPT and Codex. Use an OpenAI Platform organization where the submitter has **Apps Management: Write** and a verified individual developer or business identity. Create `Skills only`, upload the exact tested Plugin bundle containing `.codex-plugin/plugin.json` plus `skills/`, and use the repository-prepared listing metadata and review cases in `plugin/README.md`.
4. **Record the portal's automated scan and review outcome as external evidence.** Submission is not publication. Preserve the submitted version/revision when the portal exposes it, the skill safety/security scan result, review status, reviewer feedback, and any changes required by review. Repair only observed submission/review friction and resubmit the exact corrected package.
5. **After approval, explicitly Publish the approved version and run the first personal ChatGPT Web validation.** Verify that Svif appears in the universal Plugins Directory under the exact publication name, then install it from an individual-user ChatGPT surface, invoke it on a real Agnir-initialized Project, and record exact surface, observed installation state, version/revision provenance when exposed, Agnir activation/discovery, verification, any trusted authority use, independent observation for external effects, durable checkpoint, and fresh-context resume. Repository CI, review approval, or directory appearance alone is not installation evidence.
6. **Repair only friction observed from real personal-user use, then expand surface evidence.** After the ChatGPT Web baseline, exercise ChatGPT Desktop and any remaining Codex/Cursor scenarios while keeping the shared Agent Plugins/Skill implementation single-sourced. Treat DSH/other harnesses as later adapter/bridge pressure unless they become an explicit product priority.
7. **Add broader neutrality evidence** using Agnir's non-repository continuity and multi-project isolation cases without making GitHub, Cloudflare, ChatGPT, Cursor, or another execution environment universal Svif dependencies.
8. Keep live Cloudflare delivery disabled unless explicitly authorized. If authorized later, preserve exact verified-subject delivery and require independent observation before success claims.

## Current Agnir compatibility reference

- Agnir Core compatibility consumed by Svif: `0.1`.
- Repository/filesystem profile: `repository-filesystem/0.1`.
- Agnir repository release SemVer: `0.1.0` (a separate version layer; currently release-ready pending publication).
- Current Agent-operable activation route: `Project root -> AGENTS.md -> README.md / Agnir Project Instructions -> AGNIR.yaml -> declared durable memory`.
- Svif depends on Agnir continuity semantics/profile compatibility, not on Agnir's repository history, GitHub, or Skill repository at runtime.

## Distribution and iteration rules

- `plugin/` is an active product surface and the portable package targets Agent Plugins `1.0.0`.
- `plugin/skills/svif/SKILL.md` remains the shared Svif Project-orchestration workflow; product-specific packaging must reuse it rather than fork behavior.
- The initial public ChatGPT release is deliberately **Skills only**. Current OpenAI public submission accepts this shape directly; MCP/App packaging is not a publication prerequisite.
- `plugin/.codex-plugin/plugin.json` carries the current OpenAI/Codex public-listing metadata and points to the same `skills/` implementation.
- `.agents/plugins/marketplace.json` remains an auxiliary repository-distribution surface for development, Codex, managed workspaces, and validation. It is not the primary personal ChatGPT onboarding path.
- Repository CI validates package/conformance/distribution properties; do not call personal ChatGPT installation validated until an actual individual-user ChatGPT surface has installed and exercised the published Plugin.
- Publisher/account verification gates are external release constraints. They must not be mistaken for package/runtime failures or used as justification for speculative MCP/App changes.
- Plugin changes SHOULD be driven by real submission, installation, or execution friction whenever possible.
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
- Main-only branch governance is complete.

## Repository-retirement note

The former `iorLab/svif-cloudflare-reference` project is retired. No future Svif work should target it.
