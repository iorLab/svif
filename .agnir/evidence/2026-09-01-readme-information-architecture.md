# 2026-09-01 — README audience split and entry-point information architecture

The Principal approved a README information-architecture simplification for Svif.

Durable documentation rule:

- Before `## Architecture Diagram`, README content is limited to two operational audiences.
- `## Start Here` is the user-facing entry point and contains only the minimal personal-ChatGPT status, installation, normal-use, and Agnir-upgrade actions.
- `## Agnir Project Instructions` remains the canonical Agent-facing activation heading required by `AGENTS.md`; it is explicitly marked as Agent-only guidance for human readers.
- Public submission workflow, Plugin packaging rationale, compatibility detail, repository structure, and implementation/conformance explanation belong after the architecture entry point or in dedicated documents.
- Svif first-use onboarding is represented consistently with the active product decision: a genuinely uninitialized Project does not require manual Agnir pre-initialization; the shared Svif Skill owns the founding continuity bootstrap on the repository/filesystem path.
- English and Simplified Chinese READMEs follow the same audience split.
- Repository-integrity checks now enforce `Start Here -> Agnir Project Instructions -> Architecture` ordering and the canonical user prompts.

This is a documentation/operational-entry refactor only. It does not change Svif `0.2`, `project-binding/0.2`, the configured Agnir compatibility line, Project identity, runtime architecture, or external-effect authority semantics.
