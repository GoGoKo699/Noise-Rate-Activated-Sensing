# From Ramsey sensing to noise-rate activation

[30 milestones](MILESTONES.md) · [Anchor and reading map](HAASE_BRIDGE.md) · [Overview](../README.md) · [Scientific synthesis](../science/interpretation.md)

This tutorial bridges the single educational anchor, [Haase et al., arXiv:1807.11882v4](https://arxiv.org/abs/1807.11882v4), to the research. Basic qubit states, tensor products, and the Born rule are the starting language. Estimation notation is introduced as it is used. The source locations and normalization translations are in the [learning guide](HAASE_BRIDGE.md); the project derivations below are not attributed to the anchor.

## How this tutorial connects to the milestones

The [30-milestone map](MILESTONES.md) is the dependency-ordered route; this tutorial groups its calculations by mechanism. Sections 1–3 develop the experimental and statistical background. Sections 4–7 explain the two constructions and the universal bound. Sections 8–9 join local precision, global risk, and physical scope. The map supplies direct source pointers for material whose full treatment lives in the scientific pages.

## 1. One qubit, one likelihood, one clock

Prepare $`|+\rangle=(|0\rangle+|1\rangle)/\sqrt2`$. A frequency $`\omega`$ acts through $`H=\omega Z/2`$ for physical time $`t`$. In units with $`\hbar=1`$, the rotation is $`U_\omega(t)=e^{-i\omega tZ/2}`$. Read out in an equatorial basis with a known angle $`\chi`$. The two outcome probabilities are

```math
p_\pm(\omega\mid t,\chi)=\frac{1\pm\cos(\omega t-\chi)}2.
```

These probabilities, together with the chosen controls, form the **likelihood**: a rule assigning a probability to each possible data record for each candidate frequency. The phase $`\vartheta=\omega t`$ is dimensionless. Throughout this repository, $`\phi`$ is reserved for the unknown *noise direction*, not for $`\vartheta`$.

The classical Fisher information of this measurement is

```math
F_{\rm cl}(t)=\sum_{y\in\{+,-\}}\frac{(\partial_\omega p_y)^2}{p_y}=t^2
```

at regular readout points. It measures local distinguishability of nearby frequencies, not the amount by which one experimental outcome determines the frequency. Drawing and retaining a uniform angle $`\chi`$ avoids exceptional zero-probability points for any fixed phase. The qubit's quantum Fisher information also equals $`t^2`$ here; for a general state a particular measurement need not attain the quantum bound.

For $`\nu`$ independent repetitions of duration $`t`$, information adds to $`\nu t^2`$ and time adds to $`\nu t`$. With a total budget $`T=\nu t`$, this is $`Tt`$. One cannot simultaneously claim a single coherent interrogation of duration $`T`$ and $`\nu`$ free copies of its output. The ideal costs of preparation and readout are specified in the [model](../science/model.md).

## 2. Detect an error without reading the signal

Our sensor also experiences transverse errors

```math
N_\phi=\cos\phi\,X+\sin\phi\,Y,
\qquad
\dot\rho=-i\frac\omega2[Z,\rho]+\gamma(N_\phi\rho N_\phi-\rho).
```

The rate $`\gamma>0`$ has units of inverse time. The angle $`\phi`$ is fixed but unknown. Since $`N_\phi^\dagger N_\phi=I`$, errors in the ideal jump description occur with rate $`\gamma`$, independent of the sensor's logical state. This does not give the controller direct bath access.

Add a noiseless ancilla and encode a logical state as

```math
|\psi_L\rangle=c_0|00\rangle+c_1|11\rangle,
\qquad |c_0|^2+|c_1|^2=1.
```

The sensor is the first qubit. Both basis states have even parity, measured by $`Z\otimes Z`$. The signal preserves this parity. An error gives

```math
(N_\phi\otimes I)|\psi_L\rangle
=c_0e^{i\phi}|10\rangle+c_1e^{-i\phi}|01\rangle,
```

which has odd parity. Projecting onto either parity sector does not distinguish $`c_0`$ from $`c_1`$. Thus the measurement can detect an error without measuring the unknown signal phase. Arbitrarily fast ideal parity extraction supplies the syndrome record used below; finite-rate and faulty measurements are different assumptions.

If $`\phi`$ were known, applying $`N_\phi`$ after an error would undo it. A fixed sensor recovery $`X`$ also returns the state to the code, but leaves

```math
XN_\phi=e^{i\phi Z}.
```

After duration $`t`$ and $`n`$ detected errors, the logical phase is therefore

```math
\Theta=\omega t-2\phi n.
```

The state is back in the code, but its phase is not independent of the error direction. This fixed-recovery building block is attributed to the primary predecessor in [preset protocols](../science/preset_protocols.md); it is not a new general correction method.

## 3. Why a nuisance parameter costs information

A **nuisance parameter** is unknown and affects the observations, although it is not the quantity we want to report. Here it is $`\phi`$. For the complete record $`x`$, define the two scores and their Fisher matrix by

```math
\ell_\omega=\partial_\omega\log p(x\mid\omega,\phi),
\qquad \ell_\phi=\partial_\phi\log p(x\mid\omega,\phi),
\qquad J_{ij}=\mathbb E[\ell_i\ell_j].
```

Scores say how the likelihood changes under small parameter shifts. If a target shift can be imitated by a nuisance shift, part of the apparent target information is not usable without knowing the nuisance. Removing that part gives

```math
\mathcal I_\omega
=\min_c\mathbb E[(\ell_\omega+c\ell_\phi)^2]
=J_{\omega\omega}-\frac{J_{\omega\phi}^2}{J_{\phi\phi}}
```

when $`J_{\phi\phi}>0`$. The minimizing coefficient is $`c=-J_{\omega\phi}/J_{\phi\phi}`$. The first expression also covers a singular nuisance block. This is the ordinary projection of the target score away from the nuisance score, not a new definition of quantum Fisher information.

For the fixed-recovery phase $`\Theta=\omega t-2\phi n`$, the derivative vector is $`(t,-2n)`$. Averaging its outer product over $`n\sim\mathrm{Poisson}(\gamma t)`$ gives

```math
J=\begin{pmatrix}
t^2&-2\gamma t^2\\
-2\gamma t^2&4(\gamma^2t^2+\gamma t)
\end{pmatrix},
\qquad
\mathcal I_\omega=\frac{t^2}{1+\gamma t}.
```

The entry $`J_{\omega\omega}=t^2`$ treats the direction as known. With the direction unknown, this protocol has only linear leading information. Typical counts are near $`\gamma t`$, so the phase is nearly $`(\omega-2\gamma\phi)t`$: that is the ambiguity the subtraction captures.

This calculation evaluates one protocol. Only the separate [converse](../science/precision_bounds.md) shows that no allowed fixed-rate strategy escapes a linear ceiling. Also, inverse Fisher information is a bound for a local estimation task, not automatically the mean-square error of a globally usable estimator.

## 4. A complete rate-diversity example

Set $`a=1`$ and $`b=3`$ in inverse-time units and use an interrogation of duration $`t=10`$. Choose rate $`a`$ with probability $`3/4`$ and rate $`b`$ with probability $`1/4`$. Keep that rate fixed within the interrogation. Prepare $`|+_L\rangle`$, monitor parity, apply sensor $`X`$ after each detected error, and record the count $`n`$. At the end, draw and record $`\chi`$ and measure the equatorial logical basis.

The complete data are the setting label $`j`$, count $`n`$, readout angle $`\chi`$, and outcome $`y`$. Conditional on $`j`$, the count is Poisson with mean $`\gamma_jt`$ and the phase remains $`\omega t-2\phi n`$. For this example,

```math
\mathbb E[n]=15,\qquad
\mathbb E[n^2]=315,
\qquad
J=\begin{pmatrix}100&-300\\-300&1260\end{pmatrix}.
```

The efficient information is

```math
\mathcal I_\omega=100-\frac{300^2}{1260}=\frac{200}{7}\approx28.5714.
```

The universal fixed-rate $`a`$ bound at the same physical duration is $`t/a=10`$; the particular fixed-recovery baseline has $`100/11\approx9.0909`$. The rate-diverse experiment exceeds the first bound in **local information**, not necessarily in the actual error of a single-shot global estimator. The states in its individual branches still contain the nuisance.

The shared direction allows the two types of labelled data to constrain the same nuisance. Form their full Fisher matrices and combine them **before** eliminating that nuisance. Eliminating an independent direction in each branch would be a different experiment. A label supplies no target information on its own; it identifies which likelihood generated the observation.

For any two distinct positive rates, the optimal leading coefficient is $`r^2`$, where $`r=(b-a)/(b+a)`$. A fair recorded choice needs no numerical rate calibration in the design and has coefficient $`(b-a)^2/[2(a^2+b^2)]`$, at least half the optimum. For $`a=1,b=3`$, these coefficients are $`1/5`$ and $`1/4`$. Treating the rates as additional unknowns does not change the phase-information block when the complete counts are used; [preset protocols](../science/preset_protocols.md) derives that statement.

Three repetitions of the example cost 30 time units and have information $`3(200/7)=600/7`$, not three free interrogations at total cost 10. The direction must remain shared across the pooled data. No within-run rate feedback is used, but the recovery pulses still follow detected errors.

## 5. What the preset echo trades for balance

An alternative uses two timed blocks and a logical echo between them. With fixed recovery after each error, its phase is

```math
\Theta=\omega(t_a-t_b)-2\phi(n_a-n_b).
```

For $`a=1,b=3,T=10`$, choose $`t_a=7.5`$ and $`t_b=2.5`$. The expected counts are equal, so the mean signed count vanishes. With signed time $`D=5`$ and signed-count variance $`V=15`$, the Fisher matrix is $`\mathrm{diag}(25,60)`$ and the efficient information is 25.

This is statistical orthogonality: $`J_{\omega\phi}=0`$. It does not say that $`n_a=n_b`$ on each run or that its output is direction-independent. For general durations the exact information is

```math
\mathcal I_{\rm echo}=\frac{D^2V}{V+\mu^2},
\quad D=t_a-t_b,\quad V=at_a+bt_b,\quad\mu=at_a-bt_b.
```

With a fixed fractional timing imbalance, $`D`$ and $`\mu`$ grow as $`T`$ while $`V`$ grows as $`T`$. The denominator then eventually loses the quadratic advantage. Common rescaling of both rates preserves balance; differential errors need not. That sensitivity belongs to the echo, not to the recorded random-rate protocol. Neither protocol requires learning $`\phi`$ in order to choose the recovery pulse.

## 6. Let the error supply its own recovery

Now leave detected errors uncorrected. The identities

```math
N_\phi^2=I,\qquad N_\phi ZN_\phi=-Z
```

mean that two errors cancel, while the signal accumulates with reversed sign between them. On an even-count trajectory, the logical rotation depends only on

```math
D(t)=\int_0^t(-1)^{n(u)}du,
\qquad U_L(t)=e^{-i\omega D(t)Z_L/2}.
```

For a concrete path, suppose the sensor spends 0.9 time units in the even sector, jumps, spends 0.25 in the odd sector, jumps again, and spends another 0.85 in the even sector. Its physical duration is 2, but its signed time is $`0.9-0.25+0.85=1.5`$. Direct multiplication gives the Ramsey operation of duration 1.5 for every noise angle. Neither the two error times nor the resulting phase require an estimate of $`\phi`$.

Use the lower rate $`a`$ in the even sector and the higher rate $`b`$ in the odd sector. The negative intervals are shorter on average. Stop at the first time $`\tau_d`$ when $`D(t)=d>0`$. The first upward crossing is in the even sector, so each completed run gives the same exact channel $`e^{-i\omega dZ_L/2}`$, independently of $`\phi`$.

The first-passage law, derived in [stopped sensing](../science/stopped_sensing.md), gives

```math
\mathbb E[\tau_d]=\frac{d}{r},\qquad
\mathrm{Var}(\tau_d)=\frac{8ab\,d}{(b-a)^3}.
```

For $`a=1,b=3,d=4`$, the mean physical duration is 8 and the variance is 12. The exact effective time 4 does not mean physical completion at time 8 on every run. A hard deadline must retain unfinished trials. At equal rates, eventual completion has infinite mean duration; a perfect eventual output alone is not a precision advantage.

This construction uses syndrome-conditioned **rate** feedback but no recovery pulse after an error. Its channel guarantee is stronger than the preset protocols' local statistical separation. Predicting throughput needs rate information, but the signed-clock stopping rule does not.

## 7. From a protocol to an all-strategy bound

A failed protocol cannot rule out every adaptive alternative. To prove a universal restriction, consider the physical parameter family along

```math
\omega(u)=\omega_c+u,\qquad\phi(u)=\phi_c+cu.
```

Any estimator that works with an unknown direction must also handle these joint parameter changes. For a fixed protocol, its efficient target information is at most the information along any such path, which is bounded by that path's output quantum Fisher information $`F_u`$. The path is a proof device; the physical bath is not assumed to carry the target frequency.

The [theorem proof](../science/precision_bounds.md) imports the adaptive channel-growth inequality from Das and colleagues. In the gauge used here it reads

```math
\frac{dF_u}{dt}\le4(\|A\|+\|B\|\sqrt{F_u}),
\qquad
A=c^2\gamma I,\qquad B=(1/2-c\gamma)Z.
```

$`A`$ and $`B`$ are operators built from **parameter** derivatives of the generator; their norms constrain the **time** growth of information. They are not additional controls. At a fixed rate, choosing $`c=1/(2\gamma)`$ makes $`B=0`$. Integrating from a parameter-independent initial state gives $`F_u(T)\le T/\gamma`$ and therefore the universal nuisance-adjusted bound.

At two rates one common slope cannot cancel $`B`$ at both. The minimax choice yields leading coefficient at most $`r^2`$; the constructions attain it. The proof covers arbitrary permitted ancillary controls, not merely the parity protocols used to explain attainment. The anchor motivates channel bounds, but this adaptive inequality and its precise assumptions must still be read as a research-level imported premise, not as a consequence of replacing its probe number by time.

## 8. Global precision is a separate statement

A single Ramsey likelihood is periodic. Frequencies separated by $`2\pi/t`$ can produce the same phase. Large local Fisher information does not resolve that ambiguity or certify a globally accurate estimator.

The repository's global task fixes a frequency interval independently of $`T`$, permits biased estimators, and maximizes the mean-square error over the unknown frequency and direction. The [global proof](../science/global_precision.md) applies the uniform nuisance-path bound to a smooth prior using the van Trees argument. It proves a fixed-rate lower scaling $`\Omega(T^{-1})`$; paid, short no-error trials provide the matching upper scaling.

For rate access, several prescribed effective times of the exact stopped channel resolve the phase ambiguity. Their physical durations and deadline failures are all counted. Together with a global lower bound this gives

```math
R_{\rm fixed}(T;\Omega)=\Theta(T^{-1}),\qquad
R_{[a,b]}(T;\Omega)=\Theta(T^{-2}).
```

Here $`\Omega`$ inside $`R`$ denotes the fixed frequency interval; $`\Omega(T^{-1})`$ in a scaling statement denotes an asymptotic lower bound. The exact optimal global constant is not supplied by the local coefficient $`r^2`$. The preset random-rate calculation is not substituted for the stopped-channel global proof.

## 9. Carry the assumptions with the result

The shared, stable direction matters: separate unknown axes for the settings have a linear-information converse. A scalar rate change must preserve the specified signal response. Ordinary known pulses do not give independent reversal of an unknown signal while leaving every unknown noise direction unchanged.

Ideal syndrome extraction and noiseless ancillary storage are shared resources in the main comparison. Fixed-interval ideal measurements have only the separately stated compensated **local** result. A fixed positive unobserved parallel dephasing rate $`\kappa`$ restores the ceiling $`\mathcal I_\omega^*(T)\le T/(4\kappa)`$, although a quantified finite-time advantage remains. Use the project's contrast convention $`e^{-2\kappa t}`$; see the [source normalization note](HAASE_BRIDGE.md#rate-normalization-when-using-the-source).

The [physical scope](../science/physical_scope.md), [residual-noise calculation](../science/residual_dephasing.md), and [attribution](../references/RELATED_WORK.md) explain those boundaries. The [scientific synthesis](../science/interpretation.md) is the expert route through the full claims. The [milestone map](MILESTONES.md) connects these distinctions into one shared route through the project.
