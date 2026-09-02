# Svif brand master v0.1 candidate — 2026-09-02

Status: **branch-local candidate evidence; not canonical until reconciled and merged to authoritative `main`**.

## Candidate created

The selected 01 + 03 + 05 brand direction has been reconstructed as deterministic vector candidates on `brand/identity-system`:

- `brand/masters/svif-mark-v0.1.svg` — primary teal S-ribbon + particle mark;
- `brand/masters/svif-mark-small-v0.1.svg` — simplified small-size S variant;
- `brand/masters/MASTER-SPEC-v0.1.md` — exact candidate palette, geometry, and remaining lock gates.

The selected concept-board appearance remains the visual reference; the SVG is a reconstruction candidate rather than proof of exact pixel-for-pixel identity with an image-generation output.

## Candidate palette

- light: `#75CCC8` / RGB `117, 204, 200`;
- mid: `#13AEAC` / RGB `19, 174, 172`;
- dark: `#016F6C` / RGB `1, 111, 108`.

These values were sampled from the Principal-selected concept board. They are deterministic candidate values, not yet locked brand invariants.

## Preliminary rendering QA

The vector candidate was rasterized at `64px`, `32px`, and `16px` in the current work environment.

Observed result:

- the stable S silhouette remains recognizable at all tested sizes;
- particle detail materially degrades at favicon scale;
- a separate small-size variant preserves the same S centerline while removing particle detail rather than silently changing the primary master;
- preliminary recommendation is primary at `64px+`, small variant preferred at `32px`, required at `16px`, pending Principal approval.

## Boundaries

- No README, Plugin listing, favicon, PWA, social, or other production integration is authorized by this candidate.
- Wordmark/font geometry is unresolved and is not inferred from the concept-board typography.
- Monochrome, reverse/dark-background, transparency, clear-space, and final lockup QA remain open.
- This file is candidate evidence only. Before merge, selected durable conclusions must be reconciled against the latest `main` Agnir truth; the branch-local `.agnir/state.md`, `.agnir/decisions.md`, and `.agnir/next-actions.md` are not being forked for brand work.
