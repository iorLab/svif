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

## Product architecture

The active architecture has four first-class components: **Orchestrator**, **Continuity Provider**, **Execution Surface**, and **Capability Provider**. See `ARCHITECTURE.md`.

The internal lifecycle remains:

`DISCOVER -> PLAN -> CHANGE -> VERIFY -> DELIVER -> OBSERVE -> CHECKPOINT`

`REPAIR` returns to the earliest violated invariant. These lifecycle semantics are internal portable product contracts; they do not make Svif itself a standalone protocol.

## Current structure

```text
ARCHITECTURE.md                     # product architecture
SVIF.yaml                           # Project binding for this repository/filesystem integration
AGNIR.yaml                          # current Agnir discovery anchor for this Project
.agnir/                             # this repository's durable continuity

src/svif/runtime.py                 # minimal executable Orchestrator kernel
src/svif/continuity/agnir.py        # Agnir repository/filesystem Continuity Provider
tests/                              # runtime + provider integration tests

spec/                               # portable internal product contracts
profiles/                           # specializations
schemas/                            # reference machine-readable contracts
checks/                             # repository integrity
conformance/                        # portable contract conformance
history/                            # predecessor locator
```

Python is the current executable reference vehicle for the kernel; it does not freeze the eventual Plugin technology stack.

## Executable kernel

`src/svif/runtime.py` implements the first Orchestrator loop across replaceable Continuity Provider, Execution Surface, and Capability Provider interfaces.

It enforces stable subject identity, exact-subject verification before actuation, explicit authority for protected effects, subject/target preservation through delivery, independent observation before external success, and checkpoint only after applicable invariants succeed.

Execution Surfaces now return an explicit provider-neutral `ContinuityUpdate`. The Orchestrator carries this durable-truth update without interpreting provider serialization; the active Continuity Provider validates and persists it.

## Agnir Continuity Provider

`src/svif/continuity/agnir.py` is the first concrete Continuity Provider integration. It implements Agnir `repository-filesystem/0.1` for an authorized Project root while keeping that profile out of the generic Orchestrator.

It:

- resolves `AGNIR.yaml` from the Project Entry Point;
- validates Agnir Core `0.1` and `repository-filesystem/0.1`;
- rejects Project identity mismatch;
- resolves Current State / Next Actions / optional Decisions / Evidence locators relative to the Project root;
- rejects locators that escape the authorized Project root;
- preserves Agnir failure classes for unsupported version, Project mismatch, not-found/unresolvable/inconsistent discovery;
- loads durable continuity into the Execution Context;
- checkpoints explicit Current State / Next Actions / Decisions updates without inventing content;
- writes a deterministic Svif operation-evidence record when an Agnir evidence directory is configured;
- re-runs discovery after checkpoint before resumability is considered established.

This is deliberately an **Agnir profile adapter**, not a hard-coded Orchestrator dependency.

## Project binding

`SVIF.yaml` implements the repository/filesystem serialization of `project-binding/0.2`. It binds this Project to Agnir `0.1`; execution and external capability bindings remain intentionally unbound in this repository's canonical manifest.

`SVIF.yaml` is not a universal filename when another installation/execution environment supplies an equivalent binding object.

## Execution surfaces and distribution

Canonical Project truth remains execution-surface-neutral. ChatGPT is the founding Execution Surface integration and primary near-term distribution target.

The mature distribution target remains an installable Plugin; Skill packaging may be an earlier product surface where useful.

## Capability providers

Cloudflare is the founding external effect/delivery provider family. `iorLab/svif-cloudflare-reference` remains the executable reference/E2E pressure test. Reusable Cloudflare product behavior should increasingly be owned by Svif and consumed/tested by that repository.

## Checks

Run:

```bash
python checks/check_repository.py
python conformance/check_contracts.py
PYTHONPATH=src python -m unittest discover -s tests -v
```

Repository integrity, portable contracts, and executable runtime/provider behavior are distinct checks. Passing repository integrity alone is not universal Svif conformance evidence.

## Near-term implementation direction

The generic Orchestrator and first concrete Continuity Provider now exist. Next:

1. first explicit ChatGPT Execution Surface integration/product surface;
2. reusable Svif-owned Cloudflare Capability Provider implementation;
3. end-to-end founding scenario wiring Agnir + ChatGPT + Cloudflare through the Orchestrator;
4. then broader non-founding neutrality cases.
