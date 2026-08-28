# Svif Current State

Svif is the authoritative active **Project orchestration product** on `main`. ZeroLocal v0.1 is predecessor history preserved on `legacy/zerolocal-v0.1`.

## Product identity

Svif coordinates three replaceable sides around a Project:

1. **Continuity Provider** — durable Project truth and resumability. Founding/current provider: **Agnir**.
2. **Execution Surface / Executor Host** — where intent is interpreted and work is performed. Founding/current surface: **ChatGPT**.
3. **Capability / Effect Provider** — where Svif inspects, changes, delivers to, or observes Project/external state. Founding external-effect provider family: **Cloudflare**.

Svif itself is the **Orchestrator** between these sides. It loads continuity, materializes execution context, coordinates work/capabilities, enforces authority and provenance, observes/reconciles resulting state, and checkpoints durable truth.

The mature distribution target remains an installable Plugin/product surface. Skill packaging may be used as an earlier/contained product surface.

## Stable rule

> The Project persists; Executors and execution environments may change.

No execution environment becomes authoritative merely because execution occurred there.

## Product Architecture 0.2 — frozen 2026-08-28

The active Product Architecture is recorded in `ARCHITECTURE.md` and has four first-class components:

1. Orchestrator;
2. Continuity Provider interface;
3. Execution Surface interface;
4. Capability Provider interface.

Agnir, ChatGPT, and Cloudflare are founding/current bindings, not permanent definitions of Svif.

The stable Svif kernel depends on a **Continuity Provider interface**, not permanently on Agnir. The active repository binding uses Agnir Core `0.1`; Agnir remains an independent protocol/project.

Likewise, ChatGPT is the founding Execution Surface and Cloudflare is the founding external-effect provider family, but neither is a universal kernel dependency.

## Active product contracts

- Svif product line: `0.2` development (`0.2.0-dev`).
- Project Binding: `project-binding/0.2`.
- Portable orchestration contract: `spec/CORE.md`.
- Software Delivery profile: `software-delivery/0.2`.
- Capability Adapter: `capability-adapter/0.2`.
- Evidence record: `evidence-record/0.2`.
- Active Project binding serialization: `SVIF.yaml` for the repository/filesystem integration.

`SVIF.yaml` now binds the Project to replaceable continuity/execution/capability providers. Its filename is not a universal kernel requirement when another installation/execution environment supplies an equivalent binding object.

The internal lifecycle remains:

`DISCOVER -> PLAN -> CHANGE -> VERIFY -> DELIVER -> OBSERVE -> CHECKPOINT`

`REPAIR` returns to the earliest violated invariant. These are Svif product-internal portable orchestration semantics, not the whole product identity.

## Executable Orchestrator kernel

A minimal executable kernel now exists at `src/svif/runtime.py`.

It defines replaceable interfaces for:

- `ContinuityProvider`;
- `ExecutionSurface`;
- `CapabilityProvider`;
- `Orchestrator` as the cross-boundary product kernel.

The current kernel executes the minimum coherent loop:

`load continuity -> execute/materialize result -> verify exact subject -> optional actuate -> observe delivered subject/target -> checkpoint`

For non-effectful work it skips actuation/observation and checkpoints after the execution/verification path.

Runtime invariants currently enforced by executable tests:

- loaded continuity must match the bound Project identity;
- execution must return a stable subject identity;
- external actuation requires successful verification evidence for the exact subject;
- protected actuation requires the declared authority class;
- delivered evidence must match the requested subject and target;
- external success requires independent observation matching the delivered subject/target;
- failed provenance, authority, delivery, or observation paths do not checkpoint false success;
- non-effectful operations do not require delivery/observation.

The kernel does **not** hard-code Agnir, ChatGPT, or Cloudflare. Founding provider names currently appear in test bindings/fakes only.

Python is the current executable reference vehicle for this kernel; the eventual Plugin implementation technology is not frozen by this choice.

## Check separation

Repository integrity and portable contract conformance are now separate concerns:

- `checks/check_repository.py` validates the structure/coherence of `iorLab/svif` itself.
- `conformance/check_contracts.py` validates portable Project Binding, Capability Adapter, and Evidence semantics.
- `tests/test_runtime.py` validates executable Orchestrator behavior.

Passing repository integrity is not a claim that an arbitrary Project is fully Svif-conformant.

## Architecture/runtime evidence

Product Architecture freeze:

- architecture commit: `bb6f445621b65b7ad9cfa99ac0dea759e4ad40fa`;
- semantic repository-check fix: `e201de612dab27bb025f386861ada639a5b0f1e2`;
- run `33138329497`: repository-integrity and portable-contracts both succeeded.

Minimal Orchestrator kernel:

- implementation commit: `c398f17150d5fe868dc60f97dceb58e35025e2e9`;
- product-check run `33138534555`: **success**;
- repository-integrity job `98743936893`: success;
- runtime-kernel job `98743936972`: success;
- portable-contracts job `98743936987`: success.

Durable evidence: `.agnir/evidence/2026-08-28-product-architecture-runtime.md`.

## Cloudflare reference role

`iorLab/svif-cloudflare-reference` remains a separate controlled executable integration reference/E2E pressure test.

As Svif matures, reusable Cloudflare capability behavior should be owned/packaged by Svif and consumed/tested by the reference repository rather than permanently duplicated there.

Existing reference evidence remains valid:

- migration commit `819495b9e708960a613285bb9f37ee859de1652f`, CI run `33096884459` success;
- protected delivery run `33096910154` preserved exact candidate identity but stopped at `CREDENTIAL_UNAVAILABLE`; no live delivery/observation success;
- automatic delivery gate commit `45730121d60a6b8e03e1d5924b257be27ed73a9c`, CI `33097281596` success, Deploy `33097306221` skipped while delivery disabled.

## Validation Project #2

`mattamior/cloud-mail@svif/cloudflare-validation` remains the non-founding real-Project validation case while production `main` stays outside the validation mutation boundary.

Credential-free static verification is proven for immutable candidate `5b32462f3725327805f0dd696475a16f07b666aa` by run `33102032043`, verify job `98621961739` success, and delivery job `98622215176` skipped. Cloud Mail durable evidence synchronization commit: `9c670f4d74921e180734699b6429263bff717b28`.

Live provider delivery/observation remains unproven and requires explicit protected authority.

## Current implementation gap

The generic kernel is now executable, but the founding bindings are still test doubles from the kernel's perspective.

The next product phase is to implement and connect:

1. a concrete Agnir Continuity Provider adapter against current Agnir `0.1`;
2. the first explicit ChatGPT Execution Surface integration/product packaging path;
3. reusable Svif-owned Cloudflare Capability Provider behavior derived from the reference implementation;
4. one end-to-end founding scenario wiring Agnir + ChatGPT + Cloudflare through the Orchestrator without moving protected secrets into Project state.

Only after that path exists should broad non-founding neutrality cases become the main priority.

## Branch governance

- `main`: authoritative active Svif product line.
- `legacy/zerolocal-v0.1`: authoritative predecessor boundary.
- Incidental branch cleanup remains deferred until the new version is substantially complete.
