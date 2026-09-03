# Svif Next Actions

The validated published-Agnir `v0.2.0` migration is being staged for authoritative-main acceptance through target-owned reconciliation. The candidate preserves Project `urn:svif:project:svif-core`, uses logical lineage `urn:svif:lineage:authoritative`, and binds it separately to `refs/heads/main`.

1. **Validate the exact target-reconciled candidate while main remains unchanged.** Require repository-integrity, runtime-kernel full unittest discovery, portable contracts, Core/profile `0.2` self-consumption, matching `AGNIR.yaml` / `SVIF.yaml` lineage+selector binding, stable Agnir `v0.2.0` provenance, and retained Preview.1 bootstrap Core/profile `0.1` regression.
2. **Verify the candidate integration tree is exactly the intended target tree.** Any synthetic validation surface must produce the same tree as the staged candidate; do not allow a server-side merge result to choose continuity conflict sides.
3. **Fresh stale-check source and target immediately before publication.** Main must still be `dac058789a27f32f4ed1949874c1954f31f12bd8`; validated migration source must still be `267f3d706e4fba67f2fb4a3a7ea33e80b9fb48ef`. Any change invalidates the candidate.
4. **Advance main exactly once to the verified target-reconciled candidate.** Do not ordinary-merge PR #6 and do not publish migration-line `AGNIR.yaml`/State/Next first then repair them.
5. **Verify authoritative-main fresh resume and push CI.** Confirm Core/profile `0.2`, Project identity `urn:svif:project:svif-core`, lineage `urn:svif:lineage:authoritative`, selector `refs/heads/main`, unchanged durable locators, stable Agnir `v0.2.0` / `fc84095...` provenance, repository integrity, runtime/unit tests and portable contracts.
6. **Record a post-integration main checkpoint.** Capture exact accepted main revision/run and close the migration acceptance loop without rewriting the immutable Svif Preview tag or Agnir stable tag.
7. **Feed this real downstream upgrade into Agnir v1 evidence.** Distinguish it from synthetic migration fixtures and earlier pre-release Core 0.2 consumer validation; this is the first published `v0.1.1` -> published `v0.2.0` real Project upgrade boundary.
8. **Preserve the released Repository Preview and distribution evidence.** Keep `v0.2.0-preview.1` immutable and preserve its **immutable candidate**, real **Codex CLI**, and **ChatGPT desktop/Codex** acceptance evidence. Any Preview fix uses a new tag such as `v0.2.0-preview.2`.
9. **Continue the separate public/personal ChatGPT path when the publisher gate is resolvable.** Submit the supported Skills-only package to the **universal Plugins Directory**, explicitly Publish after approval, then validate a real **individual-user ChatGPT surface**, with **ChatGPT Web** remaining a first-class target.
10. Keep live Cloudflare delivery disabled unless explicitly authorized.
11. Retire temporary migration/validation refs after accepted reconciliation when a safe delete-ref path is available. `main` remains the only long-lived Svif branch.

## Accepted source receipts for target reconciliation

- captured target main: `dac058789a27f32f4ed1949874c1954f31f12bd8`;
- published Agnir source: `v0.1.1` -> `e9712357ab590e5c1e5357b3cf3219d07d789aff`;
- published Agnir target: `v0.2.0` -> `fc84095ed5d500be9e1b43a4af0e93356571bbd4`;
- validated migration source: `267f3d706e4fba67f2fb4a3a7ea33e80b9fb48ef`;
- migration source tree: `d6ffec2fddc48ec0052dd0531ca0088fb13b37b2`;
- migration checkpoint run: `33724859300` success, all three jobs green;
- prior exact product/Skill run: `33724576017` success;
- prior synthetic merge `5d145ce1eb4ec4e6b837194a3e206b77bb71665b` had exact source tree `142051872a708c9944c737e1ebcee008ac27a381` before the receipt-only checkpoint;
- target logical lineage: `urn:svif:lineage:authoritative`;
- target selector: `refs/heads/main`.

## Invariants

- Project identity remains stable across migration.
- Durable State/Next/Decisions/Evidence remain Project-owned.
- logical lineage identity != VCS selector != commit/checkpoint receipt.
- Core `0.1` -> `0.2` is explicit migration, not compatible upgrade.
- Source/migration continuity is reconciliation input, not automatic target truth.
- The released Preview.1 bootstrap baseline and the Svif repository's current self-host binding are separate versioned facts.
- Svif product architecture remains Orchestrator + Continuity Provider + Execution Surface + Capability Provider.
