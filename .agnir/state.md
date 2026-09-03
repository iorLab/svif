# Svif Current State

Svif is the authoritative active **Project orchestration product** in `iorLab/svif`. The canonical long-lived ref remains `main`; this temporary migration lineage validates a real downstream upgrade of Svif's founding Agnir Continuity Provider from published stable `v0.1.1` / Core `0.1` to published stable `v0.2.0` / Core `0.2`. The former `iorLab/svif-cloudflare-reference` project is retired.

## Product architecture

Svif continues to coordinate the same four first-class components: Orchestrator (`src/svif/runtime.py`), Continuity Provider (`src/svif/continuity/agnir.py`), Execution Surface (`src/svif/execution/chatgpt.py`), and Capability Provider (`src/svif/capabilities/cloudflare.py`). The Project persists; Executors and execution environments may change.

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

## Published Agnir v0.2.0 migration-line validation completed — 2026-09-03

Captured authoritative Svif source before migration: `main@dac058789a27f32f4ed1949874c1954f31f12bd8`.

The temporary migration line now self-hosts:

- Agnir Core `0.2`;
- `repository-filesystem/0.2`;
- unchanged Project identity `urn:svif:project:svif-core`;
- logical lineage `urn:svif:lineage:agnir-v0.2.0-stable-migration`;
- separate VCS selector `refs/heads/migration/agnir-v0.2.0-stable`;
- unchanged State / Next Actions / Decisions / Evidence locators;
- published Agnir stable `v0.2.0` at immutable revision `fc84095ed5d500be9e1b43a4af0e93356571bbd4`.

Implementation/validation sequence:

1. `ddaee058efe4c8381f60f5a2ebcae0de9ee9203d` added the already real-consumer-validated dual-line 0.1/0.2 adapter and tests without changing Project compatibility.
2. `eac2ab0dd70695d972b99afad084614eae26c77c` atomically migrated branch-local Project truth to Core/profile `0.2`.
3. Initial Draft PR #6 run `33723726831` passed portable contracts and exposed only old current-binding/repository assertions plus distribution markers omitted from the first migration Next Actions; no Core 0.2 adapter/runtime defect appeared.
4. `8aaed18dbbbbb857873500505ae941289f0029c4` converged repository/current-binding guards to 0.2 while explicitly retaining Preview.1 first-use bootstrap at 0.1. Run `33724143647` passed repository integrity, runtime/unit tests and portable contracts.
5. `5b2086bdc61cd5dad8397241565fbbda9592fc88` synchronized the active Skill and repository tree. The Skill now distinguishes current Svif self-host Core/profile `0.2` from the immutable Preview.1 bootstrap baseline `0.1`, and requires Core 0.2 lineage/selector validation.
6. Final PR-head run `33724576017` passed all three jobs: repository integrity, runtime-kernel full unittest discovery, and portable contracts.
7. PR #6 synthetic merge commit `5d145ce1eb4ec4e6b837194a3e206b77bb71665b` has tree `142051872a708c9944c737e1ebcee008ac27a381`, exactly equal to source head `5b2086...` tree. The captured main is an ancestor and no synthetic merge tree transformation occurred.

No Agnir `v0.2.0` product defect has been observed in this real downstream migration so far. The only initial failures were Svif guards that still encoded the old current self-host compatibility and one accidental omission of existing distribution markers; both were repaired without weakening 0.1 regression/bootstrap pressure.

## Acceptance boundary

This migration line remains non-authoritative. Its lineage/selector and branch-local State/Next are not main truth. The next publication boundary is a separately staged target-main candidate that accepts the validated product/package changes but reconstructs `AGNIR.yaml`, `SVIF.yaml`, State and Next Actions for authoritative main using target-owned lineage `urn:svif:lineage:authoritative` and selector `refs/heads/main`.

Before main can advance, the final migration source and main target must be re-read for staleness, the target-reconciled candidate must pass the same complete CI while main remains unchanged, and only then may main advance once to that exact candidate.

## Existing product obligations preserved

- `plugin/skills/svif/SKILL.md` remains the single-sourced orchestration workflow.
- `v0.2.0-preview.1` stays immutable; any Preview fix uses a new tag.
- Personal ChatGPT Web remains a first-class target; repository CI/package validation is not personal ChatGPT installation evidence.
- Live Cloudflare delivery remains disabled unless explicitly authorized.
- `main` remains the only long-lived branch.

`.agnir/next-actions.md` is the canonical ordered resume plan.
