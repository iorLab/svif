# 2026-08-28 — Svif Product Architecture + minimal runtime evidence

## Scope

This evidence records the architecture correction from a specification/protocol-shaped repository to an executable Project orchestration product foundation, plus the first minimal Orchestrator kernel.

It does not claim that Agnir, ChatGPT, or Cloudflare concrete product adapters are complete, and it does not claim live Cloudflare delivery.

## Product Architecture freeze

Architecture commit:

`bb6f445621b65b7ad9cfa99ac0dea759e4ad40fa`

Material changes:

- Svif product identity changed from pure Project-operation protocol framing to **Project orchestration product**.
- Added `ARCHITECTURE.md` with four first-class components: Orchestrator, Continuity Provider, Execution Surface, Capability Provider.
- Added `project-binding/0.2` through `spec/PROJECT_BINDING.md` and `schemas/project-binding.schema.json`.
- Recast `SVIF.yaml` as the repository/filesystem Project-binding serialization.
- Recast `spec/CORE.md` as an internal portable orchestration contract.
- Split repository integrity (`checks/check_repository.py`) from portable contract conformance (`conformance/check_contracts.py`).

The first architecture run exposed a wording-sensitive repository-integrity assertion while portable contracts were already successful. This was a checker overfit, not a product-contract failure.

Semantic checker fix:

`e201de612dab27bb025f386861ada639a5b0f1e2`

Verification run:

- workflow run `33138329497`;
- repository-integrity: success;
- portable-contracts: success.

## Minimal executable Orchestrator

Implementation commit:

`c398f17150d5fe868dc60f97dceb58e35025e2e9`

Added:

- `src/svif/runtime.py`;
- `src/svif/__init__.py`;
- `tests/test_runtime.py`;
- dedicated `runtime-kernel` CI job.

The kernel defines generic Continuity Provider, Execution Surface, and Capability Provider interfaces and an Orchestrator that enforces cross-boundary coherence.

Executable scenarios prove:

1. effectful success orders `load -> execute -> actuate -> observe -> checkpoint`;
2. non-effectful work orders `load -> execute -> checkpoint`;
3. a subject without exact successful verification cannot be actuated or checkpointed;
4. missing protected authority prevents actuation and checkpoint;
5. observation subject mismatch prevents checkpoint after actuation.

CI evidence:

- workflow run `33138534555`: **success**;
- repository-integrity job `98743936893`: success;
- runtime-kernel job `98743936972`: success;
- portable-contracts job `98743936987`: success.

## Boundary proven

The repository now contains both portable product contracts and an executable orchestration kernel. The Orchestrator is not hard-coded to the founding provider names.

## Boundary not yet proven

The founding product bindings are not yet concrete runtime adapters:

- Agnir Continuity Provider adapter: not yet implemented;
- ChatGPT Execution Surface integration: not yet implemented;
- Svif-owned Cloudflare Capability Provider implementation: not yet implemented;
- end-to-end Agnir + ChatGPT + Cloudflare Orchestrator scenario: not yet implemented;
- live Cloudflare delivery/observation: not authorized/proven.
