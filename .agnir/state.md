# Svif Current State

Svif remains the authoritative active **Project orchestration product** in `iorLab/svif`; `main` remains the only long-lived authoritative branch. Agnir remains the founding **Continuity Provider**, ChatGPT a founding **Execution Surface**, and Cloudflare a founding **Capability Provider**. The former `iorLab/svif-cloudflare-reference` project is retired and historical only.

## Active source lineage — 2026-09-02

Temporary branch `feature/agnir-core-0.2-parallel` is the second real Svif Continuity Lineage in the Agnir Core `0.2` validation. It was forked from coherent checkpoint `329984f94483a7cbbb21a6faa42b9cf9ed84fed2`.

Project identity remains `urn:svif:project:svif-core`. This branch has a distinct logical lineage `urn:svif:lineage:agnir-core-0.2-parallel`, bound to `refs/heads/feature/agnir-core-0.2-parallel`. The target validation lineage remains `urn:svif:lineage:agnir-core-0.2-validation` on `refs/heads/feature/agnir-core-0.2-validation` and is not mutated by this checkpoint.

The fork preserves inherited durable memory as baseline but now advances independently. A real Svif contract change in `spec/PROJECT_BINDING.md` clarifies that provider-local parallel continuity may expose multiple independently advancing provider contexts for one stable Svif Project identity, while lineage and selector semantics remain provider-specific and outside the provider-neutral Orchestrator kernel.

## Validation evidence

The migrated target baseline passed Svif product CI in run `33616508143`; the coherent target-lineage self-host checkpoint passed run `33616750662`. This source checkpoint must independently pass repository-integrity, portable-contracts, runtime-kernel, and fresh Core `0.2` self-host discovery before it is accepted as source-lineage evidence.

The self-host test is now selector/lineage-binding-driven rather than hard-coding the target branch. It reads the current `SVIF.yaml` binding, uses that selector to invoke the real Agnir provider, and verifies that the resolved logical lineage matches the binding. This allows the same Project test to validate different lineages without treating any one lineage as Project identity.

## Product/distribution state preserved

The Plugin MVP remains active. `README.md` and `README.zh-CN.md` remain synchronized entry points. Released `v0.2.0-preview.1` remains immutable with prior Codex CLI and ChatGPT desktop/Codex acceptance evidence. The separate public/personal ChatGPT Web / universal Plugins Directory path remains active work. Live Cloudflare delivery remains disabled unless explicitly authorized.

## Remaining experiment

After this source checkpoint is green, the target lineage must advance independently. Then source→target integration must be staged without moving the target ref, target continuity must be reconciled against the actual integrated Project result and both lineages' relevant truth/evidence, and the target may advance only in the coherent integrated revision. Fresh resume must then recover both source and integrated target correctly.

`.agnir/next-actions.md` is the ordered resume plan. `.agnir/decisions.md` remains authoritative for durable Svif architecture and distribution decisions.
