# Svif Next Actions

## After Agnir Core 0.2 real-consumer validation

1. **Feed the completed Svif evidence into Agnir.** Record the exact common baseline, source/target revisions, staged candidate, reconciled two-parent target, post-publication verification repair, CI runs, and independent source fresh-resume in `iorLab/agnir` on `feature/core-0.2-lineage`.
2. **Reassess Agnir Core `0.2` release readiness.** The next protocol work should focus on safe integration of Agnir PR `#4` / `#5` into Agnir `main`, migration/release documentation, and `v0.2.0-rc.1` preparation rather than adding more synthetic lineage models unless the real evidence exposes a missing invariant.
3. **Do not ordinary-merge the experimental Svif PRs.** Source PR `#4` has been integrated into the temporary target through the Agnir-aware two-parent path and may be closed as completed-via-reconciliation once evidence is recorded. Target PR `#3` remains draft; authoritative Svif `main` adoption of Agnir Core `0.2` is a separate decision after Agnir publishes/accepts the compatibility line.
4. **Keep `v0.2.0-preview.1` immutable.** Preserve the released Preview's **immutable candidate** provenance and its real **Codex CLI** plus **ChatGPT desktop/Codex** acceptance evidence. Any Preview fix uses a new tag such as `v0.2.0-preview.2` rather than moving the released tag.
5. **Continue the separate public/personal ChatGPT path when the publisher gate is resolvable.** Submit the supported Skills-only package to the **universal Plugins Directory**, explicitly Publish after approval, then validate a real **individual-user ChatGPT surface**, with **ChatGPT Web** remaining a first-class target.
6. Keep live Cloudflare delivery disabled unless explicitly authorized.

## Completed Agnir Core 0.2 validation receipts

- Project: `urn:svif:project:svif-core`.
- Target lineage: `urn:svif:lineage:agnir-core-0.2-validation`.
- Target selector: `refs/heads/feature/agnir-core-0.2-validation`.
- Source lineage: `urn:svif:lineage:agnir-core-0.2-parallel`.
- Source selector: `refs/heads/feature/agnir-core-0.2-parallel`.
- Common baseline: `329984f94483a7cbbb21a6faa42b9cf9ed84fed2`.
- Target pre-integration: `79c5b7c7ee2ed545492702bea43d0f7135602f35`; CI `33619053159` success.
- Source: `d2d0c1bf25526b54490cce14c5aa8797c85c4d54`; CI `33618885830` success.
- Staged candidate: `4b86b3adafe08cc2f7fd48eb4f685d2b633b25c3`; never published as target truth.
- Reconciled two-parent target: `1cd25539c75f8a2a32c84b822c0db80b176fd319`.
- Initial post-publication verification: `33619306602`; only one brittle workflow-heading assertion failed.
- Semantic self-host repair: `e48ae07faa6a716f7e2cd83cdcefdce6d02d8c7e`; CI `33619491154` 3/3 success.
- Agnir experimental source revision used by Svif: `414dba1e50ad1bdcae3ca91d19c6768fdaa030cc`.

## Invariants confirmed by the real Project

- The Project persists while multiple Continuity Lineages advance independently.
- Project identity is not lineage identity; lineage identity is not selector or revision receipt.
- Selection is explicit/binding-driven and never guessed by sibling scanning.
- Checkpoints are lineage-local by default.
- Source continuity is reconciliation input, not automatic target truth.
- A staged integration candidate can exist while the target ref remains unchanged.
- Target continuity can be reconciled before target publication.
- Target ref advancement is the publication boundary and can publish integrated Project + reconciled target truth coherently.
- Source continuity remains independently resumable after target integration.
- Svif Orchestrator remains Continuity-Provider-neutral; lineage mechanics remain at the provider/binding boundary.
- The released Skills-only first-use bootstrap remains on its published Agnir Core/profile `0.1` baseline until an intentional distribution release changes it.
- `main` is the only long-lived authoritative Svif branch; validation branches are temporary evidence carriers.
