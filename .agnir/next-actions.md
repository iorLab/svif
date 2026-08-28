# Svif Next Actions

1. **Implement the concrete Agnir Continuity Provider adapter** against Agnir Core `0.1` repository/filesystem discovery and checkpoint semantics, while keeping the Orchestrator dependent only on the generic Continuity Provider interface.
2. **Define and implement the first ChatGPT Execution Surface integration/product surface.** It must consume Orchestrator-materialized Project context and return inspectable results/evidence without making chat-private context canonical Project truth. Keep the Plugin as the mature distribution target.
3. **Extract/implement reusable Cloudflare Capability Provider behavior under Svif ownership.** Preserve exact verified-subject delivery, protected authority, provider failure mapping, and independent observation; evolve `iorLab/svif-cloudflare-reference` toward consuming/testing this product capability.
4. **Build one end-to-end founding scenario** wiring Agnir + ChatGPT + Cloudflare through the Orchestrator. The scenario must demonstrate continuity load, execution/verification, authority-gated actuation, observation, reconciliation, and checkpoint without transporting protected secret values through Project state.
5. After the founding product path is executable, resume broader neutrality evidence: a materially non-GitHub/Cloudflare execution/storage case, then multi-project workspace isolation after Agnir's corresponding fixture is ready.
6. Freeze exact Agnir compatibility/version expression only after Agnir Core `0.1` release criteria are concrete.
7. Keep live Cloudflare delivery disabled unless explicitly authorized. If authorized later, preserve exact verified-candidate delivery and require independent observation before success claims.
8. Keep incidental branch cleanup deferred until the new Svif version is substantially complete; preserve `legacy/zerolocal-v0.1` unchanged.

## Completed in the current implementation sequence

- Product identity corrected: Svif is a Project orchestration product, not a pure protocol; mature target remains Plugin distribution.
- Product Architecture `0.2` frozen around Orchestrator + Continuity Provider + Execution Surface + Capability Provider in commit `bb6f445621b65b7ad9cfa99ac0dea759e4ad40fa`.
- `SVIF.yaml` converted to the repository/filesystem serialization of `project-binding/0.2`; `spec/PROJECT_BINDING.md` and schema added.
- Repository integrity split from portable product-contract conformance. Run `33138329497` succeeded after eliminating wording-sensitive repository-check overfit.
- Minimal executable Orchestrator kernel implemented at `src/svif/runtime.py` in commit `c398f17150d5fe868dc60f97dceb58e35025e2e9`.
- Runtime tests prove the full effectful sequence, non-effectful checkpoint path, provenance blocking, authority blocking, and observation-mismatch blocking.
- Product-check run `33138534555` succeeded across repository-integrity job `98743936893`, runtime-kernel job `98743936972`, and portable-contracts job `98743936987`.
- Cloudflare reference static/provenance/authority-gate behavior remains proven; live delivery/observation remains unproven and disabled without explicit authority.
- Validation Project #2 (`mattamior/cloud-mail@svif/cloudflare-validation`) retains proven credential-free static verification for immutable candidate `5b32462f3725327805f0dd696475a16f07b666aa`; protected delivery was skipped.
