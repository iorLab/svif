# README Diagram Localization Checkpoint — 2026-08-28

## Scope

This checkpoint records the current Svif documentation architecture after the bilingual README and comprehension-first diagram work.

## Durable facts

- `README.md` is the English project entry point.
- `README.zh-CN.md` is the Simplified Chinese project entry point.
- Both READMEs contain a current Architecture Diagram and Runtime / Operation Flow using Mermaid.
- Architecture/runtime changes must update affected diagrams in both languages in the same change set.
- Localized diagrams are comprehension-first, not literal translations.
- In Simplified Chinese diagrams, each important node should communicate what the node is and what responsibility it has without requiring the reader to understand the English term first. English terminology may remain as a secondary parenthetical label where useful.
- This localization rule does not create a separate architecture model; all localized READMEs describe the same canonical Svif architecture.

## Implementation evidence

- Chinese diagram clarification commit: `5460bc388a638ce4dff8e5d8fe12d467c687a54a`.
- Localization-policy decision commit: `a8fcd4e76d502f57bc9e751e9763eddf3530a001`.
- Svif product-check run `33142755892`: success.
- The run covers repository integrity, runtime kernel behavior, and portable contracts.

## Resume point

Continue from the current product milestone: build the in-repository founding E2E path across Agnir + ChatGPT + Cloudflare through the Svif Orchestrator. Documentation diagrams must evolve in the same change set whenever that implementation changes the architecture or runtime flow.
