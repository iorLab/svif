# Svif Next Actions

The real Svif Project migration from published Agnir `v0.1.1` / Core-profile `0.1` to published stable Agnir `v0.2.0` / Core-profile `0.2` has been accepted on authoritative `main` through target-owned reconciliation. Main now uses logical lineage `urn:svif:lineage:authoritative` bound separately to `refs/heads/main`, and authoritative push CI is green.

1. **Feed the completed real downstream upgrade into Agnir v1 evidence.** Record the exact Svif pre-migration main, migration source, target-reconciled candidate, candidate tree, source/candidate/main CI runs, synthetic-tree receipts, fresh stale checks, main publication boundary, Project identity/locator preservation, and the distinction between current self-host Core/profile `0.2` and immutable Preview.1 bootstrap Core/profile `0.1`.
2. **Preserve the released Repository Preview and distribution evidence.** Keep `v0.2.0-preview.1` immutable and preserve its **immutable candidate**, real **Codex CLI**, and **ChatGPT desktop/Codex** acceptance evidence. Any Preview fix uses a new tag such as `v0.2.0-preview.2`.
3. **Continue the separate public/personal ChatGPT path when the publisher gate is resolvable.** Submit the supported Skills-only package to the **universal Plugins Directory**, explicitly Publish after approval, then validate a real **individual-user ChatGPT surface**, with **ChatGPT Web** remaining a first-class target.
4. **Treat future Agnir updates according to compatibility semantics.** Core `0.2` compatible repository updates may preserve the current lineage; any future incompatible Core boundary must use explicit migration rather than silent upgrade.
5. Keep live Cloudflare delivery disabled unless explicitly authorized.
6. Retire temporary migration/validation refs after their evidence has been safely captured and when a safe delete-ref path is available. `main` remains the only long-lived Svif branch.

## Completed published-Agnir migration receipts

- captured pre-migration main: `dac058789a27f32f4ed1949874c1954f31f12bd8`;
- published Agnir source: `v0.1.1` -> `e9712357ab590e5c1e5357b3cf3219d07d789aff`;
- published Agnir target: `v0.2.0` -> `fc84095ed5d500be9e1b43a4af0e93356571bbd4`;
- validated migration source: `267f3d706e4fba67f2fb4a3a7ea33e80b9fb48ef`, tree `d6ffec2fddc48ec0052dd0531ca0088fb13b37b2`;
- migration source CI: `33724859300` success, all three jobs green;
- target-reconciled candidate/main publication revision: `2b5b92ab234d4c1b0d6596bbb0b8439eb6e05cfa`;
- target candidate tree: `191db90c0b959254025cb061159044c1b0ddf3d6`;
- candidate CI: `33725164044` success, all three jobs green;
- PR #7 synthetic merge: `1db24d60c7b4d60bde243c20fac1ab6ea1968798`, exact tree `191db90c...`;
- authoritative-main push CI: `33725240001` success, all three jobs green;
- Project identity: `urn:svif:project:svif-core`;
- authoritative logical lineage: `urn:svif:lineage:authoritative`;
- authoritative selector: `refs/heads/main`;
- durable State/Next/Decisions/Evidence locators: unchanged;
- main `AGNIR.yaml` and `SVIF.yaml`: Core/profile `0.2`, matching lineage/selector binding, Agnir operational `v0.2.0@fc84095...`.

## Invariants

- Project identity remains stable across migration.
- Durable State/Next/Decisions/Evidence remain Project-owned.
- logical lineage identity != VCS selector != commit/checkpoint receipt.
- Core `0.1` -> `0.2` is explicit migration, not compatible upgrade.
- Source/migration continuity is reconciliation input, not automatic target truth.
- Main publication exposed Project result + reconciled target continuity in one coherent ref advancement.
- The released Preview.1 bootstrap baseline and the Svif repository's current self-host binding are separate versioned facts.
- Svif product architecture remains Orchestrator + Continuity Provider + Execution Surface + Capability Provider.
