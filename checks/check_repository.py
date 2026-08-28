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
        "ARCHITECTURE.md",
        "SVIF.yaml",
        "AGNIR.yaml",
        ".agnir/state.md",
        ".agnir/next-actions.md",
        ".agnir/decisions.md",
        "src/svif/__init__.py",
        "src/svif/runtime.py",
        "tests/test_runtime.py",
        "spec/CORE.md",
        "spec/PROJECT_BINDING.md",
        "spec/CAPABILITY_ADAPTER.md",
        "spec/EVIDENCE.md",
        "profiles/SOFTWARE_DELIVERY.md",
        "schemas/project-binding.schema.json",
        "schemas/capability-adapter.schema.json",
        "schemas/evidence-record.schema.json",
        "conformance/check_contracts.py",
        "history/PREDECESSOR.md",
    ]
    for path in required:
        if not (ROOT / path).exists():
            fail(f"missing active Svif product artifact: {path}")

    for forbidden in (
        ".chatgpt",
        "ZEROLOCAL.yaml",
        "SPECIFICATION.md",
        "SVIF_ARCHITECTURE_DRAFT.md",
        "SVIF_CAPABILITY_ADAPTER_DRAFT.md",
        "profiles/SOFTWARE_DELIVERY_DRAFT.md",
        "conformance/check_v0_1.py",
        "conformance/v0.1.md",
    ):
        if (ROOT / forbidden).exists():
            fail(f"predecessor/execution-surface artifact remains active: {forbidden}")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    require_text(
        readme,
        [
            "Svif is a **Project orchestration product**.",
            "Continuity Provider",
            "Execution Surface",
            "Capability Provider",
            "mature distribution target remains an installable Plugin",
        ],
        "README.md",
    )

    architecture = (ROOT / "ARCHITECTURE.md").read_text(encoding="utf-8")
    require_text(
        architecture,
        [
            "Svif is a **Project orchestration product**.",
            "**Orchestrator**",
            "**Continuity Provider**",
            "**Execution Surface**",
            "**Capability Provider**",
            "Agnir, ChatGPT, and Cloudflare are the founding/current bindings.",
            "project-binding/0.2",
            "Repository integrity is not evidence that an arbitrary Project is Svif-conformant.",
        ],
        "ARCHITECTURE.md",
    )

    svif = (ROOT / "SVIF.yaml").read_text(encoding="utf-8")
    require_text(
        svif,
        [
            'version: "0.2"',
            'manifest: "project-binding/0.2"',
            'identity: "urn:svif:project:svif-core"',
            'provider: "agnir"',
            'compatibility: "0.1"',
            'discovery: "AGNIR.yaml"',
            'runtime: "src/svif/runtime.py"',
            'repository_integrity: "checks/check_repository.py"',
            'portable_contracts: "conformance/check_contracts.py"',
            'runtime_kernel: "tests/test_runtime.py"',
        ],
        "SVIF.yaml",
    )

    core = (ROOT / "spec/CORE.md").read_text(encoding="utf-8")
    require_text(
        core,
        [
            "Svif Core defines the portable orchestration lifecycle and invariants used by the **Svif Project orchestration product**.",
            "Continuity Provider",
            "Execution Surface",
            "Capability Provider",
            "DISCOVER -> PLAN -> CHANGE -> VERIFY -> DELIVER -> OBSERVE -> CHECKPOINT",
            "The mature product target remains a Plugin.",
        ],
        "spec/CORE.md",
    )

    runtime = (ROOT / "src/svif/runtime.py").read_text(encoding="utf-8")
    require_text(
        runtime,
        [
            "class Orchestrator:",
            "class ContinuityProvider(Protocol):",
            "class ExecutionSurface(Protocol):",
            "class CapabilityProvider(Protocol):",
            "external actuation requires successful verification evidence for the exact subject",
            "observation does not match the successfully delivered subject/target",
        ],
        "src/svif/runtime.py",
    )

    binding = (ROOT / "spec/PROJECT_BINDING.md").read_text(encoding="utf-8")
    require_text(
        binding,
        [
            "**Identifier:** `project-binding/0.2`",
            "one Continuity Provider binding",
            "zero or more Execution Surfaces",
            "zero or more Capability Providers",
            "MUST NOT require plaintext protected secret values",
        ],
        "spec/PROJECT_BINDING.md",
    )

    state = (ROOT / ".agnir/state.md").read_text(encoding="utf-8")
    require_text(
        state,
        [
            "Project orchestration product",
            "Continuity Provider",
            "Execution Surface",
            "Capability / Effect Provider",
        ],
        "Agnir state",
    )

    print("PASS: Svif product repository integrity and product-architecture baseline")


if __name__ == "__main__":
    main()
