from __future__ import annotations

import json
import re
import tempfile
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


def _quoted_scalar(text: str, key: str) -> str:
    match = re.search(rf'^\s+{re.escape(key)}:\s+"([^"]+)"\s*$', text, re.MULTILINE)
    if match is None:
        raise AssertionError(f"missing quoted scalar {key!r}")
    return match.group(1)


def validate_agent_plugins_1_0_manifest(manifest: object) -> tuple[list[str], list[str]]:
    """Return fatal errors and non-fatal diagnostics using Agent Plugins 1.0 rules.

    The normative specification deliberately makes two closed-schema failures non-fatal:
    unknown top-level fields, and a non-object ``extensions`` field. The former are
    reported and ignored; the latter is reported and ignored. Unknown extension
    namespaces are client-owned and their values are not validated by a portable
    package validator.
    """
    errors: list[str] = []
    diagnostics: list[str] = []
    if not isinstance(manifest, dict):
        return ["manifest must be an object"], diagnostics

    unknown = set(manifest) - ALLOWED_MANIFEST_KEYS
    if unknown:
        diagnostics.append(f"unknown top-level fields must be reported and ignored: {sorted(unknown)}")

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

    if "extensions" in manifest and not isinstance(manifest["extensions"], dict):
        diagnostics.append("non-object extensions must be reported and ignored")

    return errors, diagnostics


def inspect_plugin_filesystem(plugin_root: Path) -> dict[str, list[str]]:
    """Model Agent Plugins 1.0 filesystem containment at its normative failure boundaries."""
    result = {
        "plugin_errors": [],
        "component_errors": [],
        "skipped_skills": [],
        "denied_paths": [],
    }
    try:
        resolved_root = plugin_root.resolve(strict=True)
    except FileNotFoundError:
        result["plugin_errors"].append("plugin root does not exist")
        return result

    manifest = plugin_root / "plugin.json"
    try:
        resolved_manifest = manifest.resolve(strict=True)
    except FileNotFoundError:
        result["plugin_errors"].append("plugin.json must exist at the plugin root")
    else:
        if not resolved_manifest.is_relative_to(resolved_root):
            result["plugin_errors"].append("plugin.json resolves outside plugin root")
        elif not resolved_manifest.is_file():
            result["plugin_errors"].append("plugin.json must resolve to a regular file")

    skills = plugin_root / "skills"
    skills_valid = True
    if skills.exists() or skills.is_symlink():
        try:
            resolved_skills = skills.resolve(strict=True)
        except FileNotFoundError:
            result["component_errors"].append("skills fixed component location does not resolve")
            skills_valid = False
        else:
            if not resolved_skills.is_relative_to(resolved_root):
                result["component_errors"].append("skills fixed component location escapes plugin root")
                skills_valid = False
            elif not resolved_skills.is_dir():
                result["component_errors"].append("skills fixed component location must resolve to a directory")
                skills_valid = False

    discovered_skill_files: set[Path] = set()
    if skills_valid and skills.is_dir():
        for skill_dir in skills.iterdir():
            if not skill_dir.is_dir():
                continue
            skill_file = skill_dir / "SKILL.md"
            if not (skill_file.exists() or skill_file.is_symlink()):
                continue
            try:
                resolved_skill = skill_file.resolve(strict=True)
            except FileNotFoundError:
                continue
            discovered_skill_files.add(skill_file)
            if not resolved_skill.is_relative_to(resolved_root):
                result["skipped_skills"].append(str(skill_dir.relative_to(skills)))
                continue
            if not resolved_skill.is_file():
                discovered_skill_files.discard(skill_file)

    for path in plugin_root.rglob("*"):
        if path == manifest or path == skills or path in discovered_skill_files:
            continue
        try:
            resolved = path.resolve(strict=True)
        except FileNotFoundError:
            result["denied_paths"].append(str(path.relative_to(plugin_root)))
            continue
        if not resolved.is_relative_to(resolved_root):
            result["denied_paths"].append(str(path.relative_to(plugin_root)))

    return result


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
    def test_manifest_conforms_to_agent_plugins_1_0_constraints(self) -> None:
        manifest = json.loads((PLUGIN_ROOT / "plugin.json").read_text(encoding="utf-8"))
        version = (PLUGIN_ROOT.parent / "VERSION").read_text(encoding="utf-8").strip()
        errors, diagnostics = validate_agent_plugins_1_0_manifest(manifest)
        self.assertEqual(errors, [])
        self.assertEqual(diagnostics, [])
        self.assertEqual(manifest["name"], "svif")
        self.assertEqual(version, "0.2.0-preview.1")
        self.assertEqual(manifest["version"], version)
        self.assertEqual(manifest["repository"], "https://github.com/iorLab/svif")
        self.assertEqual(manifest["homepage"], "https://github.com/iorLab/svif")

    def test_manifest_validator_rejects_fatal_schema_breakage(self) -> None:
        invalid = {"$schema": SCHEMA_ID, "name": "Svif"}
        errors, diagnostics = validate_agent_plugins_1_0_manifest(invalid)
        self.assertTrue(any("name violates" in error for error in errors))
        self.assertEqual(diagnostics, [])

    def test_manifest_validator_preserves_normative_non_fatal_exceptions(self) -> None:
        tolerated = {
            "$schema": SCHEMA_ID,
            "name": "svif",
            "unexpected": True,
            "extensions": "invalid-but-non-fatal",
        }
        errors, diagnostics = validate_agent_plugins_1_0_manifest(tolerated)
        self.assertEqual(errors, [])
        self.assertTrue(any("unknown top-level" in diagnostic for diagnostic in diagnostics))
        self.assertTrue(any("non-object extensions" in diagnostic for diagnostic in diagnostics))

    def test_manifest_validator_does_not_validate_unimplemented_extension_namespaces(self) -> None:
        portable = {
            "$schema": SCHEMA_ID,
            "name": "svif",
            "extensions": {"com.example.client": "opaque-to-portable-validator"},
        }
        errors, diagnostics = validate_agent_plugins_1_0_manifest(portable)
        self.assertEqual(errors, [])
        self.assertEqual(diagnostics, [])

    def test_plugin_package_paths_are_contained_within_plugin_root(self) -> None:
        result = inspect_plugin_filesystem(PLUGIN_ROOT)
        self.assertEqual(result, {
            "plugin_errors": [], "component_errors": [], "skipped_skills": [], "denied_paths": [],
        })

    def test_manifest_escape_rejects_whole_plugin(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            plugin_root = base / "plugin"
            plugin_root.mkdir()
            outside = base / "manifest.json"
            outside.write_text('{"$schema": "x", "name": "svif"}', encoding="utf-8")
            (plugin_root / "plugin.json").symlink_to(outside)
            result = inspect_plugin_filesystem(plugin_root)
            self.assertTrue(any("plugin.json resolves outside" in error for error in result["plugin_errors"]))

    def test_skills_location_escape_invalidates_only_skill_component_type(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            plugin_root = base / "plugin"
            plugin_root.mkdir()
            (plugin_root / "plugin.json").write_text('{"$schema": "x", "name": "svif"}', encoding="utf-8")
            outside_skills = base / "outside-skills"
            outside_skills.mkdir()
            (plugin_root / "skills").symlink_to(outside_skills, target_is_directory=True)
            result = inspect_plugin_filesystem(plugin_root)
            self.assertEqual(result["plugin_errors"], [])
            self.assertTrue(any("skills fixed component location escapes" in error for error in result["component_errors"]))

    def test_escaping_skill_is_skipped_without_rejecting_plugin(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            plugin_root = base / "plugin"
            skill_dir = plugin_root / "skills" / "svif"
            skill_dir.mkdir(parents=True)
            (plugin_root / "plugin.json").write_text('{"$schema": "x", "name": "svif"}', encoding="utf-8")
            outside = base / "outside.md"
            outside.write_text("outside", encoding="utf-8")
            (skill_dir / "SKILL.md").symlink_to(outside)
            result = inspect_plugin_filesystem(plugin_root)
            self.assertEqual(result["plugin_errors"], [])
            self.assertEqual(result["component_errors"], [])
            self.assertEqual(result["skipped_skills"], ["svif"])

    def test_unrelated_escape_is_denied_without_rejecting_plugin(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            plugin_root = base / "plugin"
            plugin_root.mkdir()
            (plugin_root / "plugin.json").write_text('{"$schema": "x", "name": "svif"}', encoding="utf-8")
            outside = base / "outside.txt"
            outside.write_text("outside", encoding="utf-8")
            (plugin_root / "notes.txt").symlink_to(outside)
            result = inspect_plugin_filesystem(plugin_root)
            self.assertEqual(result["plugin_errors"], [])
            self.assertIn("notes.txt", result["denied_paths"])

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
        lineage = _quoted_scalar(svif, "lineage")
        selector = _quoted_scalar(svif, "vcs_selector")

        for text in (agnir, svif):
            self.assertNotIn("predecessor_ref:", text)
            self.assertNotIn("legacy/zerolocal-v0.1", text)

        for marker in (
            'version: "0.2"',
            'discovery_profile: "repository-filesystem/0.2"',
            f'lineage: "{lineage}"',
            f'selector: "{selector}"',
        ):
            self.assertIn(marker, agnir)
        for marker in (
            'provider: "agnir"',
            'compatibility: "0.2"',
            'profile: "repository-filesystem/0.2"',
            f'lineage: "{lineage}"',
            f'vcs_selector: "{selector}"',
        ):
            self.assertIn(marker, svif)

    def test_svif_project_has_self_describing_agnir_cold_start_route(self) -> None:
        agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        agnir = (ROOT / "AGNIR.yaml").read_text(encoding="utf-8")
        svif = (ROOT / "SVIF.yaml").read_text(encoding="utf-8")

        self.assertIn("Agnir Project Instructions", agents)
        self.assertIn("README.md", agents)
        self.assertNotIn(".agnir/state.md", agents)
        self.assertNotIn(".agnir/next-actions.md", agents)

        self.assertIn("## Agnir Project Instructions", readme)
        self.assertIn(
            "Project root -> AGENTS.md -> README.md / Agnir Project Instructions -> AGNIR.yaml -> declared durable memory",
            readme,
        )
        for marker in ("Current State", "Next Actions", "Decisions", "Evidence"):
            self.assertIn(marker, readme)

        self.assertIn('state: ".agnir/state.md"', agnir)
        self.assertIn('next_actions: ".agnir/next-actions.md"', agnir)
        self.assertIn('decisions: ".agnir/decisions.md"', agnir)
        self.assertIn('evidence: ".agnir/evidence/"', agnir)
        self.assertIn(
            'activation: "AGENTS.md -> README.md / Agnir Project Instructions -> AGNIR.yaml"',
            svif,
        )

        for path in (".agnir/state.md", ".agnir/next-actions.md", ".agnir/decisions.md", ".agnir/evidence"):
            self.assertTrue((ROOT / path).exists(), path)

    def test_plugin_mvp_is_skill_only_and_does_not_shadow_runtime(self) -> None:
        self.assertFalse((PLUGIN_ROOT / "mcp.json").exists())
        self.assertFalse((PLUGIN_ROOT / "src").exists())
        self.assertTrue((ROOT / "src" / "svif" / "runtime.py").exists())


if __name__ == "__main__":
    unittest.main()
