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

## Binary repository boundary

The active GitHub connector can create Git binary blobs from base64, but the execution bridge truncates sufficiently long local binary payloads before they can be safely attached to a tree. Corrupt/unverified blobs are therefore **not** attached to the branch.

The production builder, exact source SHA, crop rules and output hashes are persisted in-repository. Current binary outputs are preserved in the local production package. Actual PNG binaries must be added only through a binary-safe Git surface or a verified repository workflow; never attach an unverified/truncated blob merely to claim the binary was committed.

## QA rules

- Principal-facing review is clean; diagnostics do not appear in brand artwork.
- Every raster master must recompose correctly on white and preserve the approved translucent ribbon / particles.
- Favicon QA is performed at actual 128 / 64 / 32 / 16 sizes.
- The frozen 10:42 AM board remains visually authoritative over all derived files.

## Next actions

1. Persist the raster-master file map and current output hashes.
2. Write `brand/brand-handoff.md` describing raster-master semantics, usage and limitations.
3. Package Svif mark / wordmark / lockups / variants / app / favicon / social derivatives for delivery.
4. Add byte-exact binaries to repository storage only through a binary-safe path and verify their SHA-256 values afterward.
5. Re-resolve latest `main`, reconcile branch-local Agnir continuity, then integrate the approved brand package coherently.
