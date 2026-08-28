# Svif Product Architecture 0.2

**Status:** Frozen product-architecture baseline for the active `0.2` development line.

Svif is a **Project orchestration product**. It coordinates durable Project continuity, the execution surface in which work is interpreted/performed, and capability providers that inspect or change Project/external state.

Svif is not itself a durable-memory protocol and is not defined by any one execution surface or provider.

> The Project persists; Executors and execution environments may change.

## 1. Product boundary

A Svif-managed operation has four first-class product components:

1. **Orchestrator**
2. **Continuity Provider**
3. **Execution Surface**
4. **Capability Provider**

The Principal supplies intent, policy, approval, authority, and risk acceptance where required. Distribution forms such as Skill, Plugin, ChatGPT App, CLI, SDK, or IDE integration package these components but do not become canonical Project truth.

Agnir, ChatGPT, and Cloudflare are the founding/current bindings. None is the permanent definition of Svif.

## 2. Orchestrator

The Orchestrator is the Svif product kernel. It owns cross-boundary coherence that no Continuity Provider, Execution Surface, or Capability Provider can guarantee alone.

It MUST be able to resolve Project/bindings, load continuity, materialize execution context, establish verification/authority/effect requirements, preserve provenance, invoke applicable capabilities, require independent observation for external success, reconcile resulting state, and checkpoint durable truth.

The default internal lifecycle remains:

`DISCOVER -> PLAN -> CHANGE -> VERIFY -> DELIVER -> OBSERVE -> CHECKPOINT`

`REPAIR` returns to the earliest violated invariant.

### Execution handoff modes

Execution Surfaces may use different directions of control.

- **Synchronous surface:** Svif can call a surface `execute()` implementation and use `Orchestrator.run()`.
- **Externally driven surface:** the host calls into Svif. Svif uses `Orchestrator.begin()` to load continuity/create an `OperationSession`, the surface integration materializes that session, and a later trusted integration call returns a structured `WorkResult` to `Orchestrator.complete()`.

ChatGPT's current Apps SDK/MCP model is externally driven, so the founding ChatGPT integration uses the second form. This prevents the product architecture from pretending ChatGPT is a synchronous function invoked by the kernel.

Trusted integration authority may be added at completion time (for example after a platform-mediated write confirmation). Untrusted model/result payloads MUST NOT self-grant protected authority.

## 3. Continuity Provider interface

A Continuity Provider supplies durable Project truth and resumability. The Svif kernel depends on this **interface**, not permanently on Agnir.

A compatible provider must allow Svif to resolve/load current state, next actions, decisions/evidence as required, preserve Project identity, checkpoint resulting truth, and distinguish unavailable/unauthorized/broken continuity from an empty/new state.

The active founding provider is Agnir Core `0.1`. `src/svif/continuity/agnir.py` implements the current `repository-filesystem/0.1` profile without promoting filesystem/Git/repository assumptions into the kernel.

## 4. Execution Surface interface

An Execution Surface hosts or exposes the Executor that interprets intent and performs work. It is replaceable and MUST NOT become authoritative merely because execution occurred there.

A compatible integration must preserve Project/operation identity, receive only the Project-scoped context needed for work, surface Principal authority transitions through trusted channels, return inspectable results/evidence/continuity updates, and avoid treating surface-private conversation as sole durable Project truth.

**ChatGPT** is the founding Execution Surface. `src/svif/execution/chatgpt.py` is the first structured bridge; `integrations/chatgpt/` tracks concrete app/MCP packaging. Future CLI, IDE, CI, local-agent, or other surfaces may implement the same boundary.

## 5. Capability Provider interface

A Capability Provider exposes inspectable or effectful operations used by Svif. Providers may cover workspace, SCM, verification, delivery, external APIs, observation, authority, or other Project capabilities.

Provider operations SHOULD use the Capability Adapter contract and preserve portable semantic effect, authority class, retry/idempotency behavior, portable failure mapping, Evidence inputs/outputs, stable subject/target identity, and protected credential references without plaintext secret transport.

**Cloudflare** is the founding external effect/delivery provider family. It is not the definition of delivery or Capability Providers generally.

## 6. Project Binding Manifest

`project-binding/0.2` binds a Project to one Continuity Provider, zero or more Execution Surfaces, zero or more Capability Providers, applicable profiles, and optional product/repository metadata.

Current repository/filesystem integrations serialize this as `SVIF.yaml`; the filename is not a universal kernel requirement when another installation/execution environment supplies an equivalent binding object.

Bindings MAY carry provider identifiers, locators, adapter references, authority classes, and non-secret configuration. They MUST NOT require plaintext protected secrets.

Normative contract: `spec/PROJECT_BINDING.md`. Reference schema: `schemas/project-binding.schema.json`.

## 7. Internal portable contracts

The following are product-internal portable contracts, not the complete product identity:

- `spec/CORE.md` — orchestration lifecycle/invariants;
- `spec/EVIDENCE.md` — provenance/evidence envelope;
- `spec/CAPABILITY_ADAPTER.md` — capability-provider adapter semantics;
- `profiles/SOFTWARE_DELIVERY.md` — software-delivery specialization;
- `schemas/` — reference serializations.

## 8. Distribution and integrations

The intended mature distribution remains an installable **Plugin**. Current ChatGPT packaging should follow the current Apps SDK/MCP app model rather than revive deprecated assumptions about historical plugin mechanics.

Distribution dependency direction is:

`distribution -> Execution Surface integration -> Orchestrator -> Continuity + Capability Providers`

A distribution MAY bundle provider adapters and surface-specific onboarding, but it MUST NOT move canonical Project truth into distribution-private state.

## 9. Cloudflare reference role

`iorLab/svif-cloudflare-reference` remains a separate controlled executable testbed. As product implementation matures, reusable Cloudflare capability behavior should be owned by Svif and consumed/tested by the reference repository, making the reference primarily an E2E integration/pressure test rather than a second source of product logic.

## 10. Checks

Repository integrity, portable contract conformance, and runtime/integration behavior are distinct verification layers. Repository integrity is not evidence that an arbitrary Project is Svif-conformant.

## 11. Near-term target

The generic Orchestrator, Agnir Continuity Provider, and ChatGPT structured Execution Surface bridge now exist. The next major implementation is a Svif-owned Cloudflare Capability Provider followed by a founding end-to-end path across Agnir + ChatGPT + Cloudflare. Remote ChatGPT Apps SDK/MCP packaging can then wrap the same bridge without duplicating kernel semantics.
