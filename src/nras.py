"""Reference calculations for the ideal shared-axis sensing model.

Time is physical sensor exposure. The simulator retains deadline failures;
it does not simulate readout errors or a finite-bandwidth environment.
"""
from __future__ import annotations

from dataclasses import dataclass
import math
from typing import Sequence

import numpy as np
from numpy.typing import NDArray

I = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.diag([1, -1]).astype(complex)


def _positive(value: float, name: str) -> float:
    value = float(value)
    if not math.isfinite(value) or value <= 0:
        raise ValueError(f"{name} must be finite and positive")
    return value


def noise_operator(phi: float) -> NDArray[np.complex128]:
    """The Hermitian unitary N_phi = cos(phi) X + sin(phi) Y."""
    if not math.isfinite(phi):
        raise ValueError("phi must be finite")
    return math.cos(phi) * X + math.sin(phi) * Y


def rotation(phase: float) -> NDArray[np.complex128]:
    return np.diag(np.exp(-0.5j * phase * np.array([1.0, -1.0])))


def path_operators(phi: float, signal: float, rate: float, slope: float):
    """Zero-gauge A and B along (omega, phi) = (omega0+u, phi0+c*u)."""
    rate = _positive(rate, "rate")
    if not all(map(math.isfinite, (signal, slope))):
        raise ValueError("signal and slope must be finite")
    jump = math.sqrt(rate) * noise_operator(phi)
    derivative = math.sqrt(rate) * slope * (-math.sin(phi) * X + math.cos(phi) * Y)
    a_op = derivative.conj().T @ derivative
    b_op = signal * Z / 2 - 0.5j * (
        derivative.conj().T @ jump - jump.conj().T @ derivative
    )
    return a_op, b_op


def trajectory(omega: float, phi: float, durations: Sequence[float],
               signals: Sequence[float], jumps_after: Sequence[bool]):
    """Direct chronological matrix product and independently accumulated signed time."""
    if not (len(durations) == len(signals) == len(jumps_after)):
        raise ValueError("trajectory arrays must have the same length")
    if not math.isfinite(omega):
        raise ValueError("omega must be finite")
    unitary = I.copy()
    signed_time = 0.0
    count = 0
    jump = noise_operator(phi)
    for dt, signal, has_jump in zip(durations, signals, jumps_after):
        if not math.isfinite(dt) or dt < 0 or not math.isfinite(signal):
            raise ValueError("durations must be nonnegative and all values finite")
        unitary = rotation(omega * signal * dt) @ unitary
        signed_time += (-1) ** count * signal * dt
        if has_jump:
            unitary = jump @ unitary
            count += 1
    return unitary, signed_time, count


def control_speed(signals: Sequence[float], rates: Sequence[float]):
    """Return the optimal leading speed and a maximizing pair of settings."""
    s = np.asarray(signals, dtype=float)
    g = np.asarray(rates, dtype=float)
    if s.ndim != 1 or s.size == 0 or s.shape != g.shape:
        raise ValueError("settings must be nonempty equal-length one-dimensional arrays")
    if not np.isfinite(s).all() or not np.isfinite(g).all() or (g <= 0).any():
        raise ValueError("signals must be finite and rates finite and positive")
    speeds = np.abs(s[:, None] * g[None, :] - s[None, :] * g[:, None]) / (
        g[:, None] + g[None, :]
    )
    pair = tuple(map(int, np.unravel_index(np.argmax(speeds), speeds.shape)))
    return float(speeds[pair]), pair


def rate_contrast(a: float, b: float) -> float:
    a, b = _positive(a, "a"), _positive(b, "b")
    if b < a:
        raise ValueError("b must be at least a")
    return (b - a) / (b + a)


def first_passage_exponent(q: float, a: float, b: float) -> float:
    """k(q) with E exp(-q*tau_d) = exp(-d*k(q)), including the finite MGF domain."""
    a, b = _positive(a, "a"), _positive(b, "b")
    rate_contrast(a, b)
    critical = (math.sqrt(b) - math.sqrt(a)) ** 2 / 2
    if not math.isfinite(q) or q < -critical:
        raise ValueError("q lies outside the real finite moment-generating domain")
    delta = (b - a) / 2
    if q == 0:
        return 0.0
    root = math.sqrt(max(0.0, delta * delta + q * (a + b + q)))
    # Rationalize to avoid cancellation near q=0 when b>a.
    return q * (a + b + q) / (root + delta) if root + delta else root - delta


def first_passage_laplace(d: float, a: float, b: float, q: float) -> float:
    d = _positive(d, "d")
    return math.exp(-d * first_passage_exponent(q, a, b))


def first_passage_moments(d: float, a: float, b: float):
    d = _positive(d, "d")
    r = rate_contrast(a, b)
    if r == 0:
        return math.inf, math.inf
    return d / r, 8 * a * b * d / (b - a) ** 3


def finite_cadence_speed(a: float, b: float, interval: float) -> float:
    interval = _positive(interval, "interval")
    rate_contrast(a, b)
    pa = -math.expm1(-2 * a * interval) / 2
    pb = -math.expm1(-2 * b * interval) / 2
    return pa * pb * (1 / a - 1 / b) / (interval * (pa + pb))


def threefold_information_lower_bound(a: float, total_time: float) -> float:
    a = _positive(a, "a")
    total_time = _positive(total_time, "total_time")
    return total_time ** 2 / 16 * max(0.0, 1 - 3 / (a * total_time))


def symmetric_signed_moments(rate: float, time: float):
    rate = _positive(rate, "rate")
    if not math.isfinite(time) or time < 0:
        raise ValueError("time must be finite and nonnegative")
    transient = -math.expm1(-2 * rate * time)
    return transient / (2 * rate), time / rate - transient / (2 * rate * rate)


@dataclass(frozen=True)
class StoppedSamples:
    times: NDArray[np.float64]
    signed_times: NDArray[np.float64]
    completed: NDArray[np.bool_]
    jumps: NDArray[np.int64]


def sample_stopped(d: float, a: float, b: float, size: int,
                   rng: np.random.Generator, deadline: float | None = None,
                   max_events: int = 1_000_000) -> StoppedSamples:
    """Exact event simulation. An event guard raises; it never discards long runs.

    Completed paths reach signed time d in the even sector. On failure the
    returned physical time is exactly the deadline. A finite deadline is
    required at equal rates because the untruncated mean stopping time diverges.
    """
    d = _positive(d, "d")
    r = rate_contrast(a, b)
    if not isinstance(size, int) or isinstance(size, bool) or size <= 0:
        raise ValueError("size must be a positive integer")
    if not isinstance(max_events, int) or max_events <= 0:
        raise ValueError("max_events must be a positive integer")
    if deadline is None:
        if r == 0:
            raise ValueError("equal-rate sampling requires a finite deadline")
        limit = math.inf
    else:
        limit = _positive(deadline, "deadline")
    t = np.zeros(size)
    x = np.zeros(size)
    even = np.ones(size, dtype=bool)
    active = np.ones(size, dtype=bool)
    completed = np.zeros(size, dtype=bool)
    jumps = np.zeros(size, dtype=np.int64)
    for _ in range(max_events):
        idx = np.flatnonzero(active)
        if not idx.size:
            return StoppedSamples(t, x, completed, jumps)
        e = even[idx]
        waits = rng.exponential(1 / np.where(e, a, b))
        crossing = np.where(e, np.maximum(0.0, d - x[idx]), math.inf)
        remaining = np.maximum(0.0, limit - t[idx])
        success = (crossing <= waits) & (crossing <= remaining)
        timeout = (~success) & (remaining <= waits)
        event = ~(success | timeout)
        elapsed = np.minimum(np.minimum(waits, crossing), remaining)
        t[idx] += elapsed
        x[idx] += np.where(e, elapsed, -elapsed)
        x[idx[success]] = d
        completed[idx[success]] = True
        active[idx[success | timeout]] = False
        even[idx[event]] = ~even[idx[event]]
        jumps[idx[event]] += 1
    if not active.any():
        return StoppedSamples(t, x, completed, jumps)
    raise RuntimeError("event guard exceeded; increase max_events or use a deadline")
