# Svif / Agnir Architecture Checkpoint — 2026-08-27 21:30 +08:00

## Scope

This checkpoint captures the cross-project architecture migration from ZeroLocal to Svif and the coordinated PPMP/PPM/Sandminni to Agnir transition.

## Svif state

- Svif is the project/product identity; ZeroLocal and ANRD are predecessor identities.
- Svif Core is project-centered and execution-environment-independent.
- Neutral Core roles are Principal and Executor; Execution Environment and Capability Adapter are first-class concepts.
- Svif depends on a compatible Agnir Core protocol version rather than a specific implementation/backend/adapter.
- Current draft dependency target is the Agnir Core 0.1 line; exact release compatibility remains unfrozen.
- Draft lifecycle: DISCOVER -> PLAN -> CHANGE -> VERIFY -> DELIVER -> OBSERVE -> CHECKPOINT, with REPAIR as the recovery loop.
- Stable candidate provenance is the Core abstraction; immutable Git revision remains a strong Software Delivery + SCM realization.
- ZeroLocal software-delivery invariants are preserved in the Software Delivery Profile rather than copied wholesale into Core.
- Capability Adapter and Software Delivery Profile drafts exist and are registered in project state.
- Validation Project #2 remains paused until new Svif/Agnir conformance boundaries are explicit.

## Version-line preservation

The predecessor ZeroLocal v0.1 line is preserved on branch `legacy/zerolocal-v0.1`, pinned to commit `8ccbb1d30520ca3d0b8b9f2cfe2963d35a853cf6`, the last pure predecessor commit before the Svif transition began.

`main` is the active Svif architecture/development line and may now evolve directly rather than maintaining long-lived predecessor compatibility in-place.

## Cross-project boundary

- Dependency direction: Svif -> Agnir.
- Durable project memory remains owned by each Project and isolated between projects.
- The shared ChatGPT workspace is an execution workspace/registry, not an authoritative shared mutable memory store.
- Cross-project decisions are recorded independently in each affected repository.

## Next work

1. Freeze Agnir repository/filesystem discovery schema and cold-start conformance.
2. Freeze Svif PLAN semantics and candidate/evidence envelope.
3. Define versioned machine-readable Capability Adapter schema and conformance IDs.
4. Introduce AGNIR-* and SVIF-* conformance tests without renaming predecessor claims.
5. Revise Validation Project #2 against Svif Core + Software Delivery Profile + Agnir cold-start discovery.
6. Only after the new contracts are executable, perform broad repository/file/integration renames.
