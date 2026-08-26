from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

spec = (ROOT / "SPECIFICATION.md").read_text(encoding="utf-8")
core = (ROOT / "skills/zerolocal-core/SKILL.md").read_text(encoding="utf-8")
cloudflare = (ROOT / "skills/cloudflare-provider/SKILL.md").read_text(encoding="utf-8")
memory = (ROOT / ".chatgpt/project-memory.yaml").read_text(encoding="utf-8")

checks = {
    "spec current delivery form": "**Current delivery form:** Skills" in spec,
    "plugin stabilization gate": "Plugin work remains gated" in spec,
    "lifecycle states": all(x in spec for x in [
        "BOOTSTRAP", "IMPLEMENT", "VERIFY", "PROVISION", "DEPLOY",
        "OBSERVE", "REPAIR/ITERATE", "CHECKPOINT"
    ]),
    "contract families": all(x in spec for x in [
        "Lifecycle Contract", "Repository Contract", "RPM Contract", "CI Contract",
        "Deployment Contract", "Trust Boundary Contract", "Provider Adapter Contract"
    ]),
    "provider hooks in spec": all(f"`{x}`" in spec for x in [
        "detect", "capabilities", "credentials", "scaffold", "validate", "provision",
        "migrate", "deploy", "endpoint", "verify", "recover"
    ]),
    "core procedures": all(f"### {x}" in core for x in [
        "Initialize", "Plan", "Implement", "Verify", "Deliver", "Observe", "Checkpoint"
    ]),
    "core secret boundary": "Never request or reproduce secret values in chat" in core,
    "core exact revision invariant": "deploy the exact immutable revision that passed the gate" in core,
    "core provider delegation": "provider skill" in core.lower() and "provider-specific behavior belongs" in core.lower(),
    "cloudflare provider hooks": all(f"### {x}" in cloudflare for x in [
        "detect", "capabilities", "credentials", "scaffold", "validate", "provision",
        "migrate", "deploy", "endpoint", "verify", "recover"
    ]),
    "cloudflare protected credentials": all(x in cloudflare for x in [
        "CLOUDFLARE_API_TOKEN", "CLOUDFLARE_ACCOUNT_ID", "Never ask the user to paste"
    ]),
    "cloudflare exact tested sha": "workflow_run.head_sha" in cloudflare,
    "rpm delivery form skills": "current_delivery_form: skills" in memory,
}

failed = [name for name, ok in checks.items() if not ok]
for name, ok in checks.items():
    print(f"{'PASS' if ok else 'FAIL'}  {name}")

if failed:
    raise SystemExit(f"ZeroLocal v0.1 conformance failed: {', '.join(failed)}")

print(f"PASS  {len(checks)} structural checks")
