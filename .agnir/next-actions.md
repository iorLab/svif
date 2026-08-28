# Svif Next Actions

1. **Build one in-repository founding E2E scenario** wiring the existing Agnir Continuity Provider, ChatGPT Execution Surface bridge, and Svif-owned Cloudflare Capability Provider through the Orchestrator. Use fake/non-secret transport by default; live provider actuation remains separately gated.
2. **Harden the concrete ChatGPT app/MCP packaging** around `integrations/chatgpt/` without duplicating kernel semantics or making chat-private context canonical truth.
3. **Add broader neutrality evidence** after the founding path is stable: a materially non-GitHub/Cloudflare execution/storage case, then multi-project workspace isolation after Agnir's fixture is ready.
4. Freeze exact Agnir compatibility/version expression only after Agnir Core `0.1` release criteria are concrete.
5. Keep live Cloudflare delivery disabled unless explicitly authorized. If authorized later, preserve exact verified-subject delivery and require independent observation before success claims.
6. Keep incidental branch cleanup deferred until the new Svif version is substantially complete; preserve `legacy/zerolocal-v0.1` unchanged.

## Repository-retirement note

`iorLab/svif-cloudflare-reference` is no longer an active Svif project or dependency. Its useful product behavior is now owned inside `iorLab/svif`; historical evidence is preserved in `history/CLOUDFLARE_REFERENCE.md`. The GitHub repository may be physically deleted after retirement/tombstone handling; no future Svif work should target it.

## Completed in the current implementation sequence

- Svif product identity corrected and Product Architecture `0.2` frozen around Orchestrator + Continuity Provider + Execution Surface + Capability Provider.
- Minimal executable Orchestrator implemented and CI-proven.
- Concrete Agnir repository/filesystem Continuity Provider implemented.
- ChatGPT structured Execution Surface bridge implemented with `begin()` / `complete()` handoff.
- Cloudflare provider ownership consolidated into `src/svif/capabilities/cloudflare.py` and `integrations/cloudflare/`; the separate Cloudflare reference project is retired from the active architecture.
- Validation Project #2 retains proven credential-free static verification; protected delivery remains unproven and disabled.
