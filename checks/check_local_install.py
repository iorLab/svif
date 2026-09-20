#!/usr/bin/env python3
"""Native Codex acceptance with separate installation and model-exercise verdicts.

This is a maintainer test, NOT another installer or Svif runtime. It delegates
installation and skill discovery to the real Codex CLI/app-server. All writes
are confined to an explicitly selected, isolated acceptance directory. The
optional --exercise uses the user's authorized Codex account and may use quota;
credentials are never copied from the normal home or included in receipts.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import platform
import queue
import shutil
import subprocess
import sys
import threading
import time
import uuid
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def file_map(root: Path) -> dict[str, str]:
    result = {}
    for path in sorted(root.rglob("*")):
        require(not path.is_symlink(), f"unexpected symlink in acceptance subject: {path}")
        if path.is_file() and ".git" not in path.relative_to(root).parts:
            result[path.relative_to(root).as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
    return result


def run(command: list[str], *, env: dict[str, str], cwd: Path, timeout: int = 90) -> str:
    completed = subprocess.run(command, cwd=cwd, env=env, text=True, encoding="utf-8",
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=timeout)
    require(completed.returncode == 0, f"command failed ({command[0:3]}): {completed.stderr[-2000:]}")
    return completed.stdout


class NativeClient:
    """Small stdio JSON-RPC test client; unknown server requests fail closed."""
    def __init__(self, binary: str, env: dict[str, str], output: Path) -> None:
        self.events: queue.Queue[dict | None] = queue.Queue()
        self.counter = 0
        self.buffer: list[dict] = []
        self.log = (output / "app-server.jsonl").open("w", encoding="utf-8")
        self.errors = (output / "app-server.stderr").open("w", encoding="utf-8")
        self.process = subprocess.Popen([binary, "app-server", "--listen", "stdio://"],
                                        env=env, cwd=output, stdin=subprocess.PIPE,
                                        stdout=subprocess.PIPE, stderr=self.errors,
                                        text=True, encoding="utf-8", bufsize=1)
        self.reader = threading.Thread(target=self._read, daemon=True)
        self.reader.start()

    def _read(self) -> None:
        try:
            for line in self.process.stdout:
                self.log.write(line)
                self.log.flush()
                try:
                    self.events.put(json.loads(line))
                except ValueError:
                    self.events.put({"error": {"message": "non-JSON native stdout"}})
        finally:
            self.events.put(None)

    def send(self, value: dict) -> None:
        self.process.stdin.write(json.dumps(value) + "\n")
        self.process.stdin.flush()

    def next(self, deadline: float) -> dict:
        try:
            value = self.events.get(timeout=max(0.01, deadline - time.monotonic()))
        except queue.Empty as exc:
            raise RuntimeError("native app-server timed out") from exc
        require(value is not None, "native app-server exited before completing acceptance")
        if "method" in value and "id" in value:
            # No hidden approvals, credential prompts or dynamic tool emulation.
            self.send({"id": value["id"], "error": {"code": -32601,
                       "message": "Acceptance harness does not grant interactive authority"}})
            raise RuntimeError("native host requested interactive authority; run the scenario interactively")
        return value

    def call(self, method: str, params: dict, timeout: int = 45) -> dict:
        self.counter += 1
        request_id = self.counter
        self.send({"id": request_id, "method": method, "params": params})
        deadline = time.monotonic() + timeout
        while time.monotonic() < deadline:
            value = self.next(deadline)
            if value.get("id") == request_id:
                require("error" not in value, f"native {method} error: {value.get('error')}")
                return value["result"]
            self.buffer.append(value)
        raise RuntimeError(f"native {method} timed out")

    def __enter__(self) -> NativeClient:
        try:
            self.call("initialize", {"clientInfo": {"name": "svif_acceptance", "version": "0.2.0"}})
            self.send({"method": "initialized"})
            return self
        except BaseException:
            self.__exit__(None, None, None)
            raise

    def __exit__(self, *args: object) -> None:
        if self.process.poll() is None:
            self.process.terminate()
            try:
                self.process.wait(timeout=10)
            except subprocess.TimeoutExpired:
                self.process.kill()
                self.process.wait(timeout=10)
        self.reader.join(timeout=5)
        self.process.stdin.close()
        self.process.stdout.close()
        self.log.close()
        self.errors.close()

    def exercise(self, cwd: Path, prompt: str, skill: dict, *, readonly: bool = False,
                 model: str | None = None) -> tuple[str, str]:
        options = {"cwd": str(cwd), "approvalPolicy": "never",
                   "sandbox": "readOnly" if readonly else "workspaceWrite"}
        if model:
            options["model"] = model
        thread_id = self.call("thread/start", options)["thread"]["id"]
        result = self.call("turn/start", {"threadId": thread_id, "input": [
            {"type": "text", "text": prompt},
            {"type": "skill", "name": skill["name"], "path": skill["path"]},
        ]})
        turn_id = result["turn"]["id"]
        messages: list[str] = []
        deadline = time.monotonic() + 600
        pending, self.buffer = self.buffer, []
        while time.monotonic() < deadline:
            value = pending.pop(0) if pending else self.next(deadline)
            params = value.get("params", {})
            if params.get("threadId") != thread_id:
                continue
            if value.get("method") == "item/completed":
                item = params.get("item", {})
                if item.get("type") == "agentMessage":
                    messages.append(item.get("text", ""))
            if value.get("method") == "turn/completed" and params.get("turn", {}).get("id") == turn_id:
                require(params["turn"]["status"] == "completed", f"native exercise failed: {params['turn']}")
                return thread_id, "\n".join(messages)
        raise RuntimeError("native exercise timed out")


def discovered_skill(response: dict, expected: Path) -> dict:
    matches = []
    for group in response.get("data", []):
        require(not group.get("errors"), "native skill discovery reports errors")
        for skill in group.get("skills", []):
            path = skill.get("path")
            if path and Path(path).resolve() == expected.resolve():
                require(skill.get("enabled") is True, "installed Skill is disabled")
                matches.append(skill)
    require(len(matches) == 1, "native host did not discover exactly the installed Svif Skill")
    return matches[0]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True, help="isolated acceptance directory outside the source repo")
    parser.add_argument("--codex", default="codex", help="real Codex binary")
    parser.add_argument("--exercise", action="store_true", help="run real model tasks using login in this isolated CODEX_HOME")
    parser.add_argument("--model", help="optional available model; no model is silently substituted")
    args = parser.parse_args()
    output = args.output.resolve()
    require(not output.is_relative_to(ROOT), "acceptance output must be outside the source repository")
    marker = output / "acceptance-owner.json"
    if output.exists() and any(output.iterdir()):
        require(marker.is_file(), "refusing to reuse a non-acceptance output directory")
        require(json.loads(marker.read_text())["source_root"] == str(ROOT), "acceptance source changed")
    output.mkdir(parents=True, exist_ok=True)
    marker.write_text(json.dumps({"source_root": str(ROOT)}), encoding="utf-8")
    binary = shutil.which(args.codex)
    require(binary is not None, "Codex binary not found; install an official native CLI first")
    env = os.environ.copy()
    home = output / "codex-home"
    home.mkdir(exist_ok=True, mode=0o700)
    env["CODEX_HOME"] = str(home)
    # No auth/config is copied from the user's ordinary Codex home.
    report: dict[str, Any] = {"schema": "svif-local-acceptance/1", "host": platform.platform(),
                              "installation": "not-run", "skill_discovery": "not-run",
                              "model_exercise": "not-run", "complete_release_acceptance": False}
    session_dir = output / ("run-" + uuid.uuid4().hex)
    session_dir.mkdir()
    try:
        report["codex_version"] = run([binary, "--version"], env=env, cwd=ROOT).strip()
        report["source_revision"] = run(["git", "rev-parse", "HEAD"], env=env, cwd=ROOT).strip()
        source_map = file_map(ROOT / "plugin")
        report["package_files_sha256"] = source_map
        report["package_digest"] = hashlib.sha256(json.dumps(source_map, sort_keys=True).encode()).hexdigest()
        report["marketplace"] = json.loads(run([binary, "plugin", "marketplace", "add", str(ROOT), "--json"], env=env, cwd=ROOT))
        installed = json.loads(run([binary, "plugin", "add", "svif@svif", "--json"], env=env, cwd=ROOT))
        report["install"] = installed
        listing = json.loads(run([binary, "plugin", "list", "--json"], env=env, cwd=ROOT))
        report["list"] = listing
        require(any(p.get("pluginId") == "svif@svif" and p.get("installed") is True
                    and p.get("enabled") is True for p in listing.get("installed", [])),
                "native host did not report Svif installed and enabled")
        cache = Path(installed["installedPath"])
        require(file_map(cache) == source_map, "installed package is not byte-identical to the selected candidate")
        report["installation"] = "passed"
        project = session_dir / "project"
        project.mkdir()
        readme = "# Ordinary Project\nPreserve this original README text.\n"
        agents = "# Existing instructions\nDo not publish, deploy, contact network providers, or delete user files.\n"
        (project / "README.md").write_text(readme, encoding="utf-8")
        (project / "AGENTS.md").write_text(agents, encoding="utf-8")
        expected_skill = cache / "skills/svif/SKILL.md"
        with NativeClient(binary, env, session_dir) as client:
            discovered = client.call("skills/list", {"cwds": [str(project)], "forceReload": True})
            report["skills"] = discovered
            skill = discovered_skill(discovered, expected_skill)
        report["skill_discovery"] = "passed"
        report["isolated_codex_home"] = str(home)
        if not args.exercise:
            report["next"] = "Sign in through the official Codex CLI using this CODEX_HOME, then rerun with --exercise. No credential values belong in this report."
            return 0

        report["model_exercise"] = "in-progress"
        token = "svif-local-" + uuid.uuid4().hex
        content = token + "\n"
        digest = hashlib.sha256(content.encode()).hexdigest()
        phase1 = session_dir / "bootstrap"
        phase1.mkdir()
        with NativeClient(binary, env, phase1) as client:
            thread1, _ = client.exercise(project,
                f"Use Svif for this selected ordinary Project. Create RESULT.md containing exactly {token!r} followed by one newline. "
                "Verify the real file and checkpoint completion with no remaining task. Preserve existing README and AGENTS instructions. "
                "Do not access network providers or publish anything.", skill, model=args.model)
        require((project / "RESULT.md").read_bytes() == content.encode(), "native task result bytes do not match")
        sys.path.insert(0, str(ROOT / "src"))
        from svif.continuity.agnir import AgnirFilesystemContinuityProvider
        provider = AgnirFilesystemContinuityProvider(project)
        values = provider._parse_discovery((project / "AGNIR.yaml").read_text(encoding="utf-8"))
        identity = values.get(("project", "identity"))
        require(isinstance(identity, str) and bool(identity), "native bootstrap did not establish Project identity")
        snapshot = provider.load(identity)
        require(bool(snapshot.state) and bool(snapshot.next_actions) and bool(snapshot.evidence), "native checkpoint is incomplete")
        require(readme.strip() in (project / "README.md").read_text(encoding="utf-8"), "README original content was destroyed")
        require(agents.strip() in (project / "AGENTS.md").read_text(encoding="utf-8"), "AGENTS original content was destroyed")
        svif = provider._parse_discovery((project / "SVIF.yaml").read_text(encoding="utf-8"))
        require(svif.get(("project", "identity")) == identity, "Svif/Agnir identity mismatch")
        before = file_map(project)
        phase2 = session_dir / "cold-resume"
        phase2.mkdir()
        # A new process and thread, not thread/resume or transcript injection.
        with NativeClient(binary, env, phase2) as client:
            thread2, answer = client.exercise(project,
                "Use Svif to recover this Project from its own durable files. Do not write anything. "
                "Independently inspect RESULT.md. Respond with JSON only containing project_identity, "
                "result_sha256, and remaining_tasks (an array of genuinely outstanding tasks).",
                skill, readonly=True, model=args.model)
        require(thread2 != thread1, "cold recovery reused a prior conversation")
        parsed = json.loads(answer.strip().removeprefix("```json").removesuffix("```").strip())
        require(parsed.get("project_identity") == identity and parsed.get("result_sha256") == digest,
                "fresh context failed to reconstruct exact Project/result identity")
        require(parsed.get("remaining_tasks") == [], "fresh context did not recover the completed next-action state")
        require(file_map(project) == before, "read-only cold recovery modified Project files")
        phase3 = session_dir / "idempotency"
        phase3.mkdir()
        with NativeClient(binary, env, phase3) as client:
            thread3, _ = client.exercise(project,
                "Enable and use Svif for this already-initialized Project. There is no new task. "
                "Validate the existing binding and completed result without recreating identity, rewriting instructions, "
                "or adding a redundant checkpoint. Do not publish or deploy.", skill, model=args.model)
        require(len({thread1, thread2, thread3}) == 3, "idempotency reused a prior conversation")
        require(file_map(project) == before, "idempotent reuse changed existing Project truth")
        report["model_exercise"] = "passed-positive-scenarios"
        report["exercise"] = {"threads": [thread1, thread2, thread3], "project_identity": identity,
                              "result_sha256": digest, "fresh_resume": True, "idempotent_reuse": True}
        report["next"] = "Positive native scenarios passed. Complete the negative host scenarios in conformance/RELEASE_READINESS.md before release sign-off."
        return 0
    except (OSError, ValueError, KeyError, RuntimeError, subprocess.SubprocessError) as exc:
        report["error"] = str(exc)
        if report["model_exercise"] == "in-progress":
            report["model_exercise"] = "failed-or-blocked"
        return 1
    finally:
        (session_dir / "report.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
        (output / "latest-report.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
        print(json.dumps(report, indent=2))


if __name__ == "__main__":
    raise SystemExit(main())
