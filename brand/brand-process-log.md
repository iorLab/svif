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
| Canonical Project ref | `main` (brand branch records candidate work until integration) |

## Brief

### Audience and positioning

Svif is a **Project orchestration product** coordinating durable Project continuity, execution surfaces, and capability providers. The brand should communicate controlled motion across replaceable execution environments without implying that any one execution surface owns the Project.

Svif and Agnir are independent Projects with a deliberate brand relationship. Svif represents motion, suspension, hovering/gliding, and orchestration around persistent Project continuity. Agnir represents the small durable pieces of Project truth. Their identities should be visibly related without making Agnir look subordinate to Svif.

### Intended surfaces

- repository / GitHub identity;
- Plugin directory/listing identity;
- documentation and README branding;
- favicon/application icons when a product surface requires them;
- social/share assets only when an actual surface references them.

Production integration into shared `main` surfaces remains deferred until production masters and visual QA are complete.

### Required languages

- Brand mark: language-neutral where practical.
- Wordmark/product name: `Svif` casing preserved.
- Supporting brand explanation: English and Simplified Chinese.

### Constraints and exclusions

- Preserve the established `Svif` motion/suspension/gliding metaphor; do not claim that standalone `svif` literally means dust.
- Preserve product neutrality: do not visually bind Svif to ChatGPT, GitHub, Cloudflare, or another replaceable environment/provider.
- Avoid generic AI clichés such as sparkle/starburst, chatbot bubble, robot head, neural-brain icon, generic cloud, or ungrounded “AI magic”.
- Favor vector-native geometry suitable for editable production SVG.
- Small-size simplification, if needed, must be an explicitly approved variant rather than an untracked redraw.
- Similarity review is not legal/trademark clearance.

### Success criteria

1. Express motion/orchestration without implying instability or loss of Project truth.
2. Maintain a visible family relationship with Agnir while remaining independently recognizable.
3. Preserve execution/provider neutrality.
4. Support vector masters and robust monochrome/contrast variants.
5. Remain recognizable at repository/Plugin icon sizes.
6. Permit derivatives to be generated from approved masters without independent redraws.

## Evidence register

| Date | Evidence | Location | What it establishes | Status |
| --- | --- | --- | --- | --- |
| 2026-09-01 | Svif current durable state | `.agnir/state.md` | Product role, architecture and distribution context | Evidence |
| 2026-09-01 | Svif active decisions | `.agnir/decisions.md` | Product architecture, name meaning, Svif/Agnir relationship, branch governance | Evidence |
| 2026-09-01 | Svif name-origin verification | `.agnir/evidence/2026-09-01-svif-name-origin.md` | Linguistic basis and approved product mapping | Evidence |
| 2026-09-01 | Existing-brand asset search | repository `main` | No existing production logo system was found | Evidence |
| 2026-09-01 | Brand Design System workflow | `mattamior/skills-hub/skills/brand-design-system` | Exploration → approval → master lock → derivatives → visual QA | External process evidence |
| 2026-09-02 | Selected identity direction | conversation-generated exploration boards | Principal selected the 01/03/05 hybrid direction and current family palette for refinement | Approval evidence; previews are not production masters |
| 2026-09-02 | Candidate continuity record | `.agnir/evidence/2026-09-02-brand-identity-direction-candidate.md` | Branch-local durable summary and integration rule | Candidate evidence |

## Exploration and decisions

| Date | Direction or decision | Outcome | Rationale | Approver |
| --- | --- | --- | --- | --- |
| 2026-09-01 | Use temporary `brand/identity-system` branch | Approved | Isolates identity work from concurrent `main` development | Principal |
| 2026-09-01 | Design Svif and Agnir as a related brand family with separate canonical assets | Approved | Matches independent-project architecture and deliberate naming metaphor | Principal |
| 2026-09-01 | Keep exploration separate from production integration | Approved working rule | Prevents unapproved concepts from leaking into production surfaces | Principal |
| 2026-09-02 | Retain directions 01 Particle + Motion, 03 S/A Geometry, and 05 Flow & Structure | Approved for synthesis | These directions best expressed motion, family geometry, and structure | Principal |
| 2026-09-02 | Fuse 01 + 03 + 05 into one family direction | **Selected direction** | Svif becomes the motion layer; Agnir the structure layer; both share particle-and-geometry language | Principal |
| 2026-09-02 | Svif uses the former Agnir teal family; Agnir uses a sand family | **Selected palette direction** | Strengthens motion/structure differentiation while retaining family coherence | Principal |
| 2026-09-02 | Generated master-style boards | Direction accepted for refinement, **not production master lock** | Generated previews establish intent, not editable vector geometry or exact production values | Principal |

## Selected direction invariants

### Geometry and proportions

Direction-level invariants now approved:

- Svif mark is based on a flowing **S-shaped motion form**.
- Particle trajectories surround/accompany the S and communicate suspension, motion and orchestration.
- Svif must read as the **Motion Layer** of the family.
- Svif and Agnir share a particle-and-geometry grammar but must remain independently recognizable.

Not yet locked: exact Bézier geometry, band widths, particle counts, particle size sequence, particle locations, construction grid, clear space, lockup ratio, and small-size simplification.

### Palette

Direction-level palette:

- **Svif: teal / turquoise family**.
- **Agnir: sand / warm mineral family**.

Exact HEX/RGB values, contrast variants and monochrome rules are not yet locked.

### Typography and casing

- `Svif` casing is approved.
- Current black sans-serif wordmark treatment is a preview convention only.
- Typeface/custom lettering and final path geometry are not yet approved.

### Negative space and backgrounds

- The flowing S and particle field must remain legible on clean light/dark backgrounds.
- Exact negative-space, reverse and transparency behavior remains to be defined and QA-tested.

### Lockups and spacing

- Standalone mark and mark + `Svif` lockup are intended production roles.
- Exact alignment, spacing and clear-space rules remain to be defined.

## Approval checkpoints

| Date | Checkpoint | Decision | Approver |
| --- | --- | --- | --- |
| 2026-09-01 | Brand work isolation | Work on temporary brand branch; keep `main` authoritative | Principal |
| 2026-09-01 | Brand-family scope | Related but independent Svif/Agnir identities | Principal |
| 2026-09-02 | Direction selection | 01 + 03 + 05 hybrid selected | Principal |
| 2026-09-02 | Color direction | Svif teal, Agnir sand | Principal |
| 2026-09-02 | Master-stage entry | Proceed to production-master reconstruction without reopening concept exploration by default | Principal |

## Inferences and unknowns

| Item | Classification | Follow-up |
| --- | --- | --- |
| Exact teal palette values | Unknown | Establish production HEX/RGB values and accessible contrast variants |
| Exact S geometry | Unknown | Reconstruct as deterministic editable vector geometry |
| Particle system parameters | Unknown | Define count/scale/spacing rules; test small sizes |
| Wordmark construction/typeface | Unknown | Select or draw; record licensing; pathify if appropriate |
| Small-size mark | Unknown | Test 16/32/64 px and explicitly approve simplification if necessary |
| Trademark/similarity clearance | Unknown | Optional visual similarity review; legal clearance remains separate |

## Next brand-stage work

1. Reconstruct the selected Svif mark as an editable SVG production candidate.
2. Freeze exact teal values and monochrome/reverse behavior.
3. Define particle geometry and construction rules shared with Agnir where appropriate.
4. Build standalone mark and horizontal lockup candidates.
5. Render and inspect 16/32/64/128/512 px outputs.
6. After explicit master approval, create `brand-handoff.md` and only the production derivatives required by actual surfaces.
7. Before merging, re-resolve latest `main`, reconcile material brand outcomes into canonical Agnir Decisions/State/Next Actions as appropriate, then integrate brand assets and continuity coherently.
