# Svif Current State

Svif is the authoritative active **Project orchestration product** in `iorLab/svif`. The canonical long-lived ref remains `main`; this temporary migration lineage exists only to validate a real downstream upgrade of Svif's founding Agnir Continuity Provider from published stable `v0.1.1` / Core `0.1` to published stable `v0.2.0` / Core `0.2`. The former `iorLab/svif-cloudflare-reference` project is retired.

## Product architecture

Svif continues to coordinate the same four first-class components: Orchestrator (`src/svif/runtime.py`), Continuity Provider (`src/svif/continuity/agnir.py`), Execution Surface (`src/svif/execution/chatgpt.py`), and Capability Provider (`src/svif/capabilities/cloudflare.py`). The Project persists; Executors and execution environments may change. No execution surface becomes canonical Project truth merely because execution occurred there.

## Released Svif product state

- Svif product line: `0.2`.
- Released Repository Preview: immutable `v0.2.0-preview.1` from authoritative main commit `2b07b6b5ea0bc8feee59f9f647be9af3069d056e`.
- Project Binding: `project-binding/0.2`.
- Software Delivery profile: `software-delivery/0.2`.
- Capability Adapter: `capability-adapter/0.2`.
- Evidence record: `evidence-record/0.2`.
- The released **Plugin MVP** / Repository Preview remains immutable and its first-use bootstrap contract stays on its published Agnir Core/profile `0.1` baseline until a later Svif distribution release intentionally changes that onboarding contract.
- Existing public/personal ChatGPT publication work remains externally blocked at publisher verification/payment-method eligibility; this is not a runtime defect.
- Live Cloudflare delivery remains disabled unless explicitly authorized.
- `README.md` and `README.zh-CN.md` remain the synchronized user/Agent entry points.

## Real Agnir stable migration under validation — 2026-09-03

Captured authoritative Svif baseline before migration: `main@dac058789a27f32f4ed1949874c1954f31f12bd8`.

Before migration, the Svif Project itself consumed Agnir Core `0.1`, `repository-filesystem/0.1`, and published Agnir repository release `v0.1.1` at `e9712357ab590e5c1e5357b3cf3219d07d789aff`.

This migration lineage now declares:

- Agnir Core compatibility `0.2`;
- discovery profile `repository-filesystem/0.2`;
- unchanged Project identity `urn:svif:project:svif-core`;
- logical Continuity Lineage `urn:svif:lineage:agnir-v0.2.0-stable-migration`;
- VCS selector binding `refs/heads/migration/agnir-v0.2.0-stable` as backend selection metadata, not lineage identity;
- unchanged memory locators `.agnir/state.md`, `.agnir/next-actions.md`, `.agnir/decisions.md`, `.agnir/evidence/`;
- published Agnir stable package `v0.2.0` at immutable revision `fc84095ed5d500be9e1b43a4af0e93356571bbd4` as operational provenance;
- `SVIF.yaml` continuity binding updated to compatibility `0.2` / profile `repository-filesystem/0.2` and explicitly carries the same lineage/selector binding while keeping `project-binding/0.2` and the same Project identity.

The preparatory commit `ddaee058efe4c8381f60f5a2ebcae0de9ee9203d` brought the previously real-consumer-validated dual-line Agnir adapter and lineage tests onto the current Svif baseline without changing Project compatibility. Migration commit `eac2ab0dd70695d972b99afad084614eae26c77c` then changed branch-local Project truth to the published stable Core/profile `0.2` line. Initial Draft PR #6 CI proved portable contracts green and localized the remaining failures to guards that still asserted the old current binding; no adapter/Core 0.2 runtime defect was observed.

This is an explicit incompatible Core migration, not the earlier compatible operational upgrade from Agnir repository `0.1.0` to `0.1.1`. Existing Decisions and historical Evidence remain durable history; unrelated Svif product/distribution obligations remain active.

## Migration acceptance boundary

This temporary branch is not authoritative main. It must not silently checkpoint branch-local State back onto `main`. Before acceptance, current-project guards must converge to Core/profile `0.2` while released Preview.1 bootstrap guards remain explicitly `0.1`. The exact migration candidate must pass repository integrity, portable contracts, runtime/unit tests, fresh discovery/resume, founding E2E and Plugin regression pressure. Only then may the accepted Project/package result be reconciled to main using target-owned main continuity and one coherent target publication.

## Existing product obligations preserved

- `plugin/skills/svif/SKILL.md` remains the single-sourced orchestration workflow.
- A genuinely uninitialized Project using the released Preview.1 contract must still be bootstrapped by Svif without requiring a separate Agnir initialization prompt.
- Existing Project content and instructions must be preserved; partial/broken continuity is repair, not clean bootstrap; another intentionally selected Continuity Provider must not be overwritten.
- Repository Preview `v0.2.0-preview.1` remains immutable; any Preview fix uses a new tag.
- Personal ChatGPT Web remains a first-class target.
- Repository CI/package validation is not personal ChatGPT installation evidence.
- `main` remains the only long-lived branch.

`.agnir/next-actions.md` is the canonical ordered resume plan for completing and validating this migration.
