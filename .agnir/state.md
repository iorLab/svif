# Svif Current State

Svif is the authoritative active **Project orchestration product** on `main`. Repository branch governance is main-only: predecessor and retired branch history are preserved by commit SHA and `history/`, not by live branch refs.

## Canonical repository topology

The active architecture has only two canonical projects/repositories:

- Svif: `iorLab/svif`;
- Agnir: `iorLab/agnir`.

The former `iorLab/svif-cloudflare-reference` project is retired. Cloudflare implementation, provider descriptors, fixtures, tests, and future E2E validation belong inside `iorLab/svif`. Historical repositories and retired branches are evidence only; they are not active dependencies, compatibility obligations, or release gates.

## Product architecture

Svif coordinates four first-class components:

1. **Orchestrator** — `src/svif/runtime.py`;
2. **Continuity Provider** — founding implementation Agnir via `src/svif/continuity/agnir.py`;
3. **Execution Surface** — founding ChatGPT bridge via `src/svif/execution/chatgpt.py`;
4. **Capability Provider** — founding Cloudflare Workers provider via `src/svif/capabilities/cloudflare.py`.

Stable rule:

> The Project persists; Executors and execution environments may change.

No execution environment becomes authoritative merely because execution occurred there.

## Distribution status

Svif now has an active **Plugin MVP**, not merely a future Plugin target.

The first installable package lives under `plugin/` and targets the portable Agent Plugins `1.0.0` package format:

- `plugin/plugin.json` — Plugin manifest;
- `plugin/skills/svif/SKILL.md` — installable Svif Project-orchestration Skill;
- `plugin/README.md` — installation/smoke-test and packaging guidance;
- `tests/test_plugin_package.py` — package/boundary regression tests.

This first increment is intentionally Skill-only so real usage can begin immediately. MCP/App packaging is now an enhancement path, not a prerequisite for starting Plugin testing and iteration.

The Plugin remains a distribution/workflow layer. It MUST NOT duplicate Orchestrator semantics, move canonical Project truth out of the Continuity Provider, or permit untrusted model/result payloads to self-grant protected authority.

Current ChatGPT Apps SDK / MCP work remains the concrete integration path for the founding ChatGPT Execution Surface and can later be packaged into the Plugin while preserving the dependency direction:

`Plugin / distribution -> Execution Surface integration -> Orchestrator -> Continuity + Capability Providers`

## Active contracts

- Svif product line: `0.2` development (`0.2.0-dev`).
- Project Binding: `project-binding/0.2`.
- Software Delivery profile: `software-delivery/0.2`.
- Capability Adapter: `capability-adapter/0.2`.
- Evidence record: `evidence-record/0.2`.
- Repository/filesystem binding serialization: `SVIF.yaml`.
- Plugin package format: Agent Plugins `1.0.0`.

## Executable product foundation

Implemented under Svif ownership:

- generic Orchestrator with synchronous and externally driven execution paths;
- Agnir repository/filesystem Continuity Provider;
- ChatGPT structured Execution Surface bridge;
- Cloudflare Workers Capability Provider with injected transport boundary;
- founding credential-free E2E scenario at `tests/test_founding_e2e.py`;
- Skill-first installable Plugin MVP at `plugin/`;
- runtime/provider/surface/Plugin tests and portable contract conformance.

The founding E2E proves the complete credential-free product loop through the real interfaces: Agnir continuity load -> `Orchestrator.begin()` -> ChatGPT context materialization/result parsing -> trusted authority at `Orchestrator.complete()` -> exact-subject Cloudflare actuation through injected fake transport -> independent observation -> Agnir checkpoint -> continuity reload/resume.

Cloudflare authority remains enforced outside untrusted model payloads. External actuation still requires successful verification for the exact subject plus required authority, and external success still requires independent observation before checkpoint.

Founding E2E success is not evidence of live Cloudflare production delivery; live delivery remains separately authorized and separately evidenced.

## Repository documentation baseline

The repository has parallel English and Simplified Chinese entry points: `README.md` and `README.zh-CN.md`.

Both READMEs contain a current Architecture Diagram, Runtime / Operation Flow diagram, current Plugin status, and compact plain-text repository tree. Localized Mermaid diagrams are comprehension-first rather than literal translations.

`REPOSITORY_TREE.md` is the exhaustive tracked-file map. Architecture/runtime/distribution changes update both README language versions; tracked file additions/removals/moves or material responsibility changes update `REPOSITORY_TREE.md` in the same change set, and both compact README trees when affected.

## Historical isolation boundary

ZeroLocal and other retired branch material exist only as lineage and audit history referenced by immutable commit SHA and `history/BRANCH_ARCHIVE.md`.

They MUST NOT become:

- active Svif runtime dependencies;
- current contract inputs;
- compatibility requirements for Svif `0.2`;
- conformance fixtures required for current architecture correctness;
- release gates for Svif or Agnir;
- a reason to reintroduce `.chatgpt/`, Skills-era, or standalone-reference-repository structure into active `main`.

Historical material MAY be consulted to understand lineage or recover an idea, but any idea that remains part of Svif must be independently accepted and stated in the current architecture/decisions. Current `main` is a greenfield architecture, not a compatibility-preserving continuation of ZeroLocal.

## Current implementation gap / resume point

1. **Install and use the Plugin MVP on real Project work**, treating failures and friction as direct inputs to Skill/packaging iteration.
2. **Add the remote ChatGPT MCP/App component** only when it reuses the existing `ChatGPTExecutionSurface` and `Orchestrator.begin()` / `complete()` lifecycle without duplicating kernel semantics or weakening the authority boundary.
3. **Add broader neutrality evidence** using Agnir's storage-neutral and multi-project isolation cases; prove Svif composition does not require GitHub, Cloudflare, or ChatGPT as universal kernel dependencies.
4. Bind Svif to the current Agnir Core compatibility line as a Continuity Provider contract, not to Agnir historical lineage or repository layout.
5. Keep live Cloudflare delivery disabled unless explicitly authorized; any future success claim requires exact verified-subject delivery plus independent observation.

## Evidence checkpoints

- README/localization: `.agnir/evidence/2026-08-28-readme-diagram-localization-checkpoint.md`.
- Founding E2E: `.agnir/evidence/2026-08-28-founding-e2e.md`, run `33143308949` success.
- Repository documentation baseline: pre-checkpoint head `97e70f9980de36aa7e3095cf8284f40c6fbf285e`, product-check run `33146795882` success.
- Main-only branch cleanup: `.agnir/evidence/2026-08-28-main-only-branch-cleanup-checkpoint.md`; verified cleanup baseline head `4ea2c138417fa365aac6d88a0154e693324640b2`, product-check run `33157419617` success.
- Retired branch tips: `history/BRANCH_ARCHIVE.md`.

## Branch governance

- `main` is the only long-lived branch and the only authoritative active Svif product line.
- All former legacy, feature, fix, and temporary branch refs are retired after their final tip SHAs are recorded in `history/BRANCH_ARCHIVE.md`.
- Historical recovery uses commit SHAs and Git history, not live branch refs.
