# Svif Plugin

This directory is the portable Svif Plugin package.

It targets **Agent Plugins 1.0.0** and intentionally starts with a Skill-only MVP. The repository now also carries an additive OpenAI/Codex distribution manifest without replacing the portable package contract:

```text
svif/
├── .agents/plugins/marketplace.json
└── plugin/
    ├── plugin.json
    ├── .codex-plugin/plugin.json
    └── skills/
        └── svif/
            └── SKILL.md
```

`plugin/plugin.json` remains the Agent Plugins 1.0 portable manifest. `plugin/.codex-plugin/plugin.json` is product-specific distribution metadata used by current Codex/OpenAI marketplace flows and points at the same `skills/` component. Neither file is allowed to introduce a second Orchestrator or a second continuity source of truth.

A Skill-only Plugin is structurally useful without an MCP server. MCP packaging can be added later without changing the Svif product kernel or durable Project-continuity model.

## Current validation status

Repository CI validates the portable package structure, Agent Plugins 1.0.0 manifest constraints used by this package, the specification's normative manifest failure semantics, Agent Skills frontmatter/guardrails, Plugin-root filesystem containment and its required failure-isolation boundaries, fixed component discovery semantics for both `skills/` and the currently absent `mcp.json`, Agnir pre-load compatibility/identity discovery guards, installation-documentation guardrails, the OpenAI/Codex GitHub-marketplace distribution mapping, and the boundary that prevents the Plugin from shadowing the Svif runtime.

The OpenAI-specific distribution test verifies that `.agents/plugins/marketplace.json` resolves the local `./plugin` root, that `.codex-plugin/plugin.json` reuses `./skills/`, and that identity metadata shared with the portable manifest remains synchronized. This is a repository-side distribution invariant; it does not prove that a workspace import actually succeeded.

The portable manifest test deliberately follows the Agent Plugins 1.0 specification text where it defines non-fatal exceptions to the closed schema: unknown top-level fields are reported and ignored, and a non-object `extensions` field is reported and ignored. A portable validator also does not validate values inside unimplemented client-extension namespaces. Other invalid permitted manifest fields remain fatal. This prevents Svif's package tests from being stricter than a conformant Agent Plugins client in ways that would reject a package the normative specification says to continue loading.

Filesystem containment is modeled at the specification's narrow failure boundaries rather than as one all-or-nothing package check: an escaping root `plugin.json` rejects the Plugin; an invalid or escaping fixed `skills/` location invalidates only that component type; an escaping discovered `SKILL.md` skips only that Skill; and unrelated escaping package paths are denied without falsely turning those narrower failures into whole-Plugin rejection.

Fixed-location discovery is checked separately. Skills are discovered only from immediate child directories of `skills/` that contain a regular `SKILL.md`; nested descendants are not recursively promoted to Skills. Missing fixed locations are valid absence. The root `mcp.json` location is also modeled now even though this MVP intentionally does not ship it: if that path later exists with the wrong filesystem kind or escapes the Plugin root, only the MCP component is invalidated while independently valid Skills remain loadable. This locks the Agent Plugins v1 component-isolation rule before the remote MCP increment is introduced.

Agnir discovery is also guarded before durable memory is trusted. The Skill must validate Core compatibility, selected discovery profile, and selected-Project identity before resolving and loading the declared continuity locators. Unsupported compatibility and Project mismatch remain explicit discovery failures rather than triggers to search chat history, sibling repositories, parent/child Projects, or retired layouts for substitute state. For the current Svif binding the expected values are Core `0.1`, profile `repository-filesystem/0.1`, and Project identity `urn:svif:project:svif-core`; these are Project-binding facts, not universal Agnir constants.

That is **package/conformance/distribution validation**, not proof that a particular ChatGPT, Codex, or other compatible client has installed and exercised this exact revision. Repository success does not prove an OpenAI workspace import, directory listing, installation policy, invocation path, or Project exercise worked.

Agent Plugins 1.0 treats the portable Plugin as a directory rooted at one filesystem location; it does not define ZIP/TAR packaging as the portable package unit. Product-specific import, upload, GitHub marketplace publication, workspace administration, and invocation UX are separate from the portable conformance claim.

## What this MVP does

The bundled `svif` Skill guides a compatible execution surface to:

- follow the current Agnir activation route: `AGENTS.md -> README.md / Agnir Project Instructions -> AGNIR.yaml -> durable memory` when those surfaces exist;
- validate Agnir Core/profile compatibility and selected-Project identity before loading durable memory;
- surface unsupported-version, Project-mismatch, and broken-locator discovery failures instead of silently falling back to unrelated state;
- load current state and next actions first, then only relevant decisions/evidence;
- distinguish Agnir Core `0.1`, profile `repository-filesystem/0.1`, and repository release SemVer `0.1.0`;
- execute the Svif lifecycle rather than merely describe it;
- preserve exact-subject verification and provenance across external effects;
- keep protected authority outside untrusted model/result payloads;
- independently observe external effects before checkpointing success;
- write explicit, resumable Current State / Next Actions / Decisions / Evidence checkpoints;
- stop rather than invent Project state when activation/discovery fails.

The Plugin is a distribution/workflow layer. It does not reimplement `src/svif/runtime.py` and it does not make ChatGPT or another plugin client authoritative Project memory.

## Portable package exercise

For an Agent Plugins 1.0 implementation or local conformance harness, `plugin/` is the portable package root. This statement describes package layout only; it is not a universal installation instruction for ChatGPT or Codex.

A useful workflow request after a client has actually loaded the Plugin or contained Skill is:

> Continue this Svif Project and implement the next concrete action. Use the Project's canonical durable state and checkpoint when finished.

Expected behavior: the executor follows Project-owned Agnir activation/discovery, performs actionable repository work with verification, distinguishes package success from external-effect success, and persists a resumable checkpoint rather than relying on conversation memory.

## OpenAI GitHub marketplace distribution

OpenAI currently documents GitHub marketplace import for eligible workspaces. A workspace admin can import a repository containing `.agents/plugins/marketplace.json`; entries may point at plugin folders in the same repository. Svif now supplies exactly that repository-side path:

- marketplace repository: `https://github.com/iorLab/svif`;
- marketplace manifest: `.agents/plugins/marketplace.json`;
- marketplace source entry: local `./plugin`;
- Codex-specific plugin metadata: `plugin/.codex-plugin/plugin.json`;
- shared Skill implementation: `plugin/skills/svif/SKILL.md`.

For an eligible workspace, the documented product flow is **Workspace settings -> Plugins -> Add -> Import marketplace**, using the repository URL and `main` (or a fixed commit when revision pinning is desired). The import/sync service supplies plugin content from GitHub; workspace installation policy and any future app permissions remain separate controls.

This repository shape materially improves installability, but it still is **not client-installation evidence**. Until an actual workspace import report and subsequent Plugin invocation are observed for a specific commit, Svif must say only that the repository is prepared for the documented GitHub marketplace route.

## OpenAI client installation exercise

Current OpenAI product installation is client/surface dependent. The Plugin Directory is the primary public discovery route when a plugin is published there. For workspace/private distribution, the GitHub marketplace route above is now the preferred concrete Svif exercise because it maps directly to repository-owned artifacts rather than relying on an unspecified local-directory convention. Other local or Codex-specific plugins may still use import, upload, sharing, or administrator workflows exposed by their surface.

For a real supported-client exercise:

1. Identify the **exact client/surface** and workspace being tested and confirm Plugins plus GitHub marketplace import are available for the acting role.
2. In an eligible workspace, import `https://github.com/iorLab/svif` through **Workspace settings -> Plugins -> Add -> Import marketplace**. Use `main` for continuous sync or pin the exact commit under test.
3. Review the import report and confirm the `svif` entry resolved `./plugin` and exposed the shared Skill. Treat any import error as installation friction, not as a package-success override.
4. Configure the Plugin's workspace installation policy. GitHub import does not itself grant unrelated app/data permissions.
5. Invoke the installed Plugin in ChatGPT using an **@ mention** or the available `+` / More flow, or in a supported Codex task view through **Sources -> Use plugins**.
6. Run the workflow request above against a real Agnir-initialized Project and observe whether activation reaches `AGNIR.yaml`, validates the expected compatibility and Project identity, and only then reaches the declared durable memory without relying on private conversation state.
7. Record the **exact Plugin or Skill revision**, **marketplace import result**, **observed activation path**, **compatibility/identity checks**, **verification performed**, and **checkpoint result**, plus any client/workspace friction or failure.

Only that observed client exercise can establish installation evidence for the tested surface and revision. Repository package/conformance/distribution validation does not prove client installation.

## Next packaging increment

Add an optional `mcp.json` only when the remote Svif MCP/App surface is ready to expose concrete `begin` / `complete` tools. The MCP component must reuse the existing Orchestrator and ChatGPT execution bridge and must preserve trusted authority outside model-controlled payloads.
