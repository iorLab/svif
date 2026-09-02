from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN_README = ROOT / "plugin" / "README.md"
ROOT_README = ROOT / "README.md"
ROOT_README_ZH = ROOT / "README.zh-CN.md"
SKILL = ROOT / "plugin" / "skills" / "svif" / "SKILL.md"
NEXT_ACTIONS = ROOT / ".agnir" / "next-actions.md"
INSTALL_PROMPT = "Install and enable Svif for this Project: https://github.com/iorLab/svif"
PREVIEW_VERSION = "v0.2.0-preview.1"


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

    def test_repository_preview_uses_short_intent_and_immutable_release_ref(self) -> None:
        plugin = PLUGIN_README.read_text(encoding="utf-8")
        english = ROOT_README.read_text(encoding="utf-8")
        chinese = ROOT_README_ZH.read_text(encoding="utf-8")

        for marker in (
            "## Repository Preview self-distribution",
            "Codex CLI",
            "ChatGPT desktop/Codex",
            INSTALL_PROMPT,
            PREVIEW_VERSION,
            ".agents/plugins/marketplace.json",
            "plugin/.codex-plugin/plugin.json",
            "codex plugin marketplace add iorLab/svif --ref v0.2.0-preview.1",
            "Never silently substitute moving `main`",
            "report the unsupported surface",
            "do not claim installation succeeded",
            "codex plugin marketplace add iorLab/svif --ref main",
            "moving development ref",
            "comparison evidence",
        ):
            self.assertIn(marker, plugin)

        for readme in (english, chinese):
            self.assertIn(INSTALL_PROMPT, readme)
            self.assertIn(PREVIEW_VERSION, readme)

        self.assertNotIn("--ref main", INSTALL_PROMPT)
        self.assertNotIn(PREVIEW_VERSION, INSTALL_PROMPT)

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
            "### Personal ChatGPT distribution status",
            "Svif is not publicly listed yet",
            "personal ChatGPT Web",
            "Repository Preview",
            "Codex CLI",
            "ChatGPT desktop/Codex",
        ):
            self.assertIn(marker, english)

        for marker in (
            "### 个人 ChatGPT 分发状态",
            "Svif 目前还没有公开上架",
            "个人 ChatGPT Web",
            "Repository Preview",
            "Codex CLI",
            "ChatGPT 桌面版/Codex",
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

    def test_durable_next_actions_sequence_preview_before_public_submission(self) -> None:
        text = NEXT_ACTIONS.read_text(encoding="utf-8")

        for marker in (
            "v0.2.0-preview.1",
            "Codex CLI",
            "ChatGPT desktop/Codex",
            "immutable candidate",
            "public/personal ChatGPT path",
            "universal Plugins Directory",
            "ChatGPT Web",
            "individual-user ChatGPT surface",
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
