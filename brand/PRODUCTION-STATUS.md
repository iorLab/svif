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
- Multi-layer color-band and three-layer gradient/blur traces retained the S silhouette and particle direction but introduced visible faceting / hard layer boundaries. They were rejected locally and not committed as candidates.
- A constrained smooth Bézier-centerline reconstruction was also tested. It removed segmentation faceting, but failed a more fundamental fidelity test: the approved Svif mark is **not representable as one centerline with progressively thicker strokes**. Its ribbon has surface width changes, distinct upper/lower edge trajectories, fold/overlap ordering, and crossing geometry. A stroke-derived S therefore changes the topology and reads as a different mark. This experiment was rejected locally and not committed.
- The next vector strategy is now constrained further: reconstruct the Svif mark as a small set of **closed Bézier ribbon surfaces** (front/back translucent sheets) with independently traced inner/outer boundaries and explicit overlap masks, then add particles from the locked raster evidence.
- Raster primary/lockup derivation remains the only currently accepted faithful production path for the Svif mark.
- Vector lockups and final variants remain blocked until the primary mark and wordmark pass the master gate.

The quality rule remains: **absence of a vector master is preferable to a visually drifting vector master.**

## Binary reference boundary

The byte-exact approved board and crop PNGs remain preserved by SHA-256 and in the locked local reference package. The current connector does not provide a practical local-file binary upload bridge for the multi-megabyte exact approved PNG, so final byte-exact repository preservation remains a pre-`main` integration gate.

## Next actions

1. Trace the Svif ribbon as separate closed Bézier surfaces using the approved upper/lower boundaries, not a centerline stroke.
2. Reconstruct front/back overlap ordering and translucency with masks/gradients that reproduce the approved crossing rather than merely approximating an S silhouette.
3. Preserve particle trajectories as a separate evidence-derived layer.
4. Run visual regression on the wordmark candidate and revise only demonstrated mismatch.
5. Use `brand/tools/derive-raster-assets.py` for interim transparent/icon derivatives; preserve native/upscale metadata.
6. Reconstruct horizontal/vertical vector lockups only after the S mark and wordmark are accepted masters.
7. Build light/dark/monochrome vector variants only from locked masters and approved examples.
8. Before final integration, preserve the byte-exact approved source in repository storage, re-resolve latest `main`, reconcile Agnir continuity, and integrate coherently.
