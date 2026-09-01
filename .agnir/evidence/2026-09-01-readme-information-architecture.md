# 2026-09-01 — README audience split and entry-point information architecture

The Principal approved a README information-architecture simplification for Svif and subsequently refined how first-use Project changes are presented.

Durable documentation rule:

- Before `## Architecture Diagram`, README content is limited to a concise product identity/name explanation plus three operational surfaces: `## Start Here` for users, canonical `## Agnir Project Instructions` for Agents, and `## What Svif Adds to a Project` as a concrete first-use Project-surface explanation.
- `Start Here` contains only the minimal personal-ChatGPT status, installation, normal-use, and Agnir-upgrade actions.
- `Agnir Project Instructions` remains the canonical Agent-facing activation heading required by `AGENTS.md`; it is explicitly marked as Agent-only guidance for human readers.
- `What Svif Adds to a Project` makes first-use mutation legible and non-destructive: existing `AGENTS.md` and `README.md` are marked **EDIT / add entry only**, while `AGNIR.yaml`, the reference `.agnir/` continuity layout, and `SVIF.yaml` are marked **ADD** for a genuinely uninitialized repository/filesystem Project.
- Existing compatible Agnir/Svif artifacts are validated and reused rather than recreated. Partial or contradictory artifacts are repair cases. A Project intentionally bound to another Continuity Provider is not silently overwritten with Agnir.
- The Architecture Diagram mirrors the same first-use ADD/EDIT surface while retaining the static Svif product roles: Orchestrator, Continuity Provider, Execution Surface, and Capability Provider.
- Runtime / Operation Flow remains a post-bootstrap runtime view. Installation-mutation ADD/EDIT labels do not belong in that flow unless runtime semantics themselves change.
- Public submission workflow, Plugin packaging rationale, compatibility detail, repository structure, and deeper implementation/conformance explanation belong after the architecture entry point or in dedicated documents.
- Svif first-use onboarding remains consistent with the active product decision: a genuinely uninitialized Project does not require manual Agnir pre-initialization; the shared Svif Skill owns the founding continuity bootstrap on the repository/filesystem path.
- English and Simplified Chinese READMEs preserve the same operational meaning, with localized diagrams remaining comprehension-first.
- Repository-integrity checks enforce `Start Here -> Agnir Project Instructions -> installed Project surface -> Architecture` ordering, required first-use surface markers, Architecture Diagram ADD/EDIT semantics, and separation from Runtime / Operation Flow.

This remains a documentation/operational-entry clarification. It does not change Svif `0.2`, `project-binding/0.2`, the configured Agnir compatibility line, Project identity, Orchestrator runtime semantics, or external-effect authority semantics.
