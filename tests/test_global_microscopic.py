"""Finite checks for global microscopic estimation and temporal access.

Physical records use simultaneous sensor--bath Hamiltonians. Exact finite
distributions check the conditional estimator, not an asymptotic minimax claim.
"""
import unittest

import numpy as np
from numpy.testing import assert_allclose
from scipy.linalg import expm
from scipy.optimize import brentq

from test_microscopic import (
    I, X, Z, EVEN, ODD, XL, YL, INITIAL, axis,
    joint_unitary, reduced_cell, conjugate,
)
from test_identifiability import adaptive_boundary_record


def plain_coefficients(g, interval, epsilon):
    radius = np.sqrt(g * g + epsilon * epsilon / 4)
    rdot = epsilon / (4 * radius)
    sine, cosine = np.sin(radius * interval), np.cos(radius * interval)
    a, b, c = cosine, epsilon * sine / (2 * radius), g * sine / radius
    adot = -interval * rdot * sine
    bdot = ((1 / (2 * radius) - epsilon * rdot / (2 * radius ** 2)) * sine
            + epsilon * interval * rdot * cosine / (2 * radius))
    cdot = g * rdot * (interval * cosine / radius - sine / radius ** 2)
    return np.array([a, b, c]), np.array([adot, bdot, cdot])


def physical_kraus(g, interval, epsilon, phi):
    hamiltonian = .5 * epsilon * np.kron(Z, I) + g * np.kron(axis(phi), X)
    unitary = expm(-1j * interval * hamiltonian).reshape(2, 2, 2, 2)
    return [unitary[:, output, :, 0] for output in (0, 1)]


def menu_data(kind, couplings, interval, epsilon):
    """Flip probabilities and continuous no-flip phases of both settings."""
    first, second = couplings
    a, b, c = plain_coefficients(second, interval, epsilon)[0]
    second_data = (c * c, 2 * np.arctan2(b, a))
    if kind == 'coupling':
        a, b, c = plain_coefficients(first, interval, epsilon)[0]
        return np.array([c * c, second_data[0]]), np.array([
            2 * np.arctan2(b, a), second_data[1]])
    radius = np.sqrt(first * first + epsilon * epsilon / 4)
    cosine = np.cos(radius * interval)
    u = cosine + first ** 2 * (1 - cosine) / radius ** 2
    v = epsilon * np.sin(radius * interval) / (2 * radius)
    x = epsilon * first * (1 - cosine) / (2 * radius ** 2)
    return np.array([x * x, second_data[0]]), np.array([
        2 * np.arctan2(v, u), second_data[1]])


def zero_derivatives(kind, couplings, interval):
    first, second = couplings
    first_d = (np.tan(first * interval) / first if kind == 'coupling'
               else np.sin(first * interval) / first)
    return np.array([first_d, np.tan(second * interval) / second])


def frozen_drift(probabilities, derivatives):
    pa, pb = probabilities
    da, db = derivatives
    return (pb * (1 - pa) * da - pa * (1 - pb) * db) / (pa + pb)


def physical_records(kind, couplings, interval, cells, epsilon, phi):
    """Complete parity tree, zero-weight branches and pulse times retained.

    The echo uses its known output frame. The additional Z on an odd echoed
    outcome belongs to the already counted boundary parity instrument.
    """
    first, second = couplings
    full_a = joint_unitary(first, interval, epsilon, phi)
    full_b = joint_unitary(second, interval, epsilon, phi)
    half = joint_unitary(first, interval / 2, epsilon, phi)
    pulse = np.kron(np.kron(Z, I), I)
    echoed = pulse @ half @ pulse @ half
    correction = np.kron(Z, I)
    records = {(): (INITIAL.copy(), (0, 0), ())}
    for cell in range(cells):
        following = {}
        for history, (state, counts, pulses) in records.items():
            previous = history[-1] if history else 1
            echo = kind == 'timing' and previous == 1
            unitary = (echoed if echo else full_a) if previous == 1 else full_b
            evolved = reduced_cell(unitary, state)
            local_pulses = pulses + ((cell + .5) * interval,) if echo else pulses
            for parity, projector in ((1, EVEN), (-1, ODD)):
                measured = conjugate(projector, evolved)
                if echo and parity != previous:
                    measured = conjugate(correction, measured)
                updated = list(counts)
                if parity == previous:
                    updated[int(previous == -1)] += 1
                following[history + (parity,)] = (measured, tuple(updated), local_pulses)
        records = following
    return records


def count_distribution(probabilities, cells):
    """Exact no-flip-count law with terminal parity retained."""
    pa, pb = probabilities
    weights = np.zeros((2, cells + 1, cells + 1))
    weights[0, 0, 0] = 1
    for _ in range(cells):
        following = np.zeros_like(weights)
        following[0, 1:, :] += (1 - pa) * weights[0, :-1, :]
        following[1] += pa * weights[0]
        following[1, :, 1:] += (1 - pb) * weights[1, :, :-1]
        following[0] += pb * weights[1]
        weights = following
    return weights


def reward_moments(probabilities, derivatives, cells):
    """Independent two-state recursion for the first two additive moments."""
    pa, pb = probabilities
    transition = np.array([[1 - pa, pa], [pb, 1 - pb]])
    reward = np.diag([derivatives[0], -derivatives[1]])
    mass, first, second = np.array([1., 0.]), np.zeros(2), np.zeros(2)
    for _ in range(cells):
        new_mass, new_first, new_second = np.zeros(2), np.zeros(2), np.zeros(2)
        for start in range(2):
            for end in range(2):
                p, value = transition[start, end], reward[start, end]
                new_mass[end] += p * mass[start]
                new_first[end] += p * (first[start] + value * mass[start])
                new_second[end] += p * (second[start] + 2 * value * first[start]
                                      + value * value * mass[start])
        mass, first, second = new_mass, new_first, new_second
    return mass, first.sum(), second.sum() - first.sum() ** 2


def record_phase(counts, phases):
    return counts[0] * phases[0] - counts[1] * phases[1]


def inverse_on_interval(function, value, interval):
    left, right = interval
    if left == right:
        return left
    target = np.clip(value, function(left), function(right))
    return brentq(lambda u: function(u) - target, left, right, xtol=2e-14)


def nested_update(interval, radius, function, readouts, minimum_count):
    estimate = ((interval[0] + interval[1]) / 2 if len(readouts) < minimum_count
                else inverse_on_interval(function, np.mean(readouts), interval))
    return (max(interval[0], estimate - radius),
            min(interval[1], estimate + radius)), estimate


def charged_schedule(stages, p0, alpha, beta, base_length, calibration_slope):
    """Actual trial counts; a failed block has the same scheduled length."""
    scale = np.pi / (8 * beta)
    gamma = min(p0 ** 2 / 2, p0 * alpha ** 2 * scale ** 2 / 8)
    calibration = int(np.ceil(2 * base_length ** 2 / (calibration_slope ** 2 * scale ** 2)
                              * (stages * np.log(8) + np.log(2))))
    blocks = [(base_length * 2 ** stage,
               int(np.ceil(((stages - stage) * np.log(8) + np.log(12)) / gamma)))
              for stage in range(1, stages + 1)]
    return calibration, blocks


class GlobalMicroscopicChecks(unittest.TestCase):
    def test_off_compensation_nuisance_curve_from_joint_unitary(self):
        for g, interval, epsilon in ((.3, .6, -.4), (.7, .8, 0.),
                                     (.7, .8, .3), (.8, .9, -.21)):
            phi, step = .47, 2e-6
            (a, b, c), (adot, bdot, cdot) = plain_coefficients(g, interval, epsilon)
            slope = (a * bdot - b * adot) / c ** 2
            center = physical_kraus(g, interval, epsilon, phi)
            plus = physical_kraus(g, interval, epsilon + step, phi + slope * step)
            minus = physical_kraus(g, interval, epsilon - step, phi - slope * step)
            tangent = [(high - low) / (2 * step) for high, low in zip(plus, minus)]
            overlap = sum(k.conj().T @ derivative for k, derivative in zip(center, tangent))
            alpha = sum(derivative.conj().T @ derivative for derivative in tangent)
            exact = adot ** 2 + bdot ** 2 + cdot ** 2 + c ** 2 * slope ** 2
            assert_allclose(overlap, np.zeros((2, 2)), atol=2e-9)
            assert_allclose(alpha, exact * I, atol=2e-9)
            self.assertLessEqual(4 * exact, interval ** 2 / c ** 2 + 1e-12)

    def test_two_coupling_even_records_have_exact_known_phase(self):
        couplings, interval, cells = (.2, .75), 1., 6
        for epsilon in (-.23, 0., .17):
            probabilities, phases = menu_data('coupling', couplings, interval, epsilon)
            reference = None
            for phi in (-.83, .41, 1.92):
                records = physical_records('coupling', couplings, interval, cells, epsilon, phi)
                masses = []
                for history, (state, counts, pulses) in records.items():
                    mass = np.trace(state).real
                    masses.append(mass)
                    previous, weight = 1, 1.
                    for parity in history:
                        flip = probabilities[int(previous == -1)]
                        weight *= 1 - flip if parity == previous else flip
                        previous = parity
                    self.assertAlmostEqual(mass, weight, places=14)
                    self.assertEqual(pulses, ())
                    if history[-1] == 1:
                        rotation = expm(-.5j * record_phase(counts, phases) * np.kron(Z, I))
                        assert_allclose(state, mass * conjugate(rotation, INITIAL), atol=3e-15)
                self.assertAlmostEqual(sum(masses), 1., places=13)
                if reference is not None:
                    assert_allclose(masses, reference, atol=3e-15)
                reference = masses

    def test_corrected_temporal_menu_records_cancel_unknown_direction(self):
        couplings, interval, cells = (.55, .55), .8, 6
        for epsilon in (-.31, 0., .27):
            probabilities, phases = menu_data('timing', couplings, interval, epsilon)
            for phi in (-.63, 1.47):
                records = physical_records('timing', couplings, interval, cells, epsilon, phi)
                self.assertEqual(len(records), 2 ** cells)
                for history, (state, counts, pulses) in records.items():
                    mass = np.trace(state).real
                    self.assertLessEqual(len(pulses), cells)
                    previous, weight = 1, 1.
                    for parity in history:
                        flip = probabilities[int(previous == -1)]
                        weight *= 1 - flip if parity == previous else flip
                        previous = parity
                    self.assertAlmostEqual(mass, weight, places=14)
                    if history[-1] == 1:
                        rotation = expm(-.5j * record_phase(counts, phases) * np.kron(Z, I))
                        assert_allclose(state, mass * conjugate(rotation, INITIAL), atol=4e-15)
                self.assertAlmostEqual(sum(np.trace(item[0]).real for item in records.values()),
                                       1., places=13)

    def test_exact_reward_distribution_and_nonstationary_moments(self):
        for kind, couplings, interval in (('coupling', (.2, .75), 1.),
                                          ('timing', (.55, .55), .8)):
            derivatives = zero_derivatives(kind, couplings, interval)
            mu0 = frozen_drift(menu_data(kind, couplings, interval, 0.)[0], derivatives)
            for epsilon in (-.12, 0., .12):
                probabilities = menu_data(kind, couplings, interval, epsilon)[0]
                pa, pb = probabilities
                decay = 1 - pa - pb
                drift = frozen_drift(probabilities, derivatives)
                for cells in (12, 80):
                    weights = count_distribution(probabilities, cells)
                    counts = np.arange(cells + 1)
                    reward = counts[:, None] * derivatives[0] - counts[None, :] * derivatives[1]
                    mean = np.sum(weights * reward)
                    variance = np.sum(weights * (reward - mean) ** 2)
                    mass, independent_mean, independent_variance = reward_moments(
                        probabilities, derivatives, cells)
                    assert_allclose(weights.sum(axis=(1, 2)), mass, atol=2e-14)
                    self.assertAlmostEqual(mean, independent_mean, places=10)
                    self.assertAlmostEqual(variance, independent_variance, delta=2e-10)
                    transient = (pa / (pa + pb) * ((1 - pa) * derivatives[0]
                                 + (1 - pb) * derivatives[1])
                                 * (1 - decay ** cells) / (1 - decay))
                    self.assertAlmostEqual(mean, cells * drift + transient, places=10)
                    self.assertGreaterEqual(mean, cells * drift - 1e-12)
                    bound = derivatives.max() ** 2 * (1 + 2 / (1 - decay)) * cells
                    self.assertLessEqual(variance, bound)
                    accepted = weights[0][reward >= mu0 * cells / 2].sum()
                    self.assertGreaterEqual(accepted, .25)
                    if kind == 'timing' and epsilon == 0.:
                        self.assertAlmostEqual(accepted, 1., places=13)

    def test_accepted_record_phase_derivatives_are_uniform_on_sampled_band(self):
        for kind, couplings, interval in (('coupling', (.2, .75), 1.),
                                          ('timing', (.55, .55), .8)):
            cells, step = 32, 1e-5
            derivatives = zero_derivatives(kind, couplings, interval)
            mu0 = frozen_drift(menu_data(kind, couplings, interval, 0.)[0], derivatives)
            counts = np.arange(cells + 1)
            frozen = counts[:, None] * derivatives[0] - counts[None, :] * derivatives[1]
            support = count_distribution(menu_data(kind, couplings, interval, .12)[0], cells)[0] > 0
            accepted = support & (frozen >= mu0 * cells / 2)
            self.assertGreater(accepted.sum(), 1)
            for candidate in np.linspace(-.12, .12, 9):
                high = menu_data(kind, couplings, interval, candidate + step)[1]
                low = menu_data(kind, couplings, interval, candidate - step)[1]
                slope = (high - low) / (2 * step)
                self.assertLessEqual(np.max(np.abs(slope - derivatives)), mu0 / 4)
                record_slopes = counts[:, None] * slope[0] - counts[None, :] * slope[1]
                self.assertGreaterEqual(record_slopes[accepted].min(), mu0 * cells / 4)

    def test_record_centered_inverse_uses_actual_conditional_probabilities(self):
        couplings, interval, cells, epsilon, center = (.2, .75), 1., 6, .041, .02
        records = physical_records('coupling', couplings, interval, cells, epsilon, 1.13)
        phases_at_center = menu_data('coupling', couplings, interval, center)[1]
        derivatives = zero_derivatives('coupling', couplings, interval)
        mu0 = frozen_drift(menu_data('coupling', couplings, interval, 0.)[0], derivatives)
        accepted = [item for history, item in records.items() if history[-1] == 1
                    and record_phase(item[1], derivatives) >= mu0 * cells / 2]
        selected = (accepted * 8)[:32]
        self.assertEqual(len(selected), 32)
        def expected_mean(candidate):
            phases = menu_data('coupling', couplings, interval, candidate)[1]
            return np.mean([np.sin(record_phase(item[1], phases - phases_at_center))
                            for item in selected])
        distribution = np.array([1.])
        actual_means = []
        for state, counts, _ in selected:
            angle = record_phase(counts, phases_at_center)
            observable = np.cos(angle) * YL - np.sin(angle) * XL
            mean = np.trace(observable @ state).real / np.trace(state).real
            actual_means.append(mean)
            distribution = np.convolve(distribution, [(1 - mean) / 2, (1 + mean) / 2])
        self.assertAlmostEqual(np.mean(actual_means), expected_mean(epsilon), places=13)
        candidate_interval = (-.02, .06)
        recovered = inverse_on_interval(expected_mean, np.mean(actual_means), candidate_interval)
        self.assertAlmostEqual(recovered, epsilon, places=12)
        samples = np.linspace(-1., 1., len(selected) + 1)
        estimates = np.array([inverse_on_interval(expected_mean, value, candidate_interval)
                              for value in samples])
        risk = distribution @ ((estimates - epsilon) ** 2)
        self.assertLessEqual(risk, 2 / (len(selected) * (mu0 / 4) ** 2 * cells ** 2))
        phase_offsets = [record_phase(item[1], menu_data('coupling', couplings, interval, epsilon)[1]
                                      - phases_at_center) for item in selected]
        self.assertGreater(abs(np.sin(np.mean(phase_offsets)) - expected_mean(epsilon)), 1e-8)

    def test_full_record_law_changes_with_frequency_and_keeps_failed_records(self):
        couplings, interval, cells, center = (.2, .75), 1., 5, -.03
        distributions = []
        for epsilon in (.07, .31):
            records = physical_records('coupling', couplings, interval, cells, epsilon, .51)
            phases_at_center = menu_data('coupling', couplings, interval, center)[1]
            complete, masses = [], []
            for history, (state, counts, _) in records.items():
                mass = np.trace(state).real
                masses.append(mass)
                if history[-1] != 1:
                    complete.append(mass)
                    continue
                angle = record_phase(counts, phases_at_center)
                observable = np.cos(angle) * YL - np.sin(angle) * XL
                complete.extend([np.trace((EVEN + sign * observable) @ state).real / 2
                                 for sign in (-1, 1)])
            self.assertAlmostEqual(sum(complete), 1., places=13)
            self.assertGreater(sum(mass for history, mass in zip(records, masses)
                                   if history[-1] == -1), 0.)
            distributions.append(np.array(masses))
        self.assertGreater(np.linalg.norm(distributions[1] - distributions[0], ord=1), 1e-4)

    def test_nested_intervals_limit_the_damage_of_wrong_and_failed_readouts(self):
        interval, truth = (-.1, .1), .035
        last_good = None
        readout_stages = ([1.] * 17 + [-1.] * 15, [-1.] * 8, [], [1.] * 8)
        for level, readouts in enumerate(readout_stages, 1):
            center = sum(interval) / 2
            length = 2 ** level
            phase_at_center = menu_data('coupling', (.2, .75), 1., center)[1][0]
            def function(candidate):
                phase = menu_data('coupling', (.2, .75), 1., candidate)[1][0]
                return np.sin(length * (phase - phase_at_center))
            updated, estimate = nested_update(interval, .01 / length, function, readouts, 4)
            self.assertLessEqual(interval[0], updated[0])
            self.assertGreaterEqual(interval[1], updated[1])
            self.assertLessEqual(updated[0], updated[1])
            self.assertGreaterEqual(estimate, interval[0])
            self.assertLessEqual(estimate, interval[1])
            interval = updated
            if level == 1:
                self.assertLessEqual(interval[0], truth)
                self.assertGreaterEqual(interval[1], truth)
                last_good = interval
            elif level == 2:
                self.assertFalse(interval[0] <= truth <= interval[1])
        self.assertFalse(interval[0] <= truth <= interval[1])
        self.assertLessEqual(abs(sum(interval) / 2 - truth), last_good[1] - last_good[0])
        self.assertLess(last_good[1] - last_good[0], .011)
        point, estimate = nested_update((.2, .2), .1, lambda u: u, [1.], 1)
        self.assertEqual(point, (.2, .2))
        self.assertEqual(estimate, .2)

    def test_multiscale_schedule_charges_failed_blocks_and_selects_feasible_depth(self):
        parameters = dict(p0=.5, alpha=2., beta=2., base_length=1, calibration_slope=.6)
        costs = []
        for stages in range(1, 9):
            calibration, schedule = charged_schedule(stages, **parameters)
            clock, failed_cells = calibration, 0
            for length, attempts in schedule:
                for attempt in range(attempts):
                    clock += length
                    if attempt % 3 == 0:
                        failed_cells += length
            self.assertGreater(failed_cells, 0)
            self.assertEqual(clock, calibration + sum(length * attempts
                                                     for length, attempts in schedule))
            self.assertGreater(clock, failed_cells + calibration)
            self.assertEqual(schedule[-1][0], 2 ** stages)
            self.assertEqual(len(schedule), stages)
            costs.append(clock)
        scale = np.pi / (8 * parameters['beta'])
        gamma = min(parameters['p0'] ** 2 / 2,
                    parameters['p0'] * parameters['alpha'] ** 2 * scale ** 2 / 8)
        coarse_factor = 2 / (parameters['calibration_slope'] ** 2 * scale ** 2)
        cost_constant = coarse_factor * (np.log(8) + np.log(2)) + 1
        cost_constant += 2 * (np.log(8) + np.log(12)) / gamma + 2
        for stages, cost in enumerate(costs, 1):
            self.assertLessEqual(cost, cost_constant * 2 ** stages)
        for next_depth in range(2, 9):
            budget = costs[next_depth - 1] - 1
            selected = max(depth for depth, cost in enumerate(costs, 1) if cost <= budget)
            self.assertEqual(selected, next_depth - 1)
            self.assertLessEqual(costs[selected - 1], budget)
            self.assertLess(budget, costs[selected])

    def test_temporal_menu_counts_pulses_and_early_readout_on_every_branch(self):
        interval = .8
        for total_cells in range(3, 9):
            for interior_budget in range(1, total_cells):
                used = min(interior_budget, (total_cells - 1) // 2)
                records = physical_records('timing', (.55, .55), interval, used, 0., .29)
                for _, (_, _, pulses) in records.items():
                    boundaries = tuple(index * interval for index in range(1, used + 1))
                    contacts = sorted(pulses + boundaries)
                    self.assertEqual(len(contacts), len(set(contacts)))
                    self.assertLessEqual(len(pulses), interior_budget)
                    self.assertLessEqual(len(contacts), total_cells - 1)
                    self.assertLess(contacts[-1], total_cells * interval)
                    self.assertIn(used * interval, contacts)
                self.assertGreaterEqual(used, interior_budget / 3)

    def test_adaptive_complete_output_information_obeys_uniform_path_bound(self):
        g, interval, phi, cells, step = .7, .8, -.39, 4, 1e-6
        for epsilon in (-.23, .0, .29):
            (a, b, c), (adot, bdot, _) = plain_coefficients(g, interval, epsilon)
            slope = (a * bdot - b * adot) / c ** 2
            center = adaptive_boundary_record(g, interval, epsilon, phi)
            plus = adaptive_boundary_record(g, interval, epsilon + step, phi + slope * step)
            minus = adaptive_boundary_record(g, interval, epsilon - step, phi - slope * step)
            derivative = (plus - minus) / (2 * step)
            self.assertGreater(center.min(), 0.)
            information = np.sum(derivative ** 2 / center)
            self.assertGreater(information, 1e-5)
            self.assertLessEqual(information, cells * interval ** 2 / c ** 2)


if __name__ == '__main__':
    unittest.main()
