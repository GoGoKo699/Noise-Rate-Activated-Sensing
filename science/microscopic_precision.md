# Optimal local precision with a fixed collision clock

[Microscopic construction](microscopic_sensing.md) · [Statistical model](model.md) · [Markovian precision bounds](precision_bounds.md)

For the finite-strength collision device, one fixed positive coupling permits only linear nuisance-adjusted local information when controls occur at the prescribed cell boundaries. Selecting between two fixed positive couplings restores quadratic information within that same control class. Both leading coefficients can be determined exactly. The result is local at a compensated operating point and does not establish a microscopic global-risk law.

## The control class is part of the theorem

Use the [exact collision channel](microscopic_sensing.md#exact-parity-conditioned-cell-channel) with cell duration $`\Delta>0`$, a fresh inaccessible environmental qubit initially in $`|0\rangle`$ for every cell, residual frequency $`\epsilon=\omega-\omega_0`$, and one fixed continuously unknown transverse direction $`\phi`$. The compensation $`\omega_0`$ is fixed under differentiation. The couplings and cell duration are fixed independently of the total duration.

A protocol uses at most $`n`$ complete cells, with physical budget $`T=n\Delta`$. At their boundaries it may perform arbitrary parameter-independent operations and instruments on the sensor and protected ancillary memory, retain every outcome, reset or swap the sensor, and adapt later boundary operations to its record. Initial preparation and terminal readout are arbitrary. Independent repetitions consume their own cells. There is no bath access, operation or drive inside a cell beyond the fixed nominal compensation, change to a cell's duration, reset of the collision clock, noise-free signal-bearing waiting interval, or extra signal-bearing channel. Parameter-independent processing of protected memory alone can be absorbed into adjacent boundary instruments.

In the fixed-coupling class, every exposed cell in every pooled trial uses the same positive $`g`$. In the two-coupling class, a classical controller may choose $`g_a`$ or $`g_b`$ before each cell, without coherently controlling the coupling label. The calibrated pair from the microscopic construction satisfies $`0<g_a\Delta<g_b\Delta<\pi/4`$. The fixed-coupling benchmark may choose either member of this same pair but cannot lower its coupling as $`n`$ grows or turn the noise off.

Write $`\mathcal I_g^*(n\Delta)`$ and $`\mathcal I_{\{g_a,g_b\}}^*(n\Delta)`$ for the supremum of attainable nuisance-adjusted classical Fisher information in these classes, evaluated at $`\epsilon=0`$. The nuisance is the shared continuous angle, with the definition in the [statistical model](model.md#information-in-the-presence-of-a-nuisance). The conclusions hold at every $`\phi`$. Knowledge of a fixed nominal frequency for a local calculation does not provide global frequency localization for free.

## The optimal fixed-coupling coefficient

For $`0<\chi=g\Delta<\pi/4`$, put $`p=\sin^2\chi`$ and $`q=1-p`$. Then

```math
\frac{n^2p}{g^2(np+q)}
\le\mathcal I_g^*(n\Delta)
\le\min\left\{(n\Delta)^2,\frac n{g^2}\right\}.
```

Consequently,

```math
\lim_{n\to\infty}\frac{\mathcal I_g^*(n\Delta)}{n\Delta}
=\frac1{g^2\Delta}.
```

The upper bound permits arbitrary adaptive boundary controls, not merely the parity-measurement construction. It is derived for this exact microscopic channel; it is not imported from the Markovian fixed-rate theorem.

### A common nuisance path removes coherent accumulation

At the operating point, write $`c=\cos\chi`$, $`s=\sin\chi`$. The exact Kraus operators and their relevant derivatives are

```math
K_0=cI,\qquad K_1=-isN_\phi,
\qquad
\partial_\epsilon K_0=-i\frac{s}{2g}Z,
\qquad \partial_\epsilon K_1=0,
\qquad \partial_\phi K_1=-is\,\partial_\phi N_\phi.
```

Consider the one-parameter submodel $`\epsilon(u)=u`$, $`\phi(u)=\phi_0+ku`$, with every control held fixed. A dot denotes this parameter derivative. Since $`N_\phi\partial_\phi N_\phi=iZ`$,

```math
\sum_{r=0}^1K_r^\dagger\dot K_r
=i\left(pk-\frac{cs}{2g}\right)Z,
\qquad
\alpha=\sum_{r=0}^1\dot K_r^\dagger\dot K_r
=\left(\frac p{4g^2}+pk^2\right)I.
```

Choosing

```math
k=\frac{\cot\chi}{2g}
```

makes the first expression vanish and gives $`\alpha=I/(4g^2)`$.

The adaptive channel-extension argument can be proved directly. Dilate one cell to the isometry $`V=\sum_rK_r\otimes|r\rangle`$, and retain a purification $`|\Psi(u)\rangle`$ of all earlier outputs, records and inaccessible environments. Its derivative after the next cell is

```math
\frac d{du}(V|\Psi\rangle)
=V|\dot\Psi\rangle+\dot V|\Psi\rangle.
```

Here $`V^\dagger\dot V=0`$, so the cross term vanishes and the derivative's squared norm increases by exactly $`1/(4g^2)`$. Parameter-independent boundary instruments can be dilated without adding a derivative. Starting from a parameter-independent input, $`4\|\dot\Psi_n\|^2\le n/g^2`$. The actual output quantum Fisher information is at most this purification bound, and efficient target information is bounded by the information along every common nuisance path. This proves the linear bound while retaining all adaptive outcomes.

The separate cap $`(n\Delta)^2`$ follows with $`\phi`$ fixed: the signal derivative in each cell Hamiltonian is $`Z/2`$, so the norm of the full purified frequency generator is at most $`n\Delta/2`$. Its quantum Fisher information is at most $`(n\Delta)^2`$. This uses a different parameter path and is combined with the previous bound by taking their minimum.

### Fixed recovery attains the leading coefficient

Encode $`|+_L\rangle`$, measure parity at every boundary, and apply $`X_S`$ after every odd result. This returns the state to the even code. A no-flip cell supplies the phase $`\theta(\epsilon)`$ from the exact instrument; a recovered flip supplies $`XN_\phi=e^{i\phi Z}`$ up to a scalar phase.

Let $`K`$ be the retained number of flips. At compensation, $`K\sim\mathrm{Binomial}(n,p)`$, and all record probabilities have zero frequency derivative. The conditional logical phase and its derivative vector are

```math
\Phi_K(\epsilon,\phi)=(n-K)\theta(\epsilon)-2K\phi,
\qquad
(\partial_\epsilon\Phi_K,\partial_\phi\Phi_K)
=((n-K)d,-2K),
\qquad d=\frac{\tan\chi}{g}.
```

A uniformly randomized, recorded equatorial readout angle avoids isolated zero-probability points and attains the phase Fisher matrix given by the outer product of this vector. Averaging the full matrix before eliminating the shared nuisance gives

```math
\mathcal I_X
=d^2\left(
\mathbb E(n-K)^2
-\frac{[\mathbb E((n-K)K)]^2}{\mathbb E K^2}
\right)
=\frac{d^2n^2q}{np+q}
=\frac{n^2p}{g^2(np+q)}.
```

The binomial moments used here are $`\mathbb E K^2=n^2p^2+npq`$ and $`\mathbb E[(n-K)K]=n(n-1)pq`$. Since $`qd^2=p/g^2`$, the ratio $`\mathcal I_X/n`$ tends to $`1/g^2`$. No angle calibration or discarded failure is needed.

## The optimal two-coupling coefficient

For each $`j\in\{a,b\}`$, define

```math
p_j=\sin^2(g_j\Delta),\qquad q_j=1-p_j,
\qquad d_j=\frac{\tan(g_j\Delta)}{g_j},
\qquad f_j=q_jd_j.
```

Let

```math
v_{\mathrm{col}}
=\frac{f_ap_b-f_bp_a}{\Delta(p_a+p_b)}.
```

This is precisely the positive drift in the [finite-cadence sensing construction](microscopic_sensing.md#positive-drift-at-every-fixed-cadence). The optimal local coefficient is

```math
\lim_{n\to\infty}
\frac{\mathcal I_{\{g_a,g_b\}}^*(n\Delta)}{(n\Delta)^2}
=v_{\mathrm{col}}^2>0.
```

The no-recovery policy with a charged finishing margin already proves attainment. It remains to bound every permitted adaptive boundary experiment.

### Adaptive upper bound

On one common nuisance path of slope $`k`$, the two settings have

```math
\alpha_j=
\left(\frac{p_j}{4g_j^2}+p_jk^2\right)I,
\qquad
\beta_j=i\sum_rK_{r,j}^\dagger\dot K_{r,j}
=\left(\frac{f_j}{2}-p_jk\right)Z.
```

A classically selected setting can be represented by a control register with orthogonal label blocks. Its isometry has these same blockwise derivatives. Set

```math
A=\max_j\|\alpha_j\|,\qquad
B=\max_j\|\beta_j\|,\qquad
C=4A,\qquad v=2B=\max_j|f_j-2kp_j|.
```

Keep the same unoptimized purification throughout the adaptive protocol and write $`G_m=4\|\dot\Psi_m\|^2`$. Cauchy–Schwarz bounds the derivative cross term by $`2B\|\dot\Psi_m\|`$. Consequently

```math
G_{m+1}\le G_m+C+2v\sqrt{G_m},
\qquad G_0=0.
```

The actual output quantum Fisher information is at most $`G_m`$; the two are not identified. Parameter-independent instrument dilations preserve the derivative norm, so the recurrence includes every adaptive boundary instrument and retained outcome. A convenient finite envelope, proved by induction, is

```math
G_m\le(v m+\sqrt{Cm})^2.
```

Indeed the difference of this envelope at successive integers is at least $`C+2v(v m+\sqrt{Cm})`$. It follows immediately that $`\limsup_{m\to\infty}G_m/m^2\le v^2`$. At $`v=0`$, the recurrence gives the sharper exact linear bound $`G_m\le Cm`$.

Minimizing over the common nuisance slope gives

```math
\min_{k\in\mathbb R}\max_{j\in\{a,b\}}|f_j-2kp_j|
=\frac{|f_ap_b-f_bp_a|}{p_a+p_b}.
```

For example, $`k_*=(f_a+f_b)/[2(p_a+p_b)]`$ makes the two residuals equal and opposite; any smaller maximum would require two incompatible intervals for $`k`$. The resulting upper coefficient is $`\Delta^2v_{\mathrm{col}}^2`$ per squared cell count. The attainable coefficient in the microscopic construction matches it.

## Scope of the separation

For the fixed positive menu $`\{g_a,g_b\}`$, the strongest strategy confined to either one coupling has information at most $`n/g_a^2`$. The two-coupling construction has $`v_{\mathrm{col}}^2(n\Delta)^2+o(n^2)`$. Thus coupling diversity changes the optimal local scaling under the same prescribed boundary clock, with the same ideal ancillary and control resources.

The timing restriction is substantive. With one fixed coupling, move the same $`n-1`$ interior contacts to the midpoints of the first $`n-1`$ cells and use each for a sensor $`Z`$ pulse. Leave the last cell unrefocused and retain its terminal parity result. At compensation, an echoed cell has a known parameter-independent $`Z`$ action and a coherent local frequency derivative with duration $`\sin\chi/g`$. Tracking those known actions in the terminal readout gives the attainable information

```math
\mathcal I_{\mathrm{midpoint}}
=q\left[(n-1)\frac{\sin\chi}{g}+d\right]^2,
\qquad
\lim_{n\to\infty}
\frac{\mathcal I_{\mathrm{midpoint}}}{(n\Delta)^2}
=q\left(\frac{\sin\chi}{\chi}\right)^2>0.
```

The factor $`q`$ charges the last cell's even-parity success probability; odd results are retained as failures. No extra boundary recovery pulse is needed. The companion [contact-placement proof](https://github.com/GoGoKo699/Markovian-Resolution-Limit/blob/main/science/sensing_bridge.md) derives this local response directly from the joint dynamics. Thus a fixed contact count alone does **not** establish a coupling-activated change of scaling: fixed-coupling sensing already has quadratic local information when those contacts may be placed inside the cells. The matching separation above concerns the prescribed boundary clock.

These results remain local at $`\epsilon=0`$. They do not transfer a Fisher-information bound to global risk, give free initial localization, price finite control duration or controller work, or establish a fixed-rate limitation for arbitrary non-Markovian reservoirs. The full interaction strength and growing finite-bath resources are specified in the [construction](microscopic_sensing.md#one-shared-interaction-and-a-fixed-measurement-clock).

The proof uses the channel-extension and common-nuisance-path method attributed in the [related-work account](../references/RELATED_WORK.md); the finite-step isometry argument above states the exact specialization needed here. Passing finite checks supplements this argument rather than proving its universal control quantifier.
