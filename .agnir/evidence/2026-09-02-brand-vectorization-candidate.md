# Svif brand vectorization candidate — 2026-09-02

Status: **branch-local candidate evidence; not canonical until reconciled and merged to authoritative `main`.**

## Locked source

The Principal-approved Today 10:42 AM Svif board remains the sole Svif-only visual authority. Its source SHA-256 and lossless extraction coordinates are recorded in `brand/APPROVED-VISUAL-REFERENCE.md` and `brand/reference/EXTRACTION-MANIFEST.md`.

## Candidate progress

- `brand/masters/candidates/svif-wordmark-trace-v0.1.svg` remains the raster-derived trace candidate of the approved standalone wordmark.
- The candidate was tightened after direct raster comparison; it is still **not** a locked master.
- Automatic contour/quantization, superpixel/SLIC, multi-layer color-band tracing, and three-layer gradient/blur tracing were all tested against the locked primary S reference.
- Those approaches preserved the broad S silhouette but introduced visible posterization, faceting, hard layer boundaries, or particle/ribbon drift.
- They were rejected locally and were **not committed as primary-mark candidates**.

## Decision boundary

No replacement font, generic S, palette cleanup, particle redesign, or aesthetic reinterpretation is authorized. A visually drifting SVG must be rejected even when technically valid.

The failed experiments materially narrow the next acceptable reconstruction method: the ribbon should be rebuilt as a small number of constrained smooth Bézier surfaces/paths with explicit translucent overlap ordering, using the approved raster as geometry and color evidence rather than as an automatically segmented shape map.

## Next acceptable move

Continue the constrained Bézier ribbon reconstruction and visual regression of the approved S; preserve the raster derivation path for interim production use. Only after S mark + wordmark pass visual review may vector lockups and final variants be promoted.
