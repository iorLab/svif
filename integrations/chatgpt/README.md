# Svif ChatGPT Execution Surface

**Status:** execution bridge implemented; remote ChatGPT app/MCP packaging not yet implemented.

Svif treats ChatGPT as an **Execution Surface**, not as canonical Project memory and not as a synchronous LLM function hidden inside the Orchestrator.

## Current ChatGPT product surface

As of 2026-08-28, OpenAI's recommended custom ChatGPT app path is the Apps SDK built on Model Context Protocol (MCP). Custom apps can be tested through ChatGPT Developer Mode; write/modify actions have platform permission and confirmation boundaries.

Official references:

- https://help.openai.com/en/articles/12515353-build-with-the-apps-sdk
- https://help.openai.com/en/articles/12584461
- https://openai.com/policies/developer-apps-terms/

Svif's mature distribution target remains a **Plugin**. The ChatGPT app/MCP surface is the execution integration that a future Svif Plugin can package alongside other product components.

## Direction of control

ChatGPT apps are externally driven: ChatGPT calls app/MCP tools. Therefore the Svif kernel exposes a two-phase operation model rather than pretending that Svif can directly invoke ChatGPT and synchronously wait for a model result.

```text
ChatGPT / App
     |
     | begin tool
     v
Svif Orchestrator.begin()
     |
     v
OperationSession + durable Project context
     |
     | materialized to ChatGPT
     v
ChatGPT performs/reasons/uses tools
     |
     | complete tool with structured result
     v
ChatGPTExecutionSurface.parse_result()
     |
     v
Svif Orchestrator.complete()
     |
     +-> provenance / authority
     +-> optional Capability Provider
     +-> observation
     +-> Continuity Provider checkpoint
```

Synchronous surfaces such as a local driver may still use `Orchestrator.run()` when their integration exposes `execute()`.

## Implemented bridge

`src/svif/execution/chatgpt.py` provides `ChatGPTExecutionSurface`.

It currently:

- materializes Project identity, operation identity, intent, bound capability names, authority-class names, and loaded durable continuity into a JSON-serializable envelope;
- validates that returned Project/operation identity matches the active `OperationSession`;
- parses structured Evidence records, optional Capability requests, and provider-neutral `ContinuityUpdate` values;
- deliberately does **not** accept authority grants from the model result payload.

A trusted MCP/App wrapper must translate platform authorization/confirmation into the `authority_grants` argument of `Orchestrator.complete()`. The model cannot self-grant protected authority by emitting a field.

## Next packaging step

Implement a remote Apps SDK/MCP wrapper that exposes at minimum:

- a read/non-effectful begin/prepare operation action;
- a completion/action boundary that maps trusted platform authorization into Svif authority classes;
- clear tool metadata distinguishing read-only preparation from effectful completion paths.

That wrapper should reuse this bridge and Orchestrator rather than duplicate Project continuity, provenance, or authority logic.
