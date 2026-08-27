# Svif Current State

Svif is the authoritative active project/protocol identity on `main`. ZeroLocal v0.1 is predecessor history preserved on `legacy/zerolocal-v0.1`.

## Active contract line

- Svif Core: `0.2` development line.
- Continuity dependency: Agnir Core `0.1` protocol line.
- Software Delivery Profile: `software-delivery/0.2`.
- Capability Adapter descriptor: `capability-adapter/0.2`.
- Evidence record: `evidence-record/0.2`.
- Project continuity is discovered from top-level `AGNIR.yaml` and stored according to its locators.
- Active Project structure no longer contains execution-surface-specific bootstrap files.

## Stable rule

The Project persists; Executors and execution environments may change.

No execution environment becomes authoritative merely because execution occurred there.

## Core lifecycle

`DISCOVER -> PLAN -> CHANGE -> VERIFY -> DELIVER -> OBSERVE -> CHECKPOINT`, with `REPAIR` returning to the earliest violated invariant.

PLAN semantics are mandatory for every material operation. A trivial operation may coalesce the PLAN state in an implementation trace when no separate plan artifact/evidence is material, but the Executor must establish scope, verification, actuation/observation applicability, trust boundaries, and repair considerations before mutation.

`DELIVER` is skipped when no external actuation is required. `OBSERVE` is skipped only when no externally observable effect is claimed.

## Agnir dependency boundary

Svif depends on a compatible Agnir Core protocol, not a specific Agnir repository layout, backend, implementation, adapter, VCS, repository host, agent, or execution surface. The active development compatibility target is Agnir Core `0.1`. The current Agnir project repository is `iorLab/agnir`.

CHECKPOINT delegates durable persistence/discovery/resumability semantics to Agnir and does not define a competing Svif memory model.

## Evidence and adapters

Svif has a standard evidence record that preserves stable subject identity, derivation, target identity, result, producer, authority reference, and evidence locator across transformation, verification, delivery, and observation.

Evidence provenance is executable conformance rather than schema-only validation. The positive fixture covers source candidate -> artifact transformation -> verification -> delivery -> observation. The negative fixture establishes a valid replacement artifact but deliberately delivers it without independent verification; conformance requires this to fail specifically as a provenance violation.

Capability Adapter operation names are implementation/profile-extensible. Each declared operation must map to a Core semantic effect (`resolve`, `inspect`, `mutate`, `identify`, `verify`, `actuate`, `observe`, `authorize`, `recover`, or `checkpoint`) so orchestration and repair do not depend on provider-specific verbs.

Concrete executable adapter fixtures cover workspace/SCM, verification, delivery/provider, and observation boundaries. They enforce semantic-effect mappings, authority and retry classes, portable failure classes, Evidence record I/O declarations, verification/delivery authority separation, protected credential references without secret-value transport, provenance mismatch reporting, and independent observation semantics.

## Branch governance

- `main`: authoritative active Svif line.
- `legacy/zerolocal-v0.1`: authoritative predecessor boundary.
- Incidental branches remain non-authoritative until explicitly promoted; cleanup is deferred until the new version is substantially complete.

## Current implementation status

The active main line contains direct Svif 0.2 Core, Capability Adapter, Evidence, Software Delivery Profile, schemas, Agnir continuity, and executable conformance. Historical ZeroLocal files remain recoverable from the legacy branch.

The former ChatGPT-specific bootstrap shim has been removed from active `main`; repository cold start now begins directly with `AGNIR.yaml`.

On 2026-08-27, evidence-chain conformance landed in commit `853ea4bf05679ab2b03864aeaa01e8aae9350542`; Svif conformance run `33090238664` completed successfully.

On 2026-08-27, concrete Capability Adapter fixtures landed in commit `67c7b4e93e0130d37c01c40a261b55fba381f786`; Svif conformance run `33090480399` completed successfully.

## Canonical repositories

- Agnir: `iorLab/agnir`
- Svif: `iorLab/svif`
- Cloudflare executable reference: `iorLab/svif-cloudflare-reference`

Legacy branch names remain unchanged because they intentionally preserve predecessor identity. Repository redirects from predecessor names are compatibility behavior only.

## Cloudflare reference boundary

`iorLab/svif-cloudflare-reference` is the provider-specific executable reference implementation for Svif Software Delivery + Cloudflare Provider Adapter semantics. It is not a user starter/template and it does not define provider-neutral Core behavior.

Its migration from the ZeroLocal-era fixture is the current provider/profile implementation task: move continuity to Agnir, replace `ZEROLOCAL.yaml` with Svif-native self-description and a concrete Cloudflare Capability Adapter descriptor, preserve exact verified-candidate delivery, protected production authority, serialized delivery, target discovery, and independent post-delivery observation.

## Known gaps

- Complete and validate the Svif-native Cloudflare reference implementation and record provider/profile implementation evidence.
- Rewrite Validation Project #2 against Svif 0.2 + Agnir 0.1 before resuming live Cloudflare deployment validation.
- Add at least one materially different execution/storage arrangement from the founding GitHub + Cloudflare path before making strong neutrality claims.
- Add multi-project workspace isolation conformance after Agnir's corresponding fixture is ready.
- Freeze the exact Agnir compatibility expression only after Agnir 0.1 release criteria are concrete.
