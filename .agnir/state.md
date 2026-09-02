# Svif Current State

Svif remains the authoritative active **Project orchestration product** in `iorLab/svif`; `main` remains the only long-lived authoritative branch. Agnir remains the independent founding Continuity Provider. The former `iorLab/svif-cloudflare-reference` project is retired and historical only.

## Active real-consumer validation — 2026-09-02

A temporary branch `feature/agnir-core-0.2-validation` is validating Svif as the first real consumer of Agnir Core `0.2` / `repository-filesystem/0.2`. This branch is experimental and does not change the released `v0.2.0-preview.1` contract on `main`.

The Project identity remains `urn:svif:project:svif-core`. The branch explicitly migrates its Agnir discovery from Core/profile `0.1` to `0.2` and establishes logical lineage `urn:svif:lineage:agnir-core-0.2-validation`, bound to selector `refs/heads/feature/agnir-core-0.2-validation`.

The migration preserves the existing `.agnir/state.md`, `.agnir/next-actions.md`, `.agnir/decisions.md`, and `.agnir/evidence/` locators. Agnir development source revision `414dba1e50ad1bdcae3ca91d19c6768fdaa030cc` is used only as explicit experimental migration provenance; it is not a published stable Agnir release.

## Product architecture

Svif continues to coordinate four first-class components:

1. **Orchestrator** — `src/svif/runtime.py`;
2. **Continuity Provider** — founding Agnir implementation at `src/svif/continuity/agnir.py`;
3. **Execution Surface** — founding ChatGPT bridge at `src/svif/execution/chatgpt.py`;
4. **Capability Provider** — founding Cloudflare Workers provider at `src/svif/capabilities/cloudflare.py`.

Stable rule: the Project persists; Executors and execution environments may change. No Execution Surface becomes canonical Project truth merely because execution occurred there.

## Agnir adapter validation change

The Svif Agnir adapter is being generalized without changing the Svif Orchestrator contract:

- published Core/profile `0.1` remains supported;
- experimental Core/profile `0.2` is accepted only when its profile, logical lineage, and optional selected VCS binding resolve coherently;
- `continuity.lineage` is treated as logical Agnir lineage identity;
- a VCS ref/worktree selector is backend binding context, not lineage identity;
- selector mismatch surfaces Agnir binding failure instead of silently falling back;
- Svif runtime checkpoint evidence records the resolved Agnir lineage when present.

`SVIF.yaml` on this validation branch explicitly constrains the Continuity Provider to Core `0.2` / `repository-filesystem/0.2` and repeats the selected lineage/selector as provider-specific binding configuration. `AGNIR.yaml` remains the provider-owned durable discovery authority.

## Released Preview remains unchanged

Svif `v0.2.0-preview.1` remains the released Repository Preview from authoritative `main`. Its immutable tag/release and prior Codex/ChatGPT desktop acceptance evidence are unaffected by this experiment.

The Plugin MVP remains active under `plugin/`, `README.md` and `README.zh-CN.md` remain the synchronized user entry points, and live Cloudflare delivery remains disabled unless explicitly authorized.

## Validation boundary

This branch must not be merged to `main` merely because the initial adapter/migration tests pass. The real validation is incomplete until:

1. fresh Svif discovery/checkpoint succeeds on the migrated Core `0.2` lineage;
2. a second temporary Svif branch is explicitly forked into a distinct logical lineage with the same Project identity;
3. both lineages checkpoint independently and fresh-resume to different continuity;
4. a staged source→target integration keeps the target ref unchanged while unreconciled;
5. target continuity is reconciled and published coherently with the integrated Project result;
6. fresh target/source resume succeeds afterward;
7. evidence is recorded in both Svif and Agnir.

`.agnir/decisions.md` remains authoritative for established Svif architecture/distribution decisions; `.agnir/next-actions.md` is the ordered plan for this validation branch.
