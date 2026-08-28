---
name: svif
description: Operate software and technical Projects with durable Agnir continuity, explicit evidence, authority boundaries, verification, external-effect observation, and reliable checkpoint/resume behavior. Use for Project implementation, debugging, delivery, repository work, or continuation where the Project should remain resumable across executors and sessions.
---

# Svif Project Orchestration

Use Svif as an execution discipline for real Project work. Prefer completing concrete work through available tools over producing abstract plans when the task is actionable.

## 1. Discover the Project before acting

When a Project exposes `AGNIR.yaml`, read it first. Treat the Project-managed Agnir state as durable authority for current state, next actions, decisions, and referenced evidence. Do not treat chat history, an executor's private context, Git, GitHub, ChatGPT, or any other execution surface as canonical merely because work happened there.

When a Project exposes `SVIF.yaml`, read it after Agnir discovery and use it to understand the Project's Svif bindings and active product contracts.

If more than one Project is involved, keep each Project's durable state isolated. Cross-project decisions must be recorded from each affected Project's own perspective rather than merged into one mutable workspace memory.

## 2. Reconstruct only the context needed for the current operation

Load the current state and the next actions first. Read decisions and evidence that materially constrain the requested operation. Avoid pulling historical or retired artifacts back into active architecture unless the current Project explicitly declares them authoritative.

Use the Project's canonical repository or substrate when one is declared. For `iorLab/svif`, `main` is the active line and repository-managed Agnir state is canonical.

## 3. Execute through the Svif lifecycle

Use this lifecycle as the default control loop:

`DISCOVER -> PLAN -> CHANGE -> VERIFY -> DELIVER -> OBSERVE -> CHECKPOINT`

`REPAIR` returns to the earliest violated invariant.

For implementation tasks:

- make the smallest coherent set of changes that satisfies the intent;
- run or inspect the strongest available verification before claiming success;
- preserve stable subject identity across verification and any later effect;
- keep evidence inspectable enough that another executor can determine what actually happened.

## 4. Enforce provenance before external effects

Never treat a successful command, CI run, deployment request, or model statement as sufficient evidence by itself.

Before an external effect that depends on verification:

1. identify the exact subject to be affected;
2. require successful verification evidence for that same subject;
3. require the applicable authority or user approval through a trusted integration boundary;
4. actuate only the verified subject or an independently verified replacement;
5. independently observe the resulting external state;
6. reconcile subject and target identity before recording success.

Untrusted model/result payloads must never self-grant protected authority.

## 5. Keep execution surfaces replaceable

Agnir is the founding Continuity Provider for Svif, ChatGPT is a founding Execution Surface, and Cloudflare is a founding Capability Provider. They are bindings, not universal kernel dependencies.

Do not introduce an unnecessary dependency on ChatGPT, GitHub, Cloudflare, Git, or a local checkout when the Project can remain portable. Use the tools available in the current environment without redefining Project truth around those tools.

## 6. Checkpoint durable truth

Checkpoint after meaningful state transitions and whenever the user asks to checkpoint, save progress, stop, finish, or equivalent.

A checkpoint should preserve at least:

- what is now true;
- what remains to do;
- durable decisions made during the operation;
- evidence needed to justify important claims or recover the work;
- enough identity information for a fresh executor to resume without relying on private prior context.

Do not checkpoint a failed or uncertain external effect as successful. Record the uncertainty and the next repair action instead.

## 7. Svif repository development rules

When operating on `iorLab/svif` itself:

- read `AGNIR.yaml`, `.agnir/state.md`, `.agnir/next-actions.md`, `.agnir/decisions.md`, and relevant evidence before substantive changes;
- also read `SVIF.yaml` and relevant specifications;
- work directly on the active `main` line unless the Project state says otherwise;
- keep `README.md` and `README.zh-CN.md` synchronized when architecture, runtime flow, or documented repository structure changes;
- update `REPOSITORY_TREE.md` whenever tracked files are added, removed, moved, or materially change responsibility;
- run the repository integrity, contract, and runtime test layers before claiming the change is complete.

The Plugin/distribution layer must call into or guide the existing Svif product semantics. It must not reimplement the Orchestrator or move canonical Project truth out of the configured Continuity Provider.
