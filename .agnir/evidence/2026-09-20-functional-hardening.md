# Functional hardening candidate — 2026-09-20

Status: locally verified implementation candidate; native effectiveness/release sign-off remains pending. OpenAI publication stays paused. No live Cloudflare transport or protected credentials were used.

## Source and changes

Captured authoritative source: `960526544da308ea8b0eb1d325b26609487ab856`. The earlier source `fe7788bd53d3a240f663860133b741799d0470e3` is the reproduced-defect subject. Preparation branch `fix/local-readiness` is temporary, not a continuity authority. A pinned source artifact was materialized by workflow `35502924625` (artifact `10602459592`) for isolated local implementation; Git objects retain the exact captured source identity.

Implemented F1: trusted `CapabilityPolicy` comes from the registered provider's operation metadata. Missing metadata fails closed. Omitted/null/empty/weaker result authority never removes mandatory `protected-delivery`. Extra requested classes only strengthen it. The real provider policy is tested against its descriptor.

Implemented F4: trusted `OperationRequest` declares required verification/check IDs (default verification required). Failed/blocked/unknown, missing or wrong-subject checks reject completion before effects/checkpoint. Explicit non-applicability requires a reason and cannot excuse a failed check. Parsing model JSON does not authenticate verifier receipts; the trusted integration retains that responsibility.

Implemented F2: all text values and required destinations are preflighted before any memory writes. The filesystem adapter serializes cooperating readers/writers, rejects stale snapshots before effects, and journals the complete State/Next/Decisions/Evidence write set. Prepared transactions roll back after interruption; committed transactions complete recovery. Conflicting outside edits require reconciliation. Six actual child-process exit boundaries exercise prepared/partial/committed states on Core/profile 0.1, 0.2 and 1.0. Ordinary I/O faults exercise rollback without partial publication.

Implemented F3: each actual read/write is confined, including discovery, evidence children, lock, receipt and temporary paths. POSIX opens walk directory descriptors with no-follow flags. Symlinks, junctions and multi-linked regular targets are rejected; uniquely created temporary files replace predictable paths. Windows uses no-link/reparse checks and OS locking but does not claim protection against hostile concurrent parent-directory replacement by equally privileged processes.

Additional safety: exact Orchestrator sessions are single-use; duplicate persisted operation receipts cannot be overwritten; uncertain external attempts leave a persistent marker across restart. Reconciliation of an independently confirmed effect requires matching observation and trusted `effect-reconciliation` authority; it never replays delivery. Provider delivery/observation errors preserve their own failure classes rather than being called continuity I/O failures.

The shared Skill now carries the same operational guards without bundling or duplicating the Python kernel. Both READMEs, architecture, applicable contract/integration notes, Project artifact registration and repository tree are updated. Native install/discovery is tested separately by `checks/check_native_install.py`; actual task/bootstrap/idempotency/fresh-session acceptance is specified in `LOCAL_ACCEPTANCE.md`. `RELEASE_READINESS.md` maps existing requirements to implementation and evidence boundaries.

## Local observed verification

The complete repository was materialized from the pinned Git bundle, not reconstructed from excerpts. Baseline: 87 tests passed. After changes: 109 tests passed on Python 3.13.5; repository integrity and portable contracts passed; source/check/test compilation passed. All external providers in these tests are injected fakes. The new test methods include parameterized cases and 18 actual process-death trials (six points on each of three compatibility lines).

The local sandbox has no Codex binary. The native harness correctly emitted `native_install=not-observed`, `native_discovery=not-observed`, `native_task_and_fresh_session=not-observed`, `release_ready=false`, and exit 2. This is blocker reporting, NOT native-host acceptance. Connected plugin discovery did not expose a suitable authorized local-host execution capability.

Remote candidate CI/native installation observations, if obtained, must be appended with exact candidate and Plugin identities. Passing those still does not replace a real authenticated native task and fresh LLM-session receipt.

## Preserved boundaries

Core/profile and Project identity/lineage/selector/locators are unchanged. The repository still self-hosts Agnir Core/profile 1.0 and preserves historical 0.1/0.2 support; the founding Skill bootstrap is still 0.1. The old Preview tag is immutable. Old ZIP/package-only receipts remain historical; changes to the Skill create a NEW Plugin tree that must be independently identified. No new release tag, GitHub Release, OpenAI submission or production delivery is authorized by this candidate.
