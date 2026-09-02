# Svif Brand Process Log

## Record metadata

| Field | Value |
| --- | --- |
| Brand or product | Svif |
| Record owner | Svif Project (`iorLab/svif`) |
| Started | 2026-09-01 |
| Last updated | 2026-09-02 |
| Approval authority | Principal |
| Working branch | `brand/identity-system` |
| Canonical Project ref | `main` — this branch records candidate work until integration |

## Brief

### Audience and positioning

Svif is a **Project orchestration product**. The identity should communicate controlled motion across replaceable execution environments without implying that an Execution Surface owns Project truth.

Svif and Agnir are independent brands with one visual family language: Svif represents motion/orchestration around persistent continuity; Agnir represents durable pieces of Project truth.

### Intended surfaces

Repository/GitHub identity, Plugin/directory identity, documentation, and later favicon/app/social assets only when an approved production master and real surface require them.

### Required languages

- Mark: language-neutral where practical.
- Product name: `Svif` casing preserved.
- Supporting brand explanation: English + Simplified Chinese.

### Constraints and exclusions

- Preserve the established motion/suspension/gliding metaphor.
- Do not bind the identity to ChatGPT, GitHub, Cloudflare, or another replaceable environment/provider.
- Avoid generic AI clichés.
- Production artwork must be vector-native and self-contained.
- Small-size simplification must be an explicitly approved variant, never a silent redraw.
- Similarity review is not legal/trademark clearance.

### Success criteria

The identity should express motion without instability, remain recognizably related to Agnir, preserve platform/provider neutrality, survive small sizes, and support reproducible derivatives from one locked master.

## Evidence register

| Date | Evidence | Location | What it establishes | Status |
| --- | --- | --- | --- | --- |
| 2026-09-01 | Svif durable state / active decisions | `.agnir/state.md`, `.agnir/decisions.md` | Product role, name meaning, brand relationship, branch governance | Evidence |
| 2026-09-01 | Name-origin verification | `.agnir/evidence/2026-09-01-svif-name-origin.md` | Linguistic basis and approved product mapping | Evidence |
| 2026-09-01 | Brand Design System workflow | `mattamior/skills-hub/skills/brand-design-system` | Exploration → approval → master lock → derivatives → visual QA | External process evidence |
| 2026-09-02 | Selected concept direction | conversation exploration boards | 01 + 03 + 05 hybrid, Svif teal / Agnir sand | Principal approval; previews are not masters |
| 2026-09-02 | Direction candidate continuity | `.agnir/evidence/2026-09-02-brand-identity-direction-candidate.md` | Branch-local selected-direction summary | Candidate evidence |
| 2026-09-02 | Deterministic master candidate | `brand/masters/svif-mark-v0.1.svg` | Fixed vector S-ribbon + particle geometry | Candidate production evidence |
| 2026-09-02 | Master specification | `brand/masters/MASTER-SPEC-v0.1.md` | Candidate palette, geometry, size rules, remaining gates | Candidate production evidence |
| 2026-09-02 | Master QA candidate | `.agnir/evidence/2026-09-02-brand-master-v0.1-candidate.md` | 64/32/16px rendering result and small-size rationale | Candidate evidence |

## Exploration and decisions

| Date | Direction or decision | Outcome | Rationale | Approver |
| --- | --- | --- | --- | --- |
| 2026-09-01 | Temporary `brand/identity-system` branch | Approved | Isolate brand work from concurrent `main` development | Principal |
| 2026-09-01 | Related but independent Svif/Agnir identity system | Approved | Matches Project architecture and paired naming metaphor | Principal |
| 2026-09-02 | Retain 01 Particle + Motion, 03 S/A Geometry, 05 Flow & Structure | Approved for synthesis | Strongest motion/family/structure directions | Principal |
| 2026-09-02 | Fuse 01 + 03 + 05 | **Selected direction** | Svif = Motion Layer; Agnir = Structure Layer | Principal |
| 2026-09-02 | Svif teal / Agnir sand | **Selected palette direction** | Differentiates motion vs structure while preserving family grammar | Principal |
| 2026-09-02 | Generated master-style boards | Accepted for reconstruction, not locked | Visual intent only; no editable production geometry | Principal |
| 2026-09-02 | Deterministic SVG master candidate v0.1 | Created, **not yet approved as locked master** | Converts visual intent into inspectable vector rules | Pending review |
| 2026-09-02 | Separate small-size candidate | Created, **not yet approved** | Full particles lose detail at favicon scale; avoids silent simplification | Pending review |

## Approved invariants

### Geometry and proportions

Approved at direction level:

- flowing S-shaped motion form;
- particle trajectories communicate suspension/orchestration;
- Svif reads as **Motion Layer / 流动层**;
- shared particle-and-geometry family grammar with Agnir.

Candidate v0.1 now fixes one reconstructable S centerline and ribbon/particle geometry, but those exact coordinates and widths remain pending master approval.

### Palette

Approved direction: teal/turquoise.

Candidate v0.1 values sampled from the selected concept board:

- Light `#75CCC8`;
- Mid `#13AEAC`;
- Dark `#016F6C`.

Exact values remain pending master approval.

### Typography and casing

- `Svif` casing approved.
- Wordmark typeface/custom lettering and path geometry unresolved.
- Concept-board black sans-serif typography is not a production font decision.

### Small-size behavior

Preliminary QA: primary mark works at repository size; particle detail degrades at favicon scale. Current candidate recommends the separate small-size S at `32px` and below, with `16px` requiring it. Pending Principal approval.

### Negative space, backgrounds, lockups

Standalone mark + horizontal lockup are intended. Exact clear space, alignment, dark/reverse/monochrome behavior and final lockup ratio remain unresolved.

## Approval checkpoints

| Date | Checkpoint | Decision | Approver |
| --- | --- | --- | --- |
| 2026-09-01 | Brand work isolation | Keep `main` authoritative; develop on temporary branch | Principal |
| 2026-09-02 | Direction selection | 01 + 03 + 05 hybrid | Principal |
| 2026-09-02 | Color direction | Svif teal, Agnir sand | Principal |
| 2026-09-02 | Master-stage entry | Reconstruct production candidates without reopening concept exploration by default | Principal |
| 2026-09-02 | Master v0.1 lock | **Pending** | Principal |

## Inferences and unknowns

| Item | Classification | Follow-up |
| --- | --- | --- |
| Candidate teal values | Candidate, not locked | Review against selected concept board and contrast requirements |
| Exact S/ribbon/particle geometry | Candidate, not locked | Principal visual review |
| Wordmark construction | Unknown | Select/draw, confirm licensing, pathify |
| Small-size switch rule | Candidate, not locked | Approve or revise after 16/32/64px review |
| Monochrome/reverse behavior | Unknown | Produce and visually QA |
| Trademark/similarity clearance | Unknown | Optional visual risk review; legal clearance separate |

## Next brand-stage work

1. Principal review of deterministic primary and small-size SVG candidates.
2. Revise/freeze geometry and candidate teal values.
3. Build a license-safe pathified wordmark and horizontal lockup candidate.
4. Produce monochrome/reverse variants and render 16/32/64/128/512px QA.
5. Lock the master only after explicit approval; then create `brand-handoff.md` and required derivatives.
6. Before merge, re-resolve latest `main` and reconcile approved brand truth into canonical Agnir continuity as one coherent integration.
