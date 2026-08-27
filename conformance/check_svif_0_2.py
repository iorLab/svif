#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def scalar(text: str, section: str, key: str) -> str | None:
    lines = text.splitlines()
    in_section = False
    for line in lines:
        if re.match(rf"^{re.escape(section)}:\s*$", line):
            in_section = True
            continue
        if in_section and line and not line.startswith((" ", "\t", "#")):
            break
        if in_section:
            m = re.match(rf"^\s{{2}}{re.escape(key)}:\s*(.+?)\s*$", line)
            if m:
                return m.group(1).strip().strip("\"'")
    return None


def load_json(path: str) -> dict:
    try:
        return json.loads((ROOT / path).read_text(encoding="utf-8"))
    except Exception as exc:
        fail(f"invalid JSON in {path}: {exc}")


def main() -> None:
    required = [
        "SVIF.yaml",
        "AGNIR.yaml",
        ".agnir/state.md",
        ".agnir/next-actions.md",
        ".agnir/decisions.md",
        "spec/CORE.md",
        "spec/CAPABILITY_ADAPTER.md",
        "spec/EVIDENCE.md",
        "profiles/SOFTWARE_DELIVERY.md",
        "schemas/capability-adapter.schema.json",
        "schemas/evidence-record.schema.json",
        "history/PREDECESSOR.md",
        ".chatgpt/project-memory.yaml",
    ]
    for path in required:
        if not (ROOT / path).exists():
            fail(f"missing active Svif artifact: {path}")

    svif_text = (ROOT / "SVIF.yaml").read_text(encoding="utf-8")
    agnir_text = (ROOT / "AGNIR.yaml").read_text(encoding="utf-8")
    if scalar(svif_text, "svif", "version") != "0.2":
        fail("SVIF.yaml does not declare Svif 0.2")
    if scalar(svif_text, "continuity", "protocol") != "agnir":
        fail("SVIF.yaml continuity protocol is not Agnir")
    if scalar(svif_text, "continuity", "compatibility") != "0.1":
        fail("SVIF.yaml does not target Agnir 0.1")
    if scalar(agnir_text, "agnir", "version") != "0.1":
        fail("AGNIR.yaml does not declare Agnir 0.1")

    core = (ROOT / "spec/CORE.md").read_text(encoding="utf-8")
    lifecycle = "DISCOVER -> PLAN -> CHANGE -> VERIFY -> DELIVER -> OBSERVE -> CHECKPOINT"
    if lifecycle not in core:
        fail("Core lifecycle is missing or changed")
    if "Planning semantics are mandatory before material mutation" not in core:
        fail("PLAN semantic rule is missing")

    adapter_schema = load_json("schemas/capability-adapter.schema.json")
    evidence_schema = load_json("schemas/evidence-record.schema.json")
    adapter_version = adapter_schema["properties"]["svif_adapter"]["properties"]["version"]["const"]
    evidence_version = evidence_schema["properties"]["svif"]["properties"]["version"]["const"]
    if adapter_version != "0.2" or evidence_version != "0.2":
        fail("schema version constants diverge from Svif 0.2")

    effects = set(adapter_schema["properties"]["operations"]["items"]["properties"]["effect"]["enum"])
    required_effects = {"resolve", "inspect", "mutate", "identify", "verify", "actuate", "observe", "authorize", "recover", "checkpoint"}
    if effects != required_effects:
        fail("Capability Adapter semantic effect vocabulary is incomplete or unexpected")

    kinds = set(evidence_schema["$defs"]["recordKind"]["enum"])
    if kinds != {"candidate", "transformation", "verification", "delivery", "observation", "checkpoint"}:
        fail("Evidence Record kind vocabulary is incomplete or unexpected")

    forbidden = [
        "SPECIFICATION.md",
        "SVIF_ARCHITECTURE_DRAFT.md",
        "SVIF_CAPABILITY_ADAPTER_DRAFT.md",
        "profiles/SOFTWARE_DELIVERY_DRAFT.md",
        "conformance/check_v0_1.py",
        "conformance/v0.1.md",
        "skills",
        ".chatgpt/state.yaml",
        ".chatgpt/next-steps.md",
        ".chatgpt/decisions.md",
        ".chatgpt/checkpoints",
        ".chatgpt/decisions",
        ".chatgpt/recovery-playbook.md",
        ".chatgpt/validation-1.md",
        ".chatgpt/validation-2.md",
    ]
    for path in forbidden:
        if (ROOT / path).exists():
            fail(f"predecessor artifact remains active on main: {path}")

    state = (ROOT / ".agnir/state.md").read_text(encoding="utf-8")
    if "The Project persists; Executors and execution environments may change." not in state:
        fail("cold-start state did not recover the expected stable rule")
    if "Svif depends on a compatible Agnir Core protocol" not in state:
        fail("Agnir protocol dependency boundary missing from durable state")

    print("PASS: Svif 0.2 active structure with Agnir 0.1 continuity")


if __name__ == "__main__":
    main()
