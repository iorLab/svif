---
name: svif
description: Operate software and technical Projects with durable Agnir continuity, explicit evidence, authority boundaries, verification, external-effect observation, and reliable checkpoint/resume behavior. Use for Project implementation, debugging, delivery, repository work, or continuation where the Project should remain resumable across executors and sessions.
---

# Svif Project Orchestration

Use Svif as an execution discipline for real Project work. Prefer completing concrete work through available tools over producing abstract plans when the task is actionable.

## 1. Discover and activate the Project before acting

For an Agnir-initialized repository/filesystem Project, follow the current Agnir activation route when those surfaces exist:

`Project root -> AGENTS.md -> README.md / Agnir Project Instructions -> AGNIR.yaml -> declared durable memory`

`AGENTS.md` is only a locator; the target Project README owns the full Agnir Project Instructions. Preserve unrelated existing `AGENTS.md` instructions and never silently override a material conflict.

Before following that route, require the authorized Project Entry Point or trusted binding context to select exactly one Project root. If multiple candidate Project roots exist and no authority rule selects one, surface `AGNIR_DISCOVERY_AMBIGUOUS` rather than choosing the most convenient candidate. Once one root is authoritatively selected, a parent or child Project with its own `AGNIR.yaml` does not make that selected root ambiguous and MUST NOT be searched as a replacement.

Before resolving a Discovery Record, select the discovery profile/adapter convention applicable to the authorized Project Entry Point from trusted integration or binding context. The Discovery Record may declare its profile for compatibility checking, but it MUST NOT bootstrap authority by choosing the adapter/convention used to discover or interpret itself. If no applicable profile can be selected safely, surface the discovery/compatibility blocker rather than guessing from nearby files or model memory.

Under the selected discovery convention, resolve exactly one authoritative Discovery Record before loading continuity. If no Discovery Record can be resolved, surface `AGNIR_DISCOVERY_NOT_FOUND`. Detect Locator Chain cycles and conflicting candidate records before compatibility or identity validation rather than following a cycle, guessing among conflicting records, or silently adopting another candidate.

When `AGNIR.yaml` is available, read it before substantive work. Before loading any declared durable memory:

1. validate `agnir.version` against the Agnir Core compatibility supported by the current Project binding;
2. validate `agnir.discovery_profile` against the already selected discovery profile;
3. verify that `project.identity` matches the Project selected by the authorized Project Entry Point or trusted binding context;
4. resolve the required memory locators only after those compatibility and identity checks pass.

For the current Svif repository binding, the expected values are Agnir Core `0.1`, profile `repository-filesystem/0.1`, and Project identity `urn:svif:project:svif-core`. Treat these as Project-binding facts, not universal Agnir constants.

Do not load state and then retroactively decide whether it belonged to the selected Project. Unsupported Core/profile compatibility must surface an explicit discovery failure such as `AGNIR_DISCOVERY_UNSUPPORTED_VERSION`; a selected-root identity mismatch must surface `AGNIR_DISCOVERY_PROJECT_MISMATCH`. A known required locator whose authorization is absent or denied must remain `AGNIR_DISCOVERY_UNAUTHORIZED` when that distinction can safely be made; a required locator that cannot resolve to durable state must remain `AGNIR_DISCOVERY_UNRESOLVABLE`. A Locator Chain that loops rather than terminating in required durable state must remain `AGNIR_DISCOVERY_CYCLE`; state known to be superseded or non-authoritative must remain `AGNIR_DISCOVERY_STALE`; and material contradiction between the Discovery Record and resolved memory, or within the resolved memory itself, must remain `AGNIR_DISCOVERY_INCONSISTENT` until safe continuation is re-established. None of these failures grants permission to search sibling repositories, parent/child Projects, home directories, chat history, or retired layouts for substitute state.

After validation, treat the Project-managed Agnir state as durable authority for current state, next actions, decisions, and referenced evidence. Do not treat chat history, an executor's private context, Git, GitHub, ChatGPT, or any other execution surface as canonical merely because work happened there.

When `SVIF.yaml` is available, read it after Agnir discovery and use it to understand the Project's Svif bindings and active product contracts.

If Agnir is expected but discovery or activation fails, do not invent Project state. Identify the failed locator/discovery step, repair the earliest violated discovery invariant when authorized, then rerun discovery from the original authorized Project Entry Point; otherwise surface the blocker and stop before making state-dependent changes.

If more than one Project is involved, keep each Project's durable state isolated. Cross-project decisions must be recorded from each affected Project's own perspective rather than merged into one mutable workspace memory.

## 2. Reconstruct only the context needed for the current operation

Load current state and next actions first. Then read only decisions and evidence that materially constrain the requested operation. Avoid pulling historical or retired artifacts back into active architecture unless the current Project explicitly declares them authoritative.

Use the Project's canonical repository or substrate when one is declared. For `iorLab/svif`, `main` is the active line and repository-managed Agnir state is canonical. Svif currently consumes Agnir Core compatibility `0.1` through the `repository-filesystem/0.1` profile; Agnir repository release `0.1.0` is a separate SemVer layer and must not be confused with the Core/profile compatibility identifiers.

## 3. Execute through the Svif lifecycle

Use this lifecycle as the default control loop:

`DISCOVER -> PLAN -> CHANGE -> VERIFY -> DELIVER -> OBSERVE -> CHECKPOINT`

`REPAIR` returns to the earliest violated invariant.

For implementation tasks:

- choose the strongest available Project tool instead of asking the user to perform work the executor can perform;
- make the smallest coherent set of changes that satisfies the intent;
- after each material change, verify the exact changed subject with the strongest available check;
- preserve stable subject identity across verification and any later effect;
- keep evidence inspectable enough that another executor can determine what actually happened;
- if verification fails, repair before delivery or checkpointing success.

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

If authority is missing, stop before actuation. If observation is unavailable or contradicts the requested result, record the effect as unconfirmed/failed rather than successful.

## 5. Keep execution surfaces replaceable

Agnir is the founding Continuity Provider for Svif, ChatGPT is a founding Execution Surface, and Cloudflare is a founding Capability Provider. They are bindings, not universal kernel dependencies.

Do not introduce an unnecessary dependency on ChatGPT, GitHub, Cloudflare, Git, or a local checkout when the Project can remain portable. Use the tools available in the current environment without redefining Project truth around those tools.

## 6. Checkpoint durable truth

Checkpoint after a meaningful state transition and whenever the user asks to checkpoint, save progress, stop, finish, or equivalent.

Write the checkpoint through the Project's declared Agnir memory locations. Update, as applicable:

- Current State: what is now demonstrably true, including the verified subject/version;
- Next Actions: concrete remaining work in resume order;
- Decisions: only durable choices made or superseded during the operation;
- Evidence: verification/observation identifiers, relevant commit/run/target identity, and uncertainty needed for audit or recovery.

Before finishing a checkpoint, re-read the durable state needed to ensure it does not contradict the operation just completed. A fresh executor should be able to resume from Project-owned surfaces without private conversation context.

Do not checkpoint a failed or uncertain external effect as successful. Record the uncertainty and the next repair action instead.

## 7. Svif repository development rules

When operating on `iorLab/svif` itself:

- follow the Agnir activation/discovery route, then read `AGNIR.yaml`, `.agnir/state.md`, `.agnir/next-actions.md`, `.agnir/decisions.md`, and relevant evidence before substantive changes;
- also read `SVIF.yaml` and relevant specifications;
- work directly on the active `main` line unless the Project state says otherwise;
- keep `README.md` and `README.zh-CN.md` synchronized when architecture, runtime flow, distribution status, or documented repository structure changes;
- update `REPOSITORY_TREE.md` whenever tracked files are added, removed, moved, or materially change responsibility;
- run repository integrity, portable contract, and runtime/unit test layers before claiming the change is complete;
- distinguish package/conformance success from real client installation success; do not claim installation validation until an actual supported client has installed/exercised the package or Skill.

The Plugin/distribution layer must call into or guide the existing Svif product semantics. It must not reimplement the Orchestrator or move canonical Project truth out of the configured Continuity Provider.
