# Global precision at a hard time budget

[Model](model.md) · [Local theorems](precision_bounds.md) · [Stopped-channel construction](stopped_sensing.md)

This comparison uses the same global squared-error criterion on both sides. It does not assume an unbiased estimator, a known noise angle, or prior frequency localization on a scale that shrinks with the available time.

## Statistical task and theorem

Fix a closed frequency interval $`\Omega`$ of width $`W>0`$, independent of $`T`$. The transverse direction is any $`\phi\in\mathbb R/\pi\mathbb Z`$, shared throughout the experiment. Let

```math
R_{\mathcal A}(T;\Omega)
=\inf_{\mathcal P,\widehat\omega}\;
\sup_{\omega\in\Omega,\phi}
\mathbb E_{\omega,\phi}^{\mathcal P}
[(\widehat\omega-\omega)^2].
```

The infimum includes every allowed control, measurement, classical randomization, and estimator at a hard physical deadline $`T`$. The access model $`\mathcal A`$ is either one fixed known rate $`\gamma>0`$ or the known selectable interval $`[a,b]`$, $`0<a<b`$. Both models permit the same ideal parameter-independent sensor–ancilla controls. The estimator can be clipped to $`\Omega`$ without increasing risk. Every trial, calibration stage, and failed stop is charged. Ancilla storage does not supply additional signal exposure.

**Global precision theorem.** Under these access models,

```math
R_{\mathrm{fixed}}(T;\Omega)=\Theta(T^{-1}),
\qquad
R_{[a,b]}(T;\Omega)=\Theta(T^{-2}).
```

The constants depend on the fixed interval and rates. More specifically,

```math
\liminf_{T\to\infty}T R_{\mathrm{fixed}}(T;\Omega)\ge\gamma,
\qquad
\liminf_{T\to\infty}T^2 R_{[a,b]}(T;\Omega)\ge\frac1{r^2},
\qquad r=\frac{b-a}{b+a}.
```

These are lower bounds on global constants, not a claim that those constants are achievable globally. The local coefficient $`r^2`$ and the globally optimal mean-square-error constant remain different quantities.

## A bound valid for biased estimators

The statistical ingredient is the scalar van Trees inequality, used here in the form developed for minimax arguments by [Gill and Levit](https://projecteuclid.org/journals/bernoulli/volume-1/issue-1-2/Applications-of-the-van-Trees-inequality--a-Bayesian-Cram%C3%A9r/bj/1186078362.full). The inequality is inherited; the nuisance paths and resulting sensing comparison are the application here.

Take an interval center $`\omega_c`$ and a fixed $`h>0`$ with $`[\omega_c-h,\omega_c+h]\subseteq\Omega`$. For $`u\in(-h,h)`$ use the density

```math
\pi_h(u)=\frac1h\cos^2\!\left(\frac{\pi u}{2h}\right),
\qquad I(\pi_h)=\frac{\pi^2}{h^2}.
```

Consider any smooth path $`\omega(u)=\omega_c+u`$, $`\phi(u)=\phi_c+cu`$ through the physical parameter family. A prior concentrated on this path is a legitimate lower-bound device for a supremum over the full parameter set; it is not extra information given to the controller. For a fixed protocol with outcome density $`p(x\mid u)`$, define the joint score

```math
S(u,x)=\partial_u\log[p(x\mid u)\pi_h(u)].
```

The density vanishes at the endpoints, and integration by parts yields

```math
\mathbb E[(\widehat\omega(x)-\omega_c-u)S(u,x)]=1.
```

The conditional likelihood score has zero mean. Consequently

```math
\mathbb E S^2=\mathbb E_{\pi_h}J_u+I(\pi_h),
\qquad
\mathbb E[(\widehat\omega-\omega)^2]
\ge\frac1{\mathbb E_{\pi_h}J_u+I(\pi_h)}.
```

Cauchy–Schwarz supplies the last inequality without any unbiasedness condition. The argument applies to the complete classical outcome of an adaptive quantum experiment, whose $`J_u`$ is bounded by the output QFI. The ideal-model bounds can equivalently be obtained as limits of regular finite-step protocols. Estimators with infinite risk already obey the lower bound.

## Fixed-rate lower bound

Choose $`c=1/(2\gamma)`$. The [nuisance-path channel bound](precision_bounds.md#the-common-nuisance-path) gives $`J_u\le F_u\le T/\gamma`$ at every point on the path, uniformly over the allowed strategies. Therefore

```math
\boxed{R_{\mathrm{fixed}}(T;\Omega)
\ge\frac1{T/\gamma+\pi^2/h^2}.}
```

Taking $`T\to\infty`$ proves the fixed-rate lower scaling and its stated liminf. Learning the angle during sensing, using a biased estimator, or changing the readout cannot avoid this global worst-case bound.

## A matching fixed-rate upper scaling

A simple paid rejection scheme suffices; optimal constants are not needed for this part. Compensate the known center $`\omega_c`$ and use repeated probes of fixed duration

```math
\tau=\min\{1/\gamma,\pi/(2W)\},
\qquad m=\lfloor T/\tau\rfloor.
```

Continuously monitor the syndrome. A trial containing no error has probability $`p_0=e^{-\gamma\tau}`$, independent of both parameters, and produces an exact Ramsey phase $`(\omega-\omega_c)\tau`$. Trials with errors still cost $`\tau`$ and are retained as failures. The number of useful trials is $`K\sim\mathrm{Binomial}(m,p_0)`$.

On each useful trial measure the sine quadrature $`Y_L`$. For $`K>0`$, clip its sample mean to $`[-\sin(W\tau/2),\sin(W\tau/2)]`$, apply $`\arcsin`$, divide by $`\tau`$, and add $`\omega_c`$. Since $`W\tau/2\le\pi/4`$, the inverse map is Lipschitz with constant at most $`\sqrt2/\tau`$. Conditional risk is at most $`2/(K\tau^2)`$. Use the interval midpoint when $`K=0`$.

The binomial identity

```math
\mathbb E\frac1{K+1}
=\frac{1-(1-p_0)^{m+1}}{(m+1)p_0},
\qquad
\frac{\mathbf1_{K>0}}K\le\frac2{K+1}
```

gives the uniform bound

```math
R_{\mathrm{fixed}}(T;\Omega)
\le\frac4{\tau^2(m+1)p_0}
+\frac{W^2}{4}(1-p_0)^m
=O(T^{-1}).
```

This is not a free postselection gain: the number of attempted trials, not just useful trials, fixes the physical cost. The known-angle assumption is never used.

## Controlled-rate lower bound

For $`c=1/(a+b)`$, the local converse gives, along this path,

```math
F_u'\le C+2r\sqrt{F_u},
\qquad C=\frac{4b}{(a+b)^2},
\qquad F_u(0)=0.
```

A convenient explicit supersolution is

```math
B(T)=(rT+\sqrt{CT})^2.
```

Indeed $`B'-(C+2r\sqrt B)=r\sqrt{CT}\ge0`$. It follows that

```math
R_{[a,b]}(T;\Omega)\ge\frac1{B(T)+\pi^2/h^2}.
```

The fixed-$`\phi`$ path $`c=0`$ separately gives the usual target-only bound $`F_u\le T^2`$ and thus

```math
R_{[a,b]}(T;\Omega)
\ge\max\left\{
\frac1{B(T)+\pi^2/h^2},
\frac1{T^2+\pi^2/h^2}
\right\}.
```

These two lower bounds use different path priors. Their maximum is valid for minimax risk; it must not be described as a bound on the QFI of a single common path. Since $`B(T)/T^2\to r^2`$, the global controlled-rate liminf follows.

## Controlled-rate upper scaling

The [stopped-channel proof](stopped_sensing.md#global-estimation-on-a-bounded-interval) supplies the matching uniform $`O(T^{-2})`$ estimator. Its essential ingredients are an exact Ramsey operation at each prescribed effective time, a multiscale schedule resolving the phase ambiguity, and a hard-deadline bound for the sum of random physical durations.

For total prescribed effective exposure $`S`$, that sum has Laplace transform $`e^{-S k(q)}`$ with the stated first-passage exponent. Choosing $`S\le\alpha rT`$, $`0<\alpha<1`$, leaves an exponentially small deadline-failure probability. A bounded fallback on failure adds exponentially small risk, while successful multiscale estimation costs $`O(T^{-2})`$ in risk. The schedule is independent of the unknown angle, and all physical times are included.

Together with the lower bounds, this completes the same-metric global comparison. It does not promote the preset random-rate experiment's local Fisher matrix into a global estimator, and does not require that the entire stopped schedule fit into one Ramsey fringe.

## Finite checks

`tests/test_risk.py` checks the prior normalization and information, the integration-by-parts ingredient, the ODE supersolution, binomial moments, and a seeded no-jump estimator against its upper bound. The universal and minimax conclusions follow from the proofs, not from sampled estimator performance.
