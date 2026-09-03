# Svif brand production status

Date: 2026-09-03
Branch: `brand/identity-system`
Canonical Project ref remains: `main`

## Locked visual authority

The Principal-approved Today 10:42 AM Svif board remains the sole Svif-only visual authority. The byte-exact board is now committed at `brand/reference/svif-approved-reference.png` with locked SHA-256 `10ad09a3c68e7ccd84e8c50ac4aaeda2bdb1e1fee4c09899ef4215fdec18f3fd`.

The byte-exact family board is committed at `brand/reference/svif-agnir-family-approved-reference.png` with SHA-256 `4110d285243b6241ac709e750cca1815a10ca41e27c3bb15e6c94b56e57fa4fb`.

## Production model

**Fidelity-first raster production is the approved Svif delivery model.** Reviewed pure-vector reconstructions materially changed the translucent ribbon topology, folds/overlaps or particle field and remain rejected.

`brand/tools/build-production-assets.py` deterministically derives the production package from the locked source and refuses a source-board SHA mismatch.

The current raster production masters are committed directly under `brand/masters/`:

- `svif-mark.png`
- `svif-wordmark.png`
- `svif-horizontal-lockup.png`
- `svif-vertical-lockup.png`

They preserve the approved raster appearance and are not infinitely scalable vector masters. `brand/masters/candidates/svif-wordmark-trace-v0.1.svg` remains provenance only.

## Materialized delivery exports

The complete delivery set is now committed under `brand/exports/`:

- `svif-light-usage.png`
- `svif-dark-usage.png`
- `svif-monochrome-usage.png`
- `svif-app-icon.png`
- `svif-social-card.png`
- `svif-favicon-128.png`
- `svif-favicon-64.png`
- `svif-favicon-32.png`
- `svif-favicon-16.png`

All files were materialized on a GitHub runner from the user-uploaded byte-exact handoff archive. Workflow run `33730468886` verified the archive SHA-256, verified each source payload SHA-256, copied each file to its final repository path, re-verified each destination SHA-256, committed the results, and removed both the transport ZIP and the temporary workflow.

Final materialization commit: `137307351dfee467472ccd997fdc714b8a71c549`.

The previously blocked 128px favicon now proves the byte-safe path succeeded: repository Git blob `40dbc1cbca075149cd8fc4e0859f09217b0c3530`, exactly matching the locally expected Git object SHA that could not traverse the earlier direct base64 bridge.

Expected production SHA-256 values remain recorded in `brand/masters/RASTER-MASTER-MANIFEST.md`.

## Complete QA

Final QA is symmetric with Agnir and covers 13/13 items:

1. mark;
2. wordmark;
3. horizontal lockup;
4. vertical lockup;
5. light usage;
6. dark usage;
7. monochrome usage;
8. app icon;
9. favicon 128;
10. favicon 64;
11. favicon 32;
12. favicon 16;
13. social card.

Complete Svif QA sheet SHA-256: `41606509a1ab49f4c48e2f8a0affbe966cdeee256f90a0d693a6c275dc9f6cb2`.

The frozen 10:42 board remains visually authoritative over every derivative.

## Latest main reconciliation

Immediately before binary materialization, authoritative `main` had advanced to `eba1b8538c4692a08bf69452525b735d23564599` and the brand branch was behind by 7 commits.

Reverse-sync PR `#8` (`main` -> `brand/identity-system`) was mergeable and was merged into the branch at `6076dd08d3e8d352d130a6c3ac2ccddb3d28bae7` before materialization. The post-reconcile branch was behind `main` by 0.

No released `v0.2.0-preview.1` tag was moved or modified.

## Repository documentation

The `brand/` product surface is represented in `README.md`, `README.zh-CN.md`, and `REPOSITORY_TREE.md`. The latest-main reconciliation preserved newer product/runtime truth while retaining the brand-only repository-map entries.

## QA and integration rules

- Principal-facing brand review stays free of diagnostic overlays.
- Raster masters must preserve the approved translucent ribbon and particle appearance.
- Favicon review is at actual 128/64/32/16 targets.
- No derivative may become permission to redesign the locked source.
- Future pure-vector replacement requires a new clean source-vs-vector review and explicit approval.

## Integration readiness

The former large-binary preservation blocker is **closed**. Byte-exact source references, raster masters, and delivery exports are now repository-resident and SHA-verified.

Remaining publication gates are only:

1. re-resolve latest `main` immediately before publication and reconcile again if it moved;
2. require Draft PR `#5` synthetic-merge product checks to be green on the final branch head;
3. integrate the approved brand package coherently without changing the immutable `v0.2.0-preview.1` release tag;
4. fresh-verify authoritative `main` after publication.
