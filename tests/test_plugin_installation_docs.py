from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN_README = ROOT / "plugin" / "README.md"
ROOT_README = ROOT / "README.md"
ROOT_README_ZH = ROOT / "README.zh-CN.md"
SKILL = ROOT / "plugin" / "skills" / "svif" / "SKILL.md"
NEXT_ACTIONS = ROOT / ".agnir" / "next-actions.md"


class PluginInstallationDocumentationTests(unittest.TestCase):
    def test_personal_chatgpt_public_directory_is_primary_distribution_path(self) -> None:
        text = PLUGIN_README.read_text(encoding="utf-8")

        for marker in (
            "## Public personal-ChatGPT distribution",
            "individual/personal ChatGPT users",
            "universal Plugins Directory",
            "Skills only",
            "Apps Management: Write",
            "verified individual developer identity",
            "Create plugin -> Skills only",
            "Submit for review",
            "explicitly publish",
        ):
            self.assertIn(marker, text)

        self.assertIn(
            "not a managed-workspace GitHub marketplace import",
            text,
        )

    def test_public_submission_is_skills_only_without_mcp_or_apps_gate(self) -> None:
        text = PLUGIN_README.read_text(encoding="utf-8")
        manifest = (ROOT / "plugin" / ".codex-plugin" / "plugin.json").read_text(encoding="utf-8")

        for marker in (
            "does not need an MCP server",
            "MCP remains an optional future capability increment",
            "Do not add MCP merely as a prerequisite for public publication",
        ):
            self.assertIn(marker, text)

        self.assertNotIn('"mcpServers"', manifest)
        self.assertNotIn('"apps"', manifest)

    def test_public_listing_and_review_materials_are_documented(self) -> None:
        text = PLUGIN_README.read_text(encoding="utf-8")

        for marker in (
            "### Proposed public listing",
            "Durable project orchestration",
            "### Review test cases to enter in the submission portal",
            "five positive and three negative review cases",
            "Resume a valid Agnir Project",
            "Checkpoint a non-effectful repository change",
            "Repair a missing Agnir locator without destroying existing instructions",
            "Resume after a prior checkpoint",
            "Handle a verified external-effect fixture",
            "Missing/ambiguous Agnir discovery",
            "Project identity or compatibility mismatch",
            "External effect without trusted authority or independent observation",
        ):
            self.assertIn(marker, text)

    def test_plugin_readme_and_skill_keep_agent_activation_mandatory(self) -> None:
        readme = PLUGIN_README.read_text(encoding="utf-8")
        skill = SKILL.read_text(encoding="utf-8")

        for marker in (
            "Agent-operable Agnir Project",
            "repository-filesystem/0.1",
            "Project root -> AGENTS.md -> README.md / Agnir Project Instructions -> AGNIR.yaml -> durable memory",
            "before normal Project work",
        ):
            self.assertIn(marker, readme)

        self.assertIn("the durable activation route is mandatory before normal Project work", skill)
        self.assertIn("current Agent can directly open `AGNIR.yaml`", skill)

    def test_repository_marketplace_is_auxiliary_and_preserves_revision_caution(self) -> None:
        text = PLUGIN_README.read_text(encoding="utf-8")

        for marker in (
            "## OpenAI repository marketplace distribution",
            "auxiliary development, Codex, managed-workspace, and validation route",
            ".agents/plugins/marketplace.json",
            "plugin/.codex-plugin/plugin.json",
            "codex plugin marketplace add iorLab/svif",
            "codex plugin marketplace add iorLab/svif --ref main",
            "moving repository ref",
            "comparison evidence",
            "not proof of the exact installed revision",
        ):
            self.assertIn(marker, text)

    def test_personal_chatgpt_installation_requires_real_surface_observation(self) -> None:
        plugin = PLUGIN_README.read_text(encoding="utf-8")
        english = ROOT_README.read_text(encoding="utf-8")
        chinese = ROOT_README_ZH.read_text(encoding="utf-8")

        for marker in (
            "public universal Plugins Directory -> personal ChatGPT Web -> install Svif",
            "Only that observed exercise establishes the personal ChatGPT Web installation baseline",
            "exact surface",
            "observed installation state",
            "Agnir activation/discovery",
            "resulting durable checkpoint",
        ):
            self.assertIn(marker, plugin)

        for marker in (
            "### Personal ChatGPT",
            "Svif is not publicly listed yet",
            "personal ChatGPT Web",
            "actual supported surface",
            "exact surface/revision",
            "observed Agnir activation/verification/checkpoint evidence",
        ):
            self.assertIn(marker, english)

        for marker in (
            "### 个人 ChatGPT 用户",
            "Svif 目前还没有公开上架",
            "个人 ChatGPT Web",
            "真实受支持客户端",
            "Agnir activation",
            "verification",
            "checkpoint",
        ):
            self.assertIn(marker, chinese)

    def test_publication_and_installation_evidence_layers_are_not_conflated(self) -> None:
        text = PLUGIN_README.read_text(encoding="utf-8")

        for marker in (
            "Submission is not publication",
            "After OpenAI approves the Plugin, explicitly publish",
            "portal submission, automated skill scan, reviewer outcome, approval, publication, and real personal-ChatGPT installation",
            "Repository CI, marketplace import, public review approval, and directory publication are related but distinct evidence layers",
        ):
            self.assertIn(marker, text)

    def test_durable_next_action_targets_public_submission_not_workspace_import(self) -> None:
        text = NEXT_ACTIONS.read_text(encoding="utf-8")

        for marker in (
            "public/personal ChatGPT path",
            "universal Plugins Directory",
            "ChatGPT Web",
            "individual-user ChatGPT surface",
        ):
            self.assertIn(marker, text)

        self.assertNotIn(
            "Perform the first real supported-client/workspace installation exercise through the repository-backed OpenAI GitHub marketplace path",
            text,
        )

    def test_installation_documentation_test_is_registered_in_project_binding(self) -> None:
        svif = (ROOT / "SVIF.yaml").read_text(encoding="utf-8")
        self.assertIn(
            'plugin_installation_docs: "tests/test_plugin_installation_docs.py"',
            svif,
        )


if __name__ == "__main__":
    unittest.main()
