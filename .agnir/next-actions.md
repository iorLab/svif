# Svif Next Actions

1. **Finish the Plugin-target migration repair** by synchronizing the restored mature distribution target — **installable Plugin** — into `README.md` and `README.zh-CN.md`, while keeping ChatGPT Apps SDK / MCP framed as current Execution Surface packaging mechanics rather than the product identity. Rerun product checks after the bilingual documentation update.
2. **Complete the real ZeroLocal predecessor -> current Svif/Agnir migration evidence envelope.** Use `iorLab/svif@legacy/zerolocal-v0.1` as genuine predecessor-memory evidence, but explicitly classify its `.chatgpt/project-memory.yaml` as earlier v1/RPM-era serialization rather than PPMP v2. Preserve what material knowledge moved forward, what was intentionally retired, and any migration regressions discovered/repaired.
3. **Harden the concrete ChatGPT app/MCP packaging** around `integrations/chatgpt/` and the existing `ChatGPTExecutionSurface` bridge. Preserve the externally driven `Orchestrator.begin()` / `Orchestrator.complete()` control direction, keep authority outside untrusted model payloads, and avoid duplicating kernel semantics in the packaging layer.
4. **Add broader neutrality evidence** using Agnir's now-proven non-repository SQLite continuity and multi-project workspace isolation cases as pressure inputs. Do not make GitHub, Cloudflare, or ChatGPT universal Svif dependencies.
5. Freeze exact Agnir compatibility/version expression only after Agnir Core `0.1` migration/release criteria are reconciled.
6. Keep live Cloudflare delivery disabled unless explicitly authorized. If authorized later, preserve exact verified-subject delivery and require independent observation before success claims.
7. Keep incidental branch cleanup deferred until the new Svif version is substantially complete; preserve `legacy/zerolocal-v0.1` unchanged.

## Documentation maintenance rule

Architecture/runtime changes are incomplete until the corresponding diagrams and affected explanatory sections in both `README.md` and `README.zh-CN.md` are updated in the same change set. Localized diagrams are comprehension-first rather than literal translations; important Simplified Chinese nodes must explain both role and responsibility.

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
- Migration audit restored **installable Plugin** as the mature product distribution target in `ARCHITECTURE.md`, `.agnir/decisions.md`, and `.agnir/state.md` after predecessor evidence showed the target had been lost during refactoring.
- Pre-checkpoint Plugin-restoration head `98868f5052a6d2e2e4b92a1f3f534dbdae799764` passed product-check run `33144484052`.
- Validation Project #2 retains proven credential-free static verification; protected live delivery remains unproven and disabled.
