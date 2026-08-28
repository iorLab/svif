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
            fail(f"{label} missing required product-architecture text: {needle}")


def main() -> None:
    required = [
        "ARCHITECTURE.md", "SVIF.yaml", "AGNIR.yaml",
        ".agnir/state.md", ".agnir/next-actions.md", ".agnir/decisions.md",
        "src/svif/runtime.py", "src/svif/continuity/agnir.py", "src/svif/execution/chatgpt.py",
        "tests/test_runtime.py", "tests/test_agnir_continuity.py", "tests/test_chatgpt_surface.py",
        "integrations/chatgpt/README.md",
        "spec/CORE.md", "spec/PROJECT_BINDING.md", "spec/CAPABILITY_ADAPTER.md", "spec/EVIDENCE.md",
        "profiles/SOFTWARE_DELIVERY.md",
        "schemas/project-binding.schema.json", "schemas/capability-adapter.schema.json", "schemas/evidence-record.schema.json",
        "conformance/check_contracts.py", "history/PREDECESSOR.md",
    ]
    for path in required:
        if not (ROOT / path).exists():
            fail(f"missing active Svif product artifact: {path}")

    for forbidden in (
        ".chatgpt", "ZEROLOCAL.yaml", "SPECIFICATION.md", "SVIF_ARCHITECTURE_DRAFT.md",
        "SVIF_CAPABILITY_ADAPTER_DRAFT.md", "profiles/SOFTWARE_DELIVERY_DRAFT.md",
        "conformance/check_v0_1.py", "conformance/v0.1.md",
    ):
        if (ROOT / forbidden).exists():
            fail(f"predecessor/execution-surface artifact remains active: {forbidden}")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    require_text(readme, [
        "Svif is a **Project orchestration product**.", "Continuity Provider", "Execution Surface",
        "Capability Provider", "mature distribution target remains an installable Plugin",
    ], "README.md")

    architecture = (ROOT / "ARCHITECTURE.md").read_text(encoding="utf-8")
    require_text(architecture, [
        "Svif is a **Project orchestration product**.", "**Orchestrator**", "**Continuity Provider**",
        "**Execution Surface**", "**Capability Provider**", "Orchestrator.begin()", "Orchestrator.complete()",
        "Untrusted model/result payloads MUST NOT self-grant protected authority.",
    ], "ARCHITECTURE.md")

    svif = (ROOT / "SVIF.yaml").read_text(encoding="utf-8")
    require_text(svif, [
        'manifest: "project-binding/0.2"', 'provider: "agnir"', 'runtime: "src/svif/runtime.py"',
        'agnir_repository_filesystem_adapter: "src/svif/continuity/agnir.py"',
        'chatgpt_execution_bridge: "src/svif/execution/chatgpt.py"',
        'chatgpt_surface: "tests/test_chatgpt_surface.py"',
    ], "SVIF.yaml")

    runtime = (ROOT / "src/svif/runtime.py").read_text(encoding="utf-8")
    require_text(runtime, [
        "class Orchestrator:", "class OperationSession:", "def begin(", "def complete(",
        "untrusted model/result payload cannot grant itself protected authority",
        "external actuation requires successful verification evidence for the exact subject",
    ], "src/svif/runtime.py")

    agnir = (ROOT / "src/svif/continuity/agnir.py").read_text(encoding="utf-8")
    require_text(agnir, [
        'provider_id = "agnir"', '"AGNIR_DISCOVERY_PROJECT_MISMATCH"',
        '"AGNIR_DISCOVERY_UNSUPPORTED_VERSION"', "def checkpoint(self, outcome: OperationOutcome)",
    ], "src/svif/continuity/agnir.py")

    chatgpt = (ROOT / "src/svif/execution/chatgpt.py").read_text(encoding="utf-8")
    require_text(chatgpt, [
        'surface_id = "chatgpt"', "def materialize(", "def parse_result(",
        "Authority grants are intentionally not accepted from this payload.",
    ], "src/svif/execution/chatgpt.py")

    state = (ROOT / ".agnir/state.md").read_text(encoding="utf-8")
    require_text(state, ["Project orchestration product", "Continuity Provider", "Execution Surface", "Capability / Effect Provider"], "Agnir state")

    print("PASS: Svif product repository integrity and product-architecture baseline")


if __name__ == "__main__":
    main()
