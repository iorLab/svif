# Checkpoint — 2026-08-27 repository identity transition

## Scope

Durable checkpoint after the first direct Svif 0.2 main-line implementation and before coordinated GitHub repository renaming.

## Source boundary

- Project: Svif
- Repository at checkpoint entry: `iorLab/zerolocal`
- Branch: `main`
- Pre-checkpoint head: `f524bf034cbfd2836ca7225cec00e8c1ec31a05c`
- Pre-checkpoint verification: Svif conformance workflow run `33081158821` completed successfully.
- Predecessor boundary: `legacy/zerolocal-v0.1` at the previously recorded ZeroLocal v0.1 boundary; the branch remains authoritative predecessor history and is not to be renamed.

## Durable result

- Svif 0.2 Core, Capability Adapter, Evidence, Software Delivery Profile, schemas, conformance, and Agnir-backed continuity are the active `main` structure.
- Svif depends on Agnir Core 0.1 semantics only; it does not depend on Agnir's repository, backend, GitHub, Git, ChatGPT, or storage realization.
- The repository-rename decision has changed from deferred cleanup to immediate next execution work.
- Planned rename order is Agnir first, Svif second, Cloudflare starter third.
- Planned names are `mattamior/agnir`, `iorLab/svif`, and `iorLab/svif-cloudflare-starter`.
- Legacy branch names remain unchanged to preserve predecessor identity.

## Resume point

1. Rename `mattamior/rpm` to `mattamior/agnir` and reconcile Agnir durable repository references.
2. Rename `iorLab/zerolocal` to `iorLab/svif` and reconcile Svif/Agnir cross-project references.
3. Rename `iorLab/zerolocal-cloudflare-starter` to `iorLab/svif-cloudflare-starter` and then migrate it as the Software Delivery + Cloudflare Provider Adapter reference implementation.
4. Verify conformance after each repository identity transition.
5. Continue executable Agnir cold-start pressure cases and Svif evidence-chain/adapter fixtures before resuming Validation Project #2.

The Git commit containing this record is the checkpoint commit; its immutable commit identity is resolved from repository history rather than recursively embedded in this file.
