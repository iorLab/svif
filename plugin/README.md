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

Repository CI validates the package structure, Agent Plugins 1.0.0 manifest constraints used by this package, Skill frontmatter/guardrails, and the boundary that prevents the Plugin from shadowing the Svif runtime.

That is **package/conformance validation**, not proof that a particular ChatGPT, Codex, or other compatible client has installed and exercised this exact package. Client installation validation remains pending until a supported client actually installs/loads the Plugin or contained Skill and the observed behavior is recorded.

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

## Portable smoke test

Use `plugin/` as the plugin root in a client that explicitly supports Agent Plugins 1.0.0, or load `skills/svif/SKILL.md` in a surface that supports compatible Agent Skills.

A useful smoke-test request is:

> Continue this Svif Project and implement the next concrete action. Use the Project's canonical durable state and checkpoint when finished.

Expected behavior: the executor follows Project-owned Agnir activation/discovery, performs actionable repository work with verification, distinguishes package success from external-effect success, and persists a resumable checkpoint rather than relying on conversation memory.

Record the client/surface, package or Skill revision, observed activation path, performed verification, and checkpoint result before calling the installation path validated.

## Next packaging increment

Add an optional `mcp.json` only when the remote Svif MCP/App surface is ready to expose concrete `begin` / `complete` tools. The MCP component must reuse the existing Orchestrator and ChatGPT execution bridge and must preserve trusted authority outside model-controlled payloads.
