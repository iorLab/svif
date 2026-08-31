# First-use bootstrap checkpoint — 2026-09-01

## Durable conclusion

Svif first-use onboarding is a product responsibility. A consumer using Svif on an ordinary selected Project MUST NOT be required to pre-initialize Agnir or pre-create `SVIF.yaml` before first use.

The shared Svif Plugin procedure now distinguishes:

1. a genuinely uninitialized Project, which may be bootstrapped through the founding Agnir repository/filesystem Continuity Provider path;
2. an existing but broken Agnir/Svif setup, which is a repair case and preserves Agnir failure semantics;
3. a Project intentionally bound to another Continuity Provider, which must not be overwritten with Agnir.

For a genuine first-use Project, Svif establishes one stable Project identity, initializes Agnir Core `0.1` / `repository-filesystem/0.1` durable continuity, creates/validates a matching minimal `project-binding/0.2` `SVIF.yaml`, fresh-activates from the Project root, and then continues the user's original Project task in the same operation.

Agnir remains an independent protocol/project. The bootstrap consumes Agnir protocol/profile semantics through Svif's founding Continuity Provider integration and does not make the Agnir Skill repository, a prior Agnir installation conversation, GitHub, or another execution surface a runtime prerequisite.

## Implementation and validation baseline

Primary implementation evidence remains `.agnir/evidence/2026-08-31-plugin-first-use-bootstrap-fix.md`.

- behavior implementation/fix baseline: `b90d1f8976b0e03d2c5a3b70c9bbb4b032c37724`;
- `Svif product checks` run `33384858568`: `completed / success`;
- later durable-state/evidence indexing baseline: `f39093d1e26fb13e12ee27d93af66f64736ff6d1`;
- `Svif product checks` run `33385105552`: `completed / success`.

The regression suite includes `tests/test_plugin_first_use_bootstrap.py`. Repository/package CI success proves repository consistency and the encoded first-use contract; it does not prove installation or invocation on a real Codex or ChatGPT client.

## Canonical resume point

The next decisive external exercise is the first real repository-backed Codex install/invocation from an ordinary Project with:

- no pre-installed Agnir;
- no pre-created `SVIF.yaml`;
- exactly one selected Project root.

The exercise should observe whether Svif itself performs first-use classification and founding continuity/binding bootstrap, preserves existing Project instructions, continues actual Project work, verifies the result, checkpoints durable truth, and supports resume from a fresh Codex context. Record the exact client/surface and accepted package/revision provenance when exposed.

After that first-use case, run a second Codex case on an already initialized Agnir/Svif Project to validate ordinary resume behavior, then proceed to Cursor-native distribution metadata/testing while keeping `plugin/skills/svif/SKILL.md` single-sourced.

The OpenAI public/personal ChatGPT publication path remains externally blocked at publisher verification/payment-method eligibility. The repository-side Skills-only package remains submission-ready and must not be weakened or converted to MCP merely to bypass that account-level gate.

## Evidence boundary

At this checkpoint there is still no real Codex client installation/invocation evidence and no personal ChatGPT public-directory installation evidence. Do not claim either until the respective real client exercise has been observed and recorded.
