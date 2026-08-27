# Validation Project #2 — `mattamior/cloud-mail`

## Status

**Selected — not started.**

## Why this project

Validation Project #1 primarily exercised a new static Workers deployment path. Validation #2 should pressure different parts of the provider contract instead of repeating the same shape.

`mattamior/cloud-mail` is a public, non-founding real repository that already targets Cloudflare and contains a materially stateful application:

- Cloudflare Workers backend;
- Vue frontend;
- D1 database usage;
- KV and R2 capabilities;
- mail ingress/sending integrations and other provider/account-level features;
- an existing Cloudflare deployment workflow;
- no ZeroLocal RPM manifest at selection time.

This makes it a useful adoption/retrofit test: ZeroLocal must inspect an existing provider-native architecture, distinguish validation from actuation, reason about provisioning/migrations and destructive account changes, preserve secret boundaries, and improve or replace existing delivery automation only when repository evidence requires it.

## Clean-room business goal

Bring the existing Cloud Mail repository under ZeroLocal and establish a reproducible repository-native Cloudflare delivery path for a **non-destructive validation deployment**. The deployed application must expose an observable healthy frontend/backend and any required stateful resources must be provisioned/migrated through an auditable repository-driven path.

Do **not** activate or change real production email routing, DNS, paid/external sending services, or destructive provider resources unless the user explicitly authorizes that trust-boundary action. The validation should still exercise a meaningful deployed application slice rather than stopping at static CI.

## Clean-room setup

1. Create a new ChatGPT Project dedicated to Validation #2 with Project-only memory.
2. Leave Project Instructions blank initially. Do not pre-seed RPM paths, Cloudflare resource topology, workflow fixes, provider hooks, secret names, or known ZeroLocal internals.
3. Ensure the connected GitHub repository is accessible.
4. Start with only the minimum source + intent, equivalent to:

   `Use the ZeroLocal Skills from iorLab/zerolocal to develop mattamior/cloud-mail. Bring the existing Cloud Mail app under ZeroLocal, create a non-destructive Cloudflare validation deployment with a working observable frontend/backend and required stateful resources, and let ZeroLocal proceed normally.`

5. Let the current ZeroLocal Core itself establish or request the locator-only durable Project bootstrap after it creates/adopts RPM. This specifically re-validates the bootstrap fix from Validation #1 from the beginning of a new project.
6. Do not coach the clean-room agent on D1/KV/R2 provisioning, migrations, existing workflow defects, exact deployment design, or which provider/account actions are safe. Those decisions must come from repository/provider evidence.

## Required observations

Record whether the run can:

- adopt a non-empty existing Cloudflare-native repository without replacing its architecture unnecessarily;
- establish RPM and durable fresh-context bootstrap correctly on the first run;
- separate untrusted CI from credentialed deployment;
- discover and validate the repository's existing frontend/backend build and test paths;
- classify provider/resource prerequisites as repository-owned, provider-owned, or human trust boundaries;
- handle stateful resource provisioning/migration idempotently and without hidden local steps;
- avoid destructive DNS/email-routing/account changes without explicit authorization;
- preserve immutable validated-revision provenance through deployment;
- discover an endpoint and perform external health/readiness verification;
- recover from at least any real failures encountered rather than bypassing them;
- checkpoint durable state and resume from a fresh conversation without replaying history.

## Success criteria

Validation #2 passes only when all applicable criteria are evidenced:

1. repository-native implementation/adoption path exists;
2. required remote validation passes for an identified immutable revision;
3. a non-destructive Cloudflare validation deployment completes for the validated revision;
4. required stateful resources/migrations for the exercised application slice are managed remotely and audibly;
5. external observation confirms a healthy deployed frontend/backend and revision provenance where available;
6. secret values remain out of chat and repository plaintext;
7. destructive or account-level mail/DNS changes remain explicit human trust boundaries;
8. RPM is durable and a fresh conversation resumes correctly using locator-only bootstrap instructions;
9. every new failure mode is classified and promoted to the appropriate specification/Core/provider/reference/conformance/recovery layer when reusable.

## Stabilization intent

If Validation #2 passes cleanly, ZeroLocal will have two non-founding project passes: one greenfield-ish static delivery and one existing stateful Cloudflare application adoption. Before opening the Plugin gate, review whether the evidence is sufficiently diverse or whether a third clean-room project is warranted.
