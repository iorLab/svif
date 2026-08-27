# Svif checkpoint — branch governance and active-line focus

Saved: 2026-08-27T06:49:51-07:00

## Boundary captured

- `main` is the authoritative active Svif development line.
- `legacy/zerolocal-v0.1` preserves the final pure ZeroLocal v0.1 predecessor boundary at `8ccbb1d30520ca3d0b8b9f2cfe2963d35a853cf6`.
- Temporary, redundant, or incidental branches are intentionally ignored during the architecture rewrite unless they become explicitly authoritative.
- Branch cleanup is deferred until the new Svif version is substantially complete.
- The active technical priorities remain Agnir discovery/conformance, Svif PLAN/evidence-envelope semantics, Capability Adapter schema, new conformance IDs/tests, and Validation Project #2 rewrite.

## Resumption rule

A fresh executor should continue from `main`, use `legacy/zerolocal-v0.1` only for predecessor evidence or compatibility comparison, and should not spend time cleaning incidental branches before the new version reaches completion unless a branch causes an actual conflict or ambiguity.
