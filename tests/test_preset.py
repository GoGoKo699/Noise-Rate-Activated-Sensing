"""Direct likelihood and trajectory checks for preset protocols."""
from pathlib import Path
import math
import sys
import unittest

import numpy as np
from numpy.testing import assert_allclose
from scipy.optimize import minimize_scalar
from scipy.stats import poisson
import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import nras
import preset


def numerical_fisher(likelihood, point, step=1e-6):
    """Finite-difference an independently specified complete likelihood."""
    point = np.asarray(point, dtype=float)
    probs = likelihood(point)
    derivatives = []
    for i in range(len(point)):
        offset = np.zeros(len(point))
        offset[i] = step
        derivatives.append((likelihood(point + offset) - likelihood(point - offset)) / (2 * step))
    gradient = np.array(derivatives)
    keep = probs > 1e-28
    return (gradient[:, keep] / probs[keep]) @ gradient[:, keep].T


def echo_likelihood(t_a, t_b):
    # At the tested rates these cutoffs leave total Poisson tail below 1e-14.
    na, nb, chi, sign = np.meshgrid(np.arange(45), np.arange(45),
                                   [.173, 1.317, 2.531, 4.073], [-1, 1], indexing='ij')
    def likelihood(point):
        omega, phi, a, b = point
        phase = omega * (t_a - t_b) - 2 * phi * (na - nb) - chi
        weights = poisson.pmf(na, a * t_a) * poisson.pmf(nb, b * t_b) / 4
        return (weights * (1 + sign * np.cos(phase)) / 2).ravel()
    return likelihood


def mixture_likelihood(time, probabilities, signals=(1., 1.)):
    n, chi, sign = np.meshgrid(np.arange(65), [.173, 1.317, 2.531, 4.073], [-1, 1], indexing='ij')
    def likelihood(point):
        omega, phi, a, b = point
        output = []
        for weight, signal, rate in zip(probabilities, signals, (a, b)):
            phase = omega * signal * time - 2 * phi * n - chi
            counts = poisson.pmf(n, rate * time)
            output.append((weight * counts * (1 + sign * np.cos(phase)) / 8).ravel())
        return np.concatenate(output)
    return likelihood


class PresetEchoTests(unittest.TestCase):
    def test_direct_two_qubit_trajectories(self):
        rng = np.random.default_rng(2001)
        code = np.eye(4, dtype=complex)[:, [0, 3]]
        recovery = np.kron(nras.X, nras.I)
        logical_flip = np.kron(nras.X, nras.X)
        for _ in range(300):
            omega, phi = rng.normal(size=2)
            t_a, t_b = rng.uniform(.01, 3, size=2)
            counts = rng.integers(0, 25, size=2)
            jump = np.kron(nras.noise_operator(phi), nras.I)
            def block(time, count):
                intervals = np.diff(np.r_[0, np.sort(rng.uniform(0, time, size=count)), time])
                unitary = np.eye(4, dtype=complex)
                for k, dt in enumerate(intervals):
                    unitary = np.kron(nras.rotation(omega * dt), nras.I) @ unitary
                    if k < count:
                        unitary = recovery @ jump @ unitary
                return unitary
            u_a, u_b = block(t_a, counts[0]), block(t_b, counts[1])
            actual = logical_flip @ u_b @ logical_flip @ u_a @ code
            phase = omega * (t_a - t_b) - 2 * phi * (counts[0] - counts[1])
            assert_allclose(actual, code @ nras.rotation(phase), atol=5e-14)

    def test_full_likelihood_including_unknown_rates(self):
        point = [.41, .263, 1.1, 2.7]
        for t_a, t_b in [(1.2, .8), (2.7, 1.1)]:
            likelihood = echo_likelihood(t_a, t_b)
            self.assertAlmostEqual(likelihood(point).sum(), 1., places=13)
            result = numerical_fisher(likelihood, point)
            expected = preset.echo_fisher(*point[2:], t_a, t_b, unknown_rates=True)
            assert_allclose(result, expected, rtol=4e-6, atol=3e-7)

    def test_balanced_exact_information(self):
        for a, b, time in [(1., 3., .3), (.4, 2.1, 700), (1., 1., 9)]:
            t_a, t_b = time * b / (a + b), time * a / (a + b)
            assert_allclose(preset.echo_information(a, b, t_a, t_b),
                            ((b - a) / (a + b)) ** 2 * time ** 2, rtol=1e-13)

    def test_unknown_rate_scores_do_not_add_nuisance_penalty(self):
        fisher = preset.echo_fisher(1, 3, 2, 1, unknown_rates=True)
        inverse_information = np.linalg.inv(fisher)[0, 0]
        self.assertAlmostEqual(1 / inverse_information, preset.echo_information(1, 3, 2, 1))

    def test_fixed_imbalance_crossover(self):
        a, b, fraction = 1., 3., .76
        drift = a * fraction - b * (1 - fraction)
        activity = a * fraction + b * (1 - fraction)
        limiting_linear_coefficient = (2 * fraction - 1) ** 2 * activity / drift ** 2
        time = 1e9
        result = preset.echo_information(a, b, fraction*time, (1-fraction)*time)
        self.assertAlmostEqual(result / time / limiting_linear_coefficient, 1., places=5)

    def test_root_time_balancing_tolerance(self):
        a, b, c, time = 1., 3., .07, 1e12
        fraction = b / (a + b) + c / math.sqrt(time)
        activity0 = 2 * a * b / (a + b)
        expected = ((b-a)/(b+a))**2 / (1+(a+b)**2*c*c/activity0)
        actual = preset.echo_information(a, b, fraction*time, (1-fraction)*time) / time**2
        self.assertAlmostEqual(actual, expected, places=6)

    def test_common_rate_rescaling_preserves_balance(self):
        for scale in [.1, 1, 7]:
            self.assertAlmostEqual(preset.echo_information(scale, 3*scale, 75, 25), 2500)

    def test_differential_relative_error_law(self):
        a0, b0, time, ea, eb = 1., 3., 100., .02, -.01
        lam = a0*b0*time/(a0+b0)
        expected = ((b0-a0)/(b0+a0))**2*time**2 / (1+lam*(ea-eb)**2/(2+ea+eb))
        actual = preset.echo_information(a0*(1+ea), b0*(1+eb), .75*time, .25*time)
        self.assertAlmostEqual(actual, expected, places=9)

    def test_echo_finite_time_certificate(self):
        for time in [3., 4., 5., 19.]:
            self.assertEqual(preset.echo_information(1, 3, .75*time, .25*time) > time, time > 4)


class RandomizedRateTests(unittest.TestCase):
    def test_full_likelihood_and_unknown_rate_block(self):
        point = [.31, .227, 1.1, 2.7]
        for signals, p in [((1, 1), (.5, .5)), ((-.3, 1.4), (.7, .3))]:
            likelihood = mixture_likelihood(2., p, signals)
            self.assertAlmostEqual(likelihood(point).sum(), 1., places=13)
            actual = numerical_fisher(likelihood, point)
            expected = preset.mixture_fisher(signals, point[2:], p, 2, unknown_rates=True)
            assert_allclose(actual, expected, rtol=4e-6, atol=3e-7)
            self.assertAlmostEqual(1/np.linalg.inv(expected)[0,0],
                                   preset.mixture_information(signals, point[2:], p, 2), places=11)

    def test_closed_form_rate_mixture(self):
        for a, b, p, time in [(1,3,.5,100), (.2,4,.8,2), (2,2,.3,7)]:
            mean = p*a + (1-p)*b
            second = p*a*a + (1-p)*b*b
            variance = p*(1-p)*(a-b)**2
            expected = time**2*(variance+mean/time)/(second+mean/time)
            self.assertAlmostEqual(preset.mixture_information([1,1], [a,b], [p,1-p], time),
                                   expected, places=10)

    def test_one_setting_recovers_attributed_formula(self):
        for gamma, time in [(1,1), (2,3), (.1,10000)]:
            self.assertAlmostEqual(preset.mixture_information([1], [gamma], [1], time),
                                   time*time/(1+gamma*time), places=9)

    def test_optimal_probability_and_sensitivity_identity(self):
        a, b, p = sp.symbols('a b p', positive=True)
        contrast2 = (b-a)**2/(b+a)**2
        denominator = p*a*a+(1-p)*b*b
        coefficient = p*(1-p)*(b-a)**2/denominator
        self.assertEqual(sp.factor(contrast2-coefficient-
                         contrast2*((a+b)*p-b)**2/denominator), 0)
        for a, b in [(1,3), (.1,1), (2,9)]:
            optimum = minimize_scalar(lambda p: -preset.mixture_coefficient([1,1], [a,b], [p,1-p]),
                                      bounds=(0,1), method='bounded')
            self.assertAlmostEqual(optimum.x, b/(a+b), places=5)

    def test_fair_coin_retains_at_least_half_optimal_coefficient(self):
        for ratio in np.geomspace(1.001, 1e5, 100):
            coefficient = preset.mixture_coefficient([1,1], [1,ratio], [.5,.5])
            optimal = ((ratio-1)/(ratio+1))**2
            self.assertGreaterEqual(coefficient/optimal, .5)
            self.assertLessEqual(coefficient/optimal, 1.+1e-12)

    def test_general_pair_attains_minimax_coefficient(self):
        rng = np.random.default_rng(2002)
        for _ in range(300):
            size = int(rng.integers(2,9))
            s, g = rng.normal(size=size), rng.uniform(.2,5,size=size)
            speed, (i,j) = nras.control_speed(s,g)
            p = g[j]/(g[i]+g[j])
            actual = preset.mixture_coefficient(s[[i,j]], g[[i,j]], [p,1-p])
            self.assertAlmostEqual(actual, speed**2, places=11)

    def test_pool_fisher_before_eliminating_common_nuisance(self):
        time = 10000
        pooled = preset.mixture_information([1,1], [1,3], [.5,.5], time)
        separate = .5*time*time/(1+time) + .5*time*time/(1+3*time)
        self.assertGreater(pooled, 100*separate)
        # Independent directions remove the gain rather than sharing the nuisance block.
        full = np.array([[time*time, -time*time, -3*time*time],
                         [-time*time, 2*(time+time*time), 0],
                         [-3*time*time, 0, 2*(3*time+9*time*time)]])
        self.assertAlmostEqual(1/np.linalg.inv(full)[0,0]/separate, 1., places=10)

    def test_exact_finite_time_separation(self):
        for time in [2., 2.8, 3., 4., 10.]:
            result = preset.mixture_information([1,1],[1,3],[.75,.25],time)
            self.assertAlmostEqual(result, time**2*(time+2)/(4*time+2), places=12)
            self.assertEqual(result>time, time>1+math.sqrt(3))

    def test_probability_endpoints_and_proportional_settings(self):
        self.assertAlmostEqual(preset.mixture_coefficient([1,1],[1,3],[1,0]),0.,places=14)
        self.assertAlmostEqual(preset.mixture_coefficient([2,6],[1,3],[.4,.6]),0.,places=14)

    def test_input_domains(self):
        for args in [([1],[0],[1]), ([1],[1],[.9]), ([1,1],[1,3],[1.1,-.1]),
                     ([1],[1,2],[1]), ([math.nan],[1],[1])]:
            with self.assertRaises(ValueError):
                preset.mixture_coefficient(*args)
        with self.assertRaises(ValueError):
            preset.mixture_information([1],[1],[1],0)
        for args in [(1,3,-1,2), (1,3,0,0), (0,3,1,2)]:
            with self.assertRaises(ValueError):
                preset.echo_statistics(*args)


class ConverseCrossCheck(unittest.TestCase):
    def test_exact_cptp_steps_have_the_stated_continuous_coefficients(self):
        gamma, signal, slope, phi, omega = 1.7, 1.2, .23, .7, .4
        last_error = math.inf
        for dt in [1e-2,1e-3,1e-4,1e-5]:
            p = -math.expm1(-gamma*dt)
            n = nras.noise_operator(phi)
            nd = -math.sin(phi)*nras.X + math.cos(phi)*nras.Y
            r = nras.rotation(signal*omega*dt)
            rd = -.5j*signal*dt*nras.Z@r
            ks = [math.sqrt(1-p)*r, math.sqrt(p)*n@r]
            ds = [math.sqrt(1-p)*rd, math.sqrt(p)*(slope*nd@r+n@rd)]
            assert_allclose(sum(k.conj().T@k for k in ks), nras.I, atol=1e-14)
            alpha = sum(d.conj().T@d for d in ds)
            beta = -1j*sum(d.conj().T@k for d,k in zip(ds,ks))
            assert_allclose(alpha,(slope*slope*p-slope*signal*p*dt+signal**2*dt**2/4)*nras.I,atol=1e-14)
            assert_allclose(beta,(signal*dt/2-slope*p)*nras.Z,atol=1e-14)
            error = np.linalg.norm(alpha/dt-gamma*slope*slope*nras.I)
            error += np.linalg.norm(beta/dt-(signal/2-gamma*slope)*nras.Z)
            self.assertLess(error,last_error/5)
            last_error = error
        self.assertLess(last_error,1e-5)


if __name__ == '__main__':
    unittest.main()
