from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN_README = ROOT / "plugin" / "README.md"
ROOT_README = ROOT / "README.md"
ROOT_README_ZH = ROOT / "README.zh-CN.md"


class PluginInstallationDocumentationTests(unittest.TestCase):
    def test_openai_client_installation_is_not_presented_as_portable_directory_loading(self) -> None:
        text = PLUGIN_README.read_text(encoding="utf-8")

        self.assertIn("## OpenAI client installation exercise", text)
        self.assertIn("Plugin Directory", text)
        self.assertIn("@ mention", text)
        self.assertIn("package/conformance/distribution validation", text)
        self.assertIn("does not prove client installation", text)

        self.assertNotIn(
            "Use `plugin/` as the plugin root in a client that explicitly supports Agent Plugins 1.0.0",
            text,
        )

    def test_github_marketplace_route_matches_current_repo_marketplace_docs_without_overclaim(self) -> None:
        text = PLUGIN_README.read_text(encoding="utf-8")

        for marker in (
            "## OpenAI repository marketplace distribution",
            ".agents/plugins/marketplace.json",
            "plugin/.codex-plugin/plugin.json",
            "codex plugin marketplace add iorLab/svif",
            "codex plugin marketplace add iorLab/svif --ref",
            "ChatGPT desktop app",
            "Plugins Directory",
            "prepared for the documented repository marketplace route",
        ):
            self.assertIn(marker, text)

        self.assertIn("not client-installation evidence", text)
        self.assertIn("observed installation", text)
        self.assertNotIn("Workspace settings -> Plugins -> Add -> Import marketplace", text)

    def test_installation_validation_requires_observed_client_evidence(self) -> None:
        text = PLUGIN_README.read_text(encoding="utf-8")
        for marker in (
            "exact client/surface",
            "exact Plugin or Skill revision",
            "marketplace source result",
            "observed activation path",
            "verification performed",
            "checkpoint result",
        ):
            self.assertIn(marker, text)

    def test_root_readmes_do_not_overclaim_real_client_validation(self) -> None:
        english = ROOT_README.read_text(encoding="utf-8")
        chinese = ROOT_README_ZH.read_text(encoding="utf-8")

        self.assertIn(
            "no ChatGPT or Codex client installation has yet been recorded as validated evidence",
            english,
        )
        self.assertIn("真实 ChatGPT/Codex installation evidence 仍待补齐", chinese)

        for forbidden in (
            "The Plugin can be tested immediately in compatible clients.",
            "Skill-only Plugin 本身就可以立即安装、测试、迭代",
            "可安装、可马上开始真实测试的 Skill-first Plugin MVP",
        ):
            self.assertNotIn(forbidden, english + chinese)

    def test_installation_validation_requires_real_surface_observation_in_both_entry_points(self) -> None:
        english = ROOT_README.read_text(encoding="utf-8")
        chinese = ROOT_README_ZH.read_text(encoding="utf-8")

        for marker in (
            "actual supported",
            "exact surface/revision",
            "observed Agnir activation/verification/checkpoint evidence",
        ):
            self.assertIn(marker, english)

        for marker in (
            "真实受支持客户端",
            "Agnir activation",
            "verification",
            "checkpoint",
            "evidence",
            "记录",
        ):
            self.assertIn(marker, chinese)

    def test_installation_documentation_test_is_registered_in_project_binding(self) -> None:
        svif = (ROOT / "SVIF.yaml").read_text(encoding="utf-8")
        self.assertIn(
            'plugin_installation_docs: "tests/test_plugin_installation_docs.py"',
            svif,
        )


if __name__ == "__main__":
    unittest.main()
