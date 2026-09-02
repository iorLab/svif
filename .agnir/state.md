# Svif Current State

Svif remains the authoritative active **Project orchestration product** in `iorLab/svif`; `main` remains the only long-lived authoritative branch. Agnir remains the independent founding **Continuity Provider**; ChatGPT remains a founding **Execution Surface**; Cloudflare remains a founding **Capability Provider**. The former `iorLab/svif-cloudflare-reference` project is retired and historical only.

## Active Core 0.2 real-consumer validation — 2026-09-02

Temporary branch `feature/agnir-core-0.2-validation` is now the first real Svif Project consumer of the Agnir Core `0.2` / `repository-filesystem/0.2` candidate. This branch is experimental and does not change authoritative `main` or released `v0.2.0-preview.1`.

Project identity remains `urn:svif:project:svif-core`. The selected logical lineage is `urn:svif:lineage:agnir-core-0.2-validation`, bound to VCS selector `refs/heads/feature/agnir-core-0.2-validation`. Existing `.agnir/state.md`, `.agnir/next-actions.md`, `.agnir/decisions.md`, and `.agnir/evidence/` locations were preserved through migration.

Agnir experimental source revision `414dba1e50ad1bdcae3ca91d19c6768fdaa030cc` is recorded as validation provenance only; it is not a published stable Agnir release.

## First real-consumer CI baseline passed

Svif Draft PR `#3` (`Validate Svif against Agnir Core 0.2 lineages`) exercises this validation branch against real repository checks.

Initial run `33615826969` produced useful pressure:

- portable-contracts passed;
- the new Agnir `0.2` adapter cases themselves passed in runtime-kernel;
- repository-integrity and three legacy tests failed because they hard-coded current Project compatibility as Agnir `0.1` or because the first branch-local Next Actions rewrite dropped still-valid Preview/public-distribution work.

Those regressions were repaired without weakening unrelated gates. The repository integrity checker now validates the **coherence of the currently selected Agnir/Svif binding** and accepts only supported `0.1` or `0.2` Core/profile pairs. For Core `0.2`, it additionally requires matching logical lineage and VCS selector binding and rejects selector==lineage identity. Legacy distribution tests now distinguish the current migrated Project binding from the released Skill's still-published `0.1` first-use bootstrap baseline. Existing Preview/Codex/public ChatGPT next actions were restored rather than discarded.

Follow-up run **`33616508143` completed successfully**:

- `repository-integrity`: success;
- `portable-contracts`: success;
- `runtime-kernel`: success.

This establishes a coherent migrated Svif Core `0.2` consumer baseline while preserving the released `0.1` bootstrap path and unrelated product gates.

## Real selected-lineage fresh discovery

`tests/test_agnir_core_0_2_self_host.py` now loads the actual Svif repository root through `AgnirFilesystemContinuityProvider` with explicit Core/profile `0.2` and selector context. It verifies:

- Project identity `urn:svif:project:svif-core`;
- logical lineage `urn:svif:lineage:agnir-core-0.2-validation`;
- selector binding `refs/heads/feature/agnir-core-0.2-validation` through provider discovery;
- recovery of real branch-local State / Next Actions / Evidence.

This checkpoint records the first coherent target-lineage baseline from which the second Svif lineage will be forked.

## Adapter boundary proven so far

The real Svif Agnir Continuity Provider now:

- retains Core/profile `0.1` support;
- accepts experimental Core/profile `0.2` only with coherent logical lineage semantics;
- treats VCS selector/binding as distinct from logical lineage identity;
- rejects selected selector absence/mismatch rather than guessing;
- records the resolved Agnir lineage in runtime checkpoint evidence;
- leaves the generic Svif Orchestrator Continuity-Provider-neutral.

## Released product/distribution state preserved

The Plugin MVP remains active under `plugin/`. `README.md` and `README.zh-CN.md` remain synchronized user entry points. Released `v0.2.0-preview.1` remains immutable, with prior Codex CLI and ChatGPT desktop/Codex acceptance evidence unchanged. The public/personal ChatGPT Web / universal Plugins Directory path remains separate work. Live Cloudflare delivery remains disabled unless explicitly authorized.

## Remaining validation boundary

Core `0.2` real-Project validation is **not complete yet**. Next required evidence:

1. this checkpoint's fresh self-host test passes in CI;
2. fork a second temporary Svif branch from this coherent checkpoint with the same Project identity but a new logical lineage identity and selector binding;
3. advance both lineages independently and fresh-resolve different Current State / Next Actions;
4. stage source→target integration without advancing the target ref while unreconciled;
5. reconcile target continuity from actual Project result + previous target truth + relevant source continuity/Evidence;
6. publish integrated Project + target checkpoint coherently;
7. fresh-resolve both target and source after integration;
8. feed the completed real-consumer evidence back into Agnir Core `0.2` release readiness.

`.agnir/decisions.md` remains authoritative for established Svif architecture/distribution decisions; `.agnir/next-actions.md` is the resume order for the active validation and still-valid distribution work.
