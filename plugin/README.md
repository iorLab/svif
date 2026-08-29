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

Repository CI validates the portable package structure, Agent Plugins 1.0.0 manifest constraints used by this package, the specification's normative manifest failure semantics, Agent Skills frontmatter/guardrails, Plugin-root filesystem containment and its required failure-isolation boundaries, fixed component discovery semantics for both `skills/` and the currently absent `mcp.json`, Agnir pre-load compatibility/identity discovery guards, installation-documentation guardrails, the OpenAI/Codex repository-marketplace distribution mapping, and the boundary that prevents the Plugin from shadowing the Svif runtime.

The OpenAI-specific distribution test verifies that `.agents/plugins/marketplace.json` resolves the local `./plugin` root, that `.codex-plugin/plugin.json` reuses `./skills/`, and that identity metadata shared with the portable manifest remains synchronized. This is a repository-side distribution invariant; it does not prove that a client or workspace actually imported the marketplace, installed the Plugin, or invoked it.

The portable manifest test deliberately follows the Agent Plugins 1.0 specification text where it defines non-fatal exceptions to the closed schema: unknown top-level fields are reported and ignored, and a non-object `extensions` field is reported and ignored. A portable validator also does not validate values inside unimplemented client-extension namespaces. Other invalid permitted manifest fields remain fatal. This prevents Svif's package tests from being stricter than a conformant Agent Plugins client in ways that would reject a package the normative specification says to continue loading.

Filesystem containment is modeled at the specification's narrow failure boundaries rather than as one all-or-nothing package check: an escaping root `plugin.json` rejects the Plugin; an invalid or escaping fixed `skills/` location invalidates only that component type; an escaping discovered `SKILL.md` skips only that Skill; and unrelated escaping package paths are denied without falsely turning those narrower failures into whole-Plugin rejection.

Fixed-location discovery is checked separately. Skills are discovered only from immediate child directories of `skills/` that contain a regular `SKILL.md`; nested descendants are not recursively promoted to Skills. Missing fixed locations are valid absence. The root `mcp.json` location is also modeled now even though this MVP intentionally does not ship it: if that path later exists with the wrong filesystem kind or escapes the Plugin root, only the MCP component is invalidated while independently valid Skills remain loadable. This locks the Agent Plugins v1 component-isolation rule before the remote MCP increment is introduced.

Agnir discovery is also guarded before durable memory is trusted. The Skill must validate Core compatibility, selected discovery profile, and selected-Project identity before resolving and loading the declared continuity locators. Unsupported compatibility and Project mismatch remain explicit discovery failures rather than triggers to search chat history, sibling repositories, parent/child Projects, or retired layouts for substitute state. For the current Svif binding the expected values are Core `0.1`, profile `repository-filesystem/0.1`, and Project identity `urn:svif:project:svif-core`; these are Project-binding facts, not universal Agnir constants.

That is **package/conformance/distribution validation**, not proof that a particular ChatGPT, Codex, or other compatible client/workspace has installed and exercised this exact revision. Repository success does not prove a marketplace source was imported, that the Plugin appeared in a Plugins Directory, that installation succeeded, that invocation worked, or that a real Project exercise reached the expected checkpoint.

Agent Plugins 1.0 treats the portable Plugin as a directory rooted at one filesystem location; it does not define ZIP/TAR packaging as the portable package unit. Product-specific marketplace setup, installation, publication, workspace administration, and invocation UX are separate from the portable conformance claim.

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

## OpenAI repository marketplace distribution

OpenAI currently exposes two distinct repository-marketplace paths that can exercise the same `.agents/plugins/marketplace.json` source:

- **Workspace-managed import:** an eligible workspace admin/owner can use `Workspace settings > Plugins > Add > Import marketplace`, provide the repository URL, optionally select a branch/tag/commit, review Import results, and configure workspace installation/authentication policy.
- **Codex-local marketplace:** Codex can add and track the repository with `codex plugin marketplace add`, then expose the Plugin through its marketplace/plugin UI on supported surfaces.

Both paths consume the same repository distribution shape:

- repository: `https://github.com/iorLab/svif`;
- marketplace manifest: `.agents/plugins/marketplace.json`;
- marketplace source entry: local `./plugin` relative to the marketplace root;
- required OpenAI/Codex Plugin manifest: `plugin/.codex-plugin/plugin.json`;
- shared Skill implementation: `plugin/skills/svif/SKILL.md`.

The documented Codex CLI route is:

```text
codex plugin marketplace add iorLab/svif
```

For a revision-sensitive Codex-local exercise, use a ref explicitly, for example:

```text
codex plugin marketplace add iorLab/svif --ref main
```

A validation run that needs exact immutable provenance should record the resolved commit SHA even when `--ref main` is used. After adding the source, `codex plugin marketplace list` should show the marketplace Codex is considering and the root path it resolves from.

For a workspace-managed exercise, enter the repository URL only (`https://github.com/iorLab/svif`) as Source, leave Path empty because the marketplace manifest is at the repository root, and use the optional Branch/tag/commit field to pin the exact revision when immutable provenance matters. Review the saved Import results before treating the marketplace as usable.

Repository marketplace `policy` values are **not workspace authority**. OpenAI workspace import/sync does not apply repository policy values such as `AVAILABLE` or `ON_USE`; workspace settings control installation and authentication there. The policy block in this repository may still inform marketplace presentation/behavior on other supported surfaces, but it MUST NOT be interpreted as granting installation, authentication, app access, protected Svif authority, or execution permission inside a workspace.

This repository shape materially improves installability, but it still is **not client-installation evidence**. Until a supported surface actually imports/adds the marketplace, reports the Plugin as available, installs or enables it under the surface's real policy controls, and invokes the exact revision, Svif must say only that the repository is prepared for the documented repository marketplace routes.

## OpenAI client/workspace installation exercise

Current OpenAI product installation is client/surface dependent. Use the supported route actually available to the environment under test; do not substitute one surface's configuration semantics for another.

For a real supported-client/workspace exercise:

1. Identify the **exact client/surface** and role being tested and confirm repository marketplace import/add plus Plugin installation are available there.
2. Select the exact source revision. For workspace import, use the optional Branch/tag/commit field; for Codex-local use an explicit `--ref` when appropriate. Record the immutable commit SHA that the exercise actually resolves to.
3. Import/add the marketplace and record the **marketplace source result**: workspace Import results or `codex plugin marketplace list`, including source identity and any reported errors.
4. Apply the surface's real installation/authentication controls. For workspace import, configure these in Workspace settings because repository `policy` values do not override workspace policy. Confirm the Plugin is actually available/installed or enabled rather than inferring success from source import alone.
5. Invoke the installed Plugin on a real Agnir-initialized Project using the invocation affordance actually exposed by that surface.
6. Observe whether activation reaches `AGNIR.yaml`, validates the expected Core compatibility, profile, and Project identity, and only then resolves the declared durable memory without relying on private conversation state.
7. Execute a concrete Svif lifecycle action while preserving trusted authority outside model-controlled payloads, exact-subject verification for any external effect, and independent observation before claiming external success.
8. Record the **exact Plugin or Skill revision**, **marketplace source result**, **observed installation**, **observed activation path**, **compatibility/identity checks**, **verification performed**, and **checkpoint result**, plus any client/workspace friction or failure.

Only that observed client/workspace exercise can establish installation evidence for the tested surface and revision. Repository package/conformance/distribution validation does not prove client installation.

## Next packaging increment

Add MCP packaging only when the remote Svif MCP/App surface is ready to expose concrete `begin` / `complete` tools **and** the resulting product-surface restriction is intentional. Current OpenAI workspace import behavior can mark a Plugin **Desktop only** when it declares MCP servers via `mcp.json` or `.mcp.json`, including remote HTTPS servers. Therefore MCP is not merely an additive file-format step for this MVP: before adding it, verify on the target OpenAI surfaces whether losing ChatGPT web availability is acceptable, and record the observed availability consequence separately from package/conformance success.

Keep the two packaging layers explicit: under Agent Plugins 1.0, portable MCP configuration lives at the Plugin root as `mcp.json` and contains the `mcpServers` object; under the current OpenAI/Codex product manifest, bundled MCP configuration is a separate product-specific root `.mcp.json` component referenced by `.codex-plugin/plugin.json` through its `mcpServers` field. The OpenAI `.mcp.json` path is not a portable Agent Plugins replacement, and portable `mcp.json` must not be renamed or inlined into portable `plugin.json`. Both layers must reuse the existing Orchestrator and ChatGPT execution bridge and preserve trusted authority outside model-controlled payloads.
