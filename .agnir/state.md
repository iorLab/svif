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

The mature Svif distribution target is an **installable Plugin**. This target is durable product intent inherited from the ZeroLocal predecessor and was re-established after migration audit found that it had been generalized away during the architecture rewrite.

Current ChatGPT Apps SDK / MCP work is the concrete packaging/integration path for the founding ChatGPT Execution Surface. It does **not** replace the Plugin product target or become canonical Project truth.

Distribution dependency direction remains:

`Plugin / distribution -> Execution Surface integration -> Orchestrator -> Continuity + Capability Providers`

The Plugin target is now synchronized in `ARCHITECTURE.md`, `.agnir/decisions.md`, this state file, `README.md`, and `README.zh-CN.md`.

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

Founding E2E success is not evidence of live Cloudflare production delivery; live delivery remains separately authorized and separately evidenced.

## Repository documentation baseline

The repository has parallel English and Simplified Chinese entry points: `README.md` and `README.zh-CN.md`.

Both READMEs contain:

- a current Architecture Diagram;
- a current Runtime / Operation Flow diagram;
- a compact plain-text repository tree that maps major directories and key files to responsibilities.

Localized Mermaid diagrams are comprehension-first rather than literal translations. Simplified Chinese nodes explain both what a component is and what it does.

A separate `REPOSITORY_TREE.md` is the exhaustive file-level repository map. It expands the current tracked `main` tree and annotates the responsibility of each tracked file. README trees remain compact navigation views; `REPOSITORY_TREE.md` is the detailed map.

Maintenance invariant:

- architecture/runtime changes update both README language versions in the same change set;
- tracked file additions/removals/moves or material responsibility changes update `REPOSITORY_TREE.md` in the same change set;
- if such a change also affects the compact README tree, both README language versions update in the same change set.

Repository integrity checks enforce the bilingual diagram/tree anchors, the `REPOSITORY_TREE.md` link, and representative deep-file coverage without byte-for-byte locking documentation prose.

The pre-checkpoint repository-documentation head `97e70f9980de36aa7e3095cf8284f40c6fbf285e` passed Svif product-check run `33146795882`.

## Predecessor migration audit

`iorLab/svif@legacy/zerolocal-v0.1` is a real predecessor Project. Its `.chatgpt/project-memory.yaml` and predecessor state are suitable for validating predecessor-memory -> current Svif/Agnir semantic migration.

The audit found one material durable-knowledge regression: predecessor state explicitly preserved `installable-plugin` as the long-term product form, while current Svif had generalized that intent to `distribution` and omitted it from canonical Project state. The Plugin target has now been restored and synchronized across canonical architecture/state/decisions and both READMEs.

The ZeroLocal predecessor serialization is an earlier v1/RPM-era form, **not PPMP v2.0.0**. It must not be relabeled as exact PPMP v2 evidence. A qualifying second external PPMP v2 Project was not found during this audit.

## Current implementation gap / resume point

1. Complete a durable ZeroLocal predecessor -> current Svif/Agnir migration evidence envelope, explicitly separating genuine v1/RPM-era predecessor evidence from the missing exact external PPMP v2 fixture.
2. Harden concrete ChatGPT app/MCP packaging around the existing externally driven bridge without duplicating Orchestrator/kernel semantics.
3. Add broader neutrality pressure using Agnir's proven storage-neutral and multi-project isolation fixtures.
4. Freeze exact Agnir compatibility/release expression only after Agnir Core `0.1` release criteria are reconciled.
5. Keep live Cloudflare delivery disabled unless explicitly authorized; any future success claim still requires exact verified-subject delivery plus independent observation.

## Evidence checkpoints

- README/localization: `.agnir/evidence/2026-08-28-readme-diagram-localization-checkpoint.md`.
- Founding E2E: `.agnir/evidence/2026-08-28-founding-e2e.md`, run `33143308949` success.
- Plugin / predecessor-migration audit: `.agnir/evidence/2026-08-28-plugin-migration-audit-checkpoint.md`.
- Repository documentation baseline: pre-checkpoint head `97e70f9980de36aa7e3095cf8284f40c6fbf285e`, product-check run `33146795882` success.

## Branch governance

- `main`: authoritative active Svif product line;
- `legacy/zerolocal-v0.1`: predecessor history;
- incidental branch cleanup remains deferred until the new version is substantially complete.
