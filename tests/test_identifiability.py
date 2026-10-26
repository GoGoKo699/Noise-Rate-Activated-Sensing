"""Finite checks of collision-clock identifiability and paid calibration.

Likelihoods and retained records come from the sensor--ancilla--bath unitary.
Risk and tail checks sum the exact finite outcome distribution; they are not
Monte Carlo evidence for the uniform theorem or the all-controller alias bound.
"""
import unittest

import numpy as np
from numpy.testing import assert_allclose
from scipy.linalg import expm
from scipy.optimize import brentq

from test_microscopic import (
    I, X, Y, Z, EVEN, ODD, YL, INITIAL,
    joint_unitary, reduced_cell, conjugate,
)


SCORES = np.array([-1., 0., 1.])
EFFECTS = ((EVEN - YL) / 2, ODD, (EVEN + YL) / 2)


def signal(g, interval, epsilon):
    radius = np.sqrt(g * g + epsilon * epsilon / 4)
    return epsilon * np.sin(2 * radius * interval) / (2 * radius)


def band(g, interval, outer_radius):
    chi = g * interval
    return (2 * np.sqrt(outer_radius ** 2 - chi ** 2) / interval,
            interval * np.cos(2 * outer_radius))


def physical_probabilities(g, interval, epsilon, phi):
    evolved = reduced_cell(joint_unitary(g, interval, epsilon, phi), INITIAL)
    return np.array([np.trace(effect @ evolved).real for effect in EFFECTS])


def repeated_instruments(g, interval, trials, total_cells, epsilon, phi):
    """Read, retain, and reprepare at each used boundary; charge early readout.

    Tracing spent baths is exact here because they are never accessed again.
    The remaining cells still act on the sensor after an early calibration.
    """
    unitary = joint_unitary(g, interval, epsilon, phi)
    states = {(): INITIAL.copy()}
    contacts = []
    for cell in range(1, total_cells + 1):
        states = {history: reduced_cell(unitary, rho)
                  for history, rho in states.items()}
        if cell > trials:
            continue
        following = {}
        for history, rho in states.items():
            for score, effect in zip(SCORES, EFFECTS):
                measured = conjugate(effect, rho)
                following[history + (int(score),)] = (
                    np.trace(measured).real * INITIAL if cell < total_cells
                    else measured)
        states = following
        if cell < total_cells:
            contacts.append(cell * interval)
    return states, contacts


def inverse_estimates(g, interval, half_width, trials):
    cap = signal(g, interval, half_width)
    estimates = []
    for total in range(-trials, trials + 1):
        target = np.clip(total / trials, -cap, cap)
        estimates.append(brentq(lambda epsilon: signal(g, interval, epsilon) - target,
                                -half_width, half_width, xtol=5e-14))
    return np.array(estimates)


def adaptive_boundary_record(g, interval, epsilon, phi, identity=False):
    """Four cells, outcome-dependent instruments, protected memory, final readout."""
    states = {(): INITIAL.copy()}
    unitary = joint_unitary(g, interval, epsilon, phi)
    for cell in range(4):
        following = {}
        for history, rho in states.items():
            evolved = rho if identity else reduced_cell(unitary, rho)
            if cell == 3:
                following[history] = evolved
                continue
            rotation = expm(-.5j * (.23 + .17 * cell + .11 * sum(history)) * Y)
            weights = np.array([.19 + .03 * cell, .79 - .04 * cell])
            feedback = expm(-.5j * (.31 + .23 * sum(history))
                            * (np.kron(X, X) + .4 * np.kron(Z, Y)))
            for outcome, rates in enumerate((weights, 1 - weights)):
                measurement = np.kron(rotation @ np.diag(np.sqrt(rates))
                                      @ rotation.conj().T, I)
                following[history + (outcome,)] = conjugate(
                    feedback, conjugate(measurement, evolved))
        states = following
    return np.concatenate([np.diag(states[history]).real for history in sorted(states)])


class CollisionIdentifiabilityTests(unittest.TestCase):
    def test_complete_likelihood_from_joint_unitary_is_nuisance_independent(self):
        for chi, interval in ((.12, .2), (.43, .9), (.72, 1.7)):
            g = chi / interval
            radius_cap = (chi + np.pi / 4) / 2
            half_width, _ = band(g, interval, radius_cap)
            for epsilon in np.linspace(-half_width, half_width, 9):
                radius = np.sqrt(g * g + epsilon * epsilon / 4)
                failure = (g * np.sin(radius * interval) / radius) ** 2
                mean = signal(g, interval, epsilon)
                expected = np.array([(1 - failure - mean) / 2,
                                     failure, (1 - failure + mean) / 2])
                for phi in (-1.13, .0, .43, 2.17):
                    actual = physical_probabilities(g, interval, epsilon, phi)
                    assert_allclose(actual, expected, atol=3e-15)
                    self.assertGreater(actual.min(), 0.)
                    self.assertAlmostEqual(actual.sum(), 1., places=14)

    def test_physical_mean_derivative_and_band_conditioning(self):
        for chi, interval, radius_cap in ((.07, .13, .4), (.41, .8, .6),
                                          (.75, 1.9, .77)):
            g = chi / interval
            half_width, conditioning = band(g, interval, radius_cap)
            step = 2e-5 / interval
            means = []
            for epsilon in np.linspace(-half_width, half_width, 31):
                values = [SCORES @ physical_probabilities(
                    g, interval, epsilon + offset * step, .71)
                    for offset in (-2, -1, 1, 2)]
                derivative = (values[0] - 8 * values[1] + 8 * values[2]
                              - values[3]) / (12 * step)
                x = epsilon * interval / 2
                radius = np.sqrt(chi * chi + x * x)
                exact = interval * (chi * chi / radius ** 2
                                    * np.sinc(2 * radius / np.pi)
                                    + x * x / radius ** 2 * np.cos(2 * radius))
                self.assertAlmostEqual(derivative, exact, delta=2e-10 * interval)
                self.assertGreaterEqual(derivative, conditioning - 2e-10 * interval)
                self.assertLessEqual(derivative, interval + 2e-10 * interval)
                means.append(SCORES @ physical_probabilities(g, interval, epsilon, .71))
            self.assertTrue(np.all(np.diff(means) > 0))

    def test_full_repeated_instrument_tree_retains_every_failure(self):
        g, interval, trials, epsilon, phi = .6, .7, 4, -.53, 1.31
        probabilities = physical_probabilities(g, interval, epsilon, phi)
        states, contacts = repeated_instruments(g, interval, trials, trials, epsilon, phi)
        self.assertEqual(len(states), 3 ** trials)
        self.assertEqual(len(contacts), trials - 1)
        total = 0.
        for history, state in states.items():
            weight = np.trace(state).real
            expected = np.prod([probabilities[score + 1] for score in history])
            self.assertAlmostEqual(weight, expected, places=14)
            self.assertGreater(weight, 0.)
            total += weight
        self.assertAlmostEqual(total, 1., places=13)
        self.assertAlmostEqual(np.trace(states[(0,) * trials]).real,
                               probabilities[1] ** trials, places=14)

    def test_exact_finite_sample_risk_and_concentration(self):
        informative_tail_checks = 0
        for chi, interval, radius_cap, trials in ((.18, .7, .4, 128),
                                                  (.18, .7, .4, 256),
                                                  (.62, 1.3, .69, 96)):
            g = chi / interval
            half_width, conditioning = band(g, interval, radius_cap)
            estimates = inverse_estimates(g, interval, half_width, trials)
            for epsilon in half_width * np.array([-1., -.37, 0., .43, 1.]):
                single = physical_probabilities(g, interval, epsilon, .57)
                distribution = np.array([1.])
                for _ in range(trials):
                    distribution = np.convolve(distribution, single)
                self.assertAlmostEqual(distribution.sum(), 1., places=11)
                error = estimates - epsilon
                risk = distribution @ (error * error)
                self.assertLessEqual(risk, 1 / (trials * conditioning ** 2) + 1e-12)
                for delta in (.35 * half_width, .7 * half_width):
                    tail = distribution[np.abs(error) >= delta].sum()
                    bound_value = 2 * np.exp(-trials * conditioning ** 2 * delta ** 2 / 2)
                    self.assertLessEqual(tail, bound_value + 1e-12)
                    informative_tail_checks += bound_value < .2
        self.assertGreaterEqual(informative_tail_checks, 10)

    def test_early_readout_is_charged_and_its_record_survives_remaining_cells(self):
        g, interval, epsilon, phi = .7, .6, .47, -.83
        for trials, total_cells in ((1, 1), (1, 4), (3, 3), (3, 6)):
            direct, direct_contacts = repeated_instruments(
                g, interval, trials, trials, epsilon, phi)
            retained, contacts = repeated_instruments(
                g, interval, trials, total_cells, epsilon, phi)
            assert_allclose([np.trace(retained[key]).real for key in direct],
                            [np.trace(direct[key]).real for key in direct], atol=3e-15)
            self.assertEqual(len(direct_contacts), trials - 1)
            self.assertEqual(len(contacts), trials - int(trials == total_cells))
            self.assertLessEqual(len(contacts), total_cells - 1)
            if trials < total_cells:
                self.assertEqual(contacts[-1], trials * interval)
                self.assertLess(contacts[-1], total_cells * interval)

    def test_resonant_joint_unitaries_preserve_entangled_inputs(self):
        rng = np.random.default_rng(7301)
        matrix = rng.normal(size=(4, 4)) + 1j * rng.normal(size=(4, 4))
        mixed = matrix @ matrix.conj().T
        mixed /= np.trace(mixed)
        for chi, interval in ((.19, .4), (.7, 1.1)):
            g = chi / interval
            for winding in (1, 2, 3):
                for sign in (-1, 1):
                    epsilon = sign * 2 / interval * np.sqrt((winding * np.pi) ** 2 - chi ** 2)
                    for phi in (-.73, 1.29):
                        unitary = joint_unitary(g, interval, epsilon, phi)
                        assert_allclose(unitary, (-1) ** winding * np.eye(8), atol=8e-15)
                        for state in (INITIAL, mixed):
                            assert_allclose(reduced_cell(unitary, state), state, atol=4e-15)

    def test_aliases_have_identical_complete_adaptive_boundary_records(self):
        g, interval, phi = .8, .6, .43
        chi = g * interval
        aliases = [2 / interval * np.sqrt(np.pi ** 2 - chi ** 2),
                   -2 / interval * np.sqrt(4 * np.pi ** 2 - chi ** 2)]
        reference = adaptive_boundary_record(g, interval, 0., phi, identity=True)
        self.assertEqual(len(reference), 32)
        self.assertAlmostEqual(reference.sum(), 1., places=13)
        self.assertGreater(reference.min(), 0.)
        for epsilon in aliases:
            actual = adaptive_boundary_record(g, interval, epsilon, phi)
            assert_allclose(actual, reference, atol=3e-15)
        off_resonance = adaptive_boundary_record(g, interval, .17, phi)
        self.assertGreater(np.linalg.norm(off_resonance - reference, ord=1), .01)


if __name__ == '__main__':
    unittest.main()
