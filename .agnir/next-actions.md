# Svif Next Actions

Svif is performing a real downstream migration from published Agnir `v0.1.1` / Core-profile `0.1` to published stable Agnir `v0.2.0` / Core-profile `0.2` on temporary lineage `urn:svif:lineage:agnir-v0.2.0-stable-migration`. Authoritative `main` remains unchanged until the exact migration result is fully validated and reconciled.

1. **Converge every active Svif surface onto Agnir Core/profile `0.2`.** Update the shared Plugin Skill first-use bootstrap/activation/current-binding text, first-use/bootstrap tests, repository checks, bilingual README and repository map where they describe the founding Agnir compatibility line. Do not change Orchestrator/Execution/Capability architecture merely because the Continuity Provider compatibility changed.
2. **Validate the migrated Svif Project as a real published-stable downstream consumer.** Require Project identity `urn:svif:project:svif-core`, logical lineage presence, selector != lineage identity, unchanged durable memory locators, stable Agnir provenance `v0.2.0` / `fc84095...`, Core/profile `0.2` discovery, checkpoint/resume, founding E2E, Plugin package/first-use behavior, repository integrity, contracts and full suite.
3. **Pressure upgrade usability rather than hiding friction.** Any failure attributable to Agnir `v0.2.0` migration semantics, Skill contract, discovery, lineage binding or recovery should be treated as Agnir product evidence and repaired in Agnir `v0.2.x` when appropriate rather than papered over in Svif.
4. **Construct a target-reconciled main candidate only after the migration branch is fully green.** Main must receive the accepted Project/package result while creating/preserving its own authoritative logical lineage and `refs/heads/main` binding. Do not copy temporary migration-line State/Next as automatic target truth, and do not advance main before candidate validation and fresh source/target stale checks.
5. **After authoritative-main verification, record this as Agnir v1 downstream-upgrade evidence.** The receipt must distinguish synthetic fixtures and earlier pre-release experiments from this published `v0.1.1` -> published `v0.2.0` real Project upgrade.
6. **Preserve existing Svif distribution obligations.** Keep `v0.2.0-preview.1` immutable; continue the separate personal ChatGPT publisher-verification path; use a new Preview tag for any Svif release fix; keep live Cloudflare delivery disabled unless explicitly authorized.
7. **Retire temporary migration/validation refs after accepted reconciliation when a safe delete-ref path is available.** `main` remains the only long-lived Svif branch.

## Captured migration receipts

- authoritative Svif baseline: `main@dac058789a27f32f4ed1949874c1954f31f12bd8`;
- previous Agnir operational release: `v0.1.1` -> `e9712357ab590e5c1e5357b3cf3219d07d789aff`;
- target Agnir stable release: `v0.2.0` -> `fc84095ed5d500be9e1b43a4af0e93356571bbd4`;
- preparatory dual-line adapter/tests commit: `ddaee058efe4c8381f60f5a2ebcae0de9ee9203d`;
- migration branch selector: `refs/heads/migration/agnir-v0.2.0-stable`;
- migration logical lineage: `urn:svif:lineage:agnir-v0.2.0-stable-migration`.

## Invariants

- Project identity remains stable across migration.
- Durable State/Next/Decisions/Evidence remain Project-owned.
- logical lineage identity != VCS selector != commit/checkpoint receipt.
- Core `0.1` -> `0.2` is explicit migration, not compatible upgrade.
- Source/migration continuity is reconciliation input, not automatic target-main truth.
- Svif product architecture remains Orchestrator + Continuity Provider + Execution Surface + Capability Provider.
