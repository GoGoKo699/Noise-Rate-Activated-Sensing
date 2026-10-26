# Global estimation from recorded phase functions

[Microscopic global precision](microscopic_global_precision.md) · [Exact collision records](microscopic_sensing.md) · [Paid calibration](microscopic_identifiability.md)

An observed trajectory can specify an exact sensing phase even when its probability and its phase response both depend on the unknown frequency. The appropriate estimator conditions on those records and inverts their actual phase functions. Averaging the phases first is unnecessary and can destroy the available coherence.

The multiscale schedule and bounded-variable concentration used below are inherited from the [phase-estimation and statistical background](../references/RELATED_WORK.md#phase-estimation-and-stopping-background). The purpose of this account is to supply the additional conditional argument, a sufficient record-selection criterion and the complete cost for a microscopic instrument. It does not assume a parameter-independent record distribution or infer risk from Fisher information.

## Recorded-phase estimation lemma

Let the target residual frequency be $`u\in J=[-E,E]`$, with $`E>0`$ fixed independently of the number of available collision cells. Adding the fixed nominal frequency to an estimate of $`u`$ leaves its squared error unchanged. Other unknown parameters, including a shared direction $`\phi`$, are nuisance parameters. Suppose the following resources are available.

1. A block of exactly $`L`$ cells produces a retained classical record $`\mathcal R`$. A known predicate declares the record accepted or failed. Every block costs $`L`$ cells, including failures. Accepted records supply the exact logical state

```math
|\psi_{\mathcal R}(u)\rangle
=e^{-i\Phi_{\mathcal R}(u)Z_L/2}|+_L\rangle,
```

where the function $`\Phi_{\mathcal R}`$ is known from the record and hardware, and is independent of the unknown nuisance. A known record-dependent phase correction can be included in this function or in the readout.

2. There are fixed constants $`p_0>0`$, $`0<\alpha\le\beta<\infty`$ and an integer $`L_0\ge1`$ such that, for every $`L\ge L_0`$, the acceptance probability is at least $`p_0`$ uniformly in the target and nuisance. Every accepted record obeys

```math
\alpha L\le \Phi_{\mathcal R}'(v)\le\beta L
\qquad\text{for every }v\in J.
```

The acceptance predicate does not use the unknown parameters. Records can have zero probability at particular parameter values; no derivative or positive-density assumption about their law is needed.

3. After readout, blocks can be reset to the same fixed input and repeated with independent fresh bath cells. Within a stage the block policy is unchanged, so its later records do not depend on earlier terminal readouts. Conditional on their records, the terminal readouts are independent. Their measurement bases can depend on the observed records and on estimates from earlier stages.

4. A coarse estimator using $`N`$ one-cell trials has the uniform concentration guarantee

```math
\sup_{u\in J,\phi}
\Pr\{|\widehat u_N-u|\ge\delta\}
\le2\exp\!\left(-\frac{N\kappa_0^2\delta^2}{2}\right),
\qquad \kappa_0>0,
```

and can be clipped to $`J`$. The [single-cell calibration theorem](microscopic_identifiability.md) supplies this resource for the collision applications.

**Conclusion.** There is an explicit estimator, with all blocks and calibration trials charged to a deterministic budget of at most $`n`$ cells, such that

```math
\sup_{u\in J,\phi}
\mathbb E[(\widehat u-u)^2]=O(n^{-2}).
```

The constant depends on the fixed band, instrument and constants above. This is an attainable risk bound, not a statement about an optimal global coefficient. The lemma accounts for cells; each application must also bound the contacts used by its block and reset instruments.

## A two-state parity gate

Here is a sufficient condition for the accepted-record hypotheses. Start a block in even parity, denoted $`+`$. Use setting $`a`$ after an even result and setting $`b`$ after an odd result. The state-independent flip probabilities are $`p_a(u),p_b(u)`$, and $`q_j=1-p_j`$. Suppose on the fixed band

```math
0\le p_a(u)\le p_b(u)\lt \frac12,
\qquad p_a(u)+p_b(u)>0,
\qquad
\lambda(u)=1-p_a(u)-p_b(u)\le\rho\lt 1.
```

An even terminal record has a known phase

```math
\Phi_{\mathcal R}(u)
=\sum_{i=1}^L\sigma_{i-1}
\mathbf1_{\{\sigma_i=\sigma_{i-1}\}}
\theta_{j(\sigma_{i-1})}(u),
\qquad j(+)=a,\quad j(-)=b,
```

possibly plus a known parameter-independent phase. Let $`d_j=\theta_j'(0)>0`$, $`M=\max_jd_j`$, and define the frozen derivative reward and its stationary mean by

```math
D_L^0=\sum_{i=1}^L\sigma_{i-1}
\mathbf1_{\{\sigma_i=\sigma_{i-1}\}}d_{j(\sigma_{i-1})},
```

```math
\mu^0(u)
=\frac{p_b(u)q_a(u)d_a-p_a(u)q_b(u)d_b}
{p_a(u)+p_b(u)},
\qquad \mu_0=\mu^0(0)>0.
```

Assume also the two uniform band conditions

```math
\mu^0(u)\ge\frac{3\mu_0}{4},
\qquad
\max_j\sup_{v\in J}|\theta_j'(v)-d_j|
\le\frac{\mu_0}{4}.
```

These are conditions on fixed functions over a fixed interval. The last two inequalities are strict at zero, so continuity supplies a nonzero interval on which they hold; its width need not shrink with the experimental budget. The separate transition-probability conditions must also hold on that interval and explicitly permit $`p_a(0)=0`$.

Accept a record precisely when

```math
\sigma_L=+,
\qquad D_L^0\ge\frac{\mu_0 L}{2}.
```

The predicate is computed from the observed record and the known zero-frequency derivatives. It does not assume that the actual frequency is zero.

### Uniform acceptance probability

At a fixed target value, write

```math
\pi_+=\frac{p_b}{p_a+p_b},\qquad
\pi_-=\frac{p_a}{p_a+p_b},\qquad
f_+=q_ad_a,\qquad f_-=-q_bd_b.
```

Starting in $`+`$, the exact two-state recursion gives

```math
\Pr\{\sigma_i=+\}=\pi_++\pi_-\lambda^i\ge\frac12,
```

```math
\mathbb E D_L^0
=L\mu^0(u)+\pi_-(f_+-f_-)
\sum_{i=0}^{L-1}\lambda^i
\ge\frac{3\mu_0L}{4}.
```

The transient term is nonnegative. These identities remain valid when $`p_a=0`$: the initial even state is then absorbing, and no irreducibility assumption is being made.

For the variance, let $`X_i`$ be the $`i`$th reward in $`D_L^0`$. Its range has length at most $`2M`$. For $`i<j`$, conditioning on the history through cell $`i`$ gives

```math
\mathbb E[X_j\mid\sigma_0,\ldots,\sigma_i]
=(P^{j-i-1}f)(\sigma_i),
\qquad
P=\begin{pmatrix}q_a&p_a\\p_b&q_b\end{pmatrix}.
```

The two possible values on the right differ by at most $`2M\rho^{j-i-1}`$. The covariance bound by one quarter of the product of the two ranges follows from Cauchy–Schwarz and the bounded-variable variance inequality. Consequently, without assuming a stationary initial distribution,

```math
|\mathrm{Cov}(X_i,X_j)|\le M^2\rho^{j-i-1},
\qquad
\mathrm{Var}(D_L^0)\le VL,
\qquad
V=M^2\left(1+\frac2{1-\rho}\right).
```

Chebyshev's inequality and the even-parity probability give

```math
\Pr\{\text{accepted}\}
\ge\frac12-\frac{16V}{\mu_0^2L}
\ge\frac14
\qquad
\left(L\ge L_0=\max\left\{1,
\left\lceil\frac{64V}{\mu_0^2}\right\rceil\right\}\right).
```

No independence between the derivative gate and final parity is asserted; the first inequality is a union bound.

### Uniform phase sensitivity on accepted records

The derivative of an accepted record differs from $`D_L^0`$ by at most $`L\mu_0/4`$ throughout the entire band. Therefore

```math
\frac{\mu_0L}{4}
\le\Phi_{\mathcal R}'(v)
\le\beta L,
\qquad
\beta=\max_j\sup_{v\in J}|\theta_j'(v)|.
```

Thus the recorded-phase lemma applies with $`p_0=1/4`$ and $`\alpha=\mu_0/4`$, whenever the exact accepted logical phase and the calibration resource are available. Positivity of the stationary frozen reward supplies sensitivity; the record gate makes that sensitivity a statement about every accepted phase function, rather than only its average.

## Nested multiscale estimation

We prove the recorded-phase lemma for general $`p_0,\alpha,\beta`$. Define

```math
s=\frac\pi{8\beta},\qquad
L_k=2^kL_0,\qquad
\gamma=\min\left\{\frac{p_0^2}{2},
\frac{p_0\alpha^2s^2}{8}\right\}>0.
```

Fix an integer $`K\ge1`$. First use the coarse estimator with

```math
N_0(K)=\left\lceil
\frac{2L_0^2}{\kappa_0^2s^2}
\bigl(K\log8+\log2\bigr)
\right\rceil
```

one-cell trials, and set $`C_0=J\cap[\widehat u_0-s/L_0,\widehat u_0+s/L_0]`$. Its failure probability is at most $`8^{-K}`$, and its diameter is at most $`2s/L_0`$. Because the estimate is clipped to $`J`$, this interval is always nonempty, even on failure.

### One refinement

At stage $`k=1,\ldots,K`$, let $`c`$ be the midpoint of $`C_{k-1}`$. Run

```math
r_k=\left\lceil
\frac{(K-k)\log8+\log12}{\gamma}
\right\rceil
```

independent blocks of length $`L_k`$. For each accepted record, measure the equatorial observable whose conditional mean is

```math
\mathbb E[Y_i\mid\mathcal R_i]
=\sin\bigl(\Phi_{\mathcal R_i}(u)-\Phi_{\mathcal R_i}(c)\bigr),
\qquad Y_i\in\{-1,+1\}.
```

For example, the observable is $`\cos(\Phi_{\mathcal R_i}(c))Y_L-\sin(\Phi_{\mathcal R_i}(c))X_L`$. This is a classical choice of the terminal measurement basis from the observed record and earlier estimate. It neither changes the Hamiltonian during a cell nor retunes the nominal compensation.

Let $`G`$ be the number of accepted blocks. If $`G<p_0r_k/2`$, set $`\widetilde u_k=c`$. Otherwise compute the known function

```math
H_k(v)=\frac1G\sum_{i:\,\mathcal R_i\text{ accepted}}
\sin\bigl(\Phi_{\mathcal R_i}(v)-\Phi_{\mathcal R_i}(c)\bigr)
\qquad (v\in C_{k-1}),
```

and invert it at the sample mean of the corresponding $`Y_i`$, after clipping that mean to the image interval $`H_k(C_{k-1})`$. Denote the result by $`\widetilde u_k`$, and set

```math
C_k=C_{k-1}\cap
[\widetilde u_k-s/L_k,\widetilde u_k+s/L_k].
```

Every $`C_k`$ is nonempty and nested, including on failure branches, because $`\widetilde u_k\in C_{k-1}`$. A degenerate interval already specifies its unique estimate and needs no inversion.

For any candidate $`v\in C_{k-1}`$ and accepted record,

```math
|\Phi_{\mathcal R_i}(v)-\Phi_{\mathcal R_i}(c)|
\le\beta L_k\frac{s}{L_{k-1}}=\frac\pi4,
\qquad H_k'(v)\ge\frac{\alpha L_k}{\sqrt2}.
```

The image is therefore a single monotone branch, although the full uncentered record phase can wind arbitrarily many times. Previous stages resolve that ambiguity by restricting the candidate interval.

### Conditional concentration

Conditional on all earlier observations, the acceptance indicators of the fresh blocks are independent and have probability at least $`p_0`$. Hoeffding's inequality yields

```math
\Pr\{G\lt p_0r_k/2\}\le e^{-p_0^2r_k/2}.
```

Next condition on all records in this stage. Their probability law can depend on the target. The accepted $`Y_i`$ are still independent, with average conditional mean exactly $`H_k(u)`$. When $`u\in C_{k-1}`$, the inverse derivative bound and clipping imply that an estimation error larger than $`s/L_k`$ requires a sample-mean deviation larger than $`\alpha s/\sqrt2`$. On $`G\ge p_0r_k/2`$, its conditional probability is at most

```math
2\exp\!\left(-\frac{G\alpha^2s^2}{4}\right)
\le2\exp\!\left(-\frac{p_0r_k\alpha^2s^2}{8}\right).
```

Integrating over the records and adding the low-count event gives the uniform conditional stage guarantee

```math
\Pr\{u\notin C_k\mid\text{earlier observations with }u\in C_{k-1}\}
\le3e^{-\gamma r_k}
\le\frac14\,8^{-(K-k)}.
```

This argument does not differentiate or replace the record distribution. Failed blocks remain in the complete experiment and its resource budget.

### Global risk and deterministic cost

Return the midpoint $`\widehat u`$ of $`C_K`$. If all stages succeed, its error is at most $`s/L_K`$. If the first failed refinement is stage $`k`$, the true target and every later estimate lie in $`C_{k-1}`$, so the final error is at most $`4s/L_k`$. If the coarse stage fails, both the target and final estimate still lie in $`J`$, giving the bound $`2E`$. Therefore

```math
\sup_{u\in J,\phi}\mathbb E[(\widehat u-u)^2]
\le\frac{s^2}{L_K^2}+4E^2\,8^{-K}
+\sum_{k=1}^K\frac{16s^2}{L_k^2}\,
\frac14\,8^{-(K-k)}
\le\frac{9s^2+4E^2L_0^2}{L_K^2}.
```

All attempted blocks, including those failing the record gate, consume their prescribed length. The deterministic cell count is

```math
B_K=N_0(K)+\sum_{k=1}^Kr_kL_k.
```

The inequalities $`\sum_{k=1}^KL_k\le2L_K`$ and $`\sum_{k=1}^K(K-k)L_k\le2L_K`$ give $`B_K\le C_*L_K`$ for a fixed constant $`C_*`$; the coarse cost is $`O(K+1)`$ and $`K+1\le2^K`$. Also $`B_K\ge L_K`$. For a hard budget $`n`$, choose the largest feasible $`K`$. Since $`n<B_{K+1}\le2C_*L_K`$, the risk is $`O(n^{-2})`$. Small budgets can use a clipped fixed estimate and are absorbed into the constant.

If the schedule finishes before the prescribed horizon, retain its classical estimate through the remaining charged cells. A terminal readout before that horizon is a counted contact. Resets, record measurements and any setting changes must be combined or charged according to the application's allowed instruments; the proof never treats repeated trials, an early readout, discarded records or free signal exposure as additional resources.

The result depends on exact recorded phase functions and a uniform positive probability of usable records. It makes no claim that an unrecorded mixture, an imperfect timing record or a phase inferred only at one operating point has the same global precision.
