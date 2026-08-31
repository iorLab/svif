# Personal ChatGPT distribution checkpoint — 2026-08-31

## Principal product intent

The primary ChatGPT audience for Svif is **individual/personal ChatGPT users**, not managed-workspace administrators.

This changes distribution priority without changing the Svif kernel architecture: ChatGPT remains an Execution Surface, Agnir remains the founding Continuity Provider, and distribution continues to reuse the existing Orchestrator rather than create a second execution kernel.

## Public consumer target

The primary mature ChatGPT path is:

`individual ChatGPT user -> universal Plugins Directory -> install -> invoke Svif in normal ChatGPT use`

The repository-backed OpenAI/Codex GitHub marketplace remains useful for development, managed workspaces, Codex, and secondary evidence exercises, but it is additive/auxiliary rather than the primary ChatGPT consumer distribution path.

ChatGPT Web is a first-class target. A future packaging change that makes Svif Desktop-only is a material product regression unless the Principal explicitly accepts that evidenced tradeoff.

## Verified OpenAI public-submission path

Current OpenAI developer documentation was re-checked on 2026-08-31 and establishes that a public Plugin can be submitted as **Skills only**. Svif therefore does not need an MCP server or Apps SDK package merely to qualify for public Plugin review.

The verified publication sequence is:

1. use an OpenAI Platform organization where the submitter has **Apps Management: Write** permission;
2. complete a verified individual developer identity or verified business identity in that same Platform organization;
3. use the plugin submission portal and choose **Create plugin -> Skills only**;
4. upload the final tested Skill bundle using `.codex-plugin/plugin.json` plus the bundled `skills/` implementation and without adding MCP/App components to that Skills-only submission;
5. supply public listing metadata, starter prompts, review test cases, country/region availability, release notes, and required attestations;
6. submit for review and record automated skill safety/security scan plus reviewer outcome;
7. after approval, explicitly **Publish** the approved version;
8. only after publication verify directory appearance and then perform the real personal ChatGPT install/invocation exercise.

Approval, publication, directory appearance, installation, invocation, and Project checkpoint are distinct evidence layers.

Official sources consulted:

- https://developers.openai.com/plugins/deploy/submission
- https://developers.openai.com/plugins/deploy/submission-errors
- https://developers.openai.com/plugins/build/plugins

OpenAI product and submission details can change; re-verify them before future release claims if the publication action happens substantially later.

## Repository preparation completed

The repository has been aligned to the current Skills-only public-submission model:

- `plugin/.codex-plugin/plugin.json` short description changed to `Durable project orchestration` and the starter prompt was shortened to stay within current public-listing limits;
- `tests/test_plugin_openai_distribution.py` now checks current public-directory listing bounds and asserts that the initial public package remains Skills-only without `mcpServers` or `apps`;
- `plugin/README.md` now documents publisher prerequisites, the Skills-only portal workflow, proposed listing metadata, five positive and three negative review cases, publication/install evidence boundaries, and the auxiliary repository-marketplace route;
- `README.md` and `README.zh-CN.md` now present the universal Plugins Directory as the mature personal ChatGPT path, state explicitly that Svif is not publicly listed yet, and keep the one-line GitHub install intent for development/compatible Agent environments;
- `tests/test_plugin_installation_docs.py` has been rewritten around the public-directory contract rather than the superseded workspace-marketplace-first documentation contract;
- `.agnir/state.md`, `.agnir/next-actions.md`, and `.agnir/decisions.md` now resume at external public submission rather than repeating publication-path research.

Key implementation commits in this sequence include:

- `7fd8c2bf6dd1a6120e88781f712246e563cdc1ff` — public-listing-safe OpenAI manifest metadata;
- `27b74fde368647e3cfb459262e6c83f14e093ffc` — public-directory metadata tests;
- `9453ea3c1b37800de1bfc1996ed639612ae00874` — public Skills-only submission guidance and review cases;
- `c9867c0c5e76b8a7bebed8437846c66dcf8529d5` / `e5f22f407b02ef565aaa82ede1d4ea58da2cadb6` — synchronized English/Chinese personal ChatGPT onboarding;
- `15f249968dcbcd35e97d9d4b90234bd04a6502ac` and `6f577a1856ec2d935cc19517a1df6dc46f884636` — installation-documentation contract migrated from workspace-first wording to public-directory semantics and stabilized.

## Validation

The repository-side public-submission-readiness baseline at commit `6f577a1856ec2d935cc19517a1df6dc46f884636` passed `Svif product checks` run `33373725911`:

- `repository-integrity`: success;
- `runtime-kernel`: success;
- `portable-contracts`: success.

The earlier personal-user distribution correction was also validated at commit `c87e209049ead2e67056d688e853c3be9b7883a3` by run `33372657758`, with the same three jobs successful.

The Agnir activation chain remains readable from root `AGENTS.md` through `README.md` and `AGNIR.yaml` to the declared durable state and next-action locations.

## Current external boundary

The next meaningful step is no longer speculative package work. It is an external publisher action in the OpenAI Platform submission portal using an organization/account with the required Apps Management permission and verified publisher identity.

Until the portal submission is actually performed, Svif must not claim:

- OpenAI skill scan success;
- review approval;
- public publication;
- universal Plugins Directory availability;
- personal ChatGPT installation or invocation success.
