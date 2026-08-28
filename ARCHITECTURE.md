# Svif Product Architecture 0.2

**Status:** active architecture baseline for the `0.2` development line.

Svif is a **Project orchestration product**. It is not a collection of separate reference projects.

> The Project persists; Executors and execution environments may change.

## 1. Product boundary

A Svif-managed operation has four first-class components:

1. **Orchestrator**
2. **Continuity Provider**
3. **Execution Surface**
4. **Capability Provider**

Agnir, ChatGPT, and Cloudflare are the founding bindings for those interfaces. None is promoted into the portable kernel contract.

## 2. Repository topology

The active product topology is intentionally two repositories:

- `iorLab/svif` owns the entire Svif product, including provider implementations, execution-surface integrations, E2E fixtures, portable contracts, and packaging work;
- `iorLab/agnir` remains independent because it is a separately useful continuity protocol.

Provider-specific Svif behavior does **not** get its own canonical project merely because it needs executable fixtures. Cloudflare reference behavior therefore lives under `iorLab/svif`.

Historical repositories may remain as migration evidence until physically deleted, but they are not active dependencies, canonical state, or release inputs.

## 3. Orchestrator

The Orchestrator is the Svif product kernel. It resolves Project/bindings, loads continuity, materializes execution context, establishes verification/authority/effect requirements, preserves provenance, invokes capabilities, requires independent observation for external success, reconciles resulting state, and checkpoints durable truth.

The default internal lifecycle remains:

`DISCOVER -> PLAN -> CHANGE -> VERIFY -> DELIVER -> OBSERVE -> CHECKPOINT`

`REPAIR` returns to the earliest violated invariant.

### Execution handoff modes

- **Synchronous surfaces:** `Orchestrator.run()` calls a surface `execute()` implementation.
- **Externally driven surfaces:** `Orchestrator.begin()` creates a bound `OperationSession`; a surface integration materializes it; a trusted integration later returns `WorkResult` to `Orchestrator.complete()`.

ChatGPT uses the externally driven form. Untrusted model/result payloads cannot self-grant protected authority.

## 4. Continuity Provider

A Continuity Provider supplies durable Project truth and resumability. The Svif kernel depends on this interface, not permanently on Agnir.

`src/svif/continuity/agnir.py` is the founding adapter for Agnir Core `0.1` repository/filesystem discovery and checkpoint semantics.

## 5. Execution Surface

An Execution Surface hosts/exposes the Executor. It must preserve Project/operation identity and return inspectable results without turning surface-private context into canonical Project truth.

`src/svif/execution/chatgpt.py` is the founding structured bridge. Concrete ChatGPT packaging remains under `integrations/chatgpt/`.

## 6. Capability Provider

A Capability Provider exposes inspectable or effectful operations. Provider implementations belong to Svif when they implement Svif product behavior.

`src/svif/capabilities/cloudflare.py` is the founding Cloudflare Workers Capability Provider. It owns Svif-facing semantics while delegating provider I/O to an injected transport. This keeps the product testable without credentials and prevents GitHub Actions, Wrangler, or one deployment mechanism from becoming kernel dependencies.

The Cloudflare boundary preserves:

- exact verified subject identity;
- logical target identity;
- protected authority enforced by the Orchestrator/integration boundary;
- portable delivery and observation evidence;
- independent post-actuation observation before external success is checkpointed.

Provider descriptor/integration notes live under `integrations/cloudflare/`.

## 7. Project Binding

`project-binding/0.2` binds a Project to one Continuity Provider, zero or more Execution Surfaces, zero or more Capability Providers, applicable profiles, and optional non-secret integration metadata.

Current repository/filesystem Projects serialize this as `SVIF.yaml`; the filename itself is not a universal kernel requirement.

## 8. Internal portable contracts

- `spec/CORE.md` — orchestration lifecycle/invariants;
- `spec/EVIDENCE.md` — provenance/evidence envelope;
- `spec/CAPABILITY_ADAPTER.md` — capability-provider semantics;
- `profiles/SOFTWARE_DELIVERY.md` — software-delivery specialization;
- `schemas/` — reference serializations.

These are internal product contracts, not separate products.

## 9. Distribution

The mature Svif product/distribution target remains an **installable Plugin**. This is a durable product goal inherited from the predecessor roadmap and is distinct from any one execution-surface packaging mechanism.

Current ChatGPT app/MCP packaging is the founding ChatGPT **Execution Surface integration**. It is one integration path packaged by Svif; it does not redefine Svif itself as a ChatGPT-only product and does not replace the mature Plugin target.

Distribution dependency direction is:

`Plugin / distribution -> Execution Surface integration -> Orchestrator -> Continuity + Capability Providers`

A distribution may bundle provider adapters and onboarding, but canonical Project truth remains with the configured Continuity Provider.

## 10. Verification layers

- repository integrity verifies the Svif repository itself;
- portable conformance validates reusable contracts;
- runtime tests validate Orchestrator/provider/surface behavior;
- E2E fixtures validate concrete founding compositions.

A provider fixture does not justify a separate canonical repository.

## 11. Near-term target

The generic Orchestrator, Agnir Continuity Provider, ChatGPT bridge, Svif-owned Cloudflare Capability Provider, and credential-free founding E2E now belong to one product tree. The next target is hardening the ChatGPT app/MCP packaging around the existing bridge, followed by broader non-founding neutrality evidence and eventual Plugin packaging/graduation without duplicating kernel semantics.
