from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PORTABLE_MANIFEST = ROOT / "plugin" / "plugin.json"
CODEX_MANIFEST = ROOT / "plugin" / ".codex-plugin" / "plugin.json"
MARKETPLACE = ROOT / ".agents" / "plugins" / "marketplace.json"


class PluginOpenAIDistributionTests(unittest.TestCase):
    def test_marketplace_exposes_local_svif_plugin_root(self) -> None:
        data = json.loads(MARKETPLACE.read_text(encoding="utf-8"))

        self.assertEqual(data["name"], "svif")
        self.assertEqual(data["interface"]["displayName"], "Svif")
        self.assertEqual(len(data["plugins"]), 1)

        entry = data["plugins"][0]
        self.assertEqual(entry["name"], "svif")
        self.assertEqual(entry["source"], {"source": "local", "path": "./plugin"})
        self.assertEqual(entry["category"], "Developer Tools")

    def test_codex_manifest_reuses_existing_skill_without_runtime_shadowing(self) -> None:
        data = json.loads(CODEX_MANIFEST.read_text(encoding="utf-8"))

        self.assertEqual(data["skills"], "./skills/")
        self.assertNotIn("mcpServers", data)
        self.assertNotIn("apps", data)
        self.assertFalse((ROOT / "plugin" / "src").exists())
        self.assertTrue((ROOT / "plugin" / "skills" / "svif" / "SKILL.md").is_file())

    def test_codex_interface_declares_workflow_capabilities_without_granting_authority(self) -> None:
        data = json.loads(CODEX_MANIFEST.read_text(encoding="utf-8"))
        interface = data["interface"]

        # The Skill necessarily reads Project-owned Agnir/Svif state before it can act,
        # and may write authorized Project changes/checkpoints. These are discoverability/UI
        # declarations only; protected authority remains enforced by the Svif lifecycle.
        self.assertEqual(interface["capabilities"], ["Interactive", "Read", "Write"])
        self.assertEqual(interface["category"], "Developer Tools")

    def test_codex_manifest_meets_public_directory_listing_limits(self) -> None:
        data = json.loads(CODEX_MANIFEST.read_text(encoding="utf-8"))
        interface = data["interface"]

        self.assertLessEqual(len(data["name"]), 64)
        self.assertRegex(data["name"], r"^[A-Za-z0-9][A-Za-z0-9_-]*$")
        self.assertLessEqual(len(interface["displayName"]), 30)
        self.assertLessEqual(len(interface["shortDescription"]), 30)
        self.assertLessEqual(len(interface["longDescription"]), 4000)
        self.assertLessEqual(len(interface["developerName"]), 80)
        self.assertIn(
            interface["category"],
            {
                "Productivity",
                "Creativity",
                "Developer Tools",
                "Business & Operations",
                "Data & Analytics",
                "Communication",
                "Education & Research",
                "Security",
                "Finance",
                "Healthcare",
                "Travel",
                "Entertainment",
                "Other",
            },
        )
        self.assertLessEqual(len(interface["capabilities"]), 20)
        self.assertLessEqual(len(interface["defaultPrompt"]), 3)
        for prompt in interface["defaultPrompt"]:
            self.assertLessEqual(len(prompt), 128)
            self.assertNotIn("@", prompt)

        # The current public target is deliberately Skills only. OpenAI public submission
        # supports that shape directly; adding app/MCP configuration would change the
        # submission type and surface requirements rather than merely enriching metadata.
        self.assertNotIn("mcpServers", data)
        self.assertNotIn("apps", data)
        self.assertNotIn("screenshots", interface)

    def test_codex_and_portable_manifests_keep_identity_metadata_in_sync(self) -> None:
        portable = json.loads(PORTABLE_MANIFEST.read_text(encoding="utf-8"))
        codex = json.loads(CODEX_MANIFEST.read_text(encoding="utf-8"))

        for field in ("name", "version", "description", "homepage", "repository", "keywords"):
            self.assertEqual(codex[field], portable[field], field)
        self.assertEqual(codex["author"], portable["author"])

    def test_distribution_files_are_registered_in_project_binding(self) -> None:
        svif = (ROOT / "SVIF.yaml").read_text(encoding="utf-8")
        self.assertIn('plugin_codex_manifest: "plugin/.codex-plugin/plugin.json"', svif)
        self.assertIn('plugin_openai_marketplace: ".agents/plugins/marketplace.json"', svif)
        self.assertIn(
            'plugin_openai_distribution: "tests/test_plugin_openai_distribution.py"',
            svif,
        )


if __name__ == "__main__":
    unittest.main()
