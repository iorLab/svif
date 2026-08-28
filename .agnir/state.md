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
- runtime/provider/surface tests and portable contract conformance.

Cloudflare authority remains enforced outside untrusted model payloads. External actuation still requires successful verification for the exact subject plus required authority, and external success still requires independent observation before checkpoint.

The Cloudflare provider transport intentionally does not embed credentials or freeze GitHub Actions/Wrangler as product dependencies.

## Historical Cloudflare evidence

The retired standalone reference supplied useful migration evidence but no live success claim. Preserved details are in `history/CLOUDFLARE_REFERENCE.md`.

No active Svif code, test, release, Project binding, or next action may depend on the retired repository.

## Validation Project #2

`mattamior/cloud-mail@svif/cloudflare-validation` remains a non-founding external Project validation case. Credential-free static verification is proven for immutable candidate `5b32462f3725327805f0dd696475a16f07b666aa` by run `33102032043`; protected delivery was skipped. Production `main` remains outside that validation mutation boundary.

## Current implementation gap

The product structure is now consolidated. The next phase is execution rather than more repository splitting:

1. build one in-repository founding E2E composition across Agnir + ChatGPT + Cloudflare;
2. harden concrete ChatGPT app/MCP packaging around the existing bridge;
3. add broader non-founding neutrality and multi-project isolation evidence;
4. freeze exact Agnir compatibility/release expression when Agnir `0.1` criteria are concrete.

Live Cloudflare delivery remains disabled unless explicitly authorized.

## Branch governance

- `main`: authoritative active Svif product line;
- `legacy/zerolocal-v0.1`: predecessor history;
- incidental branch cleanup remains deferred until the new version is substantially complete.
