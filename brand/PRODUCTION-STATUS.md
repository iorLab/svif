# Svif brand production status

Date: 2026-09-02
Branch: `brand/identity-system`
Canonical Project ref remains: `main`

## Locked input

The Principal-approved Today 10:42 AM Svif board is the sole Svif-only visual authority. See `APPROVED-VISUAL-REFERENCE.md` and `reference/EXTRACTION-MANIFEST.md`.

## Fidelity finding

Repeated reviewed attempts to convert the Svif S into a conventional pure-vector mark changed material features of the approved artwork:

- contour / quantization / SLIC introduced posterization;
- color-band and gradient/blur tracing introduced hard facets;
- a centerline Bézier stroke changed the ribbon topology;
- closed-surface Bézier experiments still failed to reproduce the approved translucent fold / overlap structure closely enough.

Those experiments remain rejected. No approximate S may be promoted merely to satisfy a file-format preference.

## Current production path

**Fidelity-first raster production is the active delivery path for Svif.**

`brand/tools/build-production-assets.py` verifies the exact approved board SHA-256 and deterministically derives:

- transparent native-resolution raster mark;
- transparent standalone wordmark;
- transparent horizontal lockup;
- transparent vertical lockup;
- approved-board light / dark / monochrome usage derivatives;
- approved app-icon derivative;
- approved social-card derivative;
- 128 / 64 / 32 / 16 favicon derivatives;
- SHA-256 manifest for every output.

This is not a redesign. It is a deterministic extraction of the frozen visual authority.

### Master semantics

- The extracted native-resolution PNGs are **raster production masters** for the current approved Svif appearance.
- They must not be described as infinitely scalable vector masters.
- An SVG wrapper around a raster master, if supplied, is a transport/convenience container only; it does not convert the artwork into true vector geometry.
- No upscale may be represented as a native-resolution source master.
- A future pure-vector reconstruction is allowed only if it passes a new source-vs-vector fidelity review. It is no longer allowed to block delivery of the approved brand package.

## Wordmark

The old `brand/masters/candidates/svif-wordmark-trace-v0.1.svg` remains provenance only. The raster-extracted approved wordmark is preferred for fidelity-first production until a separately reviewed smooth outline is demonstrated to match the locked source.

## Materialized repository binaries

The Git binary path has now been verified end-to-end for payloads that fit through the current execution bridge. The following delivery files are directly committed under `brand/exports/`:

- `svif-favicon-64.png` — Git blob `b396a8f9f36d3b59b69e16b650675e82d666e99e`;
- `svif-favicon-32.png` — Git blob `791eb44f67e6e96d55a1126bdc2fdc23b18b5050`;
- `svif-favicon-16.png` — Git blob `234044b5faf1be3a6862d5c8f8548757902bc69b`.

For each file, GitHub's returned blob SHA matched the locally calculated Git object SHA exactly, and its SHA-256 matches `brand/masters/RASTER-MASTER-MANIFEST.md`.

A failed attempt to read a PNG Git blob as UTF-8 is expected for binary content and is not evidence of corruption. The actual remaining limitation is the current execution bridge's long-base64 argument truncation: sufficiently large PNG payloads cannot traverse this bridge intact even though Git's blob API itself is binary-safe.

Therefore the larger mark / wordmark / lockups / treatment / app / 128px favicon / social PNGs remain deterministic builder outputs rather than falsely attached truncated binaries.

## QA status

Final local production QA has been run across:

- mark and wordmark;
- horizontal and vertical lockups;
- light / dark / monochrome treatments;
- app icon;
- 128 / 64 / 32 / 16 favicon targets;
- social-card composition.

The QA set preserves the approved translucent ribbon, particle trajectories and locked 10:42 composition. The complete local delivery package has also been generated with output manifests/hashes.

## QA rules

- Principal-facing review is clean; diagnostics do not appear in brand artwork.
- Every raster master must recompose correctly on white and preserve the approved translucent ribbon / particles.
- Favicon QA is performed at actual 128 / 64 / 32 / 16 sizes.
- The frozen 10:42 AM board remains visually authoritative over all derived files.

## Remaining integration gates

1. Preserve the byte-exact approved Svif board in repository storage.
2. Attach the larger deterministic PNG outputs through a binary transport that preserves exact bytes, then verify their Git blob SHA and documented SHA-256.
3. Re-resolve latest `main` and reconcile branch-local Agnir continuity.
4. Integrate the approved brand package coherently without changing the released `v0.2.0-preview.1` tag.
5. Verify the resulting authoritative `main` after publication.
