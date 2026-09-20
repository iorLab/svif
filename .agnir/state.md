# Svif Current State

Svif is the authoritative active **Project orchestration product** in `iorLab/svif`.
The former `iorLab/svif-cloudflare-reference` project is retired. Repository-managed
Agnir continuity on `main` remains canonical; staging is not a second authority.

## Active direction and verdict — 2026-09-20

The Principal requested release-standard functional repair and local effectiveness;
OpenAI Platform submission/Publish remains paused until an explicit new instruction.

**The four reproduced runtime blockers are repaired and cross-platform regression
checks pass. A new first-use version-selection repair is now under validation: existing
Agnir Projects preserve their declared Core/profile, while genuinely uninitialized
Projects resolve the canonical latest published stable Agnir. Because this changes Skill
bytes, the prior native install/discovery receipt remains historical for the preceding
candidate and must be rerun for the new candidate before model-driven release acceptance.**

## Verified repair subject

- Product/package version: unpublished `0.2.0`; product and portable contracts remain `0.2`.
- Baseline: `960526544da308ea8b0eb1d325b26609487ab856`, retaining audited product code
  `fe7788bd53d3a240f663860133b741799d0470e3`.
- Reviewed repair source: `225e535e32a18bf8db2bfc7d76efe6bed9378e97`, tree
  `12542123c9ab47e5e938f8db8fd8a7d36f28a513`, PR #11.
- Prior repaired Plugin tree `7cc90517013306181a4df2238f849b85cf716665` passed native install/discovery and remains historical evidence. The bootstrap-version-selection change creates a new Plugin subject that requires its own exact tree and native receipt before acceptance.
- Local full suite: 128 tests pass on Linux/Python 3.13.5; repository integrity and
  portable contracts pass. Tests execute real code, including process termination.
- PR candidate run `35509417968`: all eight jobs pass, including runtime on Linux
  (Python 3.12/3.13), macOS (3.12), Windows (3.12), and native installation on Linux/macOS.
- Native Codex 0.155.1 reports installed+enabled and discovers `svif:svif` at the exact
  installed cache path. All installed package file hashes equal the selected source.
- Native no-auth receipts remain distinct from model execution. No current-version
  real model task/checkpoint/fresh-LLM-session or desktop GUI acceptance is claimed.

## Implemented behavior

Provider-owned capability policy cannot be waived by omitted/null/empty model fields.
Trusted operation verification defaults to required; parsed ChatGPT declarations need
independent trusted receipts. Failed required checks cannot publish completion.

Checkpointing now has full preflight, revision CAS, process/thread locking, contained
no-follow I/O, journaled rollback/restart recovery and durable operation replay checks.
Evidence children and read/write destinations cannot silently follow unauthorized links.
Uncertain external effects persist before actuation and require independent matching
reconciliation rather than blind replay. Windows native paths and case-insensitive
archive collision fixtures are covered by the expanded cross-platform suite.

The scope/limitations are explicit in `spec/RUNTIME_SAFETY.md`: trusted Python integration,
cooperating transaction readers, local owned filesystems, and no distributed exactly-once
claim. The Skills-only Plugin guides the host; it does not bundle the Python kernel.
Orchestrator + Continuity Provider + Execution Surface + Capability Provider remain
first-class components. `conformance/RELEASE_READINESS.md` maps requirements to evidence.

Implementation, failures/repairs and exact CI/native receipts:
`.agnir/evidence/2026-09-20-runtime-readiness-repair.md`. Bootstrap version-selection rationale and current latest-stable observation are recorded in `.agnir/evidence/2026-09-20-bootstrap-version-selection.md`.

## Preserved continuity, release and product boundaries

- Project `urn:svif:project:svif-core`; Agnir Core/profile `1.0` / `repository-filesystem/1.0`.
- Lineage `urn:svif:lineage:authoritative`; distinct VCS selector `refs/heads/main`.
- Memory locators remain `.agnir/state.md`, `.agnir/next-actions.md`, `.agnir/decisions.md`,
  `.agnir/evidence/`; applied Agnir remains v1.0.0 at `6d16dcfd17b8e9f22fd25804e22b9f8a516d06c3`.
- Adapter support remains 0.1/0.2/1.0. Existing target Projects preserve the exact Agnir Core/profile they declare; invoking/installing Svif does not authorize migration. A genuinely uninitialized target resolves the latest published stable Agnir at bootstrap time and adopts that release's declared Core/profile. Svif's own self-host binding remains 1.0 and is not upgraded by this change.
- Released **Plugin MVP** / Preview `v0.2.0-preview.1` remains immutable at
  `2b07b6b5ea0bc8feee59f9f647be9af3069d056e`, tag object `2535cb89426c2d38c2e061948e81954a7c7c26d7`.
  Its historical real-client evidence is preserved, not generalized to the repaired Skill.
- Old Plugin tree `5ab4b6147dbd096c052f042b23e37f0ec39f7091` and its submission ZIP are
  historical package evidence only; their bytes do not identify the repaired candidate.
- Accepted Agnir promotion/adoption and approved brand integration remain complete.
  Approved visual assets are unchanged. `README.md` and `README.zh-CN.md` stay synchronized;
  the public one-line Preview installer still selects the immutable released Preview.
- Live Cloudflare delivery remains disabled. Remote MCP/network transport is separately
  scoped, not an invented new prerequisite for the bounded Skill-first MVP.
- No v0.2.0 tag, public release, OpenAI submission, directory availability or protected
  production effect has been created. PR #3 remains closed; its archived ref is historical.

`.agnir/next-actions.md` is the ordered resume plan.
