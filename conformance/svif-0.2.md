# Svif 0.2 Portable Contract Conformance

This directory exercises portable contracts used by the Svif product. It is intentionally distinct from checks that validate the structure of the `iorLab/svif` repository itself.

Run:

```bash
python conformance/check_contracts.py
```

The current executable layer validates:

- `project-binding/0.2` schema identity and the required Continuity Provider binding;
- Capability Adapter `0.2` semantic-effect vocabulary;
- concrete adapter descriptors for workspace/SCM, verification, delivery/provider, and observation boundaries;
- adapter operation-to-effect mappings, authority/retry classes, portable failure classes, Evidence record I/O declarations, and protected credential references without secret-value transport;
- verification authority remains distinct from protected delivery authority;
- delivery/provider actuation consumes verification evidence, emits delivery evidence, and exposes `PROVENANCE_MISMATCH`;
- observation consumes delivery evidence and emits independent observation evidence;
- a positive evidence chain from candidate -> transformation -> verification -> delivery -> observation;
- a negative provenance fixture in which a valid derived replacement is delivered without independent verification and therefore fails.

This does **not** validate the `iorLab/svif` repository layout, README, Agnir state, predecessor files, or GitHub workflow structure. Those are product-repository integrity concerns checked by:

```bash
python checks/check_repository.py
```

Passing either checker alone is not a universal claim that an arbitrary Project is fully Svif-conformant. Product/runtime conformance will expand after the Svif Orchestrator and provider/surface interfaces become executable.
