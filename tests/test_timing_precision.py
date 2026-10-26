"""Physical finite checks for systematic pulse offsets and hidden timing jitter.

The pulse is propagated inside the actual joint unitary. The leading frame Z
is part of the counted boundary instrument, not an additional interior pulse.
Finite examples support the written proofs; they do not optimize controllers.
"""
import unittest

import numpy as np
from numpy.testing import assert_allclose

from test_microscopic import (
    I, X, Y, Z, EVEN, ODD, XL, YL, INITIAL, ANGLES,
    axis, cell_kraus, joint_unitary, reduced_cell, conjugate, numerical_fisher,
)


PULSE = np.kron(np.kron(Z, I), I)


def axis_derivative(phi):
    return -np.sin(phi) * X + np.cos(phi) * Y


def coefficients(g, h, epsilon, offset):
    radius = np.sqrt(g * g + epsilon * epsilon / 4)
    difference = np.cos(2 * radius * offset) - np.cos(radius * h)
    return np.array([
        np.cos(radius * h) + g * g * difference / radius ** 2,
        epsilon * np.sin(radius * h) / (2 * radius),
        g * np.sin(2 * radius * offset) / radius,
        epsilon * g * difference / (2 * radius ** 2),
    ])


def coefficient_derivative(g, h, epsilon, offset):
    return coefficients(g, h, epsilon + 1e-20j, offset).imag / 1e-20


def framed_unitary(g, h, epsilon, phi, offset):
    return (PULSE @ joint_unitary(g, h / 2 - offset, epsilon, phi)
            @ PULSE @ joint_unitary(g, h / 2 + offset, epsilon, phi))


def physical_kraus(unitary):
    blocks = unitary.reshape(4, 2, 4, 2)
    return [blocks[:, outcome, :, 0] for outcome in (0, 1)]


def jitter_kraus(g, h, epsilon, phi, offset):
    u, v, w, x = coefficients(g, h, epsilon, offset)
    return [u * I - 1j * v * Z,
            -1j * w * axis(phi), -1j * x * axis_derivative(phi)]


def hidden_channel(unitaries, state):
    return sum(reduced_cell(unitary, state) for unitary in unitaries) / 2


def plain_curve_slope(g, h, epsilon):
    def scalar_pair(value):
        radius = np.sqrt(g * g + value * value / 4)
        return np.array([np.cos(radius * h),
                         value * np.sin(radius * h) / (2 * radius)])
    u, v = scalar_pair(epsilon)
    du, dv = scalar_pair(epsilon + 1e-20j).imag / 1e-20
    radius = np.sqrt(g * g + epsilon * epsilon / 4)
    probability = (g * np.sin(radius * h) / radius) ** 2
    return (u * dv - v * du) / probability


def gauge_data(g, h, epsilon, offset):
    u, v, w, x = coefficients(g, h, epsilon, offset)
    du, dv, dw, dx = coefficient_derivative(g, h, epsilon, offset)
    slope = plain_curve_slope(g, h, epsilon)
    gauge = (u * dv - v * du - (w * w + x * x) * slope) / (2 * w * x)
    alpha = (du * du + dv * dv + dw * dw + dx * dx
             + (w * slope + gauge * x) ** 2
             + (x * slope + gauge * w) ** 2)
    return slope, gauge, alpha


def physical_recovery(g, h, offset, cells, epsilon, phi):
    unitaries = [framed_unitary(g, h, epsilon, phi, sign * offset)
                 for sign in (-1, 1)]
    recovery = np.kron(X, I)
    states = {0: INITIAL.copy()}
    for _ in range(cells):
        following = {count: np.zeros((4, 4), dtype=complex)
                     for count in range(max(states) + 2)}
        for count, state in states.items():
            evolved = hidden_channel(unitaries, state)
            following[count] += conjugate(EVEN, evolved)
            following[count + 1] += conjugate(recovery, conjugate(ODD, evolved))
        states = following
    result = []
    for state in states.values():
        for angle in ANGLES:
            observable = np.cos(angle) * XL + np.sin(angle) * YL
            for sign in (-1, 1):
                result.append(np.trace((EVEN + sign * observable) @ state).real
                              / (2 * len(ANGLES)))
    return np.array(result)


def physical_menu_records(g, h, offset, cells, epsilon, phi):
    echoed = [framed_unitary(g, h, epsilon, phi, sign * offset)
              for sign in (-1, 1)]
    plain = joint_unitary(g, h, epsilon, phi)
    states = {(): INITIAL.copy()}
    for _ in range(cells):
        following = {}
        for history, state in states.items():
            previous = history[-1] if history else 1
            evolved = (hidden_channel(echoed, state) if previous == 1
                       else reduced_cell(plain, state))
            for sector, projector in ((1, EVEN), (-1, ODD)):
                following[history + (sector,)] = conjugate(projector, evolved)
        states = following
    result = []
    for history in sorted(states):
        state = states[history]
        if history[-1] == 1:
            result.extend([np.trace((EVEN + sign * YL) @ state).real / 2
                           for sign in (-1, 1)])
        else:
            result.append(np.trace(state).real)
    return np.array(result)


def systematic_menu_states(g, h, offset, cells, epsilon, phi):
    echoed = framed_unitary(g, h, epsilon, phi, offset)
    plain = joint_unitary(g, h, epsilon, phi)
    states = {(): INITIAL.copy()}
    for _ in range(cells):
        following = {}
        for history, state in states.items():
            previous = history[-1] if history else 1
            evolved = reduced_cell(echoed if previous == 1 else plain, state)
            for sector, projector in ((1, EVEN), (-1, ODD)):
                following[history + (sector,)] = conjugate(projector, evolved)
        states = following
    return states


def frozen_menu_records(g, h, offset, cells):
    pa, pb = np.sin(2 * g * offset) ** 2, np.sin(g * h) ** 2
    da = np.sin(g * h) / (g * np.cos(2 * g * offset))
    db = np.tan(g * h) / g
    records = {(): (1., 0.)}
    for _ in range(cells):
        following = {}
        for history, (weight, reward) in records.items():
            previous = history[-1] if history else 1
            p, d = (pa, da) if previous == 1 else (pb, db)
            following[history + (previous,)] = (weight * (1 - p), reward + previous * d)
            following[history + (-previous,)] = (weight * p, reward)
        records = following
    probabilities, derivative = [], []
    for history in sorted(records):
        weight, reward = records[history]
        if history[-1] == 1:
            probabilities.extend([weight / 2, weight / 2])
            derivative.extend([-weight * reward / 2, weight * reward / 2])
        else:
            probabilities.append(weight)
            derivative.append(0.)
    return np.array(probabilities), np.array(derivative)


class TimingPrecisionTests(unittest.TestCase):
    def test_systematic_offset_kraus_and_operating_point_derivatives(self):
        for g, h, fraction, phi in ((.7, .5, .17, .31), (1.1, .6, -.29, -.73),
                                     (3., .2, .0, 1.21)):
            offset = fraction * h
            for epsilon in (-.37, 0., .53):
                u, v, w, x = coefficients(g, h, epsilon, offset)
                expected = [np.kron(u * I - 1j * v * Z, I),
                            np.kron(-1j * (w * axis(phi) + x * axis_derivative(phi)), I)]
                actual = physical_kraus(framed_unitary(g, h, epsilon, phi, offset))
                assert_allclose(actual, expected, atol=3e-15)
            step = 1e-6
            positive = physical_kraus(framed_unitary(g, h, step, phi, offset))
            negative = physical_kraus(framed_unitary(g, h, -step, phi, offset))
            tangent = [(a - b) / (2 * step) for a, b in zip(positive, negative)]
            amplitude = np.sin(g * h) / g
            transverse = (np.cos(2 * g * offset) - np.cos(g * h)) / g
            assert_allclose(tangent[0], -.5j * amplitude * np.kron(Z, I), atol=2e-10)
            assert_allclose(tangent[1], -.5j * transverse * np.kron(axis_derivative(phi), I),
                            atol=2e-10)

    def test_unobserved_jitter_channel_is_exact_three_kraus_mixture(self):
        for g, h, epsilon, phi, fraction in ((.8, .6, .0, .43, .12),
                                            (.8, .6, .7, .43, .12),
                                            (1.3, .5, -.8, -.91, .31)):
            offset = fraction * h
            unitaries = [framed_unitary(g, h, epsilon, phi, sign * offset)
                         for sign in (-1, 1)]
            kraus = [np.kron(k, I) for k in jitter_kraus(g, h, epsilon, phi, offset)]
            assert_allclose(sum(k.conj().T @ k for k in kraus), np.eye(4), atol=3e-15)
            for i in range(4):
                for j in range(4):
                    unit = np.zeros((4, 4), dtype=complex)
                    unit[i, j] = 1
                    assert_allclose(hidden_channel(unitaries, unit),
                                    sum(conjugate(k, unit) for k in kraus), atol=4e-15)
            averaged = hidden_channel(unitaries, INITIAL)
            midpoint = reduced_cell(framed_unitary(g, h, epsilon, phi, 0.), INITIAL)
            self.assertGreater(np.linalg.norm(averaged - midpoint), .001)

    def test_common_plain_curve_and_hidden_jitter_gauge_cancel_beta(self):
        for g, h, epsilon, phi, offset in ((.8, .6, .17, .43, .07),
                                          (1.1, .5, -.33, -.57, .11),
                                          (2., .3, .51, 1.21, .03)):
            slope, t, expected_alpha = gauge_data(g, h, epsilon, offset)
            step = 1e-6
            center = jitter_kraus(g, h, epsilon, phi, offset)
            plus = jitter_kraus(g, h, epsilon + step, phi + slope * step, offset)
            minus = jitter_kraus(g, h, epsilon - step, phi - slope * step, offset)
            tangent = [(a - b) / (2 * step) for a, b in zip(plus, minus)]
            gauge = np.zeros((3, 3), dtype=complex)
            gauge[1, 2], gauge[2, 1] = 1j * t, -1j * t
            gauged = [tangent[j] - 1j * sum(gauge[j, k] * center[k] for k in range(3))
                      for j in range(3)]
            beta = 1j * sum(k.conj().T @ d for k, d in zip(center, gauged))
            alpha = sum(d.conj().T @ d for d in gauged)
            assert_allclose(beta, np.zeros((2, 2)), atol=3e-10)
            assert_allclose(alpha, expected_alpha * I, rtol=3e-8, atol=3e-10)
            plain = cell_kraus(g, h, epsilon, phi)
            plain_plus = cell_kraus(g, h, epsilon + step, phi + slope * step)
            plain_minus = cell_kraus(g, h, epsilon - step, phi - slope * step)
            plain_tangent = [(a - b) / (2 * step) for a, b in zip(plain_plus, plain_minus)]
            assert_allclose(1j * sum(k.conj().T @ d for k, d in zip(plain, plain_tangent)),
                            np.zeros((2, 2)), atol=3e-10)

    def test_actual_fixed_recovery_information_including_zero_jitter(self):
        g, h, phi = .8, .6, .327
        amplitude = np.sin(g * h) / g
        for fraction, cells in ((0., 1), (0., 7), (.04, 4), (.21, 1), (.21, 11), (.43, 7)):
            offset = fraction * h
            likelihood = lambda point: physical_recovery(g, h, offset, cells, *point)
            self.assertAlmostEqual(likelihood([0., phi]).sum(), 1., places=12)
            information = numerical_fisher(likelihood, [0., phi])
            efficient = information[0, 0]
            if information[1, 1] > 1e-12:
                efficient -= information[0, 1] ** 2 / information[1, 1]
            expected = cells ** 2 * amplitude ** 2 / (1 + (cells - 1) * np.sin(2 * g * offset) ** 2)
            self.assertAlmostEqual(efficient / expected, 1., delta=3e-6)

    def test_timing_menu_has_positive_local_drift_and_correct_full_record_tangent(self):
        g, h, phi = .9, .6, .37
        pa_plain = np.sin(g * h) ** 2
        amplitude = np.sin(g * h) / g
        for fraction, cells in ((0., 3), (.11, 4), (.32, 6), (.49, 3)):
            offset = fraction * h
            p_echo = np.sin(2 * g * offset) ** 2
            numerator = amplitude * (pa_plain * np.cos(2 * g * offset)
                                     - p_echo * np.cos(g * h))
            self.assertGreater(numerator / (pa_plain + p_echo), 0.)
            expected, derivative = frozen_menu_records(g, h, offset, cells)
            actual = physical_menu_records(g, h, offset, cells, 0., phi)
            assert_allclose(actual, expected, atol=4e-15)
            step = 1e-6
            tangent = (physical_menu_records(g, h, offset, cells, step, phi)
                       - physical_menu_records(g, h, offset, cells, -step, phi)) / (2 * step)
            assert_allclose(tangent, derivative, atol=2e-10)
            assert_allclose(physical_menu_records(g, h, offset, cells, 0., -1.13),
                            actual, atol=4e-15)
            self.assertAlmostEqual(actual.sum(), 1., places=13)

    def test_systematic_menu_even_records_have_the_exact_flip_axis_phase(self):
        g, h = .8, .6
        chi = g * h
        for fraction, cells, epsilon in ((.19, 4, -.37 / h),
                                         (-.23, 6, .31 / h),
                                         (.37, 6, .27 / h)):
            offset = fraction * h
            u, v, w, x = coefficients(g, h, epsilon, offset)
            radius = np.sqrt(g * g + epsilon * epsilon / 4)
            p_echo, p_plain = w * w + x * x, (g * np.sin(radius * h) / radius) ** 2
            theta_echo, zeta_echo = 2 * np.arctan(v / u), np.arctan(x / w)
            theta_plain = 2 * np.arctan(epsilon * np.tan(radius * h) / (2 * radius))
            original = systematic_menu_states(g, h, offset, cells, epsilon, .41)
            other_axis = systematic_menu_states(g, h, offset, cells, epsilon, -1.17)
            self.assertEqual(len(original), 2 ** cells)
            self.assertAlmostEqual(sum(np.trace(state).real for state in original.values()), 1., places=13)
            for history, state in original.items():
                previous, weight, phase = 1, 1., 0.
                for current in history:
                    p, theta, zeta = ((p_echo, theta_echo, zeta_echo) if previous == 1
                                     else (p_plain, theta_plain, 0.))
                    if current == previous:
                        weight *= 1 - p
                        phase += previous * theta
                    else:
                        weight *= p
                        phase -= 2 * previous * zeta
                    previous = current
                self.assertAlmostEqual(np.trace(state).real, weight, places=14)
                if history[-1] == 1:
                    rotation = np.kron(np.diag(np.exp(-.5j * phase * np.array([1, -1]))), I)
                    assert_allclose(state, weight * conjugate(rotation, INITIAL), atol=5e-15)
                    assert_allclose(state, other_axis[history], atol=5e-15)
            z = 2 * g * offset
            pe, pp = np.sin(z) ** 2, np.sin(chi) ** 2
            de, ze = np.sin(chi) / (g * np.cos(z)), (np.cos(z) - np.cos(chi)) / (2 * g * np.sin(z))
            fe, fp = (1 - pe) * de - 2 * pe * ze, np.sin(chi) * np.cos(chi) / g
            contrast = ((np.sin(chi) - np.sin(z)) * np.sin(chi + z)
                        / (g * np.sin(chi) * np.sin(z) ** 2))
            self.assertGreater(contrast, 0.)
            self.assertAlmostEqual((fe / pe - fp / pp) / contrast, 1., places=13)

    def test_hidden_jitter_rank_change_and_mixed_odd_branch(self):
        g, h, phi = .8, .6, .43
        for epsilon, offset, expected_rank in ((.4, .09, 3), (0., .09, 2),
                                               (.4, 0., 2), (0., 0., 1)):
            kraus = []
            for sign in (-1, 1):
                for full in physical_kraus(framed_unitary(g, h, epsilon, phi, sign * offset)):
                    sensor = full.reshape(2, 2, 2, 2)[:, 0, :, 0]
                    kraus.append(sensor / np.sqrt(2))
            choi = sum(np.outer(k.ravel(), k.ravel().conj()) for k in kraus)
            self.assertEqual(np.count_nonzero(np.linalg.eigvalsh(choi) > 1e-10), expected_rank)
        unitaries = [framed_unitary(g, h, .4, phi, sign * .09) for sign in (-1, 1)]
        odd = conjugate(ODD, hidden_channel(unitaries, INITIAL))
        odd /= np.trace(odd)
        self.assertLess(np.trace(odd @ odd).real, .999)
        self.assertEqual(np.count_nonzero(np.linalg.eigvalsh(odd) > 1e-10), 2)

    def test_small_jitter_gauge_growth_has_a_uniform_quadratic_envelope(self):
        g, h = .8, .6
        epsilon_low, epsilon_high = .1 / h, .3 / h
        maximum_radius = np.sqrt(g * g + epsilon_high ** 2 / 4)
        chi, maximum_offset = g * h, h / 4
        self.assertLess(maximum_radius * h, np.pi / 4)
        minimum_plain_probability = (g / maximum_radius * np.sin(chi)) ** 2
        maximum_slope = h / (2 * minimum_plain_probability)
        derivative_bound = h * np.sqrt(.25 + g * g * maximum_slope ** 2)
        minimum_x = epsilon_low * g * (np.cos(chi / 2) - np.cos(chi)) / (2 * maximum_radius ** 2)
        w_coefficient = 4 * g / np.pi
        envelope = (2 * maximum_offset ** 2 * derivative_bound ** 2
                    + derivative_bound ** 2 / (2 * w_coefficient ** 2 * minimum_x ** 2))
        for epsilon in np.linspace(epsilon_low, epsilon_high, 5):
            for offset in np.geomspace(h / 4000, maximum_offset, 9):
                _, _, alpha = gauge_data(g, h, epsilon, offset)
                self.assertLessEqual(offset ** 2 * alpha, envelope)
            u, v, _, x = coefficients(g, h, epsilon, 0.)
            du, dv, _, _ = coefficient_derivative(g, h, epsilon, 0.)
            slope = plain_curve_slope(g, h, epsilon)
            limit = (u * dv - v * du - x * x * slope) ** 2 / (16 * g * g)
            self.assertGreater(limit, 0.)
            offset = h * 1e-5
            _, _, alpha = gauge_data(g, h, epsilon, offset)
            self.assertAlmostEqual(offset ** 2 * alpha / limit, 1., delta=2e-5)


if __name__ == '__main__':
    unittest.main()
