# Svif Next Actions

## Active Agnir Core 0.2 real-consumer validation

1. **Make the migrated validation branch pass Svif product CI without weakening unrelated product gates.** Confirm repository-integrity, portable-contracts, and runtime-kernel behavior with Agnir Core/profile `0.2` selected in `SVIF.yaml` / `AGNIR.yaml`. Preserve legacy adapter and released Skill coverage for Core/profile `0.1`.
2. **Fresh-resolve and checkpoint the selected validation lineage.** The branch must resolve Project `urn:svif:project:svif-core`, logical lineage `urn:svif:lineage:agnir-core-0.2-validation`, and selector binding `refs/heads/feature/agnir-core-0.2-validation`; a checkpoint must preserve lineage/binding and record lineage-aware runtime evidence.
3. **Create a second temporary Svif lineage branch only after the migrated baseline is green.** Fork from the coherent validation checkpoint, assign a new logical lineage identity, bind its selector explicitly, preserve the same Project identity and inherited baseline, then advance it independently.
4. **Advance the target validation lineage independently as well.** Prove the two branches fresh-resume to different Current State / Next Actions while remaining one Project.
5. **Perform a staged source→target integration.** Do not advance the target ref while continuity is unreconciled. Reconcile actual integrated Project result + previous target truth + relevant source continuity/Evidence, then publish integrated Project + target checkpoint together and fresh-resolve both source and target.
6. **Record real-consumer evidence in Svif and Agnir.** Any defect discovered by the real workflow should be fixed at the earliest faulty Agnir Core/profile/binding or Svif adapter layer rather than masked by branch-specific exceptions.
7. **Keep `main` and released `v0.2.0-preview.1` unchanged during validation.** If the experiment succeeds, decide separately how/when Svif should adopt Agnir Core `0.2` on authoritative `main`.

## Existing release and distribution work remains active

The Core `0.2` experiment does not supersede already-valid Svif release/distribution obligations:

1. **Retain the released Repository Preview evidence.** `v0.2.0-preview.1` remains immutable. Its immutable candidate was validated through **Codex CLI** and **ChatGPT desktop/Codex** before release; do not move that tag. If an observed Preview defect requires a fix, create `v0.2.0-preview.2`.
2. **Preserve immutable-candidate provenance.** Repository CI, marketplace/import state, tag resolution, and client acceptance are distinct evidence layers. Do not rewrite the released Preview's immutable candidate history while the Core `0.2` validation proceeds on temporary branches.
3. **Continue the separate public/personal ChatGPT path after the external publisher gate is resolvable.** Submit the exact supported Skills-only package to the **universal Plugins Directory**, explicitly Publish after approval, then validate installation and invocation on a real **individual-user ChatGPT surface**, with personal **ChatGPT Web** remaining a first-class product target.
4. Keep the **public/personal ChatGPT path** separate from Repository Preview validation and from the Core `0.2` continuity experiment. A successful Core migration is not directory publication evidence, and directory/review status is not continuity evidence.
5. Keep live Cloudflare delivery disabled unless explicitly authorized. If authorized later, preserve exact verified-subject delivery and independent observation before success claims.

## Validation compatibility reference

- Svif Project identity: `urn:svif:project:svif-core`.
- Validation Agnir Core compatibility: `0.2`.
- Validation repository/filesystem profile: `repository-filesystem/0.2`.
- Validation logical lineage: `urn:svif:lineage:agnir-core-0.2-validation`.
- Validation VCS selector binding: `refs/heads/feature/agnir-core-0.2-validation`.
- Agnir experimental source revision: `414dba1e50ad1bdcae3ca91d19c6768fdaa030cc`.
- Released Svif Preview and authoritative `main` continue to represent the previously published product line until explicitly migrated/integrated.

## Invariants

- The Project persists; Executors and execution environments may change.
- Svif remains Continuity-Provider-neutral at the Orchestrator layer.
- Agnir provider-specific lineage/selector semantics stay inside the Agnir adapter/binding.
- Project identity is not Agnir lineage identity.
- Agnir lineage identity is not VCS selector identity or revision receipt.
- A selected mismatched/unbound selector must fail; no sibling/ref guessing.
- Checkpoints are lineage-local by default.
- Integration is target reconciliation, not source continuity copying.
- Target ref advancement is a publication boundary.
- The released Skills-only first-use bootstrap remains on its published Agnir Core/profile `0.1` baseline until an intentional distribution release changes it; an already-initialized Project may migrate its provider binding separately.
- `main` is the only long-lived authoritative Svif branch; validation branches are temporary evidence carriers.

## Branch governance

- `main` is the only long-lived branch.
- Historical predecessor and retired work is indexed by immutable commit SHA in `history/BRANCH_ARCHIVE.md`; live legacy refs are not retained.
- Temporary Core `0.2` validation branches exist only for the authorized experiment and must not become a second long-lived authority.
