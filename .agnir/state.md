# Svif Current State

Svif is the authoritative active **Project orchestration product** on `main`. ZeroLocal v0.1 remains predecessor history on `legacy/zerolocal-v0.1`.

## Canonical repository topology

The active architecture has only two canonical projects/repositories:

- Svif: `iorLab/svif`;
- Agnir: `iorLab/agnir`.

The former `iorLab/svif-cloudflare-reference` project is retired. Cloudflare implementation, provider descriptors, fixtures, tests, and future E2E validation belong inside `iorLab/svif`. The retired repository is historical evidence only and is not an active dependency.

## Product architecture

Svif coordinates four first-class components:

1. **Orchestrator** — `src/svif/runtime.py`;
2. **Continuity Provider** — founding implementation Agnir via `src/svif/continuity/agnir.py`;
3. **Execution Surface** — founding ChatGPT bridge via `src/svif/execution/chatgpt.py`;
4. **Capability Provider** — founding Cloudflare Workers provider via `src/svif/capabilities/cloudflare.py`.

Stable rule:

> The Project persists; Executors and execution environments may change.

No execution environment becomes authoritative merely because execution occurred there.

## Distribution target

The mature Svif distribution target is an **installable Plugin**. This durable product intent was inherited from the ZeroLocal predecessor, detected as missing during migration audit, and restored.

Current ChatGPT Apps SDK / MCP work is the concrete packaging/integration path for the founding ChatGPT Execution Surface. It does **not** replace the Plugin product target or become canonical Project truth.

Distribution dependency direction remains:

`Plugin / distribution -> Execution Surface integration -> Orchestrator -> Continuity + Capability Providers`

The Plugin target is synchronized in `ARCHITECTURE.md`, `.agnir/decisions.md`, this state file, `README.md`, and `README.zh-CN.md`.

## Agnir compatibility boundary

Svif binds to **Agnir Core compatibility `"0.1"`**, as already serialized in `SVIF.yaml`:

`bindings.continuity.compatibility: "0.1"`

This is now the correct frozen compatibility boundary. Svif MUST NOT bind its product semantics to Agnir repository release `0.1.0-rc.1`, a particular Agnir patch release, repository layout, backend, or adapter implementation.

Agnir repository `main` has entered `0.1.0-rc.1`; that release label is distinct from the Core compatibility line consumed by Svif.

## Active contracts

- Svif product line: `0.2` development (`0.2.0-dev`).
- Project Binding: `project-binding/0.2`.
- Software Delivery profile: `software-delivery/0.2`.
- Capability Adapter: `capability-adapter/0.2`.
- Evidence record: `evidence-record/0.2`.
- Repository/filesystem binding serialization: `SVIF.yaml`.

## Executable product foundation

Implemented under Svif ownership:

- generic Orchestrator with synchronous and externally driven execution paths;
- Agnir repository/filesystem Continuity Provider;
- ChatGPT structured Execution Surface bridge;
- Cloudflare Workers Capability Provider with injected transport boundary;
- founding credential-free E2E scenario at `tests/test_founding_e2e.py`;
- runtime/provider/surface tests and portable contract conformance.

The founding E2E proves the complete credential-free product loop through the real interfaces: Agnir continuity load -> `Orchestrator.begin()` -> ChatGPT context materialization/result parsing -> trusted authority at `Orchestrator.complete()` -> exact-subject Cloudflare actuation through injected fake transport -> independent observation -> Agnir checkpoint -> continuity reload/resume.

Cloudflare authority remains enforced outside untrusted model payloads. External actuation requires successful verification for the exact subject plus required authority, and external success requires independent observation before checkpoint.

Founding E2E success is not evidence of live Cloudflare production delivery; live delivery remains separately authorized and separately evidenced.

## Repository documentation baseline

The repository has parallel English and Simplified Chinese entry points: `README.md` and `README.zh-CN.md`.

Both contain current Architecture and Runtime / Operation Flow diagrams plus a compact plain-text repository tree. Localized Mermaid diagrams are comprehension-first rather than literal translations.

`REPOSITORY_TREE.md` is the exhaustive tracked-file map. Architecture/runtime changes update both README language versions; tracked file additions/removals/moves or material responsibility changes update `REPOSITORY_TREE.md` in the same change set, and both compact README trees when affected.

## Predecessor migration status

The real semantic migration audit from `iorLab/svif@legacy/zerolocal-v0.1` is **complete**.

Predecessor boundary:

- branch `legacy/zerolocal-v0.1`;
- commit `8ccbb1d30520ca3d0b8b9f2cfe2963d35a853cf6`;
- predecessor continuity entry `.chatgpt/project-memory.yaml` with `version: 1`.

The audit explicitly compares material durable knowledge and classifies it as preserved, generalized, intentionally retired, repaired after regression, or not inherited. Major preserved/generalized invariants include:

- installable Plugin as mature product target;
- provider-neutral core with Cloudflare only as founding provider;
- protected secret/authority boundaries;
- exact verified-subject provenance before external actuation;
- independent observation before external success;
- fresh-context resumability owned by the Project rather than ChatGPT history.

Intentional transitions include:

- predecessor RPM / `.chatgpt/` memory -> Agnir Continuity Provider semantics;
- ChatGPT-specific locator bootstrap -> generic Project Entry Point / Discovery Record;
- standalone Cloudflare reference project -> Svif-owned Capability Provider;
- ZeroLocal Skills / predecessor specification/conformance -> historical lineage, not active Svif 0.2 product structure.

One real durable-knowledge regression was found and repaired: the predecessor's explicit `installable-plugin` target had been generalized away during the rewrite.

Classification:

- real predecessor migration: **PASS, v1/RPM-era**;
- it is **not** exact PPMP v2 evidence;
- historical ZeroLocal validation evidence is not relabeled as current Svif conformance or live-provider evidence.

Durable evidence: `.agnir/evidence/2026-08-28-zerolocal-predecessor-migration.md`.

Agnir separately supplies canonical exact PPMP v2 historical source and executable PPMP v2 -> Agnir migration conformance, so Svif no longer carries an unresolved exact-PPMP-v2 release dependency.

## Current implementation gap / resume point

1. **Harden concrete ChatGPT Apps SDK / MCP packaging** around the existing `ChatGPTExecutionSurface` and `Orchestrator.begin()` / `complete()` lifecycle, without duplicating kernel semantics or moving protected authority into untrusted payloads.
2. **Add broader neutrality pressure** using Agnir's storage-neutral and multi-project isolation cases; prove Svif composition does not require GitHub, Cloudflare, or ChatGPT as universal kernel dependencies.
3. Mature the installable Plugin packaging only on top of validated kernel/integration behavior rather than reimplementing orchestration in the distribution layer.
4. Keep live Cloudflare delivery disabled unless explicitly authorized; any future success claim requires exact verified-subject delivery plus independent observation.
5. Keep incidental branch cleanup deferred until the new Svif version is substantially complete.

## Evidence checkpoints

- README/localization: `.agnir/evidence/2026-08-28-readme-diagram-localization-checkpoint.md`.
- Founding E2E: `.agnir/evidence/2026-08-28-founding-e2e.md`, run `33143308949` success.
- Plugin / predecessor-migration audit checkpoint: `.agnir/evidence/2026-08-28-plugin-migration-audit-checkpoint.md`.
- Real semantic predecessor migration: `.agnir/evidence/2026-08-28-zerolocal-predecessor-migration.md`.
- Repository documentation baseline: pre-checkpoint head `97e70f9980de36aa7e3095cf8284f40c6fbf285e`, product-check run `33146795882` success.

## Branch governance

- `main`: authoritative active Svif product line;
- `legacy/zerolocal-v0.1`: predecessor history;
- incidental branch cleanup remains deferred until the new version is substantially complete.
