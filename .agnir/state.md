# Svif Current State

Svif is the authoritative active **Project orchestration product** in `iorLab/svif`. The former `iorLab/svif-cloudflare-reference` project is retired. Repository-managed Agnir continuity on `main` remains canonical.

## Active direction — local effectiveness and functional readiness first

The Principal explicitly paused OpenAI Platform publication and requested two confirmations: (1) Svif can be installed locally and actually takes effect; (2) Svif's functionality is developed and complete. Publisher prerequisites and portal submission are no longer the active P0. Public publication requires a later explicit resumption instruction.

**Current verdict: neither current-version local effectiveness nor whole-product functional completion is signed off.** Historical package/CI acceptance is not withdrawn as a historical observation, but it does not establish either requested conclusion. The earlier assumption that only publisher/account blockers remain is superseded by the functional findings below.

## Audited subject and evidence levels

- Audited authoritative source: `fe7788bd53d3a240f663860133b741799d0470e3`.
- Svif product line remains `0.2`; Project Binding, Software Delivery, Capability Adapter and Evidence Record remain their `0.2` contracts.
- Active source/package version remains unpublished `0.2.0`.
- The package-only accepted Plugin subtree remains `5ab4b6147dbd096c052f042b23e37f0ec39f7091`, materialized by `f9026f7e3db4db8956cfc88ba1990daf0757a011`. No product or Plugin source is changed by this readiness checkpoint.
- The actual `svif-0.2.0.zip` was retrieved from Actions artifact `10542750132`. Independent extraction verified CRC, all five member Git blob identities, and inner ZIP SHA-256 `bc2315562f7bdeb4232aadb9b583a7442f8cd868dbeacd13bb57caf0c785177c`. This proves package identity/integrity, not native installation or activation.
- Released **Plugin MVP** / Repository Preview `v0.2.0-preview.1` remains immutable at `2b07b6b5ea0bc8feee59f9f647be9af3069d056e`, annotated tag object `2535cb89426c2d38c2e061948e81954a7c7c26d7`.
- Historical Preview.1 evidence records real Codex CLI and ChatGPT desktop/Codex installation, first-use bootstrap, work, checkpoint and fresh-context recovery. It does not establish current `0.2.0` native-host acceptance or certify all failure paths in Preview.1.
- Baseline run `35334521502` / runtime job `105566170085` reports 87 tests passed. Several Plugin behavior guards, including first-use bootstrap, assert Skill text rather than executing an installed host. Existing green tests do not cover the newly reproduced gaps.
- Four source modules were re-materialized from connector reads, verified byte-for-byte against their Git blob SHAs, and exercised in an isolated Python 3.13.5 environment. The audit did not run the full repository suite locally, did not install a native Codex/desktop host, and did not operate the Principal's computer.
- Basic Agnir load -> checkpoint -> fresh provider load succeeded in isolated fixtures on compatibility lines `0.1`, `0.2`, and `1.0`. This is provider behavior evidence, not a fresh LLM-session or native-client acceptance result.

## Open functional blockers — reproduced, not repaired

1. **Trusted authority can be bypassed by omitting the requested authority class.** `ChatGPTExecutionSurface.parse_result()` accepts a model-controlled optional `authority_class`; `Orchestrator.complete()` enforces only that supplied class. For the actual Cloudflare provider operation whose descriptor requires `protected-delivery`, omitted/null/empty values reached the injected fake deploy/observe transport and checkpointed with no trusted grants. Explicit `protected-delivery` correctly blocked the control case. Authority requirements must come from trusted provider/operation policy, not optional result data.
2. **A failed checkpoint can partially publish durable truth.** A valid discovery record with `decisions: null` loads successfully, but an outcome requesting State + Next Actions + Decisions writes State and Next Actions before raising for the unavailable Decisions locator. All three supported compatibility lines reproduced changed State/Next Actions with no new evidence receipt. Preflight, coherent publication and interruption/recovery behavior need repair and executable regression coverage.
3. **Evidence-child symlinks bypass Project-root containment.** The declared evidence directory is contained, but `_read_evidence()` follows its child-file symlinks without rechecking their resolved paths. On all three compatibility lines a dummy file outside the selected Project root was loaded as evidence without an authorized external binding. Only dummy temporary data was used.
4. **Failed non-effectful verification does not prevent a success-state checkpoint.** A result carrying a failed verification record and a completion State/Next update, with no capability request, was checkpointed. Required verification needs a trusted operation-level contract and failure handling; not every trivial non-effectful operation must necessarily require verification.

Detailed reproduction inputs, controls, results and acceptance criteria are appended under the 2026-09-20 readiness audit in `.agnir/evidence/2026-09-18-public-submission-candidate-audit.md`. This is a targeted audit, not a claim that these are the only remaining defects.

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
