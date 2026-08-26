# Decisions

## 2026-08-26 — Initialize ZeroLocal RPM

- `iorLab/zerolocal` is the canonical source of truth for the ZeroLocal project.
- RPM state is stored under `.chatgpt/` and is loaded through `.chatgpt/project-memory.yaml`.
- Chat conversations are working memory only; durable state, next steps, and decisions belong in the repository.
- `iorLab/zerolocal-cloudflare-starter` is the Cloudflare provider-flow reference/golden-fixture repository.
- `mattamior/awesome-fame-slider` is the founding case study and evidence source for the initial specification and operating model.

## 2026-08-26 — Define ZeroLocal as a conformance property

- ZeroLocal means the human operator does not require a local project checkout, local package/build toolchain, local git commands, or local deployment CLI for the normal software-development, validation, release, and repository-side recovery loop.
- ZeroLocal does **not** prohibit maintainers from using local development environments when they choose to.
- A project therefore qualifies by the existence of a complete remote/repository-native path, not by the absence of local tooling.

## 2026-08-26 — Keep the specification core provider-neutral

- ZeroLocal Core describes roles, repository authority, trust boundaries, remote validation, delivery provenance, observability, recovery, and conformance without requiring Cloudflare.
- Cloudflare Workers, D1, Wrangler, and Cloudflare-specific provisioning behavior belong to a provider-specific flow/profile rather than ZeroLocal Core.
- The founding case study may motivate requirements, but application-specific voting, X sharing, and product behavior are not ZeroLocal requirements.

## 2026-08-26 — Repository and secret boundaries

- The repository is the canonical project filesystem and durable history for a ZeroLocal project.
- Durable AI/operator project memory should be repository-backed; this project standardizes its own memory as Repository Project Memory (RPM).
- Secret values must remain in GitHub/provider secret stores or equivalent protected systems and must not be requested through chat.
- Human involvement is expected at trust boundaries such as account authorization, secret creation, billing, provider selection/configuration, and optional production approval gates.

## 2026-08-26 — Start Specification v0.1 as a working draft

- `SPECIFICATION.md` is the canonical v0.1 working draft until a later repository decision supersedes that location.
- Normative requirements use RFC-style `MUST`, `MUST NOT`, `SHOULD`, `SHOULD NOT`, and `MAY` terminology.
- v0.1 will initially optimize for observable, testable invariants derived from the founding case rather than prescribing one implementation architecture.

## 2026-08-26 — Clarify ZeroLocal product shape: plugin-first, provider-second

This decision supersedes earlier wording that positioned `iorLab/zerolocal-cloudflare-starter` as the reference implementation of ZeroLocal as a whole.

- The target product form of ZeroLocal is an installable ChatGPT plugin/skill (or equivalent installable orchestration package), not a repository starter that users must fork.
- A user should be able to install ZeroLocal and activate it through natural-language intent such as “use ZeroLocal mode for this project”.
- The ZeroLocal plugin owns the provider-neutral orchestration flow: repository discovery/initialization, RPM bootstrap and loading, remote validation, repository-native implementation, failure recovery, trust-boundary handling, delivery provenance, and checkpointing.
- Deployment provider selection is a separate decision inside the ZeroLocal flow. When deployment is required and no provider is already established, ZeroLocal should resolve or ask for the provider choice, then dispatch to the corresponding provider-specific flow.
- Provider-specific flows are modular adapters/profiles. Cloudflare is the first provider flow; future flows may target Vercel, AWS, Fly.io, or other runtimes without changing ZeroLocal Core.
- `iorLab/zerolocal-cloudflare-starter` is therefore a supporting Cloudflare provider-flow reference, scaffold, golden fixture, and conformance testbed. It is not the primary user entry point and users should not be required to fork it to use ZeroLocal.
- `iorLab/zerolocal` should ultimately contain the ZeroLocal plugin source/skills, the provider-neutral orchestration contract, the specification, conformance logic, and this project's RPM.
- Where a provider has its own installable plugin or tool integration, the ZeroLocal provider flow may delegate provider-specific operations to that integration while preserving the ZeroLocal orchestration contract.
