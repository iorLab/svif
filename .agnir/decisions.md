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
