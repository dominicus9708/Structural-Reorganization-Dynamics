from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from reproduce_dynamics import run_all_checks  # noqa: E402


def test_all_reproducibility_checks_pass() -> None:
    results = run_all_checks()
    failures = [r.name for r in results if not r.passed]
    assert not failures, f"Failed reproducibility checks: {failures}"


def test_check_names_are_unique() -> None:
    names = [r.name for r in run_all_checks()]
    assert len(names) == len(set(names))
