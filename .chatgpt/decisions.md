# Decisions

## 2026-08-26 — Initialize ZeroLocal RPM

- `iorLab/zerolocal` is the canonical source of truth for the ZeroLocal specification project.
- RPM state is stored under `.chatgpt/` and is loaded through `.chatgpt/project-memory.yaml`.
- Chat conversations are working memory only; durable state, next steps, and decisions belong in the repository.
- `iorLab/zerolocal-cloudflare-starter` is the Cloudflare reference implementation repository.
- `mattamior/awesome-fame-slider` is the founding case study and evidence source for the initial specification.

## 2026-08-26 — Define ZeroLocal as a conformance property

- ZeroLocal means the human operator does not require a local project checkout, local package/build toolchain, local git commands, or local deployment CLI for the normal software-development, validation, release, and repository-side recovery loop.
- ZeroLocal does **not** prohibit maintainers from using local development environments when they choose to.
- A project therefore qualifies by the existence of a complete remote/repository-native path, not by the absence of local tooling.

## 2026-08-26 — Keep the specification core provider-neutral

- ZeroLocal Core describes roles, repository authority, trust boundaries, remote validation, delivery provenance, observability, recovery, and conformance without requiring Cloudflare.
- Cloudflare Workers, D1, Wrangler, and Cloudflare-specific provisioning behavior belong to a Cloudflare reference profile/implementation.
- The founding case study may motivate requirements, but application-specific voting, X sharing, and product behavior are not ZeroLocal requirements.

## 2026-08-26 — Repository and secret boundaries

- The repository is the canonical project filesystem and durable history for a ZeroLocal project.
- Durable AI/operator project memory should be repository-backed; this project standardizes its own memory as Repository Project Memory (RPM).
- Secret values must remain in GitHub/provider secret stores or equivalent protected systems and must not be requested through chat.
- Human involvement is expected at trust boundaries such as account authorization, secret creation, billing, and optional production approval gates.

## 2026-08-26 — Start Specification v0.1 as a working draft

- `SPECIFICATION.md` is the canonical v0.1 working draft until a later repository decision supersedes that location.
- Normative requirements use RFC-style `MUST`, `MUST NOT`, `SHOULD`, `SHOULD NOT`, and `MAY` terminology.
- v0.1 will initially optimize for observable, testable invariants derived from the founding case rather than prescribing one implementation architecture.
