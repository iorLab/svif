# Cloudflare integration

Cloudflare is a founding Svif **Capability Provider**, not a separate Svif project.

The Svif-owned provider implementation is `src/svif/capabilities/cloudflare.py`. It deliberately separates portable Svif semantics from provider I/O through `CloudflareWorkersTransport`.

## Stable boundary

The integration must preserve:

- operation `deploy_verified_worker` with semantic effect `actuate`;
- protected delivery authority supplied through a trusted integration boundary;
- exact verified subject identity from verification through delivery;
- stable logical target identity;
- delivery evidence followed by independent observation evidence;
- no plaintext protected credentials in Project state, model payloads, or evidence.

The transport implementation may use the Cloudflare API, Wrangler, hosted automation, or another authorized mechanism. That mechanism is packaging/integration detail, not Svif kernel semantics.

`adapter.json` is the active provider descriptor. `policy_for("deploy_verified_worker")`
requires `protected-delivery` even when the result omits or empties its advisory authority
field. Regression tests verify code/descriptor equality. The transport remains injected;
the repository does not claim a production-ready Cloudflare network transport or live
production delivery. An uncertain effect is observed/reconciled without automatic replay;
see `spec/RUNTIME_SAFETY.md`.

## Reference migration

The former `iorLab/svif-cloudflare-reference` repository is retired from the active architecture. Its useful semantics and evidence have been absorbed into `iorLab/svif`; historical provenance is recorded in `history/CLOUDFLARE_REFERENCE.md`.

No Svif runtime, test, release, or next action may depend on the retired repository.
