# Svif Current State

Svif is the authoritative active **Project orchestration product** on `main`. ZeroLocal v0.1 remains predecessor history on `legacy/zerolocal-v0.1`.

## Canonical repository topology

The active architecture has only two canonical projects/repositories:

- Svif: `iorLab/svif`;
- Agnir: `iorLab/agnir`.

The former `iorLab/svif-cloudflare-reference` project is retired. Cloudflare implementation, provider descriptors, fixtures, tests, and future E2E validation belong inside `iorLab/svif`. The old repository is historical evidence only and is not an active dependency.

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

The mature Svif distribution target is an **installable Plugin**. This target is durable product intent inherited from the ZeroLocal predecessor and was re-established after migration audit found that it had been generalized away during the architecture rewrite.

Current ChatGPT Apps SDK / MCP work is the concrete packaging/integration path for the founding ChatGPT Execution Surface. It does **not** replace the Plugin product target or become canonical Project truth.

Distribution dependency direction remains:

`Plugin / distribution -> Execution Surface integration -> Orchestrator -> Continuity + Capability Providers`

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

Cloudflare authority remains enforced outside untrusted model payloads. External actuation still requires successful verification for the exact subject plus required authority, and external success still requires independent observation before checkpoint.

The Cloudflare provider transport intentionally does not embed credentials or freeze GitHub Actions/Wrangler as product dependencies. Founding E2E success is not evidence of live Cloudflare production delivery; live delivery remains separately authorized and separately evidenced.

## README architecture documentation

The repository has parallel English and Simplified Chinese entry points: `README.md` and `README.zh-CN.md`.

Both READMEs contain Architecture and Runtime / Operation Flow diagrams. Architecture/runtime changes require synchronized bilingual documentation; localized diagrams are comprehension-first rather than literal translations.

The restored installable Plugin distribution target is now canonical in `ARCHITECTURE.md`, `.agnir/decisions.md`, and this state file. **README.md and README.zh-CN.md still need explicit Plugin-target synchronization after this checkpoint.**

## Historical Cloudflare evidence

The retired standalone reference supplied useful migration evidence but no live success claim. Preserved details are in `history/CLOUDFLARE_REFERENCE.md`.

No active Svif code, test, release, Project binding, or next action may depend on the retired repository.

## Validation Project #2

`mattamior/cloud-mail@svif/cloudflare-validation` remains a non-founding external Project validation case. Credential-free static verification is proven for immutable candidate `5b32462f3725327805f0dd696475a16f07b666aa` by run `33102032043`; protected delivery was skipped. Production `main` remains outside that validation mutation boundary.

## Predecessor migration audit

`iorLab/svif@legacy/zerolocal-v0.1` is a real predecessor Project. Its `.chatgpt/project-memory.yaml` and predecessor state are suitable for validating predecessor-memory -> current Svif/Agnir semantic migration.

The audit found one material durable-knowledge regression: predecessor state explicitly preserved `installable-plugin` as the long-term product form, while current Svif had generalized that intent to `distribution` and omitted it from canonical Project state. The Plugin target has now been restored in architecture, decisions, and state.

The ZeroLocal predecessor serialization is an earlier v1/RPM-era form, **not PPMP v2.0.0**. It must not be relabeled as exact PPMP v2 evidence. A qualifying second external PPMP v2 Project was not found during this audit.

## Current implementation gap

1. Synchronize the restored installable Plugin target into `README.md` and `README.zh-CN.md` and rerun product checks.
2. Complete a durable ZeroLocal predecessor -> current Svif/Agnir migration evidence envelope, explicitly separating real predecessor-memory validation from the missing exact external PPMP v2 fixture.
3. Harden concrete ChatGPT app/MCP packaging around the existing externally driven bridge without duplicating kernel semantics.
4. Add broader neutrality pressure using Agnir's now-proven storage-neutral and multi-project isolation fixtures.
5. Freeze exact Agnir compatibility/release expression only after Agnir Core `0.1` release criteria are reconciled.

Live Cloudflare delivery remains disabled unless explicitly authorized.

## Evidence checkpoints

- README/localization: `.agnir/evidence/2026-08-28-readme-diagram-localization-checkpoint.md`.
- Founding E2E: `.agnir/evidence/2026-08-28-founding-e2e.md`, run `33143308949` success.
- Plugin / predecessor-migration audit: `.agnir/evidence/2026-08-28-plugin-migration-audit-checkpoint.md`.
- Pre-checkpoint Plugin-restoration head `98868f5052a6d2e2e4b92a1f3f534dbdae799764`; product-check run `33144484052` success.

## Branch governance

- `main`: authoritative active Svif product line;
- `legacy/zerolocal-v0.1`: predecessor history;
- incidental branch cleanup remains deferred until the new version is substantially complete.
