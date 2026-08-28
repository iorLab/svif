# ZeroLocal predecessor -> Svif/Agnir migration evidence

Date: 2026-08-28

## Scope

This record audits the real predecessor Project preserved at `iorLab/svif@legacy/zerolocal-v0.1` against the active Svif/Agnir Project on `main`.

Predecessor boundary:

- branch: `legacy/zerolocal-v0.1`
- commit: `8ccbb1d30520ca3d0b8b9f2cfe2963d35a853cf6`
- predecessor memory entry: `.chatgpt/project-memory.yaml`
- predecessor mutable continuity: `.chatgpt/state.yaml`, `.chatgpt/next-steps.md`, `.chatgpt/decisions.md`

Target Project:

- canonical repository: `iorLab/svif`
- active ref: `main`
- continuity discovery: `AGNIR.yaml`
- product binding: `SVIF.yaml`
- canonical continuity: `.agnir/state.md`, `.agnir/next-actions.md`, `.agnir/decisions.md`, `.agnir/evidence/`

This is genuine real-world predecessor evidence, but the predecessor serialization is an earlier v1/RPM-era `.chatgpt/project-memory.yaml`, **not PPMP v2.0.0**. It therefore MUST NOT be presented as exact PPMP v2 migration evidence.

## Migration result

The predecessor-to-current transition is accepted as a **semantic predecessor migration PASS with one discovered-and-repaired durable-knowledge regression**, subject to the classification boundary above.

The target Project no longer depends on predecessor-private conversational context or the predecessor `.chatgpt/` bootstrap. Current cold start resolves through Agnir `repository-filesystem/0.1` from `AGNIR.yaml`, and the executable founding path checkpoints and reloads continuity through the active Agnir adapter.

## Material durable-knowledge matrix

| Predecessor durable knowledge | Current disposition | Evidence / interpretation |
| --- | --- | --- |
| Long-term product form is `installable-plugin` | **Preserved after repair** | The predecessor manifest and state explicitly named `installable-plugin`. Migration audit found this exact durable intent had been generalized away; it has now been restored in `ARCHITECTURE.md`, `.agnir/state.md`, `.agnir/decisions.md`, `README.md`, and `README.zh-CN.md`. |
| Plugin should package stabilized behavior rather than discover core semantics | **Preserved / generalized** | Current dependency direction is `Plugin / distribution -> Execution Surface integration -> Orchestrator -> Continuity + Capability Providers`; ChatGPT app/MCP packaging is explicitly not the product identity. |
| Provider-neutral core; Cloudflare is the first provider, not a universal core dependency | **Preserved and structurally strengthened** | Current architecture separates Orchestrator from Capability Providers; Cloudflare is the founding provider under `src/svif/capabilities/cloudflare.py` and is not a kernel dependency. |
| Provider-specific behavior should remain modular | **Preserved** | Cloudflare behavior is behind the Capability Provider / injected transport boundary and integration descriptor. The former standalone reference repository is retired as an active project. |
| Human/trusted boundary governs secrets, account authority, destructive changes, billing/risk approvals | **Preserved and tightened** | Protected authority is supplied by trusted integration context; untrusted model/result payloads cannot self-grant it. Secret values remain outside Project memory/model payloads and protected operations remain authority-gated. |
| CI/deployment provenance must preserve the exact validated revision/subject | **Preserved / generalized** | Svif requires exact verified-subject evidence before external actuation. The current abstraction is subject identity rather than Git-SHA-only semantics, so the invariant applies beyond Git delivery. |
| Deployment command success is insufficient; independent external observation is required | **Preserved** | Independent observation is mandatory before external success can be checkpointed. This is enforced by the Orchestrator and founding Cloudflare provider tests/E2E. |
| Durable Project work must resume from durable state rather than founding chat history | **Preserved and generalized through Agnir** | Continuity is owned by the Project; ChatGPT is only one Execution Surface. Agnir loads Current State / Next Actions / Decisions / Evidence for fresh execution contexts. |
| ChatGPT Project Instructions should carry locator-only bootstrap metadata, not mutable state | **Semantically preserved; ChatGPT-specific mechanism retired from canonical Project structure** | Agnir generalizes this into an authorized Project Entry Point + Discovery Record / locators. Active Agnir Projects do not require `.chatgpt/project-memory.yaml` or ChatGPT Project Instructions as canonical structure. |
| Repository/GitHub is canonical source and RPM store | **Intentionally generalized, not preserved as Core requirement** | Svif currently uses repository/filesystem serialization, but Agnir Core and Svif kernel are not Git/GitHub-bound. Repository hosting is a profile/integration choice, not universal product truth. |
| ZeroLocal means the normal supported lifecycle does not require human local checkout/toolchain/git/deploy CLI | **Not promoted as a universal Svif kernel invariant** | Svif is now a broader Project orchestration product with replaceable Execution Surfaces. The predecessor property remains historical product lineage, but current Core does not define "no local tools" as a universal conformance requirement. |
| Skill-first implementation and multi-project clean-room stabilization before Plugin | **Predecessor implementation sequence retired; underlying portability pressure retained** | Active `main` no longer treats ZeroLocal Skills as the product surface. Founding E2E and planned broader neutrality/non-founding validation retain the requirement to avoid hidden-context dependence before mature Plugin packaging. |
| Validation Project #1 is a successful historical ZeroLocal case | **Preserved as history, not relabeled** | `history/PREDECESSOR.md` keeps it as ZeroLocal v0.1 evidence. It is not presented as Svif 0.2 conformance or current live-provider evidence. |
| Validation Project #2 (`cloud-mail`) was selected but not started under predecessor rules | **Not carried forward as an active validation claim** | It must be redefined against Svif/Agnir contracts before any future use. Existing older intent is historical only. |

## Explicitly retired predecessor structures

The following are intentionally not active current Project structures:

- `.chatgpt/project-memory.yaml` as the canonical continuity bootstrap;
- `.chatgpt/state.yaml`, `.chatgpt/next-steps.md`, `.chatgpt/decisions.md` as active memory locations;
- ZeroLocal Core / Cloudflare Provider Skills as the active product architecture;
- `SPECIFICATION.md` and predecessor `ZL-*` conformance as current Svif contracts;
- the standalone Cloudflare reference repository as an active canonical project.

They remain recoverable from `legacy/zerolocal-v0.1` and Git history, so predecessor conformance/history stays distinguishable from the target architecture.

## Fresh-start / target-conformance evidence

The current target independently establishes its own compatibility and discovery:

- `AGNIR.yaml` declares Agnir Core `0.1`, profile `repository-filesystem/0.1`, target Project identity, and target continuity locators;
- `SVIF.yaml` declares `project-binding/0.2`, the Agnir compatibility line, and the current product artifacts;
- `tests/test_founding_e2e.py` performs target continuity load, externally driven ChatGPT bridge handoff, trusted authority, capability actuation, independent observation, checkpoint, and continuity reload without using predecessor `.chatgpt/` state;
- current Svif product checks at checkpoint head `027dd1de5093f18a8699b7316eeb4a87ffc1a2cb` passed in run `33149153852`.

## Regression found and repaired

The audit found one material durable-knowledge regression: `installable-plugin` existed explicitly in predecessor memory but had disappeared from current canonical state during the architecture rewrite, leaving only a generic distribution concept.

That regression is repaired. The mature Svif target is again explicitly an installable Plugin, while ChatGPT Apps SDK / MCP remains the current Execution Surface packaging path rather than the product identity.

This finding demonstrates why migration validation must compare material Project knowledge, not only confirm that new locator files exist.

## Unmet / non-inherited claims

This record does **not** establish any of the following:

- exact PPMP v2.0.0 external migration evidence;
- current live Cloudflare production delivery or observation;
- current Svif conformance for historical ZeroLocal Validation Project #1;
- authorization for any protected external effect.

Those claims require their own target-era evidence.

## Conclusion

The real ZeroLocal predecessor is semantically recoverable and its material product knowledge has either been preserved, explicitly generalized/retired, or durably classified. The one detected durable-intent regression was repaired. The active Project can cold-start and operate through Svif/Agnir without predecessor-private context.

Classification: **real predecessor-memory migration PASS (v1/RPM-era), not exact PPMP v2 evidence**.
