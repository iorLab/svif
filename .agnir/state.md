# Svif Current State

Svif is the authoritative active project/protocol identity on `main`. ZeroLocal v0.1 is predecessor history preserved on `legacy/zerolocal-v0.1`.

## Active contract line

- Svif Core: `0.2` development line.
- Continuity dependency: Agnir Core `0.1` protocol line.
- Software Delivery Profile: `software-delivery/0.2`.
- Capability Adapter descriptor: `capability-adapter/0.2`.
- Evidence record: `evidence-record/0.2`.
- Project continuity is discovered from top-level `AGNIR.yaml` and stored according to its locators.

## Stable rule

The Project persists; Executors and execution environments may change.

No execution environment becomes authoritative merely because execution occurred there.

## Core lifecycle

`DISCOVER -> PLAN -> CHANGE -> VERIFY -> DELIVER -> OBSERVE -> CHECKPOINT`, with `REPAIR` returning to the earliest violated invariant.

PLAN semantics are mandatory for every material operation. A trivial operation may coalesce the PLAN state in an implementation trace when no separate plan artifact/evidence is material, but the Executor must establish scope, verification, actuation/observation applicability, trust boundaries, and repair considerations before mutation.

`DELIVER` is skipped when no external actuation is required. `OBSERVE` is skipped only when no externally observable effect is claimed.

## Agnir dependency boundary

Svif depends on a compatible Agnir Core protocol, not a specific Agnir repository layout, backend, implementation, adapter, VCS, GitHub integration, or ChatGPT integration. The active development compatibility target is Agnir Core `0.1`.

CHECKPOINT delegates durable persistence/discovery/resumability semantics to Agnir and does not define a competing Svif memory model.

## Evidence and adapters

Svif has a standard evidence record that preserves stable subject identity, derivation, target identity, result, producer, authority reference, and evidence locator across transformation, verification, delivery, and observation.

Capability Adapter operation names are implementation/profile-extensible. Each declared operation must map to a Core semantic effect (`resolve`, `inspect`, `mutate`, `identify`, `verify`, `actuate`, `observe`, `authorize`, `recover`, or `checkpoint`) so orchestration and repair do not depend on provider-specific verbs.

## Branch governance

- `main`: authoritative active Svif line.
- `legacy/zerolocal-v0.1`: authoritative predecessor boundary.
- Incidental branches remain non-authoritative until explicitly promoted; cleanup is deferred until the new version is substantially complete.

## Current implementation status

The active main line is no longer organized around the ZeroLocal v0.1 specification/Skill layout. It contains direct Svif 0.2 Core, Capability Adapter, Evidence, Software Delivery Profile, schemas, Agnir continuity, and an executable conformance checker. Historical ZeroLocal files are removed from the active structure and remain recoverable from the legacy branch.

At the 2026-08-27 checkpoint, the pre-checkpoint `main` head was `f524bf034cbfd2836ca7225cec00e8c1ec31a05c`; Svif conformance run `33081158821` completed successfully for that head.

## Repository identity transition

Repository/public-name cleanup is now approved as the next execution step rather than deferred until the end of the new-version work. The intended coordinated mapping is:

- `mattamior/rpm` -> `mattamior/agnir`
- `iorLab/zerolocal` -> `iorLab/svif`
- `iorLab/zerolocal-cloudflare-starter` -> `iorLab/svif-cloudflare-starter`

Perform the rename in that order: Agnir first, Svif second, Cloudflare starter third. Legacy branch names remain unchanged because they intentionally preserve predecessor identity.

Until each GitHub rename actually occurs, the current repository name remains the resolvable canonical location for that repository. Immediately after each rename, update durable repository references, manifests/shims, README/documentation, cross-project references, and CI/reference URLs; do not rely on GitHub redirects as the normative identity mechanism.

## Known gaps

- Repository rename and reference reconciliation are the immediate next work.
- Capability Adapter schema needs provider/reference fixtures beyond schema validation.
- Evidence-chain conformance needs positive and provenance-mismatch negative fixtures.
- Validation Project #2 must be rewritten against Svif 0.2 + Agnir 0.1 before resuming Cloudflare deployment validation.
- The Cloudflare starter still needs migration to Software Delivery + Provider Adapter terminology.
- At least one materially different execution/storage arrangement from ChatGPT + GitHub + Cloudflare is required before strong neutrality claims.
