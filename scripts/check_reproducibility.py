"""Regenerate both recorded examples without writing to the repository."""
from __future__ import annotations

import json
import math
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
PAIRS = (('reproduce.py', 'example.json'), ('reproduce_evidence.py', 'evidence.json'))


def compare(actual, expected, location: str = '$') -> None:
    """Compare structure exactly and numbers to a declared cross-version tolerance."""
    if isinstance(expected, dict):
        if not isinstance(actual, dict) or set(actual) != set(expected):
            raise ValueError(f'{location}: object keys differ')
        for key in expected:
            compare(actual[key], expected[key], f'{location}.{key}')
    elif isinstance(expected, list):
        if not isinstance(actual, list) or len(actual) != len(expected):
            raise ValueError(f'{location}: array lengths differ')
        for index, (a, e) in enumerate(zip(actual, expected)):
            compare(a, e, f'{location}[{index}]')
    elif isinstance(expected, bool) or not isinstance(expected, (int, float)):
        if type(actual) is not type(expected) or actual != expected:
            raise ValueError(f'{location}: expected {expected!r}, got {actual!r}')
    elif isinstance(actual, bool) or not isinstance(actual, (int, float)) or not math.isclose(
            actual, expected, rel_tol=1e-10, abs_tol=1e-14):
        raise ValueError(f'{location}: expected {expected!r}, got {actual!r}')


def main() -> int:
    for script, record in PAIRS:
        run = subprocess.run([sys.executable, str(ROOT/'scripts'/script)],
                             cwd=ROOT, capture_output=True, text=True, check=True)
        actual = json.loads(run.stdout)
        expected = json.loads((ROOT/'results'/record).read_text(encoding='utf-8'))
        # The producer records its runtime, not a requirement to misreport it.
        actual_environment = actual.pop('environment', None)
        expected_environment = expected.pop('environment', None)
        if (actual_environment is None) != (expected_environment is None):
            raise ValueError(f'{record}: environment metadata disappeared')
        if expected_environment is not None:
            if not isinstance(actual_environment, dict) or set(actual_environment) != set(expected_environment):
                raise ValueError(f'{record}: environment metadata keys changed')
        compare(actual, expected, record)
        print(f'{record}: regenerated values match; current environment={actual_environment}')
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except (ValueError, subprocess.CalledProcessError) as exc:
        print(exc, file=sys.stderr)
        sys.exit(1)
