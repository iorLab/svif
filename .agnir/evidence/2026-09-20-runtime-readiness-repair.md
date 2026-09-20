# Svif runtime and local-readiness repair — 2026-09-20

Status: implemented and locally regression-tested candidate; remote/native final receipts
are recorded after observation. Not a release or public submission.

## Source and authority

- Principal request: implement the observed functional gaps to release standard; prioritize
  native local installation/effectiveness and bounded functional completion.
- Canonical baseline: `960526544da308ea8b0eb1d325b26609487ab856`.
- That baseline retains product code audited at `fe7788bd53d3a240f663860133b741799d0470e3`.
- Temporary staging branch: `fix/local-release-readiness`. Canonical target remains `main`;
  Project/lineage/profile/VCS declarations are preserved, not relabeled for staging.
- Exact source export run `35507150590`, artifact `10604905339`, SHA-256
  `2d9a18d5e9df42194cc26256915c03a7aa07422117a6598233dafeaabe48ddbb`.
  Every extracted tracked file was verified against its exported Git blob identity before
  changes or tests. The local workspace Git commit is only test bookkeeping, not source authority.

## Implemented changes

1. Mandatory provider-owned capability policy and trusted verification requirements,
   including advisory model-result separation and rejection of fabricated effect receipts.
2. Complete checkpoint preflight, snapshot CAS, contained no-follow I/O, process/thread
   locks, private write-ahead intent, rollback on normal failure and coherent recovery
   on restart. Named errors preserve blockers and prevent partial success claims.
3. Single-use operation sessions, durable replay checks, pre-actuation uncertainty marker
   and independent effect reconciliation without redeployment.
4. Source-preserving atomic archive builder with negative path/link/size/I/O tests.
5. Installed Skill guidance aligned with trusted-policy and recovery semantics, without
   packaging another runtime. Native Codex acceptance harness and scoped completion matrix.

## Local verification observed

The exact source snapshot first passed the original 87 tests. After repairs, the suite
passes **126 tests** under Python 3.13.5 in the isolated Linux execution environment:

```sh
PYTHONPATH=src python -B -m unittest discover -s tests -q
python checks/check_repository.py
python conformance/check_contracts.py
```

The two structural checks also pass. The new regression tests execute the actual kernel,
bridge and filesystem adapter; they are not solely literal checks of Skill prose.

- `test_release_safety.py`: authority omission/downgrade, injected grants, untrusted success
  declarations, required-verifier coverage, non-effect failures, foreign/reused sessions,
  failed observation, stale/invalid checkpoints before actuation, operation replay and
  durable uncertain-effect recovery on all three supported Agnir lines.
- `test_agnir_transactions.py`: all-role preflight; failures after each of four publication
  writes; actual `os._exit(71)` and recovery in a different Python process; interrupted
  rollback; conflicting edits/corrupt journal; concurrent reader/writer; stale revision;
  exact retry; symlink/hardlink/alias/path protection across 0.1/0.2/1.0.
- Archive tests: unsafe destination/source, missing files, size/count/depth limits,
  prior archive preservation and cleanup after injected I/O failure.
- Harness tests only validate the checker, and are not counted as native host evidence.

All provider transport is dummy, credential-free and non-production. No live deployment,
secret retrieval, real user-machine modification or public publication was performed.

## Preliminary native host observation

Probe run `35507822026`, source `74c2850f08dd9e15d1ff7c0143fb2f3ad379bec1`,
artifact `10603907785` (digest
`2bb14a1fdf4b2016fe70d9a1eca758c9f10cb01f24cb379705a1d12b3c0a4a9e`) used
native Codex `0.155.1` with isolated CODEX_HOME on an Ubuntu runner. Native marketplace
registration and `plugin add svif@svif --json` succeeded; `plugin list --json` reported
Svif 0.2.0 installed=true and enabled=true. The fixture used no model credentials.
This probe used the earlier package bytes and did not verify final-candidate Skill
behavior. Final-candidate exact-byte native install/discovery needs its own receipt.

## Explicit remaining boundaries

- Candidate remote multi-platform CI and final native install/discovery results must be
  freshly observed. Record failures/repairs, not retrospective passing assumptions.
- Actual authenticated model execution of the final Skill, checkpoint, fresh LLM-context
  recovery, idempotency and the negative native-host scenarios remain release gates.
- The adapter's coherent snapshot guarantee requires cooperating API readers; arbitrary
  raw file readers must block on pending markers. Windows trusted-root and local-storage
  constraints are explicit in `spec/RUNTIME_SAFETY.md`.
- Cloudflare's production transport and remote MCP wrapper are not added by this repair.
- Preview.1 remains immutable. The old 0.2.0 package ZIP is not the new Skill candidate.

## Cross-platform candidate repair and acceptance

The exact first candidate tree `c3c642e7ea0c9783f6f3f7a6efd8da016e3ff339`
passed 126 tests plus both checks in source-materialization run `35509048052`.
The runner's attempt to push a workflow-changing staging commit was refused by its
workflow permission; no test failure was hidden. The verified tree was then published
through the authorized connector as `d0f90a6505509b76776b5d4bf0c4b0249c129efb`.
Temporary transfer/probe files are absent from the candidate. PR #11 carries the repair.

Initial PR run `35509114938` passed both Linux runtime jobs, repository/contract checks
and both native installation jobs. It exposed two cross-platform defects: Windows
native separators were incorrectly rejected by the path guard; macOS case-insensitive
storage made the collision test overwrite the existing manifest instead of presenting
two names. Both were repaired, not bypassed. The portable collision test now models
both member names without destroying the physical source and validates real metadata;
explicit native relative/absolute/ADS/escape tests were added. Local suite now passes
128 tests, plus both checks.

Verified repair source: `225e535e32a18bf8db2bfc7d76efe6bed9378e97`.
Verified full tree: `12542123c9ab47e5e938f8db8fd8a7d36f28a513`.
Plugin tree: `7cc90517013306181a4df2238f849b85cf716665` (unchanged by platform fixes).

PR run `35509417968` passed all eight jobs:

- Windows 2022 / Python 3.12 runtime: `106074610910`.
- Ubuntu 24.04 / Python 3.12 runtime: `106074611029`.
- Ubuntu 24.04 / Python 3.13 runtime: `106074610988`.
- macOS 14 / Python 3.12 runtime: `106074610995`.
- repository integrity: `106074610942`; portable contracts: `106074610934`.
- native installation Ubuntu: `106074610931`; macOS: `106074610959`.

Native run artifacts: Ubuntu `10604694096`, digest
`91066b1a1c725dc41763061cf4726816688906b9fb9ae061905a39274c2aeac8`;
macOS `10603999328`, digest
`931d561a202617d58249f197c334ce21070701d4ecd331d93f03d354eaabe8d7`.

The earlier same-Plugin native receipts were independently downloaded and inspected:
Ubuntu artifact `10604249612` and macOS artifact `10604254767` from run `35509114938`.
Their reports identify Codex 0.155.1, installed+enabled Svif, exact cached `svif:svif`
discovery, no discovery errors, and installed file hashes matching the reviewed source.
The package-file-map digest on both is
`55d63f208e230b34c5f8b37a4543c5deb37d8978cfbb85013761b45b7a9d23c6`.
This digest is SHA-256 of sorted JSON containing per-file SHA-256 values, not a Git
subtree or ZIP digest. Native logs use the PR synthetic-merge checkout revision; use
package hashes/tree equivalence, not a moving branch, to establish the installed subject.

Both reports explicitly say `model_exercise: not-run` and
`complete_release_acceptance: false`. No authenticated model task or desktop GUI run
has been performed. The actual task/checkpoint/fresh-LLM-context and negative host gates
remain open; the passing native installation layer must not be generalized beyond it.
A later continuity-only checkpoint may advance the candidate without changing product
code or this Plugin tree. Fresh checkpoint CI/main integration must still be observed.

## PR identity reconciliation

Fresh GitHub readback confirms this work is PR #11 on `fix/local-release-readiness`.
Earlier PR #10 is a different implementation candidate on `fix/local-readiness` at
`043464c6883518fb626bb0ea8e75020be42faf17`; its own evidence records 109 local tests
and no full native-model acceptance. A resume-time PR-number mix-up was corrected in
these records and the PR descriptions. No alternate-candidate source was discarded.
Do not merge PR #10 automatically over the continued repair; review any useful delta
separately before retiring that historical preparation ref.
