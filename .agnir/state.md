# Svif Current State

Svif remains the authoritative active **Project orchestration product** in `iorLab/svif`; `main` remains the only long-lived authoritative branch. Agnir remains the founding **Continuity Provider**, ChatGPT a founding **Execution Surface**, and Cloudflare a founding **Capability Provider**. The former `iorLab/svif-cloudflare-reference` project is retired and historical only.

## Agnir Core 0.2 real-consumer validation complete — 2026-09-02

Temporary target branch `feature/agnir-core-0.2-validation` has completed the first real Svif consumer validation of Agnir Core `0.2` / `repository-filesystem/0.2` parallel continuity.

Project identity remained `urn:svif:project:svif-core` throughout. Target logical lineage remains `urn:svif:lineage:agnir-core-0.2-validation` bound to `refs/heads/feature/agnir-core-0.2-validation`. Source logical lineage remains independently available as `urn:svif:lineage:agnir-core-0.2-parallel` on `refs/heads/feature/agnir-core-0.2-parallel`.

### Real two-lineage receipts

- common coherent baseline: `329984f94483a7cbbb21a6faa42b9cf9ed84fed2`;
- independently advanced target: `79c5b7c7ee2ed545492702bea43d0f7135602f35`, CI `33619053159` 3/3 success;
- independently advanced source: `d2d0c1bf25526b54490cce14c5aa8797c85c4d54`, CI `33618885830` 3/3 success;
- unpublished staged two-parent candidate: `4b86b3adafe08cc2f7fd48eb4f685d2b633b25c3`;
- reconciled two-parent target revision: `1cd25539c75f8a2a32c84b822c0db80b176fd319`;
- post-publication semantic self-host test repair: `e48ae07faa6a716f7e2cd83cdcefdce6d02d8c7e`, CI `33619491154` 3/3 success.

The staged candidate existed while fresh ref reads still showed target at `79c5b7c7...` and source at `d2d0c1bf...`. The target ref then advanced exactly once from `79c5b7c7...` to reconciled two-parent revision `1cd25539...`; staged candidate `4b86b3ad...` was never authoritative target truth.

The first post-publication run `33619306602` had repository-integrity and portable-contracts green but one brittle self-host assertion expected an old workflow-stage heading. All actual Core `0.2` discovery and lineage checks passed. Commit `e48ae07...` replaced that heading check with binding-driven semantic assertions; run `33619491154` then passed repository-integrity, portable-contracts, and runtime-kernel.

### Integrated real Project result

The target now contains both independently developed Project changes:

1. `ARCHITECTURE.md` states that the generic Svif Orchestrator consumes an already selected Continuity Context and must not enumerate/guess sibling provider contexts or infer Project identity from provider-local lineage/selector/revision metadata;
2. `spec/PROJECT_BINDING.md` states that one stable Svif Project may use multiple independently advancing provider-local continuity contexts while lineage/selector semantics remain provider-specific;
3. self-host and Plugin binding tests are binding-driven rather than hard-coding one lineage/selector.

Target `AGNIR.yaml` / `SVIF.yaml` remain target-bound. Source continuity is reconciliation evidence/input, not target truth.

### Independent source fresh resume

After target integration and target repair, a fresh read still observed source ref `feature/agnir-core-0.2-parallel` at `d2d0c1bf25526b54490cce14c5aa8797c85c4d54`. Its `AGNIR.yaml` still resolves Project `urn:svif:project:svif-core`, lineage `urn:svif:lineage:agnir-core-0.2-parallel`, and selector `refs/heads/feature/agnir-core-0.2-parallel`; its source-local State remains intact. Target publication did not rewrite or collapse source continuity.

## Conclusion

The real Svif consumer experiment validates migration, explicit lineage binding, independent divergence, lineage-local checkpoints, binding-driven fresh resume, staged integration without target publication, target reconciliation, coherent target advancement, and independent source survival on a real Project.

This success does **not** migrate Svif authoritative `main` or publish Agnir Core `0.2` stable. Svif `main` and released `v0.2.0-preview.1` remain unchanged. The result should now be fed back into Agnir `feature/core-0.2-lineage` as release-readiness evidence.

## Product/distribution state preserved

The Plugin MVP remains active. `README.md` and `README.zh-CN.md` remain synchronized entry points. Released `v0.2.0-preview.1` remains immutable with prior Codex CLI and ChatGPT desktop/Codex acceptance evidence. The public/personal ChatGPT Web / universal Plugins Directory path remains separate active work. Live Cloudflare delivery remains disabled unless explicitly authorized.

`.agnir/next-actions.md` is the canonical resume order; `.agnir/decisions.md` remains authoritative for durable architecture and distribution decisions.
