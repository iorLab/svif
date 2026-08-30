from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "plugin" / "skills" / "svif" / "SKILL.md"


class PluginAgnirDiscoveryTests(unittest.TestCase):
    def test_skill_requires_durable_agent_activation_route_before_discovery(self) -> None:
        text = SKILL.read_text(encoding="utf-8")

        mandatory = text.index("the durable activation route is mandatory before normal Project work")
        activation = text.index("Agnir Agent activation and Core discovery are distinct layers")
        route = text.index("durable `AGENTS.md -> README.md / Agnir Project Instructions -> AGNIR.yaml` route")
        contract = text.index("Do not validate activation by heading/link presence alone")
        direct = text.index("current Agent can directly open `AGNIR.yaml`")
        non_agent = text.index("A non-Agent Executor or trusted adapter")
        root_selection = text.index("select exactly one Project root")

        self.assertLess(mandatory, activation)
        self.assertLess(activation, route)
        self.assertLess(route, direct)
        self.assertLess(direct, contract)
        self.assertLess(contract, non_agent)
        self.assertLess(non_agent, root_selection)
        self.assertNotIn("when those surfaces exist", text)
        for marker in (
            "part of the Project activation contract, not as an optional convenience",
            "points to the canonical README Agnir section",
            "unresolved material instruction conflict",
            "MUST NOT be used to bypass a missing, stale, contradictory, or predecessor-private activation route",
            "fresh Agent can resume from the Project root",
            "does not silently convert this Agent Skill into a non-Agent activation context",
            "surface the activation blocker",
            "accidental direct readability of `AGNIR.yaml`",
        ):
            self.assertIn(marker, text)

    def test_skill_validates_canonical_readme_activation_contract_not_only_locator_shape(self) -> None:
        text = SKILL.read_text(encoding="utf-8")

        contract = text.index("Do not validate activation by heading/link presence alone")
        non_agent = text.index("A non-Agent Executor or trusted adapter")
        self.assertLess(contract, non_agent)

        for marker in (
            "canonical README `## Agnir Project Instructions` section itself MUST satisfy the current profile activation contract",
            "Project uses Agnir for durable continuity",
            "Project root as the authorized Project Entry Point",
            "read top-level `AGNIR.yaml`",
            "load Current State and Next Actions",
            "load Decisions and Evidence when relevant",
            "prefer durable Agnir Project truth over chat/private Agent memory",
            "newer Principal instruction",
            "directly observed current Project fact",
            "checkpoint material continuity changes at an intentional save/finish boundary",
            "missing, materially weakened, or contradicted",
            "activation is not healthy even when `AGENTS.md` reaches the correct heading",
            "rerun activation from the Project root",
        ):
            self.assertIn(marker, text)

    def test_skill_requires_authority_to_select_one_project_root_before_discovery(self) -> None:
        text = SKILL.read_text(encoding="utf-8")

        root_selection = text.index("select exactly one Project root")
        ambiguity = text.index("AGNIR_DISCOVERY_AMBIGUOUS")
        manifest = text.index("When `AGNIR.yaml` is available")

        self.assertLess(root_selection, ambiguity)
        self.assertLess(ambiguity, manifest)
        self.assertIn(
            "a parent or child Project with its own `AGNIR.yaml` does not make that selected root ambiguous",
            text,
        )
        self.assertIn(
            "MUST NOT be searched as a replacement",
            text,
        )

    def test_skill_selects_trusted_profile_before_resolving_discovery_record(self) -> None:
        text = SKILL.read_text(encoding="utf-8")

        root_selection = text.index("select exactly one Project root")
        profile_selection = text.index("select the discovery profile/adapter convention")
        trusted_context = text.index("trusted integration or binding context")
        record = text.index("resolve exactly one authoritative Discovery Record")
        profile_validation = text.index("validate `agnir.discovery_profile`")

        self.assertLess(root_selection, profile_selection)
        self.assertLess(profile_selection, trusted_context)
        self.assertLess(trusted_context, record)
        self.assertLess(record, profile_validation)
        self.assertIn(
            "MUST NOT bootstrap authority by choosing the adapter/convention used to discover or interpret itself",
            text,
        )
        self.assertIn("against the already selected discovery profile", text)

    def test_skill_resolves_one_record_and_detects_chain_conflicts_before_compatibility(self) -> None:
        text = SKILL.read_text(encoding="utf-8")

        record = text.index("resolve exactly one authoritative Discovery Record")
        not_found = text.index("AGNIR_DISCOVERY_NOT_FOUND")
        chain_checks = text.index("Detect Locator Chain cycles and conflicting candidate records")
        compatibility = text.index("validate `agnir.version`")

        self.assertLess(record, not_found)
        self.assertLess(not_found, chain_checks)
        self.assertLess(chain_checks, compatibility)

    def test_skill_validates_compatibility_and_identity_before_loading_memory(self) -> None:
        text = SKILL.read_text(encoding="utf-8")

        compatibility = text.index("validate `agnir.version`")
        profile = text.index("validate `agnir.discovery_profile`")
        identity = text.index("verify that `project.identity`")
        locator = text.index("resolve the required memory locators")
        load = text.index("After validation, treat the Project-managed Agnir state")

        self.assertLess(compatibility, profile)
        self.assertLess(profile, identity)
        self.assertLess(identity, locator)
        self.assertLess(locator, load)

    def test_skill_confines_relative_locators_to_selected_root_unless_external_binding_is_authorized(self) -> None:
        text = SKILL.read_text(encoding="utf-8")

        identity = text.index("verify that `project.identity`")
        locator = text.index("resolve the required memory locators")
        confinement = text.index("relative memory locators remain scoped to the selected Project root")
        external = text.index("explicit durable authorized binding/Locator Chain")
        load = text.index("After validation, treat the Project-managed Agnir state")

        self.assertLess(identity, locator)
        self.assertLess(locator, confinement)
        self.assertLess(confinement, external)
        self.assertLess(external, load)
        self.assertIn("symlink or other indirection outside that root", text)
        self.assertIn("MUST NOT become an implicitly authorized external Locator Chain", text)
        self.assertIn("merely because the target is readable", text)
        self.assertIn("AGNIR_DISCOVERY_UNAUTHORIZED", text)

    def test_skill_rejects_ephemeral_environment_values_as_locator_authority(self) -> None:
        text = SKILL.read_text(encoding="utf-8")

        external = text.index("explicit durable authorized binding/Locator Chain")
        environment = text.index("environment binding only when that binding is stable and durably associated with the selected Project")
        fresh_executor = text.index("how a fresh Executor can recover the same locator")
        load = text.index("After validation, treat the Project-managed Agnir state")

        self.assertLess(external, environment)
        self.assertLess(environment, fresh_executor)
        self.assertLess(fresh_executor, load)
        for marker in (
            "current process environment",
            "temporary workspace metadata",
            "prior conversation",
            "private model memory",
            "prompt-provided secret",
            "without predecessor-private context",
            "MUST NOT become continuity authority",
            "applicable discovery failure",
            "ephemeral successful resolution",
        ):
            self.assertIn(marker, text)

    def test_skill_respects_declared_canonical_repository_and_authoritative_ref_for_checkpointing(self) -> None:
        text = SKILL.read_text(encoding="utf-8")
        agnir = (ROOT / "AGNIR.yaml").read_text(encoding="utf-8")

        self.assertIn("canonical: \"iorLab/svif\"", agnir)
        self.assertIn("authoritative_ref: \"main\"", agnir)

        repository_binding = text.index("extensions.agnir/repository.canonical")
        checkpoint_guard = text.index("Before a state-dependent write or checkpoint")
        non_authoritative = text.index("detached commit, pull-request checkout, temporary branch, fork, mirror")
        reconcile = text.index("Reconcile accepted changes back to the declared authoritative ref")

        self.assertLess(repository_binding, checkpoint_guard)
        self.assertLess(checkpoint_guard, non_authoritative)
        self.assertLess(non_authoritative, reconcile)
        self.assertIn("MUST NOT silently become the canonical continuity write target", text)
        self.assertIn("leave the canonical checkpoint unchanged", text)
        self.assertIn("Package revision identity and target-Project authoritative-ref identity are separate facts", text)

    def test_skill_preserves_agnir_truth_reconciliation_precedence_without_granting_authority(self) -> None:
        text = SKILL.read_text(encoding="utf-8")

        observed = text.index("directly observed current Project or relevant external-system state first")
        principal = text.index("explicit current Principal instruction or policy second")
        durable = text.index("current durable Agnir state third")
        evidence = text.index("older checkpoint/evidence fourth")
        private = text.index("Executor-private context last")

        self.assertLess(observed, principal)
        self.assertLess(principal, durable)
        self.assertLess(durable, evidence)
        self.assertLess(evidence, private)
        self.assertIn("Material unresolved uncertainty must be surfaced rather than guessed", text)
        self.assertIn(
            "must be reconciled back into the Project-owned checkpoint instead of remaining only in transient execution context",
            text,
        )
        self.assertIn("does not grant protected execution authority", text)
        self.assertIn("trusted integration boundary", text)
        self.assertIn("exact-subject verification", text)
        self.assertIn("independent post-effect observation", text)

    def test_skill_verifies_post_checkpoint_cold_start_resumability(self) -> None:
        text = SKILL.read_text(encoding="utf-8")

        checkpoint = text.index("## 6. Checkpoint durable truth")
        reread = text.index("re-read the durable state needed", checkpoint)
        cold_start = text.index("cold-start discoverable from the original authorized Project Entry Point", checkpoint)
        reresolve = text.index("re-resolve the Discovery Record and Locator Chain", checkpoint)
        full_rerun = text.index("rerun the full cold-start discovery path", checkpoint)
        no_claim = text.index("A checkpoint MUST NOT claim resumability", checkpoint)

        self.assertLess(reread, cold_start)
        self.assertLess(cold_start, reresolve)
        self.assertLess(reresolve, full_rerun)
        self.assertLess(full_rerun, no_claim)
        self.assertIn("required Current State and Next Actions can be loaded without Executor-private context", text)
        self.assertIn("changed the Discovery Record, required memory locators, durable repository/ref binding", text)
        for marker in (
            "missing",
            "stale",
            "ambiguous",
            "cyclic",
            "unauthorized",
            "inconsistent",
            "otherwise unresolved",
        ):
            self.assertIn(marker, text[no_claim : no_claim + 300])

    def test_skill_surfaces_all_named_agnir_discovery_failures_without_fallback_search(self) -> None:
        text = SKILL.read_text(encoding="utf-8")

        for marker in (
            "AGNIR_DISCOVERY_NOT_FOUND",
            "AGNIR_DISCOVERY_AMBIGUOUS",
            "AGNIR_DISCOVERY_UNSUPPORTED_VERSION",
            "AGNIR_DISCOVERY_PROJECT_MISMATCH",
            "AGNIR_DISCOVERY_UNRESOLVABLE",
            "AGNIR_DISCOVERY_UNAUTHORIZED",
            "AGNIR_DISCOVERY_CYCLE",
            "AGNIR_DISCOVERY_STALE",
            "AGNIR_DISCOVERY_INCONSISTENT",
            "sibling repositories",
            "parent/child Projects",
            "chat history",
            "retired layouts",
        ):
            self.assertIn(marker, text)

        self.assertIn("repair the earliest violated discovery invariant", text)
        self.assertIn("original authorized Project Entry Point", text)

    def test_svif_binding_and_skill_agree_on_current_agnir_identity_and_compatibility(self) -> None:
        skill = SKILL.read_text(encoding="utf-8")
        agnir = (ROOT / "AGNIR.yaml").read_text(encoding="utf-8")
        svif = (ROOT / "SVIF.yaml").read_text(encoding="utf-8")

        self.assertIn('version: "0.1"', agnir)
        self.assertIn('discovery_profile: "repository-filesystem/0.1"', agnir)
        self.assertIn('identity: "urn:svif:project:svif-core"', agnir)
        self.assertIn('compatibility: "0.1"', svif)
        self.assertIn('profile: "repository-filesystem/0.1"', svif)

        for marker in (
            "Agnir Core `0.1`",
            "profile `repository-filesystem/0.1`",
            "Project identity `urn:svif:project:svif-core`",
        ):
            self.assertIn(marker, skill)

    def test_discovery_guard_test_is_registered_in_project_binding(self) -> None:
        svif = (ROOT / "SVIF.yaml").read_text(encoding="utf-8")
        self.assertIn(
            'plugin_agnir_discovery: "tests/test_plugin_agnir_discovery.py"',
            svif,
        )


if __name__ == "__main__":
    unittest.main()
