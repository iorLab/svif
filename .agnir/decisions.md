# Svif Decisions

## 2026-08-27 — New main-line architecture

- `main` implements Svif directly. ZeroLocal v0.1 remains predecessor evidence on `legacy/zerolocal-v0.1`.
- Svif product line is `0.2` development.
- PLAN semantics are mandatory before material mutation; trivial operations may coalesce PLAN in the execution trace when a separate plan artifact is immaterial.
- Stable candidate provenance is represented through standard Evidence records rather than requiring Git SHA. Full immutable Git SHA remains a strong Software Delivery + SCM realization.
- Delivery gated by verification must actuate the verified subject or an independently verified replacement.
- OBSERVE is mandatory when external effect is claimed; actuation success alone is insufficient.
- Secret values remain in authorized protected channels/stores; Svif carries references/scopes, not plaintext values.

## 2026-08-27 — Repository identity transition

- Canonical repositories are `iorLab/agnir` and `iorLab/svif`.
- Legacy branch names intentionally preserve predecessor identity: `legacy/zerolocal-v0.1` and `legacy/ppmp-v2.0.0`.
- Repository naming is packaging/discovery metadata, not a Svif kernel semantic dependency.

## 2026-08-28 — Execution-surface-neutral canonical Project structure

- Execution-surface bootstrap configuration belongs to the execution surface, not canonical Project truth.
- The former `.chatgpt/project-memory.yaml` compatibility shim is removed from active `main`.
- This repository's current Agnir repository/filesystem cold start begins at `AGNIR.yaml`.
- Removing ChatGPT-specific canonical state does **not** remove ChatGPT as a Svif product integration.

## 2026-08-28 — Cloudflare reference role

- `iorLab/svif-cloudflare-reference` is a controlled executable integration reference/E2E testbed, not a user starter/template and not a second Svif specification repository.
- It must preserve exact verified-subject delivery, protected authority, state-sensitive serialization when required, target discovery, and independent post-delivery observation.
- As Svif matures, reusable Cloudflare capability implementation should be owned/packaged by Svif and consumed/tested by the reference repository.

## 2026-08-28 — Svif product identity correction

- Svif is a **Project orchestration product**, not a pure Project-operation protocol.
- The product coordinates Continuity Providers, Execution Surfaces, and Capability Providers through a Svif Orchestrator.
- Existing lifecycle, Evidence, Capability Adapter, authority, and Software Delivery material remains as portable **internal product contracts**.
- Canonical Project truth remains execution-surface-neutral while Svif may ship deep integrations for concrete surfaces such as ChatGPT.
- The intended mature distribution remains an installable Plugin/product surface.

## 2026-08-28 — Product Architecture 0.2 freeze

- Four first-class product components are frozen for the active line: **Orchestrator**, **Continuity Provider**, **Execution Surface**, and **Capability Provider**.
- The stable Svif kernel depends on the **Continuity Provider interface**, not permanently on Agnir. Agnir Core `0.1` is the founding/current continuity binding and remains an independent protocol/project.
- ChatGPT is the founding/current Execution Surface; Cloudflare is the founding external-effect provider family. Neither is a universal kernel dependency.
- `SVIF.yaml` is now the repository/filesystem serialization of `project-binding/0.2`, which binds a Project to continuity, execution-surface, capability-provider, and profile configuration without storing protected secret values.
- Repository-integrity checking is distinct from portable contract conformance. Passing the former is not universal Svif conformance evidence.
- `spec/CORE.md`, Evidence, Capability Adapter, Software Delivery profile, and schemas are product-internal portable contracts rather than Svif's complete product identity.
- Product Architecture freeze landed in commit `bb6f445621b65b7ad9cfa99ac0dea759e4ad40fa`; the semantic checker fix landed in `e201de612dab27bb025f386861ada639a5b0f1e2`; run `33138329497` passed both repository-integrity and portable-contract jobs.

## 2026-08-28 — Minimal executable Orchestrator

- `src/svif/runtime.py` is the first executable Svif product kernel. Python is an implementation/reference vehicle for this stage, not a frozen final Plugin technology choice.
- The kernel coordinates replaceable provider/surface interfaces and deliberately contains no hard-coded Agnir, ChatGPT, or Cloudflare behavior.
- External actuation requires successful verification evidence for the exact subject and any declared authority grant.
- Delivery evidence must match the requested subject/target; observation must independently match the delivered subject/target before checkpoint.
- Failed provenance, missing authority, or observation mismatch prevents checkpoint of false success.
- Non-effectful operations may checkpoint without forcing delivery/observation.
- Implementation commit `c398f17150d5fe868dc60f97dceb58e35025e2e9`; product-check run `33138534555` succeeded across repository integrity, runtime kernel, and portable contracts.
