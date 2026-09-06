# Svif Current State

Svif is the authoritative active **Project orchestration product** in `iorLab/svif`. Authoritative `main` has accepted both the validated published-Agnir migration result and the Principal-approved Svif identity system through explicit target-owned integration. The former `iorLab/svif-cloudflare-reference` project is retired.

## Product architecture

Svif continues to coordinate the same four first-class components: Orchestrator (`src/svif/runtime.py`), Continuity Provider (`src/svif/continuity/agnir.py`), Execution Surface (`src/svif/execution/chatgpt.py`), and Capability Provider (`src/svif/capabilities/cloudflare.py`). The Project persists; Executors and execution environments may change. No execution surface becomes canonical Project truth merely because execution occurred there.

## Released Svif product state

- Svif product line: `0.2`.
- Released Repository Preview: immutable `v0.2.0-preview.1` from commit `2b07b6b5ea0bc8feee59f9f647be9af3069d056e`.
- Project Binding: `project-binding/0.2`.
- Software Delivery profile: `software-delivery/0.2`.
- Capability Adapter: `capability-adapter/0.2`.
- Evidence record: `evidence-record/0.2`.
- The released **Plugin MVP** / Preview.1 first-use bootstrap remains on its published Agnir Core/profile `0.1` baseline until a later Svif distribution intentionally changes that onboarding contract.
- The real **Codex CLI** and **ChatGPT desktop/Codex** Preview acceptance evidence remains valid and the released tag remains immutable.
- The separate public/personal ChatGPT path remains externally blocked at publisher verification/payment-method eligibility; repository CI is not personal **ChatGPT Web** installation evidence.
- Live Cloudflare delivery remains disabled unless explicitly authorized.
- `README.md` and `README.zh-CN.md` remain synchronized user/Agent entry points.

## Canonical brand identity — accepted 2026-09-07

The Principal-approved 10:42 AM Svif identity system is now part of authoritative `main`.

- canonical integration PR: `#5`;
- approved brand integration commit: `77ff3d0e8b3d0d691bb47529e065571c17a0aa81`;
- post-merge Svif product checks: run `34055656891`, repository-integrity / portable-contracts / runtime-kernel all success;
- visual authority: byte-exact `brand/reference/svif-approved-reference.png` plus the byte-exact Svif × Agnir family board;
- production model: fidelity-first raster masters under `brand/masters/`;
- delivery exports: committed under `brand/exports/`, including light/dark/monochrome, app icon, social card and favicons at 128/64/32/16;
- QA: symmetric 13/13 final package;
- deterministic rebuild path: `brand/tools/build-production-assets.py` with locked source SHA verification.

The approved Svif-only board SHA-256 remains `10ad09a3c68e7ccd84e8c50ac4aaeda2bdb1e1fee4c09899ef4215fdec18f3fd`; the family board SHA-256 remains `4110d285243b6241ac709e750cca1815a10ca41e27c3bb15e6c94b56e57fa4fb`.

The completed `brand/identity-system` branch tip `62e9aac53246cef4eccffacb9434ead9928c0c3c` is recorded in `history/BRANCH_ARCHIVE.md`; retirement workflow run `34055731552` succeeded, the temporary workflow removed itself, and the branch ref is no longer present. `main` is again the only long-lived Svif work line.

No brand integration changed the immutable `v0.2.0-preview.1` release tag or any Svif runtime/orchestration contract.

## Authoritative Agnir compatibility — accepted 2026-09-03 and preserved through brand integration

The Svif Project itself completed an explicit migration from published Agnir `v0.1.1` / Core-profile `0.1` to published stable Agnir `v0.2.0` / Core-profile `0.2`.

Authoritative continuity remains:

- Project identity: `urn:svif:project:svif-core` — unchanged;
- Agnir Core: `0.2`;
- profile: `repository-filesystem/0.2`;
- authoritative logical lineage: `urn:svif:lineage:authoritative`;
- VCS selector: `refs/heads/main`;
- durable locators: `.agnir/state.md`, `.agnir/next-actions.md`, `.agnir/decisions.md`, `.agnir/evidence/` — unchanged;
- Agnir operational release: `0.2.0`;
- immutable applied revision: `fc84095ed5d500be9e1b43a4af0e93356571bbd4`.

`SVIF.yaml` declares the same Project identity, Core/profile compatibility, logical lineage and VCS selector binding. Logical lineage identity is not derived from the branch ref or commit receipt.

Agnir `v1.0.0` is now the latest stable Agnir distribution, but this does **not** silently promote Svif's Project declaration. Agnir v1 preserves valid `0.2` Projects; `0.2` → `1.0` is a separately authorized Project-owned promotion. Brand publication did not authorize or perform that promotion, so `AGNIR.yaml` and `SVIF.yaml` intentionally remain on Core/profile `0.2`.

## Accepted published-Agnir migration receipts

Captured pre-migration authoritative main: `dac058789a27f32f4ed1949874c1954f31f12bd8`.

Validated migration source: `267f3d706e4fba67f2fb4a3a7ea33e80b9fb48ef`, tree `d6ffec2fddc48ec0052dd0531ca0088fb13b37b2`; exact source CI run `33724859300` passed repository-integrity, runtime-kernel and portable-contracts.

Target-reconciled candidate: `2b5b92ab234d4c1b0d6596bbb0b8439eb6e05cfa`, tree `191db90c0b959254025cb061159044c1b0ddf3d6`, with first parent `dac058789a27...` and second parent `267f3d706...`.

Candidate validation run `33725164044` passed all three jobs. PR #7 synthetic merge `1db24d60c7b4d60bde243c20fac1ab6ea1968798` produced exactly the same tree `191db90c...` as the staged candidate. Fresh stale checks immediately before publication confirmed main, migration source and candidate refs had not advanced.

Authoritative `main` then advanced exactly once, non-force, directly from `dac058789a27...` to `2b5b92ab234...`; ordinary PR merge was not used. There was no interval in which migration-line `AGNIR.yaml`, State or Next Actions were published as main truth and repaired afterward.

Post-publication main push CI run `33725240001` passed repository-integrity, runtime-kernel full unittest discovery and portable-contracts. Fresh reads of `main` confirm `AGNIR.yaml` and `SVIF.yaml` both resolve Core/profile `0.2`, Project `urn:svif:project:svif-core`, lineage `urn:svif:lineage:authoritative`, selector `refs/heads/main`, preserved durable locators and Agnir `v0.2.0@fc84095...` provenance.

This is the first recorded real Svif Project upgrade across the **published** Agnir `v0.1.1` -> **published** `v0.2.0` compatibility boundary. It is distinct from synthetic migration fixtures and the earlier pre-release Core 0.2 real-consumer experiment.

## Evidence consequence

Neither the accepted published-Agnir migration nor the canonical brand integration exposed a Svif/Agnir compatibility defect. Brand integration was deliberately compatibility-neutral and preserved the released Preview.1 onboarding baseline, current self-host Core/profile `0.2` binding, Project identity, lineage and durable locators.

Remaining material work is distribution/adoption work: post-1.0 Agnir downstream evidence, preservation of Preview evidence, the public/personal ChatGPT publication path when its publisher gate is resolvable, and separately authorized provider delivery work.

`.agnir/next-actions.md` is the canonical ordered resume plan.
