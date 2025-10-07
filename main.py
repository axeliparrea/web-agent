"""
Unified Job Bot Runner
----------------------
Run either the LinkedIn or Indeed bot from the repo root.

Usage examples:
  python main.py linkedin   # runs Auto_job_applier_linkedIn/runAiBot.py
  python main.py indeed     # runs indeed_bot/indeed_bot.py

Optionally you can run as a module:
  python -m main linkedin

This script delegates execution to each bot in its own working directory,
so their relative file paths and configs keep working unchanged.
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


def run_script(script_path: Path, extra_args: list[str] | None = None) -> int:
    """Run a Python script in its own folder using the current Python executable.

    Args:
        script_path: Absolute path to the script to run.

    Returns:
        The process return code.
    """
    if not script_path.exists():
        print(f"Error: script not found: {script_path}")
        return 1
    cwd = str(script_path.parent)
    cmd = [sys.executable, script_path.name]
    if extra_args:
        cmd.extend(extra_args)
    # Delegate to the child script within its directory to preserve relative paths
    proc = subprocess.run(cmd, cwd=cwd)
    return proc.returncode


def main() -> int:
    root = Path(__file__).parent.resolve()

    parser = argparse.ArgumentParser(
        description="Run LinkedIn or Indeed job apply bots from a single entrypoint.",
    )
    parser.add_argument(
        "platform",
        choices=["linkedin", "indeed"],
        help="Which bot to run",
    )
    args, rest = parser.parse_known_args()

    if args.platform == "linkedin":
        script = root / "Auto_job_applier_linkedIn" / "runAiBot.py"
    else:  # indeed
        script = root / "indeed_bot" / "indeed_bot.py"

    return run_script(script, rest)


if __name__ == "__main__":
    sys.exit(main())
