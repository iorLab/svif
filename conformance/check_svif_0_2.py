#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

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


def load_json(path: str) -> Any:
    try:
        return json.loads((ROOT / path).read_text(encoding="utf-8"))
    except Exception as exc:
        fail(f"invalid JSON in {path}: {exc}")


def evidence_fixture_errors(records: Any) -> list[str]:
    errors: list[str] = []
    if not isinstance(records, list) or not records:
        return ["fixture must be a non-empty JSON array of Evidence Records"]

    expected_project: str | None = None
    expected_operation: str | None = None
    established: set[str] = set()
    verified: set[str] = set()
    deliveries: set[tuple[str, str]] = set()
    observations: set[tuple[str, str]] = set()
    seen_kinds: set[str] = set()
    allowed_statuses = {"succeeded", "failed", "blocked", "unknown"}

    for index, record in enumerate(records):
        label = f"record[{index}]"
        if not isinstance(record, dict):
            errors.append(f"{label} is not an object")
            continue

        svif = record.get("svif")
        if not isinstance(svif, dict) or svif.get("version") != "0.2" or svif.get("schema") != "evidence-record/0.2":
            errors.append(f"{label} does not identify the Evidence Record 0.2 schema")

        metadata = record.get("record")
        if not isinstance(metadata, dict):
            errors.append(f"{label} has no record metadata")
            continue

        kind = metadata.get("kind")
        if not isinstance(kind, str):
            errors.append(f"{label} has no record kind")
            continue
        seen_kinds.add(kind)

        project_identity = metadata.get("project_identity")
        operation_id = metadata.get("operation_id")
        if not isinstance(project_identity, str) or not project_identity:
            errors.append(f"{label} has no project identity")
        elif expected_project is None:
            expected_project = project_identity
        elif project_identity != expected_project:
            errors.append(f"{label} crosses project identity within one fixture chain")

        if not isinstance(operation_id, str) or not operation_id:
            errors.append(f"{label} has no operation id")
        elif expected_operation is None:
            expected_operation = operation_id
        elif operation_id != expected_operation:
            errors.append(f"{label} crosses operation id within one fixture chain")

        subject = record.get("subject")
        if not isinstance(subject, dict) or not isinstance(subject.get("identity"), str) or not subject.get("identity"):
            errors.append(f"{label} has no stable subject identity")
            continue
        subject_identity = subject["identity"]

        result = record.get("result")
        if not isinstance(result, dict) or result.get("status") not in allowed_statuses:
            errors.append(f"{label} has an invalid result status")
            continue
        if result["status"] != "succeeded":
            continue

        if kind == "candidate":
            established.add(subject_identity)

        elif kind == "transformation":
            parents = subject.get("derived_from")
            if not isinstance(parents, list) or not parents:
                errors.append(f"{label} successful transformation has no derivation input")
            else:
                missing = [parent for parent in parents if parent not in established]
                if missing:
                    errors.append(f"{label} derives from unestablished subject(s): {', '.join(missing)}")
            established.add(subject_identity)

        elif kind == "verification":
            if subject_identity not in established:
                errors.append(f"{label} verifies a subject that was not established in the chain")
            verified.add(subject_identity)

        elif kind == "delivery":
            if subject_identity not in established:
                errors.append(f"{label} delivers a subject that was not established in the chain")
            if subject_identity not in verified:
                errors.append(f"{label} delivery subject {subject_identity} was not independently verified")
            target = record.get("target")
            if not isinstance(target, dict) or not isinstance(target.get("identity"), str) or not target.get("identity"):
                errors.append(f"{label} successful delivery has no target identity")
            else:
                deliveries.add((subject_identity, target["identity"]))

        elif kind == "observation":
            target = record.get("target")
            if not isinstance(target, dict) or not isinstance(target.get("identity"), str) or not target.get("identity"):
                errors.append(f"{label} successful observation has no target identity")
            else:
                pair = (subject_identity, target["identity"])
                if pair not in deliveries:
                    errors.append(f"{label} observation does not correspond to a successful delivered subject/target pair")
                observations.add(pair)

    required_kinds = {"candidate", "transformation", "verification", "delivery", "observation"}
    missing_kinds = required_kinds - seen_kinds
    if missing_kinds:
        errors.append(f"fixture chain is missing required record kind(s): {', '.join(sorted(missing_kinds))}")

    for subject_identity, target_identity in sorted(deliveries):
        if (subject_identity, target_identity) not in observations:
            errors.append(
                f"successful delivery of {subject_identity} to {target_identity} has no matching successful observation"
            )

    return errors


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
        "conformance/fixtures/evidence-chain-positive.json",
        "conformance/fixtures/evidence-chain-provenance-mismatch.json",
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

    positive = load_json("conformance/fixtures/evidence-chain-positive.json")
    positive_errors = evidence_fixture_errors(positive)
    if positive_errors:
        fail("positive evidence-chain fixture failed: " + "; ".join(positive_errors))

    negative = load_json("conformance/fixtures/evidence-chain-provenance-mismatch.json")
    negative_errors = evidence_fixture_errors(negative)
    if not negative_errors:
        fail("negative provenance fixture unexpectedly passed")
    if not any("not independently verified" in error for error in negative_errors):
        fail("negative provenance fixture failed for the wrong reason: " + "; ".join(negative_errors))

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

    print("PASS: Svif 0.2 structure, Agnir 0.1 continuity, and evidence provenance fixtures")


if __name__ == "__main__":
    main()
