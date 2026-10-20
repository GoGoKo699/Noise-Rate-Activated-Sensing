# Exact stopped sensing and its physical cost

[Model](model.md) · [Optimality proof](precision_bounds.md) · [Physical scope](physical_scope.md)

This construction uses rates $`0<a<b`$, unit signal strength, a shared fixed unknown $`N_\phi`$, and ideal syndrome timing. A completed operation is exact for every input logical state and every $`\omega,\phi`$, not just at a local operating point.

## Protocol and exact output

Prepare the logical state in the even code, use rate $`a`$ in the even sector and rate $`b`$ in the odd sector, and do not apply recovery pulses. From the detected count $`n(t)`$ compute

```math
D(t)=\int_0^t(-1)^{n(u)}du.
```

For a prescribed $`d>0`$, stop at

```math
\tau_d=\inf\{t\ge0:D(t)=d\}.
```

An upward crossing has even parity. The [trajectory identity](precision_bounds.md#attainment-by-leaving-the-errors-uncorrected) therefore gives the exact logical channel

```math
\rho_L\longmapsto U_\omega(d)\rho_LU_\omega(d)^\dagger,
\qquad U_\omega(d)=e^{-i\omega dZ_L/2}.
```

The recorded stopping time is independent of $`\omega`$ and $`\phi`$. Neither numerical rate values nor $`\phi`$ enter the stopping rule. Rates determine completion statistics, not the correctness of the completed channel. Encoding, syndrome extraction, decoding, and readout still require control; only error-recovery pulses during sensing are absent.

## First-passage law

Write $`r=(b-a)/(b+a)`$ and $`\delta=(b-a)/2`$. For $`q\ge0`$,

```math
\mathbb E[e^{-q\tau_d}]=e^{-dk(q)},
\qquad
k(q)=\sqrt{q^2+(a+b)q+\delta^2}-\delta.
```

To derive this, let $`f_\pm(x)`$ be the Laplace transform of the remaining first-passage time from signed position $`x<d`$ and parity $`\pm`$. The backward equations are

```math
\partial_x f_+ +a(f_- -f_+)=qf_+,
```

```math
-\partial_x f_- +b(f_+-f_-)=qf_-.
```

Set $`f_\pm(x)=v_\pm e^{-k(d-x)}`$. The outgoing boundary is $`v_+=f_+(d)=1`$. The incoming limit $`f_-(d^-)`$ is not assigned the same boundary value. The determinant condition is

```math
k^2+(b-a)k-q(q+a+b)=0,
\qquad
v_-=\frac{a+q-k}{a}=\frac b{b+q+k}.
```

The nonnegative root, bounded as $`x\to-\infty`$, gives the transform. At $`q=0`$ it is one, so completion is almost sure. Differentiating the logarithm gives

```math
\mathbb E\tau_d=\frac d r,
\qquad
\mathrm{Var}(\tau_d)=\frac{8ab\,d}{(b-a)^3}.
```

The moment-generating function is the same expression at $`q=-\theta`$, for

```math
0<\theta<\theta_c,
\qquad \theta_c=\frac{(\sqrt b-\sqrt a)^2}{2}.
```

One way to justify finiteness before analytic continuation is to use the tilted two-state generator for $`D(t)`$. Its exponential moments have a dominant eigenvalue negative for a small negative tilt, because the stationary signed drift is $`r>0`$. Since $`\{\tau_d>t\}\subseteq\{D(t)<d\}`$, an exponential Markov bound supplies an exponential first-passage tail. The transform identity then continues around zero; the displayed square-root singularity specifies the positive moment domain.

At $`a=b=\gamma`$, the transform becomes $`e^{-d\sqrt{q(q+2\gamma)}}`$. Completion is still almost sure, but its mean is infinite. Eventual perfect output is therefore not, by itself, a finite-cost precision advantage.

## A hard deadline and the optimal local coefficient

At physical time $`T`$, terminate any unfinished run. Decode completed outputs into the noiseless ancilla. Keep the success flag and assign failures a parameter-independent state. Because success is parameter-independent, this admissible experiment has efficient local information

```math
\mathcal I_\omega(T)=p_Td^2,
\qquad p_T=\Pr(\tau_d\le T).
```

For a dimensionally explicit asymptotic construction, let $`t_c=1/(a+b)`$ and set

```math
h(T)=t_c(T/t_c)^{2/3},
\qquad d=r[T-h(T)]
```

for sufficiently large $`T`$. The mean completion time is $`T-h(T)`$ and the variance is $`O(T)`$. Chebyshev's inequality gives $`1-p_T=O(T^{-1/3})`$. Thus

```math
\mathcal I_\omega(T)/T^2\longrightarrow r^2,
```

matching the universal converse. Both the margin and every failed run are charged to $`T`$.

### A finite-time separation

Choose $`b=3a`$ and $`d=T/4`$. Then

```math
\mathbb E\tau_d=T/2,
\qquad \mathrm{Var}(\tau_d)=\frac{3T}{4a},
\qquad p_T\ge\max\left\{0,1-\frac3{aT}\right\}.
```

Consequently

```math
\mathcal I_\omega(T)\ge\frac{T^2}{16}
\max\left\{0,1-\frac3{aT}\right\}.
```

For $`aT>19`$, this lower bound strictly exceeds the fixed-rate upper bound $`T/a`$. It therefore beats every allowed strategy confined to rate $`a`$, not just uncorrected Ramsey sensing. A larger fixed rate has an even smaller linear upper bound. The number 19 is a conservative sufficient threshold, not the optimized onset of advantage.

## Global estimation on a bounded interval

The exact stopped channel permits a separate global statement. For any fixed bounded frequency interval of width $`W>0`$, there is an estimation procedure, using a hard total budget $`T`$, whose worst-case mean-square error is $`O(T^{-2})`$ uniformly in the shared direction. The constant depends on the fixed interval and rates. This is not a claim that the local coefficient $`r^2`$ is the optimal global risk constant.

Here is an explicit reduction, using the established multiscale phase-estimation idea attributed in [related work](../references/RELATED_WORK.md#phase-estimation-and-stopping-background).

### A noiseless schedule with quadratic global precision

Center the interval by a known $`Z`$ rotation and choose $`d_0`$ with $`Wd_0\le\pi/2`$. Use effective durations $`d_k=2^kd_0`$ for $`k=0,\ldots,K`$. At each stage measure both Ramsey quadratures, each on $`n_k`$ fresh probes. Sample means estimate the sine and cosine of the phase. For a deviation tolerance $`1/8`$ per quadrature, Hoeffding's inequality gives

```math
\Pr(\text{stage }k\text{ is inaccurate})\le4e^{-n_k/128}.
```

On the complementary event, the phase error is less than $`\pi/6`$. Take

```math
n_k=\left\lceil128[(K-k)\log8+\log16]\right\rceil.
```

Unwrap each phase by choosing the frequency representative nearest the preceding estimate. The phase-error tolerance is smaller than $`\pi/3`$, so accurate consecutive stages select the correct representative. If the first inaccurate stage is $`k`$, the final error is $`O(2^{-k}/d_0)`$: each later nearest-representative update moves the estimate by at most $`\pi/(2^\ell d_0)`$, and the remaining geometric series is bounded. Clipping the final estimate to the known interval cannot increase squared error.

The probability of an inaccurate stage $`k`$ is at most $`8^{-(K-k)}/4`$. Hence

```math
\mathbb E[(\widehat\omega-\omega)^2]
=O(4^{-K})+
O\left(\sum_{k=0}^K4^{-k}8^{-(K-k)}\right)
=O(4^{-K}),
```

where fixed factors of $`d_0`$ are absorbed in the constants. The total effective exposure is

```math
S_K=2\sum_{k=0}^Kn_kd_k=\Theta(2^K).
```

Thus the noiseless schedule has global mean-square error $`O(S_K^{-2})`$. This construction is intentionally conservative; it establishes scaling, not an optimized experimental schedule.

### Charge the random physical durations

Replace every Ramsey experiment by its exact stopped version. Fresh runs start in the even code. Their timing laws are independent of the state, phase, angle, and measurement choices. The product of their Laplace transforms is

```math
\mathbb E[e^{-q\tau_{\rm total}}]=e^{-S_Kk(q)}.
```

Choose the largest $`K`$ for which $`S_K\le\alpha rT`$, with fixed $`0<\alpha<1`$. Since $`S_K=\Theta(2^K)`$, this still gives $`S_K=\Theta(T)`$. For sufficiently small fixed $`\theta>0`$,

```math
\Pr(\tau_{\rm total}>T)
\le \exp[-\theta T-S_Kk(-\theta)]
\le e^{-cT}
```

for some $`c>0`$, because $`-k(-\theta)=\theta/r+O(\theta^2)`$. Assign a bounded fallback estimate if the deadline is reached. Its risk contribution is at most $`W^2e^{-cT}`$. The completed schedule contributes $`O(T^{-2})`$. This proves the global statement without omitting long runs or assuming prior localization to accuracy $`1/T`$.

## Fixed-count alternative

Stopping after exactly $`m`$ complete error pairs also cancels $`\phi`$. The total even and odd residence times are independent gamma variables with shape $`m`$ and rates $`a,b`$. Therefore

```math
\mathbb E D^2=m^2\left(\frac1a-\frac1b\right)^2
+m\left(\frac1{a^2}+\frac1{b^2}\right),
```

with mean physical duration $`m(1/a+1/b)`$. This gives the same leading rate contrast, but has random effective interrogation time. The first-passage construction above instead fixes the effective time exactly and is the direct route to global phase-estimation protocols.
