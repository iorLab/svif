# Svif Project Binding 0.2

**Identifier:** `project-binding/0.2`

The Project Binding tells the Svif product which replaceable providers and surfaces apply to a Project. It is configuration for orchestration, not durable Project memory and not a provider credential store.

## 1. Required semantics

A binding MUST identify:

- the Svif product line and binding contract;
- a stable Project identity;
- one Continuity Provider binding.

A binding MAY identify:

- zero or more Execution Surfaces;
- zero or more Capability Providers;
- applicable Svif profiles;
- product/repository metadata and namespaced extensions.

A binding MUST NOT require plaintext protected secret values.

## 2. Repository/filesystem serialization

Current repository/filesystem integrations use a top-level `SVIF.yaml` serialization. The filename is a packaging/discovery convention for this integration, not a universal requirement of the Svif product kernel.

Equivalent binding objects MAY be supplied by another execution surface or installation mechanism.

## 3. Reference shape

```yaml
svif:
  version: "0.2"
  manifest: "project-binding/0.2"

project:
  identity: "urn:example:project"

bindings:
  continuity:
    provider: "agnir"
    compatibility: "0.2"
    profile: "repository-filesystem/0.2"
    config:
      discovery: "AGNIR.yaml"
      lineage: "urn:example:lineage:main"
      vcs_selector: "refs/heads/main"

  execution:
    - surface: "chatgpt"

  capabilities:
    - provider: "cloudflare.workers"
      adapter: "adapters/cloudflare.json"

profiles:
  - "software-delivery/0.2"
```

The arrays may be empty when a Project does not bind an Execution Surface or Capability Provider in this serialization.

## 4. Continuity binding

`bindings.continuity` MUST identify `provider`.

`compatibility` MAY constrain the provider contract/version. `profile` MAY constrain a provider-specific profile. `config` MAY carry non-secret provider-specific discovery, lineage-selection, selector-binding, or adapter configuration.

Svif MUST treat these fields as provider-specific constraints; it MUST NOT infer that every Continuity Provider supports Agnir compatibility lines, logical lineages, files, Git, or repositories.

For the founding Agnir integration:

- provider: `agnir`;
- the released Svif `v0.2.0-preview.1` line consumes Agnir Core `0.1` / `repository-filesystem/0.1`;
- the active Core `0.2` real-consumer validation may bind Agnir Core `0.2` / `repository-filesystem/0.2` explicitly;
- repository/filesystem discovery points to `AGNIR.yaml`;
- when Core `0.2` is selected, a provider-specific logical lineage identity and VCS selector binding MAY be supplied in `config` and MUST agree with the selected Agnir Project root/binding.

A compatibility-line change such as Agnir Core `0.1` → `0.2` is a Continuity Provider migration, not a normal compatible operational upgrade. Svif MUST preserve Project identity and provider-owned durable truth while the provider performs that migration.

### Provider-local parallel continuity

A Continuity Provider MAY expose multiple independently advancing continuity contexts for one stable Svif Project identity when the selected provider compatibility/profile supports that behavior.

Svif Project identity MUST NOT be derived from a provider lineage, namespace, branch, selector, revision, worktree, or checkpoint receipt. Provider-specific lineage identity and backend selector/binding metadata remain inside `bindings.continuity.config` (or an equivalent provider-specific binding object) and MUST NOT become generic Orchestrator identity semantics.

Two Svif bindings may therefore identify the same `project.identity` and the same Continuity Provider while selecting different provider-local continuity lineages. Each selected binding must be self-consistent and independently resumable according to that provider's contract. Svif MUST NOT scan sibling provider contexts and guess which one is current when the selected binding is absent, inconsistent, or unresolved.

When provider-local lineages are integrated, the Continuity Provider owns reconciliation and coherent publication according to its contract. Svif MUST NOT copy the source lineage's provider-specific selector or continuity metadata into the target merely because Project content was integrated.

## 5. Execution Surface bindings

`bindings.execution` is an array of execution-surface bindings.

Each item MUST identify `surface`. It MAY carry an adapter/integration reference and non-secret configuration.

An execution binding describes where/how Svif is integrated; it does not make that surface the owner of Project truth.

The founding surface is `chatgpt`.

## 6. Capability Provider bindings

`bindings.capabilities` is an array of capability-provider bindings.

Each item MUST identify `provider`. It MAY carry:

- an adapter descriptor reference;
- capability kinds;
- non-secret configuration;
- authority/policy references.

Protected values remain in authorized stores/channels.

The founding external delivery/effect provider family is Cloudflare; other providers are expected.

## 7. Profiles

`profiles` selects Svif specializations that apply to the Project. `software-delivery/0.2` is the current software-delivery profile.

Profiles add requirements but MUST NOT silently redefine provider/surface bindings.

## 8. Product metadata and extensions

`product` and `extensions` are optional.

The Svif repository uses `product` to point at its architecture/contracts and namespaced repository metadata under `extensions`. These fields are not a substitute for the required Project/provider bindings.

## 9. Reference schema

`schemas/project-binding.schema.json` is the machine-readable reference schema for this contract.
