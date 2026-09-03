# Svif Next Actions

The temporary Svif migration lineage has completed real downstream validation against published Agnir `v0.2.0` / Core-profile `0.2`. Authoritative `main` remains at the captured pre-migration Project until a target-owned reconciled candidate is independently validated.

1. **Checkpoint the final migration source and require fresh exact-head CI.** Preserve run `33724576017`, synthetic merge `5d145ce1...`, and exact tree `142051872...`; the checkpoint itself must also pass repository integrity, runtime/unit tests and portable contracts before becoming the source receipt for main reconciliation.
2. **Construct a target-reconciled main candidate without advancing main.** Accept the validated adapter/tests/Skill/repository-map/migration-evidence changes, but rebuild target continuity for Project `urn:svif:project:svif-core` on logical lineage `urn:svif:lineage:authoritative`, separately bound to `refs/heads/main`. `SVIF.yaml` must carry the matching lineage/selector binding. Preserve stable Agnir `v0.2.0` provenance at `fc84095...`.
3. **Do not copy temporary migration-line State/Next as target truth.** Reconcile main Current State and Next Actions against the actual integrated Project result and preserve unrelated Svif release/distribution obligations, including immutable `v0.2.0-preview.1`, Codex/desktop acceptance evidence, the public/personal ChatGPT path, and Cloudflare authority policy.
4. **Validate the exact target candidate while main remains unchanged.** Require repository integrity, runtime-kernel full suite, portable contracts, Core/profile `0.2` fresh self-consumption, lineage/selector agreement, retained Preview.1 bootstrap `0.1` regression, and the published-stable migration evidence guard.
5. **Fresh stale-check source and target immediately before publication.** Captured main must still be `dac058789a27f32f4ed1949874c1954f31f12bd8`; migration source must still equal the final validated checkpoint. Any advance invalidates the candidate.
6. **Advance main exactly once to the verified target-reconciled candidate.** Do not use ordinary PR merge as the publication primitive and do not publish migration-line continuity first then repair it.
7. **Verify authoritative-main fresh resume and CI.** Confirm Core/profile `0.2`, Project identity, target logical lineage `urn:svif:lineage:authoritative`, selector `refs/heads/main`, stable Agnir `v0.2.0` provenance, existing durable locators, and the complete Svif product test surface.
8. **Record a post-integration main checkpoint and feed the result back into Agnir v1 evidence.** Distinguish this published `v0.1.1` -> published `v0.2.0` real Project upgrade from earlier experimental Core 0.2 validation and synthetic fixtures.
9. **Preserve the released Repository Preview and distribution evidence.** Keep `v0.2.0-preview.1` immutable and preserve its **immutable candidate**, real **Codex CLI**, and **ChatGPT desktop/Codex** acceptance evidence. Any Preview fix uses a new tag such as `v0.2.0-preview.2`.
10. **Continue the separate public/personal ChatGPT path when the publisher gate is resolvable.** Submit the supported Skills-only package to the **universal Plugins Directory**, explicitly Publish after approval, then validate a real **individual-user ChatGPT surface**, with **ChatGPT Web** remaining a first-class target.
11. Keep live Cloudflare delivery disabled unless explicitly authorized.
12. Retire temporary migration/validation refs after accepted reconciliation when a safe delete-ref path is available. `main` remains the only long-lived Svif branch.

## Final migration-line receipts before checkpoint

- captured source main: `dac058789a27f32f4ed1949874c1954f31f12bd8`;
- Agnir source release: `v0.1.1` -> `e9712357ab590e5c1e5357b3cf3219d07d789aff`;
- Agnir target stable: `v0.2.0` -> `fc84095ed5d500be9e1b43a4af0e93356571bbd4`;
- migration head before this checkpoint: `5b2086bdc61cd5dad8397241565fbbda9592fc88`;
- migration head tree: `142051872a708c9944c737e1ebcee008ac27a381`;
- final PR-head run: `33724576017` success, all three jobs green;
- synthetic merge: `5d145ce1eb4ec4e6b837194a3e206b77bb71665b`;
- synthetic merge tree: `142051872a708c9944c737e1ebcee008ac27a381`, exact tree match;
- migration selector: `refs/heads/migration/agnir-v0.2.0-stable`;
- migration logical lineage: `urn:svif:lineage:agnir-v0.2.0-stable-migration`.

## Invariants

- Project identity remains stable across migration.
- Durable State/Next/Decisions/Evidence remain Project-owned.
- logical lineage identity != VCS selector != commit/checkpoint receipt.
- Core `0.1` -> `0.2` is explicit migration, not compatible upgrade.
- Source/migration continuity is reconciliation input, not automatic target-main truth.
- The released Preview.1 bootstrap baseline and the Svif repository's current self-host binding are separate versioned facts.
- Svif product architecture remains Orchestrator + Continuity Provider + Execution Surface + Capability Provider.
