# Svif approved-reference extraction manifest — 2026-09-02

Status: **branch-local production-preparation record**. The visual authority remains `brand/APPROVED-VISUAL-REFERENCE.md` and the Principal-approved Today 10:42 AM reference set.

## Approved source

- Source attachment: `63e7953b-4571-45fb-a233-303ec8325c78.png`
- Dimensions: `1448 × 1086`
- SHA-256: `10ad09a3c68e7ccd84e8c50ac4aaeda2bdb1e1fee4c09899ef4215fdec18f3fd`
- Applicable context: **Svif-only** usage.

The co-brand/family authority remains attachment `1d00fb70-189b-4742-b4ac-c79be2668559.png`, SHA-256 `4110d285243b6241ac709e750cca1815a10ca41e27c3bb15e6c94b56e57fa4fb`.

## Final lossless raster extraction map

Coordinates are `(left, top, right, bottom)` in approved-source pixels. These final crops were visually inspected to exclude board headings/dividers where practical. They are QA/trace references, **not independently approved redesigns or vector masters**.

| Asset role | Crop box | Size | Derived PNG SHA-256 |
| --- | --- | --- | --- |
| Primary mark | `(48, 215, 350, 495)` | `302×280` | `cd683b233d6e8062ef83b6ab63ebcf36890ce0c8e08eb3a3d56ad07faff83d81` |
| Wordmark | `(390, 265, 660, 410)` | `270×145` | `bffe9bc869a175b67145313381bd3e0372d51801bb727b90a27ce6d59bb31a6b` |
| Horizontal lockup | `(710, 240, 1065, 430)` | `355×190` | `faa4a6bd9945aa80256753b479be61c43da0bf3fd1298e235bd5c117ad97a6a0` |
| Vertical lockup | `(1130, 220, 1335, 430)` | `205×210` | `8299229989ebb9831253c29947790d443868997c35973e211727bc5ed6ce87bb` |
| Light-background example | `(38, 570, 420, 715)` | `382×145` | `34790425ef8b5631d30e63dd2a4102801b2ab81d02e8b072ea85858292859f97` |
| Dark-background example | `(468, 570, 868, 715)` | `400×145` | `3889633363fa7e3761a27e41793a69cbce4ef412ebf3127034ce5169f120103b` |
| Monochrome example | `(955, 570, 1365, 715)` | `410×145` | `58515a39e8eb86a7c06ab910416b0edd843cf82fb15d98895eb135ab02881774` |
| App-icon example | `(28, 795, 190, 960)` | `162×165` | `28ed540c3da6cae99adac870d0412d265549c4b9495084d8455ce05fbc5fb2fc` |
| Social-card example | `(545, 785, 940, 995)` | `395×210` | `3c38515e06862554f17c84228c05938911e0a94e06efb276e542a7c21e8de6fc` |

## Production rule

1. Reconstruct from the applicable approved board and these lossless crop references.
2. Do not substitute a regenerated image, generic `S`, different typeface, reconciled palette, or redesigned particle field.
3. Vectorization must be reviewed against the source crop before it can become a master.
4. The board is raster evidence; a crop's displayed pixel dimensions do not imply that the board contains a true 512px/128px source asset merely because the board labels one that way.
5. No upscaled crop may be represented as a genuine higher-resolution master.

## Binary-preservation boundary

The active GitHub connector on this execution surface exposes repository UTF-8 content writes but no local-file/binary upload action. Therefore the byte-exact source PNG and crop PNGs have been preserved in the current locked reference package and identified here by hashes, but are **not falsely claimed to be committed binary repository files**. A Git-capable/binary-upload execution surface should add the byte-exact approved source to `brand/reference/` before final `main` integration. Until then, never replace the source with a generated lookalike.
