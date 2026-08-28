# Svif Next Actions

1. **Freeze Svif Product Architecture before expanding conformance breadth.** Define the product around four first-class components: Orchestrator, Continuity Provider interface, Execution Surface interface, and Capability Provider interface.
2. Define the minimal Svif Orchestrator/runtime responsibilities: load continuity, materialize execution context, plan/coordinate operations, select/invoke capabilities, enforce authority/provenance, observe/reconcile outcomes, and checkpoint durable truth.
3. Define the three provider/surface boundaries concretely using the founding implementations without making them universal requirements:
   - Continuity Provider -> Agnir;
   - Execution Surface -> ChatGPT;
   - Capability/Effect Provider -> Cloudflare.
4. Re-evaluate `SVIF.yaml`. Decide whether it becomes a product-facing Project binding/configuration manifest and, if so, define its semantics for continuity, execution-surface, capability/provider, authority, and profile bindings.
5. Separate specification-repository integrity checks from portable Svif product/contract conformance. Rename/restructure the current `conformance/check_svif_0_2.py` role accordingly before treating it as a generic Svif checker.
6. Map existing `spec/CORE.md`, Evidence, Capability Adapter, Software Delivery profile, schemas, and fixtures into the Product Architecture as internal portable contracts rather than the whole product identity.
7. Design the first explicit ChatGPT integration/product surface while keeping canonical Project truth execution-surface-neutral; preserve the longer-term Plugin distribution target.
8. Determine which reusable behaviors currently living in `iorLab/svif-cloudflare-reference` should become Svif-owned Cloudflare capability implementation, with the reference repository consuming/testing them as an E2E integration testbed.
9. After the Product Architecture is frozen, resume broader neutrality evidence: materially non-GitHub/Cloudflare execution/storage case, then multi-project workspace isolation after Agnir's fixture is ready.
10. Freeze the exact Agnir compatibility expression only after Agnir Core `0.1` release criteria are concrete.
11. Keep live Cloudflare delivery disabled unless explicitly authorized. If authorized later, preserve exact verified-candidate delivery and require independent observation before success claims.
12. Keep incidental branch cleanup deferred until the new Svif version is substantially complete; preserve `legacy/zerolocal-v0.1` unchanged as predecessor history.

## Completed in the current implementation sequence

- Canonical repositories are `iorLab/agnir`, `iorLab/svif`, and `iorLab/svif-cloudflare-reference`.
- Execution-surface-specific canonical bootstrap was removed from Svif; Project cold start uses Agnir discovery rather than ChatGPT-owned state.
- Evidence-chain executable fixtures and concrete Capability Adapter fixtures are implemented and previously passed Svif conformance.
- `iorLab/svif-cloudflare-reference` was migrated to native Svif/Agnir structure with predecessor preservation on `legacy/zerolocal-v0.1`.
- Cloudflare reference static/provenance/authority-gate behavior is proven; live delivery/observation remains unproven and disabled without explicit authority.
- Validation Project #2 (`mattamior/cloud-mail@svif/cloudflare-validation`) has proven credential-free static verification for immutable candidate `5b32462f3725327805f0dd696475a16f07b666aa` via workflow run `33102032043`; protected delivery was skipped.
- On 2026-08-28, architecture review corrected Svif's identity from a pure Project-operation protocol back to a Project orchestration product whose specification/contracts are internal product foundations and whose mature distribution target remains a Plugin.
