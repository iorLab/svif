# Svif first-use Agnir version-selection repair — 2026-09-20

Status: implementation candidate on `fix/bootstrap-agnir-version-selection`; OpenAI Platform publication remains paused.

Principal correction: Svif must not pin all new/current Projects to Agnir Core/profile `0.1`. Existing Project truth wins. A valid existing Agnir Project keeps the Core/profile it declares; adding Svif creates/validates a matching continuity binding and does not authorize compatibility migration. Partial or contradictory Agnir artifacts remain repair cases.

Only a genuinely uninitialized Project resolves the canonical latest published stable Agnir at operation time. Stable means a published non-prerelease tag/Release, never moving `main`, RC, untagged source, stale model memory, or fallback to the old Svif Preview baseline. Package SemVer and Core/profile compatibility remain separate.

Current external observation on 2026-09-20: `iorLab/agnir` latest published stable is repository release `v1.0.2` at revision `b5626394ec40a5cb7a28c01892acde07cc0adc8e`; that release still declares Core `1.0` and `repository-filesystem/1.0`. This receipt is evidence of today's resolved stable, not a hard-coded future bootstrap constant. Future first-use operations must resolve latest stable again.

The immutable Svif `v0.2.0-preview.1` release is not modified. It remains historical evidence with its original `0.1` bootstrap behavior. The current unpublished `0.2.0` Skill is the first Svif line to supersede that rule.
