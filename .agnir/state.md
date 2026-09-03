# Svif Current State

Svif is the authoritative active **Project orchestration product** in `iorLab/svif`. This target state accepts the validated published-Agnir migration result into authoritative `main` while preserving target-owned continuity. The former `iorLab/svif-cloudflare-reference` project is retired.

## Product architecture

Svif continues to coordinate the same four first-class components: Orchestrator (`src/svif/runtime.py`), Continuity Provider (`src/svif/continuity/agnir.py`), Execution Surface (`src/svif/execution/chatgpt.py`), and Capability Provider (`src/svif/capabilities/cloudflare.py`). The Project persists; Executors and execution environments may change. No execution surface becomes canonical Project truth merely because execution occurred there.

## Released Svif product state

- Svif product line: `0.2`.
- Released Repository Preview: immutable `v0.2.0-preview.1` from commit `2b07b6b5ea0bc8feee59f9f647be9af3069d056e`.
- Project Binding: `project-binding/0.2`.
- Software Delivery profile: `software-delivery/0.2`.
- Capability Adapter: `capability-adapter/0.2`.
- Evidence record: `evidence-record/0.2`.
- The released **Plugin MVP** / Preview.1 first-use bootstrap remains on its published Agnir Core/profile `0.1` baseline until a later Svif distribution intentionally changes that onboarding contract.
- The real **Codex CLI** and **ChatGPT desktop/Codex** Preview acceptance evidence remains valid and the released tag remains immutable.
- The separate public/personal ChatGPT path remains externally blocked at publisher verification/payment-method eligibility; repository CI is not personal **ChatGPT Web** installation evidence.
- Live Cloudflare delivery remains disabled unless explicitly authorized.
- `README.md` and `README.zh-CN.md` remain synchronized user/Agent entry points.

## Authoritative Agnir compatibility target — 2026-09-03

This target state upgrades the Svif Project itself from published Agnir `v0.1.1` / Core-profile `0.1` to published stable Agnir `v0.2.0` / Core-profile `0.2`.

Target-owned continuity is:

- Project identity: `urn:svif:project:svif-core` — unchanged;
- Agnir Core: `0.2`;
- profile: `repository-filesystem/0.2`;
- authoritative logical lineage: `urn:svif:lineage:authoritative`;
- VCS selector: `refs/heads/main`;
- durable locators: `.agnir/state.md`, `.agnir/next-actions.md`, `.agnir/decisions.md`, `.agnir/evidence/` — unchanged;
- Agnir operational release: `0.2.0`;
- immutable applied revision: `fc84095ed5d500be9e1b43a4af0e93356571bbd4`.

`SVIF.yaml` declares the same Project identity, Core/profile compatibility, logical lineage and VCS selector binding. Logical lineage identity is not derived from the branch ref or commit receipt.

## Real downstream migration evidence accepted as integration input

Captured pre-migration authoritative main: `dac058789a27f32f4ed1949874c1954f31f12bd8`.

Validated migration source: `267f3d706e4fba67f2fb4a3a7ea33e80b9fb48ef`, tree `d6ffec2fddc48ec0052dd0531ca0088fb13b37b2`.

The migration line demonstrated:

- explicit published `v0.1.1` / Core `0.1` -> published `v0.2.0` / Core `0.2` migration;
- Project identity and memory-locator preservation;
- separate logical lineage and VCS selector binding;
- dual-line 0.1/0.2 adapter support and retained 0.1 regression pressure;
- current Svif self-host binding `0.2` kept distinct from immutable Preview.1 first-use bootstrap `0.1`;
- repository integrity, runtime/unit tests, founding E2E/Plugin regression surface and portable contracts all green.

Final migration-source checkpoint run `33724859300` passed repository-integrity, runtime-kernel and portable-contracts. Earlier exact PR-head run `33724576017` also passed all three jobs. Before that checkpoint, PR #6 synthetic merge tree matched the source head tree exactly; no server-side content rewrite occurred.

The migration source lineage `urn:svif:lineage:agnir-v0.2.0-stable-migration`, its branch selector, and its branch-local State/Next are reconciliation input only and are not authoritative-main truth.

## Target publication boundary

This content is designed for a staged target-reconciled candidate while main remains at captured revision `dac058789a27...`. The candidate must be independently validated on its exact tree. Immediately before publication, both captured main and migration source must be re-read; any change invalidates the candidate. Only after those checks may main advance once directly to the verified target candidate.

After main advances, fresh main CI and cold-start discovery must verify Core/profile `0.2`, Project identity, target lineage `urn:svif:lineage:authoritative`, selector `refs/heads/main`, preserved durable locators and stable Agnir `v0.2.0` provenance. A later checkpoint records the exact accepted main revision/run and feeds the real downstream upgrade receipt into Agnir's v1 evidence.

`.agnir/next-actions.md` is the canonical ordered resume plan.
