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

A deliberate 128px boundary probe confirmed the limitation rather than weakening it:

- source: `svif-favicon-128.png`, 12,183 bytes;
- locally expected Git object SHA: `40dbc1cbca075149cd8fc4e0859f09217b0c3530`;
- GitHub-returned blob SHA through the current bridge: `30eb8689852c6490c0e2e19d3ff39cb4269b1700`;
- result: **SHA mismatch; rejected and never attached to the branch tree**.

This proves the current transport is reliable for the verified <=4KB examples above but not for the tested 12KB payload. No larger binary will be attached through this path without exact Git-object equality.

## Complete QA

The earlier production review scope has been normalized to the same 13-item final QA contract used for Agnir:

1. mark;
2. wordmark;
3. horizontal lockup;
4. vertical lockup;
5. light usage;
6. dark usage;
7. monochrome usage;
8. app icon;
9. favicon 128;
10. favicon 64;
11. favicon 32;
12. favicon 16;
13. social card.

The locked translucent S and particle appearance remain the visual authority. `brand/qa/FINAL-QA.md` records the branch-local QA contract and hashes.

## Repository-documentation synchronization

The new top-level `brand/` product surface is now represented in both repository documentation layers:

- `REPOSITORY_TREE.md` includes the brand directory and responsibilities;
- `README.md` and `README.zh-CN.md` compact repository trees both include `brand/`.

The compact-tree update was applied by a one-off GitHub Actions workflow and the temporary workflow file was removed afterward. Sync run `33704957846` completed successfully.

## Integration validation

A one-off validation workflow exercised the actual brand branch. The first run exposed only a temporary workflow environment omission (`PYTHONPATH=src`), not a product defect: repository integrity and portable contract checks already passed while runtime tests could not import `svif`.

After correcting that validation environment without changing product code, run `33705138040` completed successfully with:

- `python checks/check_repository.py`;
- `python conformance/check_contracts.py`;
- `PYTHONPATH=src python -m unittest discover -s tests -p 'test_*.py' -v`.

The temporary validation workflow was then removed.

## Remaining integration boundary

Before canonical `main` integration:

1. preserve the byte-exact approved Svif board in repository storage;
2. attach the remaining larger deterministic PNG outputs through a byte-preserving transport and verify Git blob SHA plus documented SHA-256;
3. re-resolve latest `main` and reconcile branch-local continuity;
4. integrate coherently without changing the immutable released `v0.2.0-preview.1` tag;
5. verify authoritative `main` after publication.

At this point the unresolved gate is **large byte-exact binary preservation plus final latest-main reconciliation**; visual design, 13/13 QA, repository documentation, and branch validation are complete.
