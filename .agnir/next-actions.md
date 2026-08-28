# Svif Next Actions

1. **Complete the real ZeroLocal predecessor -> current Svif/Agnir migration evidence envelope.** Use `iorLab/svif@legacy/zerolocal-v0.1` as genuine predecessor-memory evidence, explicitly classify its `.chatgpt/project-memory.yaml` as earlier v1/RPM-era serialization rather than PPMP v2, and record which material durable knowledge was preserved, retired, lost, and repaired.
2. **Harden the concrete ChatGPT app/MCP packaging** around `integrations/chatgpt/` and the existing `ChatGPTExecutionSurface` bridge. Preserve the externally driven `Orchestrator.begin()` / `Orchestrator.complete()` control direction, keep protected authority outside untrusted model/result payloads, and do not duplicate kernel semantics in the packaging layer.
3. **Add broader neutrality evidence** using Agnir's proven non-repository SQLite continuity and multi-project workspace isolation cases as pressure inputs. Do not make GitHub, Cloudflare, or ChatGPT universal Svif dependencies.
4. Freeze exact Agnir compatibility/version expression only after Agnir Core `0.1` migration/release criteria are reconciled.
5. Keep live Cloudflare delivery disabled unless explicitly authorized. If authorized later, preserve exact verified-subject delivery and require independent observation before success claims.
6. Keep incidental branch cleanup deferred until the new Svif version is substantially complete; preserve `legacy/zerolocal-v0.1` unchanged.

## Documentation maintenance rule

- Architecture/runtime changes are incomplete until the corresponding diagrams and affected explanatory sections in both `README.md` and `README.zh-CN.md` are updated in the same change set.
- Localized diagrams are comprehension-first rather than literal translations; important Simplified Chinese nodes explain both role and responsibility.
- README repository trees remain compact navigation views.
- `REPOSITORY_TREE.md` is the exhaustive file-level map. Tracked file additions/removals/moves or material responsibility changes must update it in the same change set; if the compact tree is also affected, both README language versions must update as well.

## Completed in the current implementation sequence

- Product Architecture `0.2` frozen around Orchestrator + Continuity Provider + Execution Surface + Capability Provider.
- Minimal executable Orchestrator implemented and CI-proven.
- Concrete Agnir repository/filesystem Continuity Provider implemented.
- ChatGPT structured Execution Surface bridge implemented with `begin()` / `complete()` handoff.
- Cloudflare provider ownership consolidated into `src/svif/capabilities/cloudflare.py` and `integrations/cloudflare/`; the separate Cloudflare reference project is retired from the active architecture.
- English and Simplified Chinese README entry points include synchronized Architecture and Runtime / Operation Flow diagrams with comprehension-first Chinese nodes.
- Founding credential-free E2E implemented at `tests/test_founding_e2e.py`, composing Agnir + ChatGPT + Cloudflare through the real Orchestrator boundary with trusted completion-time authority, independent observation, and Agnir checkpoint/resume.
- The mature **installable Plugin** distribution target was restored after predecessor migration audit and is now synchronized into architecture, canonical state/decisions, and both READMEs.
- README compact repository trees now explain major module responsibilities; `REPOSITORY_TREE.md` provides the full tracked file-level map with per-file responsibility annotations.
- Svif repository checks enforce the documentation baseline without byte-for-byte prose locking.
- Pre-checkpoint repository-documentation head `97e70f9980de36aa7e3095cf8284f40c6fbf285e` passed product-check run `33146795882`.

## Repository-retirement note

`iorLab/svif-cloudflare-reference` is no longer an active Svif project or dependency. No future Svif work should target it.
