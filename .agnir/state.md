# Svif Current State

Svif is the authoritative active **Project orchestration product** on `main`. ZeroLocal v0.1 remains predecessor history on `legacy/zerolocal-v0.1`.

## Canonical repository topology

The active architecture has only two canonical projects/repositories:

- Svif: `iorLab/svif`;
- Agnir: `iorLab/agnir`.

The former `iorLab/svif-cloudflare-reference` project is retired. Cloudflare implementation, provider descriptors, fixtures, tests, and future E2E validation belong inside `iorLab/svif`. The old repository is historical evidence only until physically deleted and is not an active dependency.

## Product architecture

Svif coordinates four first-class components:

1. **Orchestrator** — `src/svif/runtime.py`;
2. **Continuity Provider** — founding implementation Agnir via `src/svif/continuity/agnir.py`;
3. **Execution Surface** — founding ChatGPT bridge via `src/svif/execution/chatgpt.py`;
4. **Capability Provider** — founding Cloudflare Workers provider via `src/svif/capabilities/cloudflare.py`.

Stable rule:

> The Project persists; Executors and execution environments may change.

No execution environment becomes authoritative merely because execution occurred there.

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

The founding E2E now proves the complete credential-free product loop through the real interfaces: Agnir continuity load -> `Orchestrator.begin()` -> ChatGPT context materialization/result parsing -> trusted authority at `Orchestrator.complete()` -> exact-subject Cloudflare actuation through injected fake transport -> independent observation -> Agnir checkpoint -> continuity reload/resume.

Cloudflare authority remains enforced outside untrusted model payloads. External actuation still requires successful verification for the exact subject plus required authority, and external success still requires independent observation before checkpoint.

The Cloudflare provider transport intentionally does not embed credentials or freeze GitHub Actions/Wrangler as product dependencies. Founding E2E success is not evidence of live Cloudflare production delivery; live delivery remains separately authorized and separately evidenced.

## README architecture documentation

The repository has parallel English and Simplified Chinese entry points: `README.md` and `README.zh-CN.md`.

Both READMEs MUST contain:

- an **Architecture Diagram** showing the current component/binding topology;
- a **Runtime / Operation Flow** diagram showing the current orchestration loop.

Architecture, component ownership, dependency direction, authority/provenance boundaries, or runtime-flow changes require the affected diagrams in both language versions to be updated in the same change set. Repository integrity checks enforce the presence of both localized READMEs and both Mermaid diagram classes without treating prose as a byte-for-byte contract.

Localized diagrams are **comprehension-first, not literal translations**. In the Simplified Chinese README, important diagram nodes must be understandable to a Chinese reader without requiring prior understanding of the English technical term: nodes should communicate both the role and its responsibility, while English terms may remain as secondary labels where useful.

## Historical Cloudflare evidence

The retired standalone reference supplied useful migration evidence but no live success claim. Preserved details are in `history/CLOUDFLARE_REFERENCE.md`.

No active Svif code, test, release, Project binding, or next action may depend on the retired repository.

## Validation Project #2

`mattamior/cloud-mail@svif/cloudflare-validation` remains a non-founding external Project validation case. Credential-free static verification is proven for immutable candidate `5b32462f3725327805f0dd696475a16f07b666aa` by run `33102032043`; protected delivery was skipped. Production `main` remains outside that validation mutation boundary.

## Current implementation gap

The founding product path is executable. The next phase is integration/package hardening rather than more architecture splitting:

1. harden the concrete ChatGPT app/MCP packaging around the existing externally driven bridge;
2. add broader non-founding neutrality evidence;
3. add multi-project isolation evidence aligned with Agnir once its fixture is ready;
4. freeze exact Agnir compatibility/release expression when Agnir `0.1` criteria are concrete.

Live Cloudflare delivery remains disabled unless explicitly authorized.

## 2026-08-28 README/localization checkpoint

README architecture documentation and localization policy are durable project state.

- Simplified Chinese diagram clarification commit: `5460bc388a638ce4dff8e5d8fe12d467c687a54a`.
- Localization-policy decision commit: `a8fcd4e76d502f57bc9e751e9763eddf3530a001`.
- Product-check run `33142755892`: success.
- Durable evidence: `.agnir/evidence/2026-08-28-readme-diagram-localization-checkpoint.md`.

## 2026-08-28 founding E2E advance

- Founding E2E implementation commit: `92bf66e39e7105a7db67a79da88c7e9e53398659`.
- Final bilingual/documented founding-path head: `b4ae14cc50457d6479cbdf8c2d5bef745d59dad2`.
- Product-check run `33143308949`: success across repository-integrity, runtime-kernel, and portable-contracts.
- Durable evidence: `.agnir/evidence/2026-08-28-founding-e2e.md`.
- Resume point: concrete ChatGPT app/MCP packaging hardening, while Agnir protocol work continues independently on discovery/conformance pressure.

## Branch governance

- `main`: authoritative active Svif product line;
- `legacy/zerolocal-v0.1`: predecessor history;
- incidental branch cleanup remains deferred until the new version is substantially complete.
