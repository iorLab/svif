# Svif Next Actions

## Active Agnir Core 0.2 real-consumer validation

1. **Verify this source-lineage checkpoint independently.** CI and fresh self-host discovery must resolve Project `urn:svif:project:svif-core`, logical lineage `urn:svif:lineage:agnir-core-0.2-parallel`, selector `refs/heads/feature/agnir-core-0.2-parallel`, and source-local State / Next Actions / Evidence. The target validation ref must remain at its own checkpoint.
2. **Advance the target validation lineage independently.** Make a material target-only Project/continuity change on `feature/agnir-core-0.2-validation`, preserving its lineage `urn:svif:lineage:agnir-core-0.2-validation` and selector binding.
3. **Capture source and target revisions plus continuity before integration.** Do not use sibling scanning or ref-name inference as lineage identity.
4. **Stage source→target integration without advancing the target ref.** Build the integrated Project candidate while the target ref still names its pre-integration checkpoint; any unresolved continuity conflict remains `AGNIR_VCS_RECONCILIATION_REQUIRED`-class behavior.
5. **Reconcile target continuity before publication.** Reconcile the actual integrated Project result, previous target State / Next Actions / Decisions, relevant source continuity/Evidence, and Principal intent. Source lineage/selector metadata is input, not target truth.
6. **Publish integrated Project + reconciled target continuity coherently.** Advance the target ref exactly once to the integrated revision, then fresh-resolve target and source independently.
7. **Feed the completed real-consumer evidence back into Agnir.** Update Agnir Core `0.2` release readiness and fix any defect at the earliest Core/profile/binding/consumer layer.
8. **Keep Svif `main` and released `v0.2.0-preview.1` unchanged during the experiment.** Adoption of Agnir Core `0.2` on authoritative `main` is a separate decision.

## Existing release and distribution work remains active

- `v0.2.0-preview.1` remains immutable. Its immutable candidate was exercised through **Codex CLI** and **ChatGPT desktop/Codex**; any Preview fix must use a new tag such as `v0.2.0-preview.2`.
- Preserve the released Preview's **immutable candidate** provenance and keep repository CI, tag resolution, marketplace/import state, and client acceptance as distinct evidence layers.
- Continue the separate **public/personal ChatGPT path** when the external publisher gate is resolvable: submit the supported Skills-only package to the **universal Plugins Directory**, explicitly Publish after approval, then validate a real **individual-user ChatGPT surface**, with **ChatGPT Web** remaining a first-class target.
- Core `0.2` validation is not publication evidence, and directory/review status is not continuity evidence.
- Keep live Cloudflare delivery disabled unless explicitly authorized.

## Current lineage reference

- Project: `urn:svif:project:svif-core`.
- Source lineage: `urn:svif:lineage:agnir-core-0.2-parallel`.
- Source selector: `refs/heads/feature/agnir-core-0.2-parallel`.
- Fork baseline: `329984f94483a7cbbb21a6faa42b9cf9ed84fed2`.
- Target lineage: `urn:svif:lineage:agnir-core-0.2-validation`.
- Target selector: `refs/heads/feature/agnir-core-0.2-validation`.
- Agnir experimental source revision: `414dba1e50ad1bdcae3ca91d19c6768fdaa030cc`.
- Green migrated-baseline CI: `33616508143`.
- Green target self-host checkpoint CI: `33616750662`.

## Invariants

- The Project persists; Executors and execution environments may change.
- Svif remains Continuity-Provider-neutral at the Orchestrator layer.
- Project identity is not lineage identity; lineage identity is not selector or revision receipt.
- Checkpoints are lineage-local by default.
- A selected missing or mismatched binding must fail rather than guess.
- Integration is target reconciliation, not source continuity copying.
- Target ref advancement is the VCS publication boundary.
- The released Skills-only first-use bootstrap remains on its published Agnir Core/profile `0.1` baseline until an intentional distribution release changes it.
- `main` is the only long-lived authoritative Svif branch; validation branches are temporary evidence carriers.
