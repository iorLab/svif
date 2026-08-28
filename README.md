# Svif

Svif is a **Project orchestration product**.

It coordinates durable Project continuity, the execution surface in which work is interpreted/performed, and capability providers that inspect or change Project/external state. Its stable rule is:

> The Project persists; Executors and execution environments may change.

The active founding bindings are:

- Continuity Provider: **Agnir**;
- Execution Surface: **ChatGPT**;
- Capability / Effect Provider: **Cloudflare**.

These are current integrations, not permanent product dependencies.

## Active line

`main` is the Svif `0.2` development line. ZeroLocal v0.1 is preserved as predecessor history on `legacy/zerolocal-v0.1`.

The canonical repository is `iorLab/svif`.

## Product architecture

The active architecture has four first-class components:

1. **Orchestrator** — cross-boundary Project coordination;
2. **Continuity Provider** — durable Project truth/resumability;
3. **Execution Surface** — where an Executor interprets intent and performs work;
4. **Capability Provider** — workspace/verification/delivery/external-effect capabilities.

See `ARCHITECTURE.md` for the frozen `0.2` product-architecture baseline.

The internal lifecycle remains:

`DISCOVER -> PLAN -> CHANGE -> VERIFY -> DELIVER -> OBSERVE -> CHECKPOINT`

`REPAIR` returns to the earliest violated invariant.

Those lifecycle semantics are an internal portable product contract; they do not make Svif itself a standalone protocol.

## Current structure

```text
ARCHITECTURE.md                     # Svif product architecture
SVIF.yaml                           # Project binding/configuration manifest for this repo
AGNIR.yaml                          # current Continuity Provider discovery anchor
.agnir/                             # authoritative continuity for this repository

spec/CORE.md                        # portable orchestration contract
spec/PROJECT_BINDING.md             # Project binding contract
spec/CAPABILITY_ADAPTER.md          # capability-provider adapter semantics
spec/EVIDENCE.md                    # candidate/evidence envelope
profiles/SOFTWARE_DELIVERY.md       # software-delivery specialization

schemas/                            # reference machine-readable contracts
checks/                             # Svif repository integrity checks
conformance/                        # portable contract conformance/fixtures
history/PREDECESSOR.md              # preserved ZeroLocal lineage locator
```

Product implementation/runtime and concrete integrations will grow around these foundations; the repository is no longer treated as a specification-only end state.

## Project binding

`SVIF.yaml` now implements the repository/filesystem serialization of `project-binding/0.2`.

It binds this Project to a Continuity Provider and may bind Execution Surfaces and Capability Providers. For this repository, continuity is currently Agnir `0.1`; execution and external capabilities are intentionally unbound in the canonical repository manifest.

`SVIF.yaml` is not required as a universal filename when another installation/execution environment supplies an equivalent Project binding.

## Continuity

Svif depends on a Continuity Provider interface, not permanently on one memory protocol.

Agnir is the first/current provider and remains an independent project at `iorLab/agnir`. This repository uses Agnir's repository/filesystem profile via `AGNIR.yaml`, but the Svif kernel must not assume `.agnir/`, Git, GitHub, or a particular storage backend.

## Execution surfaces

Project canonical truth remains execution-surface-neutral.

ChatGPT is the founding Svif Execution Surface integration and remains the primary near-term product/distribution target. Removing ChatGPT-owned canonical state does not remove ChatGPT from the Svif product.

The mature distribution target remains an installable Plugin; Skill packaging may remain an earlier product surface where useful.

## Capability providers

Provider/tool-specific capabilities are isolated behind adapters or equivalent bindings. Each operation maps to a portable semantic effect such as `verify`, `actuate`, or `observe`, with explicit authority, retry, failure, and evidence behavior.

Cloudflare is the founding external effect/delivery provider family. The executable reference/testbed is maintained separately at `iorLab/svif-cloudflare-reference`.

As the product matures, reusable Cloudflare capability implementation should be owned by Svif and consumed/tested by the reference repository.

## Evidence

Svif `evidence-record/0.2` preserves stable subject identity, derivation, target identity, result status, producer, authority reference, and evidence locator across boundaries.

For software delivery, full immutable Git SHA remains a strong SCM realization, but Git is not the product's universal candidate model.

## Checks

Two distinct categories are now explicit:

```bash
python checks/check_repository.py
python conformance/check_contracts.py
```

`checks/check_repository.py` checks **this Svif product repository's integrity**.

`conformance/check_contracts.py` exercises **portable product contracts** such as Capability Adapter and Evidence provenance. Passing repository integrity is not evidence that an arbitrary Project is Svif-conformant.

## Near-term implementation direction

The next milestone is a minimal Svif product kernel/integration path that demonstrates:

`load continuity -> materialize execution context -> execute/verify -> optional external capability -> observe/reconcile -> checkpoint`

using Agnir + ChatGPT + Cloudflare as the founding bindings without making them permanent kernel dependencies.
