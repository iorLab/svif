# Svif brand production status

Date: 2026-09-02
Branch: `brand/identity-system`
Canonical Project ref remains: `main`

## Locked input

The Principal-approved Today 10:42 AM Svif board is the sole Svif-only visual authority. See `APPROVED-VISUAL-REFERENCE.md` and `reference/EXTRACTION-MANIFEST.md`.

## Completed

- concept exploration ended;
- approved visual reference locked by exact source SHA-256;
- rejected deterministic v0.1 reconstruction removed from the active branch;
- lossless source-board crops prepared for primary mark, wordmark, horizontal/vertical lockups, light/dark/monochrome examples, app-icon example, and social-card example;
- crop coordinates and derived hashes persisted for reproducible trace/QA;
- `brand/masters/candidates/svif-wordmark-trace-v0.1.svg` remains the standalone wordmark review candidate;
- `brand/tools/derive-raster-assets.py` provides a deterministic white-matte extraction path for approved white-background crops, producing transparent PNG derivatives plus a SHA-256 manifest;
- local raster QA preserves the approved Svif appearance on white and at 128/64/32/16 target sizes;
- multiple primary-mark vectorization approaches have now been tested locally without being allowed to pollute the branch candidate set when they fail fidelity review.

## Current production gate

**Faithful vectorization remains the master gate.**

A vector master may be accepted only when it is reconstructed from the approved crop and visually compared with that crop. No new image generation, generic S replacement, typography substitution, palette reconciliation, or aesthetic cleanup is allowed.

The raster derivation tool is an interim/reproducible production path, not permission to redefine the master. It exists so the exact approved appearance can be used without waiting for an inferior SVG reconstruction.

### Candidate status

- Wordmark trace: **candidate only**. Geometry is derived from the locked raster reference and remains usable for review.
- Primary S mark: **still blocked from vector-master promotion**.
- Automatic contour/quantization and superpixel/SLIC experiments preserve the broad silhouette but visibly posterize the translucent ribbon.
- A new multi-layer color-band trace and a new three-layer gradient/blur trace were also tested against the locked primary-mark crop. Both retained the S silhouette and particle direction but introduced visible faceting / hard layer boundaries in the ribbon. They were rejected locally and **not committed as candidates**.
- This narrows the next reconstruction strategy: stop increasing automatic segmentation complexity and instead rebuild the ribbon as a small number of constrained smooth Bézier surfaces/paths, using the approved raster only as geometry/color evidence.
- Raster primary/lockup derivation remains the only currently accepted faithful production path for the Svif mark.
- Vector lockups and final variants remain blocked until the primary mark and wordmark pass the master gate.

The quality rule remains: **absence of a vector master is preferable to a visually drifting vector master.**

## Binary reference boundary

The byte-exact approved board and crop PNGs remain preserved by SHA-256 and in the locked local reference package. The current connector does not provide a practical local-file binary upload bridge for the multi-megabyte exact approved PNG, so final byte-exact repository preservation remains a pre-`main` integration gate.

## Next actions

1. Rebuild the Svif S as constrained smooth Bézier ribbon surfaces instead of another automatic segmentation trace.
2. Preserve the approved semi-transparent overlap ordering and particle trajectories; do not simplify them merely to make the SVG easier.
3. Run visual regression on the wordmark candidate and revise only demonstrated mismatch.
4. Use `brand/tools/derive-raster-assets.py` for interim transparent/icon derivatives; preserve native/upscale metadata.
5. Reconstruct horizontal/vertical vector lockups only after the S mark and wordmark are accepted masters.
6. Build light/dark/monochrome vector variants only from locked masters and approved examples.
7. Before final integration, preserve the byte-exact approved source in repository storage, re-resolve latest `main`, reconcile Agnir continuity, and integrate coherently.
