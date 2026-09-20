# Local acceptance — Svif 0.2.0 development candidate

OpenAI Platform publication remains paused. Use the exact candidate commit and Plugin tree recorded in Agnir, not the released Preview tag and not an unspecified moving branch. Installing a Plugin and executing its Skill are two different observations.

## Native install and discovery (no model calls)

From a clean checkout of the candidate on a computer with Codex installed:

```bash
python checks/check_native_install.py --output /absolute/path/to/new-svif-acceptance
```

The destination must be new. The harness creates an isolated HOME and CODEX_HOME, copies the exact Plugin and marketplace into that directory, installs using the native CLI, independently reads installed/enabled state, checks every installed file against the candidate, then starts a new App Server process and calls `skills/list`. It does not copy credentials or touch the user's existing Plugin configuration. It writes `receipt.json`; a missing host, changed package, unsupported command, or missing Skill returns nonzero. `release_ready` remains false even when installation/discovery pass.

The CLI command contract used by the harness was checked on 2026-09-20:
- https://developers.openai.com/codex/cli/reference — `plugin marketplace add`, `plugin add --json`, `plugin list --json`;
- https://developers.openai.com/codex/app-server/ — initialization and `skills/list`;
- https://developers.openai.com/plugins/build/plugins — local marketplace roots.

Use a compatible native version and retain its actual version in the receipt. Do not reinterpret marketplace registration as installation or substitute ZIP extraction for native discovery.

## Actual work and genuinely fresh sessions

After native installation/discovery, use the same test CODEX_HOME in an authenticated local Codex session, or install the identical candidate in ChatGPT desktop/Codex. Authenticate through the host's normal login UI. Never paste credentials into Project files, test receipts, or chat. The harness's `ordinary-project/` has only README and AGENTS sentinel text; do not pre-initialize Agnir.

First session request:

```text
Use the installed Svif Skill for this ordinary Project. Create RESULT.md containing exactly "Svif local acceptance passed" followed by one newline. Preserve the original README and AGENTS instructions. Verify the file, checkpoint the resulting Project state, and leave the next action as "Add a second acceptance result". Do not access external providers.
```

Independently inspect the filesystem, not just the model's answer: exact RESULT bytes; a shared stable Project identity in AGNIR.yaml and SVIF.yaml; preserved original instructions; working AGENTS -> README -> AGNIR activation; State, Next Actions and inspectable verification evidence. Retain the native transcript/tool trace and compute file hashes.

End that session. Start a **new** process/chat at the same Project root, without copying the earlier conversation:

```text
Continue this Project using installed Svif and its durable state. Tell me the completed result, its verification, and the next action. Do not change Project files.
```

The new context must independently recover the exact file, verification and next action from durable Project surfaces. Then repeat enablement on this initialized Project: AGNIR.yaml, SVIF.yaml and unrelated README/AGENTS content must remain unchanged; no duplicate identity, locator or instructions may appear.

## Negative fixtures

Run in separate disposable copies, never a live Project:

| Fixture | Required outcome |
|---|---|
| Partial/broken AGNIR artifacts or missing required locator | Explicit repair/blocker; no re-bootstrap or sibling-Project fallback. |
| Intentionally selected other Continuity Provider | Preserve binding; use it only if supported. |
| Failed/missing/wrong-subject required check | No successful completion checkpoint. |
| Effect with missing/null/empty/weaker requested authority | Trusted provider policy still blocks; zero actuation. |
| Unavailable/mismatched observation or terminated effect process | No success claim or blind retry; explicit repair/reconciliation. |
| Existing initialized Project | Stable identity and non-destructive/idempotent enablement. |

Only after these same-revision observations have been reviewed can local **effectiveness** be accepted. Python fixtures and old Preview.1 evidence cannot fill these cells.

## Filesystem recovery boundary

The Python Agnir adapter uses `.svif-continuity.lock`, `.svif-checkpoint.json` (only while a transaction is pending), and `.svif-effect-pending.json` (only while an external attempt is unconfirmed). These are adapter coordination metadata, not a second Project memory protocol. All declared memory locators stay unchanged. Keep journal/attempt files local and protected; do not discard them to make a check pass.

A cooperating reader recovers a prepared transaction to its before-state, or finishes a committed transaction. Conflicting external edits stop recovery without overwriting them. `AGNIR_CHECKPOINT_BUSY` means retry discovery after the other operation finishes. `AGNIR_CHECKPOINT_STALE` requires reload/reconciliation. Unconfirmed effects require independent observation and trusted `effect-reconciliation` authority via `reconcile_effect()`; this never retries delivery. Unknown/absent effects stay blocked for explicit Principal/provider reconciliation.

Multi-file isolation applies to cooperating adapter readers/writers. Direct editors, filesystem watchers, network filesystems, and malicious processes with the same OS permissions are not transaction participants. POSIX path access uses directory descriptors and no-follow opens. Windows uses reparse/link checks and an OS file lock, but does not claim containment against hostile concurrent parent-directory replacement. Native desktop/Windows effectiveness must be evidenced on that surface, not inferred from Linux tests.
