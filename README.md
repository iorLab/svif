# ZeroLocal

**ZeroLocal** is a provider-neutral operating model and evolving skill set for repository-first, AI-operated software development where a human can run the normal implementation, validation, release, and repository-side recovery loop without requiring a local project checkout or local project/deployment toolchain.

Local development is allowed. The defining property is that it is **not required**.

The founding operating model was developed under the name **AI-Native Repository Delivery (ANRD)**. ZeroLocal is the current project/product identity used to formalize, encode, validate, and eventually package that model for reuse.

## Productization sequence

ZeroLocal is deliberately **skill-first, plugin-later**:

```text
Specification v0.1
        ↓
Cloudflare executable reference
        ↓
ZeroLocal Core Skill
        ↓
Cloudflare Provider Skill
        ↓
Second-project clean-room validation
        ↓
Stable skills + contracts
        ↓
ZeroLocal Plugin packaging
```

The Plugin is a possible mature distribution/product layer, not the first implementation milestone. The workflows should be discovered and stabilized in the Specification, executable reference, and Skills before Plugin packaging freezes a broader product surface.

## Target mature experience

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

The user should not need to start from, clone, or fork a provider-specific starter to enter the mature ZeroLocal workflow.

## Status

ZeroLocal v0.1 is a **Working Draft**. The current phase is Specification + executable-reference design; the immediate reusable implementation target is a **ZeroLocal Core Skill** and provider-specific Skills.

- Canonical repository: `iorLab/zerolocal`
- Canonical specification: [`SPECIFICATION.md`](./SPECIFICATION.md)
- Repository Project Memory: [`.chatgpt/project-memory.yaml`](./.chatgpt/project-memory.yaml)
- First executable provider reference/golden fixture: `iorLab/zerolocal-cloudflare-starter`
- Founding case study: `mattamior/awesome-fame-slider`

## Architecture

ZeroLocal is intentionally split into layers:

1. **ZeroLocal Specification** — provider-neutral protocol and invariants for roles, repository authority, no-local operation, remote validation, trust boundaries, contracts, delivery provenance, recovery, durable project state, and provider adapters.
2. **Executable provider references** — real implementations used to pressure-test the specification. Cloudflare is first.
3. **ZeroLocal Core Skill** — repeatable procedural workflow that translates provider-neutral specification semantics into ChatGPT execution behavior.
4. **Provider Skills** — modular provider-specific workflows that satisfy the provider adapter contract; Cloudflare is first.
5. **Clean-room validation projects** — new projects used to prove that the skills operate from durable repository state and explicit contracts rather than hidden founding-project context.
6. **ZeroLocal Plugin** — a later packaging/distribution layer that may combine stable skills, GitHub integration, templates, installation UX, and provider discovery.

`iorLab/zerolocal-cloudflare-starter` belongs primarily to layers 2 and 4 as a reference fixture for the Cloudflare path. It is not the primary user entry point.

## Core idea

```text
Human intent / approvals
        ↓
ZeroLocal Core Skill
        ↓
Canonical repository + RPM
        ↓
Remote implementation / validation / recovery
        ↓
Provider selection + Provider Skill
        ↓
Remote delivery
        ↓
Production verification
```

The human retains trust-boundary control. Secrets stay in repository/provider secret stores rather than chat. Provider-specific capabilities should be delegated to modular integrations where practical rather than hard-coded into ZeroLocal Core.

## v0.1 focus

The current work is to define:

- protocol roles and lifecycle contracts;
- the provider-neutral orchestration model;
- Repository Project Memory (RPM) bootstrap/resume/checkpoint behavior;
- remote validation and repository-side failure recovery;
- secret and human trust boundaries;
- deployment integrity and immutable revision provenance;
- provider discovery and dispatch;
- the provider adapter interface;
- Cloudflare as the first executable provider reference;
- the ZeroLocal Core Skill and Cloudflare Provider Skill;
- clean-room validation through a second real project before Plugin packaging.

## Project state

This repository is the canonical source of truth. Durable project state, next steps, and decisions live under `.chatgpt/`; chat conversations are working memory only.
