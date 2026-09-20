# Svif Current State

Svif is the authoritative active **Project orchestration product** in `iorLab/svif`. The former `iorLab/svif-cloudflare-reference` project is retired. Repository-managed Agnir continuity on `main` remains canonical.

## Active direction: local effectiveness and release-quality functionality

The Principal paused OpenAI Platform publication, then authorized implementation to release-quality standards. Local installation/effectiveness and bounded functional readiness take priority; publication requires a later explicit resumption instruction.

The 2026-09-20 hardening candidate implements the four reproduced functional findings, with full local regression verification. **It is not yet signed off as release-ready or current-version native-task effective.** Native installation/discovery, real task/bootstrap/idempotency, and genuinely fresh-session recovery remain separate evidence gates.

## Functional candidate

- Captured source: `960526544da308ea8b0eb1d325b26609487ab856`; implementation staged on temporary `fix/local-readiness`, without changing Project authority.
- F1 repaired in candidate: mandatory authority comes from trusted registered Provider/operation metadata; missing policy fails closed and optional result fields cannot weaken it.
- F4 repaired in candidate: trusted required-verification/check IDs, explicit non-applicability, rejection of failed/blocked/unknown/missing/wrong-subject checks before successful completion.
- F2 repaired in candidate: full checkpoint preflight, cooperating cross-process lock, stale-snapshot rejection, multi-file journal, rollback/committed recovery and conflict refusal.
- F3 repaired in candidate: confined discovery/evidence/lock/receipt I/O, no-follow POSIX directory walks, rejection of symlinks/junctions/multi-linked file targets, and unique temporary files.
- Additional guards: single-use sessions, duplicate receipt rejection, persistent uncertain-effect marker and trusted observation-based reconciliation without re-delivery.
- Local complete suite: 109 tests passed (baseline 87), repository-integrity and portable-contracts passed, compile checks passed. Fault injection includes 18 real child-process crash trials across Core/profile 0.1, 0.2 and 1.0.
- Native harness: `checks/check_native_install.py` isolates HOME/CODEX_HOME, observes native install/enabled state, validates exact package bytes, and starts a new native process for Skill discovery. No local Codex binary was present; this local attempt truthfully remained not-observed.
- Evidence: `.agnir/evidence/2026-09-20-functional-hardening.md`. Scope/test/acceptance map: `RELEASE_READINESS.md`; actual local exercise: `LOCAL_ACCEPTANCE.md`.

## Product and package boundaries

The four first-class components remain Orchestrator (`src/svif/runtime.py`), Continuity Provider (`src/svif/continuity/agnir.py`), Execution Surface (`src/svif/execution/chatgpt.py`), and Capability Provider (`src/svif/capabilities/cloudflare.py`). The shared Skills-only **Plugin MVP** guides the host; it does not contain the Python kernel. Python tests therefore do not prove installed Skill effectiveness.

Svif remains product line `0.2` / `project-binding/0.2`, active unpublished source version `0.2.0`. README.md and `README.zh-CN.md` retain synchronized user/Agent entry points and now link the local acceptance/readiness contracts.

The old package-only Plugin tree `5ab4b6147dbd096c052f042b23e37f0ec39f7091` and ZIP `bc2315562f7bdeb4232aadb9b583a7442f8cd868dbeacd13bb57caf0c785177c` remain historical packaging evidence, not the new hardening package or a release approval. The updated Skill changes the Plugin subject; identify its new exact tree when accepting the candidate.

Released `v0.2.0-preview.1` remains immutable at `2b07b6b5ea0bc8feee59f9f647be9af3069d056e`. Historical Codex CLI / ChatGPT desktop/Codex acceptance remains valid for its tested paths only; no current-candidate native effect is inferred from it.

## Canonical continuity and limits

Project identity `urn:svif:project:svif-core`, Agnir Core/profile `1.0` / `repository-filesystem/1.0`, logical lineage `urn:svif:lineage:authoritative`, VCS selector `refs/heads/main`, and all four memory locators are unchanged. Applied Agnir remains `v1.0.0@6d16dcfd17b8e9f22fd25804e22b9f8a516d06c3`. Accepted promotion/adoption and brand integration remain complete.

The filesystem adapter transaction coordinates its own readers/writers, not arbitrary editors or network filesystems. Windows does not yet claim hostile concurrent-directory-replacement containment. Trusted integrations must authenticate evidence receipts and enforce real account/target/credential scopes; model-authored success fields are not proof. Live Cloudflare delivery and remote MCP/App hosting are not claimed; live delivery remains disabled unless explicitly authorized. No public submission, Publish, release tag or GitHub Release is performed here.
