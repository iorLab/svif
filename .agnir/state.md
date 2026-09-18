# Svif Current State

Svif is the authoritative active **Project orchestration product** in `iorLab/svif`. Authoritative `main` now carries the Principal-approved brand identity and the Principal-authorized Agnir Core/profile `0.2` → `1.0` Project promotion. The former `iorLab/svif-cloudflare-reference` project is retired.

## Product state

- Svif product line remains `0.2`.
- Project Binding remains `project-binding/0.2`.
- Software Delivery remains `software-delivery/0.2`.
- Capability Adapter remains `capability-adapter/0.2`.
- Evidence Record remains `evidence-record/0.2`.
- Current authoritative `main` carries the accepted **unpublished `0.2.0` public-submission candidate**. The exact package subject was materialized by repair commit `f9026f7e3db4db8956cfc88ba1990daf0757a011`; its exact Plugin subtree is `5ab4b6147dbd096c052f042b23e37f0ec39f7091`. Later continuity-only checkpoints do not change that Plugin subject.
- Released Repository Preview `v0.2.0-preview.1` remains immutable at commit `2b07b6b5ea0bc8feee59f9f647be9af3069d056e`; it is a distinct historical release subject.
- The released **Plugin MVP** / Preview.1 first-use bootstrap remains separately versioned on Agnir Core/profile `0.1`; the repository self-host promotion did not retroactively rewrite that release.
- Real Codex CLI and ChatGPT desktop/Codex Preview acceptance evidence remains valid.
- The public/personal ChatGPT path remains a separate distribution obligation. The repaired `0.2.0` repository/package candidate is accepted: product-check run `35317245771` passed repository-integrity, portable-contracts, and runtime-kernel after the directory-image repair; the final acceptance checkpoint run `35317410100` also passed all three jobs. OpenAI submission, automated scan, review, approval, explicit Publish, directory appearance, personal ChatGPT installation, invocation, checkpoint, and fresh-context resume remain separate unobserved layers.
- Root `plugin/plugin.json -> extensions.com.openai` is the canonical OpenAI metadata source; `.codex-plugin/plugin.json` is a synchronized compatibility fallback. Both required `interface.logo` and `interface.composerIcon` resolve to package-local `plugin/assets/svif-directory-icon.png`, byte-identical to the approved 128×128 `brand/exports/svif-favicon-128.png` at Git blob `40dbc1cbca075149cd8fc4e0859f09217b0c3530`.
- As of 2026-09-18, current OpenAI developer documentation still accepts **Skills-only** public Plugin submissions; MCP/App packaging is not a publication prerequisite for Svif's current package shape.
- The repository-side submission archive gate is now accepted. `checks/build_submission_bundle.py` deterministically packages the exact accepted `plugin/` tree without changing it, and `tests/test_plugin_submission_bundle.py` verifies byte-exact tree mirroring plus current archive size/path/normalization limits. Repair run `35334113062` passed repository-integrity, portable-contracts, and runtime-kernel. A one-shot exact-tree build then produced inner portal ZIP `svif-0.2.0.zip` with SHA-256 `bc2315562f7bdeb4232aadb9b583a7442f8cd868dbeacd13bb57caf0c785177c` in successful run `35334437819`, artifact `10542750132`; the workflow asserted `HEAD:plugin == 5ab4b6147dbd096c052f042b23e37f0ec39f7091` before packaging and `unzip -t` passed. Evidence: `.agnir/evidence/2026-09-18-skills-only-submission-archive.md`.
- The remaining account-side submission prerequisites are **Apps Management: Write** in the publishing OpenAI Platform organization plus a **verified developer or business identity** in that same organization; approval and explicit Publish remain separate later observations.
- Live Cloudflare delivery remains disabled unless explicitly authorized.
- `README.md` and `README.zh-CN.md` remain synchronized user/Agent entry points.

## Product architecture

Svif continues to coordinate four first-class components: Orchestrator (`src/svif/runtime.py`), Continuity Provider (`src/svif/continuity/agnir.py`), Execution Surface (`src/svif/execution/chatgpt.py`), and Capability Provider (`src/svif/capabilities/cloudflare.py`). The Project persists; Executors and execution environments may change. No execution surface owns canonical Project truth merely because execution occurred there.

## Canonical Agnir compatibility — Core/profile 1.0 accepted 2026-09-07

The Principal explicitly authorized the Svif Project to perform the separately governed, semantics-preserving Agnir Core/profile `0.2` → `1.0` promotion. That promotion is now accepted on authoritative `main`.

Current authoritative continuity is:

- Project identity: `urn:svif:project:svif-core` — preserved;
- Agnir Core: `1.0`;
- discovery profile: `repository-filesystem/1.0`;
- authoritative logical lineage: `urn:svif:lineage:authoritative` — preserved;
- VCS selector: `refs/heads/main` — preserved;
- durable locators: `.agnir/state.md`, `.agnir/next-actions.md`, `.agnir/decisions.md`, `.agnir/evidence/` — preserved;
- Agnir operational release: `1.0.0`;
- immutable applied Agnir revision: `6d16dcfd17b8e9f22fd25804e22b9f8a516d06c3`.

`SVIF.yaml` still declares Svif `0.2` / `project-binding/0.2`, while its Agnir continuity binding is now compatibility/profile `1.0` / `repository-filesystem/1.0`. The promotion therefore changed the Continuity Provider compatibility line without changing the Svif product version or Project Binding version.

The Svif Agnir filesystem adapter now supports historical `0.1` and `0.2` compatibility plus stable `1.0`; Core/profile `1.0` uses the accepted lineage and VCS-selector semantics already stabilized from `0.2`.

## Promotion receipts

- captured authoritative source: `a00ad6ed9f18abddbed1979a619f932350cefe54`;
- source Core/profile: `0.2` / `repository-filesystem/0.2`;
- complete promotion candidate: `5a88eee4bc214b8da3b4c5f48640067b167248b8`;
- successful staging/preservation/full-test run: `34076031454`;
- PR: `#9`;
- final PR synthetic-merge product checks: run `34076166897`, repository-integrity / portable-contracts / runtime-kernel all success;
- fresh pre-publication stale check: authoritative `main` still exactly `a00ad6ed9f18abddbed1979a619f932350cefe54`;
- authoritative squash merge: `5da0eb76e38e817ba0f5111ce2b08750afa3b9c3`;
- authoritative post-merge product checks: run `34076249501`, all three jobs success;
- fresh post-publication reads: `AGNIR.yaml` and `SVIF.yaml` both resolve the new 1.0 continuity binding while identity, lineage, selector and locators remain unchanged;
- immutable Preview tag object remains bound to released commit `2b07b6b5ea0bc8feee59f9f647be9af3069d056e`.

The promotion candidate branch `promotion/agnir-1.0` final tip `5a88eee4bc214b8da3b4c5f48640067b167248b8` is recorded in `history/BRANCH_ARCHIVE.md`. Retirement workflow run `34076414723` succeeded, the one-shot workflow removed itself, and the branch ref is no longer present. `main` remains the intended long-lived authority.

## Canonical brand identity

The Principal-approved 10:42 AM Svif identity system remains canonical on `main` through PR #5 / integration commit `77ff3d0e8b3d0d691bb47529e065571c17a0aa81`. Byte-exact approved references, fidelity-first raster masters, complete delivery exports, symmetric 13/13 QA and deterministic rebuild tooling remain repository-resident. The Agnir 1.0 promotion did not modify brand assets.

## Historical compatibility

The earlier published-Agnir migration from Core/profile `0.1` to `0.2` remains durable history and regression coverage. The current adapter continues to support historical 0.1/0.2 Projects while the Svif repository itself now self-consumes Core/profile 1.0. Installing or releasing a newer Svif distribution must not silently rewrite a Project's declared Agnir compatibility line.

## Current focus

No Agnir 1.0 promotion or brand integration gate remains open. The real downstream 1.0 promotion is already recorded in Agnir as accepted post-1.0 adoption evidence at `iorLab/agnir/.agnir/evidence/2026-09-07-svif-agnir-1.0-adoption.md`; that handoff is complete. Material work now returns to Svif distribution/adoption: preserve released Preview evidence, keep any future bootstrap compatibility change in a new Svif release, satisfy the OpenAI Platform publisher prerequisites, submit the exact accepted `0.2.0` Skills-only Plugin subject `5ab4b6147dbd096c052f042b23e37f0ec39f7091` for review, explicitly Publish after approval, then validate a real personal ChatGPT installation/checkpoint/resume path. Historical draft PR #3 is closed unmerged; its validation branch tip is recorded for explicit ref retirement. Candidate audit evidence is `.agnir/evidence/2026-09-18-public-submission-candidate-audit.md`; deterministic submission-archive evidence is `.agnir/evidence/2026-09-18-skills-only-submission-archive.md`. The exact accepted Plugin subtree remains `5ab4b6147dbd096c052f042b23e37f0ec39f7091`; archive tooling added outside `plugin/` does not create a new package subject. No `v0.2.0` tag, GitHub Release, OpenAI submission, or public listing has been created. Protected Cloudflare delivery remains separately authorized.

`.agnir/next-actions.md` is the canonical ordered resume plan.
