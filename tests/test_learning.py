"""Finite checks of the worked tutorial; not an assessment of reader mastery."""
import math
import unittest

import numpy as np
from numpy.testing import assert_allclose
from scipy.linalg import expm
from scipy.stats import poisson

I = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.diag([1, -1]).astype(complex)


def rotation(phase):
    return np.diag(np.exp(-.5j * phase * np.array([1., -1.])))


class LearningExampleTests(unittest.TestCase):
    def test_ramsey_born_rule_and_information(self):
        plus = np.ones(2, dtype=complex) / math.sqrt(2)
        time, omega, angle, step = 2.3, .41, .173, 1e-6
        observable = math.cos(angle)*X + math.sin(angle)*Y
        def probabilities(value):
            state = rotation(value*time) @ plus
            return np.array([np.vdot(state, (I + sign*observable) @ state).real/2
                             for sign in (1, -1)])
        p = probabilities(omega)
        expected = np.array([1+math.cos(omega*time-angle),
                             1-math.cos(omega*time-angle)])/2
        assert_allclose(p, expected, atol=1e-14)
        derivative = (probabilities(omega+step)-probabilities(omega-step))/(2*step)
        self.assertAlmostEqual(float(np.sum(derivative**2/p)), time*time, places=8)

    def test_parity_record_preserves_logical_amplitudes(self):
        code = np.eye(4, dtype=complex)[:, [0, 3]]
        parity = np.kron(Z, Z)
        logical = np.array([math.sqrt(.3), 1j*math.sqrt(.7)])
        phi = .63
        encoded = code @ logical
        n = math.cos(phi)*X+math.sin(phi)*Y
        errored = np.kron(n, I) @ encoded
        expected = np.array([0, logical[1]*np.exp(-1j*phi),
                             logical[0]*np.exp(1j*phi), 0])
        assert_allclose(errored, expected, atol=1e-14)
        assert_allclose(parity @ encoded, encoded, atol=1e-14)
        assert_allclose(parity @ errored, -errored, atol=1e-14)
        assert_allclose(np.kron(X, I) @ errored,
                        code @ rotation(-2*phi) @ logical, atol=1e-14)

    def test_fixed_rate_nuisance_projection(self):
        gamma, time = 1., 10.
        n = np.arange(100)
        weights = poisson.pmf(n, gamma*time)
        vectors = np.array([np.full(n.size, time), -2*n])
        fisher = (vectors*weights) @ vectors.T
        assert_allclose(fisher, [[100, -200], [-200, 440]], atol=1e-10)
        efficient = fisher[0, 0]-fisher[0, 1]**2/fisher[1, 1]
        self.assertAlmostEqual(efficient, 100/11, places=10)

    def test_rate_diversity_example_and_repetitions(self):
        time = 10.
        n = np.arange(150)
        weights = .75*poisson.pmf(n, time)+.25*poisson.pmf(n, 3*time)
        self.assertAlmostEqual(float(weights.sum()), 1., places=13)
        self.assertAlmostEqual(float(weights @ n), 15., places=12)
        self.assertAlmostEqual(float(weights @ (n*n)), 315., places=10)
        vectors = np.array([np.full(n.size, time), -2*n])
        fisher = (vectors*weights) @ vectors.T
        assert_allclose(fisher, [[100, -300], [-300, 1260]], atol=1e-10)
        efficient = lambda j: j[0, 0]-j[0, 1]**2/j[1, 1]
        self.assertAlmostEqual(efficient(fisher), 200/7, places=10)
        self.assertAlmostEqual(efficient(3*fisher), 600/7, places=10)
        self.assertEqual(3*time, 30.)
        fair = .25*(3-1)**2/(.5*(1+9))
        self.assertAlmostEqual(fair, .2, places=14)
        self.assertAlmostEqual(fair/.25, .8, places=14)

    def test_balanced_echo_example(self):
        a, b, t_a, t_b = 1., 3., 7.5, 2.5
        d, mu, var = t_a-t_b, a*t_a-b*t_b, a*t_a+b*t_b
        self.assertEqual((d, mu, var), (5., 0., 15.))
        fisher = np.array([[d*d, -2*d*mu], [-2*d*mu, 4*(var+mu*mu)]])
        assert_allclose(fisher, np.diag([25., 60.]), atol=1e-14)

    def test_two_error_path_and_stopped_moments(self):
        omega = .7
        for phi in [-1.2, 0., .83]:
            n = math.cos(phi)*X+math.sin(phi)*Y
            actual = rotation(.85*omega) @ n @ rotation(.25*omega) @ n @ rotation(.9*omega)
            assert_allclose(actual, rotation(1.5*omega), atol=1e-14)
        self.assertAlmostEqual(.9+.25+.85, 2.)
        a, b, d = 1., 3., 4.
        self.assertEqual(d*(b+a)/(b-a), 8.)
        self.assertEqual(8*a*b*d/(b-a)**3, 12.)

    def test_generator_to_contrast_normalization(self):
        # Checks our convention, not a machine verification of the source PDF.
        kappa, time = .07, 2.1
        generator = kappa*(np.kron(Z.conj(), Z)-np.eye(4))
        rho0 = np.ones((2, 2), dtype=complex)/2
        actual = (expm(time*generator) @ rho0.reshape(4, order='F')).reshape((2, 2), order='F')
        self.assertAlmostEqual(actual[0, 1].real, .5*math.exp(-2*kappa*time), places=13)
        self.assertNotAlmostEqual(actual[0, 1].real, .5*math.exp(-kappa*time), places=4)


if __name__ == '__main__':
    unittest.main()
