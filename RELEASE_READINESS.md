# Svif functional release-readiness matrix

Scope: the existing Skill-first MVP and the founding Python runtime/provider contracts. Remote MCP/App hosting and real Cloudflare transport remain separate integration increments; neither is invented as a prerequisite for accepting the Skill-first product. Public submission remains paused.

**This document is an acceptance contract, not a blanket release approval.** Native installation/discovery receipts and actual-work/fresh-session receipts are distinct. Refer to `.agnir/state.md` for observed status and the exact current candidate.

| Existing commitment | Implementation / executable evidence | Acceptance boundary |
|---|---|---|
| Ordinary Project first-use bootstrap, preservation, idempotency | Shared `plugin/skills/svif/SKILL.md`; `test_plugin_first_use_bootstrap.py` guards instructions | Current native actual-work evidence required; text checks are not behavior evidence. |
| Agnir 0.1 / 0.2 / 1.0 identity, lineage, selector and load/checkpoint | `agnir.py`; `test_agnir_continuity.py`, `test_agnir_stable_migration.py` | Executable provider fixtures; trusted integration supplies selected Project/ref context. |
| Exact-subject verification before completion/effects | `OperationRequest`, `EvidenceRecord.check_id`; `RuntimeReadinessTests` | Required checks are trusted configuration. Integration authenticates verifier receipts; JSON parsing does not authenticate claims. |
| Mandatory authority independent of model data | Provider `operation_policy()` + Orchestrator; omitted/null/empty/weaker-class tests, descriptor parity | Missing trusted policy fails closed. Real platform consent and target/credential scope remain integration responsibilities. |
| Single-use completion / no blind retry | Orchestrator session registry; session forgery/replay tests | In-memory session cannot be replayed; filesystem pending-effect marker additionally survives process restart. |
| Exact delivery + independent observation | Cloudflare semantic Provider; founding E2E and negative provider/runtime tests | Fake/injected transport only. No live deployment claimed or authorized. |
| Coherent checkpoint and crash recovery | `_filesystem.py` journal and cross-process lock; `ContinuityReadinessTests` | Full preflight; actual process death at six write boundaries on all three compatibility lines; cooperating-reader isolation. |
| Stale/concurrent state safety | Snapshot revision; preflight/operation guard; stale and cross-process tests | Rejects before effect when discovered state changed; same-Project effects serialized by filesystem adapter. Other providers must supply equivalent coordination. |
| Confined reads/writes and safe temporary files | Directory-descriptor/no-follow I/O on POSIX; child/anchor/lock/receipt-link tests | No authorized external-locator support added. Windows hostile directory-replacement race is outside current claim. |
| Unconfirmed external-effect repair | Persistent pending marker; `reconcile_effect()` with trusted authority and exact observation | Never automatically replays delivery; unresolved/absent effects require explicit Principal/provider reconciliation. |
| Portable package / manifests / installation mechanics | Existing package/distribution suites, `check_native_install.py`, `test_native_install_evidence.py` | Native host receipt must include matching installed bytes, enabled state and new-process discovery. |
| Fresh Executor recovers real Project work | `LOCAL_ACCEPTANCE.md` procedure | Must run on actual native host with no prior transcript; not simulated by constructing a new Python object. |

## Release acceptance rule

A local release requires all repository/portable/runtime checks passing on the exact candidate, closure of applicable failed-behavior regressions, a native install/discovery receipt for the same Plugin bytes, and reviewed real-task/bootstrap/idempotency/fresh-session/negative-case evidence. A receipt from a different commit is reusable only after exact relevant-content equivalence is established. No aggregate test count substitutes for a missing gate.

Current code adds no plaintext credentials, no automatic production deployment, and no OpenAI publication. `v0.2.0-preview.1` stays immutable. Active `0.2.0` remains a development candidate until these acceptance conditions are actually satisfied.

## Continuous gate

`Svif product checks` and `Svif local readiness` run on every pull request and main push. Native discovery accepts a namespaced Skill only with the exact Plugin origin, explicit enablement, installed path and file digest. This gate intentionally performs no authenticated model work; that remaining acceptance must not be inferred from CI success.
