# Decisions

## 2026-08-26 — Initialize ZeroLocal RPM

- `iorLab/zerolocal` is the canonical source of truth for the ZeroLocal project.
- RPM state is stored under `.chatgpt/` and is loaded through `.chatgpt/project-memory.yaml`.
- Chat conversations are working memory only; durable state, next steps, and decisions belong in the repository.
- `iorLab/zerolocal-cloudflare-starter` is the Cloudflare provider-flow executable-reference/golden-fixture repository.
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

## 2026-08-26 — Clarify long-term ZeroLocal product shape

- The long-term user experience is an installable ZeroLocal product activated through natural-language intent such as “use ZeroLocal mode for this project”.
- The provider-neutral workflow and deployment-provider selection remain separate concerns.
- `iorLab/zerolocal-cloudflare-starter` is supporting infrastructure for the Cloudflare path, not the required user entry point.
- This long-term product goal does **not** imply that Plugin packaging should be built first.

## 2026-08-26 — Restore the founding skill-first productization sequence

This decision supersedes the earlier `plugin-first` implementation sequencing while preserving Plugin as a possible mature product form.

The recovered founding roadmap is:

1. **ZeroLocal Specification v0.1** — first define protocol, roles, trust boundaries, contracts, lifecycle, conformance, and the provider adapter interface.
2. **Cloudflare executable reference** — use `iorLab/zerolocal-cloudflare-starter` to prove that the specification can be implemented and to expose ambiguity through real CI/deployment behavior.
3. **ZeroLocal Core Skill** — translate the provider-neutral specification into a repeatable procedural workflow that ChatGPT can execute consistently.
4. **Cloudflare Provider Skill** — separate Cloudflare-specific provisioning, deployment, verification, and recovery behavior from the Core Skill.
5. **Clean-room multi-project validation** — run the skills on new non-founding projects from empty repositories/fresh contexts without relying on hidden context from `awesome-fame-slider`, the founding conversation, or unstated operator knowledge.
6. **ZeroLocal Plugin only after stabilization** — once Core Skill, provider skills, contracts, failure taxonomy, and clean-room execution are stable, consider packaging them with GitHub integration, templates, onboarding, and distribution into an installable product.

Rationale:

- Skills are the right layer for stabilizing procedural knowledge before fixing a broader product/API surface.
- The executable reference tests the specification; the skills test repeatability; clean-room projects test portability and hidden-context independence.
- Packaging too early risks freezing accidental assumptions from the founding project into the product interface.
- The Plugin should compose validated workflows rather than be the place where those workflows are first discovered.

## 2026-08-26 — Provider dispatch remains part of the architecture

- Deployment provider selection occurs after or during ZeroLocal Core orchestration when deployment becomes relevant.
- Provider-specific behavior is modular and should be expressed through a defined provider adapter/skill contract.
- Cloudflare is the first provider implementation; future providers may include Vercel, AWS, Fly.io, or others without changing provider-neutral Core semantics.
- Where mature provider plugins/skills already exist, a ZeroLocal Provider Skill may delegate provider-specific operations rather than duplicate provider expertise.

## 2026-08-26 — ANRD is the former name of ZeroLocal

- `ANRD` means **AI-Native Repository Delivery** and is the former name used for the same project/operating model now called ZeroLocal.
- Do not maintain ANRD and ZeroLocal as separate conceptual architectures unless a future explicit decision creates such a distinction.
- Historical ANRD wording may be translated directly into current ZeroLocal terminology when extracting requirements and design rationale.

## 2026-08-26 — Adopt the recovered development reference as directional guidance

- The user-supplied `ZeroLocal 开发参考文档 v0.1` is accepted as a high-priority directional reference for the current development phase.
- It is **not** the canonical Specification; normative truth remains in `iorLab/zerolocal`, especially `SPECIFICATION.md` and RPM decisions.
- The reference's six-layer architecture is accepted as the current design frame: Human Governance, Agent, Repository Control Plane, Verification & Delivery, Provider Adapter, and Production Observation.
- The current Core Contract families are Lifecycle, Repository, RPM, CI, Deployment, Trust Boundary, and Provider Adapter.
- The lifecycle to formalize is `BOOTSTRAP -> IMPLEMENT -> VERIFY -> PROVISION -> DEPLOY -> OBSERVE -> REPAIR/ITERATE -> CHECKPOINT`.
- The proposed Skill procedural surface is `Initialize -> Plan -> Implement -> Verify -> Deliver -> Observe -> Checkpoint`; the Specification lifecycle and Skill procedure are related but should remain distinct layers.
- Phase ordering is authoritative for current planning: Founding Case -> Specification v0.1 -> Cloudflare Reference -> Skill v0.1 -> Skill Stabilization -> Plugin.
- v0.1 explicitly does not target broad multi-provider support or Plugin-first productization; Cloudflare is the sole initial reference provider.
- Plugin graduation is gate-driven rather than date-driven. At minimum, the skills must work on at least two new non-founding projects; the reference recommends 2-3 real projects before productization.

## 2026-08-26 — Checkpoint after roadmap recovery

- Current phase is **Phase 1 — Specification v0.1**.
- The next substantive work is to tighten the protocol, roles, lifecycle, trust boundaries, contract families, conformance requirements, and Provider Adapter Contract before implementing the Cloudflare reference.
- `iorLab/zerolocal-cloudflare-starter` remains empty/pending until the specification is sufficiently explicit to act as its contract.
- Do not begin Plugin packaging during this phase.

## 2026-08-27 — Treat RPM discovery as part of resumability

Validation Project #1 demonstrated that durable RPM content is insufficient when a fresh conversation cannot discover the repository/ref containing it.

- A conversational ZeroLocal environment that creates or adopts RPM must establish a durable bootstrap pointer into repository RPM.
- For ChatGPT Projects, Project Instructions are an acceptable bootstrap surface, but they must remain locator-only metadata rather than a second project-memory store.
- The minimum locator identifies ZeroLocal activation, the canonical repository, the RPM manifest path, and the authoritative RPM ref when it differs from the default branch.
- Checkpoint must not claim fresh-context resumability while this pointer is missing or stale.
- RPM on a feature/non-default branch is valid, but the active RPM ref must be discoverable before state is loaded.
- This failure class is named `RPM/bootstrap discovery` and belongs in the Core failure taxonomy and conformance coverage.
- Validation #1 must repeat the fresh-conversation resume test after this fix is verified and the target ChatGPT Project receives only the minimal locator instructions.
