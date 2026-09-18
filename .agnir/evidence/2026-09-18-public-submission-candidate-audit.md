# Svif 0.2.0 public-submission candidate audit — 2026-09-18

Status: **accepted repository/package candidate; not submitted, reviewed, approved, published, or consumer-installed.**

## Candidate subject

- authoritative repository: `iorLab/svif`;
- source before candidate hardening: `466adc41ffc351258556f26f9cc8e207e6d075eb`;
- accepted candidate commit: `5a81d7a8b7490a6215d7a27966759fb2656b477a`;
- accepted candidate tree: `9eb1f2e506f7e057c622ea38ed1bfa6ebb93798c`;
- exact Plugin subtree: `34d2d205455f641b9eca59c0cb4fb9ff43880804`;
- active package/version identity: `0.2.0`;
- submission type: Skills-only; no MCP/App increment.

The exact Plugin subtree is the repository candidate subject. Current OpenAI submission documentation requires the final skill package and the same file tree/instructions used in local testing; it does not make a repository CI result equivalent to portal submission or publication.

## Immutable Preview boundary

The already released Repository Preview remains unchanged:

- tag: `v0.2.0-preview.1`;
- annotated tag object: `2535cb89426c2d38c2e061948e81954a7c7c26d7`;
- peeled release commit: `2b07b6b5ea0bc8feee59f9f647be9af3069d056e`.

The current `0.2.0` package therefore has a new identity instead of reusing the immutable Preview version for changed contents.

## Packaging audit

Fresh authoritative reads after candidate publication confirmed:

- root `VERSION`: `0.2.0`;
- `plugin/plugin.json.version`: `0.2.0`;
- `plugin/.codex-plugin/plugin.json.version`: `0.2.0`;
- `integrations/cloudflare/adapter.json -> adapter.version`: `0.2.0`;
- root `plugin/plugin.json -> extensions.com.openai.interface` exactly equals the compatibility overlay `interface`;
- root portable manifest is the canonical OpenAI metadata source;
- `.codex-plugin/plugin.json` remains compatibility fallback only;
- `plugin/assets/svif-app-icon.png` and `brand/exports/svif-app-icon.png` resolve to the same Git blob `2db76d3c8ad8bc5fb365b3a17c946f90eecdddca`;
- the public candidate remains Skills-only and retains the single shared `plugin/skills/svif/SKILL.md` workflow.

## Current OpenAI submission contract checked

OpenAI documentation checked on 2026-09-18 confirms the relevant current boundary:

- portable packages use root `plugin.json`; portable skills live under root `skills/`; assets may live under root `assets/`;
- OpenAI-specific presentation metadata belongs under root `extensions.com.openai`; a separate `.codex-plugin/plugin.json` remains supported as a compatibility fallback;
- Skills-only public submissions remain supported;
- submission collects listing details, skills, starter prompts, five positive and three negative review cases, intended availability, release notes and policy attestations;
- submitting starts review; approval does not itself publish; explicit publication is a later action;
- published Plugins appear in the universal directory shared by ChatGPT and Codex.

The repository does not claim the external publisher prerequisites are satisfied. The remaining account-side prerequisites are Apps Management: Write in the publishing OpenAI Platform organization and a verified individual developer or business identity in that same organization.

## Verification receipts

Candidate CI:

- workflow: `Svif product checks`;
- run: `35316829755`;
- `repository-integrity`: job `105510201645` — success;
- `portable-contracts`: job `105510201580` — success;
- `runtime-kernel`: job `105510201457` — success.

Fresh post-CI readback confirmed authoritative `main` exactly at candidate commit `5a81d7a8b7490a6215d7a27966759fb2656b477a` before this durable checkpoint, with all four version surfaces aligned, OpenAI metadata synchronized, approved logo identity preserved, and the Preview tag still unchanged.

## Remaining evidence layers

Still unobserved and therefore not claimed complete:

1. publisher permission / identity prerequisites;
2. creation of the real OpenAI submission draft;
3. portal skill/security scan outcome;
4. human/automated review outcome;
5. explicit Publish after approval;
6. directory appearance;
7. real individual-user ChatGPT installation, with ChatGPT Web a first-class target;
8. invocation on a real Project;
9. Agnir activation, verification and durable checkpoint;
10. fresh-context resume from that checkpoint.

No `v0.2.0` Git tag or GitHub Release was created by this audit.
