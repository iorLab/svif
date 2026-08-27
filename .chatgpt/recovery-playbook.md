# ZeroLocal Stabilization Recovery Playbook

This playbook records recovery rules demonstrated by clean-room validation. It supplements the v0.1 failure taxonomy; it does not replace `SPECIFICATION.md` or provider skills.

## RPM/bootstrap discovery

**Observed in:** Validation Project #1 (`mattamior/agent-skills`).

**Symptom:** RPM was persisted successfully on a non-default working ref, but a fresh ChatGPT conversation could not discover the canonical repository/ref and behaved as if project history were absent.

**Root cause:** Persistence existed without a durable locator from the conversational environment into repository RPM.

**Recovery rule:**

1. Treat the failure as `RPM/bootstrap discovery`, not as missing project history.
2. Establish locator-only durable instructions identifying ZeroLocal activation, canonical repository, RPM manifest path, and authoritative RPM ref when non-default.
3. Load RPM from that ref before acting.
4. Never repair this class by copying mutable project history into Project Instructions or chat.
5. Re-run a fresh-conversation resume test before claiming resumability.

**Durable repair:** `ZL-RPM-006` through `ZL-RPM-009`, Core Initialize/Checkpoint changes, and conformance coverage merged through ZeroLocal PR #1.

## Dependency/toolchain mismatch

**Observed in:** Validation Project #1 first production delivery.

**Symptom:** Repository build/validation succeeded, but deployment failed when `cloudflare/wrangler-action@v3` installed Wrangler 3.90.0, which rejected an assets-only Workers configuration with `Missing entry-point`.

**Classification:** `dependency/toolchain`.

**Recovery rule:**

1. Attribute the failure to the exact deployment revision and inspect the remote job step that selected/installed the toolchain.
2. Do not rewrite application code to accommodate an accidentally stale provider CLI when the repository's declared configuration targets a supported newer toolchain.
3. Pin or explicitly select the compatible tool/action version in repository automation.
4. Create a new immutable revision, rerun remote validation, and deploy only the validated revision.
5. Preserve exact-SHA provenance through the repair loop.

**Observed repair:** PR #2 in `mattamior/agent-skills` upgraded `cloudflare/wrangler-action` to v4 and explicitly selected Wrangler major version 4.

## Protected-secret trust boundary

**Observed in:** Validation Project #1 before first production deployment.

**Symptom:** Repository implementation and validation were complete, but production delivery required `CLOUDFLARE_API_TOKEN` and `CLOUDFLARE_ACCOUNT_ID` in the protected GitHub `production` environment.

**Classification:** human trust boundary, not repository failure.

**Recovery rule:**

1. Name the required protected values and the protected store/account location.
2. State the minimum required scope.
3. Never request, echo, or persist secret values in chat/RPM/repository plaintext.
4. Keep pull-request validation untrusted and unable to access production credentials.
5. Resume delivery only after the human confirms the protected-store action is complete.

## Production propagation/readiness

**Observed in:** Validation Project #1 final production observation.

**Symptom:** The final `/health.json` observation encountered one transient propagation 404 before succeeding.

**Classification:** `production health/readiness` when it persists; transient propagation alone is not a failed release.

**Recovery rule:**

1. Use bounded external retries after deployment rather than treating deploy exit status as success.
2. Require the health/readiness response to identify the exact deployed revision when the application exposes provenance.
3. Fail the deployment if the bounded observation window expires or revision provenance does not match.
4. Record the observed endpoint and revision only after external verification passes.

## Provider resource rename / orphan awareness

**Observed in:** Validation Project #1 Worker rename from `mattamior-agent-skills` to `agent-skills`.

**Symptom:** The desired concise endpoint was created and observed, while the old Worker remained provisioned.

**Classification:** provisioning/resource-lifecycle follow-up; not a delivery failure when the new target is healthy and the old resource is harmless.

**Recovery rule:**

1. Treat provider resource renames as possible create-new-resource operations unless the provider guarantees in-place rename semantics.
2. Surface any retained legacy resource explicitly instead of silently assuming deletion.
3. Do not delete legacy production resources automatically unless repository policy or explicit human intent authorizes destructive cleanup.
4. Keep cleanup as a separate, auditable action after the replacement endpoint is observed.

## Stabilization use

Add a recovery rule only after a real run demonstrates the failure mode or a concrete regression risk. If a repeated failure reveals a protocol or provider-contract defect, promote the invariant into `SPECIFICATION.md`, Core, the provider skill, or conformance checks rather than leaving it only in this playbook.
