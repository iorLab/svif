# Svif brand handoff

Status: **approved and production-materialized on `brand/identity-system`; branch-local until integrated into authoritative `main`.**

Visual authority: the Principal-approved Today 10:42 AM Svif asset board.

## Brand idea

Svif is the **Motion Layer / 流动层**: flow, suspension and orchestration across surfaces. The identity is the approved translucent teal/turquoise `S` ribbon with suspended particle trajectories.

## Repository-resident visual references

Use these byte-exact references when source comparison is required:

- `brand/reference/svif-approved-reference.png`
- `brand/reference/svif-agnir-family-approved-reference.png`

Their SHA-256 locks are recorded in `brand/APPROVED-VISUAL-REFERENCE.md` and `brand/reference/EXTRACTION-MANIFEST.md`.

## Production-master model

Svif uses **fidelity-first raster masters** because reviewed pure-vector attempts materially changed the approved translucent ribbon topology, folds/overlaps or particle field.

Committed raster masters:

```text
brand/masters/
├── svif-mark.png
├── svif-wordmark.png
├── svif-horizontal-lockup.png
└── svif-vertical-lockup.png
```

These are native raster production masters for the approved appearance. Do not upscale them and call the result a new native source master. A future vector replacement requires a new source-vs-vector fidelity review and explicit approval.

`brand/tools/build-production-assets.py` remains the deterministic rebuild path and validates the locked source SHA-256. Expected output hashes are in `brand/masters/RASTER-MASTER-MANIFEST.md`.

## Approved treatments and delivery exports

The full repository-resident delivery set is under `brand/exports/`:

- light / dark / monochrome approved treatments;
- approved app icon;
- approved social card;
- favicons at 128 / 64 / 32 / 16px.

Use the actual committed files rather than regenerating a generic S, substitute typeface, simplified ribbon or redesigned particle field.

### Light background

Use the approved teal/brand-color wordmark treatment shown by the locked board.

### Dark background

Use the approved translucent mark treatment with white wordmark on the dark teal surface.

### Monochrome

Use the approved grayscale ribbon/particle treatment with black wordmark.

### Favicons

Do not regenerate the S for small sizes. Evaluate the actual raster target at 128/64/32/16px.

## Social card

Preserve the locked composition: translucent S, black `Svif`, `流动层 / Motion Layer`, bilingual copy and the light teal particle/ribbon field. Do not invent a campaign redesign.

## Forbidden substitutions

Do not:

- replace the S with a generic glyph;
- replace the wordmark with a merely similar font;
- simplify ribbon folds or particle trajectories;
- reconcile Agnir and Svif into one palette;
- represent an SVG wrapper around a PNG as a true vector master;
- promote rejected v0.1/vectorization candidates;
- use image generation to create a replacement production logo.

## Byte-exact materialization receipt

The former large-binary transport blocker is closed. GitHub Actions run `33730468886` verified the handoff archive and every source/destination SHA-256 before committing the complete repository package at `137307351dfee467472ccd997fdc714b8a71c549`. The temporary transport ZIP and workflow removed themselves in that commit.

## Integration gate

Before canonical `main` integration:

1. re-resolve latest `main` and reconcile if it moved;
2. require Draft PR `#5` product checks to pass on the final head;
3. integrate brand assets/evidence coherently without moving `v0.2.0-preview.1`;
4. fresh-verify the resulting authoritative `main`.
