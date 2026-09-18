# Svif 0.2.0 public-submission candidate audit — 2026-09-18

Status: **accepted repository/package candidate; not submitted, scanned by OpenAI, reviewed, approved, published, directory-listed, or consumer-installed.**

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

Fresh post-CI readback confirmed authoritative `main` exactly at candidate commit `5a81d7a8b7490a6215d7a27966759fb2656b477a` before the durable checkpoint, with all four version surfaces aligned, OpenAI metadata synchronized, approved logo identity preserved, and the Preview tag still unchanged.

The first durable-checkpoint publication at `fd94894530249e35fd373a7e80004167b08a336e` produced run `35317030008`: repository-integrity and portable-contracts passed, while runtime-kernel failed only because the durable installation-documentation guard expected the stable literal marker `public/personal ChatGPT path` and the checkpoint title had inserted `0.2.0` inside that phrase. The product/package candidate was unchanged. The follow-up repair restores the stable marker while preserving the `0.2.0` candidate semantics.

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


## Directory image blocker discovered after initial candidate CI

A fresh check against the current OpenAI public-directory submission error reference found stricter branding requirements not yet encoded by Svif CI:

- `interface.logo` is required and must reference a square image;
- `interface.composerIcon` is required and must reference a square image;
- raster branding assets must be decodable PNG/JPEG/WebP, at least 48×48, at most 4096×4096, and no larger than 5 MiB.

Fresh inspection of approved Svif exports established:

- `brand/exports/svif-app-icon.png`: 160×155, blob `2db76d3c8ad8bc5fb365b3a17c946f90eecdddca` — approved brand asset but **not square**, therefore unsuitable for the current directory branding fields;
- `brand/exports/svif-favicon-128.png`: 128×128, blob `40dbc1cbca075149cd8fc4e0859f09217b0c3530` — approved, square, and within current dimension limits.

The repair therefore reuses the approved 128×128 favicon byte-for-byte as `plugin/assets/svif-directory-icon.png`, points both required interface fields to it, removes the non-square Plugin-local app-icon copy, and adds repository regression coverage for required paths, byte identity, PNG decoding signature, exact 128×128 dimensions, 48–4096 square bounds, and the 5 MiB file limit.

This is a packaging compliance repair, not a brand redesign.


## Final image-contract repair acceptance

The directory-branding repair was published on authoritative `main` and independently re-read after CI:

- repair commit: `f9026f7e3db4db8956cfc88ba1990daf0757a011`;
- repair tree: `4963f063a7bd3dcb0c05df839e44c10dab7a3f4f`;
- exact repaired Plugin subtree: `5ab4b6147dbd096c052f042b23e37f0ec39f7091`;
- `VERSION`: `0.2.0`;
- portable manifest version: `0.2.0`;
- compatibility-overlay version: `0.2.0`;
- Cloudflare adapter package version: `0.2.0`;
- root and fallback OpenAI interface metadata: exact equality;
- `interface.logo`: `./assets/svif-directory-icon.png`;
- `interface.composerIcon`: `./assets/svif-directory-icon.png`;
- package directory icon blob: `40dbc1cbca075149cd8fc4e0859f09217b0c3530`;
- approved `brand/exports/svif-favicon-128.png` blob: same `40dbc1cbca075149cd8fc4e0859f09217b0c3530`;
- dimensions guarded by tests: 128×128;
- non-square `plugin/assets/svif-app-icon.png`: absent;
- original approved non-square brand export remains unchanged in `brand/exports/`.

Final repair CI:

- workflow run: `35317245771` — success;
- runtime-kernel job: `105511502688` — success;
- portable-contracts job: `105511502989` — success;
- repository-integrity job: `105511503097` — success.

Fresh tag readback also confirmed the immutable Repository Preview boundary remains unchanged:

- `refs/tags/v0.2.0-preview.1`;
- annotated tag object: `2535cb89426c2d38c2e061948e81954a7c7c26d7`;
- peeled released commit remains `2b07b6b5ea0bc8feee59f9f647be9af3069d056e`.

The exact submission candidate is therefore the `plugin/` tree `5ab4b6147dbd096c052f042b23e37f0ec39f7091` as materialized by source commit `f9026f7e3db4db8956cfc88ba1990daf0757a011`. A later durable checkpoint may advance `main` without changing that Plugin subtree; external submission evidence must identify the exact submitted package subject rather than merely a moving branch.

No `v0.2.0` tag, GitHub Release, OpenAI portal submission, scan result, review result, publication, directory listing, or consumer installation is claimed by this acceptance.
