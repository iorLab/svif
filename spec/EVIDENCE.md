# Svif Evidence Record 0.2

**Reference schema:** `schemas/evidence-record.schema.json`

Svif evidence records provide a portable semantic envelope for candidate provenance and lifecycle claims. The schema is a reference serialization; equivalent semantics may be represented elsewhere.

## Record kinds

- `candidate` — establishes a stable source/configuration/state identity.
- `transformation` — establishes an output subject derived from one or more input subjects.
- `verification` — records a check against a stable subject.
- `delivery` — records actuation of a stable subject into a target.
- `observation` — records independent resulting-state evidence for a target/subject.
- `checkpoint` — records a meaningful operation evidence boundary; durable Project Memory remains Agnir's responsibility.

## Subject descriptor

A subject descriptor has a stable `identity`, optional `kind`, optional digest/version, and optional `derived_from` identities.

The identity must be stable/unambiguous for the claim being made. Examples include a full Git commit SHA, artifact digest, versioned document/object ID, immutable transaction ID, or a target-state version token.

## Provenance chain

For a build that transforms source `A` into artifact `B`:

1. candidate record identifies `A`;
2. transformation record identifies `B` and `derived_from: [A]`;
3. verification record references the subject actually verified (`A` or `B`);
4. delivery record references the actual subject actuated and target;
5. observation record references the target and, when observable, the resulting subject/version.

A delivery gated on verification fails provenance if the delivered subject is not the verified subject and there is no independently verified replacement/derivation accepted by Project policy.

## Result status

Portable statuses are `succeeded`, `failed`, `blocked`, and `unknown`.

A successful command with an unobserved external effect is not automatically a successful observation record.

## Producer and authority

Evidence SHOULD identify the producing adapter/implementation when available. Protected operations SHOULD carry an authority class/reference sufficient to explain the trust boundary without exposing credential values.

## Evidence locator

`evidence_locator` may point to logs, attestations, workflow runs, test reports, provider records, rendered artifacts, or other inspectable evidence. It may be null when the record itself is the durable evidence and Project policy accepts that form.
