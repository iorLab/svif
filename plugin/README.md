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

The OpenAI-specific distribution test verifies that `.agents/plugins/marketplace.json` resolves the local `./plugin` root, that `.codex-plugin/plugin.json` reuses `./skills/`, and that identity metadata shared with the portable manifest remains synchronized. This is a repository-side distribution invariant; it does not prove that a client actually added the marketplace source, installed the Plugin, or invoked it.

The portable manifest test deliberately follows the Agent Plugins 1.0 specification text where it defines non-fatal exceptions to the closed schema: unknown top-level fields are reported and ignored, and a non-object `extensions` field is reported and ignored. A portable validator also does not validate values inside unimplemented client-extension namespaces. Other invalid permitted manifest fields remain fatal. This prevents Svif's package tests from being stricter than a conformant Agent Plugins client in ways that would reject a package the normative specification says to continue loading.

Filesystem containment is modeled at the specification's narrow failure boundaries rather than as one all-or-nothing package check: an escaping root `plugin.json` rejects the Plugin; an invalid or escaping fixed `skills/` location invalidates only that component type; an escaping discovered `SKILL.md` skips only that Skill; and unrelated escaping package paths are denied without falsely turning those narrower failures into whole-Plugin rejection.

Fixed-location discovery is checked separately. Skills are discovered only from immediate child directories of `skills/` that contain a regular `SKILL.md`; nested descendants are not recursively promoted to Skills. Missing fixed locations are valid absence. The root `mcp.json` location is also modeled now even though this MVP intentionally does not ship it: if that path later exists with the wrong filesystem kind or escapes the Plugin root, only the MCP component is invalidated while independently valid Skills remain loadable. This locks the Agent Plugins v1 component-isolation rule before the remote MCP increment is introduced.

Agnir discovery is also guarded before durable memory is trusted. The Skill must validate Core compatibility, selected discovery profile, and selected-Project identity before resolving and loading the declared continuity locators. Unsupported compatibility and Project mismatch remain explicit discovery failures rather than triggers to search chat history, sibling repositories, parent/child Projects, or retired layouts for substitute state. For the current Svif binding the expected values are Core `0.1`, profile `repository-filesystem/0.1`, and Project identity `urn:svif:project:svif-core`; these are Project-binding facts, not universal Agnir constants.

That is **package/conformance/distribution validation**, not proof that a particular ChatGPT, Codex, or other compatible client has installed and exercised this exact revision. Repository success does not prove a marketplace source was added, that the Plugin appeared in a Plugins Directory, that installation succeeded, that invocation worked, or that a real Project exercise reached the expected checkpoint.

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

OpenAI's current packaging documentation defines repository marketplaces as authoring, testing, and team-distribution sources separate from the universal public Plugins Directory. Svif carries the documented repo-scoped marketplace location and points it at the same Plugin root:

- repository: `https://github.com/iorLab/svif`;
- marketplace manifest: `.agents/plugins/marketplace.json`;
- marketplace source entry: local `./plugin` relative to the marketplace root;
- required OpenAI/Codex Plugin manifest: `plugin/.codex-plugin/plugin.json`;
- shared Skill implementation: `plugin/skills/svif/SKILL.md`.

The documented CLI route for adding the repository marketplace is:

```text
codex plugin marketplace add iorLab/svif
```

For a revision-sensitive exercise, use a ref explicitly, for example:

```text
codex plugin marketplace add iorLab/svif --ref main
```

A validation run that needs exact immutable provenance should record the resolved commit SHA even when `--ref main` is used. After adding the source, `codex plugin marketplace list` should show the marketplace Codex is considering and the root path it resolves from. The current OpenAI documentation then directs local Plugin installation/testing to the **ChatGPT desktop app**: restart the app, open the **Plugins Directory**, select the marketplace source, install `svif`, and test it in a new chat.

This repository shape materially improves installability, but it still is **not client-installation evidence**. Until the marketplace source is actually added, the Plugin is observed in a supported Plugins Directory, installation succeeds, and the exact revision is subsequently invoked, Svif must say only that the repository is prepared for the documented repository marketplace route.

## OpenAI client installation exercise

Current OpenAI product installation is client/surface dependent. The universal Plugins Directory is the public distribution surface once a Plugin is published. Repo and local marketplaces are separate development/team-distribution sources, and their availability varies by surface. For the current Svif MVP, the highest-value concrete exercise is therefore the documented repo marketplace flow above rather than an inferred workspace-import UI.

For a real supported-client exercise:

1. Identify the **exact client/surface** being tested and confirm repository marketplaces and Plugin installation are available there.
2. Add this repository as a marketplace source with `codex plugin marketplace add iorLab/svif`; for a controlled run, select and record the intended ref and resolved commit SHA.
3. Run `codex plugin marketplace list` and record the **marketplace source result**, including the resolved root/source identity. Treat source-resolution errors as installation friction, not as package-success overrides.
4. Restart the ChatGPT desktop app, open the **Plugins Directory**, select the Svif marketplace, and install `svif`. Confirm the installed Plugin exposes the shared `svif` Skill from the exact revision under test.
5. Invoke the installed Plugin on a real Agnir-initialized Project using the invocation affordance actually exposed by that surface; do not infer success from marketplace listing alone.
6. Observe whether activation reaches `AGNIR.yaml`, validates the expected Core compatibility, profile, and Project identity, and only then resolves the declared durable memory without relying on private conversation state.
7. Execute a concrete Svif lifecycle action while preserving trusted authority outside model-controlled payloads, exact-subject verification for any external effect, and independent observation before claiming external success.
8. Record the **exact Plugin or Skill revision**, **marketplace source result**, **observed installation**, **observed activation path**, **compatibility/identity checks**, **verification performed**, and **checkpoint result**, plus any client friction or failure.

Only that observed client exercise can establish installation evidence for the tested surface and revision. Repository package/conformance/distribution validation does not prove client installation.

## Next packaging increment

Add an optional `.mcp.json` / `mcpServers` component only when the remote Svif MCP/App surface is ready to expose concrete `begin` / `complete` tools. The MCP component must reuse the existing Orchestrator and ChatGPT execution bridge and must preserve trusted authority outside model-controlled payloads.
