# Svif Decisions

## 2026-08-27 — New main-line architecture

- `main` implements Svif directly. ZeroLocal v0.1 remains predecessor evidence on `legacy/zerolocal-v0.1`; its active Skill/spec/conformance layout is not retained on the Svif main line.
- Svif Core version is the `0.2` development line and depends on the Agnir Core `0.1` protocol line.
- Svif's own durable continuity is discovered through `AGNIR.yaml`.
- PLAN semantics are mandatory, but a trivial operation may coalesce PLAN in its execution trace when no separately inspectable plan artifact/evidence is material. Planning preconditions still apply before CHANGE.
- Capability Adapter operation names are extensible; every operation declares one Core semantic effect. This keeps third-party/provider APIs out of Core while preserving portable orchestration semantics.
- The Core semantic effects are `resolve`, `inspect`, `mutate`, `identify`, `verify`, `actuate`, `observe`, `authorize`, `recover`, and `checkpoint`.
- Stable candidate provenance is represented through standard evidence records rather than requiring Git SHA. Git full SHA remains the recommended strong Software Delivery + SCM realization.
- The standard evidence record carries Project/operation identity, record kind, stable subject identity, optional derivation chain, optional target identity, result status, producer/adapter reference, authority reference, evidence locator, and timestamp.
- Delivery gated by verification must actuate the verified candidate or a replacement that has independent verification evidence.
- OBSERVE is mandatory when external effect is claimed; actuation success alone is not sufficient.
- CHECKPOINT remains a Svif lifecycle state but delegates persistence/resumability to Agnir.
- Secret values remain in authorized protected channels/stores; adapter descriptors and evidence may carry references/scopes but not require plaintext secret transport.

## 2026-08-27 — Repository identity transition

- Canonical repositories are `iorLab/agnir` and `iorLab/svif`.
- Legacy branch names are intentionally not renamed: `legacy/zerolocal-v0.1` and `legacy/ppmp-v2.0.0` preserve predecessor identity and history.
- Repository redirects are compatibility behavior rather than canonical project identity.
- Repository naming remains packaging/discovery metadata, not a Svif semantic dependency.

## 2026-08-28 — Execution-surface-neutral canonical Project structure

- Execution-surface bootstrap configuration belongs to the execution surface, not canonical Project truth.
- The former `.chatgpt/project-memory.yaml` compatibility shim is removed from active `main`.
- For this repository's Agnir repository/filesystem profile, cold start begins directly at top-level `AGNIR.yaml`.
- Removing ChatGPT-specific canonical state does **not** mean Svif should omit a ChatGPT product integration layer; execution-surface neutrality and product integrations are separate concerns.

## 2026-08-28 — Cloudflare implementation role

- The Cloudflare repository is canonical at `iorLab/svif-cloudflare-reference`.
- Its role is a controlled executable integration reference/testbed for Svif Software Delivery + Cloudflare capability behavior.
- It is not a user starter/template and does not define provider-neutral Svif semantics.
- It must preserve exact verified-candidate delivery, protected production authority, serialized state-sensitive delivery, target discovery, and independent post-delivery observation.
- As the Svif product matures, reusable Cloudflare capability implementation should be owned/packaged by Svif and the reference repository should increasingly consume/test that implementation rather than permanently owning product logic.

## 2026-08-28 — Svif product identity correction

- Svif is a **Project orchestration product**, not a pure Project-operation protocol.
- Agnir remains the independent continuity/memory protocol. Dependency direction remains `Svif -> Agnir`.
- The product's stable three-sided environment is:
  - **Continuity Provider** — current implementation: Agnir;
  - **Execution Surface / Executor Host** — current founding integration: ChatGPT;
  - **Capability / Effect Provider** — current founding provider: Cloudflare.
- Svif is the orchestration layer between these sides. It loads continuity, constructs execution context, coordinates work/capabilities, enforces authority and provenance, observes/reconciles effects, and checkpoints durable truth.
- Existing lifecycle, Evidence, Capability Adapter, authority, and Software Delivery material is retained as portable **internal product contracts** and design foundations. It must not be used to redefine the whole Svif product as a standards/protocol repository.
- Project canonical truth must remain execution-surface-neutral, while Svif itself may and should ship integrations for concrete execution surfaces such as ChatGPT.
- Svif's intended mature distribution remains an installable Plugin/product surface. Specification/contracts are a subset of the product, not the product identity.
- The active repository has drifted too far toward `spec/` + `schemas/` + `conformance/` and lacks the actual Svif orchestration/runtime layer; this is now an explicit architecture correction item.
- Before adding more neutrality/conformance breadth, freeze a Product Architecture around four first-class components:
  1. Orchestrator;
  2. Continuity Provider interface (first: Agnir);
  3. Execution Surface interface (first: ChatGPT);
  4. Capability Provider interface (first provider family: Cloudflare).
- `SVIF.yaml` must be re-evaluated. A likely product-facing direction is a Project binding/configuration manifest that declares continuity, execution-surface, capability/provider, authority, and applicable profile bindings; exact semantics are not yet frozen.
- Specification-repository integrity checks must be distinguished from portable Svif product/contract conformance. `conformance/check_svif_0_2.py` currently mixes these concerns.
- The previously first-priority materially non-GitHub/Cloudflare conformance case is paused until the Product Architecture correction is resolved.
