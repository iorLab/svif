# Svif Plugin

This directory is the portable Svif Plugin package.

It targets **Agent Plugins 1.0.0** and intentionally starts with a Skill-only MVP. The repository also carries OpenAI/Codex distribution metadata without replacing the portable package contract:

```text
svif/
├── .agents/plugins/marketplace.json
└── plugin/
    ├── plugin.json
    ├── .codex-plugin/plugin.json
    └── skills/
        └── svif/
            └── SKILL.md
```

`plugin/plugin.json` remains the Agent Plugins 1.0 portable manifest. `plugin/.codex-plugin/plugin.json` is product-specific OpenAI/Codex distribution metadata and points at the same `skills/` component. Neither file is allowed to introduce a second Orchestrator or a second continuity source of truth.

A Skill-only Plugin is structurally useful without an MCP server. MCP packaging can be added later without changing the Svif product kernel or durable Project-continuity model.

## Current validation status

Repository CI validates the portable package structure, Agent Plugins 1.0.0 manifest constraints used by this package, Agent Skills frontmatter/guardrails, Plugin-root filesystem containment and component isolation, Agnir activation/discovery guards, OpenAI/Codex distribution metadata, public-directory listing limits represented in `.codex-plugin/plugin.json`, and the boundary that prevents the Plugin from shadowing the Svif runtime.

That is **package/conformance/distribution validation**, not proof that a particular ChatGPT, Codex, or other compatible client has installed and exercised this exact revision. Repository success does not prove that the Plugin has passed OpenAI public review, appeared in the universal Plugins Directory, been installed by a personal ChatGPT user, or reached a real Project checkpoint.

## What this MVP does

The bundled `svif` Skill guides a compatible execution surface to:

- for an Agent-operable Agnir Project using `repository-filesystem/0.1`, require the durable activation route `Project root -> AGENTS.md -> README.md / Agnir Project Instructions -> AGNIR.yaml -> durable memory` before normal Project work;
- validate Agnir Core/profile compatibility and selected-Project identity before loading durable memory;
- surface unsupported-version, Project-mismatch, authorization, locator, cycle, stale, and inconsistency failures instead of silently falling back to unrelated state;
- load current state and next actions first, then only relevant decisions/evidence;
- execute the Svif lifecycle rather than merely describe it;
- preserve exact-subject verification and provenance across external effects;
- keep protected authority outside untrusted model/result payloads;
- independently observe external effects before checkpointing success;
- write explicit, resumable Current State / Next Actions / Decisions / Evidence checkpoints;
- stop rather than invent Project state when activation/discovery fails.

The Plugin is a distribution/workflow layer. It does not reimplement `src/svif/runtime.py` and it does not make ChatGPT or another plugin client authoritative Project memory.

## Public personal-ChatGPT distribution

The primary ChatGPT audience for Svif is **individual/personal ChatGPT users**. The mature consumer path is therefore the **universal Plugins Directory**, not a managed-workspace GitHub marketplace import.

Current OpenAI developer documentation explicitly allows a public Plugin submission to be **Skills only**. Svif does not need an MCP server or Apps SDK integration merely to qualify for public Plugin review. A skills-only public submission uses the existing OpenAI plugin manifest at `.codex-plugin/plugin.json` plus the bundled `skills/` tree. MCP remains an optional future capability increment rather than a publication prerequisite.

The current public publishing flow is:

1. Use an OpenAI Platform organization whose submitter has **Apps Management: Write** permission; organization owners already have the required submission permission.
2. Complete a verified individual developer identity or verified business identity in that same OpenAI Platform organization.
3. Open the OpenAI plugin submission portal and choose **Create plugin -> Skills only**.
4. Upload the final Skill bundle/package rooted around the same tested `.codex-plugin/plugin.json` and `skills/` implementation. Do not add `apps`, `.app.json`, `mcpServers`, or `.mcp.json` to a Skills-only submission.
5. Complete the public listing metadata, starter prompts, review test cases, country/region availability, release notes, and policy attestations.
6. Submit for review. Submission is not publication.
7. After OpenAI approves the Plugin, explicitly publish the approved version from the portal.
8. Only after publication should Svif be expected to appear in the universal Plugins Directory shared by ChatGPT and Codex. Confirm publication by searching the exact publication name or using the directory URL exposed by the submission portal; main-page featuring is separate from publication.

The current `.codex-plugin/plugin.json` is intentionally kept inside OpenAI's final-directory listing limits used by Svif: `displayName` <= 30 characters, `shortDescription` <= 30 characters, `longDescription` <= 4,000 characters, `developerName` <= 80 characters, no more than 20 capabilities, and no more than three starter prompts with each prompt <= 128 characters and no `@mention`. Repository tests guard these limits.

For a Skills-only public submission, OpenAI's current directory validation treats website/support/privacy/terms URLs as optional, while a verified developer or business identity and skill safety/security scans remain required. If Svif later adds MCP, the submission type and review requirements become materially broader; do not silently treat that as the same release surface.

### Proposed public listing

- **Name:** Svif
- **Package name:** `svif`
- **Developer:** `iorLab` (subject to the verified publisher identity selected in the portal)
- **Category:** Developer Tools
- **Short description:** `Durable project orchestration`
- **Long description:** `Continue a durable Svif Project through Agnir continuity, explicit verification, trusted authority boundaries, independent observation, and resumable checkpointing without moving canonical Project truth into the execution surface.`
- **Starter prompt:** `Continue this Project using its durable state, implement the next action, verify the result, and checkpoint when finished.`

### Review test cases to enter in the submission portal

OpenAI currently asks for five positive and three negative review cases. These cases should be exercised against reviewer-readable fixture Projects rather than relying on private conversation context.

**Positive cases**

1. **Resume a valid Agnir Project.** Prompt: continue the Project and implement the next concrete action. Expected: follow `AGENTS.md -> README Agnir Project Instructions -> AGNIR.yaml`, validate compatibility/identity, load Current State + Next Actions, perform the concrete work, verify it, and checkpoint durable state.
2. **Checkpoint a non-effectful repository change.** Expected: run DISCOVER -> PLAN -> CHANGE -> VERIFY -> CHECKPOINT without inventing DELIVER/OBSERVE evidence.
3. **Repair a missing Agnir locator without destroying existing instructions.** Expected: preserve unrelated `AGENTS.md` content, add only the minimal locator when authorized, rerun activation, and remain idempotent on a second pass.
4. **Resume after a prior checkpoint.** Expected: a fresh execution context reconstructs required Project truth from Project-owned durable surfaces rather than conversation memory.
5. **Handle a verified external-effect fixture.** Expected: require exact-subject verification and trusted authority, actuate only the verified subject through the available capability boundary, independently observe the resulting target, then checkpoint success.

**Negative cases**

1. **Missing/ambiguous Agnir discovery.** Expected: surface the discovery blocker and stop; do not search sibling Projects or chat history for substitute state.
2. **Project identity or compatibility mismatch.** Expected: preserve the explicit Agnir failure class and do not load/checkpoint the mismatched Project state.
3. **External effect without trusted authority or independent observation.** Expected: do not actuate when authority is absent; if observation is unavailable or mismatched, do not checkpoint the effect as successful.

These are submission materials, not evidence that OpenAI review has occurred. The portal submission, automated skill scan, reviewer outcome, approval, publication, and real personal-ChatGPT installation are all external observations that must be recorded separately.

## Portable package exercise

For an Agent Plugins 1.0 implementation or local conformance harness, `plugin/` is the portable package root. This statement describes package layout only; it is not a universal installation instruction for ChatGPT or Codex.

A useful workflow request after a client has actually loaded the Plugin or contained Skill is:

> Continue this Project using its durable state, implement the next action, verify the result, and checkpoint when finished.

Expected behavior: the executor follows Project-owned Agnir activation/discovery, performs actionable Project work with verification, distinguishes package success from external-effect success, and persists a resumable checkpoint rather than relying on conversation memory.

## OpenAI repository marketplace distribution

The repository marketplace remains an **auxiliary development, Codex, managed-workspace, and validation route**. It is not the primary personal ChatGPT onboarding path.

OpenAI currently exposes repository-marketplace paths that can exercise `.agents/plugins/marketplace.json`, including managed-workspace import and Codex-local marketplace registration. Both reuse the same repository distribution shape:

- repository: `https://github.com/iorLab/svif`;
- marketplace manifest: `.agents/plugins/marketplace.json`;
- marketplace source entry: local `./plugin` relative to the marketplace root;
- OpenAI/Codex Plugin manifest: `plugin/.codex-plugin/plugin.json`;
- shared Skill implementation: `plugin/skills/svif/SKILL.md`.

The Codex CLI route is:

```text
codex plugin marketplace add iorLab/svif
```

For a revision-sensitive Codex-local exercise, use a ref explicitly, for example:

```text
codex plugin marketplace add iorLab/svif --ref main
```

`--ref main` selects a moving repository ref. Its repository SHA is comparison evidence, not proof of the exact installed revision unless a client-exposed accepted-version signal binds the invocation to that immutable commit.

For workspace-managed testing, use the repository URL as Source, leave Path empty because the marketplace manifest is at the repository root, and prefer a fixed commit when exact provenance matters. Workspace repository policy values are not workspace execution authority.

Repository marketplace success remains distinct from public-directory publication and from personal ChatGPT installation evidence.

## Installation and invocation evidence

For any real supported surface, record the exact surface, observed installation state, revision/version provenance when exposed, invocation path, Agnir activation/discovery, verification, any trusted authority use, independent observation for external effects, and resulting durable checkpoint.

For the primary consumer target, the first decisive exercise is:

`public universal Plugins Directory -> personal ChatGPT Web -> install Svif -> invoke on a real Agnir Project -> verify -> checkpoint -> fresh-context resume`

Only that observed exercise establishes the personal ChatGPT Web installation baseline. Repository CI, marketplace import, public review approval, and directory publication are related but distinct evidence layers.

## Future MCP/App increment

Add MCP/App packaging only when Svif needs concrete server-backed capabilities that the Skill-only Plugin cannot provide and the surface consequences have been tested. The increment must reuse the existing ChatGPT Execution Surface and `Orchestrator.begin()` / `Orchestrator.complete()` lifecycle, preserve protected authority outside model-controlled payloads, and avoid creating a second kernel or continuity store.

Do not add MCP merely as a prerequisite for public publication: current OpenAI public submission explicitly accepts Skills-only Plugins.
