# Next Steps

## Immediate — converge the Svif v0.2 contract set

1. Preserve ZeroLocal v0.1, its Skills, `ZL-*` contracts, conformance checks, Cloudflare reference, and clean-room validation as **historical predecessor evidence**. Do not silently relabel them as Svif.
2. Reconcile these transition artifacts into one coherent normative Svif v0.2 draft:
   - `SVIF_ARCHITECTURE_DRAFT.md`;
   - `SVIF_CAPABILITY_ADAPTER_DRAFT.md`;
   - `profiles/SOFTWARE_DELIVERY_DRAFT.md`;
   - Agnir Core/Discovery/Migration drafts in `mattamior/rpm`.
3. Decide whether `PLAN` is always an explicit lifecycle state or may be implicit for trivial operations while planning semantics remain required.
4. Define the standard candidate/evidence envelope that connects:
   - source candidate identity;
   - transformed build/artifact identity;
   - verification result;
   - delivered identity;
   - target/environment identity;
   - external observation evidence.
5. Define machine-readable Capability Adapter schema/versioning and determine which operation names are Svif-Core-normative versus profile-extensible.
6. Keep adapter authority, secret references, failure mapping, retry/idempotency, and evidence semantics portable across provider/tool implementations.

## Agnir dependency boundary

7. Continue coordinated work with `mattamior/rpm` on the Agnir Core 0.1 contract and first repository/filesystem discovery profile.
8. Keep the Svif dependency at the **Agnir Core protocol** layer. Do not depend on a particular Agnir implementation, backend, adapter, repository layout, or ChatGPT integration.
9. Treat `Agnir Core 0.1` as the current draft dependency target; freeze the exact release compatibility version/range only after the Agnir Core/discovery contract is stable enough for conformance testing.
10. Ensure Svif-specific lifecycle, delivery, provider, and stricter protected-secret semantics do not leak into Agnir Core.

## Svif Core invariants to preserve

11. Keep these as Core unless further evidence shows they are domain-specific:
   - Project-centered authority and continuity;
   - execution-environment neutrality;
   - evidence-driven lifecycle transitions;
   - stable candidate provenance when material change identity matters;
   - verification/delivery authority separation;
   - observable success for externally claimed effects;
   - explicit Trust Boundaries;
   - Capability Adapter isolation;
   - durable continuation through Agnir;
   - repair routed to the earliest violated invariant.
12. Keep secret values inside authorized protected channels/stores. Core must not require secret transfer through unprotected conversational or execution surfaces.
13. Keep CHECKPOINT as a Svif lifecycle state but delegate durable memory/discovery/resumability semantics to Agnir rather than creating a Svif-specific memory contract.

## Software Delivery Profile refinement

14. Review `profiles/SOFTWARE_DELIVERY_DRAFT.md` against all ZeroLocal v0.1 contract families and Validation #1 evidence.
15. Preserve in the profile where justified:
   - stable/immutable delivery candidate identity;
   - exact verified-candidate delivery;
   - verification evidence attribution;
   - PREPARE/PROVISION, MIGRATE, DEPLOY/PUBLISH delivery substates;
   - stateful migration ordering and replay safety;
   - state-sensitive delivery concurrency coordination;
   - provider resource lifecycle awareness;
   - protected production authority separation;
   - externally observed readiness/health;
   - evidence-based recovery taxonomy.
16. Keep Git/repository/branch/PR/workflow mechanics in future SCM/repository profile or adapters rather than generic Software Delivery or Svif Core unless truly necessary.
17. Recast `iorLab/zerolocal-cloudflare-starter` as a **Svif Software Delivery + Cloudflare Provider Adapter reference implementation** after the generic adapter schema is stable enough.

## Conformance migration

18. Create new Svif conformance identifiers and tests. Do not rename existing `ZL-*` identifiers in place.
19. Define separate conformance layers for:
   - Svif Core;
   - Agnir continuity dependency;
   - Capability Adapter semantics;
   - Software Delivery Profile;
   - provider-specific implementation evidence.
20. Require a fresh-Executor Agnir cold-start case with no predecessor-private memory path supplied by the test harness.
21. Require evidence-chain tests that detect candidate/provenance mismatch across verification and delivery.
22. Include at least one execution/storage arrangement materially different from ChatGPT + GitHub + Cloudflare so neutrality is demonstrated rather than asserted.
23. Add a multi-project workspace isolation case when Agnir's discovery/registry profile is ready.

## Validation Project #2 — `mattamior/cloud-mail`

24. Preserve `.chatgpt/validation-2.md` and the existing non-destructive stateful Cloudflare validation intent.
25. Keep execution paused until Svif Core, Agnir discovery, Capability Adapter semantics, Software Delivery Profile, and new conformance layers are concrete enough to test.
26. Then rewrite Validation #2 success criteria to pressure:
   - fresh-Executor Agnir discovery;
   - existing-project adoption;
   - stable candidate/evidence chain;
   - stateful provider resources and migrations;
   - non-destructive resource lifecycle handling;
   - protected trust boundaries;
   - externally observed frontend/backend readiness;
   - repair routing across Project, adapter, provider, and continuity layers.

## Shared workspace / separate durable state

27. Continue using this ChatGPT Project as a workspace for Svif and Agnir when useful, not as either project's source of truth.
28. Keep independent durable state for each Project; persist cross-project decisions locally in each affected Project.
29. Do not create shared mutable workspace memory. A future workspace registry may contain only project/discovery locators.
30. Update the external ChatGPT Project bootstrap to that thin registry only after repository-side Agnir discovery targets are explicit.

## Naming and packaging — deferred

31. Defer broad renames of `iorLab/zerolocal`, `iorLab/zerolocal-cloudflare-starter`, `ZEROLOCAL.yaml`, Skill directories, public identifiers, and historical files until migration/compatibility rules are explicit.
32. Treat Skill, Plugin, CLI, SDK, IDE extension, CI automation, and similar surfaces as integrations/packaging rather than Svif Core architecture.
33. Revisit product packaging only after generalized Core/profile/adapter contracts pass materially diverse conformance cases.
