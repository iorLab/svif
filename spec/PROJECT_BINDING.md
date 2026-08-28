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
    compatibility: "0.1"
    config:
      discovery: "AGNIR.yaml"

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

`compatibility` MAY constrain the provider contract/version. `config` MAY carry non-secret provider-specific discovery/configuration.

For the active founding integration:

- provider: `agnir`;
- compatibility: `0.1`;
- repository/filesystem discovery may point to `AGNIR.yaml`.

Svif kernel semantics MUST NOT infer that all Continuity Providers use Agnir, files, Git, or repositories.

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
