# Next Steps

## Phase 4 — Skill Stabilization (current, mandatory before Plugin)

### Validation Project #1 — `mattamior/agent-skills` — PASS

1. Preserve the completed evidence in `.chatgpt/validation-1.md` and reusable recovery rules in `.chatgpt/recovery-playbook.md`.
2. Treat the following as demonstrated recovery classes from Validation #1:
   - `RPM/bootstrap discovery`;
   - `dependency/toolchain`;
   - protected-secret trust boundary;
   - bounded production propagation/readiness observation;
   - provider resource rename/orphan awareness.
3. Non-blocking repository hygiene: the final target RPM is still authoritative on `feat/skill-gallery-cloudflare`. When convenient, consolidate the final RPM checkpoint onto target `main`, update the ChatGPT Project locator so no non-default `RPM ref` is needed, verify one fresh-context resume, then delete the feature branch only if desired. Do not treat this hygiene item as a Validation #1 pass blocker.

### Validation Project #2 — `mattamior/cloud-mail`

4. Create a fresh ChatGPT Project dedicated to Validation #2 with **Project-only memory**.
5. Leave **Project Instructions blank initially**. The repaired ZeroLocal Core must itself establish or request locator-only bootstrap instructions after RPM is created/adopted. Do not pre-seed repository/RPM paths, Cloudflare resource topology, workflow repairs, secret names, or provider internals.
6. Ensure GitHub access is available. Validation must remain compatible with the user's current personal Plus environment and must not depend on Personal Skill upload/install availability.
7. Start a fresh conversation with only the minimum source and business intent, equivalent to:

   `Use the ZeroLocal Skills from iorLab/zerolocal to develop mattamior/cloud-mail. Bring the existing Cloud Mail app under ZeroLocal, create a non-destructive Cloudflare validation deployment with a working observable frontend/backend and required stateful resources, and let ZeroLocal proceed normally.`

8. Do not coach the clean-room agent on the repository's existing Cloudflare workflow, D1/KV/R2 provisioning, migrations, exact deployment design, secret names, or repair steps. Any hidden-context requirement is evidence of a ZeroLocal defect.
9. Require ZeroLocal to distinguish clearly between:
   - repository-owned code/config/automation work;
   - provider resource provisioning or migration work;
   - protected credentials/account state;
   - destructive or domain/mail-routing changes requiring explicit human authorization.
10. Do **not** authorize real DNS/email-routing changes, paid/external mail sending, or destructive provider cleanup merely to make the validation pass. A non-destructive validation deployment must exercise a meaningful frontend/backend/stateful slice while keeping those operations at a named trust boundary unless explicitly approved.
11. Let the run exercise the complete applicable lifecycle:
   - Initialize / BOOTSTRAP, including durable bootstrap establishment;
   - Plan;
   - Implement / IMPLEMENT;
   - Verify / VERIFY;
   - Provision/Migrate as actually required by repository evidence;
   - Deliver / DEPLOY;
   - Observe / OBSERVE;
   - Repair/Iterate on real failures;
   - Checkpoint / CHECKPOINT.
12. After the first meaningful checkpoint, open another fresh conversation in the Validation #2 ChatGPT Project and test resume without manually restating project history. This is again a required recovery test.
13. Record every new observed failure or hidden assumption in `.chatgpt/validation-2.md`, and promote reusable repairs to the correct durable layer:
   - protocol invariant/lifecycle ambiguity -> `SPECIFICATION.md`;
   - provider-neutral procedure -> `skills/zerolocal-core/SKILL.md`;
   - Cloudflare-specific behavior -> `skills/cloudflare-provider/SKILL.md`;
   - executable provider behavior -> `iorLab/zerolocal-cloudflare-starter`;
   - resumability/state issue -> RPM contract/files;
   - reusable recovery -> `.chatgpt/recovery-playbook.md`;
   - regression risk -> conformance checks.
14. Validation #2 passes only with remote verification for an immutable revision, a non-destructive stateful Cloudflare deployment, auditable resource/migration handling for the exercised slice, external frontend/backend health observation, preserved secret/trust boundaries, durable RPM, and fresh-conversation resumability.

### Stabilization gate after Validation #2

15. Compare Validation #1 and #2 evidence. Minimum numerical gate is two non-founding project passes, but do not open Plugin work merely because the count reaches two.
16. Require the two runs together to demonstrate sufficiently diverse repository shapes and recovery behavior, with no known hidden-context dependency and reusable treatment of recurring failures.
17. If Validation #2 exposes unstable provider hooks/contracts, or if both passes leave important stateful/provider behavior untested, select a third clean-room project before Plugin graduation.
18. Tighten `ZEROLOCAL.yaml`/Provider Adapter fields only when a concrete fresh-project failure demonstrates a missing contract; avoid speculative schema expansion.

## Live Cloudflare reference evidence

19. Static repository conformance and CI remain part of Skill v0.1 completion. Live provider deploy/observation for `iorLab/zerolocal-cloudflare-starter` remains a separate explicit trust boundary until its required protected Cloudflare authorization exists.
20. When those protected prerequisites are available, confirm one reference deployment with successful CI SHA -> same deployed SHA -> discovered target -> passing `/health` observation. Never move secret values into chat or repository plaintext.

## Phase 5 — Plugin (still gated)

21. Do not begin Plugin packaging until the multi-project clean-room gate passes and recurring failure modes have durable recovery strategies.
22. Before graduation, require at minimum two new project passes (preferably 2-3), stable Core/provider interfaces across a minor cycle, and no known hidden-context dependency.
23. Only after that gate should Plugin work package the validated Skills, GitHub integration, templates, onboarding, provider discovery, versioning, and natural-language activation.
24. Add a second provider implementation only after the Cloudflare path is stable enough to test provider neutrality rather than merely speculate about it.
