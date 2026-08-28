from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN_ROOT = ROOT / "plugin"
SCHEMA_ID = "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"
ALLOWED_MANIFEST_KEYS = {
    "$schema", "name", "version", "description", "author", "homepage",
    "repository", "license", "keywords", "extensions",
}
ALLOWED_AUTHOR_KEYS = {"name", "email", "url"}
NAME_PATTERN = re.compile(r"^(?!.*(?:--|\.\.))[a-z0-9](?:[a-z0-9.-]*[a-z0-9])?$")
SKILL_NAME_PATTERN = re.compile(r"^(?!.*--)[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$")
ALLOWED_SKILL_FRONTMATTER_KEYS = {
    "name", "description", "license", "compatibility", "metadata", "allowed-tools",
}


def validate_agent_plugins_1_0_manifest(manifest: object) -> list[str]:
    errors: list[str] = []
    if not isinstance(manifest, dict):
        return ["manifest must be an object"]

    unknown = set(manifest) - ALLOWED_MANIFEST_KEYS
    if unknown:
        errors.append(f"additional properties are forbidden: {sorted(unknown)}")
    if manifest.get("$schema") != SCHEMA_ID:
        errors.append("$schema must target Agent Plugins 1.0.0")
    if "name" not in manifest:
        errors.append("name is required")
    else:
        name = manifest["name"]
        if not isinstance(name, str) or not 1 <= len(name) <= 64 or not NAME_PATTERN.fullmatch(name):
            errors.append("name violates Agent Plugins 1.0.0 constraints")

    for key in ("version", "description", "homepage", "repository", "license"):
        if key in manifest and not isinstance(manifest[key], str):
            errors.append(f"{key} must be a string")

    if "author" in manifest:
        author = manifest["author"]
        if not isinstance(author, dict):
            errors.append("author must be an object")
        else:
            unknown_author = set(author) - ALLOWED_AUTHOR_KEYS
            if unknown_author:
                errors.append(f"author has forbidden properties: {sorted(unknown_author)}")
            for key, value in author.items():
                if not isinstance(value, str):
                    errors.append(f"author.{key} must be a string")

    if "keywords" in manifest:
        keywords = manifest["keywords"]
        if not isinstance(keywords, list) or any(not isinstance(item, str) for item in keywords):
            errors.append("keywords must be an array of strings")

    if "extensions" in manifest:
        extensions = manifest["extensions"]
        if not isinstance(extensions, dict) or any(not isinstance(value, dict) for value in extensions.values()):
            errors.append("extensions must be an object whose values are objects")

    return errors


def parse_skill_frontmatter(text: str) -> tuple[dict[str, str], str, list[str]]:
    errors: list[str] = []
    if not text.startswith("---\n"):
        return {}, text, ["SKILL.md must start with YAML frontmatter"]

    closing = text.find("\n---\n", 4)
    if closing == -1:
        return {}, text, ["SKILL.md frontmatter must have a closing delimiter"]

    raw_frontmatter = text[4:closing]
    body = text[closing + 5:]
    fields: dict[str, str] = {}
    for line in raw_frontmatter.splitlines():
        if not line.strip():
            continue
        if line.startswith((" ", "\t")) or ":" not in line:
            errors.append("test validator supports only flat scalar frontmatter used by this Skill")
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if key in fields:
            errors.append(f"duplicate frontmatter key: {key}")
        fields[key] = value

    return fields, body, errors


def validate_agent_skill(skill_dir: Path, text: str) -> list[str]:
    fields, body, errors = parse_skill_frontmatter(text)
    unknown = set(fields) - ALLOWED_SKILL_FRONTMATTER_KEYS
    if unknown:
        errors.append(f"unsupported Agent Skills frontmatter fields: {sorted(unknown)}")

    name = fields.get("name", "")
    if not name:
        errors.append("skill name is required")
    elif len(name) > 64 or not SKILL_NAME_PATTERN.fullmatch(name):
        errors.append("skill name violates Agent Skills naming constraints")
    elif name != skill_dir.name:
        errors.append("skill name must match its parent directory name")

    description = fields.get("description", "")
    if not description:
        errors.append("skill description is required")
    elif len(description) > 1024:
        errors.append("skill description exceeds 1024 characters")

    compatibility = fields.get("compatibility")
    if compatibility is not None and not 1 <= len(compatibility) <= 500:
        errors.append("skill compatibility must be 1-500 characters when present")

    if not body.strip():
        errors.append("SKILL.md must contain instruction body content")

    return errors


class PluginPackageTests(unittest.TestCase):
    def test_manifest_conforms_to_agent_plugins_1_0_schema_constraints(self) -> None:
        manifest = json.loads((PLUGIN_ROOT / "plugin.json").read_text(encoding="utf-8"))
        self.assertEqual(validate_agent_plugins_1_0_manifest(manifest), [])
        self.assertEqual(manifest["name"], "svif")
        self.assertEqual(manifest["version"], "0.2.0-dev")
        self.assertEqual(manifest["repository"], "https://github.com/iorLab/svif")
        self.assertEqual(manifest["homepage"], "https://github.com/iorLab/svif")

    def test_manifest_validator_rejects_schema_breakage(self) -> None:
        invalid = {"$schema": SCHEMA_ID, "name": "Svif", "unexpected": True}
        errors = validate_agent_plugins_1_0_manifest(invalid)
        self.assertTrue(errors)
        self.assertTrue(any("additional properties" in error for error in errors))
        self.assertTrue(any("name violates" in error for error in errors))

    def test_svif_skill_conforms_to_agent_skills_frontmatter_contract(self) -> None:
        skill_dir = PLUGIN_ROOT / "skills" / "svif"
        text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
        self.assertEqual(validate_agent_skill(skill_dir, text), [])

    def test_skill_validator_rejects_name_directory_mismatch_and_long_description(self) -> None:
        invalid = "---\nname: other-skill\ndescription: " + ("x" * 1025) + "\n---\n\nDo work.\n"
        errors = validate_agent_skill(PLUGIN_ROOT / "skills" / "svif", invalid)
        self.assertTrue(any("parent directory" in error for error in errors))
        self.assertTrue(any("1024" in error for error in errors))

    def test_svif_skill_has_required_core_guards(self) -> None:
        text = (PLUGIN_ROOT / "skills" / "svif" / "SKILL.md").read_text(encoding="utf-8")
        for marker in (
            "Project root -> AGENTS.md -> README.md / Agnir Project Instructions -> AGNIR.yaml",
            "repository-filesystem/0.1",
            "AGNIR.yaml",
            "SVIF.yaml",
            "DISCOVER -> PLAN -> CHANGE -> VERIFY -> DELIVER -> OBSERVE -> CHECKPOINT",
            "Untrusted model/result payloads must never self-grant protected authority.",
            "Checkpoint durable truth",
            "REPOSITORY_TREE.md",
            "do not claim installation validation",
        ):
            self.assertIn(marker, text)

    def test_current_agnir_binding_has_no_live_predecessor_ref(self) -> None:
        agnir = (ROOT / "AGNIR.yaml").read_text(encoding="utf-8")
        svif = (ROOT / "SVIF.yaml").read_text(encoding="utf-8")

        for text in (agnir, svif):
            self.assertNotIn("predecessor_ref:", text)
            self.assertNotIn("legacy/zerolocal-v0.1", text)

        self.assertIn('discovery_profile: "repository-filesystem/0.1"', agnir)
        self.assertIn('provider: "agnir"', svif)
        self.assertIn('compatibility: "0.1"', svif)
        self.assertIn('profile: "repository-filesystem/0.1"', svif)

    def test_plugin_mvp_is_skill_only_and_does_not_shadow_runtime(self) -> None:
        self.assertFalse((PLUGIN_ROOT / "mcp.json").exists())
        self.assertFalse((PLUGIN_ROOT / "src").exists())
        self.assertTrue((ROOT / "src" / "svif" / "runtime.py").exists())


if __name__ == "__main__":
    unittest.main()
