# Svif Next Actions

## Active Agnir Core 0.2 real-consumer validation

1. **Verify this independently advanced target lineage.** CI and fresh self-host discovery must resolve Project `urn:svif:project:svif-core`, target lineage `urn:svif:lineage:agnir-core-0.2-validation`, target selector `refs/heads/feature/agnir-core-0.2-validation`, and target-local State / Next Actions / Evidence.
2. **Wait for the source lineage to be independently green.** Source `feature/agnir-core-0.2-parallel` must resolve its different lineage/selector and pass the same product gates without relying on target constants.
3. **Capture immutable pre-integration facts.** Record target revision/continuity and source revision/continuity before staging; verify both share Project identity but have different logical lineage identities and selectors.
4. **Stage source→target Project integration without advancing the target ref.** The target ref must remain at its pre-integration checkpoint while the candidate is unreconciled.
5. **Reconcile target continuity.** Use the actual integrated Project candidate, previous target truth, relevant source continuity/Evidence, and Principal intent. Source lineage/selector metadata is reconciliation input, never automatic target truth.
6. **Publish coherently.** Construct one two-parent target revision containing integrated Project content plus reconciled target continuity, then advance the target ref once and fresh-resolve target and source independently.
7. **Record completed real-consumer evidence back in Agnir.** If the experiment passes, update Core `0.2` release readiness and begin planning safe Agnir PR #4/#5 integration and `v0.2.0` RC preparation.
8. **Keep Svif `main` and `v0.2.0-preview.1` unchanged during the experiment.**

## Existing release and distribution work remains active

- `v0.2.0-preview.1` remains immutable; its **immutable candidate** was exercised through **Codex CLI** and **ChatGPT desktop/Codex**. Any Preview fix uses a new tag.
- Continue the separate **public/personal ChatGPT path** when the publisher gate is resolvable: submit the Skills-only package to the **universal Plugins Directory**, explicitly Publish after approval, then validate a real **individual-user ChatGPT surface**, with **ChatGPT Web** remaining a first-class target.
- Core `0.2` validation is not directory publication evidence, and directory/review status is not continuity evidence.
- Keep live Cloudflare delivery disabled unless explicitly authorized.

## Target lineage reference

- Project: `urn:svif:project:svif-core`.
- Target lineage: `urn:svif:lineage:agnir-core-0.2-validation`.
- Target selector: `refs/heads/feature/agnir-core-0.2-validation`.
- Common fork baseline: `329984f94483a7cbbb21a6faa42b9cf9ed84fed2`.
- Source lineage: `urn:svif:lineage:agnir-core-0.2-parallel`.
- Source selector: `refs/heads/feature/agnir-core-0.2-parallel`.
- Agnir experimental source revision: `414dba1e50ad1bdcae3ca91d19c6768fdaa030cc`.
- Green migrated-baseline CI: `33616508143`.
- Green target self-host checkpoint CI: `33616750662`.

## Invariants

- The Project persists; Executors and execution environments may change.
- Svif Orchestrator remains Continuity-Provider-neutral.
- Project identity is not lineage identity; lineage identity is not selector or revision receipt.
- Selection is explicit/binding-driven and never guessed by sibling scanning.
- Checkpoints are lineage-local by default.
- Integration is target reconciliation, not source continuity copying.
- Target ref advancement is the publication boundary.
- The released Skills-only first-use bootstrap remains on its published Agnir Core/profile `0.1` baseline until an intentional distribution release changes it.
- `main` is the only long-lived authoritative Svif branch; validation branches are temporary evidence carriers.
