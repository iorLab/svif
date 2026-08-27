# Svif Next Actions

1. Decide the final packaging identity of `iorLab/svif-cloudflare-starter`: keep `starter` only if it is intended as a user-copyable bootstrap/template; otherwise rename/recast it as a Cloudflare reference implementation or adapter testbed.
2. If retained, recast that repository from ZeroLocal v0.1 into Svif Software Delivery + Cloudflare Provider Adapter terminology and executable evidence while preserving predecessor history separately.
3. Rewrite Validation Project #2 (`mattamior/cloud-mail`) success criteria for Svif Core 0.2 + Software Delivery Profile 0.2 + Agnir Core 0.1 cold start.
4. Add a materially non-ChatGPT/GitHub/Cloudflare execution/storage conformance case to prove neutrality rather than assert it.
5. Add multi-project workspace isolation conformance after Agnir's corresponding fixture is ready.
6. Freeze the exact Agnir compatibility expression only after Agnir 0.1 release criteria are concrete.
7. Keep incidental branch cleanup deferred until the new Svif version is substantially complete; preserve `legacy/zerolocal-v0.1` unchanged as predecessor history.

## Completed in the current implementation sequence

- Coordinated repository identity transition completed: `mattamior/rpm` -> `iorLab/agnir` (including organization transfer), `iorLab/zerolocal` -> `iorLab/svif`, and `iorLab/zerolocal-cloudflare-starter` -> `iorLab/svif-cloudflare-starter`.
- Canonical repository references in Svif's `AGNIR.yaml`, `SVIF.yaml`, ChatGPT bootstrap shim, README, and durable state were reconciled to the new identities.
- Evidence-chain executable fixtures: positive candidate -> transformation -> verification -> delivery -> observation chain plus deliberate unverified-replacement provenance failure. Commit `853ea4bf05679ab2b03864aeaa01e8aae9350542`; conformance run `33090238664` succeeded.
- Concrete Capability Adapter fixtures for workspace/SCM, verification, delivery/provider, and observation boundaries, with semantic effect, authority/retry, portable failure, Evidence I/O, credential-reference, provenance, and independent-observation checks. Commit `67c7b4e93e0130d37c01c40a261b55fba381f786`; conformance run `33090480399` succeeded.
