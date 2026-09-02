# Svif Next Actions

## Complete the real Agnir Core 0.2 lineage validation

1. **Publish the already-reconciled two-parent target revision exactly once.** The target ref must advance from pre-integration `79c5b7c7ee2ed545492702bea43d0f7135602f35` directly to the final integrated revision; do not publish staged candidate `4b86b3adafe08cc2f7fd48eb4f685d2b633b25c3` as target truth.
2. **Run full target verification after publication.** Require repository-integrity, portable-contracts, runtime-kernel, and fresh Core `0.2` target self-host discovery to pass on the final target revision.
3. **Fresh-resolve the source lineage independently after target publication.** Source ref `feature/agnir-core-0.2-parallel` must remain at its own revision and resolve `urn:svif:lineage:agnir-core-0.2-parallel` / `refs/heads/feature/agnir-core-0.2-parallel` without being rewritten by target integration.
4. **Record the completed real-consumer validation in Agnir.** Feed exact Svif source/target revisions, staged candidate, final integration revision, CI runs, and fresh-resume observations into `iorLab/agnir` on `feature/core-0.2-lineage`.
5. **Reassess Agnir Core `0.2` release gates.** If no new defect appears, move from synthetic/consumer validation toward safe Agnir PR #4/#5 integration design and repository `v0.2.0-rc.1` preparation; do not merge Agnir `main` through an unsafe ordinary server-side path.
6. **Keep Svif `main` and released `v0.2.0-preview.1` unchanged during this validation.** Decide authoritative Svif adoption of Agnir Core `0.2` separately after Agnir's compatibility line is accepted.

## Existing release and distribution work remains active

- `v0.2.0-preview.1` remains immutable; its **immutable candidate** was exercised through **Codex CLI** and **ChatGPT desktop/Codex**. Any Preview fix uses a new tag.
- Continue the separate **public/personal ChatGPT path** when the publisher gate is resolvable: submit the Skills-only package to the **universal Plugins Directory**, explicitly Publish after approval, then validate a real **individual-user ChatGPT surface**, with **ChatGPT Web** remaining a first-class target.
- Core `0.2` validation is not directory publication evidence, and directory/review status is not continuity evidence.
- Keep live Cloudflare delivery disabled unless explicitly authorized.

## Integration receipts

- Common baseline: `329984f94483a7cbbb21a6faa42b9cf9ed84fed2`.
- Target pre-integration: `79c5b7c7ee2ed545492702bea43d0f7135602f35`; CI `33619053159` success.
- Source: `d2d0c1bf25526b54490cce14c5aa8797c85c4d54`; CI `33618885830` success.
- Staged candidate: `4b86b3adafe08cc2f7fd48eb4f685d2b633b25c3`; target ref remained unchanged after staging.
- Target lineage: `urn:svif:lineage:agnir-core-0.2-validation`.
- Source lineage: `urn:svif:lineage:agnir-core-0.2-parallel`.
- Agnir experimental source revision: `414dba1e50ad1bdcae3ca91d19c6768fdaa030cc`.

## Invariants

- The Project persists; Executors and execution environments may change.
- Svif Orchestrator remains Continuity-Provider-neutral.
- Project identity is not lineage identity; lineage identity is not selector or revision receipt.
- Selection is explicit/binding-driven and never guessed by sibling scanning.
- Checkpoints are lineage-local by default.
- Source continuity is reconciliation input, not automatic target truth.
- Target ref advancement is the publication boundary.
- The released Skills-only first-use bootstrap remains on its published Agnir Core/profile `0.1` baseline until an intentional distribution release changes it.
- `main` is the only long-lived authoritative Svif branch; validation branches are temporary evidence carriers.
