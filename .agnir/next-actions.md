# Svif Next Actions

1. **Harden the concrete ChatGPT Apps SDK / MCP packaging** around `integrations/chatgpt/` and the existing `ChatGPTExecutionSurface` bridge. Preserve the externally driven `Orchestrator.begin()` / `Orchestrator.complete()` control direction, keep protected authority outside untrusted model/result payloads, and do not duplicate kernel semantics in the packaging layer.
2. **Add broader neutrality evidence** using Agnir's proven non-repository SQLite continuity and multi-project workspace isolation cases as pressure inputs. Demonstrate that GitHub, Cloudflare, and ChatGPT are founding/current bindings rather than universal Svif kernel dependencies.
3. **Keep Svif's Agnir dependency bound to Core compatibility `"0.1"`**, not to Agnir repository `0.1.0-rc.1`, a future `0.1.x` patch, one backend, or one repository layout. `SVIF.yaml` already expresses the correct compatibility line.
4. **Prepare mature installable Plugin packaging only on top of validated kernel/integration behavior.** Distribution may compose integrations/providers/onboarding but must not reimplement Orchestrator semantics or create a second canonical Project truth.
5. Keep live Cloudflare delivery disabled unless explicitly authorized. If authorized later, preserve exact verified-subject delivery and require independent observation before success claims.
6. Keep incidental branch cleanup deferred until the new Svif version is substantially complete; preserve `legacy/zerolocal-v0.1` unchanged.

## Completed in the current implementation sequence

- Product Architecture `0.2` frozen around Orchestrator + Continuity Provider + Execution Surface + Capability Provider.
- Minimal executable Orchestrator implemented and CI-proven.
- Concrete Agnir repository/filesystem Continuity Provider implemented.
- ChatGPT structured Execution Surface bridge implemented with `begin()` / `complete()` handoff.
- Cloudflare provider ownership consolidated into `src/svif/capabilities/cloudflare.py` and `integrations/cloudflare/`; the separate Cloudflare reference project is retired from the active architecture.
- English and Simplified Chinese README entry points include synchronized Architecture and Runtime / Operation Flow diagrams with comprehension-first Chinese nodes.
- Founding credential-free E2E composes Agnir + ChatGPT + Cloudflare through the real Orchestrator boundary with trusted completion-time authority, independent observation, and Agnir checkpoint/resume.
- The mature **installable Plugin** distribution target is restored and synchronized across architecture, canonical state/decisions, and both READMEs.
- README compact repository trees explain major module responsibilities; `REPOSITORY_TREE.md` provides the exhaustive tracked-file map.
- Real ZeroLocal predecessor -> current Svif/Agnir semantic migration audit is complete and recorded in `.agnir/evidence/2026-08-28-zerolocal-predecessor-migration.md`.
- The real predecessor audit is classified as **PASS, v1/RPM-era**, not PPMP v2; it detected and repaired the lost `installable-plugin` durable intent.
- Agnir has separately completed exact PPMP v2 -> Agnir migration conformance and frozen Core compatibility `"0.1"` on repository RC `0.1.0-rc.1`.
- Svif's existing `bindings.continuity.compatibility: "0.1"` is therefore the correct durable compatibility boundary.

## Documentation maintenance rule

- Architecture/runtime changes update affected diagrams and explanations in both `README.md` and `README.zh-CN.md` in the same change set.
- Localized diagrams remain comprehension-first rather than literal translations.
- README repository trees remain compact navigation views.
- `REPOSITORY_TREE.md` is the exhaustive file-level map. Tracked file additions/removals/moves or material responsibility changes must update it in the same change set; if the compact tree is also affected, both README language versions must update as well.

## Repository-retirement note

`iorLab/svif-cloudflare-reference` is no longer an active Svif project or dependency. No future Svif work should target it.
