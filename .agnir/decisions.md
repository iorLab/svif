# Svif Decisions

## 2026-08-27 — New main-line architecture

- `main` implements Svif directly. ZeroLocal v0.1 remains predecessor evidence on `legacy/zerolocal-v0.1`; its active Skill/spec/conformance layout is not retained on the Svif main line.
- Svif Core version is the `0.2` development line and depends on the Agnir Core `0.1` protocol line.
- Svif's own durable continuity is discovered through `AGNIR.yaml`.
- PLAN semantics are mandatory, but a trivial operation may coalesce PLAN in its execution trace when no separately inspectable plan artifact/evidence is material. Planning preconditions still apply before CHANGE.
- Capability Adapter operation names are extensible; every operation declares one Core semantic effect. This keeps third-party/provider APIs out of Core while preserving portable orchestration semantics.
- The Core semantic effects are `resolve`, `inspect`, `mutate`, `identify`, `verify`, `actuate`, `observe`, `authorize`, `recover`, and `checkpoint`.
- Stable candidate provenance is represented through standard evidence records rather than requiring Git SHA. Git full SHA remains the recommended strong Software Delivery + SCM realization.
- The standard evidence record carries Project/operation identity, record kind, stable subject identity, optional derivation chain, optional target identity, result status, producer/adapter reference, authority reference, evidence locator, and timestamp.
- Delivery gated by verification must actuate the verified candidate or a replacement that has independent verification evidence.
- OBSERVE is mandatory when external effect is claimed; actuation success alone is not sufficient.
- CHECKPOINT remains a Svif lifecycle state but delegates persistence/resumability to Agnir.
- Secret values remain in authorized protected channels/stores; adapter descriptors and evidence may carry references/scopes but not require plaintext secret transport.

## 2026-08-27 — Repository identity transition

- Canonical repositories are `iorLab/agnir` and `iorLab/svif`.
- Legacy branch names are intentionally not renamed: `legacy/zerolocal-v0.1` and `legacy/ppmp-v2.0.0` preserve predecessor identity and history.
- Repository redirects are compatibility behavior rather than canonical project identity.
- Repository naming remains packaging/discovery metadata, not a Svif Core semantic dependency.

## 2026-08-28 — Execution-surface-neutral active Project structure

- Execution-surface bootstrap configuration belongs to the execution surface, not the canonical Svif Project structure.
- The former `.chatgpt/project-memory.yaml` compatibility shim is removed from active `main`.
- For this repository's Agnir repository/filesystem profile, cold start begins directly at top-level `AGNIR.yaml`.
- Svif conformance treats active `.chatgpt/` structure as forbidden in this reference Project.

## 2026-08-28 — Cloudflare implementation role

- The Cloudflare repository is canonical at `iorLab/svif-cloudflare-reference`.
- Its role is an executable reference implementation/conformance testbed for Svif Software Delivery + Cloudflare Provider Adapter semantics.
- It is not a user starter/template and does not define provider-neutral Core semantics.
- The reference must preserve exact verified-candidate delivery, protected production authority, serialized state-sensitive delivery, target discovery, and independent post-delivery observation while replacing ZeroLocal-era naming and memory layout with Svif/Agnir-native structure.
