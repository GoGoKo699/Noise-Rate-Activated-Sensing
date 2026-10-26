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

## Limited access inside collision cells

The boundary restriction can be relaxed quantitatively. Write $`h=\Delta`$, fix $`0<\chi=gh<\pi/4`$, and put $`p=\sin^2\chi`$, $`q=\cos^2\chi`$. Keep the same fixed coupling, fresh-cell bath, fixed nominal compensation and physical horizon $`T=nh`$.

Allow at most $`n-1`$ instantaneous system–memory contacts strictly between times zero and $`T`$. At most $`m`$ of them may lie strictly inside collision cells, where $`n\ge1`$ and $`0\le m\le n-1`$. The other contacts may occur at cell boundaries. Both bounds hold on every controller branch, including transcripts with zero probability at the operating point. Initial preparation and final readout at $`T`$ are free. A readout performed earlier is a counted contact. All outcomes and failures are retained, and an early completed outcome is stored until the charged horizon $`T`$.

The controller may use arbitrary parameter-independent adaptive instruments and protected memory. Contact times are selected classically; coherent superpositions of different contact times are not included. The bath, cell duration and coupling remain fixed, with no bath access, altered collision clock or noise-free signal-bearing waiting interval. Let $`\mathcal I_{n,m}^*`$ be the optimal nuisance-adjusted information at $`\epsilon=0`$ in this class.

The theorem includes finite adaptive instrument trees, parameter-independent classical mixtures of them, and the following controlled limits: for fixed $`n,m,g,h`$ and a common output space, every event probability converges pointwise throughout an open parameter neighborhood, with the same branchwise budgets. The derivative control needed for these limits is stated below; probability convergence alone is not being treated as Fisher-information continuity.

**Finite-budget theorem.** Define

```math
B_n=\frac{n^2p}{g^2(np+q)},
\qquad E_m=\frac p{g^2}(1+m\cos\chi)^2.
```

Then

```math
\max\{B_n,E_m\}
\le\mathcal I_{n,m}^*
\le\min\left\{n^2h^2,
\left(\frac{\sqrt n}{g}+\frac{mh}{\sin\chi}\right)^2\right\}.
```

In particular, for every permitted $`n,m`$,

```math
c_L(n+m^2)
\le\frac{\mathcal I_{n,m}^*}{h^2}
\le c_U(n+m^2),
\qquad
c_L=\frac{pq}{\chi^2(1+q)}\ge\frac8{3\pi^2},
\qquad c_U=\frac2p.
```

Thus $`\mathcal I_{n,m}^*/h^2=\Theta_\chi(n+m^2)`$. The bounds do not claim optimal crossover constants.

### Two experiments supply the lower bound

The fixed-recovery experiment above uses $`n-1`$ interior boundary contacts; its last recovery and readout are included in the free terminal instrument. It uses no contact inside a cell and attains $`B_n`$.

For the second experiment, put a sensor $`Z`$ pulse at the midpoint of each of the first $`m`$ cells. Leave cell $`m+1`$ unrefocused, then measure parity and the appropriate logical quadrature as one instrument. The known $`Z`$ actions from the echoed cells are accounted for in the readout, without extra recovery pulses. At compensation, each echoed cell contributes local phase duration $`\sin\chi/g`$; the final even branch contributes $`d=\tan\chi/g`$ and occurs with probability $`q`$. Retaining the odd result as a failure gives

```math
q\left[m\frac{\sin\chi}{g}+d\right]^2
=\frac p{g^2}(1+m\cos\chi)^2=E_m.
```

The [joint-dynamics calculation](https://github.com/GoGoKo699/Markovian-Resolution-Limit/blob/main/science/sensing_bridge.md) establishes this local response without assuming that echoed cells are noiseless away from compensation. If $`m<n-1`$, the measurement at $`(m+1)h<T`$ is one counted boundary contact, for a total of $`m+1\le n-1`$. Store its outcome through the remaining cells. If $`m=n-1`$, that measurement is the free readout at $`T`$, so there are exactly $`m=n-1`$ contacts. These rules also cover $`m=0`$ and $`n=1`$. Neither a successful branch nor an early readout reduces the charged physical horizon.

Since $`B_n/h^2\ge pn/\chi^2`$ and $`E_m/h^2\ge pqm^2/\chi^2`$, the maximum of the two experiments is at least $`c_L(n+m^2)`$. The uniform lower estimate on $`c_L`$ uses $`(\sin\chi/\chi)^2\ge8/\pi^2`$ and $`q/(1+q)\ge1/3`$ on the stated interval.

### Clean cells and controlled cells have different derivative costs

Use the same nuisance slope $`k=\cot\chi/(2g)`$ as in the fixed-coupling converse. An untouched cell has a dilation satisfying

```math
V^\dagger\dot V=0,
\qquad \|\dot V\|\le\frac1{2g}.
```

A cell containing interior contacts need not have the zero-overlap property. Its derivative is nevertheless bounded. Along the common nuisance path,

```math
\partial_uH
=\frac Z2+kg\,\partial_\phi N_\phi\otimes X_E,
\qquad
\|\partial_uH\|=\frac1{2\sin\chi}.
```

The terms anticommute. In a dilation of the adaptive instruments, the same bound holds in every classical record block at each laboratory time. Integrating the derivative insertion over one full cell therefore gives $`\|\dot V_{\mathrm{active}}\|\le L=h/(2\sin\chi)`$, even when contact times depend on earlier outcomes. The integration uses the common laboratory interval of length $`h`$, not a sum of maxima of branch-dependent waiting times.

At most $`m`$ cells can be active on a branch. The companion [derivative bound with a hard activity budget](https://github.com/GoGoKo699/Markovian-Resolution-Limit/blob/main/science/intervention_bounds.md#a-derivative-bound-with-a-hard-activity-budget) separates mutually orthogonal clean-cell derivative insertions from active-cell insertions supported on immutable activity records. Its bound with $`a=1/(2g)`$ and $`L=h/(2\sin\chi)`$ is

```math
\|\dot\Psi_n\|
\le\frac{\sqrt n}{2g}+\frac{mh}{2\sin\chi}.
```

It covers adaptively chosen active cells, protected-memory observations and nominal zero-probability branches. Multiplication by four after squaring bounds the path quantum Fisher information and hence efficient target information. The independent fixed-$`\phi`$ signal bound supplies $`n^2h^2`$.

The same proof extends to the stated limits using bounded second derivatives, rather than a continuity assumption for Fisher information. Along this path,

```math
D_1=\frac1{2\sin\chi},
\qquad D_2=gk^2,
\qquad
|\partial_u^2P(B)|\le2TD_2+4T^2D_1^2
```

for every outcome event $`B`$, uniformly over the allowed controllers. The companion [controlled-derivative limit argument](https://github.com/GoGoKo699/Markovian-Resolution-Limit/blob/main/science/intervention_bounds.md#limits-with-controlled-parameter-derivatives) shows that event-probability convergence on an open neighborhood then controls first derivatives; finite-partition Fisher information preserves the upper bound in the limit.

Finally, $`(x+y)^2\le2x^2+2y^2`$ and $`p\le\chi^2`$ give the stated $`c_U=2/p`$.

### How much access changes the scaling

With $`\chi`$ and $`h`$ fixed, $`m=O(\sqrt n)`$ retains linear information $`\Theta(n)`$; in particular this holds for $`m=o(\sqrt n)`$. If $`m/\sqrt n\to\infty`$, information is $`\Theta(m^2)`$ and is superlinear in the number of cells. A nonzero quadratic-in-$`T`$ order is possible precisely when $`m=\Omega(n)`$ under the imposed $`m\le n-1`$ budget. More generally, $`m=\Theta(n^\alpha)`$ gives order $`n+n^{2\alpha}`$ for $`0\le\alpha\le1`$.

These statements concern local information at the fixed compensated operating point. They do not identify a global estimation risk, infer derivative control from single-parameter probability agreement, or price finite-duration pulses and measurements.

## Scope of the separation

For the fixed positive menu $`\{g_a,g_b\}`$, the strongest strategy confined to either one coupling has information at most $`n/g_a^2`$. The two-coupling construction has $`v_{\mathrm{col}}^2(n\Delta)^2+o(n^2)`$. Thus coupling diversity changes the optimal local scaling under the same prescribed boundary clock, with the same ideal ancillary and control resources.

The timing restriction is substantive. The [limited-interior-access theorem](#limited-access-inside-collision-cells) quantifies it: a fixed contact count alone does **not** establish a coupling-activated change of scaling. Fixed-coupling sensing already has quadratic local information when a linear number of those contacts may be placed inside the cells. The matching two-coupling separation above concerns the prescribed boundary clock.

These results remain local at $`\epsilon=0`$. They do not transfer a Fisher-information bound to global risk, give free initial localization, price finite control duration or controller work, or establish a fixed-rate limitation for arbitrary non-Markovian reservoirs. The full interaction strength and growing finite-bath resources are specified in the [construction](microscopic_sensing.md#one-shared-interaction-and-a-fixed-measurement-clock).

The proof uses the channel-extension and common-nuisance-path method attributed in the [related-work account](../references/RELATED_WORK.md); the finite-step isometry argument above states the exact specialization needed here. Passing finite checks supplements this argument rather than proving its universal control quantifier.
