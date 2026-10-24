"""Algebraic and numerical checks; not an independent proof review."""
from pathlib import Path
from decimal import Decimal, localcontext
import math
import sys
import unittest

import numpy as np
from numpy.testing import assert_allclose
from scipy.linalg import expm
from scipy.optimize import linprog
import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import nras


class AlgebraTests(unittest.TestCase):
    def test_involution_and_anticommutation(self):
        for phi in np.linspace(-4, 4, 27):
            n = nras.noise_operator(phi)
            assert_allclose(n @ n, nras.I, atol=1e-14)
            assert_allclose(n @ nras.Z @ n, -nras.Z, atol=1e-14)

    def test_fixed_recovery_phase(self):
        for phi in np.linspace(-3, 3, 13):
            assert_allclose(nras.X @ nras.noise_operator(phi),
                            nras.rotation(-2 * phi), atol=1e-14)

    def test_nuisance_path_operators(self):
        rng = np.random.default_rng(102)
        for _ in range(100):
            phi, s, c = rng.normal(size=3)
            g = rng.uniform(.1, 4)
            aa, bb = nras.path_operators(phi, s, g, c)
            assert_allclose(aa, g * c * c * nras.I, atol=1e-13)
            assert_allclose(bb, (s / 2 - g * c) * nras.Z, atol=1e-13)

    def test_fixed_rate_cancellation(self):
        aa, bb = nras.path_operators(.73, 1, 1.9, 1 / 3.8)
        assert_allclose(bb, np.zeros((2, 2)), atol=1e-15)
        assert_allclose(aa, nras.I / 7.6, atol=1e-15)

    def test_symbolic_nuisance_identity(self):
        phi, g, c, s = sp.symbols('phi g c s', real=True)
        x, y, z = map(sp.Matrix, (nras.X, nras.Y, nras.Z))
        n = sp.cos(phi) * x + sp.sin(phi) * y
        derivative = sp.diff(n, phi)
        aa = sp.simplify(g * c ** 2 * derivative.conjugate().T * derivative)
        bb = sp.simplify(s * z / 2 - sp.I * g * c / 2 * (
            derivative.conjugate().T * n - n.conjugate().T * derivative))
        self.assertEqual(sp.simplify(aa - g * c ** 2 * sp.eye(2)), sp.zeros(2))
        self.assertEqual(sp.simplify(bb - (s / 2 - g * c) * z), sp.zeros(2))

    def test_random_trajectories(self):
        rng = np.random.default_rng(501)
        for _ in range(500):
            count = int(rng.integers(1, 35))
            durations = rng.exponential(size=count)
            signals = rng.normal(size=count)
            flags = rng.integers(0, 2, size=count).astype(bool)
            phi, omega = rng.normal(size=2)
            u, d, jumps = nras.trajectory(omega, phi, durations, signals, flags)
            expected = np.linalg.matrix_power(nras.noise_operator(phi), jumps % 2)
            expected = expected @ nras.rotation(omega * d)
            assert_allclose(u, expected, atol=8e-14)

    def test_odd_trajectory_retains_unknown_direction(self):
        u, d, _ = nras.trajectory(.7, .3, [1.0], [1.0], [True])
        self.assertGreater(np.linalg.norm(u - nras.rotation(.7 * d)), .5)

    def test_collision_channel(self):
        rng = np.random.default_rng(701)
        for _ in range(25):
            chi, phi = rng.normal(size=2)
            state = rng.normal(size=2) + 1j * rng.normal(size=2)
            state /= np.linalg.norm(state)
            rho = np.outer(state, state.conj())
            n = nras.noise_operator(phi)
            v = expm(-1j * chi * np.kron(n, nras.X))
            joint = v @ np.kron(rho, np.diag([1., 0.])) @ v.conj().T
            reduced = np.trace(joint.reshape(2, 2, 2, 2), axis1=1, axis2=3)
            expected = math.cos(chi) ** 2 * rho + math.sin(chi) ** 2 * n @ rho @ n
            assert_allclose(reduced, expected, atol=1e-14)

    def test_short_step_kraus_normalization(self):
        gamma, omega, dt = 1.7, .9, .003
        p = 1 - math.exp(-gamma * dt)
        r = nras.rotation(omega * dt)
        k0, k1 = math.sqrt(1-p) * r, math.sqrt(p) * nras.noise_operator(.7) @ r
        assert_allclose(k0.conj().T @ k0 + k1.conj().T @ k1, nras.I, atol=1e-14)


class ControlTests(unittest.TestCase):
    def test_pairwise_formula_against_linear_program(self):
        rng = np.random.default_rng(801)
        for _ in range(500):
            count = int(rng.integers(1, 10))
            s, g = rng.normal(size=count), rng.uniform(.1, 5, size=count)
            a_ub = np.vstack((np.column_stack((-2*g, -np.ones(count))),
                              np.column_stack((2*g, -np.ones(count)))))
            result = linprog([0., 1.], A_ub=a_ub, b_ub=np.r_[-s, s],
                             bounds=[(None, None), (0, None)], method='highs')
            self.assertTrue(result.success)
            speed, (i, j) = nras.control_speed(s, g)
            self.assertAlmostEqual(speed, result.fun, places=10)
            self.assertAlmostEqual(speed, abs(s[i]*g[j]-s[j]*g[i])/(g[i]+g[j]))

    def test_rate_only_contrast(self):
        self.assertEqual(nras.control_speed([1, 1], [1, 3])[0], .5)

    def test_proportional_clock_change_has_zero_speed(self):
        self.assertEqual(nras.control_speed([2, 4, 6], [1, 2, 3])[0], 0)

    def test_single_setting_has_zero_speed(self):
        self.assertEqual(nras.control_speed([-2], [3])[0], 0)

    def test_signal_sign_change(self):
        self.assertEqual(nras.control_speed([1, -1], [2, 2])[0], 1)

    def test_independent_axes_cancel_separately(self):
        for s, g, phi in [(1., 2., .4), (-3., .7, -.2)]:
            aa, bb = nras.path_operators(phi, s, g, s/(2*g))
            assert_allclose(bb, 0, atol=1e-14)
            assert_allclose(4*aa, s*s/g*nras.I, atol=1e-14)

    def test_invalid_settings(self):
        for s, g in [([], []), ([1], [0]), ([1, 2], [1]), ([np.nan], [1])]:
            with self.assertRaises(ValueError):
                nras.control_speed(s, g)


class TimingTests(unittest.TestCase):
    def test_first_passage_differential_equation(self):
        for a, b, q in [(1., 3., .2), (2., 2., .3), (.1, 4., -.1)]:
            k = nras.first_passage_exponent(q, a, b)
            self.assertAlmostEqual(k*k+(b-a)*k-q*(q+a+b), 0, places=12)
            vminus = (a+q-k)/a
            self.assertAlmostEqual(b-(k+b+q)*vminus, 0, places=12)

    def test_symbolic_first_passage_moments(self):
        q, a, delta, d = sp.symbols('q a delta d', positive=True)
        b = a + delta
        k = sp.sqrt(delta**2/4 + q*(a+b+q)) - delta/2
        mean = sp.diff(d*k, q).subs(q, 0)
        var = -sp.diff(d*k, q, 2).subs(q, 0)
        self.assertEqual(sp.simplify(mean-d*(a+b)/delta), 0)
        self.assertEqual(sp.simplify(var-8*a*b*d/delta**3), 0)

    def test_threefold_moments(self):
        self.assertEqual(nras.first_passage_moments(4, 1, 3), (8., 12.))

    def test_equal_rates_infinite_mean(self):
        self.assertEqual(nras.first_passage_moments(1, 2, 2), (math.inf, math.inf))
        self.assertAlmostEqual(nras.first_passage_exponent(.1, 2, 2), math.sqrt(.41))

    def test_laplace_normalization_and_composition(self):
        self.assertEqual(nras.first_passage_laplace(3, 1, 3, 0), 1)
        l1 = nras.first_passage_laplace(1, 1, 3, .2)
        l2 = nras.first_passage_laplace(2, 1, 3, .2)
        self.assertAlmostEqual(l1*l2, nras.first_passage_laplace(3, 1, 3, .2))

    def test_mgf_domain_and_small_q(self):
        with self.assertRaises(ValueError):
            nras.first_passage_exponent(-1, 1, 3)
        self.assertAlmostEqual(nras.first_passage_exponent(1e-12, 1, 3)/1e-12, 2, places=9)

    def test_mgf_nearly_equal_rates_against_high_precision(self):
        a, b, q = 1., math.nextafter(1., math.inf), -1e-34
        with localcontext() as context:
            context.prec = 80
            da, db, dq = map(Decimal, (a, b, q))
            delta = (db - da) / 2
            expected = float((delta * delta + dq * (da + db + dq)).sqrt() - delta)
        actual = nras.first_passage_exponent(q, a, b)
        self.assertTrue(math.isclose(actual, expected, rel_tol=2e-15))
        with self.assertRaises(ValueError):
            nras.first_passage_exponent(-1e-32, a, b)

    def test_mgf_large_positive_laplace_parameter(self):
        # k(q) / q -> 1; the intermediate discriminant need not fit in a float.
        self.assertTrue(math.isclose(nras.first_passage_exponent(1e200, 1, 3),
                                     1e200, rel_tol=2e-15))

    def test_threefold_finite_time_threshold(self):
        for t in [10, 18, 19, 20, 100]:
            lhs = nras.threefold_information_lower_bound(1, t)
            self.assertEqual(lhs > t, t > 19)

    def test_symmetric_telegraph_second_moment(self):
        # Differentiate the tilted generator, independently of the closed form.
        g, t, eps = 1.3, 2.7, 1e-4
        q = np.array([[-g, g], [g, -g]])
        def mgf(z):
            return (np.array([1., 0.]) @ expm((q+z*np.diag([1., -1.]))*t) @ np.ones(2))
        mean, second = nras.symmetric_signed_moments(g, t)
        self.assertAlmostEqual((mgf(eps)-mgf(-eps))/(2*eps), mean, places=7)
        self.assertAlmostEqual((mgf(eps)-2*mgf(0)+mgf(-eps))/eps**2, second, places=6)

    def test_symmetric_telegraph_short_exposure_against_high_precision(self):
        for rate, time in [(1e-18, 1.), (1., 1e-18), (1., 4e-4), (1., 6e-4)]:
            with self.subTest(rate=rate, time=time), localcontext() as context:
                context.prec = 80
                g, t = Decimal(rate), Decimal(time)
                transient = 1 - (-2 * g * t).exp()
                expected_mean = float(transient / (2 * g))
                expected_second = float(t / g - transient / (2 * g * g))
                mean, second = nras.symmetric_signed_moments(rate, time)
                self.assertTrue(math.isclose(mean, expected_mean, rel_tol=2e-15))
                self.assertTrue(math.isclose(second, expected_second, rel_tol=5e-13))
                self.assertGreater(second, 0.)
        self.assertEqual(nras.symmetric_signed_moments(1., 0.), (0., 0.))

    def test_invalid_rates_and_times(self):
        for a, b in [(0, 2), (2, 1), (1, math.inf)]:
            with self.assertRaises(ValueError):
                nras.rate_contrast(a, b)
        with self.assertRaises(ValueError):
            nras.first_passage_laplace(0, 1, 3, .1)


class CadenceTests(unittest.TestCase):
    def test_finite_cadence_against_augmented_generator(self):
        for a, b, dt in [(1., 3., .1), (.2, 2., 1.), (2., 2., .5)]:
            transitions, rewards = [], []
            for g, start in [(a, 0), (b, 1)]:
                # dp/dt=Q^T p, dy/dt=(1,-1)p; start is the measured sector.
                generator = np.array([[-g, g, 0], [g, -g, 0], [1, -1, 0]])
                initial = np.eye(3)[start]
                result = expm(generator*dt) @ initial
                transitions.append(result[:2])
                rewards.append(result[2])
            pa, pb = transitions[0][1], transitions[1][0]
            stationary = np.array([pb, pa])/(pa+pb)
            direct = stationary @ rewards / dt
            self.assertAlmostEqual(direct, nras.finite_cadence_speed(a, b, dt), places=12)

    def test_small_interval_limit(self):
        self.assertAlmostEqual(nras.finite_cadence_speed(1, 3, 1e-8), .5, places=7)

    def test_finite_interval_positive_and_equal_rate_zero(self):
        for dt in [.01, .1, 1, 10]:
            self.assertGreater(nras.finite_cadence_speed(1, 3, dt), 0)
            self.assertEqual(nras.finite_cadence_speed(2, 2, dt), 0)


class SimulationTests(unittest.TestCase):
    def test_stopping_distribution(self):
        samples = nras.sample_stopped(4, 1, 3, 30000, np.random.default_rng(1101))
        self.assertTrue(samples.completed.all())
        self.assertTrue((samples.jumps % 2 == 0).all())
        assert_allclose(samples.signed_times, 4)
        self.assertLess(abs(samples.times.mean()-8), 6*math.sqrt(12/len(samples.times)))
        self.assertLess(abs(samples.times.var(ddof=1)-12), 1.2)
        for q in [.1, .4]:
            values = np.exp(-q*samples.times)
            truth = nras.first_passage_laplace(4, 1, 3, q)
            self.assertLess(abs(values.mean()-truth), 6*values.std(ddof=1)/math.sqrt(len(values)))

    def test_deadline_accounts_for_failures(self):
        samples = nras.sample_stopped(5, 1, 3, 20000, np.random.default_rng(1102), deadline=20)
        self.assertTrue((samples.times <= 20+1e-12).all())
        self.assertTrue((samples.times[~samples.completed] == 20).all())
        self.assertGreater((~samples.completed).sum(), 0)
        info = 25*samples.completed.mean()
        self.assertGreater(info, nras.threefold_information_lower_bound(1, 20))
        assert_allclose(samples.signed_times[samples.completed], 5)

    def test_deadline_before_target_all_fail(self):
        samples = nras.sample_stopped(3, 1, 3, 100, np.random.default_rng(1103), deadline=2)
        self.assertFalse(samples.completed.any())
        assert_allclose(samples.times, 2)

    def test_equal_rates_require_deadline(self):
        with self.assertRaises(ValueError):
            nras.sample_stopped(1, 1, 1, 100, np.random.default_rng(1))
        sample = nras.sample_stopped(1, 1, 1, 100, np.random.default_rng(1), deadline=3)
        self.assertTrue((sample.times <= 3).all())

    def test_guard_raises_instead_of_discarding(self):
        finished = nras.sample_stopped(.1, 1, 3, 1, np.random.default_rng(1), max_events=1)
        self.assertTrue(finished.completed.all())
        with self.assertRaises(RuntimeError):
            nras.sample_stopped(100, 1, 3, 100, np.random.default_rng(1), max_events=1)


if __name__ == '__main__':
    unittest.main()
