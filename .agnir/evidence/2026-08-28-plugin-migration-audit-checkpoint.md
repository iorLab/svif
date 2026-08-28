# Svif Plugin / predecessor-migration audit checkpoint

Timestamp: 2026-08-28T13:23:00+08:00

## Verified repository state

- Canonical repository: `iorLab/svif`.
- Authoritative branch: `main`.
- Pre-checkpoint head: `98868f5052a6d2e2e4b92a1f3f534dbdae799764` (`docs: restore durable Plugin distribution decision`).
- Svif product-check run `33144484052`: **success**.
- Founding credential-free product E2E remains proven by run `33143308949`.

## Migration audit finding

The ZeroLocal predecessor state on `legacy/zerolocal-v0.1` explicitly recorded `installable-plugin` as the long-term product form. During the Svif architecture rewrite this intent became too generic: current architecture/state used the broader term `distribution` and canonical Agnir state no longer explicitly carried the Plugin target.

This was treated as a durable-knowledge migration regression, not as an obsolete naming detail. The mature distribution target is therefore restored as **installable Plugin** while ChatGPT Apps SDK / MCP remains the current concrete ChatGPT Execution Surface packaging path rather than a replacement product identity.

Restoration completed before this checkpoint:

- `ARCHITECTURE.md` explicitly restores the installable Plugin mature distribution target and dependency direction;
- `.agnir/decisions.md` records the restored Plugin decision;
- head `98868f5052a6d2e2e4b92a1f3f534dbdae799764` passes product checks.

## Predecessor evidence classification

`iorLab/svif@legacy/zerolocal-v0.1` is a real predecessor Project and contains `.chatgpt/project-memory.yaml` plus predecessor state/next-actions/decisions. It is suitable for validating predecessor-memory-to-Agnir semantic migration for Svif.

It is **not** an exact PPMP v2.0.0 external fixture. Its project-memory serialization is an earlier v1/RPM-era form. No qualifying second external Project with a clear PPMP v2.0.0 manifest was found during this audit. That gap must remain explicit rather than being satisfied by relabeling older predecessor evidence.

## Boundaries preserved

- Live Cloudflare production delivery remains disabled and unproven without explicit authority.
- Credential-free founding E2E success is not live-provider evidence.
- `legacy/zerolocal-v0.1` remains predecessor history and must not be mutated as part of active Svif development.
- ChatGPT execution/package state remains non-canonical; canonical Project truth remains with the configured Continuity Provider.

## Resume point

1. Synchronize the restored **installable Plugin** target into the remaining Svif user-facing documentation, especially `README.md` and `README.zh-CN.md`, while keeping Apps SDK / MCP as current ChatGPT integration mechanics.
2. Complete and record the real ZeroLocal predecessor -> current Svif/Agnir migration evidence envelope, explicitly separating validated predecessor-memory migration from the still-missing exact external PPMP v2 fixture.
3. Resume concrete ChatGPT app/MCP packaging hardening around the existing externally driven bridge.
4. Use Agnir's now-proven multi-project/storage-neutral fixtures for broader Svif neutrality pressure.
