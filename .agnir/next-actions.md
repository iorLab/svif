# Svif Next Actions

Svif is performing a real downstream migration from published Agnir `v0.1.1` / Core-profile `0.1` to published stable Agnir `v0.2.0` / **Agnir Core 0.2** / `repository-filesystem/0.2` on temporary lineage `urn:svif:lineage:agnir-v0.2.0-stable-migration`. Authoritative `main` remains unchanged until the exact migration result is fully validated and reconciled.

1. **Converge current-Project guards onto Agnir Core/profile `0.2`.** Update repository integrity and current-binding tests to accept the explicit logical lineage + selector binding. Preserve the released Skills-only Preview.1 first-use bootstrap baseline at Core/profile `0.1`; changing that onboarding contract requires a later intentional distribution release, not this Project migration.
2. **Validate the migrated Svif Project as a real published-stable downstream consumer.** Require Project identity `urn:svif:project:svif-core`, logical lineage presence, selector != lineage identity, unchanged durable memory locators, stable Agnir provenance `v0.2.0` / `fc84095...`, Core/profile `0.2` discovery, checkpoint/resume, founding E2E, Plugin package/first-use behavior, repository integrity, contracts and full suite.
3. **Pressure upgrade usability rather than hiding friction.** Any failure attributable to Agnir `v0.2.0` migration semantics, discovery, lineage binding or recovery should be treated as Agnir product evidence and repaired in Agnir `v0.2.x` when appropriate rather than papered over in Svif.
4. **Construct a target-reconciled main candidate only after the migration branch is fully green.** Main must receive the accepted Project/package result while establishing target-owned authoritative logical lineage and `refs/heads/main` binding. Do not copy temporary migration-line State/Next as automatic target truth, and do not advance main before candidate validation and fresh source/target stale checks.
5. **After authoritative-main verification, record this as Agnir v1 downstream-upgrade evidence.** The receipt must distinguish synthetic fixtures and earlier pre-release experiments from this published `v0.1.1` -> published `v0.2.0` real Project upgrade.
6. **Preserve the released Repository Preview and distribution evidence.** Keep `v0.2.0-preview.1` immutable and preserve its **immutable candidate**, real **Codex CLI**, and **ChatGPT desktop/Codex** acceptance evidence. Any Preview fix uses a new tag such as `v0.2.0-preview.2`.
7. **Continue the separate public/personal ChatGPT path when the publisher gate is resolvable.** Submit the supported Skills-only package to the **universal Plugins Directory**, explicitly Publish after approval, then validate a real **individual-user ChatGPT surface**, with **ChatGPT Web** remaining a first-class target.
8. Keep live Cloudflare delivery disabled unless explicitly authorized.
9. **Retire temporary migration/validation refs after accepted reconciliation when a safe delete-ref path is available.** `main` remains the only long-lived Svif branch.

## Captured migration receipts

- authoritative Svif baseline: `main@dac058789a27f32f4ed1949874c1954f31f12bd8`;
- previous Agnir operational release: `v0.1.1` -> `e9712357ab590e5c1e5357b3cf3219d07d789aff`;
- target Agnir stable release: `v0.2.0` -> `fc84095ed5d500be9e1b43a4af0e93356571bbd4`;
- preparatory dual-line adapter/tests commit: `ddaee058efe4c8381f60f5a2ebcae0de9ee9203d`;
- migration Project-truth commit: `eac2ab0dd70695d972b99afad084614eae26c77c`;
- initial Draft PR #6 run: `33723726831`; portable contracts success, failures limited to old current-binding/repository guards and preserved distribution-marker assertions;
- migration branch selector: `refs/heads/migration/agnir-v0.2.0-stable`;
- migration logical lineage: `urn:svif:lineage:agnir-v0.2.0-stable-migration`.

## Invariants

- Project identity remains stable across migration.
- Durable State/Next/Decisions/Evidence remain Project-owned.
- logical lineage identity != VCS selector != commit/checkpoint receipt.
- Core `0.1` -> `0.2` is explicit migration, not compatible upgrade.
- Source/migration continuity is reconciliation input, not automatic target-main truth.
- The released Preview.1 bootstrap baseline and the Svif repository's current self-host binding are separate versioned facts.
- Svif product architecture remains Orchestrator + Continuity Provider + Execution Surface + Capability Provider.
