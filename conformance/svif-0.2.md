# Svif 0.2 Conformance — initial executable layer

This conformance layer belongs to the new Svif line. It does not rename or reuse predecessor `ZL-*` conformance claims.

The initial structural checker validates:

- Svif `0.2` self-description and Agnir `0.1` continuity dependency;
- Agnir repository/filesystem cold-start anchor for this Project;
- presence of Core, Capability Adapter, Evidence, and Software Delivery Profile contracts;
- machine-readable adapter/evidence schema version constants and semantic enums;
- PLAN semantics and generalized lifecycle in Core;
- absence of active ZeroLocal v0.1 spec/Skill/conformance files on `main`;
- recovery of a material current fact from authoritative `.agnir` state.

This is not final release conformance. Evidence-chain fixtures, adapter fixtures, negative provenance tests, provider/profile implementation evidence, Agnir multi-project isolation, and a materially different execution/storage arrangement remain required.
