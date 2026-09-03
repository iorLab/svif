# Svif raster production master manifest

Status: **branch-local production record; visual authority remains the Principal-approved Today 10:42 AM Svif board.**

Source board SHA-256:

`10ad09a3c68e7ccd84e8c50ac4aaeda2bdb1e1fee4c09899ef4215fdec18f3fd`

The files below are the expected deterministic outputs of `brand/tools/build-production-assets.py`. They are fidelity-first raster masters / approved-board derivatives, not pure-vector replacements.

| Asset | Role | Native size | Expected SHA-256 |
| --- | --- | ---: | --- |
| `svif-mark.png` | raster master | 292×290 | `5895265cbf7fec4f0ef67f6ffdc10ae3622452b253325c9a66b3a04db8411f31` |
| `svif-wordmark.png` | raster master | 255×155 | `9cd52530c102af04b9fdf577efce7ebc3c2feadd2d6ef538d8c2289f28d2a927` |
| `svif-horizontal-lockup.png` | raster master | 361×200 | `273dc67eed55f8dc9c0f831989a781a44c38d8ece9b466174e45d1016b02d252` |
| `svif-vertical-lockup.png` | raster master | 208×215 | `ae7f98e723eba74cbe81126bfe29cc85c9950844d6e3603248da362982127a5d` |
| `svif-light-usage.png` | approved-board derivative | 378×140 | `72a688daeae4ee885027065e55f5c98d8d9bf2df85c096c4cdbaa643d44a5e88` |
| `svif-dark-usage.png` | approved-board derivative | 395×140 | `35733817193eb26d30cc06a834ec39311545f7cb8fc1c3c914dc48847a50856d` |
| `svif-monochrome-usage.png` | approved-board derivative | 385×140 | `b5e3f89c6874a216c06bc6a4bf4a0a67ec445db0f726187c2e94f3dab2a02449` |
| `svif-app-icon.png` | approved-board derivative | 160×155 | `11d156135d6b40313489772e03f4d20b2e67b10bb59cfee552d3aeefeef34b77` |
| `svif-social-card.png` | approved-board derivative | 395×210 | `cb78b5a2c94e61b29f50d8b303411a9e0a342e662395d1f576c8dc78340d31f3` |
| `svif-favicon-128.png` | favicon | 128×128 | `ef18af5dc8d8b5f777911437dc234f4d30a80044088514e724708499a8481685` |
| `svif-favicon-64.png` | favicon | 64×64 | `3645ec61b83c0cb2168f365b59902153eec74b5252b615eab06c92aa1ae76a97` |
| `svif-favicon-32.png` | favicon | 32×32 | `8698f84498e5cb61471e73f1fee1316b2892c5c9d1b46d283503da0594f2a2e2` |
| `svif-favicon-16.png` | favicon | 16×16 | `0f9f49ab937210fc6e73fc06b903429562ee1e26dba38b7af578cd617c5fb378` |

## Materialized binary verification

The following files are now committed directly under `brand/exports/` after byte-level Git blob verification:

| Repository file | Git blob SHA-1 | SHA-256 status |
| --- | --- | --- |
| `brand/exports/svif-favicon-64.png` | `b396a8f9f36d3b59b69e16b650675e82d666e99e` | matches table above |
| `brand/exports/svif-favicon-32.png` | `791eb44f67e6e96d55a1126bdc2fdc23b18b5050` | matches table above |
| `brand/exports/svif-favicon-16.png` | `234044b5faf1be3a6862d5c8f8548757902bc69b` | matches table above |

Git blob acceptance criterion is exact: the SHA returned by GitHub must equal the locally calculated Git object SHA for the byte sequence. A UTF-8 decoding failure when attempting to read a PNG blob as text is expected and is **not** evidence of blob corruption.

## Semantics

- Native raster dimensions are part of the master record.
- Do not label an enlarged raster export as a new native master.
- Do not substitute a regenerated S or a failed pure-vector approximation for these outputs.
- The black standalone wordmark / lockups and the teal light-background treatment are both intentional parts of the approved board; use the applicable asset for the surface.
- A future pure-vector master may supersede the raster master only after a new Principal-facing source-vs-vector fidelity review.

## Repository-binary gate

The Git binary path itself is proven for payloads that can traverse the current execution bridge intact. The current bridge truncates sufficiently long base64 tool arguments, so larger PNGs remain gated even though Git's blob API is binary-safe. Never attach a larger blob when its returned Git blob SHA differs from the locally expected Git blob SHA.
