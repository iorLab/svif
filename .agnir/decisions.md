# Svif Decisions

## 2026-08-27 — New main-line architecture

- `main` implements Svif directly. ZeroLocal v0.1 remains predecessor evidence on `legacy/zerolocal-v0.1`; its active Skill/spec/conformance layout is not retained on the Svif main line.
- Svif Core version is the `0.2` development line and depends on the Agnir Core `0.1` protocol line.
- Svif's own durable continuity is now discovered through `AGNIR.yaml`; `.chatgpt/project-memory.yaml` is only a ChatGPT bootstrap shim and not a second memory root.
- PLAN semantics are mandatory, but a trivial operation may coalesce PLAN in its execution trace when no separately inspectable plan artifact/evidence is material. Planning preconditions still apply before CHANGE.
- Capability Adapter operation *names* are extensible; every operation declares one Core semantic effect. This keeps third-party/provider APIs out of Core while preserving portable orchestration semantics.
- The Core semantic effects are `resolve`, `inspect`, `mutate`, `identify`, `verify`, `actuate`, `observe`, `authorize`, `recover`, and `checkpoint`.
- Stable candidate provenance is represented through standard evidence records rather than requiring Git SHA. Git full SHA remains the recommended strong Software Delivery + SCM realization.
- The standard evidence record carries Project/operation identity, record kind, stable subject identity, optional derivation chain, optional target identity, result status, producer/adapter reference, authority reference, evidence locator, and timestamp.
- Delivery gated by verification must actuate the verified candidate or a replacement that has independent verification evidence.
- OBSERVE is mandatory when external effect is claimed; actuation success alone is not sufficient.
- CHECKPOINT remains a Svif lifecycle state but delegates persistence/resumability to Agnir.
- Secret values remain in authorized protected channels/stores; adapter descriptors and evidence may carry references/scopes but not require plaintext secret transport.

## 2026-08-27 — Repository identity transition

- The repository rename is no longer deferred until late-stage completion. The main-line architecture is sufficiently separated from predecessor layout that old repository names now create more identity debt than migration safety.
- Rename sequence is: `mattamior/rpm` -> `mattamior/agnir`, `iorLab/zerolocal` -> `iorLab/svif`, then `iorLab/zerolocal-cloudflare-starter` -> `iorLab/svif-cloudflare-starter`.
- Legacy branch names are intentionally not renamed: `legacy/zerolocal-v0.1` and `legacy/ppmp-v2.0.0` preserve predecessor identity and history.
- GitHub redirects may preserve navigation after a rename, but redirects are compatibility behavior rather than canonical project identity. Durable manifests, repository extensions, bootstrap shims, documentation, cross-project references, and CI/reference URLs must be updated after each rename.
- Repository naming remains packaging/discovery metadata, not a Svif Core semantic dependency.
