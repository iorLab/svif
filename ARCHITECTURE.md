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

The Principal supplies intent, policy, approval, authority, and risk acceptance where required. Distribution forms such as Skill, Plugin, CLI, SDK, or IDE integration package these components but do not become canonical Project truth.

```text
                         Principal
                            |
                            v
                    +----------------+
                    |      Svif      |
                    |  Orchestrator  |
                    +----------------+
                      /      |      \
                     /       |       \
                    v        v        v
          Continuity     Execution   Capability
           Provider       Surface     Provider
              |               |          |
            Agnir          ChatGPT    Cloudflare
          (current)       (current)    (current)
```

Agnir, ChatGPT, and Cloudflare are the founding/current bindings. None is the permanent definition of Svif.

## 2. Orchestrator

The Orchestrator is the Svif product kernel. For a material operation it is responsible for the cross-boundary coherence that no provider or surface can guarantee alone.

It MUST be able to:

- resolve the Project identity and applicable Svif bindings;
- load durable continuity from the configured Continuity Provider;
- materialize the minimum execution context needed by the active Execution Surface;
- establish operation scope, required verification, authority boundaries, and effect/observation requirements before material mutation;
- select and invoke Project/capability operations through declared adapters or equivalent bindings;
- preserve stable subject identity and provenance across change, verification, actuation, observation, and checkpoint;
- prevent verification authority from silently becoming protected actuation authority;
- require independent observation before claiming an external effect succeeded;
- reconcile observed/resulting state with intended state;
- checkpoint resulting durable truth through the configured Continuity Provider.

The existing lifecycle is the default internal orchestration contract:

`DISCOVER -> PLAN -> CHANGE -> VERIFY -> DELIVER -> OBSERVE -> CHECKPOINT`

`REPAIR` returns to the earliest violated invariant.

## 3. Continuity Provider interface

A Continuity Provider supplies durable Project truth and resumability. The Svif kernel depends on this **interface**, not permanently on Agnir.

A compatible provider MUST make it possible for Svif to:

- discover or resolve the continuity source from an authorized Project entry point or binding;
- load current durable state, decisions, next actions, and evidence references needed for the operation;
- associate continuity with the correct Project identity;
- checkpoint/reconcile resulting Project truth durably;
- distinguish unavailable/unauthorized/broken continuity from an empty or new Project state.

The active `0.2` repository binding uses **Agnir Core 0.1** as the first Continuity Provider. Agnir remains an independent protocol/project. Agnir-specific filesystem layout, Git, GitHub, or ChatGPT assumptions MUST NOT leak into the Svif kernel.

## 4. Execution Surface interface

An Execution Surface hosts or exposes the Executor that interprets intent and performs work. It is replaceable and MUST NOT become authoritative merely because execution occurred there.

A compatible surface MUST allow the Svif integration to:

- receive Project/operation-scoped context materialized by the Orchestrator;
- preserve Project and operation identity while work is in progress;
- surface Principal intent, approval, or authority transitions when required;
- invoke or route Svif capabilities available to that surface;
- return outputs/evidence references needed for reconciliation and checkpoint;
- avoid treating surface-private conversation/context as the sole durable Project truth.

**ChatGPT** is the founding Execution Surface integration. A future CLI, IDE, CI runner, local agent, or other host may implement the same product boundary.

Canonical Project state remains execution-surface-neutral even when a concrete Svif distribution integrates deeply with ChatGPT.

## 5. Capability Provider interface

A Capability Provider exposes inspectable or effectful operations used by Svif. Providers may cover workspace, SCM, verification, delivery, external APIs, observation, authority, or other Project capabilities.

Provider operations SHOULD be described through the existing Capability Adapter contract and MUST preserve, where applicable:

- a portable semantic effect (`resolve`, `inspect`, `mutate`, `identify`, `verify`, `actuate`, `observe`, `authorize`, `recover`, `checkpoint`);
- authority class;
- retry/idempotency behavior;
- portable failure classification;
- evidence inputs/outputs and stable subject/target identity;
- protected credential references without plaintext secret transport.

**Cloudflare** is the founding external effect/delivery provider family. It is not the definition of delivery or of Capability Providers generally.

## 6. Project Binding Manifest

Svif needs a Project-facing binding/configuration contract that identifies which providers/surfaces apply to a Project.

`project-binding/0.2` is the active development contract. The repository/filesystem serialization used by current Svif Projects is `SVIF.yaml`; the filename itself is not a universal product requirement when another execution environment supplies an equivalent binding object.

A binding identifies at minimum:

- Svif product/manifest version;
- Project identity;
- Continuity Provider binding;
- zero or more Execution Surface bindings;
- zero or more Capability Provider bindings;
- applicable profiles;
- optional product/repository metadata.

Bindings MAY carry provider identifiers, locators, adapter references, authority classes, and non-secret configuration. They MUST NOT require plaintext protected secrets.

The normative contract is `spec/PROJECT_BINDING.md`; the reference machine-readable schema is `schemas/project-binding.schema.json`.

## 7. Internal portable contracts

The following are product-internal portable contracts, not the complete product identity:

- `spec/CORE.md` — orchestration lifecycle/invariants;
- `spec/EVIDENCE.md` — provenance/evidence envelope;
- `spec/CAPABILITY_ADAPTER.md` — capability-provider adapter semantics;
- `profiles/SOFTWARE_DELIVERY.md` — software-delivery specialization;
- `schemas/` — reference serializations.

They exist so different integrations/providers can interoperate with the Orchestrator without promoting founding implementation details into the product kernel.

## 8. Distribution and integrations

The intended mature distribution remains an installable **Plugin**. Skill packaging may remain an earlier/contained distribution step where useful.

Distribution dependency direction is:

`distribution -> Execution Surface integration -> Orchestrator -> Continuity + Capability Providers`

A distribution MAY bundle provider adapters and surface-specific onboarding, but it MUST NOT move canonical Project truth into distribution-private state.

## 9. Cloudflare reference role

`iorLab/svif-cloudflare-reference` remains a separate controlled executable testbed.

During early development it may contain reference behavior that has not yet been packaged by Svif. As the product implementation matures, reusable Cloudflare capability behavior should be owned by Svif and consumed by the reference repository, so the reference becomes primarily an E2E integration/pressure test rather than a second source of product logic.

## 10. Conformance and repository integrity

Two different checks are required:

- **Repository integrity** verifies that `iorLab/svif` itself contains a coherent product architecture, contracts, continuity state, and active-line structure.
- **Portable contract conformance** validates evidence/provenance and adapter semantics that can apply outside this repository.

Repository integrity is not evidence that an arbitrary Project is Svif-conformant.

## 11. Near-term implementation target

With this architecture frozen, the next implementation milestone is a minimal executable Svif kernel/integration path that demonstrates:

`load continuity -> materialize execution context -> execute/verify -> invoke optional capability -> observe/reconcile -> checkpoint`

using the founding bindings Agnir + ChatGPT + Cloudflare without making any of them permanent kernel dependencies.
