# Svif branch-governance decision

Date: 2026-08-27
Status: Accepted

## Decision

During the Svif architecture rewrite, branch governance is intentionally minimal:

- `main` is the authoritative active Svif development line.
- `legacy/zerolocal-v0.1` preserves the final pure ZeroLocal v0.1 predecessor boundary at `8ccbb1d30520ca3d0b8b9f2cfe2963d35a853cf6`.
- Temporary, experimental, redundant, or otherwise non-authoritative branches do not require immediate cleanup while the new version is still under active restructuring.
- Branch cleanup is deferred until the new Svif version is substantially complete, at which point non-authoritative branches should be reviewed and removed deliberately.
- Durable project state, specifications, conformance work, and migration decisions MUST treat `main` and the explicit `legacy/*` predecessor branch as the meaningful branch boundaries. Incidental branches MUST NOT become hidden sources of truth.

## Rationale

The current priority is architectural convergence, not repository housekeeping. Immediate cleanup of incidental branches adds churn without improving protocol correctness, while preserving a clear active line and predecessor line is sufficient for safe development and historical recovery.

## Consequence

Future work may rewrite `main` aggressively toward Svif without preserving predecessor layout in-place. Historical ZeroLocal v0.1 behavior remains recoverable from `legacy/zerolocal-v0.1`. Non-authoritative branch cleanup is a release-completion task rather than an architecture-transition blocker.
