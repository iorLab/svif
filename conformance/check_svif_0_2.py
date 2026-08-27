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
    in_section = False
    for line in text.splitlines():
        if re.match(rf"^{re.escape(section)}:\s*$", line):
            in_section = True
            continue
        if in_section and line and not line.startswith((" ", "\t", "#")):
            break
        if in_section:
            match = re.match(rf"^\s{{2}}{re.escape(key)}:\s*(.+?)\s*$", line)
            if match:
                return match.group(1).strip().strip("\"'")
    return None


def load_json(path: str) -> Any:
    try:
        return json.loads((ROOT / path).read_text(encoding="utf-8"))
    except Exception as exc:
        fail(f"invalid JSON in {path}: {exc}")


def evidence_errors(records: Any) -> list[str]:
    if not isinstance(records, list) or not records:
        return ["fixture must be a non-empty array"]

    errors: list[str] = []
    established: set[str] = set()
    verified: set[str] = set()
    deliveries: set[tuple[str, str]] = set()
    observations: set[tuple[str, str]] = set()
    seen: set[str] = set()
    project: str | None = None
    operation: str | None = None

    for index, record in enumerate(records):
        label = f"record[{index}]"
        if not isinstance(record, dict):
            errors.append(f"{label} is not an object")
            continue
        svif = record.get("svif", {})
        if svif.get("version") != "0.2" or svif.get("schema") != "evidence-record/0.2":
            errors.append(f"{label} has wrong Evidence schema")
        metadata = record.get("record", {})
        kind = metadata.get("kind")
        seen.add(kind) if isinstance(kind, str) else None
        current_project = metadata.get("project_identity")
        current_operation = metadata.get("operation_id")
        if project is None:
            project = current_project
        elif current_project != project:
            errors.append(f"{label} crosses project identity")
        if operation is None:
            operation = current_operation
        elif current_operation != operation:
            errors.append(f"{label} crosses operation id")
        subject = record.get("subject", {})
        identity = subject.get("identity")
        if not isinstance(identity, str) or not identity:
            errors.append(f"{label} has no stable subject identity")
            continue
        if record.get("result", {}).get("status") != "succeeded":
            continue

        if kind == "candidate":
            established.add(identity)
        elif kind == "transformation":
            parents = subject.get("derived_from", [])
            if not parents or any(parent not in established for parent in parents):
                errors.append(f"{label} has invalid derivation")
            established.add(identity)
        elif kind == "verification":
            if identity not in established:
                errors.append(f"{label} verifies unestablished subject")
            verified.add(identity)
        elif kind == "delivery":
            if identity not in verified:
                errors.append(f"{label} delivery subject {identity} was not independently verified")
            target = record.get("target", {}).get("identity")
            if not isinstance(target, str) or not target:
                errors.append(f"{label} has no delivery target")
            else:
                deliveries.add((identity, target))
        elif kind == "observation":
            target = record.get("target", {}).get("identity")
            pair = (identity, target)
            if pair not in deliveries:
                errors.append(f"{label} does not observe a delivered subject/target pair")
            elif isinstance(target, str):
                observations.add(pair)

    required = {"candidate", "transformation", "verification", "delivery", "observation"}
    if not required <= seen:
        errors.append("fixture is missing required Evidence record kinds")
    for pair in deliveries:
        if pair not in observations:
            errors.append(f"delivery {pair!r} has no matching observation")
    return errors


def adapter_errors(descriptor: Any, schema: dict[str, Any], evidence_kinds: set[str]) -> list[str]:
    if not isinstance(descriptor, dict):
        return ["descriptor is not an object"]
    errors: list[str] = []
    if descriptor.get("svif_adapter", {}).get("version") != "0.2":
        errors.append("wrong adapter schema version")

    adapter = descriptor.get("adapter", {})
    if not adapter.get("id") or not adapter.get("version"):
        errors.append("adapter identity/version missing")
    allowed_kinds = set(schema["properties"]["adapter"]["properties"]["kinds"]["items"]["enum"])
    kinds = adapter.get("kinds", [])
    if not isinstance(kinds, list) or not kinds or not set(kinds) <= allowed_kinds:
        errors.append("adapter kinds invalid")

    op_schema = schema["properties"]["operations"]["items"]["properties"]
    allowed_effects = set(op_schema["effect"]["enum"])
    allowed_authority = set(op_schema["authority"]["enum"])
    allowed_retry = set(op_schema["retry"]["enum"])
    allowed_failures = set(schema["$defs"]["failureClass"]["enum"])
    names: set[str] = set()
    for op in descriptor.get("operations", []):
        name = op.get("name")
        if not name or name in names:
            errors.append("operation name missing or duplicated")
        names.add(name)
        if op.get("effect") not in allowed_effects:
            errors.append(f"{name}: invalid effect")
        if op.get("authority") not in allowed_authority:
            errors.append(f"{name}: invalid authority")
        if op.get("retry") not in allowed_retry:
            errors.append(f"{name}: invalid retry class")
        for key in ("input_record_kinds", "output_record_kinds"):
            if not set(op.get(key, [])) <= evidence_kinds:
                errors.append(f"{name}: invalid {key}")
        if not set(op.get("failure_classes", [])) <= allowed_failures:
            errors.append(f"{name}: invalid failure class")
        if op.get("effect") == "verify" and op.get("authority") in {"protected-delivery", "destructive", "principal-action"}:
            errors.append(f"{name}: verification implies excessive authority")

    allowed_credential_keys = {"reference", "purpose", "minimum_scope", "value_transport"}
    for credential in descriptor.get("credentials", []):
        if not set(credential) <= allowed_credential_keys:
            errors.append("credential descriptor contains secret/unknown field")
        if not credential.get("reference") or not credential.get("purpose"):
            errors.append("credential reference/purpose missing")
        if credential.get("value_transport") not in {"none", "protected-store-only", "adapter-managed"}:
            errors.append("credential value_transport invalid")
    return errors


def main() -> None:
    adapters = [
        "conformance/fixtures/adapters/workspace-scm.json",
        "conformance/fixtures/adapters/verification.json",
        "conformance/fixtures/adapters/delivery-provider.json",
        "conformance/fixtures/adapters/observation.json",
    ]
    required = [
        "SVIF.yaml", "AGNIR.yaml", ".agnir/state.md", ".agnir/next-actions.md", ".agnir/decisions.md",
        "spec/CORE.md", "spec/CAPABILITY_ADAPTER.md", "spec/EVIDENCE.md", "profiles/SOFTWARE_DELIVERY.md",
        "schemas/capability-adapter.schema.json", "schemas/evidence-record.schema.json",
        "conformance/fixtures/evidence-chain-positive.json", "conformance/fixtures/evidence-chain-provenance-mismatch.json",
        *adapters, "history/PREDECESSOR.md",
    ]
    for path in required:
        if not (ROOT / path).exists():
            fail(f"missing active Svif artifact: {path}")

    if (ROOT / ".chatgpt").exists():
        fail("execution-surface-specific .chatgpt structure remains active on main")

    svif = (ROOT / "SVIF.yaml").read_text(encoding="utf-8")
    agnir = (ROOT / "AGNIR.yaml").read_text(encoding="utf-8")
    if scalar(svif, "svif", "version") != "0.2":
        fail("SVIF.yaml does not declare Svif 0.2")
    if scalar(svif, "continuity", "protocol") != "agnir" or scalar(svif, "continuity", "compatibility") != "0.1":
        fail("SVIF.yaml does not declare Agnir 0.1 continuity")
    if scalar(agnir, "agnir", "version") != "0.1":
        fail("AGNIR.yaml does not declare Agnir 0.1")

    core = (ROOT / "spec/CORE.md").read_text(encoding="utf-8")
    if "DISCOVER -> PLAN -> CHANGE -> VERIFY -> DELIVER -> OBSERVE -> CHECKPOINT" not in core:
        fail("Core lifecycle is missing or changed")
    if "Planning semantics are mandatory before material mutation" not in core:
        fail("PLAN semantic rule is missing")

    adapter_schema = load_json("schemas/capability-adapter.schema.json")
    evidence_schema = load_json("schemas/evidence-record.schema.json")
    evidence_kinds = set(evidence_schema["$defs"]["recordKind"]["enum"])
    expected_effects = {"resolve", "inspect", "mutate", "identify", "verify", "actuate", "observe", "authorize", "recover", "checkpoint"}
    actual_effects = set(adapter_schema["properties"]["operations"]["items"]["properties"]["effect"]["enum"])
    if actual_effects != expected_effects:
        fail("Capability Adapter effect vocabulary diverged")

    by_id: dict[str, Any] = {}
    aggregate_kinds: set[str] = set()
    aggregate_effects: set[str] = set()
    for path in adapters:
        descriptor = load_json(path)
        errors = adapter_errors(descriptor, adapter_schema, evidence_kinds)
        if errors:
            fail(f"Capability Adapter fixture {path} failed: " + "; ".join(errors))
        by_id[descriptor["adapter"]["id"]] = descriptor
        aggregate_kinds.update(descriptor["adapter"]["kinds"])
        aggregate_effects.update(op["effect"] for op in descriptor["operations"])

    if not {"workspace", "scm", "verification", "delivery", "provider", "observation"} <= aggregate_kinds:
        fail("Capability Adapter fixtures do not cover required boundary kinds")
    if not {"resolve", "inspect", "mutate", "identify", "verify", "actuate", "observe", "recover"} <= aggregate_effects:
        fail("Capability Adapter fixtures do not exercise required effects")

    actuate = next(op for op in by_id["fixture.delivery-provider"]["operations"] if op["effect"] == "actuate")
    if actuate["authority"] != "protected-delivery" or "verification" not in actuate.get("input_record_kinds", []) or "delivery" not in actuate.get("output_record_kinds", []) or "PROVENANCE_MISMATCH" not in actuate.get("failure_classes", []):
        fail("delivery/provider fixture does not preserve verification-gated protected delivery semantics")
    observe = next(op for op in by_id["fixture.observation"]["operations"] if op["effect"] == "observe")
    if "delivery" not in observe.get("input_record_kinds", []) or "observation" not in observe.get("output_record_kinds", []):
        fail("observation fixture does not preserve independent observation semantics")

    positive_errors = evidence_errors(load_json("conformance/fixtures/evidence-chain-positive.json"))
    if positive_errors:
        fail("positive evidence-chain fixture failed: " + "; ".join(positive_errors))
    negative_errors = evidence_errors(load_json("conformance/fixtures/evidence-chain-provenance-mismatch.json"))
    if not any("not independently verified" in error for error in negative_errors):
        fail("negative provenance fixture did not fail for provenance mismatch")

    for path in ["SPECIFICATION.md", "SVIF_ARCHITECTURE_DRAFT.md", "SVIF_CAPABILITY_ADAPTER_DRAFT.md", "profiles/SOFTWARE_DELIVERY_DRAFT.md", "conformance/check_v0_1.py", "conformance/v0.1.md", "skills"]:
        if (ROOT / path).exists():
            fail(f"predecessor artifact remains active on main: {path}")

    state = (ROOT / ".agnir/state.md").read_text(encoding="utf-8")
    if "The Project persists; Executors and execution environments may change." not in state:
        fail("cold-start state did not recover the expected stable rule")
    if "Svif depends on a compatible Agnir Core protocol" not in state:
        fail("Agnir protocol dependency boundary missing from durable state")

    print("PASS: Svif 0.2 structure, Agnir 0.1 continuity, evidence provenance, and Capability Adapter fixtures")


if __name__ == "__main__":
    main()
