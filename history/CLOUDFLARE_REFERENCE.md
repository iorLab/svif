# Retired Cloudflare reference project

The former repository `iorLab/svif-cloudflare-reference` was used during the ZeroLocal -> Svif transition as an executable Cloudflare pressure test.

It is **not part of the active Svif architecture** after 2026-08-28. Cloudflare provider behavior and fixtures are owned by `iorLab/svif`.

## Preserved historical evidence

Historical claims remain evidence only and are not rewritten:

- migration commit `819495b9e708960a613285bb9f37ee859de1652f`; CI run `33096884459` succeeded;
- protected delivery run `33096910154` preserved the exact candidate but stopped at `CREDENTIAL_UNAVAILABLE`; no live delivery/observation success was established;
- authority-gate commit `45730121d60a6b8e03e1d5924b257be27ed73a9c`; CI run `33097281596` succeeded;
- deploy run `33097306221` was skipped while automatic delivery was disabled;
- final active reference `main` before retirement: `f5755a8fe94301cb6f6551c865d647c492616db2`.

The old repository may be physically deleted without loss of active Svif product state once this migration is accepted. Svif code, tests, release inputs, and Agnir state must never rely on that repository again.
