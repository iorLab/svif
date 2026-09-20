#!/usr/bin/env python3
"""Observe native Codex installation/discovery without model calls or user auth.

Uses a new HOME/CODEX_HOME and a frozen copy of the local Plugin tree. Never
modifies the user's installed plugins. This does NOT certify task execution or
fresh-LLM-session recovery; those require the exercises in LOCAL_ACCEPTANCE.md.
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
import threading
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def tree_hashes(root: Path) -> dict[str, str]:
    result = {}
    for path in sorted(root.rglob("*")):
        if path.is_symlink():
            raise ValueError("package contains a symlink")
        if path.is_file():
            result[path.relative_to(root).as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
    return result


def discovered_skills(codex: str, env: dict[str, str], project: Path) -> dict:
    """Ask a genuinely new native App Server process to enumerate its skills."""
    messages: queue.Queue[str | None] = queue.Queue()
    with (project.parent / "app-server.stderr.log").open("w", encoding="utf-8") as errors:
        process = subprocess.Popen([codex, "app-server"], cwd=project, env=env,
                                   stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                   stderr=errors, text=True, encoding="utf-8")
        def receive():
            for line in process.stdout:
                messages.put(line)
            messages.put(None)
        reader = threading.Thread(target=receive, daemon=True)
        reader.start()
        def request(identifier, method, params):
            process.stdin.write(json.dumps({"id": identifier, "method": method, "params": params}) + "\n")
            process.stdin.flush()
            deadline = time.monotonic() + 30
            while time.monotonic() < deadline:
                line = messages.get(timeout=max(0.1, deadline - time.monotonic()))
                if line is None:
                    raise RuntimeError("native App Server exited before its response")
                message = json.loads(line)
                if message.get("id") == identifier:
                    if "error" in message: raise RuntimeError(str(message["error"]))
                    return message["result"]
            raise TimeoutError("native skill discovery timed out")
        try:
            request(1, "initialize", {"clientInfo": {"name": "svif-readiness", "version": "0.2.0"},
                                       "capabilities": {"experimentalApi": True}})
            process.stdin.write(json.dumps({"method": "initialized"}) + "\n")
            process.stdin.flush()
            return request(2, "skills/list", {"cwds": [str(project)], "forceReload": True})
        finally:
            process.terminate()
            try: process.wait(timeout=5)
            except subprocess.TimeoutExpired: process.kill(); process.wait()
            reader.join(timeout=5)
            process.stdin.close()
            process.stdout.close()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path, help="new isolated acceptance directory")
    parser.add_argument("--codex", default="codex")
    args = parser.parse_args()
    output = args.output.resolve()
    if output.exists():
        parser.error("output must not already exist; do not reuse a populated test home")
    if output.is_relative_to(ROOT / "plugin"):
        parser.error("output must not be inside the Plugin source")
    output.mkdir(parents=True)
    report = {"native_install": "not-observed", "native_discovery": "not-observed",
              "native_task_and_fresh_session": "not-observed", "release_ready": False,
              "host": platform.platform(), "source_file_sha256": tree_hashes(ROOT / "plugin")}
    try:
        codex = shutil.which(args.codex)
        if codex is None: raise RuntimeError("native Codex executable is unavailable")
        home, codex_home, market, project = [output / x for x in ("home", "codex-home", "marketplace", "ordinary-project")]
        for path in (home, codex_home, market, project): path.mkdir()
        shutil.copytree(ROOT / "plugin", market / "plugin")
        marketplace_path = market / ".agents/plugins"
        marketplace_path.mkdir(parents=True)
        shutil.copyfile(ROOT / ".agents/plugins/marketplace.json", marketplace_path / "marketplace.json")
        (project / "README.md").write_text("# Ordinary acceptance Project\nPreserve this original sentence.\n", encoding="utf-8")
        (project / "AGENTS.md").write_text("Preserve original Project instructions.\n", encoding="utf-8")
        # Do not inherit API keys, provider credentials or the user's plugin state.
        env = {k: v for k, v in os.environ.items() if k in {"PATH", "SystemRoot", "WINDIR", "TEMP", "TMP", "LANG"}}
        env.update({"HOME": str(home), "USERPROFILE": str(home), "CODEX_HOME": str(codex_home)})
        def run(*command):
            result = subprocess.run([codex, *command], env=env, cwd=project, capture_output=True,
                                    text=True, encoding="utf-8", timeout=60)
            if result.returncode:
                raise RuntimeError(f"native command failed: {' '.join(command)}: {result.stderr[-3000:]}")
            return result.stdout
        report["codex_version"] = run("--version").strip()
        report["marketplace"] = run("plugin", "marketplace", "add", str(market), "--json")
        installed = json.loads(run("plugin", "add", "svif@svif", "--json"))
        report["installation_receipt"] = installed
        report["listing"] = json.loads(run("plugin", "list", "--json"))
        matches = [x for x in report["listing"].get("installed", []) if x.get("name") == "svif" and x.get("installed") is True and x.get("enabled") is True]
        if len(matches) != 1: raise RuntimeError("native host did not report exactly one installed/enabled Svif")
        version = json.loads((ROOT / "plugin/plugin.json").read_text())["version"]
        if matches[0].get("version") != version: raise RuntimeError("native version differs from tested source")
        installed_path = Path(installed["installedPath"])
        if tree_hashes(installed_path) != report["source_file_sha256"]:
            raise RuntimeError("installed package bytes differ from tested source")
        report["native_install"] = "passed"
        result = discovered_skills(codex, env, project)
        report["skills_list"] = result
        skills = [s for item in result.get("data", []) for s in item.get("skills", []) if s.get("name") == "svif" and s.get("enabled", True)]
        if len(skills) != 1: raise RuntimeError("new native process did not discover one enabled Svif Skill")
        skill = Path(skills[0]["path"])
        if hashlib.sha256(skill.read_bytes()).hexdigest() != report["source_file_sha256"]["skills/svif/SKILL.md"]:
            raise RuntimeError("discovered native Skill differs from tested source")
        report["native_discovery"] = "passed"
        return_code = 0
    except (OSError, ValueError, KeyError, RuntimeError, TimeoutError, queue.Empty, subprocess.SubprocessError) as exc:
        report["blocker"] = str(exc)
        return_code = 2
    (output / "receipt.json").write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({k: report[k] for k in ("native_install", "native_discovery", "native_task_and_fresh_session", "release_ready")}))
    print(output / "receipt.json")
    return return_code


if __name__ == "__main__":
    raise SystemExit(main())
