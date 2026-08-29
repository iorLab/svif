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

Svif has an active **Plugin MVP** under `plugin/`, with a portable Agent Plugins `1.0.0` package plus additive OpenAI/Codex repository distribution metadata.

Current package, distribution, and conformance surfaces include:

- `plugin/plugin.json` — portable Agent Plugins 1.0 manifest;
- `plugin/.codex-plugin/plugin.json` — OpenAI/Codex product-specific manifest that reuses the same `skills/` and does not shadow runtime;
- `.agents/plugins/marketplace.json` — repository-backed OpenAI/Codex GitHub marketplace catalog mapping to local `./plugin`;
- `plugin/skills/svif/SKILL.md` — installable Svif Project-orchestration Skill;
- `plugin/README.md` — portable/package/distribution guidance plus explicit Agnir pre-load discovery, GitHub marketplace, and client-installation evidence boundaries;
- `tests/test_plugin_package.py` — portable manifest, Agent Skills frontmatter, filesystem-containment/failure-isolation, Agnir activation, and runtime-shadowing regression tests;
- `tests/test_plugin_component_discovery.py` — fixed component locations, immediate-child Skill discovery, and MCP component-isolation regression tests;
- `tests/test_plugin_installation_docs.py` — documentation guardrails that prevent portable package/conformance/distribution validation from being presented as ChatGPT/Codex client installation evidence;
- `tests/test_plugin_agnir_discovery.py` — guards the Agnir repository/filesystem discovery order: Core/profile compatibility and selected-Project identity must validate before continuity locators are resolved/loaded, with unsupported-version and Project-mismatch failures surfaced rather than fallback search;
- `tests/test_plugin_openai_distribution.py` — guards the marketplace source mapping, Codex manifest reuse of the shared Skill, and identity metadata parity with the portable manifest.

`SVIF.yaml` registers all five Plugin validation test surfaces plus the portable manifest, Codex manifest, and OpenAI marketplace catalog. Distribution metadata is additive: portable `plugin/plugin.json` remains the Agent Plugins contract, while OpenAI/Codex-specific files exist only to make the same Plugin root consumable through current product-supported repository import flows.

This first increment is intentionally Skill-only. Missing `mcp.json` is valid for the portable package; MCP/App packaging remains an additive enhancement rather than a prerequisite for beginning Plugin testing and iteration.

Repository CI proves package/conformance, Agnir discovery guardrails, distribution metadata consistency, installation-documentation boundaries, and product-boundary properties only. **No supported ChatGPT/Codex client or workspace installation has yet been recorded as validated evidence**, including the new GitHub marketplace route. A real marketplace import report plus subsequent invocation of the exact revision is still required.

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
- Portable Plugin package format: Agent Plugins `1.0.0`.
- OpenAI/Codex repository distribution path: `.agents/plugins/marketplace.json` -> local `./plugin` -> `.codex-plugin/plugin.json` + shared `skills/`.
- Agnir Core compatibility: `0.1` with `repository-filesystem/0.1` as the current profile binding.

## Executable product foundation

Implemented under Svif ownership:

- generic Orchestrator with synchronous and externally driven execution paths;
- Agnir repository/filesystem Continuity Provider;
- ChatGPT structured Execution Surface bridge;
- Cloudflare Workers Capability Provider with injected transport boundary;
- founding credential-free E2E scenario at `tests/test_founding_e2e.py`;
- Skill-first portable Plugin MVP at `plugin/`;
- OpenAI/Codex GitHub marketplace distribution metadata that points at the same Plugin/Skill implementation;
- Plugin package, fixed-component discovery, Agnir pre-load discovery, installation-documentation, and OpenAI distribution tests;
- runtime/provider/surface tests and portable contract conformance.

The founding E2E proves the complete credential-free product loop through the real interfaces: Agnir continuity load -> `Orchestrator.begin()` -> ChatGPT context materialization/result parsing -> trusted authority at `Orchestrator.complete()` -> exact-subject Cloudflare actuation through injected fake transport -> independent observation -> Agnir checkpoint -> continuity reload/resume.

Cloudflare authority remains enforced outside untrusted model payloads. External actuation still requires successful verification for the exact subject plus required authority, and external success still requires independent observation before checkpoint.

Founding E2E success is not evidence of live Cloudflare production delivery; live delivery remains separately authorized and separately evidenced.

## Repository documentation baseline

The repository has parallel English and Simplified Chinese entry points: `README.md` and `README.zh-CN.md`.

Both READMEs contain a current Architecture Diagram, Runtime / Operation Flow diagram, current Plugin status including the OpenAI GitHub marketplace path, Agnir Project Instructions, and compact plain-text repository tree. Localized Mermaid diagrams are comprehension-first rather than literal translations.

The active Agnir activation route is:

`Project root -> AGENTS.md -> README.md / Agnir Project Instructions -> AGNIR.yaml -> declared durable memory`

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

1. **Perform the first real supported OpenAI workspace/client installation through the GitHub marketplace path.** Import `https://github.com/iorLab/svif`, record or pin the exact revision, capture the marketplace import result, invoke `svif`, and record the exact client/surface, Agnir activation/discovery path, compatibility/profile/Project-identity checks, verification performed, observed failures/friction, and resulting durable checkpoint. Package/conformance/distribution CI and documentation guardrails are not installation evidence.
2. **Repair Plugin workflow or distribution friction from that real exercise.** Avoid speculative complexity now that manifest, Skill frontmatter, filesystem containment/failure isolation, fixed-component discovery, Agnir activation plus pre-load compatibility/identity validation, client-installation claim boundaries, and repository-backed OpenAI distribution metadata are covered.
3. **Add the remote ChatGPT MCP/App component** only when it reuses the existing `ChatGPTExecutionSurface` and `Orchestrator.begin()` / `complete()` lifecycle without duplicating kernel semantics or weakening the authority boundary.
4. **Add broader neutrality evidence** using Agnir's storage-neutral and multi-project isolation cases; prove Svif composition does not require GitHub, Cloudflare, or ChatGPT as universal kernel dependencies.
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
