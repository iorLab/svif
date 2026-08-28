# Svif Next Actions

1. **Harden the concrete ChatGPT app/MCP packaging** around `integrations/chatgpt/` and the existing `ChatGPTExecutionSurface` bridge. Preserve the externally driven `Orchestrator.begin()` / `Orchestrator.complete()` control direction, keep authority outside untrusted model payloads, and avoid duplicating kernel semantics in the packaging layer.
2. **Add broader neutrality evidence** after packaging is coherent: a materially non-GitHub/Cloudflare execution/storage case, then multi-project workspace isolation after Agnir's corresponding fixture is ready.
3. Freeze exact Agnir compatibility/version expression only after Agnir Core `0.1` release criteria are concrete.
4. Keep live Cloudflare delivery disabled unless explicitly authorized. If authorized later, preserve exact verified-subject delivery and require independent observation before success claims.
5. Keep incidental branch cleanup deferred until the new Svif version is substantially complete; preserve `legacy/zerolocal-v0.1` unchanged.

## Documentation maintenance rule

Architecture/runtime changes are incomplete until the corresponding diagrams in both `README.md` and `README.zh-CN.md` are updated in the same change set. Localized diagrams are comprehension-first rather than literal translations; important Simplified Chinese nodes must explain both role and responsibility.

## Repository-retirement note

`iorLab/svif-cloudflare-reference` is no longer an active Svif project or dependency. Its useful product behavior is now owned inside `iorLab/svif`; historical evidence is preserved in `history/CLOUDFLARE_REFERENCE.md`. No future Svif work should target it.

## Completed in the current implementation sequence

- Svif product identity corrected and Product Architecture `0.2` frozen around Orchestrator + Continuity Provider + Execution Surface + Capability Provider.
- Minimal executable Orchestrator implemented and CI-proven.
- Concrete Agnir repository/filesystem Continuity Provider implemented.
- ChatGPT structured Execution Surface bridge implemented with `begin()` / `complete()` handoff.
- Cloudflare provider ownership consolidated into `src/svif/capabilities/cloudflare.py` and `integrations/cloudflare/`; the separate Cloudflare reference project is retired from the active architecture.
- English and Simplified Chinese README entry points include synchronized Architecture and Runtime / Operation Flow diagrams; Simplified Chinese nodes are comprehension-first.
- Founding credential-free E2E implemented at `tests/test_founding_e2e.py`, composing Agnir + ChatGPT + Cloudflare through the real Orchestrator boundary with trusted completion-time authority, independent observation, and Agnir checkpoint/resume.
- Product-check run `33143308949` succeeded for the founding path; durable evidence is `.agnir/evidence/2026-08-28-founding-e2e.md`.
- Validation Project #2 retains proven credential-free static verification; protected live delivery remains unproven and disabled.
