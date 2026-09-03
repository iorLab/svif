# Svif approved-reference extraction manifest — 2026-09-03

Status: **branch-local production record**. The visual authority remains `brand/APPROVED-VISUAL-REFERENCE.md` and the Principal-approved Today 10:42 AM reference set.

## Approved source

- Original attachment: `63e7953b-4571-45fb-a233-303ec8325c78.png`
- Repository path: `brand/reference/svif-approved-reference.png`
- Dimensions: `1448 × 1086`
- SHA-256: `10ad09a3c68e7ccd84e8c50ac4aaeda2bdb1e1fee4c09899ef4215fdec18f3fd`
- Applicable context: **Svif-only** usage.

Co-brand/family authority:

- Original attachment: `1d00fb70-189b-4742-b4ac-c79be2668559.png`
- Repository path: `brand/reference/svif-agnir-family-approved-reference.png`
- Dimensions: `1448 × 1086`
- SHA-256: `4110d285243b6241ac709e750cca1815a10ca41e27c3bb15e6c94b56e57fa4fb`

Both files were byte-exactly materialized and SHA-verified by GitHub Actions run `33730468886` before commit `137307351dfee467472ccd997fdc714b8a71c549`.

## Production extraction map

The active production builder uses the reviewed final crop/extraction coordinates defined in `brand/tools/build-production-assets.py`. Those coordinates and the expected native production output hashes are operationally frozen by `brand/masters/RASTER-MASTER-MANIFEST.md`; the committed production masters/exports are the byte-exact outputs of that approved path.

The older crop experiments recorded during vectorization review are provenance only and must not override the production builder or raster-master manifest.

## Production rule

1. Rebuild only from `brand/reference/svif-approved-reference.png` or another byte-identical copy with the same locked SHA-256.
2. Do not substitute a regenerated image, generic `S`, different typeface, reconciled palette or redesigned particle field.
3. The approved board is raster visual authority; labels such as 512px/128px on the specimen board do not imply an independent higher-resolution native source.
4. No upscale may be represented as a genuine higher-resolution master.
5. Vectorization may supersede current raster masters only after a new clean source-vs-vector review and explicit Principal approval.

## Binary-preservation status

The former binary-preservation gate is **closed** for the brand branch. Both approved reference PNGs are repository-resident, and the complete raster production package is committed under `brand/masters/` and `brand/exports/` after source/destination SHA verification on the GitHub runner.
