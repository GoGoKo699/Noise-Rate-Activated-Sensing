"""Print a seeded example; write only when --output is explicitly supplied."""
from pathlib import Path
import argparse
import json
import platform
import sys

import numpy as np
import scipy
import sympy

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src'))
import nras


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    samples = nras.sample_stopped(4, 1, 3, 30000, np.random.default_rng(1101))
    deadline = nras.sample_stopped(5, 1, 3, 20000, np.random.default_rng(1102), deadline=20)
    mean, var = nras.first_passage_moments(4, 1, 3)
    result = {
        'scope': 'Seeded numerical examples for the ideal model; not independent proof validation.',
        'environment': {'python': platform.python_version(), 'numpy': np.__version__,
                        'scipy': scipy.__version__, 'sympy': sympy.__version__},
        'first_passage': {'a': 1, 'b': 3, 'd': 4, 'samples': 30000, 'seed': 1101,
                          'mean_exact': mean, 'mean_sample': float(samples.times.mean()),
                          'variance_exact': var, 'variance_sample': float(samples.times.var(ddof=1)),
                          'laplace_q': .1, 'laplace_exact': nras.first_passage_laplace(4, 1, 3, .1),
                          'laplace_sample': float(np.exp(-.1*samples.times).mean())},
        'deadline': {'a': 1, 'b': 3, 'd': 5, 'T': 20, 'samples': 20000, 'seed': 1102,
                     'failures_retained': int((~deadline.completed).sum()),
                     'success_fraction': float(deadline.completed.mean()),
                     'information_sample': float(25*deadline.completed.mean()),
                     'information_certified_lower': nras.threefold_information_lower_bound(1, 20),
                     'fixed_rate_information_upper': 20},
        'rate_contrast': nras.rate_contrast(1, 3),
        'finite_cadence_speeds': {str(dt): nras.finite_cadence_speed(1, 3, dt)
                                  for dt in [.01, .1, 1.]},
    }
    text = json.dumps(result, indent=2, allow_nan=False) + '\n'
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding='utf-8')
    print(text, end='')


if __name__ == '__main__':
    main()
