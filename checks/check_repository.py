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
            "├── spec/",
            "├── .agnir/",
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
            "AGNIR.yaml",
            "SVIF.yaml",
            "ARCHITECTURE.md",
            "README.zh-CN.md",
            "REPOSITORY_TREE.md",
            "VERSION",
        ],
        "REPOSITORY_TREE.md",
    )


def main() -> None:
    required = [
        "ARCHITECTURE.md", "SVIF.yaml", "AGNIR.yaml", "README.md", "README.zh-CN.md", "REPOSITORY_TREE.md",
        ".agnir/state.md", ".agnir/next-actions.md", ".agnir/decisions.md",
        "src/svif/runtime.py", "src/svif/continuity/agnir.py", "src/svif/execution/chatgpt.py",
        "src/svif/capabilities/cloudflare.py",
        "tests/test_runtime.py", "tests/test_agnir_continuity.py", "tests/test_chatgpt_surface.py",
        "tests/test_cloudflare_capability.py", "tests/test_founding_e2e.py",
        "integrations/chatgpt/README.md", "integrations/cloudflare/README.md", "integrations/cloudflare/adapter.json",
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
        "Capability Provider", "iorLab/svif", "iorLab/agnir",
    ], "README.md")
    require_readme_diagrams("README.md", ("## Architecture Diagram", "## Runtime / Operation Flow"))
    require_readme_diagrams("README.zh-CN.md", ("## 架构图", "## 运行流程"))
    require_readme_repository_tree("README.md", "## Repository Structure")
    require_readme_repository_tree("README.zh-CN.md", "## 仓库结构")
    require_full_repository_tree()

    architecture = (ROOT / "ARCHITECTURE.md").read_text(encoding="utf-8")
    require_text(architecture, [
        "Project orchestration product", "Orchestrator", "Continuity Provider",
        "Execution Surface", "Capability Provider", "Orchestrator.begin()", "Orchestrator.complete()",
        "Provider-specific Svif behavior does **not** get its own canonical project",
    ], "ARCHITECTURE.md")

    svif = (ROOT / "SVIF.yaml").read_text(encoding="utf-8")
    require_text(svif, [
        'manifest: "project-binding/0.2"', 'provider: "agnir"', 'runtime: "src/svif/runtime.py"',
        'agnir_repository_filesystem_adapter: "src/svif/continuity/agnir.py"',
        'chatgpt_execution_bridge: "src/svif/execution/chatgpt.py"',
        'cloudflare_workers_capability: "src/svif/capabilities/cloudflare.py"',
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
        "README.zh-CN.md",
    ], "Agnir state")

    print("PASS: Svif product repository integrity and single-repository architecture baseline")


if __name__ == "__main__":
    main()
