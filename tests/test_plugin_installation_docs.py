from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN_README = ROOT / "plugin" / "README.md"


class PluginInstallationDocumentationTests(unittest.TestCase):
    def test_openai_client_installation_is_not_presented_as_portable_directory_loading(self) -> None:
        text = PLUGIN_README.read_text(encoding="utf-8")

        self.assertIn("## OpenAI client installation exercise", text)
        self.assertIn("Plugin Directory", text)
        self.assertIn("import, upload, or administrator", text)
        self.assertIn("@ mention", text)
        self.assertIn("Sources", text)
        self.assertIn("package/conformance validation", text)
        self.assertIn("does not prove", text)

        self.assertNotIn(
            "Use `plugin/` as the plugin root in a client that explicitly supports Agent Plugins 1.0.0",
            text,
        )

    def test_installation_validation_requires_observed_client_evidence(self) -> None:
        text = PLUGIN_README.read_text(encoding="utf-8")
        for marker in (
            "exact client/surface",
            "exact Plugin or Skill revision",
            "observed activation path",
            "verification performed",
            "checkpoint result",
        ):
            self.assertIn(marker, text)

    def test_installation_documentation_test_is_registered_in_project_binding(self) -> None:
        svif = (ROOT / "SVIF.yaml").read_text(encoding="utf-8")
        self.assertIn(
            'plugin_installation_docs: "tests/test_plugin_installation_docs.py"',
            svif,
        )


if __name__ == "__main__":
    unittest.main()
