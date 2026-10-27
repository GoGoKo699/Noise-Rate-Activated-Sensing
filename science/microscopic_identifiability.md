# Identifiability on a fixed microscopic frequency band

[Collision construction](microscopic_sensing.md) · [Local precision](microscopic_precision.md) · [Global precision](microscopic_global_precision.md) · [Statistical model](model.md)

One fixed-coupling collision already supplies a frequency-sensitive likelihood independent of the unknown transverse direction. On an explicit fixed-width frequency band, repeating this experiment gives a uniformly consistent estimator with a paid calibration cost. This is a finite-strength, off-compensation statement. It does not infer a global risk law from the local information coefficients.

## Hardware and the frequency promise

Fix the coupling $`g>0`$, cell duration $`h>0`$, nominal compensation $`\omega_0`$, and shared unknown angle $`\phi`$. Write

```math
\epsilon=\omega-\omega_0,
\qquad \chi=gh\in(0,\pi/4),
\qquad
H=\frac\epsilon2Z_S+gN_\phi\otimes X_E.
```

Choose a number $`r_*`$ with $`\chi<r_*<\pi/4`$, and define

```math
E=\frac2h\sqrt{r_*^2-\chi^2},
\qquad
\Omega=[\omega_0-E,\omega_0+E],
\qquad
\kappa=h\cos(2r_*)>0.
```

An explicit default is $`r_*=(\chi+\pi/4)/2`$. This gives a sufficient band, not a claim that the band is maximal. The interval, coupling, cell duration and compensation are fixed independently of the available number of cells. The promise $`\omega\in\Omega`$ does not shrink as resources increase, and no probability distribution on that interval or on $`\phi`$ is assumed. The full interaction obeys $`\|H\|=\sqrt{g^2+\epsilon^2/4}\le r_*/h`$ throughout the band; an imposed hardware strength budget must cover this bound.

Every bath qubit starts in $`|0\rangle`$ at time zero, interacts during its assigned cell and is retained afterward without reuse. The sensor has a protected ancillary qubit. There is no bath access or control inside a cell, and the compensation is not retuned during the experiment.

## An exact three-outcome experiment

Prepare the even-parity logical state

```math
|+_L\rangle=\frac{|00\rangle+|11\rangle}{\sqrt2}.
```

After one complete cell, measure parity. On an even result measure $`Y_L`$ and record its value $`W\in\{-1,+1\}`$; on an odd result record $`W=0`$. Here $`W`$ denotes the classical score, not the sensor Pauli operator $`Z_S`$. The odd outcome remains in the likelihood and consumes the same cell duration.

Put $`R=\sqrt{g^2+\epsilon^2/4}`$ and $`r=Rh`$. The [exact collision instrument](microscopic_sensing.md#exact-parity-conditioned-cell-channel) has Kraus operators

```math
K_0=\cos r\,I-i\frac{\epsilon}{2R}\sin r\,Z_S,
\qquad
K_1=-i\frac gR\sin r\,N_\phi.
```

Writing $`a=\cos r`$ and $`b=\epsilon\sin r/(2R)`$, the three probabilities are

```math
p(\epsilon)=\Pr\{W=0\}=\frac{g^2}{R^2}\sin^2 r,
\qquad q(\epsilon)=1-p(\epsilon),
```

```math
\Pr\{W=\pm1\}
=\frac12(a\pm b)^2
=\frac{q(\epsilon)\pm f(\epsilon)}2,
\qquad
f(\epsilon)=\mathbb E W
=\frac{\epsilon\sin(2Rh)}{2R}.
```

All three probabilities are independent of $`\phi`$ for every residual frequency. The even Kraus branch contains no angle, and the odd branch is used only through its probability. Thus the experiment eliminates the nuisance without estimating it or conditioning away an outcome.

On the promised band, $`\chi\le r\le r_*<\pi/4`$. All three probabilities are strictly positive: $`p>0`$ and $`|b|<\sin r<a`$. In particular, this likelihood has no zero-probability singularity on the band.

## A uniform inverse for the signal

Direct differentiation gives

```math
f'(\epsilon)
=h\left[
\frac{g^2}{R^2}\frac{\sin(2r)}{2r}
+\frac{\epsilon^2}{4R^2}\cos(2r)
\right].
```

The two weights in brackets are nonnegative and sum to one. For $`0<x<\pi/2`$, the inequality $`\sin x/x\ge\cos x`$ follows because $`\sin x-x\cos x`$ vanishes at zero and has derivative $`x\sin x\ge0`$. Both functions being averaged are therefore at least $`\cos(2r_*)`$ and at most one. Consequently

```math
\kappa\le f'(\epsilon)\le h
\qquad (|\epsilon|\le E).
```

The odd function $`f`$ is strictly increasing on $`[-E,E]`$, with

```math
\kappa|\epsilon_1-\epsilon_2|
\le |f(\epsilon_1)-f(\epsilon_2)|
\le h|\epsilon_1-\epsilon_2|.
```

Thus this single quadrature identifies frequency throughout the promised band, uniformly in the unknown angle. No second quadrature is required for this sufficient-band result.

## Repetition, risk and confidence

Repeat the same preparation and readout for $`N\ge1`$ cells. Fresh bath partners and a complete sensor–ancilla re-preparation make the scores $`W_1,\ldots,W_N`$ independent with the likelihood above. Let $`\overline W=N^{-1}\sum_jW_j`$, project it onto $`[f(-E),f(E)]`$, and define

```math
\widehat\epsilon_N
=f^{-1}\!\left(\mathrm{clip}_{[f(-E),f(E)]}(\overline W)\right).
```

The physical-frequency estimate is $`\widehat\omega=\omega_0+\widehat\epsilon_N`$. Projection onto the interval cannot increase the distance to $`f(\epsilon)`$. The inverse bound therefore implies

```math
|\widehat\omega-\omega|
\le\frac{|\overline W-f(\epsilon)|}{\kappa}.
```

Since $`W\in[-1,1]`$, its variance is $`q-f^2\le1`$. Hence the exact uniform mean-square-error guarantee is

```math
\sup_{\omega\in\Omega,\,\phi}
\mathbb E(\widehat\omega-\omega)^2
\le\frac1{N\kappa^2}
=\frac1{Nh^2\cos^2(2r_*)}.
```

The standard [Hoeffding bounded-variable concentration inequality](../references/RELATED_WORK.md#phase-estimation-and-stopping-background) gives, for every $`\delta>0`$,

```math
\sup_{\omega\in\Omega,\,\phi}
\Pr\{|\widehat\omega-\omega|\ge\delta\}
\le2\exp\!\left(-\frac{N\kappa^2\delta^2}{2}\right).
```

For a confidence error $`0<\eta<1`$, it is therefore sufficient to use

```math
N=\left\lceil
\frac{2\log(2/\eta)}{\kappa^2\delta^2}
\right\rceil
```

cells. The mean and concentration arguments are standard statistical ingredients; the exact likelihood, monotonicity band and contact accounting specify their application to this microscopic device.

## Every calibration cell and readout is charged

For a stand-alone $`N`$-cell experiment, prepare at time zero, combine each intermediate readout and next Bell preparation into one boundary instrument, and use the free terminal readout at $`T=Nh`$. This costs exactly $`N-1`$ system contacts, none inside a collision, and $`N`$ preinitialized bath cells. Every outcome contributes to the estimator.

If these $`N`$ cells form a calibration prefix of a longer $`n`$-cell run with $`N<n`$, the readout at $`Nh<T`$ is a counted nonterminal boundary contact. The prefix uses $`N`$ counted boundary instruments, including that last readout and preparation for the continuation. Under a total budget $`n-1`$, only $`n-1-N`$ contacts remain. The prefix costs physical time $`Nh`$ regardless of its outcome; its stated confidence error cannot be omitted from any subsequent risk analysis.

The estimate is classical information about frequency. Producing it does not change the residual Hamiltonian or supply permission to retune the fixed compensation. Any later protocol must use the remaining time and contacts in its stated access model.

## Scope

This establishes an exact identifiable experiment, a uniform attainable $`O(N^{-1})`$ risk bound on a fixed band, and a paid localization guarantee. The separate [microscopic global theorem](microscopic_global_precision.md) supplies a matching fixed-coupling lower order and uses this calibration resource in the two-coupling global estimator. The companion [global contact theorem](https://github.com/GoGoKo699/Markovian-Resolution-Limit/blob/main/science/global_contact_precision.md) uses it for an echoed/untouched temporal menu. Those results require their own uniform converses and recorded-phase constructions; they do not follow from this one-cell estimator alone.

The bandwidth restriction is substantive. The companion [frequency-alias obstruction](https://github.com/GoGoKo699/Markovian-Resolution-Limit/blob/main/science/sensing_bridge.md#frequency-aliases-of-the-collision-clock) gives frequencies whose complete boundary-controlled experiments are identical. No unrestricted-band conclusion follows from the monotone-band calculation here.
