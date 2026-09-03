# Svif production exports

Svif uses a fidelity-first raster production model because reviewed pure-vector reconstructions materially changed the approved translucent ribbon topology.

## Repository-resident exports

The complete approved delivery set is now committed directly under this directory:

- `svif-light-usage.png`
- `svif-dark-usage.png`
- `svif-monochrome-usage.png`
- `svif-app-icon.png`
- `svif-social-card.png`
- `svif-favicon-128.png`
- `svif-favicon-64.png`
- `svif-favicon-32.png`
- `svif-favicon-16.png`

Core raster masters live separately under `brand/masters/`.

All binary files were materialized through GitHub Actions run `33730468886`. The run verified the uploaded handoff archive SHA-256, verified every source payload SHA-256, copied each payload to its final repository path and re-verified every destination before commit `137307351dfee467472ccd997fdc714b8a71c549`.

The 128px favicon now has repository Git blob `40dbc1cbca075149cd8fc4e0859f09217b0c3530`, matching the expected Git object SHA exactly.

## Deterministic rebuild

The package can be reproduced from the byte-exact committed source board with:

```bash
python brand/tools/build-production-assets.py \
  --board brand/reference/svif-approved-reference.png \
  --out <output-directory>
```

The builder validates the locked source SHA-256. Expected output SHA-256 values are recorded in `brand/masters/RASTER-MASTER-MANIFEST.md`.

## Rules

- Do not replace committed assets with regenerated or approximate artwork.
- Do not call raster assets infinitely scalable vector masters.
- Do not substitute a generic S or similar typeface.
- Preserve the approved light/dark/monochrome, app-icon, favicon and social-card compositions.
- Any future pure-vector replacement requires a new explicit fidelity approval.
