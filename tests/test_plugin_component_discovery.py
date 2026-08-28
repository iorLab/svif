from __future__ import annotations

import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN_ROOT = ROOT / "plugin"


def inspect_fixed_components(plugin_root: Path) -> dict[str, object]:
    """Model Agent Plugins 1.0 fixed-location discovery without implementing a client."""
    resolved_root = plugin_root.resolve(strict=True)
    result: dict[str, object] = {
        "skills_component_errors": [],
        "mcp_component_errors": [],
        "discovered_skills": [],
        "skipped_skills": [],
        "mcp_present": False,
    }

    skills = plugin_root / "skills"
    if skills.exists() or skills.is_symlink():
        try:
            resolved_skills = skills.resolve(strict=True)
        except FileNotFoundError:
            result["skills_component_errors"].append("skills fixed location does not resolve")
        else:
            if not resolved_skills.is_relative_to(resolved_root):
                result["skills_component_errors"].append("skills fixed location escapes plugin root")
            elif not resolved_skills.is_dir():
                result["skills_component_errors"].append("skills fixed location is not a directory")
            else:
                for child in skills.iterdir():
                    if not child.is_dir():
                        continue
                    skill_file = child / "SKILL.md"
                    if not (skill_file.exists() or skill_file.is_symlink()):
                        continue
                    try:
                        resolved_skill = skill_file.resolve(strict=True)
                    except FileNotFoundError:
                        result["skipped_skills"].append(child.name)
                        continue
                    if not resolved_skill.is_relative_to(resolved_root) or not resolved_skill.is_file():
                        result["skipped_skills"].append(child.name)
                        continue
                    result["discovered_skills"].append(child.name)

    mcp = plugin_root / "mcp.json"
    if mcp.exists() or mcp.is_symlink():
        try:
            resolved_mcp = mcp.resolve(strict=True)
        except FileNotFoundError:
            result["mcp_component_errors"].append("mcp.json fixed location does not resolve")
        else:
            if not resolved_mcp.is_relative_to(resolved_root):
                result["mcp_component_errors"].append("mcp.json fixed location escapes plugin root")
            elif not resolved_mcp.is_file():
                result["mcp_component_errors"].append("mcp.json fixed location is not a regular file")
            else:
                result["mcp_present"] = True

    return result


class PluginComponentDiscoveryTests(unittest.TestCase):
    def test_current_skill_only_package_discovers_exactly_svif_and_allows_missing_mcp(self) -> None:
        result = inspect_fixed_components(PLUGIN_ROOT)
        self.assertEqual(result["skills_component_errors"], [])
        self.assertEqual(result["mcp_component_errors"], [])
        self.assertEqual(result["discovered_skills"], ["svif"])
        self.assertEqual(result["skipped_skills"], [])
        self.assertFalse(result["mcp_present"])

    def test_skills_are_discovered_only_from_immediate_child_directories(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            plugin_root = Path(temporary) / "plugin"
            direct = plugin_root / "skills" / "direct"
            nested = plugin_root / "skills" / "group" / "nested"
            direct.mkdir(parents=True)
            nested.mkdir(parents=True)
            (direct / "SKILL.md").write_text("direct", encoding="utf-8")
            (nested / "SKILL.md").write_text("nested", encoding="utf-8")

            result = inspect_fixed_components(plugin_root)
            self.assertEqual(result["discovered_skills"], ["direct"])
            self.assertNotIn("nested", result["discovered_skills"])

    def test_wrong_kind_mcp_location_invalidates_only_mcp_component(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            plugin_root = Path(temporary) / "plugin"
            skill_dir = plugin_root / "skills" / "svif"
            skill_dir.mkdir(parents=True)
            (skill_dir / "SKILL.md").write_text("skill", encoding="utf-8")
            (plugin_root / "mcp.json").mkdir()

            result = inspect_fixed_components(plugin_root)
            self.assertEqual(result["discovered_skills"], ["svif"])
            self.assertTrue(any("not a regular file" in error for error in result["mcp_component_errors"]))

    def test_escaping_mcp_location_invalidates_only_mcp_component(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            plugin_root = base / "plugin"
            skill_dir = plugin_root / "skills" / "svif"
            skill_dir.mkdir(parents=True)
            (skill_dir / "SKILL.md").write_text("skill", encoding="utf-8")
            outside = base / "outside-mcp.json"
            outside.write_text("{}", encoding="utf-8")
            (plugin_root / "mcp.json").symlink_to(outside)

            result = inspect_fixed_components(plugin_root)
            self.assertEqual(result["discovered_skills"], ["svif"])
            self.assertTrue(any("escapes plugin root" in error for error in result["mcp_component_errors"]))
            self.assertFalse(result["mcp_present"])

    def test_missing_fixed_component_locations_are_not_errors(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            plugin_root = Path(temporary) / "plugin"
            plugin_root.mkdir()

            result = inspect_fixed_components(plugin_root)
            self.assertEqual(result["skills_component_errors"], [])
            self.assertEqual(result["mcp_component_errors"], [])
            self.assertEqual(result["discovered_skills"], [])
            self.assertFalse(result["mcp_present"])


if __name__ == "__main__":
    unittest.main()
