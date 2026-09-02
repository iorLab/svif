# Svif brand production / vectorization evidence — 2026-09-02

Status: **branch-local candidate continuity; not canonical until reconciled and merged to authoritative `main`.**

## Locked source

The Principal-approved Today 10:42 AM Svif board remains the sole Svif-only visual authority. Its source SHA-256 and extraction coordinates are recorded in `brand/APPROVED-VISUAL-REFERENCE.md`, `brand/reference/EXTRACTION-MANIFEST.md`, and `brand/masters/RASTER-MASTER-MANIFEST.md`.

## Vectorization finding

Multiple pure-vector reconstruction strategies were tested against the approved S:

- automatic contour / quantization;
- superpixel / SLIC;
- multi-layer color-band tracing;
- gradient / blur tracing;
- centerline Bézier stroke;
- constrained closed Bézier ribbon surfaces.

Each materially changed some combination of the approved translucency, fold topology, ribbon-width variation, overlap ordering, particle trajectories, or edge softness. Those approaches were rejected; none is authorized as the Svif production mark.

The old `brand/masters/candidates/svif-wordmark-trace-v0.1.svg` remains provenance only and is not a production master.

## Production decision

Delivery must not be blocked merely to obtain a nominally vector file. The current accepted engineering path is **fidelity-first raster production**:

- verify the exact approved source-board SHA-256;
- deterministically crop the approved assets;
- recover transparent mark / wordmark / lockups from the white presentation matte;
- preserve the approved-board light / dark / monochrome, app-icon and social-card treatments;
- derive real target-size favicons;
- record SHA-256 values and native dimensions for every output.

`brand/tools/build-production-assets.py` implements this path. `brand/masters/RASTER-MASTER-MANIFEST.md` records the expected output hashes.

## Semantics boundary

The resulting PNGs are raster production masters / approved-board derivatives. They must not be described as infinitely scalable vectors. An SVG wrapper, if later supplied, is only a container around raster artwork and does not change that semantic.

A future pure-vector replacement is allowed only if it passes a new source-vs-vector fidelity review; format preference cannot override the frozen visual authority.

## Binary write boundary

The current connector path has demonstrated truncation risk for sufficiently long base64 binary payloads. Unverified binary blobs are therefore not attached to the branch. Add actual PNG binaries only through a binary-safe Git path and verify them against the recorded SHA-256 values afterward.

## Next acceptable move

Complete the Svif production handoff/package using the deterministic raster outputs, verify actual-size favicon/app/social surfaces, add verified binaries through a safe Git path, then reconcile this branch-local decision into the latest canonical `main` during integration.
