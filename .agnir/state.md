# Svif Current State

Svif remains the authoritative active **Project orchestration product** in `iorLab/svif`; `main` remains the only long-lived authoritative branch. Agnir remains the founding **Continuity Provider**, ChatGPT a founding **Execution Surface**, and Cloudflare a founding **Capability Provider**. The former `iorLab/svif-cloudflare-reference` project is retired and historical only.

## Reconciled Core 0.2 target lineage — 2026-09-02

Temporary target `feature/agnir-core-0.2-validation` remains Project `urn:svif:project:svif-core`, logical lineage `urn:svif:lineage:agnir-core-0.2-validation`, selector `refs/heads/feature/agnir-core-0.2-validation`.

The real two-lineage experiment reached independent green checkpoints:

- target pre-integration revision: `79c5b7c7ee2ed545492702bea43d0f7135602f35`, CI run `33619053159` 3/3 success;
- source revision: `d2d0c1bf25526b54490cce14c5aa8797c85c4d54`, CI run `33618885830` 3/3 success;
- staged two-parent candidate: `4b86b3adafe08cc2f7fd48eb4f685d2b633b25c3`.

The staged candidate was created without advancing the target ref. A fresh ref check after candidate construction still observed target `79c5b7c7...` and source `d2d0c1bf...`, proving the integration candidate existed while the authoritative target remained unchanged.

## Integrated Project result

The reconciled target contains both independently developed Project changes:

1. target `ARCHITECTURE.md`: the generic Svif Orchestrator consumes an already selected Continuity Context and must not enumerate/guess sibling provider contexts or infer Project identity from provider lineage/selector/revision metadata;
2. source `spec/PROJECT_BINDING.md`: one stable Svif Project may use multiple independently advancing provider-local continuity contexts, with lineage/selector semantics remaining provider-specific;
3. source test hardening: self-host and Plugin binding tests are now binding-driven rather than hard-coding one target lineage/selector.

The target `AGNIR.yaml` / `SVIF.yaml` remain target-bound. Source logical lineage and source selector are preserved as source evidence, not copied into target truth.

## Reconciliation result

Target continuity is reconciled from the actual integrated Project candidate, previous target truth, relevant source continuity/evidence, and the authorized experiment intent. The source lineage remains independently resumable at `feature/agnir-core-0.2-parallel` and is not collapsed into the target lineage.

The source evidence file is retained as historical/reconciliation input. The final integration evidence records the staged candidate, both parent revisions, ref-stability check, and publication boundary.

## Product/distribution state preserved

The Plugin MVP remains active. `README.md` and `README.zh-CN.md` remain synchronized entry points. Released `v0.2.0-preview.1` remains immutable with prior Codex CLI and ChatGPT desktop/Codex acceptance evidence. The public/personal ChatGPT Web / universal Plugins Directory path remains separate active work. Live Cloudflare delivery remains disabled unless explicitly authorized.

## Remaining verification

After the reconciled two-parent revision is published to the temporary target ref, run full Svif product CI and fresh target self-host discovery. Then verify the source ref still resolves the source lineage independently. If both pass, feed the completed real-consumer evidence back into Agnir Core `0.2` release readiness. No Svif `main` adoption or Agnir `main` integration is implied by this temporary-lineage success.
