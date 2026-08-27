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


def adapter_fixture_errors(descriptor: Any, adapter_schema: dict[str, Any], evidence_kinds: set[str]) -> list[str]:
    errors: list[str] = []
    if not isinstance(descriptor, dict):
        return ["adapter fixture must be a JSON object"]

    svif_adapter = descriptor.get("svif_adapter")
    if not isinstance(svif_adapter, dict) or svif_adapter.get("version") != "0.2":
        errors.append("adapter fixture does not declare svif_adapter 0.2")

    adapter = descriptor.get("adapter")
    if not isinstance(adapter, dict):
        return errors + ["adapter fixture has no adapter metadata"]

    if not isinstance(adapter.get("id"), str) or not adapter.get("id"):
        errors.append("adapter id is missing")
    if not isinstance(adapter.get("version"), str) or not adapter.get("version"):
        errors.append("adapter version is missing")

    allowed_kinds = set(adapter_schema["properties"]["adapter"]["properties"]["kinds"]["items"]["enum"])
    kinds = adapter.get("kinds")
    if not isinstance(kinds, list) or not kinds:
        errors.append("adapter kinds must be a non-empty array")
        kinds = []
    elif len(kinds) != len(set(kinds)):
        errors.append("adapter kinds are not unique")
    unknown_kinds = set(kinds) - allowed_kinds
    if unknown_kinds:
        errors.append(f"adapter uses unknown kind(s): {', '.join(sorted(unknown_kinds))}")

    operation_schema = adapter_schema["properties"]["operations"]["items"]["properties"]
    allowed_effects = set(operation_schema["effect"]["enum"])
    allowed_authority = set(operation_schema["authority"]["enum"])
    allowed_retry = set(operation_schema["retry"]["enum"])
    allowed_failures = set(adapter_schema["$defs"]["failureClass"]["enum"])

    operations = descriptor.get("operations")
    if not isinstance(operations, list) or not operations:
        errors.append("adapter operations must be a non-empty array")
        operations = []

    names: set[str] = set()
    for index, operation in enumerate(operations):
        label = f"operation[{index}]"
        if not isinstance(operation, dict):
            errors.append(f"{label} is not an object")
            continue

        name = operation.get("name")
        if not isinstance(name, str) or not name:
            errors.append(f"{label} has no name")
        elif name in names:
            errors.append(f"duplicate operation name: {name}")
        else:
            names.add(name)

        effect = operation.get("effect")
        authority = operation.get("authority")
        retry = operation.get("retry")
        if effect not in allowed_effects:
            errors.append(f"{label} has unknown semantic effect: {effect}")
        if authority not in allowed_authority:
            errors.append(f"{label} has unknown authority class: {authority}")
        if retry not in allowed_retry:
            errors.append(f"{label} has unknown retry class: {retry}")

        for record_key in ("input_record_kinds", "output_record_kinds"):
            record_kinds = operation.get(record_key, [])
            if not isinstance(record_kinds, list):
                errors.append(f"{label} {record_key} is not an array")
                continue
            if len(record_kinds) != len(set(record_kinds)):
                errors.append(f"{label} {record_key} contains duplicates")
            unknown_records = set(record_kinds) - evidence_kinds
            if unknown_records:
                errors.append(f"{label} {record_key} uses unknown Evidence kind(s): {', '.join(sorted(unknown_records))}")

        failure_classes = operation.get("failure_classes", [])
        if not isinstance(failure_classes, list):
            errors.append(f"{label} failure_classes is not an array")
        else:
            if len(failure_classes) != len(set(failure_classes)):
                errors.append(f"{label} failure_classes contains duplicates")
            unknown_failures = set(failure_classes) - allowed_failures
            if unknown_failures:
                errors.append(f"{label} uses unknown failure class(es): {', '.join(sorted(unknown_failures))}")

        if effect == "verify" and authority in {"protected-delivery", "destructive", "principal-action"}:
            errors.append(f"{label} verification operation improperly implies protected delivery/destructive authority")

    credentials = descriptor.get("credentials", [])
    if not isinstance(credentials, list):
        errors.append("credentials is not an array")
    else:
        allowed_credential_keys = {"reference", "purpose", "minimum_scope", "value_transport"}
        allowed_transport = {"none", "protected-store-only", "adapter-managed"}
        for index, credential in enumerate(credentials):
            label = f"credential[{index}]"
            if not isinstance(credential, dict):
                errors.append(f"{label} is not an object")
                continue
            extra_keys = set(credential) - allowed_credential_keys
            if extra_keys:
                errors.append(f"{label} contains forbidden/unknown field(s): {', '.join(sorted(extra_keys))}")
            if not isinstance(credential.get("reference"), str) or not credential.get("reference"):
                errors.append(f"{label} has no protected credential reference")
            if not isinstance(credential.get("purpose"), str) or not credential.get("purpose"):
                errors.append(f"{label} has no purpose")
            if credential.get("value_transport") not in allowed_transport:
                errors.append(f"{label} has invalid value_transport")

    return errors


def main() -> None:
    adapter_fixture_paths = [
        "conformance/fixtures/adapters/workspace-scm.json",
        "conformance/fixtures/adapters/verification.json",
        "conformance/fixtures/adapters/delivery-provider.json",
        "conformance/fixtures/adapters/observation.json",
    ]
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
        *adapter_fixture_paths,
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

    aggregate_adapter_kinds: set[str] = set()
    aggregate_fixture_effects: set[str] = set()
    adapters_by_id: dict[str, dict[str, Any]] = {}
    for path in adapter_fixture_paths:
        descriptor = load_json(path)
        descriptor_errors = adapter_fixture_errors(descriptor, adapter_schema, kinds)
        if descriptor_errors:
            fail(f"Capability Adapter fixture {path} failed: " + "; ".join(descriptor_errors))
        adapter_id = descriptor["adapter"]["id"]
        if adapter_id in adapters_by_id:
            fail(f"duplicate Capability Adapter fixture id: {adapter_id}")
        adapters_by_id[adapter_id] = descriptor
        aggregate_adapter_kinds.update(descriptor["adapter"]["kinds"])
        aggregate_fixture_effects.update(operation["effect"] for operation in descriptor["operations"])

    required_fixture_kinds = {"workspace", "scm", "verification", "delivery", "provider", "observation"}
    if not required_fixture_kinds <= aggregate_adapter_kinds:
        missing = required_fixture_kinds - aggregate_adapter_kinds
        fail("Capability Adapter fixtures do not cover boundary kind(s): " + ", ".join(sorted(missing)))

    required_fixture_effects = {"resolve", "inspect", "mutate", "identify", "verify", "actuate", "observe", "recover"}
    if not required_fixture_effects <= aggregate_fixture_effects:
        missing = required_fixture_effects - aggregate_fixture_effects
        fail("Capability Adapter fixtures do not exercise semantic effect(s): " + ", ".join(sorted(missing)))

    workspace = adapters_by_id["fixture.workspace-scm"]
    identify_ops = [operation for operation in workspace["operations"] if operation["effect"] == "identify"]
    if not identify_ops or "candidate" not in identify_ops[0].get("output_record_kinds", []):
        fail("workspace/SCM fixture does not emit candidate evidence from identify")

    verification = adapters_by_id["fixture.verification"]
    verify_ops = [operation for operation in verification["operations"] if operation["effect"] == "verify"]
    if not verify_ops or verify_ops[0]["authority"] != "verification" or "verification" not in verify_ops[0].get("output_record_kinds", []):
        fail("verification fixture does not preserve verification-only authority/evidence semantics")

    delivery = adapters_by_id["fixture.delivery-provider"]
    actuate_ops = [operation for operation in delivery["operations"] if operation["effect"] == "actuate"]
    if not actuate_ops:
        fail("delivery/provider fixture has no actuation operation")
    actuate = actuate_ops[0]
    if actuate["authority"] != "protected-delivery":
        fail("delivery/provider actuation does not declare protected-delivery authority")
    if "verification" not in actuate.get("input_record_kinds", []) or "delivery" not in actuate.get("output_record_kinds", []):
        fail("delivery/provider actuation does not consume verification and emit delivery evidence")
    if "PROVENANCE_MISMATCH" not in actuate.get("failure_classes", []):
        fail("delivery/provider actuation does not expose portable provenance mismatch failure")

    observation = adapters_by_id["fixture.observation"]
    observe_ops = [operation for operation in observation["operations"] if operation["effect"] == "observe"]
    if not observe_ops or "delivery" not in observe_ops[0].get("input_record_kinds", []) or "observation" not in observe_ops[0].get("output_record_kinds", []):
        fail("observation fixture does not consume delivery and emit independent observation evidence")

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

    print("PASS: Svif 0.2 structure, Agnir 0.1 continuity, evidence provenance, and Capability Adapter fixtures")


if __name__ == "__main__":
    main()
