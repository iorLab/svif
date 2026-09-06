# Svif brand binary materialization — 2026-09-03

Status: **branch-local integration evidence; not canonical until integrated into authoritative `main`.**

## Trigger

The approved 10:42 AM source board and larger raster production outputs could not be sent byte-exactly through the direct ChatGPT-to-GitHub base64 bridge. A controlled 12,183-byte PNG probe returned a different Git object SHA and was rejected rather than attached.

The Principal then uploaded the prepared handoff ZIP directly to the root of `brand/identity-system`.

## Transport verification

The uploaded archive was verified before use:

- filename: `svif-agnir-brand-binary-integration-handoff.zip`;
- size: `7,925,506` bytes;
- SHA-256: `52e8cee3c03f0762fc47d579505122dc452e5de97dafb462a3b470ed5457f72d`;
- Git blob: `3f49c176a5c5680620de6f4de09beb6297f99bf0`.

The same Git blob was observed in both Svif and Agnir repositories, proving the browser uploads preserved the exact archive bytes.

## Stale-base reconciliation

Before materialization, authoritative Svif `main` had advanced to `eba1b8538c4692a08bf69452525b735d23564599`; the brand branch was behind by 7 commits.

Reverse-sync PR `#8` (`main` -> `brand/identity-system`) was mergeable and was merged into the brand branch at `6076dd08d3e8d352d130a6c3ac2ccddb3d28bae7`. Post-reconcile comparison reported `behind main = 0`.

## Byte-exact GitHub-runner materialization

Temporary workflow creation commit: `9726a22107df137d36980faceb6b38a4de06af2c`.

Workflow run `33730468886` completed successfully. It:

1. verified the uploaded archive SHA-256;
2. extracted the handoff;
3. selected all Svif payload targets;
4. explicitly restored the family-board Svif mapping omitted by the handoff manifest-v1 duplicate-key bug;
5. verified each source payload SHA-256;
6. copied each source to its final repository path;
7. verified each destination SHA-256 again;
8. committed the assets;
9. removed the root transport ZIP and temporary workflow.

Final materialization commit: `137307351dfee467472ccd997fdc714b8a71c549`.

## Repository result

Byte-exact approved references now exist at:

- `brand/reference/svif-approved-reference.png`;
- `brand/reference/svif-agnir-family-approved-reference.png`.

Raster production masters now exist at:

- `brand/masters/svif-mark.png`;
- `brand/masters/svif-wordmark.png`;
- `brand/masters/svif-horizontal-lockup.png`;
- `brand/masters/svif-vertical-lockup.png`.

The complete light/dark/mono/app/favicon/social delivery set exists under `brand/exports/`.

A particularly useful integrity receipt is `brand/exports/svif-favicon-128.png`: Git blob `40dbc1cbca075149cd8fc4e0859f09217b0c3530`, exactly equal to the locally expected Git object SHA that the earlier direct bridge failed to preserve.

## Gate result

The **large byte-exact binary preservation gate is closed** for the Svif brand branch. Remaining gates are latest-main freshness, final Draft PR synthetic-merge CI, coherent publication to authoritative `main`, and post-publication verification.
