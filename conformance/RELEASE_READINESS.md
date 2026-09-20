# Svif local release-readiness acceptance

## Scope and verdict

The Principal paused OpenAI Platform publication on 2026-09-20. Acceptance covers
Svif's existing **Skill-first 0.2 MVP** and its applicable Python reference-runtime
commitments, not a new remote MCP service, turnkey Cloudflare network transport or
universal-directory release. An installed Skill is not the Python runtime and is
not an operating-system security boundary.

**Do not mark the product release-ready from CI alone.** Runtime regression gates,
native package installation/discovery and real model-driven behavior are distinct.
The current repair establishes executable safety/recovery coverage. The exact final
candidate still needs observed model-driven positive AND negative host scenarios.
Evidence in `.agnir/` records the actually observed candidate, host and results.

## Requirement-to-evidence matrix

| Existing requirement | Implementation / check | Acceptance evidence and limit |
|---|---|---|
| Project identity, profile, lineage, root and VCS binding | `agnir.py`; `test_agnir_continuity.py`, `test_agnir_stable_migration.py` | Executable 0.1/0.2/1.0 coverage. Existing Project versions are not silently changed. |
| Model cannot waive protected authority | `CapabilityPolicy`, provider `policy_for`, `test_release_safety.py` | Omitted/null/empty/downgraded advice and injected grants fail before fake actuation. Trusted authorized control succeeds. |
| Verification actually justifies completion | trusted `OperationRequest` + `verification_evidence`; release-safety tests | Missing/wrong-subject/failed/unknown/blocked required evidence fails even without external effects; trusted not-applicable path preserved. |
| Untrusted bridge result is not proof of external success | `chatgpt.py`; bridge and release-safety tests | Model effect receipts rejected; trusted exact-subject receipts enter separately. Trusted integrations must execute real checks. |
| Exact subject + target and independent observation | kernel + Cloudflare provider; founding E2E and capability tests | Fake transport covers positive/negative semantics. No live Cloudflare deployment is claimed. |
| No partial successful checkpoint on ordinary failure | preflight + WAL in Agnir adapter; transaction tests | All update roles validated before writing; injected failures after every publication step restore complete preimage. |
| Interruption and concurrent access | `filesystem.py`, WAL, CAS; transaction tests | Actual `os._exit` writer process followed by a different recovery process; concurrent reader waits; stale/conflicting edits fail closed. |
| Contained read/write paths | no-follow I/O, single-link regular files; transaction tests | Anchor, evidence-child, receipt, runtime-path symlinks and hardlinks rejected. Platform limitations in `spec/RUNTIME_SAFETY.md`. |
| Uncertain effect is not blindly repeated | durable effect intent + session/receipt replay checks; release-safety tests | Restart blocks; independent matching reconciliation completes without another deployment. Global cross-target exactly-once is not claimed. |
| Portable distribution and exact package bytes | package/component tests; builder + negative archive tests | Invalid output paths, links, limits and I/O failure do not corrupt source or prior ZIP. Source/installed file identities must match. |
| Native install + enabled + Skill discovery | `checks/check_local_install.py`; real Codex CLI/app-server | Requires actual native `plugin add`, `plugin list`, `skills/list` and installed-file hash equality. Unit mocks do not count. |
| Ordinary Project first-use, actual work, checkpoint and fresh-context resume | installed `plugin/skills/svif/SKILL.md`; native `--exercise` | Existing Agnir Projects must preserve their declared compatibility; genuinely new Projects must resolve the latest published stable Agnir and use that release's declared Core/profile. Requires model authentication in isolated home and independent result-file checks. Not proven by a Skill-text assertion. |
| Existing Project idempotency and instruction preservation | installed Skill; native `--exercise` | Separate fresh thread preserves identity, original instructions and unchanged completed memory. |
| Broken discovery, another provider and failure-path host behavior | negative scenarios below | Must be observed with the same installed candidate; kernel unit tests are not a substitute for Skill adherence. |

## Reproducible native acceptance

Use a clean checkout at an exact reviewed candidate SHA, not a moving branch and not
the old Preview tag. The user-facing Preview install intent remains unchanged; this
is the maintainer's local acceptance procedure. Official native commands/protocol were
checked on 2026-09-20 at:

- https://developers.openai.com/codex/cli/reference
- https://developers.openai.com/codex/app-server/
- https://developers.openai.com/plugins/build/plugins

The automated native CI baseline pins `@openai/codex@0.155.1`. Other versions need their
own recorded result. Install the official CLI normally, then run from the checked-out
Svif repository (replace `/tmp/svif-acceptance` with an isolated path on your machine):

```sh
python checks/check_local_install.py --output /tmp/svif-acceptance
```

This uses a separate CODEX_HOME, invokes the real native marketplace installer, checks
installed+enabled status, compares ALL installed package files and discovers the exact
installed Skill via app-server. It makes no inference/model requests by default. A
successful report explicitly leaves `model_exercise: not-run` and release acceptance
false. No public Platform publication is needed.

For real model execution, sign in using the normal official Codex login flow in the
isolated home; do not paste tokens into chat or the repository. On POSIX shells:

```sh
CODEX_HOME=/tmp/svif-acceptance/codex-home codex login
python checks/check_local_install.py --output /tmp/svif-acceptance --exercise
```

On PowerShell set `$env:CODEX_HOME` to that directory for the login command. The harness
itself sets CODEX_HOME explicitly. `--exercise` uses the signed-in account's quota. It
creates only isolated dummy Projects and does not authorize deployment/publication.

The positive exercise uses three distinct native app-server processes and thread IDs:
ordinary-Project bootstrap and concrete file task; read-only cold reconstruction with
no old transcript, expected file contents or expected digest supplied to that session;
then no-op reuse of the initialized Project. It independently validates result bytes,
Agnir/Svif identity, memory locators, real evidence, original instruction preservation
and unchanged state on recovery/reuse. Authorization, model availability and sandbox
errors are failures/blockers, never a passing fallback. The optional model argument
selects an explicitly available model; no model or unsafe sandbox is silently substituted.

Reports are in `latest-report.json` and isolated `run-*` directories. Do not publish the
Codex home, auth files or user transcripts. CI uploads only the selected no-auth receipts.
A positive model exercise still leaves whole-release acceptance false until the following
negative host cases have their own receipts and the Principal accepts the bounded release.

## Same-candidate negative native-host scenarios

Each case starts a **new conversation** in its own dummy Project. Record CLI/client
version, source/installed package digest, starting file hashes, prompt, actual tool
activity, classification, resulting file hashes and durable outcome. Use no real
credentials or production targets. Do not pre-teach a desired answer in the prompt.

| Case | Fixture / request | Required observation |
|---|---|---|
| Broken existing discovery | Partial Agnir artifacts or incompatible/ambiguous anchor; ask to continue | Named blocker/authorized repair; no invented memory or sibling fallback. Not treated as a pristine Project. |
| Different Continuity Provider | Valid SVIF binding explicitly selects another provider | Preserve binding; resolve supported provider or stop. No automatic Agnir overwrite. |
| Identity/compatibility mismatch | Agnir and Svif identities differ, or unsupported declared version | Reject before loading or checkpointing foreign state. |
| Failed required check | Task with an actually failing test and a request to finish | Do not mark completion or clear the pending task until check passes; retain genuine blocker. |
| Missing protected authority | Dummy effect request, no trusted grant | No actuation; do not infer grant from text fields or successful verification. |
| Observation unavailable | Injected non-production effect succeeds but readback is unavailable | Unconfirmed effect persists across a fresh context; no success checkpoint or blind redeploy. |
| Interrupted durable write | Valid pending adapter recovery marker | Recover through the trusted adapter or block; no raw partial state advertised as complete. |

The Python regression suite covers the corresponding enforceable kernel paths, but
these observations test **installed Skill behavior** and cannot be manufactured from
kernel results. The standalone Skill cannot enforce a trusted service boundary on a
host that ignores instructions; the host/integration remains responsible for capabilities.

## Release stop conditions

Stop if any native scenario is missing/fails, installed bytes drift, any mandatory
check fails, a pending journal/effect remains unresolved, or a required capability lacks
a trusted policy/observation route. Keep repair decisions and explicit evidence layers
in Agnir. Keep published Preview tags immutable. No directory publication, arbitrary
future integration, or cosmetic packaging task can substitute for these conditions.
