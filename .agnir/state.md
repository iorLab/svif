# Svif Current State

Svif is the authoritative active project/protocol identity on `main`. ZeroLocal v0.1 is predecessor history preserved on `legacy/zerolocal-v0.1`.

## Active contract line

- Svif Core: `0.2` development line.
- Continuity dependency: Agnir Core `0.1` protocol line.
- Software Delivery Profile: `software-delivery/0.2`.
- Capability Adapter descriptor: `capability-adapter/0.2`.
- Evidence record: `evidence-record/0.2`.
- Project continuity is discovered from top-level `AGNIR.yaml` and stored according to its locators.
- Active Project structure contains no execution-surface-specific bootstrap files.

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

The former execution-surface-specific bootstrap shim has been removed from active `main`; repository cold start begins directly with `AGNIR.yaml`.

On 2026-08-27, evidence-chain conformance landed in commit `853ea4bf05679ab2b03864aeaa01e8aae9350542`; Svif conformance run `33090238664` completed successfully.

On 2026-08-27, concrete Capability Adapter fixtures landed in commit `67c7b4e93e0130d37c01c40a261b55fba381f786`; Svif conformance run `33090480399` completed successfully.

On 2026-08-28, execution-surface bootstrap removal landed in commit `2cf537e7a1612599ab26e6a331d0b1ffe45b88fd`; Svif conformance run `33096542705` completed successfully.

## Canonical repositories

- Agnir: `iorLab/agnir`
- Svif: `iorLab/svif`
- Cloudflare executable reference: `iorLab/svif-cloudflare-reference`

Legacy branch names remain unchanged because they intentionally preserve predecessor identity. Repository redirects from predecessor names are compatibility behavior only.

## Cloudflare reference implementation evidence

`iorLab/svif-cloudflare-reference` is now a Svif/Agnir-native executable reference implementation rather than a ZeroLocal-era starter fixture.

- The predecessor fixture is preserved on `legacy/zerolocal-v0.1`.
- Active `main` uses `AGNIR.yaml`, `.agnir/`, `SVIF.yaml`, and a concrete `cloudflare.workers` Capability Adapter descriptor; active `.chatgpt/` and `ZEROLOCAL.yaml` were removed.
- Migration commit `819495b9e708960a613285bb9f37ee859de1652f` passed CI run `33096884459`.
- Deploy run `33096910154` preserved the exact verified SHA through the delivery boundary but failed at provider actuation because `CLOUDFLARE_API_TOKEN` was unavailable. This is classified as `CREDENTIAL_UNAVAILABLE`; observation was skipped and no live delivery success is claimed.
- Automatic delivery is now explicitly separated from verification authority through the non-secret gate `SVIF_ENABLE_PRODUCTION_DELIVERY=true`.
- Authority-gate commit `45730121d60a6b8e03e1d5924b257be27ed73a9c` passed CI run `33097281596`; its Deploy run `33097306221` was correctly `skipped` with production delivery disabled.

The reference therefore provides executable provider/profile evidence for static conformance, provenance, verification/delivery authority separation, and disabled-authority behavior. Successful live Cloudflare delivery + independent `/health` observation remains an explicit unproven boundary until protected authority is enabled.

## Validation Project #2 evidence

`mattamior/cloud-mail` now has a Svif/Agnir-native non-founding validation ref `svif/cloudflare-validation`, derived from predecessor ref `zerolocal/cloudflare-validation` while keeping production `main` outside the validation mutation boundary.

- Migration commit `250e5173f3cb0258e865097f9f9cd632aabe95f0` replaced active `.chatgpt/`, `ZEROLOCAL.yaml`, predecessor workflow/script/config names with `AGNIR.yaml`, `.agnir/`, `SVIF.yaml`, a Cloudflare validation Capability Adapter, explicit success criteria, and a Svif validation workflow.
- Production `.github/workflows/deploy-cloudflare.yml` was not changed by the migration.
- Svif Validation run `33098133983` failed in its conformance step before dependency install/build/dry-run. The failure was traced to the checker requiring literal `checks.assets` while the existing Cloud Mail health hook validly expresses the assets check as `assets: Boolean(env.assets)`.
- The failed run's protected delivery job was skipped; no provider actuation or observation occurred.
- Checker fix commit `dde68f0b2c55224ba5e36bc6d7c30671ff311b25` relaxes the implementation-form assumption without weakening the semantic health contract.
- Explicit checkpoint commit `5b32462f3725327805f0dd696475a16f07b666aa` persists the current Validation #2 state, next actions, and evidence in Agnir.
- At this checkpoint, a successful post-fix credential-free static verification run has not yet been recorded, so Validation Project #2 static success and end-to-end success remain unproven.
- Live provider actuation remains explicitly gated by `SVIF_ENABLE_VALIDATION_DELIVERY=true` and is disabled by default.

## Known gaps

- Complete the post-checker credential-free static verification for Validation Project #2 and record the immutable candidate/run evidence if and only if it succeeds.
- Complete a successful protected Cloudflare delivery + `/health` observation when live authority is explicitly enabled; do not treat this as a prerequisite for provider-neutral Core work.
- Add at least one materially different execution/storage arrangement from the founding GitHub + Cloudflare path before making strong neutrality claims.
- Add multi-project workspace isolation conformance after Agnir's corresponding fixture is ready.
- Freeze the exact Agnir compatibility expression only after Agnir 0.1 release criteria are concrete.
