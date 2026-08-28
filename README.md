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

src/svif/                           # minimal executable Orchestrator kernel
tests/                              # runtime invariant tests

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

The repository now contains both portable product contracts and a minimal executable kernel. Python is the current executable reference vehicle for the kernel; this does not freeze the eventual Plugin implementation technology.

## Executable kernel

`src/svif/runtime.py` implements the first Orchestrator loop across replaceable Continuity Provider, Execution Surface, and Capability Provider interfaces.

The current kernel enforces:

- Project identity consistency when continuity is loaded;
- stable subject identity from execution;
- exact-subject verification before external actuation;
- explicit authority before protected actuation;
- subject/target preservation across delivery;
- independent observation matching the delivered subject/target;
- checkpoint only after all applicable invariants succeed;
- direct checkpoint for non-effectful operations without forcing delivery/observation.

The founding provider names appear only in tests/bindings; the Orchestrator itself does not hard-code Agnir, ChatGPT, or Cloudflare.

## Project binding

`SVIF.yaml` implements the repository/filesystem serialization of `project-binding/0.2`.

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

Three distinct executable checks are active:

```bash
python checks/check_repository.py
python conformance/check_contracts.py
PYTHONPATH=src python -m unittest discover -s tests -v
```

`checks/check_repository.py` checks this Svif product repository's integrity. `conformance/check_contracts.py` exercises portable Project Binding, Capability Adapter, and Evidence contracts. Runtime tests exercise Orchestrator behavior and failure ordering.

Passing repository integrity is not evidence that an arbitrary Project is Svif-conformant.

## Near-term implementation direction

The minimal generic Orchestrator kernel now exists. The next milestone is to replace scripted founding test doubles with concrete product integrations:

1. Agnir Continuity Provider adapter;
2. ChatGPT Execution Surface integration/product surface;
3. reusable Cloudflare Capability Provider implementation;
4. an end-to-end founding scenario wiring all three through the Orchestrator.

Only after that product path is executable should broader non-founding neutrality cases become the main priority.
