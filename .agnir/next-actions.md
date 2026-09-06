# Svif Next Actions

The Principal-approved Svif identity system is now integrated into authoritative `main`, post-merge product checks are green, and the completed `brand/identity-system` branch has been archived and retired. The Svif Project itself intentionally remains on Agnir Core/profile `0.2`; Agnir `v1.0.0` being latest stable does not silently promote this Project.

1. **Record the completed real Svif downstream upgrade as Agnir post-1.0 adoption evidence.** Preserve the exact Svif pre-migration main, migration source, target-reconciled candidate/tree, source/candidate/main CI runs, synthetic-tree receipts, stale checks, publication boundary, Project identity/locator preservation, and the distinction between current self-host Core/profile `0.2` and immutable Preview.1 bootstrap Core/profile `0.1`. This is adoption evidence, not a reason to reopen satisfied Agnir v1 release gates.
2. **Preserve the released Repository Preview and distribution evidence.** Keep `v0.2.0-preview.1` immutable and preserve its **immutable candidate**, real **Codex CLI**, and **ChatGPT desktop/Codex** acceptance evidence. Any Preview fix uses a new tag such as `v0.2.0-preview.2`.
3. **Continue the separate public/personal ChatGPT path when the publisher gate is resolvable.** Submit the supported Skills-only package to the **universal Plugins Directory**, explicitly Publish after approval, then validate a real **individual-user ChatGPT surface**, with **ChatGPT Web** remaining a first-class target.
4. **Treat future Agnir updates according to compatibility semantics.** The current Svif Project remains Core/profile `0.2`. Agnir 1.0 distribution availability alone is not a Project promotion. Any `0.2` → `1.0` Project promotion requires separate explicit authorization and must preserve Project identity, lineage, selectors, locators and migration evidence.
5. Keep live Cloudflare delivery disabled unless explicitly authorized.
6. **Retire remaining temporary migration/validation refs only after their evidence is safely captured.** The completed `brand/identity-system` branch is already archived at tip `62e9aac53246cef4eccffacb9434ead9928c0c3c` and retired; `main` remains the only intended long-lived Svif branch.

## Canonical brand integration receipts

- final brand candidate head: `62e9aac53246cef4eccffacb9434ead9928c0c3c`;
- final PR #5 synthetic-merge/product checks: run `34055608705`, all three jobs success;
- authoritative brand merge: `77ff3d0e8b3d0d691bb47529e065571c17a0aa81`;
- authoritative post-merge product checks: run `34055656891`, all three jobs success;
- approved Svif reference SHA-256: `10ad09a3c68e7ccd84e8c50ac4aaeda2bdb1e1fee4c09899ef4215fdec18f3fd`;
- approved family reference SHA-256: `4110d285243b6241ac709e750cca1815a10ca41e27c3bb15e6c94b56e57fa4fb`;
- byte-exact materialization run: `33730468886` success;
- materialization commit: `137307351dfee467472ccd997fdc714b8a71c549`;
- branch-archive commit: `ff3b2ce8310add5f3890a3aeb5756e272bf9b6b8`;
- retirement workflow run: `34055731552` success;
- one-shot workflow removal/main head before this checkpoint: `d8b2feb546e88b6b8692078dc6536d195d0bc9c6`;
- `brand/identity-system`: retired after archive receipt;
- `v0.2.0-preview.1`: unchanged and immutable;
- main `AGNIR.yaml` / `SVIF.yaml`: still Core/profile `0.2`.

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

- Project identity remains stable across migration and brand integration.
- Durable State/Next/Decisions/Evidence remain Project-owned.
- logical lineage identity != VCS selector != commit/checkpoint receipt.
- Core `0.1` -> `0.2` is explicit migration, not compatible upgrade.
- Core/profile `0.2` -> `1.0` requires separate explicit Project-owned promotion.
- Source/migration/brand branch continuity is reconciliation input, not automatic target truth.
- Main publication exposes integrated Project result + reconciled target continuity coherently.
- The released Preview.1 bootstrap baseline and the Svif repository's current self-host binding are separate versioned facts.
- The approved brand visual authority cannot be redesigned by downstream derivatives.
- Svif product architecture remains Orchestrator + Continuity Provider + Execution Surface + Capability Provider.
