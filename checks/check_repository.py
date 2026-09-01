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


def require_readme_entry_guide(
    path: str,
    *,
    start_heading: str,
    surface_heading: str,
    architecture_heading: str,
    install_prompt: str,
    upgrade_prompt: str,
    normal_use_marker: str,
    surface_markers: tuple[str, ...],
) -> None:
    text = (ROOT / path).read_text(encoding="utf-8")
    require_text(
        text,
        [
            start_heading,
            install_prompt,
            upgrade_prompt,
            normal_use_marker,
            "## Agnir Project Instructions",
            surface_heading,
            architecture_heading,
        ],
        f"{path} entry guide",
    )
    start_position = text.find(start_heading)
    agent_position = text.find("## Agnir Project Instructions")
    surface_position = text.find(surface_heading)
    architecture_position = text.find(architecture_heading)
    if not (0 <= start_position < agent_position < surface_position < architecture_position):
        fail(
            f"{path} must present Start Here, then Agnir Project Instructions, "
            "then the installed Project surface, before architecture material"
        )
    surface_text = text[surface_position:architecture_position]
    for marker in surface_markers:
        if marker not in surface_text:
            fail(f"{path} first-use Project surface missing required marker: {marker}")


def require_readme_diagrams(
    path: str,
    headings: tuple[str, str],
    *,
    architecture_markers: tuple[str, ...],
    runtime_forbidden_markers: tuple[str, ...],
) -> None:
    text = (ROOT / path).read_text(encoding="utf-8")
    if text.count("```mermaid") < 2:
        fail(f"{path} must contain at least two Mermaid diagrams")
    require_text(text, list(headings), path)
    architecture_start = text.find(headings[0])
    runtime_start = text.find(headings[1])
    if not (0 <= architecture_start < runtime_start):
        fail(f"{path} must place architecture before runtime flow")
    architecture_text = text[architecture_start:runtime_start]
    for marker in architecture_markers:
        if marker not in architecture_text:
            fail(f"{path} Architecture Diagram missing first-use marker: {marker}")
    runtime_text = text[runtime_start:]
    for marker in runtime_forbidden_markers:
        if marker in runtime_text:
            fail(f"{path} Runtime / Operation Flow must not include installation mutation marker: {marker}")


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
            "test_plugin_component_discovery.py",
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
        "tests/test_plugin_component_discovery.py",
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
    require_readme_entry_guide(
        "README.md",
        start_heading="## Start Here",
        surface_heading="## What Svif Adds to a Project",
        architecture_heading="## Architecture Diagram",
        install_prompt="Install and enable Svif for this Project: https://github.com/iorLab/svif",
        upgrade_prompt="Upgrade the Agnir used by this Project to the latest stable release: https://github.com/iorLab/agnir",
        normal_use_marker="No recurring Svif installation prompt is required.",
        surface_markers=(
            "[EDIT: add entry only]",
            "[ADD] founding Agnir discovery anchor",
            "[ADD] Project-owned durable continuity",
            "[ADD] Svif Project Binding",
            "intentionally bound to another Continuity Provider",
        ),
    )
    require_readme_entry_guide(
        "README.zh-CN.md",
        start_heading="## 从这里开始",
        surface_heading="## Svif 会给 Project 增加什么",
        architecture_heading="## 架构图",
        install_prompt="为这个 Project 安装并启用 Svif：https://github.com/iorLab/svif",
        upgrade_prompt="把这个 Project 使用的 Agnir 升级到最新稳定版：https://github.com/iorLab/agnir",
        normal_use_marker="不需要在每次对话里重复 Svif 安装提示。",
        surface_markers=(
            "[编辑：仅添加入口]",
            "[新增] founding Agnir discovery anchor",
            "[新增] Project 自己拥有的 durable continuity",
            "[新增] Svif Project Binding",
            "明确绑定其他 Continuity Provider",
        ),
    )
    require_readme_diagrams(
        "README.md",
        ("## Architecture Diagram", "## Runtime / Operation Flow"),
        architecture_markers=(
            "non-destructive first-use setup",
            "EDIT: add activation locator only",
            "EDIT: add Agnir instructions only",
            "ADD: founding continuity",
            "ADD: Project binding",
            "Svif Orchestrator",
            "Continuity Provider",
            "Execution integration",
            "Capability Providers",
        ),
        runtime_forbidden_markers=("EDIT: add", "ADD: founding", "ADD: Project binding"),
    )
    require_readme_diagrams(
        "README.zh-CN.md",
        ("## 架构图", "## 运行流程"),
        architecture_markers=(
            "非破坏性 first-use setup",
            "编辑：仅添加 activation locator",
            "编辑：仅添加 Agnir instructions",
            "新增：founding continuity",
            "新增：Project binding",
            "Svif 编排器",
            "项目连续性提供者",
            "执行环境适配层",
            "能力提供层",
        ),
        runtime_forbidden_markers=("编辑：仅添加", "新增：founding", "新增：Project binding"),
    )
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
        'plugin_component_discovery: "tests/test_plugin_component_discovery.py"',
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
