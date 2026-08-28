#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def require_text(text: str, needles: list[str], label: str) -> None:
    for needle in needles:
        if needle not in text:
            fail(f"{label} missing required product-architecture marker: {needle}")


def require_readme_diagrams(path: str, headings: tuple[str, str]) -> None:
    text = (ROOT / path).read_text(encoding="utf-8")
    if text.count("```mermaid") < 2:
        fail(f"{path} must contain at least two Mermaid diagrams")
    require_text(text, list(headings), path)


def require_readme_repository_tree(path: str, heading: str) -> None:
    text = (ROOT / path).read_text(encoding="utf-8")
    require_text(
        text,
        [
            heading,
            "svif/",
            "├── src/",
            "├── integrations/",
            "├── plugin/",
            "├── spec/",
            "├── .agnir/",
            "AGENTS.md",
            "plugin.json",
            "SKILL.md",
            "capabilities/",
            "cloudflare.py",
            "continuity/",
            "agnir.py",
            "execution/",
            "chatgpt.py",
            "REPOSITORY_TREE.md",
        ],
        path,
    )


def require_full_repository_tree() -> None:
    text = (ROOT / "REPOSITORY_TREE.md").read_text(encoding="utf-8")
    require_text(
        text,
        [
            "# Repository Tree",
            "src/",
            "└── svif/",
            "runtime.py",
            "integrations/",
            "adapter.json",
            "plugin/",
            "plugin.json",
            "skills/",
            "SKILL.md",
            "test_plugin_package.py",
            "spec/",
            "CAPABILITY_ADAPTER.md",
            "profiles/",
            "SOFTWARE_DELIVERY.md",
            "schemas/",
            "evidence-record.schema.json",
            "tests/",
            "test_founding_e2e.py",
            "conformance/",
            "evidence-chain-provenance-mismatch.json",
            "workspace-scm.json",
            "checks/",
            "check_repository.py",
            "history/",
            "CLOUDFLARE_REFERENCE.md",
            ".agnir/",
            "2026-08-28-founding-e2e.md",
            ".github/",
            "conformance.yml",
            "AGENTS.md",
            "AGNIR.yaml",
            "SVIF.yaml",
            "ARCHITECTURE.md",
            "README.zh-CN.md",
            "REPOSITORY_TREE.md",
            "VERSION",
        ],
        "REPOSITORY_TREE.md",
    )


def require_agnir_activation() -> None:
    agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    agnir = (ROOT / "AGNIR.yaml").read_text(encoding="utf-8")
    svif = (ROOT / "SVIF.yaml").read_text(encoding="utf-8")

    require_text(agents, ["Agnir Project Instructions", "README.md", "AGNIR.yaml"], "AGENTS.md")
    if ".agnir/state.md" in agents or ".agnir/next-actions.md" in agents:
        fail("AGENTS.md must remain a locator and must not duplicate durable Project memory")

    require_text(readme, [
        "## Agnir Project Instructions",
        "authorized Project Entry Point",
        "AGNIR.yaml",
        "Current State",
        "Next Actions",
        "Decisions",
        "Evidence",
        "Project root -> AGENTS.md -> README.md / Agnir Project Instructions -> AGNIR.yaml -> declared durable memory",
    ], "README.md Agnir activation")

    require_text(agnir, [
        'version: "0.1"',
        'discovery_profile: "repository-filesystem/0.1"',
        'state: ".agnir/state.md"',
        'next_actions: ".agnir/next-actions.md"',
        'decisions: ".agnir/decisions.md"',
        'evidence: ".agnir/evidence/"',
    ], "AGNIR.yaml")
    require_text(svif, [
        'compatibility: "0.1"',
        'profile: "repository-filesystem/0.1"',
        'activation: "AGENTS.md -> README.md / Agnir Project Instructions -> AGNIR.yaml"',
    ], "SVIF.yaml Agnir binding")

    for path in (".agnir/state.md", ".agnir/next-actions.md", ".agnir/decisions.md", ".agnir/evidence"):
        if not (ROOT / path).exists():
            fail(f"Agnir activation target is missing: {path}")


def main() -> None:
    required = [
        "ARCHITECTURE.md", "SVIF.yaml", "AGNIR.yaml", "AGENTS.md", "README.md", "README.zh-CN.md", "REPOSITORY_TREE.md",
        ".agnir/state.md", ".agnir/next-actions.md", ".agnir/decisions.md",
        "src/svif/runtime.py", "src/svif/continuity/agnir.py", "src/svif/execution/chatgpt.py",
        "src/svif/capabilities/cloudflare.py",
        "tests/test_runtime.py", "tests/test_agnir_continuity.py", "tests/test_chatgpt_surface.py",
        "tests/test_cloudflare_capability.py", "tests/test_founding_e2e.py", "tests/test_plugin_package.py",
        "integrations/chatgpt/README.md", "integrations/cloudflare/README.md", "integrations/cloudflare/adapter.json",
        "plugin/plugin.json", "plugin/README.md", "plugin/skills/svif/SKILL.md",
        "spec/CORE.md", "spec/PROJECT_BINDING.md", "spec/CAPABILITY_ADAPTER.md", "spec/EVIDENCE.md",
        "profiles/SOFTWARE_DELIVERY.md",
        "schemas/project-binding.schema.json", "schemas/capability-adapter.schema.json", "schemas/evidence-record.schema.json",
        "conformance/check_contracts.py", "history/PREDECESSOR.md", "history/CLOUDFLARE_REFERENCE.md",
    ]
    for path in required:
        if not (ROOT / path).exists():
            fail(f"missing active Svif product artifact: {path}")

    for forbidden in (
        ".chatgpt", "ZEROLOCAL.yaml", "SPECIFICATION.md", "SVIF_ARCHITECTURE_DRAFT.md",
        "SVIF_CAPABILITY_ADAPTER_DRAFT.md", "profiles/SOFTWARE_DELIVERY_DRAFT.md",
        "conformance/check_v0_1.py", "conformance/v0.1.md", "目录树.md",
    ):
        if (ROOT / forbidden).exists():
            fail(f"predecessor/execution-surface artifact remains active: {forbidden}")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    require_text(readme, [
        "Project orchestration product", "Continuity Provider", "Execution Surface",
        "Capability Provider", "iorLab/svif", "iorLab/agnir", "installable Plugin",
    ], "README.md")
    require_readme_diagrams("README.md", ("## Architecture Diagram", "## Runtime / Operation Flow"))
    require_readme_diagrams("README.zh-CN.md", ("## 架构图", "## 运行流程"))
    require_readme_repository_tree("README.md", "## Repository Structure")
    require_readme_repository_tree("README.zh-CN.md", "## 仓库结构")
    require_full_repository_tree()
    require_agnir_activation()

    architecture = (ROOT / "ARCHITECTURE.md").read_text(encoding="utf-8")
    require_text(architecture, [
        "Project orchestration product", "Orchestrator", "Continuity Provider",
        "Execution Surface", "Capability Provider", "Orchestrator.begin()", "Orchestrator.complete()",
        "Provider-specific Svif behavior does **not** get its own canonical project",
        "Agent Plugins 1.0.0", "plugin/plugin.json", "plugin/skills/svif/SKILL.md",
    ], "ARCHITECTURE.md")

    svif = (ROOT / "SVIF.yaml").read_text(encoding="utf-8")
    require_text(svif, [
        'manifest: "project-binding/0.2"', 'provider: "agnir"', 'runtime: "src/svif/runtime.py"',
        'agnir_repository_filesystem_adapter: "src/svif/continuity/agnir.py"',
        'chatgpt_execution_bridge: "src/svif/execution/chatgpt.py"',
        'cloudflare_workers_capability: "src/svif/capabilities/cloudflare.py"',
        'plugin_manifest: "plugin/plugin.json"', 'plugin_skill: "plugin/skills/svif/SKILL.md"',
        'plugin_package: "tests/test_plugin_package.py"',
        'cloudflare_capability: "tests/test_cloudflare_capability.py"',
        'founding_e2e: "tests/test_founding_e2e.py"',
    ], "SVIF.yaml")

    runtime = (ROOT / "src/svif/runtime.py").read_text(encoding="utf-8")
    require_text(runtime, [
        "class Orchestrator:", "class OperationSession:", "def begin(", "def complete(",
        "external actuation requires successful verification evidence for the exact subject",
    ], "src/svif/runtime.py")

    cloudflare = (ROOT / "src/svif/capabilities/cloudflare.py").read_text(encoding="utf-8")
    require_text(cloudflare, [
        'provider_id = "cloudflare.workers"', "class CloudflareWorkersTransport", "class CloudflareWorkersCapabilityProvider",
        "def actuate(", "def observe(",
    ], "src/svif/capabilities/cloudflare.py")

    plugin = (ROOT / "plugin/skills/svif/SKILL.md").read_text(encoding="utf-8")
    require_text(plugin, [
        "name: svif", "AGNIR.yaml", "SVIF.yaml",
        "DISCOVER -> PLAN -> CHANGE -> VERIFY -> DELIVER -> OBSERVE -> CHECKPOINT",
        "Untrusted model/result payloads must never self-grant protected authority.",
    ], "Svif Plugin skill")

    founding = (ROOT / "tests/test_founding_e2e.py").read_text(encoding="utf-8")
    require_text(founding, [
        "AgnirFilesystemContinuityProvider", "ChatGPTExecutionSurface",
        "CloudflareWorkersCapabilityProvider", "orchestrator.begin", "orchestrator.complete",
        "authority_grants=frozenset({AUTHORITY})",
    ], "tests/test_founding_e2e.py")

    state = (ROOT / ".agnir/state.md").read_text(encoding="utf-8")
    require_text(state, [
        "Project orchestration product", "Continuity Provider", "Execution Surface", "Capability Provider",
        "former `iorLab/svif-cloudflare-reference` project is retired",
        "README.zh-CN.md", "Plugin MVP",
    ], "Agnir state")

    print("PASS: Svif product repository integrity, Agnir activation, Plugin packaging, and single-repository architecture baseline")


if __name__ == "__main__":
    main()
