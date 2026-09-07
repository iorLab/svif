# Branch Archive

This file records branch names and tip commits that were intentionally retired from `iorLab/svif`. The repository governance target is **main-only**: `main` is the only long-lived branch; historical work is referenced by commit SHA and Git history rather than preserved branch refs.

## Retired branches

- `legacy/zerolocal-v0.1` -> `8ccbb1d30520ca3d0b8b9f2cfe2963d35a853cf6` — ZeroLocal v0.1 predecessor boundary and historical validation lineage.
- `fix/rpm-bootstrap-resume` -> `e705aa368adfa2778430349e6e411df48a64f1a1` — superseded RPM/ZeroLocal bootstrap-resumability work.
- `tmp/checkpoint-probe` -> `6032406771120d490282ec710a3ba160e1578c92` — obsolete checkpoint probe branch.
- `tmp/delete-test-never` -> `aa81568cfce4d13974b5b52b27da475ca63a0e45` — temporary branch-ref capability probe; no unique product work.
- `tmp/archive-write-probe` -> `aa81568cfce4d13974b5b52b27da475ca63a0e45` — temporary branch-ref capability probe; no unique product work.
- `brand/identity-system` -> `62e9aac53246cef4eccffacb9434ead9928c0c3c` — Principal-approved Svif identity-system production branch; material result integrated to authoritative `main` by PR #5 at `77ff3d0e8b3d0d691bb47529e065571c17a0aa81`.
- `promotion/agnir-1.0` -> `5a88eee4bc214b8da3b4c5f48640067b167248b8` — Principal-authorized semantics-preserving Svif Project promotion from Agnir Core/profile 0.2 to 1.0; material result integrated to authoritative `main` by PR #9 at `5da0eb76e38e817ba0f5111ce2b08750afa3b9c3`.

These SHAs are historical locators only. None of the retired branches is an active dependency, compatibility obligation, conformance input, or release gate for Svif.
