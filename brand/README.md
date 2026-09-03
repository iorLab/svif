# Svif brand system

This directory contains the fidelity-first Svif identity system derived from the Principal-approved Today 10:42 AM visual reference.

## Directory responsibilities

```text
brand/
├── README.md                         # this guide
├── APPROVED-VISUAL-REFERENCE.md      # locked visual authority and source hashes
├── PRODUCTION-STATUS.md              # current production gate / completed work
├── brand-handoff.md                  # downstream usage rules
├── brand-process-log.md              # design/production chronology retained for audit
├── reference/                        # extraction coordinates and reference manifests
├── masters/                          # raster-master manifest + any future approved master geometry
│   └── candidates/                   # rejected/review candidates; not production truth
├── exports/                          # committed delivery derivatives that passed binary verification
├── qa/                               # final review scope and QA evidence metadata
└── tools/                            # deterministic extraction/build tooling
```

## Production authority

The current Svif production model is fidelity-first raster, not an approximate pure-vector reconstruction. `masters/RASTER-MASTER-MANIFEST.md` records the native production assets and expected SHA-256 values. `tools/build-production-assets.py` reconstructs them only from the byte-exact approved board and rejects a source hash mismatch.

The old `masters/candidates/svif-wordmark-trace-v0.1.svg` and rejected S-vector experiments are provenance only; they must not replace the approved raster appearance.

## Derivatives

The complete local delivery package contains mark, wordmark, horizontal/vertical lockups, light/dark/monochrome usage, app icon, 128/64/32/16 favicons and social card. The 64/32/16 favicon PNGs have already been committed through Git binary blobs and verified by Git blob SHA. Larger binaries remain hash-gated until a byte-safe repository path is available.

## QA

`qa/FINAL-QA.md` defines the symmetric 13-item final QA scope shared with Agnir. The approved Today 10:42 AM board remains visually authoritative over every derivative.

## Integration status

Everything in this directory is branch-local until reconciled with the latest authoritative `main` and integrated coherently. Integration must not turn a raster-backed transport wrapper into a claimed true-vector master or regenerate the S artwork.
