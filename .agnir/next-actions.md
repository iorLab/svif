# Svif Next Actions

1. Execute the coordinated repository rename in this order: `mattamior/rpm` -> `mattamior/agnir`, `iorLab/zerolocal` -> `iorLab/svif`, then `iorLab/zerolocal-cloudflare-starter` -> `iorLab/svif-cloudflare-starter`.
2. After each rename, immediately reconcile canonical repository references in `AGNIR.yaml`, `SVIF.yaml` where applicable, `.chatgpt/project-memory.yaml`, README/docs, cross-project references, and CI/reference URLs; verify conformance on the renamed repository rather than relying on GitHub redirects.
3. Add executable evidence-chain fixtures covering source candidate -> artifact transformation -> verification -> delivery -> observation and a deliberate provenance mismatch failure.
4. Add concrete Capability Adapter descriptors and conformance fixtures for at least workspace/SCM, verification, delivery/provider, and observation boundaries.
5. Recast the renamed Cloudflare starter as a Svif Software Delivery + Cloudflare Provider Adapter reference implementation while preserving ZeroLocal history separately.
6. Rewrite Validation Project #2 (`mattamior/cloud-mail`) success criteria for Svif Core 0.2 + Software Delivery Profile 0.2 + Agnir Core 0.1 cold start.
7. Add a materially non-ChatGPT/GitHub/Cloudflare execution/storage conformance case to prove neutrality rather than assert it.
8. Add multi-project workspace isolation conformance after Agnir's corresponding fixture is ready.
9. Freeze the exact Agnir compatibility expression only after Agnir 0.1 release criteria are concrete.
10. Keep incidental branch cleanup deferred until the new Svif version is substantially complete; preserve `legacy/zerolocal-v0.1` unchanged as predecessor history.
