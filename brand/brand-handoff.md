# Svif brand handoff

Status: **approved visual direction on `brand/identity-system`; branch-local until integrated into authoritative `main`.**

Visual authority: the Principal-approved Today 10:42 AM Svif asset board recorded in `APPROVED-VISUAL-REFERENCE.md`.

## Brand idea

Svif is the **Motion Layer / 流动层**.

- 流动、悬浮、跨表面编排
- Flow, suspension, orchestration across surfaces

The identity is a translucent teal/turquoise `S` ribbon with suspended particle trajectories. Svif is distinct from Agnir while sharing the family particle-and-geometry language.

## Production-master model

The approved S artwork contains translucent ribbon sheets, soft overlaps and particle trails that did not survive reviewed pure-vector reconstruction faithfully.

Therefore current production uses **fidelity-first raster masters** generated from the locked approved board by:

```bash
python brand/tools/build-production-assets.py \
  --board <byte-exact-approved-Svif-board.png> \
  --out <output-directory>
```

The builder refuses a board whose SHA-256 does not match the locked approved source.

Expected output hashes are recorded in `brand/masters/RASTER-MASTER-MANIFEST.md`.

### Core raster masters

- `svif-mark.png` — transparent approved S + particles, native 292×290.
- `svif-wordmark.png` — transparent approved standalone black wordmark, native 255×155.
- `svif-horizontal-lockup.png` — transparent approved mark + black wordmark, native 361×200.
- `svif-vertical-lockup.png` — transparent approved vertical composition, native 208×215.

These files preserve the approved visual but are **not infinitely scalable vectors**. Do not upscale them and call the result a new native master.

## Approved treatments

### Light background

Use the teal/brand-colored wordmark treatment shown in the approved light-background example. Do not assume the standalone black wordmark means all light-background placements must be black.

### Dark background

Use the approved translucent mark treatment with a white wordmark on the dark teal surface.

### Monochrome

Use the approved grayscale ribbon / particle treatment with a black wordmark.

The builder emits exact approved-board derivatives for these three usage examples.

## App / repository / avatar usage

- App icon: use the approved rounded-square treatment.
- Repository icon / profile avatar: prefer the mark-only treatment with clear space.
- Do not force the full wordmark into very small avatars.

## Favicons

The builder derives 128 / 64 / 32 / 16px transparent favicon files from the approved raster mark.

Directly committed delivery binaries currently exist for:

- `brand/exports/svif-favicon-64.png`;
- `brand/exports/svif-favicon-32.png`;
- `brand/exports/svif-favicon-16.png`.

These three were accepted only after exact Git object-SHA verification and their SHA-256 values match `RASTER-MASTER-MANIFEST.md`.

- Do not regenerate the S for small sizes.
- Do not substitute a generic letter `S`.
- Evaluate the actual raster target, not an enlarged preview.
- A future special small-size vector variant would require explicit new Principal approval; none is currently authorized.

## Social card

The approved board defines the Svif social-card composition: translucent S on the left, black `Svif`, `流动层 / Motion Layer`, bilingual motion copy and the light teal particle/ribbon field along the lower edge. Preserve that composition rather than inventing a campaign variant.

## Pure-vector status

Pure-vector reconstruction remains optional future work, not a delivery gate. The following approaches were rejected because they materially drifted from the approved S:

- automatic contour / quantization;
- SLIC / superpixel tracing;
- layered color-band tracing;
- gradient/blur tracing;
- centerline stroke reconstruction;
- constrained closed Bézier ribbon surfaces tested so far.

A future vector master may replace the raster production master only after a clean source-vs-vector fidelity review and explicit approval.

## Forbidden substitutions

Do not:

- regenerate the Logo with image generation and use the result as an asset;
- replace the S with a generic glyph;
- replace the wordmark with a merely similar font;
- simplify ribbon folds or particle trajectories for convenience;
- recolor Agnir/Svif into one palette;
- represent an SVG wrapper around a PNG as a true vector master;
- treat the rejected deterministic v0.1 reconstruction or current wordmark trace candidate as production truth.

## Binary repository boundary

Git's binary blob path is proven. The active execution bridge, however, truncates sufficiently long base64 tool arguments. Therefore only binaries whose returned Git blob SHA exactly matches the locally expected Git object SHA may be attached.

The 16/32/64px favicons pass this gate and are committed. Larger files remain deterministic outputs of `build-production-assets.py` until a larger-payload binary transport is available. Never populate missing paths with approximate or regenerated artwork.

## QA / delivery status

A final clean production QA has been completed locally for the core raster masters, lockups, three approved treatments, app icon, all favicon targets and social card. A complete local delivery package with manifests has been generated. This local package is a delivery artifact; repository truth remains the locked reference, builder, hashes and files actually committed to the branch.

## Integration gate

Before merging brand work to canonical `main`:

1. preserve the byte-exact approved board in repository storage;
2. add the remaining larger generated PNG package through a byte-preserving transport and verify all SHA-256 / Git blob values;
3. re-resolve latest `main` and reconcile branch-local Agnir continuity;
4. integrate assets and continuity coherently;
5. verify from `main` after publication.
