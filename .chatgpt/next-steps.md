# Next Steps

## Immediate — Svif / Agnir architecture transition

1. Treat ZeroLocal v0.1, its Skills, conformance checks, validation evidence, and Cloudflare reference as the **historical predecessor baseline**. Do not silently rename existing claims into Svif conformance.
2. Coordinate with `mattamior/rpm`, the independent project evolving from PPMP / PPM / Sandminni into **Agnir**. Record matching cross-project decisions there without creating shared mutable project memory.
3. Define the target Agnir identity and migration boundary first enough that Svif can depend on a versioned, platform/storage/executor-neutral durable-memory contract.
4. Draft Svif's generalized Core architecture and vocabulary. Remove normative dependence on:
   - ChatGPT;
   - GitHub or any repository host;
   - Git or a required VCS;
   - a particular AI agent;
   - conversational state;
   - ChatGPT Skill packaging;
   - the local-vs-remote distinction as the defining conformance property.
5. Replace predecessor role/surface terminology with neutral concepts. Current candidates include:
   - `Principal` for intent/authority/policy;
   - `Executor` for any human, agent, CLI, automation, CI runner, or composed system that performs work;
   - `cold-start discovery` / `fresh-executor recovery` for the generalized resumability invariant.
6. Define the Svif <-> Agnir dependency explicitly:
   - Agnir is independently usable without Svif;
   - Svif requires durable project continuity through Agnir or a precisely defined compatible contract;
   - project memory is project-owned and must be discoverable without executor-private predecessor context.
7. Decide which ZeroLocal v0.1 invariants remain Svif Core invariants after the generalization. Re-evaluate, rather than automatically discard, exact-revision provenance, observable verification, trust boundaries, provider isolation, evidence-driven lifecycle transitions, repair taxonomy, and checkpoint semantics.
8. Design an explicit migration plan for names and files only after the architecture is stable enough to preserve compatibility. Candidate changes include `ZEROLOCAL.yaml`, `skills/zerolocal-core`, provider Skill naming, `.chatgpt/`-specific semantics, conformance identifiers, the canonical repository name, and the Cloudflare reference repository name.

## Shared workspace / separate project state

9. Use this ChatGPT Project as a **workspace** for Svif and Agnir when useful, not as either project's canonical memory store.
10. Keep independent durable state for each project. Project-scoped work loads only that project's Agnir; explicitly cross-project work loads both projects.
11. Persist cross-project decisions separately in each affected project according to their local meaning. Do not create a third shared mutable state store.
12. Later update the external ChatGPT Project bootstrap to a thin multi-project registry containing only project/discovery locators. Until that external configuration is synchronized, do not claim fully proven fresh-context multi-project resumability.

## Validation Project #2 — `mattamior/cloud-mail`

13. Preserve `.chatgpt/validation-2.md` and the previously selected non-destructive stateful Cloudflare validation intent.
14. **Pause execution** of Validation #2 while the Svif/Agnir architecture and migration boundary are being defined. A fresh clean-room run against predecessor-only ZeroLocal v0.1 would no longer test the intended target architecture.
15. When the new contracts are ready, revise Validation #2 success criteria to test Svif's generalized executor/project semantics plus the Agnir cold-start/discovery contract, while retaining the strong stateful-provider, trust-boundary, exact-provenance, and external-observation pressure from the original plan where those invariants survive review.

## Historical evidence to preserve

16. Keep Validation Project #1 (`mattamior/agent-skills`) as a passed ZeroLocal v0.1 clean-room result. Its main reusable design evidence includes:
   - discovery/resumability failure pressure;
   - dependency/toolchain recovery;
   - protected-secret trust boundaries;
   - bounded production readiness observation;
   - provider resource lifecycle awareness;
   - immutable revision provenance.
17. Reinterpret the **lesson**, not the old claim: the fresh-conversation RPM failure becomes evidence for a generalized fresh-executor / cold-start discovery invariant in Agnir and Svif.

## Productization

18. Keep Plugin/product packaging gated. Do not freeze a new distribution surface while Svif Core and Agnir interfaces are undergoing a deliberate architecture migration.
19. After the generalized contracts stabilize, validate them on multiple execution surfaces and project shapes before deciding the next packaging form. ChatGPT Skill/Plugin remains one integration option rather than the normative architecture.
