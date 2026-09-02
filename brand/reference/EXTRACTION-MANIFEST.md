# Svif approved-reference extraction manifest — 2026-09-02

Status: **branch-local production-preparation record**. The visual authority remains `brand/APPROVED-VISUAL-REFERENCE.md` and the Principal-approved Today 10:42 AM reference set.

## Approved source

- Source attachment: `63e7953b-4571-45fb-a233-303ec8325c78.png`
- Dimensions: `1448 × 1086`
- SHA-256: `10ad09a3c68e7ccd84e8c50ac4aaeda2bdb1e1fee4c09899ef4215fdec18f3fd`
- Applicable context: **Svif-only** usage.

The co-brand/family authority remains attachment `1d00fb70-189b-4742-b4ac-c79be2668559.png`, SHA-256 `4110d285243b6241ac709e750cca1815a10ca41e27c3bb15e6c94b56e57fa4fb`.

## Lossless raster extraction map

Coordinates are `(left, top, right, bottom)` in approved-source pixels. These crops are QA/trace references, **not independently approved redesigns or vector masters**.

| Asset role | Crop box | Size | Derived PNG SHA-256 |
| --- | --- | --- | --- |
| Primary mark | `(48, 200, 340, 490)` | `292×290` | `bac686f1ccaeb91be7ccc74b7f83698d716248f69189426dd37f9f841c5a4ab3` |
| Wordmark | `(395, 255, 650, 410)` | `255×155` | `061002aa430cdf5d199b890397cdfc4fd9a912219bb81b46e24ef23d7aa32ebb` |
| Horizontal lockup | `(704, 230, 1065, 430)` | `361×200` | `4e99ab5c84af0038166b7a83c30efe9ed52760f4536c4d4085690442add651ad` |
| Vertical lockup | `(1122, 215, 1330, 430)` | `208×215` | `281e9805f30552c6bd1c5c1846972996c13159278424b0bc979124bb1b5c2dd3` |
| Light-background example | `(40, 555, 418, 715)` | `378×160` | `c8a3eb93c4d9a0edb586961a350b12877d4dfb6d023a8916f92c626a3452f62c` |
| Dark-background example | `(470, 555, 865, 715)` | `395×160` | `950e44236464f6737d7218ce24bef32266e33eb6cc4b51bd17c07a89c1021413` |
| Monochrome example | `(965, 555, 1350, 715)` | `385×160` | `ead7488542fd0dd2d13ebaf549d936d08042d1f097cd666d988c189d4e932efd` |
| App-icon example | `(28, 782, 188, 955)` | `160×173` | `c5a5110f74d53e1ec5454850333799759d6b35d909f1ac84ae4e6189a3eb5612` |
| Social-card example | `(545, 785, 940, 995)` | `395×210` | `3c38515e06862554f17c84228c05938911e0a94e06efb276e542a7c21e8de6fc` |

## Production rule

1. Reconstruct from the applicable approved board and these lossless crop references.
2. Do not substitute a regenerated image, generic `S`, different typeface, reconciled palette, or redesigned particle field.
3. Vectorization must be reviewed against the source crop before it can become a master.
4. The board is raster evidence; a crop's displayed pixel dimensions do not imply that the board contains a true 512px/128px source asset merely because the board labels one that way.
5. No upscaled crop may be represented as a genuine higher-resolution master.

## Binary-preservation boundary

The active GitHub connector on this execution surface exposes repository UTF-8 content writes but no local-file/binary upload action. Therefore the byte-exact source PNG and crop PNGs have been preserved in the current locked reference package and identified here by hashes, but are **not falsely claimed to be committed binary repository files**. A Git-capable/binary-upload execution surface should add the byte-exact approved source to `brand/reference/` before final `main` integration. Until then, never replace the source with a generated lookalike.
