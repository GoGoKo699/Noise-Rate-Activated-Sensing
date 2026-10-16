"""Global-risk bounds and a scoped residual-dephasing calculation.

The global bounds apply to the hard-deadline task in docs/GLOBAL_RISK.md.
The dephasing formula is attainable local information for the specified
recorded random-rate and random-angle readout, not a global risk or optimum.
"""
from __future__ import annotations

import math


def _positive(value: float, name: str) -> float:
    value = float(value)
    if not math.isfinite(value) or value <= 0:
        raise ValueError(f'{name} must be finite and positive')
    return value


def prior_information(half_width: float) -> float:
    """Fisher information of cos^2(pi*u/(2*h))/h on (-h,h)."""
    h = _positive(half_width, 'half_width')
    return (math.pi / h) ** 2


def fixed_rate_risk_lower(rate: float, time: float, half_width: float) -> float:
    """Minimax MSE lower bound; no unbiasedness assumption is needed."""
    rate, time = _positive(rate, 'rate'), _positive(time, 'time')
    return 1 / (time / rate + prior_information(half_width))


def controlled_qfi_envelope(a: float, b: float, time: float) -> float:
    """Supersolution for the nuisance-path QFI; not the exact optimum."""
    a, b, time = _positive(a, 'a'), _positive(b, 'b'), _positive(time, 'time')
    if b <= a:
        raise ValueError('controlled bound requires b > a')
    r = (b - a) / (b + a)
    linear = 4 * b / (a + b) ** 2
    return (r * time + math.sqrt(linear * time)) ** 2


def controlled_risk_lower(a: float, b: float, time: float, half_width: float) -> float:
    """Maximum of two valid minimax bounds obtained from different priors.

    The min in the denominator does NOT bound the QFI of one common path:
    time^2 uses constant phi, while the envelope uses phi'=1/(a+b).
    """
    envelope = controlled_qfi_envelope(a, b, time)
    return 1 / (min(time ** 2, envelope) + prior_information(half_width))


def fixed_rate_risk_upper(rate: float, time: float, width: float) -> float:
    """Conservative uniform MSE bound for paid, constant-time no-jump trials."""
    rate, time, width = (_positive(x, n) for x, n in
                         [(rate, 'rate'), (time, 'time'), (width, 'width')])
    tau = min(1 / rate, math.pi / (2 * width))
    count = int(math.floor(time / tau))
    if count == 0:
        return width ** 2 / 4
    p = math.exp(-rate * tau)
    bound = 4 / (tau ** 2 * (count + 1) * p)
    bound += width ** 2 / 4 * (1 - p) ** count
    # The midpoint estimator is independently available at any time.
    return min(width ** 2 / 4, bound)


def random_angle_weight(kappa: float, time: float) -> float:
    """Averaged phase information at contrast exp(-2*kappa*time)."""
    kappa = float(kappa)
    time = _positive(time, 'time')
    if not math.isfinite(kappa) or kappa < 0:
        raise ValueError('kappa must be finite and nonnegative')
    argument = -4 * kappa * time
    squared_contrast = math.exp(argument)
    return squared_contrast / (1 + math.sqrt(-math.expm1(argument)))


def dephased_mixture_information(a: float, b: float, p: float,
                                time: float, kappa: float) -> float:
    """Exact local information for the prescribed full-record readout."""
    a, b, time = _positive(a, 'a'), _positive(b, 'b'), _positive(time, 'time')
    if not math.isfinite(p) or not 0 <= p <= 1:
        raise ValueError('p must lie in [0,1]')
    mean = p * a + (1 - p) * b
    second = p * a * a + (1 - p) * b * b
    variance = p * (1 - p) * (a - b) ** 2
    ideal = time ** 2 * (variance + mean / time) / (second + mean / time)
    return random_angle_weight(kappa, time) * ideal


def dephasing_all_strategy_upper(kappa: float, time: float) -> float:
    """Information upper bound with an unobserved parallel Lindblad error."""
    kappa, time = _positive(kappa, 'kappa'), _positive(time, 'time')
    return time / (4 * kappa)


def threefold_dephasing_tolerance() -> float:
    """Sufficient kappa/a threshold at a*T=10, b=3a, and p=3/4."""
    return math.log(400 / 231) / 40
