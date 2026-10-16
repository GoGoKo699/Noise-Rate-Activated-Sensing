# Preset protocols and rate calibration

[Model](MODEL.md) · [Optimality](THEOREMS.md) · [Exact stopped sensing](STOPPED_SENSING.md)

Two positive rates suffice to attain the optimal leading **local** information without syndrome-conditioned bath-rate changes. The protocols here still detect errors and apply a fixed sensor recovery $X$. They retain the setting, count record, and final measurement outcome. They do not produce a direction-independent channel on every trajectory.

The fixed-recovery building block and the single-rate formula below are inherited from Tanggara et al., Appendix A.4(a), Eqs. (A19)–(A29), with $\omega=2\theta$. The additions are the rate-diverse designs, their exact information, and their calibration dependence. Pooling Fisher matrices and eliminating a common nuisance are statistical operations, not new formalisms. See [attribution](../literature/RELATED_WORK.md).

## Common readout and the order of nuisance elimination

Use the even-parity code $|0_L\rangle=|00\rangle$, $|1_L\rangle=|11\rangle$. Every detected sensor error is followed by $X$. Since

$$
XN_\phi=e^{i\phi Z},
$$

a constant setting of duration $t$, signal strength $s$, and observed count $n$ leaves the logical phase $\Theta=\omega st-2\phi n$. Error times do not enter this phase in the ideal instantaneous-recovery limit.

Prepare $|+_L\rangle$, draw and record an independent uniform equatorial readout angle $\chi$, and measure the two outcomes with conditional probabilities

$$
p_\pm=\frac{1\pm\cos(\Theta-\chi)}2.
$$

The conditional classical Fisher information about $\Theta$ is one away from isolated zero-probability points. Uniform recorded $\chi$ makes those points a null set for every fixed unknown phase. No estimate of $\phi$ is needed to select this measurement.

For a phase $\Theta=\omega D-2\phi M$ and a parameter-independent record $(D,M)$, the complete classical Fisher matrix for $(\omega,\phi)$ is

$$
J=\begin{pmatrix}
\mathbb E D^2&-2\mathbb E[DM]\\
-2\mathbb E[DM]&4\mathbb E M^2
\end{pmatrix}.
$$

First pool this matrix over recorded counts and settings; then take its nuisance Schur complement. Taking a Schur complement separately in each conditional experiment and averaging it answers a different question. All settings and repetitions share the same fixed nuisance angle in the present model.

## Two-block echo

Preset two durations $t_a,t_b>0$, with $t_a+t_b=T$. Use rate $a$ in the first block and $b$ in the second. Apply the fixed recovery after each jump, insert a logical $X_L$ between blocks, and undo it at the end. The two block phases subtract:

$$
\Theta=\omega D-2\phi M,
\qquad D=t_a-t_b,
\qquad M=n_a-n_b.
$$

Here $n_a,n_b$ are independent Poisson counts. Set

$$
\mu=at_a-bt_b,
\qquad V=at_a+bt_b.
$$

Then $\mathbb E M=\mu$, $\mathbb E M^2=V+\mu^2$, and

$$
J=\begin{pmatrix}D^2&-2D\mu\\-2D\mu&4(V+\mu^2)\end{pmatrix},
\qquad
\mathcal I_{\rm echo}=\frac{D^2V}{V+\mu^2}.
$$

The known-rate choice

$$
t_a=\frac b{a+b}T,
\qquad t_b=\frac a{a+b}T
$$

has $\mu=0$ and gives the **exact finite-time** local information

$$
\mathcal I_{\rm echo}=r^2T^2,
\qquad r=\frac{b-a}{b+a}.
$$

The nuisance is statistically orthogonal to the target, not absent from each output state. The bath schedule is preset; the recovery pulses still depend on detected errors. All runs finish at $T$ and none are postselected. For $b=3a$, this particular protocol exceeds the universal fixed-rate-$a$ upper bound $T/a$ whenever $aT>4$.

### Timing imbalance and its crossover

Write $t_a=fT$, $t_b=(1-f)T$, and define the fixed rates

$$
q=af-b(1-f),
\qquad v=af+b(1-f).
$$

The exact law becomes

$$
\mathcal I_{\rm echo}
=\frac{(2f-1)^2T^2}{1+(q^2/v)T}.
$$

For a nonzero fixed imbalance $q$, it crosses to linear information at times of order $v/q^2$. For a sequence of designs approaching $f_*=b/(a+b)$, a nonzero quadratic coefficient requires $q^2T/v=O(1)$; recovering the ideal coefficient requires $q^2T/v\to0$. Thus this single echo's differential balancing error must scale as $T^{-1/2}$ or better in fixed rate units. This is a limitation of this design, not a lower bound on all rate-diverse protocols.

To isolate calibration error, choose durations using nominal rates $a_0,b_0$ while the true rates are $a=a_0(1+\epsilon_a)$, $b=b_0(1+\epsilon_b)$. With

$$
\lambda_0=\frac{a_0b_0}{a_0+b_0}T,
\qquad r_0=\frac{b_0-a_0}{b_0+a_0},
$$

one obtains

$$
\mathcal I_{\rm echo}
=\frac{r_0^2T^2}
{1+\lambda_0(\epsilon_a-\epsilon_b)^2/(2+\epsilon_a+\epsilon_b)}.
$$

A common multiplicative rate error preserves balance. Differential error produces the penalty. This expression describes the correctly specified likelihood at the true rates, not the bias of an estimator that inserts wrong rates and ignores them.

## A recorded random choice of one rate

At the start of an interrogation, choose rate $a$ with probability $p$ and rate $b$ otherwise. Retain that label and keep its rate constant for the full physical duration $T$. Use the same fixed recovery $X$ and readout as above. There is no within-run rate switch or logical echo pulse.

For the random rate $\Gamma$, define

$$
\bar\gamma=pa+(1-p)b,
\qquad g_2=pa^2+(1-p)b^2,
\qquad \sigma_\gamma^2=p(1-p)(b-a)^2.
$$

Conditioned on the label, $N\sim\operatorname{Poisson}(\Gamma T)$ and $\Theta=\omega T-2\phi N$. Pooling the labelled Fisher matrices gives

$$
J=\begin{pmatrix}
T^2&-2\bar\gamma T^2\\
-2\bar\gamma T^2&4(g_2T^2+\bar\gamma T)
\end{pmatrix},
$$

and hence

$$
\mathcal I_p(T)=T^2\frac{\sigma_\gamma^2+\bar\gamma/T}{g_2+\bar\gamma/T}.
$$

For a single rate this reduces to the inherited formula $T^2/(1+\gamma T)$. For distinct rates and any fixed $0<p<1$, its leading coefficient is positive:

$$
C(p)=\lim_{T\to\infty}\frac{\mathcal I_p(T)}{T^2}
=\frac{p(1-p)(b-a)^2}{pa^2+(1-p)b^2}.
$$

The two labels produce different leading target–nuisance score directions. The gain comes from their joint statistical model, not from a rate-dependent target signal or a direction-free output in either branch.

### Optimal and calibration-free choices

The maximum leading coefficient is $r^2$, at $p_*=b/(a+b)$. The identity

$$
r^2-C(p)
=r^2\frac{[(a+b)p-b]^2}{pa^2+(1-p)b^2}
$$

proves optimality within this labelled design and quantifies its tolerance. A fixed probability error changes the coefficient continuously; it does not cause the time-amplified penalty of an unbalanced echo. This probability is held fixed when differentiating the unknown parameters, even when selected using nominal rates.

No numerical rate calibration is needed to choose $p=1/2$. Its coefficient obeys

$$
C(1/2)=\frac{(b-a)^2}{2(a^2+b^2)},
\qquad
\frac{C(1/2)}{r^2}=\frac{(a+b)^2}{2(a^2+b^2)}\in(1/2,1)
$$

for distinct positive rates. A fair choice therefore retains at least half the optimal **local-information coefficient**, without precisely balancing expected counts. This fraction is not a precision or risk ratio for a globally unknown frequency. For $b=3a$ it is $4/5$ of the optimal coefficient.

At $b=3a$, $p=3/4$, the exact finite-time law simplifies to

$$
\mathcal I_{3/4}(T)=T^2\frac{aT+2}{4aT+2}.
$$

It exceeds the universal fixed-rate-$a$ upper bound for $aT>1+\sqrt3$. This is a certificate for one local-information protocol, not an optimal finite-time threshold.

### Also treating the numerical rates as unknown

For fixed durations or fixed randomization probabilities, the conditional phase likelihood depends on $(\omega,\phi)$ and the observed counts, not explicitly on $(a,b)$. The rate score comes from the count likelihood. Its cross-information with each conditional phase score vanishes because the latter has zero conditional mean.

Consequently the full Fisher matrix for $(\omega,\phi,a,b)$ is block diagonal between the first two and last two parameters. The rate blocks are

$$
J_{\rm rates}^{\rm echo}=\operatorname{diag}(t_a/a,t_b/b),
\qquad
J_{\rm rates}^{\rm mixture}=\operatorname{diag}(pT/a,(1-p)T/b).
$$

Eliminating the numerical rates as additional nuisance parameters leaves the displayed efficient information unchanged. This does not grant a free rate oracle to the estimator: joint inference uses the retained counts. It establishes that the fair random design needs no rate-calibration stage to retain quadratic local information. It does not assert global risk bounds for that design or a calibration cost for every possible adaptive scheme.

### General selectable settings

For a recorded random setting $j$ with probability $p_j$, Hamiltonian strength $s_j$, and rate $\gamma_j$, the same calculation gives

$$
\frac{\mathcal I(T)}{T^2}
=\mathbb E[s^2]
-\frac{\mathbb E[s\gamma]^2}{\mathbb E[\gamma^2]+\mathbb E[\gamma]/T}.
$$

For a pair $i,j$, choose probabilities $p_i=\gamma_j/(\gamma_i+\gamma_j)$ and $p_j=1-p_i$. Direct substitution yields

$$
\lim_{T\to\infty}\frac{\mathcal I(T)}{T^2}
=\left(\frac{s_i\gamma_j-s_j\gamma_i}{\gamma_i+\gamma_j}\right)^2.
$$

A maximizing pair therefore attains [Theorem 3](THEOREMS.md#theorem-3--selectable-signal-and-noise-strengths) without syndrome-conditioned rate control.

## Relation to stopped sensing

| Construction | Rate choice | Recovery pulses | Rate knowledge for its stated purpose | Output guarantee |
|---|---|---|---|---|
| Balanced preset echo | Two timed blocks | Fixed $X$ after each error, plus logical echo | Ratio needed for balance | Exact local information $r^2T^2$ |
| Recorded random rate | Once at the start | Fixed $X$ after each error | None for the fair design; ratio optimizes the coefficient | Quadratic local information; no trajectory-wise cancellation |
| Stopped sensing | Conditioned on measured parity | None after errors | Not needed for output correctness; throughput bounds require rate information | Exact direction-independent Ramsey channel on success |

Every construction still uses ideal syndrome monitoring and noiseless ancillary support. For the random design, $T$ is the duration of **each** complete interrogation; $\nu$ repetitions cost $\nu T$ and have Fisher matrix $\nu J$. Its local statement must not be reinterpreted as an $O(T^{-2})$ global risk guarantee for one random branch. The [stopped protocol](STOPPED_SENSING.md) supplies the separate bounded-interval global theorem with every duration and failure charged.

If different settings have independently unknown directions, the Fisher matrices have separate nuisance columns. The rate-mixing gain then disappears, consistent with the [independent-axis converse](THEOREMS.md#independent-setting-dependent-directions). A retained label and a shared stable nuisance are load-bearing resources.
