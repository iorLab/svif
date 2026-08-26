# ZeroLocal

**ZeroLocal** is an installable, provider-neutral orchestration plugin and working specification for repository-first, AI-operated software development where a human can run the normal implementation, validation, release, and repository-side recovery loop without requiring a local project checkout or local project/deployment toolchain.

Local development is allowed. The defining property is that it is **not required**.

## Target experience

```text
Install ZeroLocal
        ↓
“Use ZeroLocal mode for this project”
        ↓
ZeroLocal Core
(repository + RPM + validation + recovery + trust boundaries)
        ↓
Deployment needed?
        ↓
Choose or resolve provider
   ├─ Cloudflare → Cloudflare provider flow
   ├─ Vercel     → Vercel provider flow
   ├─ AWS        → AWS provider flow
   └─ ...
        ↓
Remote delivery + production verification
```

The user should not need to start from, clone, or fork a provider-specific starter to enter the ZeroLocal workflow.

## Status

ZeroLocal v0.1 is a **Working Draft** covering both the normative operating model and the architecture of the installable orchestration plugin.

- Canonical repository: `iorLab/zerolocal`
- Canonical specification: [`SPECIFICATION.md`](./SPECIFICATION.md)
- Repository Project Memory: [`.chatgpt/project-memory.yaml`](./.chatgpt/project-memory.yaml)
- First provider reference/golden fixture: `iorLab/zerolocal-cloudflare-starter`
- Founding case study: `mattamior/awesome-fame-slider`

## Architecture

ZeroLocal is intentionally split into layers:

1. **ZeroLocal Core specification** — provider-neutral invariants for repository authority, no-local operation, remote validation, trust boundaries, delivery provenance, recovery, and durable project state.
2. **ZeroLocal plugin/orchestrator** — the installable user-facing workflow that activates ZeroLocal mode, operates the repository, maintains RPM, and dispatches provider-specific work.
3. **Provider flows/adapters** — modular deployment-specific behavior for Cloudflare, Vercel, AWS, or other platforms.
4. **Provider reference fixtures** — repositories used to validate what a provider flow generates and how it behaves end to end.

`iorLab/zerolocal-cloudflare-starter` belongs primarily to layer 4 and supports development/testing of the first Cloudflare provider flow. It is not the primary ZeroLocal product or required user entry point.

## Core idea

```text
Human intent / approvals
        ↓
ZeroLocal plugin
        ↓
Canonical repository + RPM
        ↓
Remote implementation / validation / recovery
        ↓
Provider selection + provider flow
        ↓
Remote delivery
        ↓
Production verification
```

The human retains trust-boundary control. Secrets stay in repository/provider secret stores rather than chat. Provider-specific capabilities should be delegated to modular integrations where practical rather than hard-coded into ZeroLocal Core.

## v0.1 focus

The current work is to define:

- the installable ZeroLocal plugin activation and lifecycle contract;
- the provider-neutral orchestration state machine;
- Repository Project Memory (RPM) bootstrap/resume/checkpoint behavior;
- provider discovery and dispatch;
- the provider adapter interface;
- remote validation and repository-side failure recovery;
- secret and human trust boundaries;
- deployment integrity and immutable revision provenance;
- project and provider-flow conformance checks;
- Cloudflare as the first complete provider path.

## Project state

This repository is the canonical source of truth. Durable project state, next steps, and decisions live under `.chatgpt/`; chat conversations are working memory only.
