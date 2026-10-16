# Residual parallel dephasing: asymptotics and finite advantage

[Physical scope](PHYSICAL_SCOPE.md) · [Preset protocols](PRESET_PROTOCOLS.md) · [Local theorems](THEOREMS.md)

The ideal scaling theorem is not a fault-tolerance claim. This controlled variation makes one important imperfection quantitative: add the independent, unobserved Lindblad operator

```math
L_z=\sqrt\kappa\,Z,\qquad\kappa>0,
```

while keeping the original shared transverse direction, ideal syndrome detection, noiseless ancilla, and bounded rate access. Its convention is $`\kappa(Z\rho Z-\rho)`$, so off-diagonal coherence decays as $`e^{-2\kappa T}`$. Here $`\kappa`$ is known. Parity detects the transverse errors but does not resolve these parallel errors.

## Every fixed positive parallel rate restores a linear ceiling

The established Lindblad-span obstruction applies because the signal generator is in the span of $`I,L_z`$. To obtain its constant directly from the [inherited channel bound](THEOREMS.md#the-inherited-channel-bound), vary $`\omega`$ with all nuisance parameters fixed and choose the gauge entry connecting the identity to $`L_z`$ as

```math
h_{0z}=h_{z0}=-\frac1{4\sqrt\kappa},
```

with all other entries zero. The operators in that bound are

```math
A=\frac{I}{16\kappa},
\qquad B=\frac Z2+2h_{0z}\sqrt\kappa Z=0.
```

This choice works for every classically selected transverse rate. Therefore

```math
\boxed{\mathcal I_\omega^*(T)\le\frac{T}{4\kappa}.}
```

The bound applies even when the transverse direction is known. Its mechanism and general bounding method are standard error-corrected metrology, not a new impossibility principle. It makes the scope precise: a fixed uncorrectable parallel rate removes the strict $`T\to\infty`$ quadratic law. No claim of arbitrary-noise protection is appropriate.

## Exact performance of the prescribed preset readout

For a fixed-duration preset interrogation, parallel dephasing commutes, as a channel, with the signal, the transverse-error conjugations, and the fixed recovery $`X`$. It therefore factors out as deterministic contrast

```math
\eta=e^{-2\kappa T}.
```

Conditioned on the retained rate and error count, the two readout probabilities at a recorded uniform equatorial angle $`\chi`$ become

```math
p_\pm=\frac{1\pm\eta\cos(\Theta-\chi)}2.
```

The conditional phase information is $`\eta^2\sin^2(\Theta-\chi)/(1-\eta^2\cos^2(\Theta-\chi))`$. Its average over $`\chi`$ is

```math
w(\eta)=1-\sqrt{1-\eta^2}.
```

For example, write the integrand as $`1-(1-\eta^2)/(1-\eta^2\cos^2\chi)`$ and use the elementary integral of the second denominator. At $`\eta=1`$, the pure-state null set of readout angles is handled by the continuous extension.

Every entry in the $`(\omega,\phi)`$ Fisher block is multiplied by the same $`w`$. Its Schur complement is therefore multiplied by $`w`$ as well. For the [recorded random-rate protocol](PRESET_PROTOCOLS.md#a-recorded-random-choice-of-one-rate),

```math
\boxed{\mathcal I_p^{(\kappa)}(T)
=\left(1-\sqrt{1-e^{-4\kappa T}}\right)\mathcal I_p^{(0)}(T).}
```

This is the exact local information of the specified readout, not the optimum over all mixed-state measurements. The same multiplicative law applies to the fixed-duration echo. It is not the stopped-channel formula: stopping has a random physical duration, which would have to be retained separately.

## A certified finite-time advantage with nonzero dephasing

Take $`b=3a`$, choose the lower rate with probability $`p=3/4`$, and set $`T=10/a`$. The ideal preset information is $`\mathcal I_p^{(0)}=200/(7a^2)`$. The universal upper bound for every strategy confined to rate $`a`$, **even without the additional parallel dephasing**, is $`T/a=10/a^2`$.

The imperfect two-rate protocol beats this stronger fixed-rate benchmark whenever

```math
1-\sqrt{1-e^{-40\kappa/a}}>\frac7{20},
```

or equivalently

```math
\boxed{\frac\kappa a<\frac1{40}\log\frac{400}{231}
\simeq0.01372617.}
```

For $`\kappa/a=0.01`$, its exact information is approximately $`12.16635/a^2`$, versus the ideal fixed-rate upper bound $`10/a^2`$. This is a finite local-information comparison with every interrogation charged. It is not a global mean-square-error ratio, an optimized onset threshold, or a hardware tolerance claim incorporating readout and feedback faults.

The two statements coexist: finite advantage persists in a nonzero imperfection window, while every fixed positive parallel rate eventually forbids quadratic asymptotic scaling. Long interrogation times alone are not the correct operating strategy outside the ideal model.

## Verification and attribution

`src/risk.py` evaluates the exact formulas with stable handling of very small contrast. `tests/test_risk.py` compares the angular integral with quadrature, the mixed-state likelihood with finite differences, the channel factorization with superoperator matrices, and the gauge and finite-advantage thresholds with direct calculations. The general obstruction is attributed to the channel-bound and known-noise foundations in [related work](../literature/RELATED_WORK.md).
