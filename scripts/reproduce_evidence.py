"""Evaluate deterministic evidence tables; write only with explicit --output."""
from pathlib import Path
import argparse
import json
import math
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src'))
import preset
import risk


def evidence():
    times = [.5, 1., 2., 3., 4., 10., 100., 1000.]
    rows = []
    for time in times:
        rows.append({
            'time': time,
            'fixed_rate_information_upper': min(time**2, time),
            'fixed_recovery_information': preset.mixture_information([1], [1], [1], time),
            'balanced_echo_information': preset.echo_information(1, 3, .75*time, .25*time),
            'optimal_leading_design_information': preset.mixture_information([1, 1], [1, 3], [.75, .25], time),
            'fair_design_information': preset.mixture_information([1, 1], [1, 3], [.5, .5], time),
            'fixed_imbalance_echo_information': preset.echo_information(1, 3, .76*time, .24*time),
            'parallel_dephasing_information': risk.dephased_mixture_information(1, 3, .75, time, .01),
        })
    return {
        'scope': 'Exact formula evaluations, not global-risk estimates or finite-time optimality claims.',
        'parameters': {'a': 1, 'b': 3, 'kappa': .01, 'shared_unknown_direction': True},
        'local_information': rows,
        'finite_certificate': {
            'a_times_T': 10,
            'kappa_over_a': .01,
            'information': risk.dephased_mixture_information(1, 3, .75, 10, .01),
            'ideal_fixed_rate_upper': 10,
            'sufficient_kappa_over_a_threshold': risk.threefold_dephasing_tolerance(),
            'threshold_expression': 'log(400/231)/40',
        },
        'global_risk_bounds': {
            'scope': 'Lower and upper bounds, not exact or simulated minimax risks.',
            'frequency_interval': [-1, 1],
            'prior_half_width': .5,
            'rows': [{
                'time': time,
                'fixed_lower': risk.fixed_rate_risk_lower(1, time, .5),
                'fixed_upper': risk.fixed_rate_risk_upper(1, time, 2),
                'controlled_lower': risk.controlled_risk_lower(1, 3, time, .5),
            } for time in [10., 100., 1000., 10000.]],
        },
        'rate_contrast': .5,
        'fair_to_optimal_leading_information_ratio': .8,
        'preset_finite_separation_threshold': 1+math.sqrt(3),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    text = json.dumps(evidence(), indent=2, allow_nan=False) + '\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding='utf-8')
    print(text, end='')


if __name__ == '__main__':
    main()
