# Svif production exports

Svif uses a fidelity-first raster production model because reviewed pure-vector reconstructions materially changed the approved translucent ribbon topology.

## Directly committed binaries

The branch currently materializes these delivery-safe favicon PNGs directly:

- `svif-favicon-16.png`
- `svif-favicon-32.png`
- `svif-favicon-64.png`

Each was uploaded through Git's binary blob API and accepted only after the returned Git blob SHA matched the locally computed Git blob SHA exactly. Their SHA-256 values also match `brand/masters/RASTER-MASTER-MANIFEST.md`.

## Larger assets

The larger mark, wordmark, lockups, treatments, app icon, 128px favicon and social card remain deterministic outputs of:

```bash
python brand/tools/build-production-assets.py \
  --board <byte-exact-approved-Svif-board.png> \
  --out <output-directory>
```

The builder validates the locked source-board SHA-256 and the expected output hashes. The current execution bridge has a long-base64 payload limit, so larger PNG files are not attached through that bridge unless their exact Git blob integrity can be verified.

Do not replace missing larger binaries with regenerated or approximate artwork merely to populate a path.
