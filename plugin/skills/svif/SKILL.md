---
name: svif
description: Operate software and technical Projects with durable Agnir continuity, explicit evidence, authority boundaries, verification, external-effect observation, and reliable checkpoint/resume behavior. Use for Project implementation, debugging, delivery, repository work, or continuation where the Project should remain resumable across executors and sessions.
---

# Svif Project Orchestration

Use Svif as an execution discipline for real Project work. Prefer completing concrete work through available tools over producing abstract plans when the task is actionable.

## 1. Discover and activate the Project before acting

### Bind existing continuity or bootstrap a genuinely new Project

Do not require the user to initialize Agnir separately before Svif can operate an ordinary Project. Before treating a missing Agnir Discovery Record as a discovery failure, distinguish an existing valid Agnir Project, a partial/broken Agnir Project, a Project intentionally bound to another Continuity Provider, and a genuinely uninitialized Project.

Select exactly one authorized Project root, then inspect Project-owned durable surfaces including `SVIF.yaml`, `AGNIR.yaml`, root `AGENTS.md`, `AGNIR.md`, the README, and `.agnir/` when present.

#### Existing Agnir Project: preserve the declared compatibility line

If `AGNIR.yaml` exists or durable Project artifacts clearly establish an Agnir binding, do **not** run clean bootstrap merely because a newer Agnir release exists.

1. Resolve and validate the Project's actual `agnir.version`, `agnir.discovery_profile`, Project identity, lineage/selector semantics when applicable, and declared memory locators before loading durable memory.
2. Dispatch according to the compatibility identifiers the Project actually declares. A valid Core/profile `0.1` Project remains `0.1`; a valid `0.2` Project remains `0.2`; a valid `1.0` Project remains `1.0`. The same rule applies to future supported `x.y` lines. Installing or discovering a newer Agnir distribution is **not** authorization to migrate or relabel compatibility.
3. If `SVIF.yaml` is absent and Svif setup is authorized, create a minimal `project-binding/0.2` binding that reuses the exact Agnir Project identity and binds `continuity.provider: "agnir"`, `compatibility` equal to the existing `agnir.version`, `profile` equal to the existing `agnir.discovery_profile`, and discovery `"AGNIR.yaml"`.
4. If `SVIF.yaml` already exists, require its Agnir compatibility/profile/identity to agree with the existing Agnir Project. A mismatch is a repair/binding case, not permission to choose whichever version is newer.
5. An operational Agnir package upgrade and a Core/profile compatibility migration are different operations. Neither is implied by installing or invoking Svif. Normal binding/resume of an existing Project does not require a latest-release lookup. Preserve its recorded operational release/provenance as well; absent optional package provenance is not evidence of an uninitialized Project.

Do not treat partial or contradictory Agnir/Svif artifacts as a clean first-use bootstrap. If durable surfaces show that the Project already intends to use Agnir but activation/discovery is incomplete, broken, unsupported, or inconsistent, enter repair and preserve the applicable Agnir failure class. Do not silently replace that Project with a newly initialized latest-version Project.

If `SVIF.yaml` or another durable binding intentionally selects a different Continuity Provider, do not overwrite it with Agnir. Use the configured provider when supported or surface a binding/support blocker.

#### Genuinely uninitialized Project: resolve the latest published stable Agnir

Only when the selected Project has no `SVIF.yaml` continuity binding, no `AGNIR.yaml`, no Agnir activation route or declared Agnir memory, and no durable configuration selecting another Continuity Provider, classify it as a **first-use bootstrap**.

An explicit Principal request to install/enable Svif for the selected Project, or to invoke Svif to operate that Project after the Plugin has been enabled, authorizes the non-destructive Project files required to establish Svif's founding continuity binding unless stricter Project policy says otherwise. That bootstrap authority does not grant authority for protected external effects.

For a genuinely new repository/filesystem Project:

1. Resolve the canonical `iorLab/agnir` **latest published stable release** at operation time. "Latest stable" means an actually published non-prerelease tag/Release with immutable source provenance; never substitute moving `main`, another branch, an RC, or an untagged commit.
2. Read that release's package/release metadata, declared Core contract, repository/filesystem profile, activation/install procedure, and schema before mutating the Project. Package SemVer and Core/profile compatibility are distinct version layers: use the Core/profile declared by the resolved stable release rather than deriving compatibility from the package tag string.
3. If the latest stable release cannot be resolved or its required installation contract cannot be obtained through available authorized tools, report a bootstrap capability blocker. **Do not fall back to Core/profile `0.1`, a cached historical baseline, model memory, or moving `main` and call that latest.**
4. Establish one stable Project identity and initialize Agnir according to that resolved release's install contract. Persist the release-declared Core/profile exactly, including logical lineage and selector/binding semantics when that compatibility line requires them. Use the release's canonical activation surface, preserve unrelated Project files/instructions, create the declared durable memory, and record immutable Agnir operational provenance when supported.
5. Create a minimal repository/filesystem `SVIF.yaml` using `project-binding/0.2`. It MUST use the same stable Project identity and bind `continuity.provider: "agnir"`, `compatibility` equal to the newly created `AGNIR.yaml -> agnir.version`, `profile` equal to `AGNIR.yaml -> agnir.discovery_profile`, and discovery `"AGNIR.yaml"`.
6. Run the fresh activation route required by the resolved Agnir release, then validate that `SVIF.yaml` identifies the same Project and exact continuity compatibility/profile.
7. Once bootstrap passes, continue the user's original Project task in the same operation. Do not make the user issue a separate Agnir initialization prompt and do not stop merely because the Project started without Agnir.

A trusted integration may supply a fresh, same-operation canonical release-resolution receipt and exact source files through authorized local tools. Verify their tag/revision and contract provenance; this is not permission to substitute an old cached version. Before writing any Project files, confirm the selected adapter supports the resolved latest Core/profile. If unsupported, stop without initializing or selecting an older release.

The released `v0.2.0-preview.1` artifact is immutable historical evidence and still contains its original Core/profile `0.1` first-use procedure. Do not move or rewrite that tag. The current unpublished `0.2.0` line deliberately supersedes that historical bootstrap rule: existing Projects preserve their declared Agnir compatibility, while genuinely new Projects resolve the latest published stable Agnir at bootstrap time.

This bootstrap behavior MUST NOT require a preinstalled Agnir Skill, a previous Agnir installation conversation, or predecessor-private memory. Resolving latest stable may read canonical Agnir release and contract artifacts through available authorized tools. If that resolution is unavailable, surface the blocker instead of inventing a version. A compatible surface may delegate installation to an available Agnir installer, but Svif remains responsible for selecting the correct existing-vs-new branch and verifying the resulting Project binding.

If the current execution surface cannot perform the required non-destructive Project writes or latest-stable resolution, report that bootstrap capability blocker rather than pretending that pre-initialization was a user prerequisite.

#### Activate according to the Project's installed Agnir contract

For an Agent-operable Agnir Project, the durable activation route required by that Project's compatible Agnir installation is mandatory before normal Project work. Do not infer the activation route from the newest available version; follow Project-owned activation artifacts and operational provenance.

Supported existing Projects may legitimately use different activation forms. Legacy Core/profile `0.1`, `0.2`, and Agnir `1.0.0` packaging may enter through `Project root -> AGENTS.md -> README.md / Agnir Project Instructions -> AGNIR.yaml -> declared durable memory`. Newer stable packaging may use `Project root -> AGENTS.md -> AGNIR.md -> AGNIR.yaml -> declared durable memory`, with the README heading retained only as a compatibility locator. Preserve a valid existing route unless an explicit compatible operational upgrade or repair authorizes changing it.

Agnir Agent activation and Core discovery are distinct layers. **Do not validate activation by heading/link presence alone.** Validate the canonical instruction surface selected by the installed Agnir contract. When README is the canonical instruction surface, the canonical README `## Agnir Project Instructions` section itself MUST satisfy that installed activation contract. When `AGNIR.md` is canonical, validate the same required operational semantics in `AGNIR.md` and require the README Agnir heading to remain only the compatible locator specified by the selected release.

Whichever canonical instruction surface applies, it must state that the Project uses Agnir for durable continuity and direct a fresh Agent to treat the Project root as the authorized Project Entry Point, read top-level `AGNIR.yaml`, validate compatibility and Project identity before state loading, load Current State and Next Actions, load Decisions and Evidence when relevant, prefer durable Agnir Project truth over chat/private Agent memory unless superseded by a newer Principal instruction or directly observed current Project fact, and checkpoint material continuity changes at an intentional save/finish boundary. If any required instruction is missing, materially weakened, or contradicted, activation is not healthy even when `AGENTS.md` reaches the expected locator; repair the earliest defect when authorized and rerun activation from the Project root.

The fact that the current Agent can directly open `AGNIR.yaml` MUST NOT be used to bypass a missing, stale, contradictory, or predecessor-private activation route or to claim that a fresh Agent can resume from the Project root. A non-Agent Executor or trusted adapter already given the applicable profile implementation may begin discovery at `AGNIR.yaml` as the profile permits; that exception does not silently redefine Agent activation.

`AGENTS.md` remains locator-only. When installing or repairing its Agnir locator, make the smallest locator-only merge: do not delete, reorder, normalize, summarize, or otherwise rewrite unrelated Project-owned instructions merely to install or repair Agnir. If an equivalent Agnir locator already exists, keep the operation idempotent rather than adding another copy. If resolving a material conflict would require deleting, overriding, or reinterpreting an existing Project instruction, surface the conflict to the Principal and do not report Agent activation healthy until it is explicitly resolved and a fresh activation test passes. The selected canonical activation surface—legacy README procedure or current `AGNIR.md` procedure—owns the full Agnir Project instructions.

Before following that route, require the authorized Project Entry Point or trusted binding context to select exactly one Project root. If multiple candidate Project roots exist and no authority rule selects one, surface `AGNIR_DISCOVERY_AMBIGUOUS` rather than choosing the most convenient candidate. Once one root is authoritatively selected, a parent or child Project with its own `AGNIR.yaml` does not make that selected root ambiguous and MUST NOT be searched as a replacement.

Before resolving a Discovery Record, select the discovery profile/adapter convention applicable to the authorized Project Entry Point from trusted integration or binding context. The Discovery Record may declare its profile for compatibility checking, but it MUST NOT bootstrap authority by choosing the adapter/convention used to discover or interpret itself. If no applicable profile can be selected safely, surface the discovery/compatibility blocker rather than guessing from nearby files or model memory.

Under the selected discovery convention, resolve exactly one authoritative Discovery Record before loading continuity. If no Discovery Record can be resolved after the first-use-bootstrap check above, surface `AGNIR_DISCOVERY_NOT_FOUND`. Detect Locator Chain cycles and conflicting candidate records before compatibility or identity validation rather than following a cycle, guessing among conflicting records, or silently adopting another candidate.

When `AGNIR.yaml` is available, read it before substantive work. Before loading any declared durable memory:

1. validate `agnir.version` against the Agnir Core compatibility supported by the current Project binding;
2. validate `agnir.discovery_profile` against the already selected discovery profile;
3. verify that `project.identity` matches the Project selected by the authorized Project Entry Point or trusted binding context;
4. for Core `0.2` or `1.0`, require a non-empty logical `continuity.lineage`; when a VCS selector is selected by trusted context, require the durable selector binding and verify that it matches that context while remaining distinct from the logical lineage identity;
5. resolve the required memory locators only after those compatibility, identity, lineage, and applicable selector-binding checks pass.

For supported `repository-filesystem/0.1`, `repository-filesystem/0.2`, and `repository-filesystem/1.0` profiles, relative memory locators remain scoped to the selected Project root after resolving filesystem indirection. A relative locator that traverses a symlink or other indirection outside that root MUST NOT become an implicitly authorized external Locator Chain merely because the target is readable. Follow external memory only through an explicit durable authorized binding/Locator Chain; otherwise preserve the applicable discovery failure, including `AGNIR_DISCOVERY_UNAUTHORIZED` when the locator is known but authorization is absent or denied.

A Locator Chain hop may use an environment binding only when that binding is stable and durably associated with the selected Project. A value that exists only in the current process environment, temporary workspace metadata, a prior conversation, private model memory, or a prompt-provided secret MUST NOT become continuity authority merely because it makes the locator resolve in this run. Require the Project Entry Point or another durable Project-owned binding to establish how a fresh Executor can recover the same locator and invoke any required authorization without predecessor-private context. If that durable association cannot be established, surface the applicable discovery failure rather than accepting an ephemeral successful resolution or checkpointing it as resumable continuity.

For repository-aware Projects that declare `extensions.agnir/repository.canonical` and `authoritative_ref`, treat those values as durable backend metadata for canonical continuity, not as decorative provenance. Before a state-dependent write or checkpoint, determine whether the selected working copy/revision is actually on the declared canonical repository/ref. A detached commit, pull-request checkout, temporary branch, fork, mirror, or otherwise non-authoritative execution copy MAY be used for observation, implementation, and verification, but MUST NOT silently become the canonical continuity write target merely because it is writable. Reconcile accepted changes back to the declared authoritative ref, or surface the repository/ref mismatch and leave the canonical checkpoint unchanged until the Project policy or trusted Principal explicitly authorizes a different durable binding. Package revision identity and target-Project authoritative-ref identity are separate facts and MUST NOT be conflated.

For the current Svif repository binding, the expected values are Agnir Core `1.0`, profile `repository-filesystem/1.0`, Project identity `urn:svif:project:svif-core`, one explicit logical Continuity Lineage, and a matching durable VCS selector binding. Treat these as Project-binding facts, not universal Agnir constants. Existing target Projects likewise dispatch according to their own declared compatibility. The immutable released `v0.2.0-preview.1` retains its historical Core/profile `0.1` bootstrap bytes, while the current unpublished `0.2.0` Skill uses existing-version preservation plus latest-stable selection for genuinely new Projects.

Do not load state and then retroactively decide whether it belonged to the selected Project. Unsupported Core/profile compatibility must surface an explicit discovery failure such as `AGNIR_DISCOVERY_UNSUPPORTED_VERSION`; a selected-root identity mismatch must surface `AGNIR_DISCOVERY_PROJECT_MISMATCH`. Core `0.2` or `1.0` without a selected logical lineage must surface `AGNIR_LINEAGE_REQUIRED`. A selected VCS context without a durable selector binding, or with a conflicting selector binding, must preserve the applicable binding failure rather than guessing another lineage. A known required locator whose authorization is absent or denied must remain `AGNIR_DISCOVERY_UNAUTHORIZED` when that distinction can safely be made; a required locator that cannot resolve to durable state must remain `AGNIR_DISCOVERY_UNRESOLVABLE`. A Locator Chain that loops rather than terminating in required durable state must remain `AGNIR_DISCOVERY_CYCLE`; state known to be superseded or non-authoritative must remain `AGNIR_DISCOVERY_STALE`; and material contradiction between the Discovery Record and resolved memory, or within the resolved memory itself, must remain `AGNIR_DISCOVERY_INCONSISTENT` until safe continuation is re-established. None of these failures grants permission to search sibling repositories, parent/child Projects, home directories, chat history, or retired layouts for substitute state.

After validation, treat the Project-managed Agnir state as the durable continuity authority for current state, next actions, decisions, and referenced evidence, but reconcile conflicting truth using the precedence defined by the selected compatible Agnir Core line unless stricter Project policy applies: directly observed current Project or relevant external-system state first; explicit current Principal instruction or policy second; current durable Agnir state third; older checkpoint/evidence fourth; Executor-private context last. Material unresolved uncertainty must be surfaced rather than guessed. A newer observed fact or Principal instruction that supersedes durable state must be reconciled back into the Project-owned checkpoint instead of remaining only in transient execution context.

This truth-reconciliation precedence does not grant protected execution authority. Principal approval or policy is usable for protected effects only when it arrives through the applicable trusted integration boundary, and directly observed state does not replace exact-subject verification, required authority, or independent post-effect observation.

Do not treat chat history, an executor's private context, Git, GitHub, ChatGPT, or any other execution surface as canonical merely because work happened there.

When `SVIF.yaml` is available, read it after Agnir discovery and use it to understand the Project's Svif bindings and active product contracts.

If Agnir is expected but discovery or activation fails, do not invent Project state. Identify the failed locator/discovery step, repair the earliest violated discovery invariant when authorized, then rerun discovery from the original authorized Project Entry Point; otherwise surface the blocker and stop before making state-dependent changes.

If more than one Project is involved, keep each Project's durable state isolated. Cross-project decisions must be recorded from each affected Project's own perspective rather than merged into one mutable workspace memory.

### Interrupted operations and contained reads

Before loading a filesystem Project as coherent current truth, inspect for
`.svif-runtime/agnir-pending.json` and `.svif-runtime/agnir-effect.json`. These are
local recovery markers, not alternate Project memory. When present, recover through
the configured trusted adapter or stop with an explicit recovery/reconciliation blocker.
Do not delete the marker, read partial State/Next Actions as completed work, repeat an
uncertain external effect, or publish/check out an unresolved working copy. Every actual
read/write target, including evidence children and temporary output paths, must stay
within its authorized boundary. Reject unauthorized symlinks/junctions/hardlinks rather
than following them as substitute continuity. Preserve required recovery data.

## 2. Reconstruct only the context needed for the current operation

Load current state and next actions first. Then read only decisions and evidence that materially constrain the requested operation. Avoid pulling historical or retired artifacts back into active architecture unless the current Project explicitly declares them authoritative.

Use the Project's canonical repository or substrate when one is declared. For `iorLab/svif`, `main` is the active authoritative line and repository-managed Agnir state is canonical. The Svif repository Project consumes its recorded Agnir operational distribution while declaring Core compatibility `1.0` and profile `repository-filesystem/1.0`; its logical lineage and VCS selector binding are declared separately in `AGNIR.yaml` / `SVIF.yaml`. Target Projects are different: preserve an existing Project's declared compatibility exactly, and for a genuinely uninitialized Project resolve the canonical latest published stable Agnir and adopt the Core/profile declared by that release. Repository SemVer, operational distribution provenance, and Core/profile compatibility identifiers are separate version layers and must not be conflated.

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

The trusted Project/operation or provider policy determines required authorization;
omitting or weakening a result's `authority_class` cannot waive that policy. Verification
success must be based on inspectable check/tool output for the exact subject, not the
Executor declaring its own result successful. Establish required checks before changing
files; failed, blocked, unknown or missing required checks block completion even when no
external delivery is involved. A genuinely not-applicable check needs an explicit trusted
planning basis, not a result field that disables verification. When using the Python
bridge, trusted receipts and grants enter `Orchestrator.complete()` separately from the
parsed model payload; never copy unverified model declarations into those arguments.

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

For direct file-based checkpoints, preflight the complete State/Next/Decisions/Evidence
update before writing. Prefer one coherent VCS commit or the configured adapter's
recoverable transaction; individual atomic file writes alone do not make a multi-file
checkpoint atomic. Re-read authoritative identity and resulting state before claiming
success. Preserve unresolved effect identity and observation requirements across restart;
recovery must independently observe/reconcile, not blindly deploy again. Installed Skill
instructions are not a sandbox and do not automatically install the Python runtime.

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
