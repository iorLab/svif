# Svif Plugin

This directory is the installable Svif Plugin package.

It targets the portable **Agent Plugins 1.0.0** package format and intentionally starts with a Skill-only MVP:

```text
plugin/
├── plugin.json
└── skills/
    └── svif/
        └── SKILL.md
```

A Skill-only Plugin is useful immediately and does not require an MCP server to be structurally valid. MCP packaging can be added later without changing the Svif product kernel or the durable Project-continuity model.

## What this MVP does

The bundled `svif` Skill teaches a compatible execution surface to:

- discover Project-owned Agnir continuity before acting;
- load current state, next actions, decisions, and relevant evidence;
- execute the Svif lifecycle rather than merely describe it;
- preserve exact-subject verification and provenance across external effects;
- keep protected authority outside untrusted model/result payloads;
- independently observe external effects before checkpointing success;
- checkpoint durable Project truth so a fresh executor can resume.

The Plugin is a distribution layer. It does not reimplement `src/svif/runtime.py` and it does not make ChatGPT or another plugin client authoritative Project memory.

## Install / test

Use the `plugin/` directory as the plugin root in an Agent Plugins 1.0 compatible client.

For ChatGPT environments that expose Skill upload before full custom Plugin packaging, the contained `skills/svif/SKILL.md` can also be tested directly as a Skill. This is the same workflow component shipped by the Plugin; it is not a separate product architecture.

A useful first smoke test is:

> Continue this Svif Project and implement the next concrete action. Use the Project's canonical durable state and checkpoint when finished.

Expected behavior: the executor discovers Agnir first, loads the current Svif state, performs actionable repository work with verification, and persists a resumable checkpoint rather than relying on conversation memory.

## Next packaging increment

Add an optional `mcp.json` only when the remote Svif MCP/App surface is ready to expose concrete `begin` / `complete` tools. The MCP component must reuse the existing Orchestrator and ChatGPT execution bridge and must preserve trusted authority outside model-controlled payloads.
