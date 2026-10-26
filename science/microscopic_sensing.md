# Finite-strength collisions and local sensing

[Physical scope](physical_scope.md) · [Statistical model](model.md) · [Local precision](precision_bounds.md)

A bounded collision implementation can retain quadratic **local** information with a fixed, nonzero parity-check interval. This construction supplies one microscopic realization of the rate-diverse sensing mechanism. It does not transfer the Markovian fixed-rate converse to microscopic dynamics, or establish an advantage over every strategy using the same microscopic hardware.

The companion [controlled-record comparison](https://github.com/GoGoKo699/Markovian-Resolution-Limit/blob/main/science/sensing_bridge.md) studies when the complete sensing record can agree with a Markovian prediction. Agreement at one operating point, parameter-uniform distributional approximation, and agreement of parameter derivatives are separate statements.

## One shared interaction and a fixed measurement clock

Fix $`0<a<b`$, a parity-check interval $`\Delta>0`$, and a nominal frequency $`\omega_0`$. Compensate that fixed nominal frequency and write $`\epsilon=\omega-\omega_0`$. All control settings, including the compensation and the couplings below, are held fixed when differentiating $`\epsilon`$.

For each label $`\gamma\in\{a,b\}`$, define

```math
p_\gamma=\frac{1-e^{-2\gamma\Delta}}2,
\qquad q_\gamma=1-p_\gamma,
\qquad \chi_\gamma=\arcsin\sqrt{p_\gamma},
\qquad g_\gamma=\frac{\chi_\gamma}{\Delta}.
```

Thus $`0<\chi_a<\chi_b<\pi/4`$. The labels $`a,b`$ calibrate the parity-transition probabilities at the operating point; away from that point, this finite collision device is not asserted to obey the corresponding Lindblad equation.

During a cell of duration $`\Delta`$, the sensor interacts with one fresh environmental qubit through

```math
H_\gamma(\epsilon,\phi)
=\frac\epsilon2 Z_S\otimes I_E
+g_\gamma N_\phi\otimes X_E,
\qquad N_\phi=\cos\phi\,X_S+\sin\phi\,Y_S.
```

All environmental qubits begin in $`|0\rangle`$ at time zero. Spent cells are retained and never reused; no environmental state or output is accessible to the controller. Classical selection changes only the scalar coupling to the same unknown transverse operator. The signal term is unchanged by that selection. For a horizon $`T`$, $`\lfloor T/\Delta\rfloor`$ cells suffice, giving bath dimension $`2^{\lfloor T/\Delta\rfloor}`$. The bath is finite for every finite experiment; its required size grows with the experiment duration.

The sensor and one protected ancilla encode $`|0_L\rangle=|00\rangle`$, $`|1_L\rangle=|11\rangle`$. At each cell boundary measure their parity, retaining the outcome. Use label $`a`$ after an even result and label $`b`$ after an odd result. Apply no recovery pulse. Preparation, parity measurements, switching at cell boundaries, decoding, readout and ancillary storage have the same ideal-control status as in the [statistical model](model.md); finite measurement duration or control work is not priced here.

Since the two terms in the cell Hamiltonian anticommute, its full operator norm is

```math
\|H_\gamma(\epsilon,\phi)\|
=R_\gamma(\epsilon)
=\sqrt{g_\gamma^2+\epsilon^2/4}.
```

In particular, on $`|\epsilon|\le E`$ the whole device obeys the uniform interaction bound $`\sqrt{g_b^2+E^2/4}`$, independently of $`\phi`$. A prescribed strength budget must cover this bound. The quantities $`a,b,g_\gamma,\epsilon`$ have units of inverse time; $`\chi_\gamma`$ is dimensionless.

## Exact parity-conditioned cell channel

The same anticommutation gives

```math
U_\gamma
=\cos(R_\gamma\Delta)I
-i\frac{\sin(R_\gamma\Delta)}{R_\gamma}
\left(\frac\epsilon2 Z_S\otimes I_E
+g_\gamma N_\phi\otimes X_E\right).
```

With the bath input $`|0\rangle`$, the two Kraus operators are

```math
K_{0,\gamma}
=\cos(R_\gamma\Delta)I
-i\frac{\epsilon}{2R_\gamma}\sin(R_\gamma\Delta)Z_S,
\qquad
K_{1,\gamma}
=-i\frac{g_\gamma}{R_\gamma}\sin(R_\gamma\Delta)N_\phi.
```

The first preserves sensor–ancilla parity; the second flips it. A parity measurement therefore identifies these alternatives without measuring the bath or revealing the logical amplitudes. Their probabilities are state independent:

```math
p_\gamma(\epsilon)
=\frac{g_\gamma^2}{R_\gamma(\epsilon)^2}
\sin^2(R_\gamma(\epsilon)\Delta),
\qquad q_\gamma(\epsilon)=1-p_\gamma(\epsilon).
```

Both are independent of $`\phi`$ and even in $`\epsilon`$. At zero residual frequency they equal $`p_\gamma,q_\gamma`$ above, so the complete parity chain coincides with the finite-cadence Markovian chain at that point.

In a neighborhood of zero, write the normalized no-flip Kraus operator as

```math
K_{0,\gamma}/\sqrt{q_\gamma(\epsilon)}
=e^{-i\theta_\gamma(\epsilon)Z_S/2},
\qquad \theta_\gamma(0)=0.
```

The branch of the phase is continuous at zero; its derivative is

```math
d_\gamma=\theta_\gamma'(0)
=\frac{\tan\chi_\gamma}{g_\gamma}
=\Delta\frac{\tan\chi_\gamma}{\chi_\gamma}.
```

The normalized flip branch is $`N_\phi`$ up to a scalar phase and has no logical signal rotation. Its probability has zero first derivative at the operating point. Although the conditional no-flip phase derivative exceeds $`\Delta`$, it is not a free postselection gain:

```math
q_\gamma d_\gamma^2
=\Delta^2\frac{\sin^2\chi_\gamma}{\chi_\gamma^2}
\le\Delta^2.
```

## Cancellation and the accumulated local phase

Let $`\sigma_{k-1}\in\{+1,-1\}`$ be the parity immediately before cell $`k`$, starting with $`\sigma_0=+1`$. A no-flip result contributes a signal rotation; a flip contributes $`N_\phi`$. Moving each signal rotation past earlier flips uses $`N_\phi Z_SN_\phi=-Z_S`$.

For every record ending in even parity, the total number of flips is even. Consequently its normalized logical output is exactly

```math
U_{\mathcal R}(\epsilon)
=\exp[-i\Phi_{\mathcal R}(\epsilon)Z_L/2],
\qquad
\Phi_{\mathcal R}(\epsilon)
=\sum_k\sigma_{k-1}
\mathbf 1_{\{\sigma_k=\sigma_{k-1}\}}
\theta_{\gamma(\sigma_{k-1})}(\epsilon),
```

where $`\gamma(+1)=a`$ and $`\gamma(-1)=b`$. All dependence on the unknown direction cancels, for every such record and every residual frequency where the phase representation is used. This is an exact statement about the collision instrument, not an approximation by a jump trajectory.

The derivative of the accumulated phase at zero is the additive reward

```math
D_{\mathcal R}
=\Phi_{\mathcal R}'(0)
=\sum_k\sigma_{k-1}
\mathbf 1_{\{\sigma_k=\sigma_{k-1}\}}
 d_{\gamma(\sigma_{k-1})}.
```

The duration $`D_{\mathcal R}`$ is a local phase derivative. It is not a continuously measured signed residence time, and the collision protocol does not implement the Markovian exact stopped channel at a prescribed effective time.

## Positive drift at every fixed cadence

At $`\epsilon=0`$, the parity chain has transition matrix and stationary distribution

```math
P=\begin{pmatrix}q_a&p_a\\p_b&q_b\end{pmatrix},
\qquad
\pi_+=\frac{p_b}{p_a+p_b},
\qquad
\pi_-=\frac{p_a}{p_a+p_b}.
```

It is irreducible and aperiodic. The expected reward per cell in stationarity is

```math
\mu=\frac{p_bq_ad_a-p_aq_bd_b}{p_a+p_b},
\qquad
v_{\mathrm{col}}=\frac\mu\Delta.
```

For $`m`$ cells starting in the even sector, geometric mixing gives

```math
\mathbb E D_m=m\mu+O(1),
\qquad \mathrm{Var}(D_m)=O(m).
```

The constants depend on the fixed rates and cadence. To see the variance bound, the cell reward is bounded and depends only on adjacent states. Covariances of rewards separated by $`\ell`$ cells are bounded by a constant times $`|1-p_a-p_b|^{\ell-1}`$; summing this geometric bound gives linear variance. In particular the mean reward per cell converges to $`\mu`$ in mean square.

The drift is strictly positive. Indeed,

```math
v_{\mathrm{col}}
=\frac{p_ap_b}{\Delta(p_a+p_b)}
\left(\frac{q_ad_a}{p_a}-\frac{q_bd_b}{p_b}\right),
\qquad
\frac{q_\gamma d_\gamma}{p_\gamma}
=\Delta\frac{\cot\chi_\gamma}{\chi_\gamma}.
```

For $`0<\chi<\pi/4`$, $`\cot\chi/\chi`$ has derivative $`-(\chi\csc^2\chi+\cot\chi)/\chi^2<0`$. Since $`\chi_a<\chi_b`$, this proves $`v_{\mathrm{col}}>0`$.

## A hard deadline and an attainable local coefficient

Prepare $`|+_L\rangle`$ and let $`m=\lfloor T/\Delta\rfloor`$. For sufficiently large $`m`$, reserve

```math
k_m=\left\lceil\frac{3\log m}{-\log q_b}\right\rceil
```

cells for finishing. Run the policy for $`m-k_m`$ cells. If parity is even, decode into protected storage immediately. If it is odd, continue until the first even result, using at most the reserved cells. Keep any deadline failure as a flag with a parameter-independent fallback output.

At the operating point the failure probability is at most $`q_b^{k_m}\le m^{-3}`$. The extra or omitted reward associated with the finishing margin is $`O(\log m)`$ in absolute value, while excluding failed branches changes the mean prefix reward by at most $`O(m^{-2})`$. It follows that

```math
p_{\mathrm{s}}=1-O(m^{-3}),
\qquad
p_{\mathrm{s}}\,\mathbb E[D_{\mathcal R}\mid\mathrm{success}]
=m\mu+O(\log m).
```

All successful outputs are independent of $`\phi`$. Measure $`Y_L`$, retaining both the success flag and every parity record. For a lower bound on the available information, one may use just the marginal success flag and terminal readout. At $`\epsilon=0`$, successful outputs have equal readout probabilities, and their derivative magnitudes are $`\mathbb E[D_{\mathcal R}\mid\mathrm{success}]/2`$. All record and success probabilities have zero first derivative because they are even functions of $`\epsilon`$.

Thus the nuisance-adjusted information in this marginal readout is

```math
\mathcal I_\omega^{\mathrm{marginal}}(T)
=p_{\mathrm{s}}
\bigl(\mathbb E[D_{\mathcal R}\mid\mathrm{success}]\bigr)^2
=v_{\mathrm{col}}^2T^2+o(T^2).
```

The complete retained record has at least this much information. The equality states the coefficient of the specified marginal readout, not an optimal coefficient over all collision-device controls. No directional calibration is used. The local conclusion is evaluated at the fixed compensated operating point; it does not supply prior localization for free in a global estimation problem.

## What this connection establishes

At every fixed $`\Delta>0`$, both couplings are finite and this explicit microscopic experiment has a positive quadratic local-information coefficient. In the short-cadence limit,

```math
g_\gamma\sim\sqrt{\gamma/\Delta},
\qquad
v_{\mathrm{col}}\longrightarrow\frac{b-a}{b+a}.
```

The limit requires diverging microscopic strength; the finite-cadence conclusion does not. A bath and contact budget must also accompany a duration-dependent family of experiments.

Matching the parity chain at zero does not match its frequency derivatives. For example, the conditional no-flip mean signed time in the Markovian model is $`\tanh(\gamma\Delta)/\gamma`$, whereas the collision phase derivative is $`d_\gamma=\Delta\tan\chi_\gamma/\chi_\gamma`$. The former is below $`\Delta`$ and the latter above it. This is why the local coefficient above is derived directly from the microscopic instrument.

For comparison within this particular protocol family, keep one coupling $`g`$ fixed in both parity sectors, with $`0<g\Delta<\pi/4`$. The parity chain is then symmetric, its stationary reward has zero mean, and the same bounded-reward mixing calculation gives $`\mathbb E D_m^2=O(m)`$. Including the logarithmic return margin preserves this bound. The complete retained record and a terminal $`Y_L`$ readout have local information $`\mathbb E[\mathbf 1_{\mathrm{success}}D_{\mathcal R}^2]=O(T)`$, since every record probability has zero first derivative at compensation. This compares the specified no-recovery, boundary-parity experiment with and without coupling diversity; it is not a converse for arbitrary microscopic controls.

The [Markovian global-risk theorem](global_precision.md), its exact stopped-channel implementation, and its fixed-rate converse keep their stated Markovian scope. The construction here proves neither an optimized microscopic global-risk law nor a same-hardware fixed-rate separation. A bounded-loss risk comparison requires parameter-uniform control of the full experiment; a Fisher-information comparison additionally requires control of derivatives. A visible discrepancy in parity records alone proves neither loss nor improvement of metrological performance.

The companion [finite verification script](https://github.com/GoGoKo699/Markovian-Resolution-Limit/blob/main/verification/verify_sensing_bridge.py) checks the collision instrument and the cross-project formulas; the [verification guide](../verification/README.md) records the executable entrypoints and their scope. Finite checks supplement the derivations and do not establish the asymptotic statements by sampling.
