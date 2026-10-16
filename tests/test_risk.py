"""Finite checks of the global-bound ingredients and dephasing example."""
from pathlib import Path
import math
import sys
import unittest

import numpy as np
from numpy.testing import assert_allclose
from scipy.integrate import quad, solve_ivp
from scipy.linalg import expm
from scipy.stats import binom
import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import risk


class GlobalRiskTests(unittest.TestCase):
    def test_cosine_prior_normalization(self):
        for h in [.1, 1., 3.]:
            integral = quad(lambda u: math.cos(math.pi*u/(2*h))**2/h, -h, h)[0]
            self.assertAlmostEqual(integral, 1, places=12)

    def test_prior_information_by_integration(self):
        for h in [.2, 2.]:
            # The density times squared score is regular at both endpoints.
            value = quad(lambda u: math.pi**2/h**3 * math.sin(math.pi*u/(2*h))**2, -h, h)[0]
            self.assertAlmostEqual(value, risk.prior_information(h), places=10)

    def test_integration_by_parts_identity(self):
        h = .8
        def integrand(u):
            derivative = -math.pi / h**2 * math.sin(math.pi*u/h) / 2
            return (-u) * derivative
        self.assertAlmostEqual(quad(integrand, -h, h)[0], 1, places=12)

    def test_qfi_envelope_is_a_supersolution(self):
        t, v, c = sp.symbols('t v c', positive=True)
        f = (v*t+sp.sqrt(c*t))**2
        excess = sp.diff(f,t) - c - 2*v*(v*t+sp.sqrt(c*t))
        self.assertEqual(sp.simplify(excess-v*sp.sqrt(c*t)), 0)

    def test_envelope_against_ode_integration(self):
        for a,b in [(1,3), (.7, .8), (.1,5)]:
            v, c = (b-a)/(b+a), 4*b/(a+b)**2
            times = np.geomspace(1e-4, 100, 70)
            solution = solve_ivp(lambda t,y: [c+2*v*math.sqrt(max(0,y[0]))],
                                 (0,100), [0.], t_eval=times, rtol=1e-10, atol=1e-12)
            self.assertTrue(solution.success)
            envelopes = np.array([risk.controlled_qfi_envelope(a,b,t) for t in times])
            self.assertTrue(np.all(solution.y[0] <= envelopes+1e-9))

    def test_global_lower_asymptotic_constants(self):
        time = 1e12
        self.assertAlmostEqual(time*risk.fixed_rate_risk_lower(2,time,1), 2, places=8)
        result = time**2*risk.controlled_risk_lower(1,3,time,1)
        self.assertAlmostEqual(result, 4, places=4)

    def test_binomial_inverse_moment_bound(self):
        for m,p in [(1,.2), (5,.4), (50,.8)]:
            k = np.arange(m+1)
            probs = binom.pmf(k,m,p)
            identity = (1-(1-p)**(m+1))/((m+1)*p)
            self.assertAlmostEqual(np.dot(probs,1/(k+1)),identity,places=12)
            reciprocal = np.dot(probs[1:],1/k[1:])
            self.assertLessEqual(reciprocal,2*identity)

    def test_fixed_rate_upper_has_inverse_time_scaling(self):
        for time in [1e6,2e6]:
            upper = risk.fixed_rate_risk_upper(1,time,1)
            self.assertAlmostEqual(time*upper,4*math.e,places=4)
            self.assertGreaterEqual(upper, risk.fixed_rate_risk_lower(1,time,.4))

    def test_nojump_estimator_risk_check(self):
        rng = np.random.default_rng(3011)
        rate, tau, width, m, samples = 1., 1., 1., 1000, 3000
        p = math.exp(-rate*tau)
        for omega in [-.5,-.17,0,.31,.5]:
            counts = rng.binomial(m,p,size=samples)
            positive = rng.binomial(counts,(1+math.sin(omega*tau))/2)
            mean = np.divide(2*positive-counts,counts,out=np.zeros(samples),where=counts>0)
            estimate = np.arcsin(np.clip(mean,-math.sin(width*tau/2),math.sin(width*tau/2)))/tau
            mse = float(np.mean((estimate-omega)**2))
            self.assertLess(mse,risk.fixed_rate_risk_upper(rate,m*tau,width))


class ResidualDephasingTests(unittest.TestCase):
    def test_random_angle_integral(self):
        for kappa in [0,1e-4,.03,.5,5.]:
            eta2 = math.exp(-4*kappa)
            def information(angle):
                if kappa == 0:
                    return 1.0  # Continuous extension at a null set of pure-state readout angles.
                denominator = 1-eta2*math.cos(angle)**2
                return eta2*math.sin(angle)**2/denominator
            actual = quad(information,0,2*math.pi,epsabs=1e-10,limit=200)[0]/(2*math.pi)
            self.assertAlmostEqual(actual,risk.random_angle_weight(kappa,1),places=9)

    def test_dephasing_channel_commutes_with_recovery_and_transverse_noise(self):
        x = np.array([[0,1],[1,0]],complex)
        y = np.array([[0,-1j],[1j,0]],complex)
        z = np.diag([1,-1]).astype(complex)
        identity = np.eye(4)
        n = math.cos(.71)*x+math.sin(.71)*y
        dz = np.kron(z.conj(),z)-identity
        dn = np.kron(n.conj(),n)-identity
        recovery = np.kron(x.conj(),x)
        assert_allclose(dz@dn,dn@dz,atol=1e-13)
        assert_allclose(dz@recovery,recovery@dz,atol=1e-13)
        initial = np.array([[.5,.5],[.5,.5]],complex)
        actual = (expm(.03*4*dz)@initial.reshape(4,order='F')).reshape((2,2),order='F')
        self.assertAlmostEqual(actual[0,1].real,.5*math.exp(-2*.03*4),places=12)

    def test_dephasing_gauge_cancels_signal(self):
        for kappa in [.001,.1,4.]:
            z = np.diag([1.,-1.])
            vector_entry = -1/(4*math.sqrt(kappa))
            b_op = z/2+2*vector_entry*math.sqrt(kappa)*z
            assert_allclose(b_op,0,atol=1e-14)
            self.assertAlmostEqual(4*vector_entry**2,1/(4*kappa),places=10)

    def test_full_mixed_state_likelihood_fisher(self):
        # Finite differences of actual readout probabilities, averaged over chi.
        time, kappa, d, n, omega, phi = 2., .05, 2., 3, .4, .27
        angles = (np.arange(4096)+.37)*2*math.pi/4096
        eta = math.exp(-2*kappa*time)
        def probability(point):
            phase = point[0]*d-2*point[1]*n-angles
            return np.concatenate(((1+eta*np.cos(phase))/2,(1-eta*np.cos(phase))/2))/len(angles)
        point = np.array([omega,phi]); eps = 1e-6
        gradients = []
        for i in range(2):
            offset = np.eye(2)[i]*eps
            gradients.append((probability(point+offset)-probability(point-offset))/(2*eps))
        gradient = np.array(gradients)
        fisher = (gradient/probability(point))@gradient.T
        vector = np.array([d,-2*n])
        expected = risk.random_angle_weight(kappa,time)*np.outer(vector,vector)
        assert_allclose(fisher,expected,rtol=1e-7,atol=1e-8)

    def test_nonzero_dephasing_finite_advantage(self):
        ideal_fixed_upper = 10.
        actual = risk.dephased_mixture_information(1,3,.75,10,.01)
        self.assertGreater(actual,ideal_fixed_upper)
        self.assertLess(actual,risk.dephasing_all_strategy_upper(.01,10))

    def test_exact_tolerance_boundary(self):
        critical = risk.threefold_dephasing_tolerance()
        for factor in [.999,1.,1.001]:
            value = risk.dephased_mixture_information(1,3,.75,10,critical*factor)
            if factor == 1:
                self.assertAlmostEqual(value,10,places=12)
            else:
                self.assertEqual(value>10,factor<1)

    def test_zero_noise_limit_and_long_time_decay(self):
        self.assertEqual(risk.random_angle_weight(0,10),1)
        self.assertGreater(risk.random_angle_weight(5,10),0)
        self.assertAlmostEqual(risk.random_angle_weight(5,10)/(.5*math.exp(-200)),1,places=12)

    def test_input_domains(self):
        for arguments in [(0,3,1),(1,1,1),(2,1,1),(1,3,-1)]:
            with self.assertRaises(ValueError):
                risk.controlled_qfi_envelope(*arguments)
        for kappa in [-1,math.inf,math.nan]:
            with self.assertRaises(ValueError):
                risk.random_angle_weight(kappa,1)
        with self.assertRaises(ValueError):
            risk.prior_information(0)
        with self.assertRaises(ValueError):
            risk.dephased_mixture_information(1,3,1.1,10,.01)


class ResourceAndEvidenceTests(unittest.TestCase):
    def test_known_pulse_transforms_signal_and_unknown_axis_together(self):
        x = np.array([[0,1],[1,0]],complex)
        y = np.array([[0,-1j],[1j,0]],complex)
        z = np.diag([1.,-1.])
        phi, gamma = .71, 1.3
        n = math.cos(phi)*x+math.sin(phi)*y
        derivative = -math.sin(phi)*x+math.cos(phi)*y
        assert_allclose(x@n@x, math.cos(phi)*x-math.sin(phi)*y, atol=1e-14)
        assert_allclose(x@z@x, -z, atol=1e-14)
        jump = math.sqrt(gamma)*x@n@x
        djump = x@derivative@x/(2*math.sqrt(gamma))
        b_op = -z/2-.5j*(djump.conj().T@jump-jump.conj().T@djump)
        assert_allclose(b_op,0,atol=1e-14)

    def test_independent_unknown_offsets_make_target_unidentifiable(self):
        strengths = np.array([1., -.7, 2.3])
        offsets = np.array([.2, .9, -.5])
        omega, shift = .3, 1.4
        original = strengths*omega+offsets
        reparametrized = strengths*(omega+shift)+(offsets-strengths*shift)
        assert_allclose(original,reparametrized,atol=1e-14)

    def test_deterministic_evidence_record(self):
        import importlib.util
        import json
        root = Path(__file__).resolve().parents[1]
        spec = importlib.util.spec_from_file_location('reproduce_evidence',root/'scripts/reproduce_evidence.py')
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        expected = json.loads((root/'results/evidence.json').read_text())
        actual = module.evidence()
        def compare(a,b):
            if isinstance(a,dict):
                self.assertEqual(set(a),set(b))
                for key in a:
                    compare(a[key],b[key])
            elif isinstance(a,list):
                self.assertEqual(len(a),len(b))
                for x,y in zip(a,b):
                    compare(x,y)
            elif isinstance(a,float):
                self.assertAlmostEqual(a,b,delta=1e-11*max(1,abs(a)))
            else:
                self.assertEqual(a,b)
        compare(actual,expected)


if __name__ == '__main__':
    unittest.main()
