# Next Steps

## Phase 4 — Skill Stabilization (current, mandatory before Plugin)

1. Select at least **two new non-founding real projects**, preferably **2-3**, that do not depend on `awesome-fame-slider` or this founding conversation.
2. Start each validation from a fresh context and repository state. The operator should have only the installed ZeroLocal Skills plus repository/RPM evidence available.
3. For each project, exercise the complete relevant path:
   - Initialize / BOOTSTRAP
   - Plan
   - Implement / IMPLEMENT
   - Verify / VERIFY
   - Deliver / PROVISION + DEPLOY when applicable
   - Observe / OBSERVE
   - Repair/Iterate on at least one real failure when encountered
   - Checkpoint / CHECKPOINT
4. Treat any dependency on hidden chat history, founding-project knowledge, unstated provider assumptions, or human local tooling as a ZeroLocal defect.
5. Fix each defect in the correct durable layer:
   - protocol invariant or lifecycle ambiguity -> `SPECIFICATION.md`
   - provider-neutral execution procedure -> `skills/zerolocal-core/SKILL.md`
   - Cloudflare-specific behavior -> `skills/cloudflare-provider/SKILL.md`
   - executable provider behavior -> `iorLab/zerolocal-cloudflare-starter`
   - durable resume/bootstrap gap -> RPM contract/files
   - regression risk -> conformance checks
6. Build a reusable failure taxonomy/recovery playbook from observed failures, covering at least CI, dependencies/toolchain, repository permissions, protected secrets, provider authorization, provisioning, migrations/state transitions, routing/DNS, and production health/readiness.
7. Tighten `ZEROLOCAL.yaml`/Provider Adapter fields only when fresh-project use demonstrates a concrete missing contract.
8. Repeat clean-room runs until a fresh conversation can bootstrap, develop, validate, deliver, diagnose, repair, observe, and checkpoint without founding context or mandatory local project tooling.

## Live Cloudflare reference evidence

9. Static repository conformance and CI are part of Skill v0.1 completion. Live provider deploy/observation remains an explicit trust boundary until `CLOUDFLARE_API_TOKEN` and `CLOUDFLARE_ACCOUNT_ID` exist in the reference repository's protected GitHub Actions secret store.
10. When those protected prerequisites are available, confirm one end-to-end reference deployment: successful CI SHA -> same deployed SHA -> discovered Cloudflare target -> passing `/health` observation. Never move secret values into chat or repository plaintext.

## Phase 5 — Plugin (still gated)

11. Do not begin Plugin packaging until the multi-project clean-room gate passes and recurring failure modes have reusable recovery strategies.
12. Before graduation, require at minimum two new project passes (preferably 2-3), stable Core/provider interfaces across a minor cycle, and no known hidden-context dependency.
13. Only after that gate should Plugin work package the validated Skills, GitHub integration, templates, onboarding, provider discovery, versioning, and natural-language activation.
14. Add a second provider implementation only after the Cloudflare path is stable enough to test provider neutrality rather than merely speculate about it.
