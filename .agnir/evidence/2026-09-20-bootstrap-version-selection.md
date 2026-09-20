# Svif first-use Agnir version-selection repair — 2026-09-20

Status: version-selection implementation plus executable checker and native installation gates accepted for the PR #13 candidate; authenticated model behavior and whole-release sign-off remain pending. OpenAI Platform publication remains paused.

Principal correction: Svif must not pin all new/current Projects to Agnir Core/profile `0.1`. Existing Project truth wins. A valid existing Agnir Project keeps the Core/profile it declares; adding Svif creates/validates a matching continuity binding and does not authorize compatibility migration. Partial or contradictory Agnir artifacts remain repair cases.

Only a genuinely uninitialized Project resolves the canonical latest published stable Agnir at operation time. Stable means a published non-prerelease tag/Release, never moving `main`, RC, untagged source, stale model memory, or fallback to the old Svif Preview baseline. Package SemVer and Core/profile compatibility remain separate.

Current external observation on 2026-09-20: `iorLab/agnir` latest published stable is repository release `v1.0.2` at revision `b5626394ec40a5cb7a28c01892acde07cc0adc8e`; that release still declares Core `1.0` and `repository-filesystem/1.0`. This receipt is evidence of today's resolved stable, not a hard-coded future bootstrap constant. Future first-use operations must resolve latest stable again.

The immutable Svif `v0.2.0-preview.1` release is not modified. It remains historical evidence with its original `0.1` bootstrap behavior. The current unpublished `0.2.0` Skill is the first Svif line to supersede that rule.

## Completed acceptance implementation

The initial selection rule reached main at `9501fd7ed0843f46882ee63ed9c19cd2759a7cb2`
(run `35519581944`, success). Follow-up inspection found that the native exercise still
prohibited model network lookup and only compared Project identity after bootstrap;
it did not verify that the new Project matched an independently resolved latest stable.
The actual Agnir adapter already supports 0.1/0.2/1.0; no runtime default change was needed.

The completed candidate is `08f2c7c7581edb8845cea161b971a0c4dca2de4d` on temporary
`fix/bootstrap-acceptance`, PR #13. Exact tree:
`3c053b2371f0fe916379ac7ea2f74ce1eb4bad3f`.
Exact Plugin tree: `77953ba954b2c0f3ff7dcc6f9c7814df5fa05e12`.

`checks/check_local_install.py` now resolves latest stable only for a new-Project model
exercise, verifies release/tag/commit and each source file's Git blob hash, obtains the
matching installer/Core/profile/schema/activation files and provides the model a fresh
same-operation source snapshot outside the still-uninitialized Project. It does not
relax the model sandbox or copy the source repository's Project identity/memory. The
independent result checker enforces Agnir/Svif identity and compatibility/profile,
applied package/source/revision provenance and selected-release activation locator.
The no-auth install path performs no Agnir lookup. Existing-Project validation is
read-only, supports 0.1/0.2/1.0 and does not require optional historical package provenance.
Unavailable or unsupported latest stops; it is never replaced with an older release.

The shared Skill, bilingual first-use diagrams, repository map and acceptance matrix
agree with these rules. This repository's existing Agnir activation, compatibility,
identity, lineage, selector, memory locators and applied v1.0.0 provenance are preserved.

## Verification receipts and boundaries

- Local full suite: 141 tests, success. Repository integrity, portable contracts and
  diff checks pass. New executable fixtures cover stable/package version separation,
  old-Project preservation, binding/provenance mismatches, RC/unpublished targets,
  unsupported compatibility, corrupt source and unavailable latest. Fixtures are
  checker regression evidence, not native-model behavior.
- PR run `35520792408`: all eight jobs succeeded for the candidate, including runtime
  on Linux (Python 3.12/3.13), macOS (3.12) and Windows (3.12), plus repository integrity,
  portable contracts and native Codex installation/discovery on Linux/macOS.
- Native synthetic merge checkout: `ddbc9b1d51a8701f51ee83c9cde6152d0e559384`.
  Linux artifact `10608285647`, outer digest
  `5102d99af3518ce903092aaf5ff4f6da428dd6ac1582a5dd49b7f2351919dea1`;
  macOS artifact `10607959357`, outer digest
  `024b0ac82e0df4416b608c55ee347af145460fac557c9d46d1e0cc0efe4b8efc`.
  Both were downloaded and compared to ALL candidate Plugin source file hashes.
- Actual host: Codex CLI 0.155.1 on Linux and macOS. Installation, enabled state and
  installed Skill discovery passed. Package-file-map SHA-256:
  `4e6ccce8405606f260d010d058622b1f32eeafdb59501658ea75d971a621ed81`.
  Both reports retain `model_exercise: not-run`, `complete_release_acceptance: false`.
- Exact generated inner `svif-0.2.0.zip` SHA-256:
  `08ad8bb13657c359d799d66c9adafcd552f8d6afdd27ed1ad96d4e34e093911b`.
  Its regular-file map was independently compared byte-for-byte to this Plugin tree.

## Actual upstream observation and auxiliary workflow failures

One-shot validation run `35520533567` passed 141 tests and both structural checks,
resolved actual canonical Agnir v1.0.2, built the exact ZIP and materialized the tested
Git tree. Its final summary command incorrectly used `git rev-parse :plugin` and failed.
The run as a whole is a failure, NOT a green pipeline claim. Artifact `10607369559`
retains the real tests, live-resolution receipt, ZIP and checksum. Outer artifact digest:
`35970da37830902b13034c56060ba3bd4af62eaa91df78bd9e7e33d9c8f83857`.

The live resolver observed at `2026-09-20T15:44:51.613206+00:00`:
release `v1.0.2`, publication `2026-09-18T14:14:18Z`, release ID `391529372`, exact commit
`b5626394ec40a5cb7a28c01892acde07cc0adc8e`, Core `1.0`,
profile `repository-filesystem/1.0`, activation `AGNIR.md`. Eight source files were
retrieved from that exact commit and verified. This is today's source observation,
not a pinned future default and not proof of a model executing the installer.

After correcting the summary command, run `35520615978` passed tests but encountered
GitHub public API HTTP 403 rate limiting at latest lookup. It stopped as designed,
without fallback or target initialization. This auxiliary run also remains a failure.
The completed tree was independently read back through the authorized GitHub connector
and validated by the separate fully green PR suite. The one-shot transfer/verification
workflow is absent from the accepted product tree; it is not a new runtime dependency.

## Outstanding release gate

Authenticated positive/negative native behavior on this exact changed Skill still
needs actual observations. Existing-Project versions must remain unchanged in those
exercises; new Projects must match stable resolved in that operation. Passing source,
checker, archive or no-auth install tests cannot replace these observations.
No v0.2.0 tag, public Release, Platform submission/Publish or live Cloudflare effect is
created or authorized. Released Preview history remains immutable.
