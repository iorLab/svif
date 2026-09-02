# Svif brand production candidate — 2026-09-02

Status: **branch-local evidence; not canonical until reconciled and integrated into authoritative `main`.**

## Locked authority

The Principal-approved Today 10:42 AM Svif asset board remains the sole Svif-only visual authority. Production work in this branch does not authorize a regenerated S, replacement wordmark, palette cleanup or ribbon simplification.

## Fidelity-first production decision

Reviewed pure-vector approaches materially changed the approved translucent ribbon topology, fold/overlap structure or particle field. They were rejected. Delivery therefore uses deterministic raster extraction from the locked approved board rather than accepting a visually drifting SVG merely for format preference.

`brand/tools/build-production-assets.py` validates the approved source SHA-256 and deterministically creates the native raster masters and approved-board derivatives recorded in `brand/masters/RASTER-MASTER-MANIFEST.md`.

## Binary materialization evidence

Git's binary blob API was tested with exact Git-object verification. The following repository binaries are directly committed under `brand/exports/`:

- `svif-favicon-64.png` — Git blob `b396a8f9f36d3b59b69e16b650675e82d666e99e`;
- `svif-favicon-32.png` — Git blob `791eb44f67e6e96d55a1126bdc2fdc23b18b5050`;
- `svif-favicon-16.png` — Git blob `234044b5faf1be3a6862d5c8f8548757902bc69b`.

For each, the GitHub-returned blob SHA matched the locally calculated Git object SHA exactly and the SHA-256 matches the production manifest.

A PNG failing UTF-8 decoding is normal binary behavior and is not evidence of corruption. The actual active limitation is the current execution bridge's long-base64 argument truncation. Larger PNG payloads must not be attached unless the returned Git blob SHA matches the locally expected SHA exactly.

## QA

Final local production QA was run across the mark, wordmark, horizontal/vertical lockups, light/dark/monochrome treatments, app icon, 128/64/32/16 favicon targets and social-card composition. The locked translucent S and particle appearance remain the visual authority.

## Remaining integration boundary

Before canonical `main` integration:

1. preserve the byte-exact approved Svif board in repository storage;
2. attach the remaining larger deterministic PNG outputs through a byte-preserving transport and verify Git blob SHA plus documented SHA-256;
3. re-resolve latest `main` and reconcile branch-local continuity;
4. integrate coherently without changing the immutable released `v0.2.0-preview.1` tag;
5. verify authoritative `main` after publication.
