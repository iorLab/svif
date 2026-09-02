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

- `iorLab/svif` owns the entire Svif product, including provider implementations, execution-surface integrations, E2E fixtures, portable contracts, Plugin packaging, and tests;
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

`src/svif/continuity/agnir.py` is the founding adapter for Agnir repository/filesystem discovery and checkpoint semantics.

A Continuity Provider may expose more than one provider-local continuity context for the same stable Svif Project identity when its own contract supports that behavior. The **selected** continuity context comes from the Project Binding or another trusted adapter context; the generic Orchestrator consumes the selected `ContinuitySnapshot` and MUST NOT enumerate sibling provider contexts, infer one from a backend branch/ref/revision, or silently switch contexts when selection is missing or inconsistent.

Provider-local lineage, namespace, selector, revision, and reconciliation semantics therefore remain at the Continuity Provider / Project Binding boundary. They do not become generic Svif Project identity or Orchestrator lifecycle semantics.

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

Svif now ships an **installable Plugin MVP** under `plugin/` using the portable **Agent Plugins 1.0.0** package format.

The current package is intentionally Skill-first:

```text
plugin/
├── plugin.json
├── README.md
└── skills/
    └── svif/
        └── SKILL.md
```

- `plugin/plugin.json` is the portable Plugin manifest.
- `plugin/skills/svif/SKILL.md` is the first installable workflow component.
- The Plugin guides compatible execution surfaces through Agnir discovery, Svif lifecycle execution, provenance/authority guards, independent observation, and durable checkpointing.
- The Plugin is a distribution layer and does not reimplement `src/svif/runtime.py`.

A Skill-only Plugin is a valid and useful first product increment. An optional `mcp.json` will be added when the concrete remote Svif MCP/App surface is ready; MCP completion is not a prerequisite for testing and iterating the Plugin workflow itself.

Current ChatGPT app/MCP work remains the founding ChatGPT **Execution Surface integration**. It can be packaged into the Plugin later without redefining Svif as ChatGPT-only and without moving canonical Project truth out of the configured Continuity Provider.

Distribution dependency direction remains:

`Plugin / distribution -> Execution Surface integration -> Orchestrator -> Continuity + Capability Providers`

For the current Skill-first MVP, the Plugin can also guide an execution surface directly through the portable Project workflow while the remote MCP wrapper is still being hardened.

## 10. Verification layers

- repository integrity verifies the Svif repository itself and registers Plugin package artifacts;
- `tests/test_plugin_package.py` validates the Plugin manifest, Skill content guards, and the rule that Plugin packaging must not shadow the runtime;
- portable conformance validates reusable contracts;
- runtime tests validate Orchestrator/provider/surface behavior;
- E2E fixtures validate concrete founding compositions.

A provider fixture does not justify a separate canonical repository.

## 11. Near-term target

The generic Orchestrator, Agnir Continuity Provider, ChatGPT bridge, Svif-owned Cloudflare Capability Provider, credential-free founding E2E, and installable Skill-first Plugin MVP now belong to one product tree.

The next target is **test-driven Plugin iteration**: install/use the Skill-first package on real Project work, harden its workflow guidance from failures, and add the remote ChatGPT MCP/App component when it can reuse the existing `Orchestrator.begin()` / `Orchestrator.complete()` boundary without duplicating kernel semantics or weakening authority separation.
