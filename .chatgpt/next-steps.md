# Next Steps

## Phase 1 — Specification v0.1 (current)

1. Restructure and tighten `SPECIFICATION.md` around the ZeroLocal protocol rather than around any provider implementation. Define roles, normative terminology, lifecycle states/transitions, repository authority, and observable conformance evidence.
2. Formalize the seven current Core Contract families:
   - Lifecycle Contract
   - Repository Contract
   - RPM Contract
   - CI Contract
   - Deployment Contract
   - Trust Boundary Contract
   - Provider Adapter Contract
3. Specify the lifecycle `BOOTSTRAP -> IMPLEMENT -> VERIFY -> PROVISION -> DEPLOY -> OBSERVE -> REPAIR/ITERATE -> CHECKPOINT`, including entry conditions, required evidence, valid transitions, failure paths, and completion criteria for each state.
4. Define the Provider Adapter Contract in enough detail that a provider implementation can declare capabilities, dependencies, credential names/minimum scopes, initialization, scaffolding, CI/CD behavior, provisioning, migrations/state transitions, deployment, immutable revision provenance, endpoint discovery, production verification, and recovery hooks.
5. Define glossary, maturity/conformance model, and the boundary between repository-static conformance evidence and live operational evidence.
6. Align the existing numbered `ZL-CORE-*`, RPM, and Continuous Delivery requirements with the contract/lifecycle model; remove accidental Cloudflare/GitHub-specific assumptions from normative Core language.
7. Resolve the v0.1 questions that block an executable reference, especially RPM's normative status, human production approval gates, exact validated-revision semantics, and the minimum machine-readable project/provider manifest.

## Phase 2 — Cloudflare executable reference

8. Once Phase 1 is sufficiently explicit, bootstrap `iorLab/zerolocal-cloudflare-starter` as the first executable reference implementation of the provider contract.
9. Provide the smallest runnable reference covering RPM, CI, Deploy, exact-tested-SHA release, Cloudflare Workers, optional D1 provisioning/migrations, serialized production operations where required, and health/readiness verification.
10. Treat every implementation ambiguity as specification feedback. Refine Core/contracts rather than silently encoding Cloudflare-specific assumptions into generic semantics.

## Phase 3 — ZeroLocal Skill v0.1

11. Implement the **ZeroLocal Core Skill** as procedural knowledge corresponding to `Initialize -> Plan -> Implement -> Verify -> Deliver -> Observe -> Checkpoint`, while preserving the distinction between Skill procedures and protocol lifecycle states.
12. Implement the **Cloudflare Provider Skill** separately from Core. It should satisfy the Provider Adapter Contract and may delegate mature provider-specific operations to existing Cloudflare tools/skills instead of duplicating them.
13. Add conformance and acceptance checks for both repository/project invariants and provider-skill behavior.

## Phase 4 — Skill stabilization (mandatory before Plugin)

14. Run the skills end to end on at least **two new non-founding real projects**, preferably **2-3**, starting from empty repositories/fresh contexts.
15. Treat any dependency on `awesome-fame-slider`, founding-chat history, this conversation, or unstated operator knowledge as a defect. Fix the missing knowledge in Specification, Core Skill, Provider Skill, reference fixture, or RPM as appropriate.
16. Build a reusable failure taxonomy and recovery strategy for CI, dependencies, secrets, permissions, provisioning, migrations, DNS/routing, and production health/readiness failures.
17. Repeat clean-room runs until a fresh conversation can bootstrap, develop, validate, deploy, diagnose, repair, observe, and checkpoint from repository state plus installed skills alone.

## Phase 5 — Plugin (gated)

18. Define explicit graduation criteria for Plugin work. Plugin packaging begins only after Core contracts and provider interfaces are stable across at least one minor cycle and the clean-room project gates pass.
19. Only then design the ZeroLocal Plugin as the distribution/product shell combining validated skills, GitHub integration, templates, guided setup, provider discovery, versioning, installability, and natural-language activation.
20. After the Cloudflare skill/reference path is stable, add a second provider implementation to validate provider neutrality before broad provider claims.
