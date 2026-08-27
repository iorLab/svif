# Svif

Svif is an execution-environment-independent Project operation protocol.

It coordinates Project work from discovery and planning through change, verification, optional delivery, external observation, repair, and durable continuation. Its stable rule is:

> The Project persists; Executors and execution environments may change.

## Active line

`main` is the Svif `0.2` development line. ZeroLocal v0.1 is preserved as predecessor history on `legacy/zerolocal-v0.1`; predecessor `ZL-*` conformance and ChatGPT Skill packaging are not active Svif Core structure.

The repository is still named `iorLab/zerolocal` during transition. Repository naming is not protocol identity.

## Structure

```text
SVIF.yaml                           # this repository's Svif self-description
AGNIR.yaml                          # Agnir cold-start discovery anchor
.agnir/                             # authoritative Project continuity for this repo
spec/CORE.md                        # Svif Core 0.2
spec/CAPABILITY_ADAPTER.md          # portable adapter semantics
spec/EVIDENCE.md                    # candidate/evidence envelope
profiles/SOFTWARE_DELIVERY.md       # software-delivery specialization
schemas/                            # reference machine-readable contracts
conformance/                        # executable new-line conformance pressure
```

`SVIF.yaml` is a repository self-description, not a universal mandatory Svif Core filename. `AGNIR.yaml` is defined by Agnir's repository/filesystem profile, not by Svif Core.

## Lifecycle

`DISCOVER -> PLAN -> CHANGE -> VERIFY -> DELIVER -> OBSERVE -> CHECKPOINT`

`REPAIR` returns to the earliest violated invariant.

PLAN semantics are required before material mutation, but trivial operations may coalesce PLAN in an execution trace when no separate plan artifact is material. DELIVER is optional when no external actuation is required. OBSERVE is mandatory whenever external effect is claimed.

## Agnir

Svif delegates durable Project continuity to Agnir. The active development target is Agnir Core `0.1`, consumed at the protocol layer only.

Svif does not require Agnir's reference repository, storage backend, ChatGPT adapter, Git, GitHub, or `.agnir/` layout. This repository happens to self-host using Agnir's repository/filesystem profile.

## Capability Adapters

Provider/tool-specific capabilities are isolated behind adapters. Operation names remain implementation/profile-extensible; each operation maps to a portable Core effect such as `verify`, `actuate`, or `observe`.

## Evidence

Svif `evidence-record/0.2` standardizes stable subject identity, derivation, target identity, result status, producer, authority reference, and evidence locator so candidate provenance can survive adapter boundaries.

For software delivery, full immutable Git SHA remains a strong SCM realization, but Git is not the Core candidate model.

## Conformance

Run the initial active-line structural checker:

```bash
python conformance/check_svif_0_2.py
```

Release-quality conformance still requires evidence-chain fixtures, adapter fixtures, provider/profile evidence, Agnir cold-start/isolation pressure, and at least one materially different execution/storage arrangement from the founding ChatGPT + GitHub + Cloudflare path.
