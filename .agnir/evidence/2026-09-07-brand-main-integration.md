# Canonical Svif brand identity integration — 2026-09-07

Status: **accepted on authoritative `main`.**

## Scope

This checkpoint accepts the Principal-approved Svif identity system as canonical repository truth without changing Svif's product/version/continuity compatibility contracts.

## Final candidate and target relation

- authoritative target before merge: `eba1b8538c4692a08bf69452525b735d23564599`;
- final brand candidate head: `62e9aac53246cef4eccffacb9434ead9928c0c3c`;
- final comparison before merge: brand ahead, `behind main = 0`, merge base equal to the authoritative target;
- PR #5: mergeable and ready after final gate recheck;
- final PR synthetic-merge/product-check run: `34055608705`, all repository-integrity / portable-contracts / runtime-kernel jobs success.

## Authoritative integration

PR #5 was squash-merged to authoritative `main` as:

- merge commit: `77ff3d0e8b3d0d691bb47529e065571c17a0aa81`;
- commit title: `brand: integrate approved Svif identity system`.

The squash preserved the complete material brand result while avoiding publication of dozens of intermediate candidate/review commits as first-class mainline history.

Post-merge push run `34055656891` passed all three canonical Svif product-check jobs.

## Byte-exact visual authority and production package

Canonical repository assets include:

- `brand/reference/svif-approved-reference.png` — locked SHA-256 `10ad09a3c68e7ccd84e8c50ac4aaeda2bdb1e1fee4c09899ef4215fdec18f3fd`, Git blob `32471dcf038a32d3b2fe78b543d0d0097aa1c551`;
- `brand/reference/svif-agnir-family-approved-reference.png` — locked SHA-256 `4110d285243b6241ac709e750cca1815a10ca41e27c3bb15e6c94b56e57fa4fb`, Git blob `bee7c715ee243ff4ccf45fad489858bdb43bcb5d`;
- fidelity-first raster masters under `brand/masters/`;
- complete light/dark/monochrome, app-icon, social-card and 128/64/32/16 favicon exports under `brand/exports/`;
- symmetric 13/13 QA contract under `brand/qa/`;
- deterministic locked-source rebuild tooling under `brand/tools/`.

The earlier large-binary transport blocker remains closed. GitHub materialization run `33730468886` verified source and destination SHA-256 values and produced materialization commit `137307351dfee467472ccd997fdc714b8a71c549`. The formerly blocked 128px favicon Git blob is `40dbc1cbca075149cd8fc4e0859f09217b0c3530`.

## Compatibility preservation

Fresh authoritative reads after merge confirm:

- `AGNIR.yaml`: Agnir Core `0.2`, `repository-filesystem/0.2`, operational release `0.2.0` at applied revision `fc84095ed5d500be9e1b43a4af0e93356571bbd4`;
- `SVIF.yaml`: Svif `0.2`, Project Binding `project-binding/0.2`, continuity provider `agnir`, compatibility/profile `0.2`;
- Project identity: `urn:svif:project:svif-core`;
- logical lineage: `urn:svif:lineage:authoritative`;
- selector: `refs/heads/main`;
- durable continuity locators unchanged.

Agnir `v1.0.0` is now latest stable, but Agnir v1 preserves valid `0.2` Projects and requires `0.2` → `1.0` to be a separately authorized Project-owned promotion. Brand integration was compatibility-neutral and neither authorized nor performed that promotion.

The immutable Svif `v0.2.0-preview.1` release tag and released Preview.1 bootstrap Core/profile `0.1` baseline were not moved or rewritten.

## Branch retirement

Svif governance requires `main` to remain the only long-lived branch.

- completed brand branch final tip: `62e9aac53246cef4eccffacb9434ead9928c0c3c`;
- archive receipt added to `history/BRANCH_ARCHIVE.md` at commit `ff3b2ce8310add5f3890a3aeb5756e272bf9b6b8`;
- one-shot retirement workflow creation: `cca67027c58136a87cf1e8fc460b63c182b88fec`;
- retirement workflow run: `34055731552`, success;
- workflow self-removal/main revision before this checkpoint: `d8b2feb546e88b6b8692078dc6536d195d0bc9c6`;
- post-run GitHub branch lookup for `brand/identity-system`: `404 Branch not found`;
- one-shot workflow path is absent from `main` after the run.

## Result

The Svif identity system is canonical, byte-exact source authority is preserved, production/QA assets are repository-resident, canonical product checks are green, compatibility remains deliberately on Agnir Core/profile `0.2`, the released Preview remains immutable, and the temporary brand branch has been retired.

No Svif brand integration gate remains open.
