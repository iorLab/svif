# Svif Current State

Svif remains the authoritative active **Project orchestration product** in `iorLab/svif`; `main` remains the only long-lived authoritative branch. Agnir remains the founding **Continuity Provider**, ChatGPT a founding **Execution Surface**, and Cloudflare a founding **Capability Provider**. The former `iorLab/svif-cloudflare-reference` project is retired and historical only.

## Active target lineage — 2026-09-02

Temporary branch `feature/agnir-core-0.2-validation` remains the target lineage for the real Agnir Core `0.2` consumer experiment. Project identity remains `urn:svif:project:svif-core`; logical lineage remains `urn:svif:lineage:agnir-core-0.2-validation`; selector remains `refs/heads/feature/agnir-core-0.2-validation`.

This target lineage has now advanced independently from common checkpoint `329984f94483a7cbbb21a6faa42b9cf9ed84fed2`. Its target-only real Project change updates `ARCHITECTURE.md` to state that the generic Svif Orchestrator consumes an already selected Continuity Context and must not enumerate/guess sibling provider contexts or infer Project identity from provider lineage/selector/revision metadata.

The source lineage is separate: `urn:svif:lineage:agnir-core-0.2-parallel` on `refs/heads/feature/agnir-core-0.2-parallel`. Its `PROJECT_BINDING` contract change and source-local continuity are not copied into target truth before integration.

## Validation evidence

The migrated target baseline passed run `33616508143`; the coherent target self-host checkpoint passed run `33616750662`. Source-lineage CI exposed and then removed remaining tests that treated the target selector as a Project constant; those tests are being made binding-driven on the source branch before integration.

This target checkpoint must pass repository-integrity, portable-contracts, runtime-kernel, and fresh target self-host discovery before staged integration begins.

## Product/distribution state preserved

The Plugin MVP remains active; `README.md` and `README.zh-CN.md` remain synchronized entry points. Released `v0.2.0-preview.1` remains immutable with prior Codex CLI and ChatGPT desktop/Codex acceptance evidence. The public/personal ChatGPT Web / universal Plugins Directory path remains separate active work. Live Cloudflare delivery remains disabled unless explicitly authorized.

## Next boundary

After both target and source are independently green, capture both revisions and continuity. Build the integrated Project candidate without moving the target ref. Reconcile target continuity from the actual integrated result, previous target truth, relevant source continuity/evidence, and Principal intent. Only then publish the integrated Project + reconciled target continuity in the same target-advancing revision and fresh-resolve both lineages.

`.agnir/next-actions.md` is the active resume order; `.agnir/decisions.md` remains authoritative for durable architecture and distribution decisions.
