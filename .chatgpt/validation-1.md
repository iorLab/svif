# Validation Project #1 — mattamior/agent-skills

## 2026-08-27 — Fresh-conversation resume failure

### Setup

- Fresh ChatGPT Project with Project-only memory.
- Project Instructions intentionally left blank at initialization.
- ZeroLocal source supplied as `iorLab/zerolocal`.
- Target repository supplied as `mattamior/agent-skills`.
- First run created repository RPM on `feat/skill-gallery-cloudflare`, implemented the gallery, opened PR #1, and checkpointed state.

### Evidence

- Target RPM manifest exists on `feat/skill-gallery-cloudflare` at `.chatgpt/project-memory.yaml`.
- Target RPM did not exist on the default `main` branch at the time of the resume test.
- The target PR head later advanced to `d1cbfff421db187a9eaf75e094ed80e44f206c3e` and its `Validate skills` workflow completed successfully.
- A new conversation in the same ChatGPT Project did not recover the target repository/working ref/RPM automatically and behaved as if project history were absent.

### Classification

`RPM/bootstrap discovery`

RPM persistence succeeded, but fresh-context discovery failed. The repository-backed state was durable yet unreachable because no durable conversational bootstrap pointer identified the canonical repository, RPM manifest, and non-default authoritative RPM ref.

### Root cause

The v0.1 RPM contract required resumable repository state but did not require a durable entry pointer from a fresh conversational context into that state. The Core Skill likewise created RPM without ensuring that the surrounding ChatGPT Project retained locator-only bootstrap instructions.

### Required repair

- Specification: require durable bootstrap discovery and non-default RPM ref resolution.
- Core Skill: establish a locator-only bootstrap pointer after creating/adopting RPM; verify it at Checkpoint.
- Failure taxonomy: add `RPM/bootstrap discovery`.
- Conformance: add structural checks for the new contract.
- Validation target: after the fix is merged, add the minimum Project Instructions pointer and repeat the fresh-conversation resume test without restating project history.

### Status

Repair implemented on ZeroLocal branch `fix/rpm-bootstrap-resume`; fresh-conversation retest remains pending until the fix is verified/merged and the validation project's minimal bootstrap pointer is configured.
