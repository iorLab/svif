# Plugin first-use continuity bootstrap fix — 2026-08-31

## Problem

Real Codex-test planning exposed a product-logic defect: the repository documentation said Svif should establish Agnir continuity when a selected Project was not yet Agnir-initialized, but the shared `plugin/skills/svif/SKILL.md` only defined operation for an already Agnir-enabled Project. A missing `AGNIR.yaml` therefore fell into discovery failure instead of a first-use onboarding path.

Pre-initializing Agnir manually before the first Svif client exercise would have hidden this defect and would only have tested an already-prepared environment.

## Fix

The shared Svif Skill now distinguishes three states before normal Agnir discovery:

1. **genuinely uninitialized Project** — no Svif continuity binding, no `AGNIR.yaml`, no Agnir activation/memory intent, and no durable selection of another Continuity Provider;
2. **existing but broken Agnir/Svif setup** — repair while preserving the applicable Agnir failure class;
3. **intentional different Continuity Provider** — do not overwrite it with Agnir.

For the founding repository/filesystem path, first-use bootstrap now:

- establishes one stable Project identity, generating and durably persisting a UUID-based URN when no authoritative identity exists;
- initializes Agnir Core `0.1` / `repository-filesystem/0.1` with `AGNIR.yaml`, `.agnir/state.md`, `.agnir/next-actions.md`, `.agnir/decisions.md`, `.agnir/evidence/`, canonical README Agnir instructions, and a minimal non-destructive `AGENTS.md` locator;
- creates/validates a minimal `project-binding/0.2` `SVIF.yaml` with the same Project identity and Agnir continuity binding;
- reruns fresh activation from the selected Project root;
- continues the user's original Project task in the same operation instead of requiring a separate Agnir initialization prompt.

The bootstrap is deliberately self-contained in the Svif Plugin procedure. It consumes Agnir protocol/profile semantics through the founding Continuity Provider integration and does not require the Agnir Skill repository, a prior Agnir installation conversation, GitHub, or another execution surface at runtime.

Bootstrap authority is limited to the non-destructive Project files needed to make the selected Project Svif-operable under the founding binding. It does not grant protected external-effect authority.

## Regression pressure

Added `tests/test_plugin_first_use_bootstrap.py`, covering:

- bootstrap-before-discovery-failure ordering;
- creation of Agnir + Svif durable binding with one Project identity;
- no separate Agnir initialization prompt;
- preservation of existing/conflicting continuity state;
- no overwrite of an intentionally different Continuity Provider;
- no protected-effect authority escalation;
- no runtime dependency on the Agnir Skill repository.

`SVIF.yaml` registers the new regression test and `REPOSITORY_TREE.md` documents it.

## Implementation sequence

- `93b2dde7b3201387298d382c9a588bfcf2f78be6` — implement first-use bootstrap behavior in the shared Skill;
- `e0aab25bc2104c2eab47b652ac8a55bc8ca78bcb` — add first-use bootstrap regression tests;
- `b4de83a3ba94b04d017c2dd3086ad4ff6402e093` — register the test in `SVIF.yaml`;
- `dd5d73d90730d26a9912f9ed66b0ca05a412bd11` — update exhaustive repository tree;
- `b90d1f8976b0e03d2c5a3b70c9bbb4b032c37724` — preserve existing discovery-failure ordering after first-use classification.

An intermediate CI run correctly caught a textual ordering regression in the legacy discovery test: the bootstrap preamble mentioned the literal `AGNIR_DISCOVERY_NOT_FOUND` token before the existing discovery-record ordering assertion. The final fix removed that premature token without weakening the new first-use behavior.

## Validation

Final commit `b90d1f8976b0e03d2c5a3b70c9bbb4b032c37724` passed `Svif product checks` run `33384858568` with overall conclusion `success`.

This is repository/package behavior evidence, not real Codex installation evidence.

## Correct next external exercise

The first real Codex exercise MUST start from an ordinary selected Project with **no pre-installed Agnir and no pre-created `SVIF.yaml`**. Install/enable Svif, invoke it on actual Project work, and observe whether the Plugin itself establishes continuity, continues the task, checkpoints, and supports fresh-context resume.
