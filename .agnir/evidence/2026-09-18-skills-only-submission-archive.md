# Svif Skills-only submission archive acceptance — 2026-09-18

Status: **accepted repository-side submission-archive gate; no OpenAI portal submission is claimed.**

## Exact package subject

The public-submission package subject remains unchanged:

- product/package version: `0.2.0`;
- materializing commit: `f9026f7e3db4db8956cfc88ba1990daf0757a011`;
- exact Plugin subtree: `5ab4b6147dbd096c052f042b23e37f0ec39f7091`;
- package root: `plugin/`;
- submission type: Skills-only;
- released Preview remains separately immutable as `v0.2.0-preview.1`.

A fresh comparison from `f9026f7e3db4db8956cfc88ba1990daf0757a011` to the archive-gate head found **no changed path under `plugin/`**. The builder and archive tests therefore validate transport of the accepted package rather than create a new Plugin subject.

## Deterministic archive builder

Repository tooling now includes:

- `checks/build_submission_bundle.py`;
- `tests/test_plugin_submission_bundle.py`.

Canonical build command:

```bash
python checks/build_submission_bundle.py --output svif-0.2.0.zip
```

The builder:

- reads only the accepted `plugin/` tree;
- rejects symlinks;
- writes package members directly at ZIP root, so `plugin.json` remains the plugin-root manifest;
- uses sorted paths and a fixed ZIP timestamp for deterministic bytes;
- emits a SHA-256 digest for the generated archive;
- does not mutate `plugin/` or Project continuity.

The archive test proves the ZIP's regular-file map is byte-for-byte identical to the source `plugin/` regular-file map.

## Current archive guards

The repository-side gate encodes the currently documented public-submission ZIP boundary used for this candidate:

- compressed archive size <= 100 MiB;
- regular-file entry count <= 5,000;
- each member <= 100 MiB;
- aggregate uncompressed regular-file size <= 512 MiB;
- member paths use relative forward-slash form;
- no leading/trailing path whitespace;
- no empty, `.`, or `..` path segments;
- path depth <= 20 segments;
- no Unicode-NFC + case-fold path collisions;
- required `plugin.json`, `skills/svif/SKILL.md`, and approved package icon are present;
- no MCP/App packaging is introduced.

These checks are repository/package evidence only. The real OpenAI ingestion pipeline may still reject a submitted archive for a rule not represented here; any such result becomes new external evidence and must be reconciled rather than overridden.

## Verification receipts

Initial archive-gate commit:

- commit: `20e076aa66f38d75e5a603995594aaecd2ce41c0`;
- workflow run: `35334016729` — success.

The first hard-limit expansion commit `5ff34253cb1e7d74fc806543a1fcc6b84ca48793` exposed a builder-local `NameError` because the new constants/import were incompletely materialized. Repository-integrity and portable-contracts remained green; runtime-kernel correctly failed the new archive tests. No `plugin/` bytes changed.

Repair:

- commit: `a4ace22ed2f8c2f785b85fd7963d7e1d8745c959`;
- workflow run: `35334113062` — success;
- portable-contracts job: `105564901686` — success;
- runtime-kernel job: `105564901881` — success;
- repository-integrity job: `105564901919` — success.

Fresh compare after repair confirmed no `plugin/` changes relative to the accepted package materialization commit.

## Remaining external layers

Not yet observed and therefore not claimed:

1. Apps Management: Write for the publishing OpenAI Platform organization;
2. verified developer or business identity in that organization;
3. real portal draft creation;
4. upload of the generated exact candidate archive;
5. OpenAI scan / ingestion result;
6. review outcome;
7. explicit Publish after approval;
8. universal Plugins Directory appearance;
9. real personal ChatGPT installation and invocation;
10. Agnir checkpoint and fresh-context resume on that public surface.

No `v0.2.0` Git tag or GitHub Release is created by this archive gate.
