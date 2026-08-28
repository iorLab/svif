# Svif Decisions

## 2026-08-27 — New main-line architecture

- `main` implements Svif directly; ZeroLocal v0.1 remains predecessor evidence on `legacy/zerolocal-v0.1`.
- Svif product line is `0.2` development.
- Delivery gated by verification must actuate the verified subject or an independently verified replacement.
- OBSERVE is mandatory when external effect is claimed; actuation success alone is insufficient.
- Secret values remain in authorized protected channels/stores; Svif carries references/scopes, not plaintext values.

## 2026-08-28 — Product Architecture 0.2

- Svif is a **Project orchestration product**, not a pure protocol.
- Four first-class components are **Orchestrator**, **Continuity Provider**, **Execution Surface**, and **Capability Provider**.
- Agnir is the founding Continuity Provider but remains an independent protocol/project.
- ChatGPT is the founding Execution Surface; canonical Project truth remains execution-surface-neutral.
- Cloudflare is the founding external-effect Capability Provider family, not a kernel dependency.
- `SVIF.yaml` is the repository/filesystem serialization of `project-binding/0.2`.
- Portable Core/Evidence/Capability Adapter/Software Delivery material is internal product contract, not the complete product identity.

## 2026-08-28 — Executable product foundation

- `src/svif/runtime.py` is the executable Orchestrator kernel.
- `src/svif/continuity/agnir.py` implements the current Agnir repository/filesystem profile.
- `src/svif/execution/chatgpt.py` implements the structured ChatGPT execution bridge.
- Externally driven surfaces use `Orchestrator.begin()` / `Orchestrator.complete()`; untrusted result payloads cannot self-grant protected authority.

## 2026-08-28 — Single-repository Svif product topology

- Active canonical repositories are only `iorLab/svif` and `iorLab/agnir`.
- Provider-specific Svif implementations, fixtures, integration notes, and E2E pressure tests belong in `iorLab/svif` unless they are independently useful protocols/products in their own right.
- `iorLab/svif-cloudflare-reference` is retired from the active architecture and must not remain a runtime, conformance, release, Project-state, or next-action dependency.
- Historical evidence from the retired repository is preserved in `history/CLOUDFLARE_REFERENCE.md`; this is evidence only, not a dependency.
- Svif owns the Cloudflare Workers Capability Provider at `src/svif/capabilities/cloudflare.py` and its descriptor/integration boundary under `integrations/cloudflare/`.
- Cloudflare transport is injected so provider I/O/credentials can vary without making GitHub Actions, Wrangler, or a standalone repository part of the product architecture.
- The old repository may be physically deleted after tombstoning; no active Svif behavior is allowed to depend on it.

## 2026-08-28 — README architecture diagrams and localization

- `README.md` is the English project entry point and `README.zh-CN.md` is the Simplified Chinese entry point.
- Both language versions MUST show the current **Architecture Diagram** and **Runtime / Operation Flow** using Mermaid so the repository explains both static component topology and dynamic operation semantics without requiring a reader to reconstruct them from specifications.
- Architecture, component ownership, dependency direction, authority/provenance boundaries, or runtime-flow changes MUST update the affected diagrams in both README language versions in the same change set.
- Localized READMEs describe the same canonical architecture. Translation may adapt explanatory prose, but it must not introduce a separate product model.
- Localized diagrams are comprehension-first, not literal translations. In the Simplified Chinese README, important nodes must communicate both role and responsibility so the diagram remains understandable without prior knowledge of the English term; English terminology may remain as a secondary label.
- Repository checks enforce diagram/locale structure rather than exact prose wording.

## 2026-08-28 — Founding credential-free E2E baseline

- `tests/test_founding_e2e.py` is the founding in-repository executable product scenario across Agnir + ChatGPT + Cloudflare through the real Svif Orchestrator boundary.
- The scenario MUST use injected non-secret/fake provider transport by default so the product loop is continuously testable without protected credentials.
- Trusted authority is supplied to `Orchestrator.complete()` by the integration context; model/result payloads do not carry or self-grant `protected-delivery` authority.
- A successful founding E2E proves the orchestration loop, boundary contracts, exact-subject verification, independent observation, and Agnir checkpoint/resume behavior.
- Credential-free founding E2E success does **not** constitute evidence of live Cloudflare production actuation. Live provider delivery remains separately authorized and separately evidenced.
- Product-check run `33143308949` succeeded with repository-integrity, runtime-kernel, and portable-contracts jobs; durable evidence is `.agnir/evidence/2026-08-28-founding-e2e.md`.

## 2026-08-28 — Mature distribution target preserved

- The mature Svif product/distribution target remains an **installable Plugin**, preserving the predecessor roadmap's long-term product form.
- ChatGPT app/MCP packaging is the founding/current ChatGPT Execution Surface integration and MUST NOT be treated as a replacement for the mature Plugin target.
- Distribution may package integrations/providers/onboarding, but it MUST NOT duplicate Orchestrator semantics or move canonical Project truth out of the configured Continuity Provider.
- Dependency direction is `Plugin / distribution -> Execution Surface integration -> Orchestrator -> Continuity + Capability Providers`.
- This durable target was explicitly restored after predecessor-migration review found that the current Agnir state/decisions had accidentally stopped stating it even though it remained part of the accepted product direction.

## 2026-08-28 — README repository structure tree

- The README repository explanation uses a **plain-text tree**, not a third Mermaid architecture diagram and not a separate abstract repository map.
- The tree MUST follow the actual repository structure closely enough to show where major product responsibilities live, while remaining selective rather than exhaustively listing every fixture/evidence file.
- Each documented directory or key file SHOULD include a short responsibility explanation directly in the tree.
- If a documented directory is added, removed, moved, or materially changes responsibility, `README.md` and `README.zh-CN.md` MUST update the affected tree in the same change set.
- Repository integrity checks enforce the presence of the explanatory tree and key module anchors without byte-for-byte locking the whole tree.

## 2026-08-28 — Exhaustive repository tree companion

- README repository trees remain compact navigation views.
- `REPOSITORY_TREE.md` is the exhaustive tracked-file repository map for documentation purposes.
- Tracked file additions, removals, moves, or material responsibility changes MUST update `REPOSITORY_TREE.md` in the same change set.
- If a change affects the compact repository map, both `README.md` and `README.zh-CN.md` MUST update together.
- `REPOSITORY_TREE.md` explains file ownership/responsibility; it is not a second product architecture or contract source.

## 2026-08-28 — Real ZeroLocal predecessor migration accepted

- `iorLab/svif@legacy/zerolocal-v0.1` at commit `8ccbb1d30520ca3d0b8b9f2cfe2963d35a853cf6` is accepted as genuine real predecessor migration evidence.
- Its `.chatgpt/project-memory.yaml` declares predecessor `version: 1`, so it is explicitly classified as **v1/RPM-era**, not PPMP v2. It MUST NOT be relabeled as exact PPMP v2 evidence.
- Migration validation compares material durable Project knowledge, not merely file or locator presence.
- The audit classifies predecessor knowledge as preserved, generalized, intentionally retired, repaired after regression, or explicitly not inherited.
- The mature `installable-plugin` target was one material durable fact that had been lost during the rewrite; the audit detected this regression and the target is now restored across architecture, canonical state/decisions, and both README languages.
- Provider neutrality, protected secret/authority boundaries, exact verified-subject provenance, independent observation, and fresh-context resumability remain preserved/generalized in the current architecture.
- `.chatgpt/` RPM state, ChatGPT-specific bootstrap, ZeroLocal Skills, predecessor `SPECIFICATION.md`/ZL conformance, and the standalone Cloudflare reference project are intentionally not active Svif 0.2 structures.
- Historical ZeroLocal Validation #1 remains predecessor evidence and is not relabeled as Svif conformance or current live Cloudflare evidence. Validation #2 requires redefinition against current Svif/Agnir contracts before reuse.
- Durable migration evidence is `.agnir/evidence/2026-08-28-zerolocal-predecessor-migration.md`.

## 2026-08-28 — Agnir compatibility binding is the Core line

- Svif's durable continuity compatibility boundary is **Agnir Core `"0.1"`**, already serialized as `bindings.continuity.compatibility: "0.1"` in `SVIF.yaml`.
- Svif MUST NOT bind product compatibility to Agnir repository release `0.1.0-rc.1`, any particular `0.1.x` patch, Agnir repository layout, backend, or adapter implementation.
- Agnir's repository SemVer and Svif's Continuity Provider compatibility are different version layers.
- A compatible alternate Agnir implementation/backend may satisfy Svif when it honors the same Core `"0.1"` semantics and the configured Project binding.
- Agnir has completed exact PPMP v2 -> Agnir migration conformance separately, so Svif does not carry a remaining requirement to locate a second external historical PPMP v2 Project.
- The next Svif product milestone is concrete ChatGPT Apps SDK / MCP packaging around the existing externally driven bridge, not further expansion of the kernel architecture.
