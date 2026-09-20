# Svif 0.2.0 public-submission candidate audit — 2026-09-18

Status: **accepted repository/package candidate; not submitted, scanned by OpenAI, reviewed, approved, published, directory-listed, or consumer-installed.**

Update 2026-09-20: the historical acceptance above is packaging-only. The Principal has paused OpenAI Platform publication. The local-readiness audit appended below reproduces functional blockers; current-version local effectiveness and whole-product completion are NOT accepted.

## Candidate subject

- authoritative repository: `iorLab/svif`;
- source before candidate hardening: `466adc41ffc351258556f26f9cc8e207e6d075eb`;
- accepted candidate commit: `5a81d7a8b7490a6215d7a27966759fb2656b477a`;
- accepted candidate tree: `9eb1f2e506f7e057c622ea38ed1bfa6ebb93798c`;
- exact Plugin subtree: `34d2d205455f641b9eca59c0cb4fb9ff43880804`;
- active package/version identity: `0.2.0`;
- submission type: Skills-only; no MCP/App increment.

The exact Plugin subtree is the repository candidate subject. Current OpenAI submission documentation requires the final skill package and the same file tree/instructions used in local testing; it does not make a repository CI result equivalent to portal submission or publication.

## Immutable Preview boundary

The already released Repository Preview remains unchanged:

- tag: `v0.2.0-preview.1`;
- annotated tag object: `2535cb89426c2d38c2e061948e81954a7c7c26d7`;
- peeled release commit: `2b07b6b5ea0bc8feee59f9f647be9af3069d056e`.

The current `0.2.0` package therefore has a new identity instead of reusing the immutable Preview version for changed contents.

## Packaging audit

Fresh authoritative reads after candidate publication confirmed:

- root `VERSION`: `0.2.0`;
- `plugin/plugin.json.version`: `0.2.0`;
- `plugin/.codex-plugin/plugin.json.version`: `0.2.0`;
- `integrations/cloudflare/adapter.json -> adapter.version`: `0.2.0`;
- root `plugin/plugin.json -> extensions.com.openai.interface` exactly equals the compatibility overlay `interface`;
- root portable manifest is the canonical OpenAI metadata source;
- `.codex-plugin/plugin.json` remains compatibility fallback only;
- `plugin/assets/svif-app-icon.png` and `brand/exports/svif-app-icon.png` resolve to the same Git blob `2db76d3c8ad8bc5fb365b3a17c946f90eecdddca`;
- the public candidate remains Skills-only and retains the single shared `plugin/skills/svif/SKILL.md` workflow.

## Current OpenAI submission contract checked

OpenAI documentation checked on 2026-09-18 confirms the relevant current boundary:

- portable packages use root `plugin.json`; portable skills live under root `skills/`; assets may live under root `assets/`;
- OpenAI-specific presentation metadata belongs under root `extensions.com.openai`; a separate `.codex-plugin/plugin.json` remains supported as a compatibility fallback;
- Skills-only public submissions remain supported;
- submission collects listing details, skills, starter prompts, five positive and three negative review cases, intended availability, release notes and policy attestations;
- submitting starts review; approval does not itself publish; explicit publication is a later action;
- published Plugins appear in the universal directory shared by ChatGPT and Codex.

The repository does not claim the external publisher prerequisites are satisfied. The remaining account-side prerequisites are Apps Management: Write in the publishing OpenAI Platform organization and a verified individual developer or business identity in that same organization.

## Verification receipts

Candidate CI:

- workflow: `Svif product checks`;
- run: `35316829755`;
- `repository-integrity`: job `105510201645` — success;
- `portable-contracts`: job `105510201580` — success;
- `runtime-kernel`: job `105510201457` — success.

Fresh post-CI readback confirmed authoritative `main` exactly at candidate commit `5a81d7a8b7490a6215d7a27966759fb2656b477a` before the durable checkpoint, with all four version surfaces aligned, OpenAI metadata synchronized, approved logo identity preserved, and the Preview tag still unchanged.

The first durable-checkpoint publication at `fd94894530249e35fd373a7e80004167b08a336e` produced run `35317030008`: repository-integrity and portable-contracts passed, while runtime-kernel failed only because the durable installation-documentation guard expected the stable literal marker `public/personal ChatGPT path` and the checkpoint title had inserted `0.2.0` inside that phrase. The product/package candidate was unchanged. The follow-up repair restores the stable marker while preserving the `0.2.0` candidate semantics.

## Remaining evidence layers

Still unobserved and therefore not claimed complete:

1. publisher permission / identity prerequisites;
2. creation of the real OpenAI submission draft;
3. portal skill/security scan outcome;
4. human/automated review outcome;
5. explicit Publish after approval;
6. directory appearance;
7. real individual-user ChatGPT installation, with ChatGPT Web a first-class target;
8. invocation on a real Project;
9. Agnir activation, verification and durable checkpoint;
10. fresh-context resume from that checkpoint.

No `v0.2.0` Git tag or GitHub Release was created by this audit.


## Directory image blocker discovered after initial candidate CI

A fresh check against the current OpenAI public-directory submission error reference found stricter branding requirements not yet encoded by Svif CI:

- `interface.logo` is required and must reference a square image;
- `interface.composerIcon` is required and must reference a square image;
- raster branding assets must be decodable PNG/JPEG/WebP, at least 48×48, at most 4096×4096, and no larger than 5 MiB.

Fresh inspection of approved Svif exports established:

- `brand/exports/svif-app-icon.png`: 160×155, blob `2db76d3c8ad8bc5fb365b3a17c946f90eecdddca` — approved brand asset but **not square**, therefore unsuitable for the current directory branding fields;
- `brand/exports/svif-favicon-128.png`: 128×128, blob `40dbc1cbca075149cd8fc4e0859f09217b0c3530` — approved, square, and within current dimension limits.

The repair therefore reuses the approved 128×128 favicon byte-for-byte as `plugin/assets/svif-directory-icon.png`, points both required interface fields to it, removes the non-square Plugin-local app-icon copy, and adds repository regression coverage for required paths, byte identity, PNG decoding signature, exact 128×128 dimensions, 48–4096 square bounds, and the 5 MiB file limit.

This is a packaging compliance repair, not a brand redesign.


## Final image-contract repair acceptance

The directory-branding repair was published on authoritative `main` and independently re-read after CI:

- repair commit: `f9026f7e3db4db8956cfc88ba1990daf0757a011`;
- repair tree: `4963f063a7bd3dcb0c05df839e44c10dab7a3f4f`;
- exact repaired Plugin subtree: `5ab4b6147dbd096c052f042b23e37f0ec39f7091`;
- `VERSION`: `0.2.0`;
- portable manifest version: `0.2.0`;
- compatibility-overlay version: `0.2.0`;
- Cloudflare adapter package version: `0.2.0`;
- root and fallback OpenAI interface metadata: exact equality;
- `interface.logo`: `./assets/svif-directory-icon.png`;
- `interface.composerIcon`: `./assets/svif-directory-icon.png`;
- package directory icon blob: `40dbc1cbca075149cd8fc4e0859f09217b0c3530`;
- approved `brand/exports/svif-favicon-128.png` blob: same `40dbc1cbca075149cd8fc4e0859f09217b0c3530`;
- dimensions guarded by tests: 128×128;
- non-square `plugin/assets/svif-app-icon.png`: absent;
- original approved non-square brand export remains unchanged in `brand/exports/`.

Final repair CI:

- workflow run: `35317245771` — success;
- runtime-kernel job: `105511502688` — success;
- portable-contracts job: `105511502989` — success;
- repository-integrity job: `105511503097` — success.

Fresh tag readback also confirmed the immutable Repository Preview boundary remains unchanged:

- `refs/tags/v0.2.0-preview.1`;
- annotated tag object: `2535cb89426c2d38c2e061948e81954a7c7c26d7`;
- peeled released commit remains `2b07b6b5ea0bc8feee59f9f647be9af3069d056e`.

The exact submission candidate is therefore the `plugin/` tree `5ab4b6147dbd096c052f042b23e37f0ec39f7091` as materialized by source commit `f9026f7e3db4db8956cfc88ba1990daf0757a011`. A later durable checkpoint may advance `main` without changing that Plugin subtree; external submission evidence must identify the exact submitted package subject rather than merely a moving branch.

No `v0.2.0` tag, GitHub Release, OpenAI portal submission, scan result, review result, publication, directory listing, or consumer installation is claimed by this acceptance.

## 2026-09-20 — Local-readiness audit; publication paused

### Principal instruction and verdict

The Principal requested: pause OpenAI Platform publication; first confirm local installation/effectiveness and completion of Svif functionality. The old publisher-first resume order is superseded. No public submission, account change, publication, release/tag mutation or live Cloudflare call was performed.

Verdict: **current 0.2.0 native-host effectiveness remains unobserved; whole-product functional completion is blocked by reproduced defects.** This is a targeted source/behavior audit, not exhaustive certification. The historical package checks above remain packaging evidence only.

### Exact subjects and method

Captured main: `fe7788bd53d3a240f663860133b741799d0470e3`; root tree `dc01838f822d363af7bbf1bc27593edad7b19ab7`. Source modules fetched through the GitHub connector were materialized in an isolated Python 3.13.5 sandbox and checked using Git's blob identity formula (SHA-1 of `blob <byte-length>\0<bytes>`):

- `src/svif/runtime.py`: `5d68ed8255767b7e67bfe681b18d8deb7fe72fa4`;
- `src/svif/execution/chatgpt.py`: `6b32a6a35812581eaa1e059c52833e06458a57e8`;
- `src/svif/capabilities/cloudflare.py`: `0f6836d27ec5ff32347ca3fc38f34e127d7ae039`;
- `src/svif/continuity/agnir.py`: `bed682ead6c1edd5b0b577d6d46d755ab9780517`.

All four matched. Minimal empty package initializers only enabled imports; these probes did not exercise repository package exports. The complete repository test suite was not re-run locally. Baseline CI log from run `35334521502`, job `105566170085`, was independently read and reports 87 tests passing on the captured source. In particular, `tests/test_plugin_first_use_bootstrap.py` tests Skill text markers and order rather than executing a native installed host.

The existing Actions artifact `10542750132` was actually downloaded and extracted. Outer archive SHA-256 matched `56c86a8da18d36edd02786da0ff6af4e7094438639656b3983497d42af133d3f`; inner `svif-0.2.0.zip` matched `bc2315562f7bdeb4232aadb9b583a7442f8cd868dbeacd13bb57caf0c785177c`; CRC validation returned no errors. Its five regular files matched the accepted Plugin blobs: root manifest `411835e3f60c557c388c8040b78cfb4c841dc968`, fallback manifest `cfd99269ad786175641b59e229c64fccd5699b19`, README `7510dbab616259c99c35163e91c5181f8b208442`, icon `40dbc1cbca075149cd8fc4e0859f09217b0c3530`, Skill `87f5c51d3c6c7ead8b7cc1ac565b06faf2d7e96d`.

This package contains workflow instructions, metadata and an icon, not the Python kernel. ZIP verification/extraction is not host installation. The sandbox had no installed `codex` executable and no native desktop host; direct git cloning also failed DNS resolution. Plugin discovery found no connected local-host execution capability suitable for installing on the Principal's computer. No current-version installed/enabled, host Skill-discovery or fresh native-session receipt is claimed.

Historical native acceptance was re-read in `2026-09-02-svif-v0.2.0-preview.1-candidate.md` and `2026-09-02-svif-v0.2.0-preview.1-release.md`: Preview.1 was observed on isolated Codex CLI and ChatGPT desktop/Codex with work/checkpoint/recovery exercises. Those receipts concern a different package subject and tested paths only; they do not certify current 0.2.0 or all failure paths in the old release.

### Reproduced open gaps

**F1 — protected authority requirement is result-controlled (blocking).** The descriptor `integrations/cloudflare/adapter.json` requires `protected-delivery` for `deploy_verified_worker`. The ChatGPT bridge nevertheless parses an optional model-controlled `authority_class`, and the Orchestrator only checks that field. With zero trusted grants, omitted, null and empty values each produced one fake deployment, one fake observation and one successful checkpoint. An otherwise identical request with explicit `protected-delivery` raised `AuthorityRequired`, with zero transport calls and zero checkpoints. An effect without verification correctly raised `ProvenanceMismatch`. Repair must resolve mandatory authority requirements from trusted operation/provider policy, independently of result payloads. These were fake transport calls, NOT live Cloudflare actions.

**F2 — failed checkpoint partially mutates durable truth (blocking).** A valid Project with `memory.decisions: null` can load. Requesting State, Next Actions and Decisions updates writes the first two before raising `AGNIR_DISCOVERY_UNRESOLVABLE` for Decisions. Reproduced on Core/profile 0.1, 0.2 and 1.0: State changed, Next Actions changed, no new evidence receipt. Per-file `os.replace` does not establish a coherent multi-file checkpoint. Required repairs include preflight before any writes, coherent publication/recovery, and interruption/concurrency tests appropriate to the provider contract.

**F3 — evidence-child symlink escapes Project root (blocking).** The evidence-directory locator is contained, but `_read_evidence()` follows child-file symlinks outside that root. For each of Core/profile 0.1, 0.2 and 1.0, a sibling temporary file containing the dummy string `DUMMY-OUTSIDE-PROJECT-NOT-A-SECRET` was returned as Project evidence. There was no authorized external binding. Repair must apply resolved-path authorization to each child read and relevant write path, not just the parent locator. No real secret or user file was accessed.

**F4 — failed non-effectful verification can accompany a completion checkpoint (readiness gap).** With no capability request, a WorkResult carrying failed verification and State `task completed` / Next Actions `none` reached checkpoint. A missing-verification control also reached checkpoint, but missing verification is not necessarily erroneous for every trivial operation. The gap is absence of a trusted required-check contract and enforcement preventing failed required verification from being recorded as successful completion. This observation does not redefine all non-effectful operations as requiring checks.

Positive controls: ordinary provider load -> text checkpoint -> a newly constructed provider load recovered the new State and Next Actions on all three supported compatibility lines. This does not simulate a fresh LLM/host session.

### Minimal credential-free reproduction

Run the following from a checkout of the captured source, with `PYTHONPATH=src`. All transport and out-of-root data are fixtures. These assertions document the observed BAD behaviors; a future repair should replace them with desired-behavior regression assertions, not suppress the failures.

```python
import tempfile
from pathlib import Path
from svif.runtime import (
    ContinuitySnapshot, ContinuityUpdate, OperationOutcome, OperationRequest,
    Orchestrator, ProjectBinding, ProviderBinding,
)
from svif.execution.chatgpt import ChatGPTExecutionSurface
from svif.capabilities.cloudflare import CloudflareWorkersCapabilityProvider
from svif.continuity.agnir import AgnirFilesystemContinuityProvider

class Memory:
    provider_id = 'fixture'
    def __init__(self): self.saved = []
    def load(self, identity): return ContinuitySnapshot(identity)
    def checkpoint(self, outcome): self.saved.append(outcome)

class FakeTransport:
    def __init__(self): self.deploys = 0
    def deploy_worker(self, **kwargs): self.deploys += 1
    def observe_worker(self, **kwargs): return True

memory, transport, surface = Memory(), FakeTransport(), ChatGPTExecutionSurface()
provider = CloudflareWorkersCapabilityProvider(transport)
engine = Orchestrator(continuity_providers=(memory,), execution_surfaces=(surface,),
                      capability_providers=(provider,))
binding = ProjectBinding('urn:test:readiness', ProviderBinding('fixture'),
                         'chatgpt', frozenset({'cloudflare.workers'}))
session = engine.begin(binding, OperationRequest('audit', 'fixture only'))
payload = {
    'project_identity': binding.project_identity, 'operation_id': 'audit',
    'subject_identity': 'sha256:fixture',
    'evidence': [{'kind': 'verification', 'subject_identity': 'sha256:fixture',
                  'status': 'succeeded'}],
    'capability_request': {'provider': 'cloudflare.workers',
        'operation': 'deploy_verified_worker', 'effect': 'actuate',
        'subject_identity': 'sha256:fixture', 'target_identity': 'urn:test:target'},
}
engine.complete(session, surface.parse_result(session, payload))
assert transport.deploys == 1 and len(memory.saved) == 1  # F1, zero trusted grants
payload.pop('capability_request')
payload['evidence'][0]['status'] = 'failed'
payload['continuity_update'] = {'state': 'task completed', 'next_actions': 'none'}
session2 = engine.begin(binding, OperationRequest('audit-2', 'fixture only'))
payload['operation_id'] = 'audit-2'
engine.complete(session2, surface.parse_result(session2, payload))
assert memory.saved[-1].continuity_update.state == 'task completed'  # F4

for version in ('0.1', '0.2', '1.0'):
    with tempfile.TemporaryDirectory() as temporary:
        root = Path(temporary) / 'project'
        (root / 'memory/evidence').mkdir(parents=True)
        (root / 'memory/state.md').write_text('old state')
        (root / 'memory/next.md').write_text('old next')
        (root / 'AGNIR.yaml').write_text(
            f'agnir:\n  version: "{version}"\n'
            f'  discovery_profile: "repository-filesystem/{version}"\n'
            'project:\n  identity: "urn:test:readiness"\n'
            'continuity:\n  lineage: "urn:test:lineage"\n'
            'memory:\n  state: "memory/state.md"\n'
            '  next_actions: "memory/next.md"\n  decisions: null\n'
            '  evidence: "memory/evidence"\n')
        continuity = AgnirFilesystemContinuityProvider(root)
        continuity.load('urn:test:readiness')
        update = ContinuityUpdate(state='new state', next_actions='new next',
                                  decisions='new decision')
        outcome = OperationOutcome('urn:test:readiness', 'checkpoint-audit',
                                   'sha256:fixture', (), False, update)
        try:
            continuity.checkpoint(outcome)
        except Exception as error:
            assert 'AGNIR_DISCOVERY_UNRESOLVABLE' in str(error)
        else:
            raise AssertionError('Expected missing Decisions-locator failure')
        assert (root / 'memory/state.md').read_text() == 'new state'  # F2
        assert (root / 'memory/next.md').read_text() == 'new next'
        dummy = Path(temporary) / 'outside-dummy.txt'
        dummy.write_text('DUMMY-OUTSIDE-PROJECT-NOT-A-SECRET')
        (root / 'memory/evidence/link.txt').symlink_to(dummy)
        snapshot = continuity.load('urn:test:readiness')
        assert snapshot.evidence['link.txt'] == dummy.read_text()  # F3
```

### Acceptance required before either user-requested confirmation

Local gate: exact candidate + host/version + installed/enabled + actual host Skill discovery; clean ordinary-Project bootstrap; concrete verified work; durable checkpoint; a genuinely new session recovering without old transcript; repeat on an initialized Project with unchanged identity/unrelated instructions; negative cases for broken discovery, another provider, failed verification, missing authority and unavailable observation. Use isolated disposable Projects and no protected effects during this acceptance.

Functional gate: close F1-F4 with executable desired-behavior tests, then finish a requirement-to-implementation/test matrix for the bounded Skill-first MVP and applicable runtime contracts. Distinguish optional future MCP/App/live-provider integration from defects in existing promised functionality. No remote MCP requirement is added solely for completion or publication.

This checkpoint records the audit and new priorities only. It does not repair product code, does not prove native local installation, and does not grant release/publication authority.
