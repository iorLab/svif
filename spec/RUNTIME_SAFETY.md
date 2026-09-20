# Svif 0.2 reference-runtime safety and recovery

This implements existing CORE, Evidence, Capability Adapter and Software Delivery
invariants. It does not change their `0.2` versions or add a new continuity protocol.

## Trusted integration boundary

`Orchestrator.begin()` takes a trusted `ProjectBinding` and `OperationRequest`.
The integration must resolve Project-owned binding/policy before creating them.
`verification_required=True` is the default; `False` is allowed only when trusted
planning determines verification is genuinely not applicable. `required_verifiers`
requires successful exact-subject receipts from every named verifier. Neither field
is accepted from model results. Failure/blocked/unknown verification for the current
subject cannot be represented as successful completion, even in the optional case.

`ChatGPTExecutionSurface.parse_result()` marks returned verification as advisory.
The integration obtains actual tool/test receipts and passes them through
`complete(..., verification_evidence=(...))`. Copying the model's declarations into
that trusted argument is NOT verification. Model delivery, observation and checkpoint
records are rejected. A synchronous `execute()` implementation is trusted adapter code;
its returned evidence has the same responsibilities as explicit trusted receipts.

Every bound effect provider implements `policy_for(operation) -> CapabilityPolicy`.
Unknown operations and missing policies fail closed. The provider's required authority
set is mandatory; a model's optional `authority_class` may add a requirement but cannot
remove one. Cloudflare `deploy_verified_worker` always requires `protected-delivery`,
matching `integrations/cloudflare/adapter.json`. Grants come only from trusted request
or invocation context, not JSON result fields. Direct Python API callers are trusted
integration code, not a safe deserialization interface for untrusted code or objects.

Sessions are identity-bound and single-use within an Orchestrator. A pre-effect
validation failure may be repaired using that session. Once actuation or checkpoint
begins, an exception makes it uncertain: do not blindly call complete again. Durable
operation receipts reject conflicting operation-id reuse across process restarts.
Project continuity is preflighted and stale snapshots are rejected BEFORE actuation.

## Agnir filesystem checkpoint transaction

The adapter supports Agnir Core/profile `0.1`, `0.2`, and `1.0` without relabeling any
Project. The existing supported nested-scalar YAML subset is retained; duplicate keys,
ambiguous role aliases, unsupported identity/profile and invalid paths fail closed.
There is no claim of a general-purpose YAML parser or all possible Agnir backends.

A snapshot includes a digest of the discovery anchor and loaded durable objects.
Every Orchestrator checkpoint supplies this opaque revision as a compare-and-swap
precondition. Direct trusted checkpoint callers may omit it for a deliberately fresh
operation; they must not omit it for a stale read-modify-write. All updates, locator
availability, file types and receipt serialization are validated before publication.

The adapter uses a per-Project thread/process lock and a private write-ahead journal at
`.svif-runtime/agnir-pending.json`. The journal contains before/after bytes, checksums,
Project/operation identity and the discovery-anchor digest. Normal write failures roll
back the complete preimage. Process death leaves the durable intent; the next adapter
entry completes the transaction before exposing a snapshot. Conflicting independent
edits, corrupt journals or changed bindings stop with `AGNIR_CHECKPOINT_RECOVERY_REQUIRED`
rather than overwriting them. Exact checkpoint retries are no-ops; contradictory
reuse of an operation identity fails with `AGNIR_OPERATION_REPLAY`.

This is **recoverable coherent publication through the adapter**, not an assertion
that several arbitrary OS file reads or Git checkouts are an atomic transaction.
All cooperating processes must use the guard. A Skill or external reader that reads
raw files must check for pending runtime markers, recover through the adapter or stop,
and must not claim a mixed state is a completed checkpoint. Do not copy, commit,
checkout, or discard a Project with an unresolved transaction. Resolve it first or
retain the whole recovery directory with the working copy for authorized recovery.
The ignored runtime directory is local transaction machinery, not another source of
canonical Project truth. Journals can contain Project data; do not publish them as logs.

POSIX I/O uses component-relative no-follow opens, regular single-link file checks,
random exclusive temporary files, fsync and rename. Anchor, locator, evidence child,
receipt, journal and lock paths all use contained I/O. Windows checks symlinks/junctions
and uses the OS file lock. The selected root and its owner are trusted: this is not a
security sandbox against an administrator or hostile concurrent Windows filesystem
mutation. Supported local-filesystem behavior is tested; network filesystems, power
loss on storage that ignores fsync, and multi-host transactions are not certified.

## External effects and interruption

Agnir records `.svif-runtime/agnir-effect.json` before external actuation. It binds
Project/operation/provider/subject/target, the preflight revision and planned checkpoint.
An interrupted or failed observation blocks normal continuation with
`AGNIR_EFFECT_RECONCILIATION_REQUIRED`, including after a process restart. Successful
matching delivery + independent observation are checkpointed before retiring the marker.

A trusted integration may inspect `pending_effect(project_identity)`, obtain independent
provider receipts, then call `reconcile_effect(project_identity, delivery=..., observation=...)`.
This operation never redeploys. Wrong subject/target/provider or stale Project memory
blocks recovery. If an effect did not happen or cannot be observed, keep it unresolved
and involve the Principal rather than converting uncertainty to success or retrying
actuation automatically. This is not a distributed exactly-once transaction guarantee.
Cross-Project target coordination and real transport idempotency belong to integrations.

## Compatibility and acceptance

Runtime checkpoint receipt serialization is now `svif_runtime_checkpoint: "0.2"`.
It records the enclosing Project/operation and original evidence plus update digests;
this is an implementation receipt, not a replacement for `evidence-record/0.2`.
Runtime EvidenceRecord is an exact-subject subset. A build/transform integration must
retain its richer derivation/log/authority provenance in Project evidence; the minimal
kernel does not authorize a different delivered subject using an unsupported derivation.

The installed Skills-only Plugin does not contain or automatically invoke the Python
kernel. Skill adherence and native host behavior require their own observations.
See `conformance/RELEASE_READINESS.md` for scoped acceptance and remaining gates.
