# Next Steps

## Phase 4 — Skill Stabilization (current, mandatory before Plugin)

### Validation Project #1 — `mattamior/agent-skills`

1. Create a fresh ChatGPT Project dedicated to Validation #1 with **Project-only memory**.
2. Leave **Project Instructions blank initially**. Do not pre-seed RPM paths, lifecycle instructions, Cloudflare workflow details, or other ZeroLocal implementation knowledge. Whether durable bootstrap/Project Instructions are needed should be discovered and proposed by ZeroLocal itself.
3. Ensure GitHub access is available. The user's current environment is a personal Plus plan, so this validation must not depend on ChatGPT Personal Skill upload/install availability.
4. Start a fresh conversation with only the minimum bootstrap and business intent: use the ZeroLocal Skills from `iorLab/zerolocal` to develop `mattamior/agent-skills`; build a showcase website for the repository's Agent Skills and deploy it to Cloudflare; then let ZeroLocal proceed normally.
5. Do not coach the clean-room agent on RPM structure, Initialize/BOOTSTRAP mechanics, CI design, deployment workflow, provider configuration, or checkpoint implementation. Any need for founding-context guidance is evidence of a ZeroLocal defect.
6. Let the run exercise the complete relevant path:
   - Initialize / BOOTSTRAP
   - Plan
   - Implement / IMPLEMENT
   - Verify / VERIFY
   - Deliver / PROVISION + DEPLOY
   - Observe / OBSERVE
   - Repair/Iterate on real failures
   - Checkpoint / CHECKPOINT
7. When the clean-room agent first requests human participation, pause and classify the request before supplying help. Legitimate trust-boundary requests include account authorization, protected secret-store configuration, billing/ownership decisions, and explicit production-risk approval. Never place secret values in chat or repository plaintext.
8. Record every observed failure or hidden assumption and fix it in the correct durable layer:
   - protocol invariant or lifecycle ambiguity -> `SPECIFICATION.md`
   - provider-neutral execution procedure -> `skills/zerolocal-core/SKILL.md`
   - Cloudflare-specific behavior -> `skills/cloudflare-provider/SKILL.md`
   - executable provider behavior -> `iorLab/zerolocal-cloudflare-starter`
   - durable resume/bootstrap gap -> RPM contract/files
   - regression risk -> conformance checks
9. After the first run checkpoints, open another fresh conversation in the validation project and test whether work can resume from repository/RPM evidence without manually restating project history. This is a required recovery/resume test, not an optional convenience.
10. Validation #1 success requires more than a visible website: repository-driven Skill content, passing verification, Cloudflare production delivery, observable endpoint verification, durable RPM state, and fresh-conversation resumability.

### Remaining stabilization gate

11. After Validation #1, select at least one additional non-founding real project; total requirement remains at least **two**, preferably **2-3**.
12. Build a reusable failure taxonomy/recovery playbook from observed runs, covering at least CI, dependencies/toolchain, repository permissions, protected secrets, provider authorization, provisioning, migrations/state transitions, routing/DNS, and production health/readiness.
13. Tighten `ZEROLOCAL.yaml`/Provider Adapter fields only when fresh-project use demonstrates a concrete missing contract.
14. Repeat clean-room runs until a fresh conversation can bootstrap, develop, validate, deliver, diagnose, repair, observe, and checkpoint without founding context or mandatory local project tooling.

## Live Cloudflare reference evidence

15. Static repository conformance and CI are part of Skill v0.1 completion. Live provider deploy/observation remains an explicit trust boundary until `CLOUDFLARE_API_TOKEN` and `CLOUDFLARE_ACCOUNT_ID` exist in the reference repository's protected GitHub Actions secret store.
16. When those protected prerequisites are available, confirm one end-to-end reference deployment: successful CI SHA -> same deployed SHA -> discovered Cloudflare target -> passing `/health` observation. Never move secret values into chat or repository plaintext.

## Phase 5 — Plugin (still gated)

17. Do not begin Plugin packaging until the multi-project clean-room gate passes and recurring failure modes have reusable recovery strategies.
18. Before graduation, require at minimum two new project passes (preferably 2-3), stable Core/provider interfaces across a minor cycle, and no known hidden-context dependency.
19. Only after that gate should Plugin work package the validated Skills, GitHub integration, templates, onboarding, provider discovery, versioning, and natural-language activation.
20. Add a second provider implementation only after the Cloudflare path is stable enough to test provider neutrality rather than merely speculate about it.
