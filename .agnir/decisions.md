# Svif Decisions

## 2026-08-27 — New main-line architecture

- `main` implements Svif directly; ZeroLocal v0.1 remains predecessor evidence in Git history.
- Svif product line is `0.2` development.
- Delivery gated by verification must actuate the verified subject or an independently verified replacement.
- OBSERVE is mandatory when external effect is claimed; actuation success alone is insufficient.
- Secret values remain in authorized protected channels/stores; Svif carries references/scopes, not plaintext values.

## 2026-09-01 — Name origin and product meaning

- `Svif` is an Icelandic neuter noun whose core dictionary senses include flight, hovering, floating, and gliding.
- Icelandic environmental usage includes `svifryk` for suspended particulate matter / particulate matter. This association is intentionally recorded, but it does **not** mean that `svif` by itself means dust or particles.
- The product metaphor maps the motion/suspension sense to Svif's architecture: Project execution may move across replaceable Execution Surfaces and Capability Providers while no single execution environment owns the Project or its durable truth.
- The pairing with Agnir is conceptually deliberate. Agnir's name maps to the durable pieces of Project truth; Svif's name maps to motion around that persistent continuity as execution environments change.
- This naming relationship is a product/brand metaphor, not a protocol dependency or a requirement that Agnir data physically move with every Svif execution step.
- Linguistic and usage evidence is recorded in `.agnir/evidence/2026-09-01-svif-name-origin.md`.

## 2026-08-28 — Product Architecture 0.2

- Svif is a **Project orchestration product**, not a pure protocol.
- Four first-class components are **Orchestrator**, **Continuity Provider**, **Execution Surface**, and **Capability Provider**.
- Agnir is the founding Continuity Provider but remains an independent protocol/project.
- ChatGPT is the founding Execution Surface; canonical Project truth remains execution-surface-neutral.
- Cloudflare is the founding external-effect Capability Provider family, not a kernel dependency.
- `SVIF.yaml` is the repository/filesystem serialization of `project-binding/0.2`.
- Portable Core/Evidence/Capability Adapter/Software Delivery material is internal product contract, not the complete product identity.

## 2026-08-28 — Executable product foundation

- `src/svif/runtime.py` is the executable Orchestrator kernel.
- `src/svif/continuity/agnir.py` implements the current Agnir repository/filesystem profile.
- `src/svif/execution/chatgpt.py` implements the structured ChatGPT execution bridge.
- Externally driven surfaces use `Orchestrator.begin()` / `Orchestrator.complete()`; untrusted result payloads cannot self-grant protected authority.

## 2026-08-28 — Single-repository Svif product topology

- Active canonical repositories are only `iorLab/svif` and `iorLab/agnir`.
- Provider-specific Svif implementations, fixtures, integration notes, and E2E pressure tests belong in `iorLab/svif` unless they are independently useful protocols/products in their own right.
- `iorLab/svif-cloudflare-reference` is retired from the active architecture and must not remain a runtime, conformance, release, Project-state, or next-action dependency.
- Historical evidence from the retired repository is preserved in `history/CLOUDFLARE_REFERENCE.md`; this is evidence only, not a dependency.
- Svif owns the Cloudflare Workers Capability Provider at `src/svif/capabilities/cloudflare.py` and its descriptor/integration boundary under `integrations/cloudflare/`.
- Cloudflare transport is injected so provider I/O/credentials can vary without making GitHub Actions, Wrangler, or a standalone repository part of the product architecture.
- The old repository may be physically deleted after tombstoning; no active Svif behavior is allowed to depend on it.

## 2026-08-28 — README architecture diagrams and localization

- `README.md` is the English project entry point and `README.zh-CN.md` is the Simplified Chinese entry point.
- Both language versions MUST show the current **Architecture Diagram** and **Runtime / Operation Flow** using Mermaid so the repository explains both static component topology and dynamic operation semantics without requiring a reader to reconstruct them from specifications.
- Architecture, component ownership, dependency direction, authority/provenance boundaries, runtime-flow, or distribution changes MUST update the affected diagrams in both README language versions in the same change set.
- Localized READMEs describe the same canonical architecture. Translation may adapt explanatory prose, but it must not introduce a separate product model.
- Localized diagrams are comprehension-first, not literal translations. In the Simplified Chinese README, important nodes must communicate both role and responsibility so the diagram remains understandable without prior knowledge of the English term; English terminology may remain as a secondary label.
- Repository checks enforce diagram/locale structure rather than exact prose wording.

## 2026-08-28 — Founding credential-free E2E baseline

- `tests/test_founding_e2e.py` is the founding in-repository executable product scenario across Agnir + ChatGPT + Cloudflare through the real Svif Orchestrator boundary.
- The scenario MUST use injected non-secret/fake provider transport by default so the product loop is continuously testable without protected credentials.
- Trusted authority is supplied to `Orchestrator.complete()` by the integration context; model/result payloads do not carry or self-grant `protected-delivery` authority.
- A successful founding E2E proves the orchestration loop, boundary contracts, exact-subject verification, independent observation, and Agnir checkpoint/resume behavior.
- Credential-free founding E2E success does **not** constitute evidence of live Cloudflare production actuation. Live provider delivery remains separately authorized and separately evidenced.
- Product-check run `33143308949` succeeded with repository-integrity, runtime-kernel, and portable-contracts jobs; durable evidence is `.agnir/evidence/2026-08-28-founding-e2e.md`.

## 2026-08-28 — Mature distribution target preserved

- The mature Svif product/distribution target is an **installable Plugin**.
- This is a current Svif decision. Historical ZeroLocal material is not its authority and is not required for the target to remain valid.
- ChatGPT app/MCP packaging is the founding/current ChatGPT Execution Surface integration and MUST NOT be treated as a replacement for the mature Plugin target.
- Distribution may package integrations/providers/onboarding, but it MUST NOT duplicate Orchestrator semantics or move canonical Project truth out of the configured Continuity Provider.
- Dependency direction is `Plugin / distribution -> Execution Surface integration -> Orchestrator -> Continuity + Capability Providers`.

## 2026-08-28 — README repository structure tree

- The README repository explanation uses a **plain-text tree**, not a third Mermaid architecture diagram and not a separate abstract repository map.
- The tree MUST follow the actual repository structure closely enough to show where major product responsibilities live, while remaining selective rather than exhaustively listing every fixture/evidence file.
- Each documented directory or key file SHOULD include a short responsibility explanation directly in the tree.
- If a documented directory is added, removed, moved, or materially changes responsibility, `README.md` and `README.zh-CN.md` MUST update the affected tree in the same change set.
- Repository integrity checks enforce the presence of the explanatory tree and key module anchors without byte-for-byte locking the whole tree.

## 2026-08-28 — Greenfield mainline; history is non-authoritative

- This decision supersedes any interpretation that Svif `0.2` must migrate, preserve compatibility with, or prove conformance against ZeroLocal/legacy architecture.
- Historical material is retained only for lineage, audit, and optional historical reference.
- Active `main` contracts, runtime, conformance, release gates, Project state, and next actions MUST NOT depend on legacy serialization, `.chatgpt/` memory layout, Skills-era structure, standalone reference repositories, or predecessor validation projects.
- Historical ideas MAY be reconsidered, but they become active only when independently reaffirmed in current Svif architecture/decisions.
- Current Svif architecture is intentionally greenfield: Orchestrator + Continuity Provider + Execution Surface + Capability Provider is authoritative even where it differs materially from ZeroLocal.

## 2026-08-28 — Main-only branch governance

- `main` is the only long-lived branch in `iorLab/svif`.
- Legacy, feature, fix, and temporary branch refs are deleted after their final tip SHAs are recorded in `history/BRANCH_ARCHIVE.md`.
- Historical predecessor boundaries are referenced by immutable commit SHA and Git history rather than a live `legacy/*` branch.
- No active product behavior, conformance, release gate, or recovery path may require a retired branch ref.

## 2026-08-29 — Plugin-first delivery and iteration

- Svif MUST stop treating Plugin packaging as a future graduation gate. The first installable Plugin is now an active `0.2` product artifact and real usage begins before remote MCP packaging is complete.
- The Plugin package targets **Agent Plugins 1.0.0** and lives under `plugin/` with `plugin/plugin.json` as the manifest and `plugin/skills/svif/SKILL.md` as the first workflow component.
- The first increment is intentionally **Skill-first**. A Plugin may be useful and testable without an MCP server; therefore `mcp.json` is not a prerequisite for beginning Plugin testing.
- The Plugin Skill operationalizes current Svif behavior: Agnir-first discovery, Project-scoped context recovery, executable lifecycle discipline, exact-subject verification/provenance, trusted authority separation, independent observation, and durable checkpointing.
- Plugin/distribution code and instructions MUST NOT reimplement the Orchestrator, shadow `src/svif/runtime.py`, make an Execution Surface canonical Project truth, or allow model-controlled payloads to self-grant protected authority.
- The remote ChatGPT MCP/App surface remains an additive capability direction. It is accepted only when it reuses `ChatGPTExecutionSurface` and the existing `Orchestrator.begin()` / `Orchestrator.complete()` boundary cleanly.
- Plugin quality is now driven primarily by **install -> real Project use -> observe failure/friction -> repair -> repeat**, with contracts tightened as implementation pressure reveals actual needs.

## 2026-08-29 — OpenAI repository distribution is additive

- The portable Plugin contract remains `plugin/plugin.json` plus shared components under `plugin/`; OpenAI/Codex product distribution metadata does not supersede Agent Plugins 1.0 semantics.
- `.agents/plugins/marketplace.json` is the repository-level OpenAI/Codex GitHub marketplace entry and maps to local `./plugin`.
- `plugin/.codex-plugin/plugin.json` is an additive product-specific manifest that reuses the same `plugin/skills/` implementation; it MUST NOT introduce a second Orchestrator, continuity store, authority model, or execution kernel.
- Shared identity metadata between the portable and Codex manifests is kept synchronized by tests.
- Repository package/conformance/distribution validation is not installation evidence. A successful real-client claim requires observed installation and invocation on the claimed surface, followed by the existing Agnir activation, exact-subject verification, authority, independent-observation, and checkpoint rules.

## 2026-08-31 — Personal ChatGPT users are the primary ChatGPT audience

- Svif's primary ChatGPT product audience is **individual/personal ChatGPT users**, not managed-workspace administrators.
- The preferred mature consumer experience is `Plugins Directory -> discover Svif -> install -> invoke in normal ChatGPT use`, subject to the user's actual plan, region, supported surface, and current OpenAI product availability.
- Repository-backed GitHub marketplace import remains useful for development, Codex, managed-workspace administration, and evidence exercises, but it is **auxiliary** and MUST NOT be treated as the primary consumer onboarding path.
- ChatGPT Web is a first-class target surface for the personal-user product. A packaging change that makes Svif Desktop-only is a material product regression unless the Principal explicitly accepts that tradeoff based on observed evidence.
- The user-facing installation UX should remain minimal in the Agnir style: users express install intent, while distribution-specific mechanics belong to the installation/package procedure. Where the product surface provides direct directory installation, README onboarding should prefer that product-native path over asking ordinary users to understand marketplace manifests or administrator controls.
- Evidence for this decision is `.agnir/evidence/2026-08-31-personal-chatgpt-distribution-checkpoint.md`.

## 2026-08-31 — Skills-only public Plugin is the initial personal ChatGPT release path

- Current OpenAI developer documentation explicitly accepts **Skills-only** Plugins for public review and publication into the universal Plugins Directory shared by ChatGPT and Codex.
- Svif's initial public ChatGPT release therefore reuses the existing `plugin/.codex-plugin/plugin.json` plus `plugin/skills/svif/` implementation. MCP/App packaging is **not** a prerequisite for the initial public release and MUST NOT be added merely to satisfy publication.
- Public submission requires an OpenAI Platform organization where the submitter has **Apps Management: Write** plus a verified individual developer or business identity. These are publisher/account prerequisites, not Svif runtime dependencies.
- Submission, automated skill scan, reviewer approval, explicit publication, directory appearance, installation, invocation, and real Project checkpoint are distinct evidence layers and MUST NOT be collapsed into one success claim.
- Approval does not itself publish the Plugin; after approval the publisher must explicitly publish the approved version before directory availability is claimed.
- The first decisive consumer validation target is a real **personal ChatGPT Web** install from the universal Plugins Directory followed by invocation on an Agnir-initialized Project and a resumable checkpoint.
- `.agents/plugins/marketplace.json` remains an auxiliary development/Codex/managed-workspace path. Its success cannot substitute for public-directory publication or personal-user installation evidence.
- Future MCP/App work is driven by concrete server-backed capability needs and surface evidence, not by publication anxiety. Any such increment must preserve the existing Svif Orchestrator, authority boundaries, continuity semantics, and desired ChatGPT Web availability.

## 2026-08-31 — Svif owns first-use continuity bootstrap

- A consumer MUST NOT have to pre-initialize Agnir before first Svif use on an ordinary Project. Requiring that step hides a Svif onboarding defect and tests only an already-prepared environment.
- Before normal Agnir discovery failure handling, the shared Svif Skill distinguishes a genuinely uninitialized Project from a broken existing Agnir/Svif setup and from a Project intentionally bound to another Continuity Provider.
- On the founding repository/filesystem path, a genuinely uninitialized Project is bootstrapped with one stable Project identity shared by Agnir and Svif, Agnir Core `0.1` / `repository-filesystem/0.1` durable continuity, and a minimal `project-binding/0.2` `SVIF.yaml` whose continuity provider is Agnir.
- The bootstrap preserves existing README and `AGENTS.md` content, uses locator-only/idempotent Agnir activation, and stops on material instruction conflict rather than overwriting Project-owned instructions.
- Partial or contradictory Agnir/Svif artifacts are repair cases, not clean initialization cases. A durable binding that intentionally chooses another Continuity Provider MUST NOT be overwritten with Agnir.
- First-use bootstrap is part of the Svif Plugin procedure and consumes Agnir protocol/profile semantics through the founding Continuity Provider integration. It MUST NOT make the Agnir Skill repository, a prior installation conversation, GitHub, or another execution surface a runtime prerequisite.
- Permission to install/enable/invoke Svif for a selected Project authorizes only the non-destructive Project files needed to establish the founding Svif continuity binding, subject to stricter Project policy. It does not grant protected external-effect authority.
- The first real Codex and personal ChatGPT consumer exercises SHOULD start from an ordinary non-Agnir Project so they validate onboarding rather than bypassing it.
- Durable evidence is `.agnir/evidence/2026-08-31-plugin-first-use-bootstrap-fix.md`.

## 2026-09-01 — README user/Agent entry-point information architecture

- Before the Architecture Diagram, both READMEs are deliberately limited to two operational audiences: **Start Here / 从这里开始** for users, followed by the canonical **Agnir Project Instructions** for Agents.
- A short product identity/name explanation may appear before `Start Here`; it is introductory context rather than a third operational audience.
- `Start Here` contains only the minimum current actions: personal-ChatGPT availability status, install intent for compatible Agent environments, normal continuation, and upgrade of the Agnir used by the Project.
- `Agnir Project Instructions` remains the canonical activation heading resolved from `AGENTS.md` and is explicitly marked as Agent guidance for human readers.
- Public-submission workflow, Plugin packaging rationale, compatibility detail, repository structure, and implementation/conformance explanation belong after the architecture entry point or in dedicated documents.
- The user-facing README must reflect the active first-use decision: a genuinely uninitialized Project does not require manual Agnir pre-initialization; Svif owns the founding continuity bootstrap on the repository/filesystem path.
- English and Simplified Chinese READMEs preserve the same audience split and operational meaning. Localized diagrams remain comprehension-first.
- Repository-integrity checks enforce `Start Here -> Agnir Project Instructions -> Architecture` ordering and the canonical install/Agnir-upgrade intents so future edits do not rebuild the old mixed-audience front section.
