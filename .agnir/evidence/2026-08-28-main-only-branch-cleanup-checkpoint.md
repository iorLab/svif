# Svif main-only branch cleanup checkpoint

Date: 2026-08-28

## Result

`iorLab/svif` now uses **main-only branch governance**. GitHub branch enumeration after cleanup returned only `main`.

Verified pre-checkpoint baseline:

- `main`: `4ea2c138417fa365aac6d88a0154e693324640b2`;
- product-check run `33157419617`: success;
- all former legacy, fix, feature, temporary, and branch-capability-probe refs were deleted;
- the one-shot cleanup workflow used to remove refs was deleted from `main` after use.

## Historical preservation

Before branch deletion, retired branch names and final tip SHAs were recorded in `history/BRANCH_ARCHIVE.md`. ZeroLocal predecessor lineage is therefore recoverable by immutable commit SHA and Git history without retaining a live `legacy/*` branch.

Historical commits are evidence only. They are not active Svif runtime dependencies, compatibility obligations, conformance inputs, release gates, or recovery requirements.

## Resume point

Continue with the current greenfield product line:

1. harden ChatGPT Apps SDK / MCP packaging around the existing `ChatGPTExecutionSurface` and `Orchestrator.begin()` / `complete()` lifecycle;
2. add broader neutrality pressure;
3. advance installable Plugin packaging only on top of the validated kernel/integration boundary.

Live Cloudflare production delivery remains separately authorized and unproven.