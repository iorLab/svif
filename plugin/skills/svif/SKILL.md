---
name: svif
description: Operate software and technical Projects with durable Agnir continuity, explicit evidence, authority boundaries, verification, external-effect observation, and reliable checkpoint/resume behavior. Use for Project implementation, debugging, delivery, repository work, or continuation where the Project should remain resumable across executors and sessions.
---

# Svif Project Orchestration

Use Svif as an execution discipline for real Project work. Prefer completing concrete work through available tools over producing abstract plans when the task is actionable.

## 1. Discover and activate the Project before acting

### Bootstrap a Project that has no continuity binding

Do not require the user to initialize Agnir separately before Svif can operate an ordinary Project. Before treating a missing Agnir Discovery Record as a discovery failure, first distinguish a genuinely uninitialized Project from a Project whose intended continuity setup is broken.

Select exactly one authorized Project root, then inspect the Project-owned surfaces that can establish intent or an existing binding, including `SVIF.yaml`, `AGNIR.yaml`, root `AGENTS.md`, the README, and `.agnir/` when present. If the selected Project has no `SVIF.yaml` continuity binding, no `AGNIR.yaml`, no Agnir activation route or declared Agnir memory, and no Project instruction or durable configuration selecting another Continuity Provider, classify it as a **first-use bootstrap** rather than a discovery failure.

An explicit Principal request to install/enable Svif for the selected Project, or to invoke Svif to operate that Project after the Plugin has been enabled, authorizes the non-destructive Project files required to establish Svif's founding continuity binding unless stricter Project policy says otherwise. That bootstrap authority does not grant authority for protected external effects.

For the current repository/filesystem founding path, bootstrap the Project in this order:

1. Establish one stable Project identity. Reuse an existing durable Project identity when one is already authoritative. Otherwise generate a new UUID-based URN such as `urn:uuid:<uuid>` and persist exactly the same identity in both the Agnir Discovery Record and the Svif Project Binding.
2. Initialize the Agnir `repository-filesystem/0.1` continuity contract inside the selected Project root using Agnir Core `0.1`: create top-level `AGNIR.yaml`; create `.agnir/state.md`, `.agnir/next-actions.md`, `.agnir/decisions.md`, and `.agnir/evidence/`; persist concise initial Project truth and at least one initialization evidence record; create or update the canonical README `## Agnir Project Instructions`; and install only the minimal Agnir locator in root `AGENTS.md`.
3. Preserve unrelated Project documentation and instructions. If `AGENTS.md` already exists, merge only the minimal locator without deleting, reordering, normalizing, summarizing, or rewriting unrelated instructions. If an equivalent locator exists, remain idempotent. If a material existing instruction conflicts with Agnir activation, surface the conflict to the Principal instead of silently overriding it.
4. Create or validate a minimal repository/filesystem `SVIF.yaml` using `project-binding/0.2`. It MUST use the same stable Project identity and bind `continuity.provider: "agnir"`, compatibility `"0.1"`, profile `"repository-filesystem/0.1"`, and discovery `"AGNIR.yaml"`. Execution and capability bindings may remain empty unless the Project intentionally persists them.
5. Run fresh activation from the selected Project root only: `Project root -> AGENTS.md -> README.md / Agnir Project Instructions -> AGNIR.yaml -> declared durable memory`. Validate the Agnir identity/profile/version and then validate that `SVIF.yaml` identifies the same Project and continuity binding.
6. Once bootstrap passes, continue the user's original Project task in the same operation. Do not make the user issue a separate Agnir initialization prompt and do not stop merely because the Project started without Agnir.

This bootstrap behavior consumes Agnir protocol/profile semantics through Svif's founding Continuity Provider integration; it MUST NOT require the Agnir Skill repository, a previous Agnir installation conversation, GitHub, or another execution surface as a runtime prerequisite. A compatible surface may delegate to an available Agnir installer, but successful first use must remain possible from the Svif Plugin procedure itself.

Do not treat partial or contradictory Agnir/Svif artifacts as a clean first-use bootstrap. If any durable surface shows that the Project already intends to use Agnir but activation/discovery is incomplete or broken, enter repair and preserve the applicable Agnir failure class. If `SVIF.yaml` or another durable binding intentionally selects a different Continuity Provider, do not overwrite it with Agnir; use the configured provider when supported or surface a binding/support blocker. If the current execution surface cannot perform the required non-destructive Project writes, report that bootstrap capability blocker rather than pretending that pre-initialization was a user prerequisite.

For an Agent-operable Agnir Project using `repository-filesystem/0.1`, the durable activation route is mandatory before normal Project work:

`Project root -> AGENTS.md -> README.md / Agnir Project Instructions -> AGNIR.yaml -> declared durable memory`

Agnir Agent activation and Core discovery are distinct layers. When this Skill is operating an Agent-operable Project under `repository-filesystem/0.1`, treat the durable `AGENTS.md -> README.md / Agnir Project Instructions -> AGNIR.yaml` route as part of the Project activation contract, not as an optional convenience. Validate that the route is present, points to the canonical README Agnir section, and contains no unresolved material instruction conflict before treating Agent activation as healthy. The fact that the current Agent can directly open `AGNIR.yaml` MUST NOT be used to bypass a missing, stale, contradictory, or predecessor-private activation route or to claim that a fresh Agent can resume from the Project root.

Do not validate activation by heading/link presence alone. The canonical README `## Agnir Project Instructions` section itself MUST satisfy the current profile activation contract: it must state that the Project uses Agnir for durable continuity and, before Project work, direct a fresh Agent to treat the Project root as the authorized Project Entry Point, read top-level `AGNIR.yaml`, load Current State and Next Actions, load Decisions and Evidence when relevant, prefer durable Agnir Project truth over chat/private Agent memory unless superseded by newer Principal instruction or directly observed current Project fact, and checkpoint material continuity changes at an intentional save/finish boundary. If any required instruction is missing, materially weakened, or contradicted, activation is not healthy even when `AGENTS.md` reaches the correct heading; repair that earliest activation-contract defect when authorized and rerun activation from the Project root.

A non-Agent Executor or trusted adapter that is already given the applicable profile implementation may begin discovery at `AGNIR.yaml` as the profile permits. That exception does not silently convert this Agent Skill into a non-Agent activation context. If the Project is intended to be Agent-operable and its durable activation route is broken, surface the activation blocker and repair that earliest invariant when authorized; do not relabel the accidental direct readability of `AGNIR.yaml` as successful Agent activation.

`AGENTS.md` is only a locator; the target Project README owns the full Agnir Project Instructions. Preserve unrelated existing `AGENTS.md` instructions and never silently override a material conflict. When repairing or installing the Agnir locator in an existing root `AGENTS.md`, make the smallest locator-only merge: do not delete, reorder, normalize, summarize, or otherwise rewrite unrelated Project-owned instructions merely to install or repair Agnir. If an equivalent Agnir locator already exists, keep the operation idempotent rather than adding another copy. If resolving a material conflict would require deleting, overriding, or reinterpreting an existing Project instruction, surface the conflict to the Principal and do not report Agent activation healthy until it is explicitly resolved and a fresh activation test passes.

Before following that route, require the authorized Project Entry Point or trusted binding context to select exactly one Project root. If multiple candidate Project roots exist and no authority rule selects one, surface `AGNIR_DISCOVERY_AMBIGUOUS` rather than choosing the most convenient candidate. Once one root is authoritatively selected, a parent or child Project with its own `AGNIR.yaml` does not make that selected root ambiguous and MUST NOT be searched as a replacement.

Before resolving a Discovery Record, select the discovery profile/adapter convention applicable to the authorized Project Entry Point from trusted integration or binding context. The Discovery Record may declare its profile for compatibility checking, but it MUST NOT bootstrap authority by choosing the adapter/convention used to discover or interpret itself. If no applicable profile can be selected safely, surface the discovery/compatibility blocker rather than guessing from nearby files or model memory.

Under the selected discovery convention, resolve exactly one authoritative Discovery Record before loading continuity. If no Discovery Record can be resolved after the first-use-bootstrap check above, surface `AGNIR_DISCOVERY_NOT_FOUND`. Detect Locator Chain cycles and conflicting candidate records before compatibility or identity validation rather than following a cycle, guessing among conflicting records, or silently adopting another candidate.

When `AGNIR.yaml` is available, read it before substantive work. Before loading any declared durable memory:

1. validate `agnir.version` against the Agnir Core compatibility supported by the current Project binding;
2. validate `agnir.discovery_profile` against the already selected discovery profile;
3. verify that `project.identity` matches the Project selected by the authorized Project Entry Point or trusted binding context;
4. resolve the required memory locators only after those compatibility and identity checks pass.

For the `repository-filesystem/0.1` profile, relative memory locators remain scoped to the selected Project root after resolving filesystem indirection. A relative locator that traverses a symlink or other indirection outside that root MUST NOT become an implicitly authorized external Locator Chain merely because the target is readable. Follow external memory only through an explicit durable authorized binding/Locator Chain; otherwise preserve the applicable discovery failure, including `AGNIR_DISCOVERY_UNAUTHORIZED` when the locator is known but authorization is absent or denied.

A Locator Chain hop may use an environment binding only when that binding is stable and durably associated with the selected Project. A value that exists only in the current process environment, temporary workspace metadata, a prior conversation, private model memory, or a prompt-provided secret MUST NOT become continuity authority merely because it makes the locator resolve in this run. Require the Project Entry Point or another durable Project-owned binding to establish how a fresh Executor can recover the same locator and invoke any required authorization without predecessor-private context. If that durable association cannot be established, surface the applicable discovery failure rather than accepting an ephemeral successful resolution or checkpointing it as resumable continuity.

For repository-aware Projects that declare `extensions.agnir/repository.canonical` and `authoritative_ref`, treat those values as durable backend metadata for canonical continuity, not as decorative provenance. Before a state-dependent write or checkpoint, determine whether the selected working copy/revision is actually on the declared canonical repository/ref. A detached commit, pull-request checkout, temporary branch, fork, mirror, or otherwise non-authoritative execution copy MAY be used for observation, implementation, and verification, but MUST NOT silently become the canonical continuity write target merely because it is writable. Reconcile accepted changes back to the declared authoritative ref, or surface the repository/ref mismatch and leave the canonical checkpoint unchanged until the Project policy or trusted Principal explicitly authorizes a different durable binding. Package revision identity and target-Project authoritative-ref identity are separate facts and MUST NOT be conflated.

For the current Svif repository binding, the expected values are Agnir Core `0.1`, profile `repository-filesystem/0.1`, and Project identity `urn:svif:project:svif-core`. Treat these as Project-binding facts, not universal Agnir constants.

Do not load state and then retroactively decide whether it belonged to the selected Project. Unsupported Core/profile compatibility must surface an explicit discovery failure such as `AGNIR_DISCOVERY_UNSUPPORTED_VERSION`; a selected-root identity mismatch must surface `AGNIR_DISCOVERY_PROJECT_MISMATCH`. A known required locator whose authorization is absent or denied must remain `AGNIR_DISCOVERY_UNAUTHORIZED` when that distinction can safely be made; a required locator that cannot resolve to durable state must remain `AGNIR_DISCOVERY_UNRESOLVABLE`. A Locator Chain that loops rather than terminating in required durable state must remain `AGNIR_DISCOVERY_CYCLE`; state known to be superseded or non-authoritative must remain `AGNIR_DISCOVERY_STALE`; and material contradiction between the Discovery Record and resolved memory, or within the resolved memory itself, must remain `AGNIR_DISCOVERY_INCONSISTENT` until safe continuation is re-established. None of these failures grants permission to search sibling repositories, parent/child Projects, home directories, chat history, or retired layouts for substitute state.

After validation, treat the Project-managed Agnir state as the durable continuity authority for current state, next actions, decisions, and referenced evidence, but reconcile conflicting truth using Agnir Core `0.1` precedence unless stricter Project policy applies: directly observed current Project or relevant external-system state first; explicit current Principal instruction or policy second; current durable Agnir state third; older checkpoint/evidence fourth; Executor-private context last. Material unresolved uncertainty must be surfaced rather than guessed. A newer observed fact or Principal instruction that supersedes durable state must be reconciled back into the Project-owned checkpoint instead of remaining only in transient execution context.

This truth-reconciliation precedence does not grant protected execution authority. Principal approval or policy is usable for protected effects only when it arrives through the applicable trusted integration boundary, and directly observed state does not replace exact-subject verification, required authority, or independent post-effect observation.

Do not treat chat history, an executor's private context, Git, GitHub, ChatGPT, or any other execution surface as canonical merely because work happened there.

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

Before finishing a checkpoint, re-read the durable state needed to ensure it does not contradict the operation just completed. Then verify that the resulting authoritative memory remains cold-start discoverable from the original authorized Project Entry Point: re-resolve the Discovery Record and Locator Chain and confirm that required Current State and Next Actions can be loaded without Executor-private context. If the checkpoint changed the Discovery Record, required memory locators, durable repository/ref binding, or other discovery-critical state, rerun the full cold-start discovery path rather than validating only the files just written. A checkpoint MUST NOT claim resumability when the resulting authoritative Locator Chain is missing, stale, ambiguous, cyclic, unauthorized, inconsistent, or otherwise unresolved.

A fresh executor should be able to resume from Project-owned surfaces without private conversation context.

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