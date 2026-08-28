# Svif

Svif is a **Project orchestration product** coordinating durable Project continuity, execution surfaces, and capability/effect providers.

> The Project persists; Executors and execution environments may change.

Founding/current bindings are Agnir (Continuity Provider), ChatGPT (Execution Surface), and Cloudflare (Capability / Effect Provider). They are integrations, not permanent kernel dependencies.

## Product architecture

The four first-class components are **Orchestrator**, **Continuity Provider**, **Execution Surface**, and **Capability Provider**. See `ARCHITECTURE.md`.

The internal lifecycle remains `DISCOVER -> PLAN -> CHANGE -> VERIFY -> DELIVER -> OBSERVE -> CHECKPOINT`, with `REPAIR` returning to the earliest violated invariant.

## Executable product foundation

```text
src/svif/runtime.py                 # Orchestrator kernel
src/svif/continuity/agnir.py        # Agnir repository/filesystem Continuity Provider
src/svif/execution/chatgpt.py       # ChatGPT structured Execution Surface bridge
integrations/chatgpt/               # current ChatGPT app/MCP packaging direction

tests/                              # runtime/provider/surface behavior
spec/                               # portable internal product contracts
profiles/                           # specializations
schemas/                            # reference machine-readable contracts
checks/                             # repository integrity
conformance/                        # portable contract conformance
```

Python is the current executable reference vehicle; it does not freeze the eventual Plugin technology stack.

## Orchestrator execution modes

Svif now supports two directions of control:

- synchronous surfaces use `Orchestrator.run()` and expose `execute()`;
- externally driven surfaces use `Orchestrator.begin()` to load/bind Project continuity and `Orchestrator.complete()` after the surface returns a structured result.

The second form exists specifically so ChatGPT Apps/MCP integration reflects the real platform direction: ChatGPT calls the app, rather than the Svif kernel pretending it can synchronously invoke ChatGPT as a function.

Trusted integration layers may supply authority grants to `complete()` after platform-mediated approval. Model/result payloads cannot self-grant protected authority.

## Agnir Continuity Provider

`src/svif/continuity/agnir.py` implements Agnir `repository-filesystem/0.1` for an authorized Project root. It validates Agnir version/profile and Project identity, resolves root-bound memory locators, preserves semantic discovery failures, loads state/next/decisions/evidence, checkpoints explicit durable-truth updates, writes operation evidence, and re-validates discovery after checkpoint.

This is a profile adapter; the generic Orchestrator remains Continuity-Provider-neutral.

## ChatGPT Execution Surface

`src/svif/execution/chatgpt.py` implements the first ChatGPT bridge. It materializes an `OperationSession` into a JSON-serializable Project context and validates a later structured ChatGPT result into `WorkResult`.

As of 2026-08-28, the current OpenAI custom ChatGPT app path is Apps SDK + MCP. The bridge deliberately has no OpenAI network client so platform packaging can evolve without duplicating Svif kernel semantics. `integrations/chatgpt/README.md` records the current packaging boundary.

The mature Svif distribution target remains an installable **Plugin**; the ChatGPT app/MCP integration is a surface that can be packaged by that product.

## Cloudflare

Cloudflare remains the founding external effect/delivery provider family. `iorLab/svif-cloudflare-reference` is the controlled executable reference/E2E pressure test. Reusable Cloudflare capability behavior should move under Svif ownership and be consumed/tested by the reference.

## Project binding

`SVIF.yaml` is the repository/filesystem serialization of `project-binding/0.2`. It binds this Project to Agnir `0.1`; execution and capability bindings remain intentionally empty for this repository itself.

## Checks

```bash
python checks/check_repository.py
python conformance/check_contracts.py
PYTHONPATH=src python -m unittest discover -s tests -v
```

Repository integrity, portable contracts, and runtime/integration behavior are distinct checks.

## Next

The generic kernel, Agnir provider, and ChatGPT bridge exist. The next major implementation is a Svif-owned Cloudflare Capability Provider, then a founding end-to-end Agnir + ChatGPT + Cloudflare scenario, followed by the remote Apps SDK/MCP packaging layer and broader non-founding neutrality evidence.
