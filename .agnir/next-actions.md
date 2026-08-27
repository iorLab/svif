# Svif Next Actions

1. Execute the coordinated repository rename in this order: `mattamior/rpm` -> `mattamior/agnir`, `iorLab/zerolocal` -> `iorLab/svif`, then `iorLab/zerolocal-cloudflare-starter` -> `iorLab/svif-cloudflare-starter`. The current connected GitHub execution surface does not expose repository rename/settings mutation, so this remains pending rather than skipped.
2. After each rename, immediately reconcile canonical repository references in `AGNIR.yaml`, `SVIF.yaml` where applicable, `.chatgpt/project-memory.yaml`, README/docs, cross-project references, and CI/reference URLs; verify conformance on the renamed repository rather than relying on GitHub redirects.
3. Recast the Cloudflare starter as a Svif Software Delivery + Cloudflare Provider Adapter reference implementation while preserving ZeroLocal history separately; use it to add provider/profile implementation evidence beyond the generic Capability Adapter fixtures now on `main`.
4. Rewrite Validation Project #2 (`mattamior/cloud-mail`) success criteria for Svif Core 0.2 + Software Delivery Profile 0.2 + Agnir Core 0.1 cold start.
5. Add a materially non-ChatGPT/GitHub/Cloudflare execution/storage conformance case to prove neutrality rather than assert it.
6. Add multi-project workspace isolation conformance after Agnir's corresponding fixture is ready.
7. Freeze the exact Agnir compatibility expression only after Agnir 0.1 release criteria are concrete.
8. Keep incidental branch cleanup deferred until the new Svif version is substantially complete; preserve `legacy/zerolocal-v0.1` unchanged as predecessor history.

## Completed in the current implementation sequence

- Evidence-chain executable fixtures: positive candidate -> transformation -> verification -> delivery -> observation chain plus deliberate unverified-replacement provenance failure. Commit `853ea4bf05679ab2b03864aeaa01e8aae9350542`; conformance run `33090238664` succeeded.
- Concrete Capability Adapter fixtures for workspace/SCM, verification, delivery/provider, and observation boundaries, with semantic effect, authority/retry, portable failure, Evidence I/O, credential-reference, provenance, and independent-observation checks. Commit `67c7b4e93e0130d37c01c40a261b55fba381f786`; conformance run `33090480399` succeeded.
