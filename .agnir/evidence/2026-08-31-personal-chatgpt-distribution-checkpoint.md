# Personal ChatGPT distribution checkpoint — 2026-08-31

## Principal product intent

The primary ChatGPT audience for Svif is **individual/personal ChatGPT users**, not managed-workspace administrators.

This changes the distribution priority without changing the Svif kernel architecture: ChatGPT remains an Execution Surface, Agnir remains the founding Continuity Provider, and distribution must continue to reuse the existing Orchestrator rather than create a second execution kernel.

## Current observed OpenAI product facts

OpenAI Help Center material checked on 2026-08-31 states that:

- the **Plugins Directory** is the primary discovery surface for workflow capabilities across ChatGPT and Codex and is visible across ChatGPT plans, while actual install/use availability depends on plan, region, surface, workspace/account conditions, and included capabilities;
- users can install a listed plugin from the Plugins surface when `Install plugin` is available;
- ChatGPT invocation may use an `@` mention or `+` -> `More` where that surface exposes those controls;
- workspace GitHub marketplace import and workspace installation policy are administrator-oriented distribution/management paths, so they are not the primary consumer onboarding route for Svif's intended personal-user audience;
- imported plugins that declare MCP servers can be marked **Desktop only**, so ChatGPT Web availability must be treated as an explicit product constraint rather than assumed from package conformance.

Sources consulted:

- https://help.openai.com/en/articles/20001256-plugins-in-chatgpt-and-codex
- https://help.openai.com/en/articles/11487775
- https://help.openai.com/en/articles/20001066

These are product-surface observations, not Svif protocol requirements. OpenAI rollout details can change and must be re-verified before publication claims.

## Distribution consequence

The repository-backed OpenAI/Codex GitHub marketplace metadata remains useful for development, managed workspaces, Codex, and evidence exercises, but it is **additive/auxiliary rather than the primary ChatGPT consumer distribution path**.

The primary ChatGPT product target is now:

`individual ChatGPT user -> public Plugins Directory listing -> install -> invoke Svif in normal ChatGPT use`

The implementation/publication mechanism that produces that public listing must be verified against current OpenAI developer publication requirements before Svif claims personal-ChatGPT installability.

## Documentation checkpoint

Immediately before this checkpoint, the bilingual root READMEs were simplified to an Agnir-style user-facing one-line install intent:

- English commit: `95a95423d74c19a3fb63c027a6be8e8bcc232b5a`;
- Simplified Chinese synchronization commit: `2a6829834799e4afc291ace370412bb6b9ec2cc7`;
- `Svif product checks` run `33356222213` completed successfully.

That one-line UX principle remains desirable, but its actual ChatGPT consumer installation route must now be aligned with public/personal Plugin distribution rather than treating managed-workspace GitHub import as the default user path.

## Resume pressure

Do not spend the next iteration proving only workspace-admin import. First establish the exact current publication/install path that lets an individual ChatGPT user discover and install Svif from the Plugins Directory, preserve ChatGPT Web as a first-class target, and then run the first personal-user installation/invocation exercise on the exact published revision when the surface makes revision evidence observable.
