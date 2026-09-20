# Svif Current State

Svif is the authoritative active **Project orchestration product** in `iorLab/svif`. The former `iorLab/svif-cloudflare-reference` project is retired. Repository-managed Agnir continuity on `main` remains canonical.

## Active direction — local effectiveness and functional readiness first

The Principal explicitly paused OpenAI Platform publication and requested two confirmations: (1) Svif can be installed locally and actually takes effect; (2) Svif's functionality is developed and complete. Publisher prerequisites and portal submission are no longer the active P0. Public publication requires a later explicit resumption instruction.

**Current verdict: safety/recovery repairs are implemented in the candidate; current-version full native effectiveness and whole-product release acceptance are not yet signed off.** Historical package/CI acceptance is not withdrawn as a historical observation, but it does not establish either requested conclusion. The earlier assumption that only publisher/account blockers remain is superseded by the functional findings below.

## Historical audited subject and evidence levels

- Audited authoritative source: `fe7788bd53d3a240f663860133b741799d0470e3`.
- Svif product line remains `0.2`; Project Binding, Software Delivery, Capability Adapter and Evidence Record remain their `0.2` contracts.
- Active source/package version remains unpublished `0.2.0`.
- The historical package-only accepted Plugin subtree was `5ab4b6147dbd096c052f042b23e37f0ec39f7091`, materialized by `f9026f7e3db4db8956cfc88ba1990daf0757a011`. That historical audit changed continuity only; the 2026-09-20 implementation candidate changes the runtime, Skill and acceptance tooling.
- The actual `svif-0.2.0.zip` was retrieved from Actions artifact `10542750132`. Independent extraction verified CRC, all five member Git blob identities, and inner ZIP SHA-256 `bc2315562f7bdeb4232aadb9b583a7442f8cd868dbeacd13bb57caf0c785177c`. This proves package identity/integrity, not native installation or activation.
- Released **Plugin MVP** / Repository Preview `v0.2.0-preview.1` remains immutable at `2b07b6b5ea0bc8feee59f9f647be9af3069d056e`, annotated tag object `2535cb89426c2d38c2e061948e81954a7c7c26d7`.
- Historical Preview.1 evidence records real Codex CLI and ChatGPT desktop/Codex installation, first-use bootstrap, work, checkpoint and fresh-context recovery. It does not establish current `0.2.0` native-host acceptance or certify all failure paths in Preview.1.
- Baseline run `35334521502` / runtime job `105566170085` reports 87 tests passed. Several Plugin behavior guards, including first-use bootstrap, assert Skill text rather than executing an installed host. Existing green tests do not cover the newly reproduced gaps.
- Four source modules were re-materialized from connector reads, verified byte-for-byte against their Git blob SHAs, and exercised in an isolated Python 3.13.5 environment. The audit did not run the full repository suite locally, did not install a native Codex/desktop host, and did not operate the Principal's computer.
- Basic Agnir load -> checkpoint -> fresh provider load succeeded in isolated fixtures on compatibility lines `0.1`, `0.2`, and `1.0`. This is provider behavior evidence, not a fresh LLM-session or native-client acceptance result.

## Functional repair candidate — 2026-09-20

The Principal authorized implementation to release standard. The four reproduced
baseline gaps are now repaired in the staged source candidate and covered by executable
regressions; they are no longer merely audit findings. The complete local suite passes
126 tests, plus repository-integrity and portable-contract checks. Remote candidate
verification and native model-behavior acceptance must still be observed separately.

- Provider-owned `CapabilityPolicy` is mandatory at the effect boundary. Omitted/null/
  empty/downgraded model authority advice cannot waive Cloudflare protected-delivery.
- Trusted operation-level verification defaults to required. Parsed ChatGPT verification
  declarations need independent trusted receipts; failed required non-effect checks cannot
  publish completion. Legitimate trusted not-applicable operations remain supported.
- Full checkpoint preflight, revision CAS, no-follow contained I/O, a process/thread lock
  and recoverable write-ahead journal prevent normal failures from leaving a successful
  partial checkpoint and recover interruptions before exposing adapter snapshots.
- Evidence children, anchor/locator/receipt/runtime paths and unsafe link types are checked.
- Single-use sessions, durable operation replay checks and a pre-actuation effect marker
  prevent uncertain effects from being blindly repeated after restart. Independent trusted
  reconciliation does not redeploy. This is not a distributed exactly-once guarantee.
- Executable tests cover all three Agnir compatibility lines, every publication failure
  position, actual process death followed by recovery in another process, concurrency,
  stale/conflicting memory, corruption, links and trusted-policy/receipt boundaries.

Native Codex `0.155.1` was installed and exercised without model credentials in an
isolated Ubuntu runner: probe run `35507822026` reported the then-current Svif `0.2.0`
package installed and enabled. That preliminary probe does not validate the final
modified Skill or actual LLM behavior. The final native acceptance harness verifies
exact installed bytes plus app-server Skill discovery; optional authenticated positive
model scenarios and same-candidate negative host scenarios remain distinct release gates.

`conformance/RELEASE_READINESS.md` is the requirement-to-evidence matrix and native
acceptance procedure. `spec/RUNTIME_SAFETY.md` defines the trusted integration and
recovery boundary. The Skill now explicitly covers those failure semantics without
bundling or duplicating the Python kernel. Package bytes have changed: old tree
`5ab4b6147dbd096c052f042b23e37f0ec39f7091` and its ZIP remain historical packaging evidence,
not the new local candidate. No release tag or public submission is created.

Candidate implementation evidence: `.agnir/evidence/2026-09-20-runtime-readiness-repair.md`.

## Product architecture and scope

The four first-class components remain Orchestrator (`src/svif/runtime.py`), Continuity Provider (`src/svif/continuity/agnir.py`), Execution Surface (`src/svif/execution/chatgpt.py`), and Capability Provider (`src/svif/capabilities/cloudflare.py`).

The installed Skills-only package guides the host through Svif workflow semantics; it does not package the Python Orchestrator. Skill effectiveness and Python runtime enforcement therefore need separate evidence. Remote MCP/App packaging remains an optional increment, not an invented prerequisite for accepting the Skill-first MVP. Live Cloudflare transport/production delivery is not claimed and remains disabled unless explicitly authorized.

## Canonical continuity and preserved boundaries

- Project identity: `urn:svif:project:svif-core`.
- Agnir Core/profile: `1.0` / `repository-filesystem/1.0`.
- Logical lineage: `urn:svif:lineage:authoritative`; VCS selector: `refs/heads/main`.
- Durable locators remain `.agnir/state.md`, `.agnir/next-actions.md`, `.agnir/decisions.md`, `.agnir/evidence/`.
- Applied Agnir operational release remains `v1.0.0@6d16dcfd17b8e9f22fd25804e22b9f8a516d06c3`; no Agnir upgrade or compatibility promotion is performed here.
- The current adapter retains `0.1` / `0.2` / `1.0` support. The existing Skill founding bootstrap remains Core/profile `0.1`; installing a newer distribution is not permission to relabel an existing Project.
- Accepted 0.2 -> 1.0 repository promotion receipts remain in `.agnir/evidence/2026-09-07-agnir-1.0-main-promotion.md`; the cross-project adoption handoff is already complete in `iorLab/agnir/.agnir/evidence/2026-09-07-svif-agnir-1.0-adoption.md`.
- Approved brand integration remains PR #5 / commit `77ff3d0e8b3d0d691bb47529e065571c17a0aa81`. Approved assets and package-local 128x128 icon are unchanged. Root OpenAI metadata and its compatibility fallback are unchanged.
- `README.md` and `README.zh-CN.md` remain synchronized user/Agent entry points; the release/install entry currently selects immutable Preview.1, not moving `main` or the unaccepted 0.2.0 candidate.
- Historical PR #3 is closed unmerged; its tip `d42489f72cc8985d353ccbf2f9b6ae7249fe6480` remains archived pending physical branch-ref retirement. It is not an active feature or release dependency.
- No `v0.2.0` tag, GitHub Release, OpenAI submission, review, Publish, directory availability, current-version consumer installation, or live provider effect is claimed.

`.agnir/next-actions.md` is the canonical ordered resume plan.
