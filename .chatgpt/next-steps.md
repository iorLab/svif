# Next Steps

## Immediate — make Svif v0.2 and Agnir 0.1 testable

1. Treat ZeroLocal v0.1, its Skills, conformance checks, validation evidence, and Cloudflare reference as the **historical predecessor baseline**. Do not silently rename existing claims into Svif conformance.
2. Continue coordinated work with `mattamior/rpm`, which is evolving the PPMP / PPM / Sandminni lineage into **Agnir**.
3. Tighten `SVIF_ARCHITECTURE_DRAFT.md` and `mattamior/rpm/spec/AGNIR_CORE_DRAFT.md` into testable normative drafts before broad rename work.
4. In Agnir, finalize the Discovery Record, Locator Chain, cold-start failure semantics, and PPMP v2 -> Agnir 0.1 migration mapping.
5. In Svif, keep the dependency at the **Agnir Core protocol** layer. Do not depend on a particular Agnir implementation, backend, adapter, repository layout, or execution surface.
6. Treat `Agnir Core 0.1` as the current draft dependency target; freeze the exact release compatibility version/range only after Agnir Core stabilizes.

## Svif Core refinement

7. Refine the generalized lifecycle:
   - `DISCOVER -> PLAN -> CHANGE -> VERIFY -> DELIVER -> OBSERVE -> CHECKPOINT`;
   - `REPAIR` returns to the earliest violated invariant;
   - states may be skipped only when their semantic effect is inapplicable.
8. Decide whether `PLAN` remains a normative lifecycle state for all operations or may be implicit for trivial work while retaining planning semantics.
9. Define stable candidate provenance precisely enough to cover Git revisions, content digests, versioned objects/documents, transactions, and other unambiguous candidate identities.
10. Define the minimum machine-readable **Capability Adapter** contract, including capabilities, required authority, evidence outputs, failure classes, and optional delivery/observation hooks.
11. Keep these as Svif Core invariants unless later evidence disproves their generality:
   - evidence-driven lifecycle transitions;
   - stable candidate provenance;
   - verification/delivery authority separation;
   - observable success for externally claimed effects;
   - explicit trust boundaries;
   - adapter isolation;
   - durable continuation through Agnir.
12. Keep protected secret values inside authorized protected channels/stores. Core must not require secret transfer through unprotected conversational or execution surfaces.

## Svif Software Delivery Profile

13. Extract the strongest ZeroLocal software-delivery semantics into a future **Svif Software Delivery Profile** instead of keeping them universal Core requirements.
14. Re-evaluate and preserve where justified:
   - immutable SCM revision identity;
   - exact-validated-revision delivery;
   - CI evidence attribution;
   - provisioning/deployment substates beneath generic `DELIVER`;
   - stateful migration ordering;
   - production concurrency coordination;
   - provider resource lifecycle awareness;
   - remote recovery paths;
   - externally observed readiness/health.
15. Move repository-specific and GitHub-specific mechanics into SCM/repository adapters or profile conventions rather than Core.
16. Recast the Cloudflare reference as a **Svif Software Delivery + Cloudflare provider implementation**, not as a definition of Svif Core.

## Conformance migration

17. Design new Svif/Agnir conformance identifiers rather than renaming existing `ZL-*` claims in place.
18. Preserve Validation Project #1 (`mattamior/agent-skills`) as a passed ZeroLocal v0.1 result and requirements-discovery evidence.
19. Require future Svif conformance to test Agnir cold-start discovery from a fresh Executor without predecessor-private context.
20. Include at least one execution/storage arrangement materially different from the founding ChatGPT + GitHub + Cloudflare route so neutrality is demonstrated rather than asserted.
21. Add a multi-project workspace isolation case once Agnir's workspace-registry/discovery semantics are ready.

## Shared workspace / separate project state

22. Continue using this ChatGPT Project as a **workspace** for Svif and Agnir when useful, not as either project's canonical memory store.
23. Keep independent durable state for each Project. Project-scoped work loads only that Project; explicitly cross-project work loads both.
24. Persist cross-project decisions separately in each affected Project according to local meaning. Do not create a third shared mutable state store.
25. Update the external ChatGPT Project bootstrap to a thin multi-project registry only after repository-side Agnir discovery targets are explicit. Until then, do not claim fully proven fresh-context multi-project resumability.

## Validation Project #2 — `mattamior/cloud-mail`

26. Preserve `.chatgpt/validation-2.md` and the previously selected non-destructive stateful Cloudflare validation intent.
27. Keep Validation #2 paused until the Svif Core draft, Agnir dependency/discovery contract, Software Delivery Profile, and migration boundary are explicit enough to define conformance.
28. When resumed, revise success criteria to test Svif generalized executor/project semantics plus Agnir cold-start discovery while retaining stateful-provider, trust-boundary, candidate-provenance, and external-observation pressure where those invariants survive.

## Naming and packaging — defer until contracts settle

29. Do not broadly rename `iorLab/zerolocal`, `iorLab/zerolocal-cloudflare-starter`, `ZEROLOCAL.yaml`, Skill directories, public identifiers, or historical evidence until migration/compatibility rules are explicit.
30. Treat Skill, Plugin, CLI, SDK, IDE extension, and other surfaces as integrations/packaging rather than Svif Core architecture.
31. Revisit packaging only after the generalized contracts pass materially diverse conformance cases.
