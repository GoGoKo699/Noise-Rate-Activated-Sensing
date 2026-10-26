"""Finite checks of the adaptive activity lemma and contact precision bounds.

The adaptive-controller checks use the upper-bound relaxation: arbitrary
boundary instruments, but at most m cell-interior contacts on every branch.
They are not advertised as lower protocols with only n−1 total contacts.
The separate early-readout checks do enforce that total-contact budget.
"""
import unittest
import numpy as np
from numpy.testing import assert_allclose
from scipy.linalg import expm

from test_microscopic import (
    I, X, Y, Z, EVEN, ODD, YL, INITIAL, calibration, axis,
    joint_unitary, reduced_cell, conjugate, numerical_fisher,
    recovery_likelihood, echo_likelihood,
)


def append_cell(vector, unitary):
    """Apply the actual S--new-bath unitary to a purified existing state."""
    incoming = vector.reshape(2, -1)
    isometry = unitary.reshape(2, 2, 2, 2)[:, :, :, 0]
    return np.einsum('abs,sc->acb', isometry, incoming).reshape(-1)


def sensor_map(matrix, vector):
    return (matrix @ vector.reshape(2, -1)).reshape(-1)


def measured_choice(index, history, cap):
    """Parameter-independent quantum instruments; no branch is pruned."""
    if sum(history) == cap:
        return {0: I}
    rotation = expm(-.5j * (.43 + .19 * index) * Y) @ expm(-.5j * (.31 + .27 * sum(history)) * Z)
    # Rare first-cell activation checks that no normalized-branch shortcuts
    # replace the derivative of the complete experiment.
    rates = (.003, .0002) if index == 0 else (.37 + .05 * history[-1], .07)
    active = rotation @ np.diag(np.sqrt(rates)) @ rotation.conj().T
    inactive = rotation @ np.diag(np.sqrt(1 - np.array(rates))) @ rotation.conj().T
    assert_allclose(active.conj().T @ active + inactive.conj().T @ inactive, I, atol=2e-14)
    return {0: inactive, 1: active}


def cell_unitary(g, interval, epsilon, phi, active):
    hamiltonian = epsilon * np.kron(Z, I) / 2 + g * np.kron(axis(phi), X)
    if active:
        half = expm(-.5j * interval * hamiltonian)
        return half @ np.kron(Z, I) @ half
    return expm(-1j * interval * hamiltonian)


def adaptive_purification(g, interval, cells, cap, epsilon=0., phi=.37,
                          source=None, derivative_step=1e-6):
    """Classical histories are orthogonal retained purification registers.

    source=(index, activity) inserts just that cell's nuisance-path tangent;
    all other cells and the input stay at the operating point. The quantum
    measurement maps themselves remain parameter independent.
    """
    chi = g * interval
    slope = 1 / (2 * g * np.tan(chi))
    initial = np.array([1, 0, 0, 1], dtype=complex) / np.sqrt(2)
    states = {(): initial}
    for index in range(cells):
        following = {}
        for history, vector in states.items():
            for active, measurement in measured_choice(index, history, cap).items():
                measured = sensor_map(measurement, vector)
                if source is not None and index == source[0]:
                    if active != source[1]:
                        unitary = np.zeros((4, 4), dtype=complex)
                    else:
                        plus = cell_unitary(g, interval, derivative_step,
                                            phi + slope * derivative_step, active)
                        minus = cell_unitary(g, interval, -derivative_step,
                                             phi - slope * derivative_step, active)
                        unitary = (plus - minus) / (2 * derivative_step)
                else:
                    unitary = cell_unitary(g, interval, epsilon, phi, active)
                following[history + (active,)] = append_cell(measured, unitary)
        states = following
    return states


def inner(left, right):
    assert left.keys() == right.keys()
    return sum(np.vdot(left[key], right[key]) for key in left)


def norm_squared(states):
    return float(inner(states, states).real)


def add_sources(sources):
    return {key: sum(source[key] for source in sources) for key in sources[0]}


def source_data(g, interval, cells, cap):
    inactive = [adaptive_purification(g, interval, cells, cap, source=(index, 0))
                for index in range(cells)]
    active = [adaptive_purification(g, interval, cells, cap, source=(index, 1))
              for index in range(cells)]
    return inactive, active


def accessible_likelihood(g, interval, cells, cap):
    # Product tetrahedral POVM on sensor and protected ancilla, while every
    # bath is traced out. No environmental derivative information is read.
    vertices = np.array([[1, 1, 1], [1, -1, -1], [-1, 1, -1], [-1, -1, 1]]) / np.sqrt(3)
    local = [(I + v[0] * X + v[1] * Y + v[2] * Z) / 4 for v in vertices]
    effects = [np.kron(left, right) for left in local for right in local]
    def likelihood(point):
        states = adaptive_purification(g, interval, cells, cap, epsilon=point[0], phi=point[1])
        probabilities = []
        for vector in states.values():
            tensor = vector.reshape(4, -1)
            rho = tensor @ tensor.conj().T
            probabilities.extend(float(np.trace(effect @ rho).real) for effect in effects)
        return np.array(probabilities)
    return likelihood


def early_readout_likelihood(g, interval, horizon_cells, echoes):
    """Read after echoes+1 cells; retain all outcomes through later noise."""
    pulse = np.kron(np.kron(Z, I), I)
    frame = np.kron(np.linalg.matrix_power(Z, echoes), I)
    readout = ((EVEN + YL) / 2, (EVEN - YL) / 2, ODD)
    def likelihood(point):
        epsilon, phi = point
        half = joint_unitary(g, interval / 2, epsilon, phi)
        full = joint_unitary(g, interval, epsilon, phi)
        state = INITIAL.copy()
        for _ in range(echoes):
            state = reduced_cell(half @ pulse @ half, state)
        state = conjugate(frame, reduced_cell(full, state))
        branches = [conjugate(projector, state) for projector in readout]
        # This is an actual early measurement, not a free early endpoint.
        # Its classical label is stored; no further system contact is made.
        for _ in range(horizon_cells - echoes - 1):
            branches = [reduced_cell(full, rho) for rho in branches]
        return np.array([float(np.trace(rho).real) for rho in branches])
    return likelihood


def bounds(g, interval, cells, cap):
    chi = g * interval
    p, q = np.sin(chi) ** 2, np.cos(chi) ** 2
    baseline = cells * cells * p / (g * g * (cells * p + q))
    echo = p / (g * g) * (1 + cap * np.cos(chi)) ** 2
    upper = min((cells * interval) ** 2,
                (np.sqrt(cells) / g + cap * interval / np.sin(chi)) ** 2)
    return max(baseline, echo), upper, baseline, echo


class AdaptiveActivityLemmaTests(unittest.TestCase):
    def test_relaxed_controller_retains_rare_parameter_dependent_flags(self):
        g, interval, cells, cap = .9, .4, 4, 2
        center = adaptive_purification(g, interval, cells, cap)
        self.assertAlmostEqual(norm_squared(center), 1., places=13)
        self.assertEqual(len(center), 11)
        self.assertTrue(all(sum(history) <= cap for history in center))
        probabilities = [float(np.vdot(v, v).real) for v in center.values()]
        self.assertGreater(min(probabilities), 0.)
        self.assertLess(min(probabilities), .001)
        step = 1e-6
        plus = adaptive_purification(g, interval, cells, cap, epsilon=step)
        minus = adaptive_purification(g, interval, cells, cap, epsilon=-step)
        derivatives = [(np.vdot(plus[k], plus[k]).real - np.vdot(minus[k], minus[k]).real) / (2 * step)
                       for k in center]
        self.assertGreater(max(abs(value) for value in derivatives), 1e-5)

    def test_inactive_derivative_sources_are_pairwise_orthogonal(self):
        g, interval, cells, cap = .9, .4, 4, 2
        inactive, active = source_data(g, interval, cells, cap)
        for i in range(cells):
            for j in range(i):
                self.assertLess(abs(inner(inactive[i], inactive[j])), 2e-10)
        summed = add_sources(inactive)
        self.assertAlmostEqual(norm_squared(summed), sum(norm_squared(x) for x in inactive), places=9)
        self.assertLessEqual(norm_squared(summed), cells / (4 * g * g) + 1e-10)
        slope, step = 1 / (2 * g * np.tan(g * interval)), 1e-6
        plus = adaptive_purification(g, interval, cells, cap, epsilon=step, phi=.37 + slope * step)
        minus = adaptive_purification(g, interval, cells, cap, epsilon=-step, phi=.37 - slope * step)
        full_tangent = {key: (plus[key] - minus[key]) / (2 * step) for key in plus}
        reconstructed = add_sources(inactive + active)
        for key in full_tangent:
            assert_allclose(full_tangent[key], reconstructed[key], atol=5e-10)

    def test_active_source_support_and_hard_branch_budget(self):
        for cells, cap in ((1, 0), (3, 1), (4, 2)):
            g, interval = .9, .4
            center = adaptive_purification(g, interval, cells, cap)
            inactive, active = source_data(g, interval, cells, cap)
            lipschitz = interval / (2 * np.sin(g * interval))
            activity_sum = 0.
            for index, source in enumerate(active):
                for history, vector in source.items():
                    if not history[index]:
                        self.assertLess(np.linalg.norm(vector), 1e-14)
                probability = sum(np.vdot(v, v).real for history, v in center.items() if history[index])
                activity_sum += probability
                self.assertLessEqual(norm_squared(source), lipschitz * lipschitz * probability + 1e-10)
            self.assertLessEqual(activity_sum, cap + 1e-12)
            total_active = norm_squared(add_sources(active))
            self.assertLessEqual(total_active, cap * sum(norm_squared(x) for x in active) + 1e-10)
            self.assertLessEqual(total_active, cap * cap * lipschitz * lipschitz + 1e-10)
            total = norm_squared(add_sources(inactive + active))
            self.assertLessEqual(total, (np.sqrt(cells) / (2 * g) + cap * lipschitz) ** 2 + 1e-9)

    def test_accessible_full_record_information_obeys_relaxed_upper(self):
        g, interval = .9, .4
        for cells, cap in ((1, 0), (3, 1), (4, 2)):
            likelihood = accessible_likelihood(g, interval, cells, cap)
            self.assertAlmostEqual(likelihood([0., .37]).sum(), 1., places=13)
            fisher = numerical_fisher(likelihood, [0., .37])
            self.assertGreater(fisher[1, 1], 0.)
            efficient = fisher[0, 0] - fisher[0, 1] ** 2 / fisher[1, 1]
            upper = bounds(g, interval, cells, cap)[1]
            self.assertGreaterEqual(efficient, -1e-10)
            self.assertLessEqual(efficient, upper + 1e-7)


class FiniteContactPrecisionTests(unittest.TestCase):
    def test_early_readout_records_survive_remaining_sensor_noise(self):
        g, interval = .9, .4
        for cells, cap in ((1, 0), (2, 0), (6, 0), (6, 2), (6, 5)):
            actual = early_readout_likelihood(g, interval, cells, cap)
            immediate = echo_likelihood(g, interval, cap + 1)
            for epsilon, phi in ((0., .37), (.23, -.61)):
                assert_allclose(actual([epsilon, phi]), immediate([epsilon, phi]), atol=3e-14)
            times = [(index + .5) * interval for index in range(cap)]
            if cap < cells - 1:
                times.append((cap + 1) * interval)
            self.assertEqual(len(times), cap + int(cap < cells - 1))
            self.assertLessEqual(len(times), cells - 1)
            self.assertTrue(all(0 < time < cells * interval for time in times))

    def test_early_readout_information_charges_success_and_contact(self):
        g, interval = .9, .4
        p, q = np.sin(g * interval) ** 2, np.cos(g * interval) ** 2
        for cells, cap in ((1, 0), (5, 0), (5, 1), (7, 3), (7, 6)):
            likelihood = early_readout_likelihood(g, interval, cells, cap)
            assert_allclose(likelihood([0., .37]), [q / 2, q / 2, p], atol=3e-14)
            fisher = numerical_fisher(likelihood, [0., .37])
            expected = p / (g * g) * (1 + cap * np.cos(g * interval)) ** 2
            self.assertAlmostEqual(fisher[0, 0] / expected, 1., places=7)
            self.assertLess(fisher[1, 1], 1e-16)

    def test_independent_lower_protocols_fit_finite_upper_grid(self):
        for gamma, interval in ((.4, .2), (1.3, .3)):
            _, _, g = calibration(gamma, interval)
            for cells in (1, 2, 5, 9):
                baseline_fisher = numerical_fisher(recovery_likelihood(g, interval, cells), [0., .263])
                baseline = baseline_fisher[0, 0] - baseline_fisher[0, 1] ** 2 / baseline_fisher[1, 1]
                for cap in sorted({0, min(1, cells - 1), cells - 1}):
                    echo = numerical_fisher(early_readout_likelihood(g, interval, cells, cap), [0., .263])[0, 0]
                    lower, upper, exact_baseline, exact_echo = bounds(g, interval, cells, cap)
                    assert_allclose([baseline, echo], [exact_baseline, exact_echo], rtol=8e-7, atol=2e-8)
                    self.assertLessEqual(max(baseline, echo), upper + 2e-7)
                    self.assertLessEqual(lower, upper + 1e-12)

    def test_sampled_order_envelopes_include_crossover_and_endpoints(self):
        # A finite algebraic consistency check; not a proof by sampling.
        g, interval = .9, .4
        chi = g * interval
        p, q = np.sin(chi) ** 2, np.cos(chi) ** 2
        lower_constant = p * q / (chi * chi * (1 + q))
        upper_constant = 2 / p
        for cells in (1, 2, 10, 100, 10000, 1000000):
            caps = {0, min(1, cells - 1), int(cells ** .25), int(cells ** .5), int(cells ** .75), cells - 1}
            for cap in caps:
                if cap > cells - 1:
                    continue
                lower, upper, _, _ = bounds(g, interval, cells, cap)
                scale = interval * interval * (cells + cap * cap)
                self.assertGreaterEqual(lower / scale, lower_constant - 1e-12)
                self.assertLessEqual(upper / scale, upper_constant + 1e-12)
                self.assertLessEqual(lower, upper + 1e-5)


if __name__ == '__main__':
    unittest.main()
