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
