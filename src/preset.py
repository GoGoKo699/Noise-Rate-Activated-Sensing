"""Local classical information for preset rate-diversity protocols.

All formulas retain the setting, jump counts, and final readout. Nuisance
elimination is performed after pooling the full Fisher matrices. These are
local-information formulas, not global mean-square-error guarantees.
"""
from __future__ import annotations

import math
from typing import Sequence

import numpy as np
from numpy.typing import NDArray


def _finite(value: float, name: str, *, positive: bool = False) -> float:
    value = float(value)
    if not math.isfinite(value) or (positive and value <= 0):
        qualifier = 'finite and positive' if positive else 'finite'
        raise ValueError(f'{name} must be {qualifier}')
    return value


def echo_statistics(a: float, b: float, t_a: float, t_b: float) -> tuple[float, float, float]:
    """Return signed time D, mean signed count mu, and count variance V."""
    a, b = _finite(a, 'a', positive=True), _finite(b, 'b', positive=True)
    t_a, t_b = _finite(t_a, 't_a'), _finite(t_b, 't_b')
    if min(t_a, t_b) < 0 or t_a + t_b <= 0:
        raise ValueError('block durations must be nonnegative with positive total')
    return t_a - t_b, a * t_a - b * t_b, a * t_a + b * t_b


def echo_fisher(a: float, b: float, t_a: float, t_b: float,
                *, unknown_rates: bool = False) -> NDArray[np.float64]:
    """Fisher matrix ordered (omega, phi[, a, b]); durations are held fixed."""
    d, mu, var = echo_statistics(a, b, t_a, t_b)
    size = 4 if unknown_rates else 2
    fisher = np.zeros((size, size))
    fisher[:2, :2] = [[d * d, -2 * d * mu], [-2 * d * mu, 4 * (var + mu * mu)]]
    if unknown_rates:
        fisher[2, 2], fisher[3, 3] = t_a / a, t_b / b
    return fisher


def echo_information(a: float, b: float, t_a: float, t_b: float) -> float:
    """Efficient information, also valid with a,b as additional nuisances."""
    d, mu, var = echo_statistics(a, b, t_a, t_b)
    return d * d / (1 + mu * mu / var)


def _settings(signals: Sequence[float], rates: Sequence[float],
              probabilities: Sequence[float]) -> tuple[NDArray, NDArray, NDArray]:
    s, g, p = (np.asarray(x, dtype=float) for x in (signals, rates, probabilities))
    if s.ndim != 1 or s.size == 0 or s.shape != g.shape or s.shape != p.shape:
        raise ValueError('settings must be nonempty equal-length one-dimensional arrays')
    if not all(np.isfinite(x).all() for x in (s, g, p)) or (g <= 0).any() or (p < 0).any():
        raise ValueError('signals must be finite, rates positive, and probabilities nonnegative')
    if not math.isclose(float(p.sum()), 1., rel_tol=1e-12, abs_tol=1e-12):
        raise ValueError('probabilities must sum to one')
    return s, g, p / p.sum()


def mixture_fisher(signals: Sequence[float], rates: Sequence[float],
                   probabilities: Sequence[float], time: float,
                   *, unknown_rates: bool = False) -> NDArray[np.float64]:
    """Choose one setting for the entire duration and retain its label.

    Probabilities are fixed controls, not differentiated with the unknown rates.
    The optional rate block is diagonal; rate scores are orthogonal to the
    target and direction scores for this full-record likelihood.
    """
    s, g, p = _settings(signals, rates, probabilities)
    time = _finite(time, 'time', positive=True)
    size = 2 + (len(g) if unknown_rates else 0)
    fisher = np.zeros((size, size))
    fisher[0, 0] = time ** 2 * np.dot(p, s * s)
    fisher[0, 1] = fisher[1, 0] = -2 * time ** 2 * np.dot(p, s * g)
    fisher[1, 1] = 4 * (time ** 2 * np.dot(p, g * g) + time * np.dot(p, g))
    if unknown_rates:
        fisher[2:, 2:] = np.diag(p * time / g)
    return fisher


def mixture_information(signals: Sequence[float], rates: Sequence[float],
                        probabilities: Sequence[float], time: float) -> float:
    """Efficient local information using a stable nonnegative residual formula."""
    s, g, p = _settings(signals, rates, probabilities)
    time = _finite(time, 'time', positive=True)
    noise = np.dot(p, g) / time
    slope = np.dot(p, s * g) / (np.dot(p, g * g) + noise)
    return float(time ** 2 * (np.dot(p, (s - slope * g) ** 2) + slope * slope * noise))


def mixture_coefficient(signals: Sequence[float], rates: Sequence[float],
                        probabilities: Sequence[float]) -> float:
    """Limit of efficient information / time**2 for the fixed labelled design."""
    s, g, p = _settings(signals, rates, probabilities)
    slope = np.dot(p, s * g) / np.dot(p, g * g)
    return float(np.dot(p, (s - slope * g) ** 2))
