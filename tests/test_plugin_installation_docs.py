from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN_README = ROOT / "plugin" / "README.md"
ROOT_README = ROOT / "README.md"
ROOT_README_ZH = ROOT / "README.zh-CN.md"
SKILL = ROOT / "plugin" / "skills" / "svif" / "SKILL.md"


class PluginInstallationDocumentationTests(unittest.TestCase):
    def test_openai_client_installation_is_not_presented_as_portable_directory_loading(self) -> None:
        text = PLUGIN_README.read_text(encoding="utf-8")

        self.assertIn("## OpenAI client/workspace installation exercise", text)
        self.assertIn("package/conformance/distribution validation", text)
        self.assertIn("does not prove client installation", text)

        self.assertNotIn(
            "Use `plugin/` as the plugin root in a client that explicitly supports Agent Plugins 1.0.0",
            text,
        )

    def test_plugin_readme_and_skill_keep_agent_activation_mandatory(self) -> None:
        readme = PLUGIN_README.read_text(encoding="utf-8")
        skill = SKILL.read_text(encoding="utf-8")

        for text in (readme, skill):
            self.assertNotIn("when those surfaces exist", text)

        for marker in (
            "Agent-operable Agnir Project",
            "repository-filesystem/0.1",
            "Project root -> AGENTS.md -> README.md / Agnir Project Instructions -> AGNIR.yaml -> durable memory",
            "before normal Project work",
            "direct readability of `AGNIR.yaml` is not a substitute",
        ):
            self.assertIn(marker, readme)

        self.assertIn("the durable activation route is mandatory before normal Project work", skill)
        self.assertIn("current Agent can directly open `AGNIR.yaml`", skill)

    def test_repository_marketplace_docs_cover_both_current_openai_routes_without_overclaim(self) -> None:
        text = PLUGIN_README.read_text(encoding="utf-8")

        for marker in (
            "## OpenAI repository marketplace distribution",
            ".agents/plugins/marketplace.json",
            "plugin/.codex-plugin/plugin.json",
            "Workspace settings > Plugins > Add > Import marketplace",
            "codex plugin marketplace add iorLab/svif",
            "codex plugin marketplace add iorLab/svif --ref",
            "workspace Import results",
            "prepared for the documented repository marketplace routes",
        ):
            self.assertIn(marker, text)

        self.assertIn("not client-installation evidence", text)
        self.assertIn("observed installation", text)
        self.assertNotIn("rather than an inferred workspace-import UI", text)

    def test_workspace_import_does_not_treat_repository_policy_as_workspace_authority(self) -> None:
        text = PLUGIN_README.read_text(encoding="utf-8")

        for marker in (
            "Repository marketplace `policy` values are **not workspace authority**",
            "does not apply repository policy values such as `AVAILABLE` or `ON_USE`",
            "workspace settings control installation and authentication",
            "MUST NOT be interpreted as granting installation, authentication, app access, protected Svif authority, or execution permission",
        ):
            self.assertIn(marker, text)

    def test_workspace_installation_evidence_is_stable_against_marketplace_sync(self) -> None:
        text = PLUGIN_README.read_text(encoding="utf-8")

        for marker in (
            "sync automatically each day",
            "fixed commit remains at that revision",
            "prefer a **fixed commit**",
            "re-check the saved marketplace/sync result immediately before invocation",
            "Record the immutable commit SHA that the exercise actually invokes",
            "marketplace source result and sync status",
        ):
            self.assertIn(marker, text)

        self.assertIn(
            "do not attribute activation, verification, or checkpoint evidence to an earlier imported SHA",
            text,
        )

    def test_codex_directory_refresh_lag_is_not_misclassified_as_package_failure(self) -> None:
        text = PLUGIN_README.read_text(encoding="utf-8")

        for marker in (
            "directory propagation as a distinct observation",
            "can take up to **6 hours** to refresh",
            "record the elapsed propagation state",
            "re-check the directory rather than rewriting package metadata",
            "temporarily stale Codex directory",
        ):
            self.assertIn(marker, text)

    def test_installation_validation_requires_observed_client_or_workspace_evidence(self) -> None:
        text = PLUGIN_README.read_text(encoding="utf-8")
        for marker in (
            "exact client/surface",
            "exact Plugin or Skill revision",
            "marketplace source result",
            "observed activation path",
            "verification performed",
            "checkpoint result",
            "immutable commit SHA",
        ):
            self.assertIn(marker, text)

    def test_next_mcp_increment_keeps_portable_and_openai_paths_distinct(self) -> None:
        text = PLUGIN_README.read_text(encoding="utf-8")

        for marker in (
            "under Agent Plugins 1.0, portable MCP configuration lives at the Plugin root as `mcp.json`",
            "required `$schema` and `mcpServers` top-level fields",
            "https://agent-plugins.org/schemas/1.0.0/mcp.schema.json",
            "OpenAI/Codex product manifest",
            "product-specific root `.mcp.json` component",
            "`.codex-plugin/plugin.json` through its `mcpServers` field",
            "OpenAI `.mcp.json` path is not a portable Agent Plugins replacement",
            "portable `mcp.json` must not be renamed or inlined into portable `plugin.json`",
        ):
            self.assertIn(marker, text)

        self.assertNotIn("do not rename it to a client-native path", text)

    def test_next_mcp_increment_records_current_openai_surface_availability_risk(self) -> None:
        text = PLUGIN_README.read_text(encoding="utf-8")

        for marker in (
            "Desktop only",
            "declares MCP servers via `mcp.json` or `.mcp.json`",
            "including remote HTTPS servers",
            "losing ChatGPT web availability",
            "record the observed availability consequence separately from package/conformance success",
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
