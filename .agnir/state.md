# Svif Current State

Svif is the authoritative active **product** identity on `main`. ZeroLocal v0.1 is predecessor history preserved on `legacy/zerolocal-v0.1`.

## Product identity correction — 2026-08-28

Svif is **not** a pure Project-operation protocol. It is a Project orchestration product intended to become an installable/distributable capability, with the mature distribution target remaining a Plugin.

Its stable product role is to coordinate three replaceable sides around a Project:

1. **Continuity Provider** — durable Project truth and resumability. Current implementation: **Agnir**.
2. **Execution Surface / Executor Host** — where intent is interpreted and work is performed. Current founding integration: **ChatGPT**.
3. **Capability / Effect Provider** — where Svif causes and observes external/authoritative effects. Current founding provider: **Cloudflare**.

Svif itself is the orchestration layer that binds these sides, enforces lifecycle, authority, provenance, and observation invariants, reconciles resulting state, and checkpoints durable Project truth.

Agnir stores durable Project continuity; an execution surface such as ChatGPT consumes that continuity and performs work; a capability provider such as Cloudflare changes external state; Svif keeps these processes coherent.

The existing lifecycle remains useful as an internal Svif operational contract:

`DISCOVER -> PLAN -> CHANGE -> VERIFY -> DELIVER -> OBSERVE -> CHECKPOINT`, with `REPAIR` returning to the earliest violated invariant.

These semantics describe how Svif operates; they do not make Svif itself a standalone protocol in the same sense as Agnir.

## Current architecture line

- Svif product line: `0.2` development.
- Continuity dependency: Agnir Core `0.1` protocol line.
- Software Delivery specialization: `software-delivery/0.2`.
- Capability Adapter contract: `capability-adapter/0.2`.
- Evidence record: `evidence-record/0.2`.
- Current version marker: `0.2.0-dev`.
- Active branch: `main`.
- Predecessor: `legacy/zerolocal-v0.1`.

## Stable rule

The Project persists; Executors and execution environments may change.

No execution environment becomes authoritative merely because execution occurred there.

This rule remains valid, but it is a product architecture invariant rather than sufficient definition of Svif's product identity.

## Agnir dependency boundary

Agnir remains an independent project/protocol and the current Continuity Provider. Dependency direction is `Svif -> Agnir`.

Svif consumes Agnir through a portable continuity boundary and MUST NOT make ChatGPT, GitHub, Git, `.agnir/`, a repository/filesystem backend, or any specific Agnir implementation part of Svif product identity.

CHECKPOINT delegates durable persistence/discovery/resumability semantics to Agnir and does not define a competing Svif memory model.

## Existing assets that remain valid

The current protocol-oriented work is not discarded. The following are retained as internal product contracts/foundations:

- lifecycle semantics;
- Evidence/provenance model;
- Capability Adapter vocabulary and portable semantic effects;
- verification/delivery authority separation;
- protected-secret transport boundary;
- Software Delivery specialization;
- Agnir continuity dependency;
- executable provider/reference evidence.

Evidence provenance remains important because Svif must keep the subject that was changed, verified, delivered, observed, and checkpointed coherent across the three sides.

Capability Adapter semantic effects remain:

`resolve`, `inspect`, `mutate`, `identify`, `verify`, `actuate`, `observe`, `authorize`, `recover`, `checkpoint`.

They should be treated as Svif runtime capability boundaries rather than evidence that Svif is primarily a standards/protocol repository.

## Current identity/structure drift

The current `main` over-rotated from execution-surface/provider neutrality into protocol/specification identity.

Symptoms:

- `README.md` and `spec/CORE.md` currently define Svif as an execution-environment-independent Project operation protocol.
- The repository is dominated by `spec/`, `profiles/`, `schemas/`, and `conformance/`.
- There is no real Svif orchestration runtime that loads continuity, materializes execution context, selects/invokes capabilities, enforces authority/provenance, reconciles results, and checkpoints state.
- ChatGPT-specific canonical state was correctly removed, but the active product also lost an explicit ChatGPT execution-surface integration layer.
- Reusable Cloudflare behavior remains mostly in `iorLab/svif-cloudflare-reference` rather than in a Svif-owned capability implementation consumed by the reference.
- `SVIF.yaml` currently behaves mainly as repository self-description; its future role as a Project binding/configuration manifest remains unresolved.
- `conformance/check_svif_0_2.py` currently mixes specification-repository integrity with portable conformance semantics.

This is an architecture/product-identity drift, not a reason to discard the portable contracts already developed.

## Intended product architecture

Before expanding conformance breadth, Svif should freeze a Product Architecture with four first-class components:

1. **Orchestrator** — load continuity, construct execution context, plan/execute operations, select capabilities, enforce authority/provenance, observe results, reconcile state, checkpoint continuity.
2. **Continuity Provider interface** — first implementation: Agnir.
3. **Execution Surface interface** — first integration: ChatGPT; future surfaces may include CLI, IDE, CI, or other executors.
4. **Capability Provider interface** — first provider family: Cloudflare; future providers may include other deployment/external systems.

Target dependency direction:

`Plugin/distribution -> execution-surface integration -> Svif orchestrator -> continuity + capability providers`

Project canonical truth remains execution-surface-neutral even when the Svif product integrates deeply with ChatGPT.

## Branch governance

- `main`: authoritative active Svif product line.
- `legacy/zerolocal-v0.1`: authoritative predecessor boundary.
- Incidental branches remain non-authoritative until explicitly promoted; cleanup is deferred until the new version is substantially complete.

## Canonical repositories

- Agnir: `iorLab/agnir`
- Svif: `iorLab/svif`
- Cloudflare executable reference/testbed: `iorLab/svif-cloudflare-reference`

Legacy branch names remain unchanged because they intentionally preserve predecessor identity.

## Cloudflare reference role and evidence

`iorLab/svif-cloudflare-reference` remains separate, but its mature role is a controlled executable integration reference/testbed for Svif Software Delivery + Cloudflare behavior, not a second Svif specification repository and not a user starter/template.

As Svif product implementation matures, reusable Cloudflare capability behavior should move into or be owned by Svif, while the reference repository increasingly consumes/tests that capability as E2E validation.

Existing evidence remains valid:

- Migration commit `819495b9e708960a613285bb9f37ee859de1652f` passed CI run `33096884459`.
- Deploy run `33096910154` preserved the exact verified SHA but stopped at `CREDENTIAL_UNAVAILABLE`; observation was skipped and no live delivery success is claimed.
- Automatic delivery remains separately gated by `SVIF_ENABLE_PRODUCTION_DELIVERY=true`.
- Authority-gate commit `45730121d60a6b8e03e1d5924b257be27ed73a9c` passed CI run `33097281596`; Deploy run `33097306221` was correctly skipped with delivery disabled.

## Validation Project #2 evidence

`mattamior/cloud-mail@svif/cloudflare-validation` remains the non-founding real-Project validation case while production `main` stays outside the validation mutation boundary.

Credential-free static verification is proven:

- immutable candidate `5b32462f3725327805f0dd696475a16f07b666aa`;
- Svif Validation run `33102032043` succeeded;
- verify job `98621961739` succeeded;
- delivery job `98622215176` was skipped;
- Cloud Mail durable evidence synchronization commit `9c670f4d74921e180734699b6429263bff717b28`.

Live provider delivery/observation remains unproven and requires explicit protected authority.

## Current architectural gaps

Before further neutrality/conformance expansion, resolve:

- minimal Svif Orchestrator/runtime responsibilities;
- Continuity Provider, Execution Surface, and Capability Provider interfaces;
- the role of `SVIF.yaml` as repository self-description versus Project binding/configuration manifest;
- separation of specification-repository integrity checks from portable product/contract conformance;
- which Cloudflare reference behaviors become reusable Svif-owned capabilities;
- the first distributable ChatGPT surface on the path from product capability to final Plugin;
- how existing Core/Evidence/Capability Adapter/Software Delivery material maps into the product architecture without turning Svif back into a pure protocol project.

The previously planned materially non-GitHub/Cloudflare conformance case is paused until this product architecture correction is resolved.
