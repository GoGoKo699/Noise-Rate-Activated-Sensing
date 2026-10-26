"""Finite checks for boundary controls and true microscopic midpoint echoes.

Interior-pulse checks propagate the joint sensor--bath unitary. Subdividing
a calibrated endpoint channel would test a different physical experiment.
"""
import unittest
import numpy as np
from numpy.testing import assert_allclose
from scipy.linalg import expm
from scipy.stats import binom

I = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.diag([1, -1]).astype(complex)
E0 = np.diag([1, 0]).astype(complex)
EVEN = (np.eye(4) + np.kron(Z, Z)) / 2
ODD = np.eye(4) - EVEN
XL, YL = np.zeros((4, 4), dtype=complex), np.zeros((4, 4), dtype=complex)
XL[0, 3] = XL[3, 0] = 1
YL[0, 3], YL[3, 0] = -1j, 1j
bell = np.array([1, 0, 0, 1], dtype=complex) / np.sqrt(2)
INITIAL = np.outer(bell, bell.conj())
ANGLES = (.173, 1.317, 2.531, 4.073)

def axis(phi):
    return np.cos(phi) * X + np.sin(phi) * Y

def calibration(gamma, interval):
    p = -np.expm1(-2 * gamma * interval) / 2
    chi = np.arcsin(np.sqrt(p))
    return float(p), float(chi), float(chi / interval)

def cell_kraus(g, interval, epsilon, phi):
    radius = np.sqrt(g * g + epsilon * epsilon / 4)
    sinc = np.sin(radius * interval) / radius
    return (np.cos(radius * interval) * I - .5j * epsilon * sinc * Z,
            -1j * g * sinc * axis(phi))

def joint_unitary(g, duration, epsilon, phi):
    # Subsystem order: sensor, protected ancilla, cell bath.
    hamiltonian = (.5 * epsilon * np.kron(np.kron(Z, I), I)
                   + g * np.kron(np.kron(axis(phi), I), X))
    return expm(-1j * duration * hamiltonian)

def conjugate(u, rho):
    return u @ rho @ u.conj().T

def reduced_cell(unitary, rho):
    joint = conjugate(unitary, np.kron(rho, E0))
    return np.trace(joint.reshape(4, 2, 4, 2), axis1=1, axis2=3)

def numerical_fisher(likelihood, point, step=1e-6):
    point = np.asarray(point, dtype=float)
    probabilities = likelihood(point)
    derivatives = []
    for index in range(len(point)):
        offset = np.zeros_like(point)
        offset[index] = step
        derivatives.append((likelihood(point + offset) - likelihood(point - offset)) / (2 * step))
    gradient = np.array(derivatives)
    keep = probabilities > 1e-24
    return (gradient[:, keep] / probabilities[keep]) @ gradient[:, keep].T

def recovery_likelihood(g, interval, cells):
    counts = np.arange(cells + 1)
    def likelihood(point):
        epsilon, phi = point
        radius = np.sqrt(g * g + epsilon * epsilon / 4)
        p = (g / radius * np.sin(radius * interval)) ** 2
        theta = 2 * np.arctan2(epsilon * np.sin(radius * interval) / (2 * radius),
                               np.cos(radius * interval))
        phase = (cells - counts) * theta - 2 * counts * phi
        weights = binom.pmf(counts, cells, p)
        return np.array([weights * (1 + sign * np.cos(phase - angle)) / (2 * len(ANGLES))
                         for angle in ANGLES for sign in (-1, 1)]).T.ravel()
    return likelihood

def physical_recovery_likelihood(g, interval, cells, epsilon, phi):
    """Full joint dynamics, boundary parity, fixed X recovery, then readout."""
    unitary, recovery = joint_unitary(g, interval, epsilon, phi), np.kron(X, I)
    states = {0: INITIAL.copy()}
    for _ in range(cells):
        following = {count: np.zeros((4, 4), dtype=complex) for count in range(max(states) + 2)}
        for count, rho in states.items():
            evolved = reduced_cell(unitary, rho)
            following[count] += conjugate(EVEN, evolved)
            following[count + 1] += conjugate(recovery, conjugate(ODD, evolved))
        states = following
    output = []
    for rho in states.values():
        for angle in ANGLES:
            observable = np.cos(angle) * XL + np.sin(angle) * YL
            for sign in (-1, 1):
                output.append(float(np.trace((EVEN + sign * observable) @ rho).real
                                    / (2 * len(ANGLES))))
    return np.array(output)

def tangent_alpha_beta(g, interval, phi, nuisance_slope, step=1e-6):
    center = cell_kraus(g, interval, 0., phi)
    positive = cell_kraus(g, interval, step, phi + nuisance_slope * step)
    negative = cell_kraus(g, interval, -step, phi - nuisance_slope * step)
    tangent = [(plus - minus) / (2 * step) for plus, minus in zip(positive, negative)]
    return (sum(dot.conj().T @ dot for dot in tangent),
            1j * sum(k.conj().T @ dot for dot, k in zip(tangent, center)))

def echo_likelihood(g, interval, cells):
    """Only cells−1 midpoint pulses; terminal parity/readout is retained."""
    pulse = np.kron(np.kron(Z, I), I)
    frame = np.kron(np.linalg.matrix_power(Z, cells - 1), I)
    def likelihood(point):
        epsilon, phi = point
        half = joint_unitary(g, interval / 2, epsilon, phi)
        echo, full = half @ pulse @ half, joint_unitary(g, interval, epsilon, phi)
        state = INITIAL.copy()
        for _ in range(cells - 1):
            state = reduced_cell(echo, state)
        state = conjugate(frame, reduced_cell(full, state))
        return np.array([np.trace((EVEN + YL) @ state).real / 2,
                         np.trace((EVEN - YL) @ state).real / 2,
                         np.trace(ODD @ state).real])
    return likelihood

class MicroscopicBoundaryTests(unittest.TestCase):
    def test_exact_kraus_channel_against_joint_unitary(self):
        for gamma, interval, epsilon, phi in ((.4, .03, -.7, .13), (1.3, .2, 1.1, 1.27),
                                              (2., .7, 0., 2.3)):
            _, _, g = calibration(gamma, interval)
            unitary = joint_unitary(g, interval, epsilon, phi)
            kraus = [np.kron(k, I) for k in cell_kraus(g, interval, epsilon, phi)]
            for i in range(4):
                for j in range(4):
                    matrix_unit = np.zeros((4, 4), dtype=complex)
                    matrix_unit[i, j] = 1
                    assert_allclose(reduced_cell(unitary, matrix_unit),
                                    sum(conjugate(k, matrix_unit) for k in kraus), atol=2e-14)

    def test_fixed_recovery_complete_likelihood_from_physical_instruments(self):
        for gamma, interval, cells in ((.4, .2, 3), (1.3, .3, 6)):
            _, _, g = calibration(gamma, interval)
            for epsilon, phi in ((0., .263), (.17, -.31)):
                actual = physical_recovery_likelihood(g, interval, cells, epsilon, phi)
                expected = recovery_likelihood(g, interval, cells)([epsilon, phi])
                self.assertAlmostEqual(actual.sum(), 1., places=13)
                assert_allclose(actual, expected, atol=3e-14)

    def test_fixed_recovery_full_fisher_and_nuisance_elimination(self):
        for gamma, interval, cells in ((.4, .2, 1), (.4, .2, 7), (1.3, .3, 20)):
            p, chi, g = calibration(gamma, interval)
            q, d = 1 - p, np.tan(chi) / g
            actual = numerical_fisher(recovery_likelihood(g, interval, cells), [0., .263])
            expected = np.array([[d * d * (cells * cells * q * q + cells * p * q),
                                  -2 * d * cells * (cells - 1) * p * q],
                                 [-2 * d * cells * (cells - 1) * p * q,
                                  4 * (cells * cells * p * p + cells * p * q)]])
            assert_allclose(actual, expected, rtol=5e-7, atol=3e-8)
            efficient = actual[0, 0] - actual[0, 1] ** 2 / actual[1, 1]
            formula = cells * cells * p / (g * g * (cells * p + q))
            self.assertAlmostEqual(efficient / formula, 1., places=6)
            self.assertLessEqual(formula, cells / (g * g))

    def test_fixed_recovery_approaches_linear_channel_bound(self):
        for gamma, interval in ((.2, .03), (.8, .4), (2.1, .9)):
            p, _, g = calibration(gamma, interval)
            q, cells = 1 - p, 10**9
            efficient = cells * cells * p / (g * g * (cells * p + q))
            self.assertAlmostEqual(efficient / (cells / (g * g)), 1., places=6)

    def test_fixed_rate_nuisance_tangent_cancels_beta(self):
        for gamma, interval, phi in ((.4, .15, .23), (1.7, .6, -.71), (.7, .04, 1.2)):
            _, chi, g = calibration(gamma, interval)
            slope = 1 / (2 * g * np.tan(chi))
            alpha, beta = tangent_alpha_beta(g, interval, phi, slope)
            assert_allclose(beta, np.zeros((2, 2)), atol=3e-10)
            assert_allclose(alpha, I / (4 * g * g), rtol=2e-9, atol=3e-10)

    def test_two_rates_have_opposite_beta_with_one_nuisance_path(self):
        for a, b, interval in ((.4, 1.3, .03), (.4, 1.3, .7), (1., 1.001, .2)):
            pa, ca, ga = calibration(a, interval)
            pb, cb, gb = calibration(b, interval)
            fa, fb = (1 - pa) * np.tan(ca) / ga, (1 - pb) * np.tan(cb) / gb
            slope, mu = (fa + fb) / (2 * (pa + pb)), (pb * fa - pa * fb) / (pa + pb)
            self.assertGreater(mu, 0.)
            for p, g, sign in ((pa, ga, 1), (pb, gb, -1)):
                alpha, beta = tangent_alpha_beta(g, interval, .39, slope)
                assert_allclose(beta, sign * mu * Z / 2, atol=4e-10)
                assert_allclose(alpha, (p / (4 * g * g) + p * slope * slope) * I,
                                rtol=3e-9, atol=4e-10)

class MicroscopicInteriorEchoTests(unittest.TestCase):
    def test_joint_midpoint_echo_cancels_noise_at_compensation(self):
        pulse = np.kron(np.kron(Z, I), I)
        for g, interval, phi in ((.7, .3, .2), (1.2, .6, -.9), (4., .05, 1.4)):
            half = joint_unitary(g, interval / 2, 0., phi)
            assert_allclose(half @ pulse @ half, pulse, atol=3e-14)

    def test_joint_echo_derivative_contains_unobserved_bath_term(self):
        pulse, step = np.kron(np.kron(Z, I), I), 1e-6
        for g, interval, phi in ((.7, .3, .2), (1.2, .6, -.9)):
            def framed(epsilon):
                half = joint_unitary(g, interval / 2, epsilon, phi)
                return pulse @ half @ pulse @ half
            tangent = (framed(step) - framed(-step)) / (2 * step)
            chi = g * interval
            a, b = np.sin(chi) / g, (1 - np.cos(chi)) / g
            derivative = -np.sin(phi) * X + np.cos(phi) * Y
            expected = -.5j * (a * np.kron(np.kron(Z, I), I)
                               + b * np.kron(np.kron(derivative, I), X))
            assert_allclose(tangent, expected, atol=8e-11)

    def test_same_contact_budget_echo_likelihood_and_information(self):
        for gamma, interval, cells in ((.4, .2, 1), (.4, .2, 2), (1.3, .3, 7), (.7, .5, 13)):
            p, chi, g = calibration(gamma, interval)
            q, d = 1 - p, np.tan(chi) / g
            likelihood = echo_likelihood(g, interval, cells)
            assert_allclose(likelihood([0., .263]), [q / 2, q / 2, p], atol=3e-14)
            actual = numerical_fisher(likelihood, [0., .263])
            target = q * ((cells - 1) * np.sin(chi) / g + d) ** 2
            stable = p / (g * g) * (1 + (cells - 1) * np.cos(chi)) ** 2
            self.assertAlmostEqual(target / stable, 1., places=13)
            self.assertLessEqual(target, (cells * interval) ** 2)
            self.assertAlmostEqual(actual[0, 0] / target, 1., places=7)
            self.assertLess(abs(actual[0, 1]), 3e-8)
            self.assertLess(actual[1, 1], 1e-16)

    def test_midpoint_pulse_cannot_use_markov_endpoint_surrogate(self):
        gamma, interval, phi = .8, .4, .61
        p, _, g = calibration(gamma, interval)
        pulse = np.kron(np.kron(Z, I), I)
        half = joint_unitary(g, interval / 2, 0., phi)
        physical = reduced_cell(half @ pulse @ half, INITIAL)
        self.assertAlmostEqual(np.trace(EVEN @ physical).real, 1., places=13)
        n, sensor_pulse = np.kron(axis(phi), I), np.kron(Z, I)
        p_half = -np.expm1(-gamma * interval) / 2
        def markov_half(rho):
            return (1 - p_half) * rho + p_half * conjugate(n, rho)
        surrogate = markov_half(conjugate(sensor_pulse, markov_half(INITIAL)))
        self.assertAlmostEqual(np.trace(EVEN @ surrogate).real, 1 - p, places=13)
        self.assertGreater(p, .1)

    def test_interior_echo_exceeds_boundary_only_information_bound(self):
        # Both controls use twelve interior contacts and thirteen cells.
        # The boundary theorem cannot be extended merely by counting contacts.
        cells, interval = 13, .5
        _, _, g = calibration(.7, interval)
        actual = numerical_fisher(echo_likelihood(g, interval, cells), [0., .263])
        boundary_upper = cells / (g * g)
        self.assertGreater(actual[0, 0], 2 * boundary_upper)
        self.assertLess(actual[1, 1], 1e-16)

if __name__ == '__main__':
    unittest.main()
