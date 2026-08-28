# Svif

Svif is a **Project orchestration product** coordinating durable Project continuity, execution surfaces, and capability providers.

> The Project persists; Executors and execution environments may change.

## Canonical repositories

Svif now uses a deliberately small repository topology:

- `iorLab/svif` — the complete Svif product: Orchestrator, integrations, capability providers, contracts, tests, and E2E fixtures;
- `iorLab/agnir` — the independent Agnir continuity protocol consumed by Svif.

There is no separate Cloudflare reference project in the active architecture. Cloudflare is a Svif Capability Provider and its reference/E2E material lives in this repository.

## Product architecture

The four first-class components are:

1. **Orchestrator** — cross-boundary coordination and invariants;
2. **Continuity Provider** — durable Project truth; founding provider: Agnir;
3. **Execution Surface** — where an Executor performs work; founding surface: ChatGPT;
4. **Capability Provider** — inspectable/effectful external capabilities; founding provider family: Cloudflare.

The internal lifecycle remains `DISCOVER -> PLAN -> CHANGE -> VERIFY -> DELIVER -> OBSERVE -> CHECKPOINT`, with `REPAIR` returning to the earliest violated invariant.

## Repository layout

```text
src/svif/runtime.py                    # Orchestrator kernel
src/svif/continuity/agnir.py           # Agnir Continuity Provider
src/svif/execution/chatgpt.py          # ChatGPT Execution Surface bridge
src/svif/capabilities/cloudflare.py    # Svif-owned Cloudflare Capability Provider

integrations/chatgpt/                  # ChatGPT app/MCP packaging boundary
integrations/cloudflare/               # Cloudflare provider descriptor and integration notes

tests/                                # runtime/provider/surface behavior
conformance/                          # portable contract conformance
spec/                                 # internal portable contracts
profiles/                             # specializations
schemas/                              # machine-readable contracts
history/                              # predecessor/retired-project evidence only
```

Python is the current executable reference vehicle; it does not freeze the eventual distribution technology.

## Current founding path

- Agnir repository/filesystem continuity adapter exists.
- ChatGPT structured execution bridge exists and supports externally driven `Orchestrator.begin()` / `Orchestrator.complete()` handoff.
- Cloudflare provider logic is now owned by Svif and is transport-injected so tests do not require live credentials.
- Protected authority remains outside untrusted model/result payloads.
- External success still requires exact verified-subject delivery plus independent observation before checkpoint.

## Project binding

`SVIF.yaml` is the repository/filesystem serialization of `project-binding/0.2` for this Project. It describes product-owned implementation artifacts while keeping execution and capability bindings replaceable.

## Checks

```bash
python checks/check_repository.py
python conformance/check_contracts.py
PYTHONPATH=src python -m unittest discover -s tests -v
```

## Next

The next milestone is one in-repository founding E2E scenario wiring Agnir + ChatGPT + Cloudflare through the Orchestrator. After that: ChatGPT packaging hardening, broader neutrality evidence, and release compatibility work.
