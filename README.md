# ZeroLocal

**ZeroLocal** is a working specification for repository-first, AI-operated software delivery where a human can run the normal development, validation, release, and repository-side recovery loop without requiring a local project checkout or local project/deployment toolchain.

Local development is allowed. The defining property is that it is **not required**.

## Status

ZeroLocal Specification v0.1 is a **Working Draft**.

- Canonical specification: [`SPECIFICATION.md`](./SPECIFICATION.md)
- Repository Project Memory: [`.chatgpt/project-memory.yaml`](./.chatgpt/project-memory.yaml)
- Cloudflare reference implementation: `iorLab/zerolocal-cloudflare-starter`
- Founding case study: `mattamior/awesome-fame-slider`

## Core idea

```text
Human intent / approvals
        ↓
AI / repository operator
        ↓
Canonical repository + durable project state
        ↓
Remote validation
        ↓
Remote delivery
        ↓
Production verification
```

The human retains trust-boundary control. Secrets stay in repository/provider secret stores rather than chat. Implementation, validation, deployment orchestration, diagnostics, and repository memory are designed to remain operable remotely.

## v0.1 focus

The first draft defines:

- a provider-neutral ZeroLocal Core;
- the exact meaning of "no local prerequisite";
- repository authority and immutable revision provenance;
- remote validation and repository-side failure recovery;
- secrets and human trust boundaries;
- deployment integrity for deployable systems;
- an optional Repository Project Memory (RPM) profile;
- an optional Continuous Delivery profile;
- the boundary for provider-specific reference profiles.

The first reference profile will target GitHub Actions + Cloudflare Workers, with optional D1 usage.

## Project state

This repository is the canonical source of truth. Durable project state, next steps, and decisions live under `.chatgpt/`; chat conversations are working memory only.
