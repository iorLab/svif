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

Svif depends on a compatible Agnir Core protocol, not a specific Agnir repository layout, backend, implementation, adapter, VCS, GitHub integration, or ChatGPT integration. The active development compatibility target is Agnir Core `0.1`. The current Agnir project repository is `iorLab/agnir`.

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

The active main line is no longer organized around the ZeroLocal v0.1 specification/Skill layout. It contains direct Svif 0.2 Core, Capability Adapter, Evidence, Software Delivery Profile, schemas, Agnir continuity, and an executable conformance checker. Historical ZeroLocal files are removed from the active structure and remain recoverable from the legacy branch.

On 2026-08-27, evidence-chain conformance landed in commit `853ea4bf05679ab2b03864aeaa01e8aae9350542`; Svif conformance run `33090238664` completed successfully.

On 2026-08-27, concrete Capability Adapter fixtures landed in commit `67c7b4e93e0130d37c01c40a261b55fba381f786`; Svif conformance run `33090480399` completed successfully.

## Repository identity transition

The coordinated repository identity transition is complete.

Canonical repositories are now:

- Agnir: `iorLab/agnir` (renamed from `mattamior/rpm` and transferred into the organization)
- Svif: `iorLab/svif`
- Cloudflare reference repository: `iorLab/svif-cloudflare-starter`

Legacy branch names remain unchanged because they intentionally preserve predecessor identity. GitHub redirects from predecessor repository names are compatibility behavior only; active durable repository references use the canonical names above.

## Cloudflare reference boundary

`iorLab/svif-cloudflare-starter` is currently a ZeroLocal-era executable Cloudflare delivery fixture after repository rename. Its existing contents demonstrate real CI/deploy/trust-boundary behavior, but still use `ZEROLOCAL.yaml` and ZeroLocal vocabulary. It must be semantically recast before it can serve as Svif provider/profile implementation evidence. Whether its public name should remain `starter` or become a more precise `reference`/`adapter` identity is an explicit packaging decision, not a Core protocol decision.

## Known gaps

- Decide and implement the final packaging/role of the Cloudflare repository, then recast it as Svif Software Delivery + Cloudflare Provider Adapter evidence if retained.
- Rewrite Validation Project #2 against Svif 0.2 + Agnir 0.1 before resuming Cloudflare deployment validation.
- Add at least one materially different execution/storage arrangement from ChatGPT + GitHub + Cloudflare before making strong neutrality claims.
- Add multi-project workspace isolation conformance after Agnir's corresponding fixture is ready.
- Freeze the exact Agnir compatibility expression only after Agnir 0.1 release criteria are concrete.
