# Svif Plugin

This directory is the portable Svif Plugin package.

It targets **Agent Plugins 1.0.0** and intentionally starts with a Skill-only MVP:

```text
plugin/
├── plugin.json
└── skills/
    └── svif/
        └── SKILL.md
```

A Skill-only Plugin is structurally useful without an MCP server. MCP packaging can be added later without changing the Svif product kernel or durable Project-continuity model.

## Current validation status

Repository CI validates the package structure, Agent Plugins 1.0.0 manifest constraints used by this package, the specification's normative manifest failure semantics, Agent Skills frontmatter/guardrails, Plugin-root filesystem containment and its required failure-isolation boundaries, fixed component discovery semantics for both `skills/` and the currently absent `mcp.json`, installation-documentation guardrails, and the boundary that prevents the Plugin from shadowing the Svif runtime.

The manifest test deliberately follows the Agent Plugins 1.0 specification text where it defines non-fatal exceptions to the closed schema: unknown top-level fields are reported and ignored, and a non-object `extensions` field is reported and ignored. A portable validator also does not validate values inside unimplemented client-extension namespaces. Other invalid permitted manifest fields remain fatal. This prevents Svif's package tests from being stricter than a conformant Agent Plugins client in ways that would reject a package the normative specification says to continue loading.

Filesystem containment is modeled at the specification's narrow failure boundaries rather than as one all-or-nothing package check: an escaping root `plugin.json` rejects the Plugin; an invalid or escaping fixed `skills/` location invalidates only that component type; an escaping discovered `SKILL.md` skips only that Skill; and unrelated escaping package paths are denied without falsely turning those narrower failures into whole-Plugin rejection.

Fixed-location discovery is checked separately. Skills are discovered only from immediate child directories of `skills/` that contain a regular `SKILL.md`; nested descendants are not recursively promoted to Skills. Missing fixed locations are valid absence. The root `mcp.json` location is also modeled now even though this MVP intentionally does not ship it: if that path later exists with the wrong filesystem kind or escapes the Plugin root, only the MCP component is invalidated while independently valid Skills remain loadable. This locks the Agent Plugins v1 component-isolation rule before the remote MCP increment is introduced.

That is **package/conformance validation**, not proof that a particular ChatGPT, Codex, or other compatible client has installed and exercised this exact package. Portable package success does not prove an OpenAI product installation path, directory listing, workspace policy, import flow, or invocation path worked for this revision.

Agent Plugins 1.0 treats the Plugin as a directory rooted at one filesystem location; it does not define ZIP/TAR packaging as the portable package unit. Product-specific import, upload, directory publication, workspace administration, and invocation UX are separate from the portable conformance claim.

## What this MVP does

The bundled `svif` Skill guides a compatible execution surface to:

- follow the current Agnir activation route: `AGENTS.md -> README.md / Agnir Project Instructions -> AGNIR.yaml -> durable memory` when those surfaces exist;
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

## OpenAI client installation exercise

Current OpenAI product installation is client/surface dependent. The primary public distribution route is the **Plugin Directory** when the plugin is available there. A local or Codex-specific plugin may instead need to be made available through an **import, upload, or administrator** workflow before it can be selected; therefore this repository does not claim one universal local-directory installation command.

For a real supported-client exercise:

1. Identify the **exact client/surface** being tested (for example ChatGPT web, ChatGPT desktop, ChatGPT Work, or a supported Codex task view) and confirm Plugins are available for the account/workspace.
2. Install/select the Plugin through the product-supported route available on that surface: Plugin Directory when published there, or the surface's supported import/upload/administrator path for a local or workspace-specific Plugin.
3. If the Plugin appears in ChatGPT, invoke it using the supported plugin controls such as an **@ mention** or the available `+` / More flow.
4. In a supported Codex task view, open **Sources**, choose the plugin option exposed by that client, then select the installed Plugin.
5. Run the workflow request above against a real Agnir-initialized Project and observe whether activation reaches `AGNIR.yaml` and the declared durable memory without relying on private conversation state.
6. Record the **exact Plugin or Skill revision**, **observed activation path**, **verification performed**, and **checkpoint result**, plus any client/workspace friction or failure.

Only that observed client exercise can establish installation evidence for the tested surface and revision. Repository package/conformance validation does not prove client installation.

## Next packaging increment

Add an optional `mcp.json` only when the remote Svif MCP/App surface is ready to expose concrete `begin` / `complete` tools. The MCP component must reuse the existing Orchestrator and ChatGPT execution bridge and must preserve trusted authority outside model-controlled payloads.
