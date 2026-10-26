# From open-system dynamics to global noise-strength sensing

[30 milestones](MILESTONES.md) · [Anchor and reading map](ANCHOR.md) · [Overview](../README.md) · [Scientific synthesis](../science/interpretation.md)

This tutorial bridges the sisters’ single educational anchor, [Rivas and Huelga, _Open Quantum Systems: An Introduction_, arXiv:1104.5242v2](https://arxiv.org/abs/1104.5242v2), to the sensing research. Basic qubit states, tensor products, and the Born rule are the starting language. Estimation notation is introduced as it is used. The source locations and normalization translations are in the [learning guide](ANCHOR.md); the project derivations below are not attributed to the anchor.

## How this tutorial connects to the milestones

The [30-milestone map](MILESTONES.md) is the dependency-ordered route; this tutorial groups calculations by mechanism. Sections 1–3 introduce the experiment, the parity code and the nuisance parameter. The **principal microscopic route** then follows [sections 10–13](#10-from-a-bounded-collision-to-an-observed-phase): exact finite-strength records, the global one-versus-two-coupling comparison, ambiguity resolution, and the boundary with temporal access. Sections 4–9 provide a separately proved Markovian counterpart through simple numerical examples, sharp local information and exact stopped sensing.

The common anchor supplies channels, generators and microscopic reduction. The statistical and control arguments below are supplied locally and attributed to their primary sources. They should not be read as consequences of a textbook Markov approximation. The scientific pages contain the full proofs; the tutorial makes their dependencies visible.

## 1. One qubit, one likelihood, one clock

Prepare $`|+\rangle=(|0\rangle+|1\rangle)/\sqrt2`$. A frequency $`\omega`$ acts through $`H=\omega Z/2`$ for physical time $`t`$. In units with $`\hbar=1`$, the rotation is $`U_\omega(t)=e^{-i\omega tZ/2}`$. Read out in an equatorial basis with a known angle $`\zeta`$. The two outcome probabilities are

```math
p_\pm(\omega\mid t,\zeta)=\frac{1\pm\cos(\omega t-\zeta)}2.
```

These probabilities, together with the chosen controls, form the **likelihood**: a rule assigning a probability to each possible data record for each candidate frequency. The phase $`\vartheta=\omega t`$ is dimensionless. Throughout this repository, $`\phi`$ is reserved for the unknown *noise direction*, not for $`\vartheta`$.

The classical Fisher information of this measurement is

```math
F_{\rm cl}(t)=\sum_{y\in\{+,-\}}\frac{(\partial_\omega p_y)^2}{p_y}=t^2
```

at regular readout points. It measures local distinguishability of nearby frequencies, not the amount by which one experimental outcome determines the frequency. Drawing and retaining a uniform angle $`\zeta`$ avoids exceptional zero-probability points for any fixed phase. The qubit's quantum Fisher information also equals $`t^2`$ here; for a general state a particular measurement need not attain the quantum bound.

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

which has odd parity. Projecting onto either parity sector does not distinguish $`c_0`$ from $`c_1`$. Thus the measurement can detect an error without measuring the unknown signal phase. Arbitrarily fast ideal parity extraction supplies the continuous-time syndrome record in sections 4–9. In sections 10–13, parity is measured only at fixed collision boundaries and the exact instrument is derived afresh. Faulty measurements remain a different assumption.

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

Set $`a=1`$ and $`b=3`$ in inverse-time units and use an interrogation of duration $`t=10`$. Choose rate $`a`$ with probability $`3/4`$ and rate $`b`$ with probability $`1/4`$. Keep that rate fixed within the interrogation. Prepare $`|+_L\rangle`$, monitor parity, apply sensor $`X`$ after each detected error, and record the count $`n`$. At the end, draw and record $`\zeta`$ and measure the equatorial logical basis.

The complete data are the setting label $`j`$, count $`n`$, readout angle $`\zeta`$, and outcome $`y`$. Conditional on $`j`$, the count is Poisson with mean $`\gamma_jt`$ and the phase remains $`\omega t-2\phi n`$. For this example,

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

At two rates one common slope cannot cancel $`B`$ at both. The minimax choice yields leading coefficient at most $`r^2`$; the constructions attain it. The proof covers arbitrary permitted ancillary controls, not merely the parity protocols used to explain attainment. The anchor supplies channel and generator language; this adaptive inequality and its precise assumptions are a separate research-level premise. It is not obtained by replacing probe number with time in a parallel-metrology bound.

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

Ideal syndrome extraction and noiseless ancillary storage are shared resources in this Markovian comparison. Its fixed-interval ideal-measurement calculation is a compensated **local** result. The exact finite-strength collision model has the separate global theorem explained below. A fixed positive unobserved parallel dephasing rate $`\kappa`$ restores the ceiling $`\mathcal I_\omega^*(T)\le T/(4\kappa)`$, although a quantified finite-time advantage remains. Use the project's contrast convention $`e^{-2\kappa t}`$; see the [source normalization note](ANCHOR.md#rate-normalization).

The [physical scope](../science/physical_scope.md), [residual-noise calculation](../science/residual_dephasing.md), and [attribution](../references/RELATED_WORK.md) explain those boundaries. The [scientific synthesis](../science/interpretation.md) is the expert route through the full claims. The [milestone map](MILESTONES.md) connects these distinctions into one shared route through the project.

## 10. From a bounded collision to an observed phase

The principal microscopic theorem fixes a cell duration $`h`$, a nominal compensation $`\omega_0`$, and either one positive coupling or a menu $`0<g_a<g_b<\pi/(4h)`$. During each cell, signal and noise act simultaneously:

```math
H=\frac\epsilon2 Z_S\otimes I_E+gN_\phi\otimes X_E,
\qquad \epsilon=\omega-\omega_0.
```

Every bath qubit begins in $`|0\rangle`$, is used once and remains inaccessible. All bath cells are prepared at time zero and retained afterward. Controls occur only at cell boundaries. The full Hamiltonian norm is $`R=\sqrt{g^2+\epsilon^2/4}`$; a physical strength budget must cover the signal term as well as the noisy coupling.

The two terms anticommute and square to multiples of the identity. Exponentiating the joint Hamiltonian and taking bath matrix elements gives the exact operators

```math
K_0=\cos(Rh)I-i\frac{\epsilon}{2R}\sin(Rh)Z_S,
\qquad
K_1=-i\frac gR\sin(Rh)N_\phi.
```

The parity code of section 2 makes these branches observable without measuring the bath: $`K_0`$ preserves the sector and $`K_1`$ flips it. Each branch probability is independent of the logical input. Write $`p_g=(g^2/R^2)\sin^2(Rh)`$ and $`q_g=1-p_g`$. On a sufficiently small fixed band around compensation,

```math
K_0/\sqrt{q_g}=e^{-i\theta_g(\epsilon)Z_S/2},
\qquad
\theta_g(\epsilon)=2\arctan\!\left[
\frac{\epsilon}{2R}\tan(Rh)
\right].
```

After every even result choose $`g_a`$; after every odd result choose $`g_b`$. Let $`\sigma_i=\pm1`$ denote the measured parity after cell $`i`$, starting with $`\sigma_0=+1`$. A record ending even contains an even number of $`N_\phi`$ factors. Commuting the intervening rotations through them reverses the rotation signs, and the paired unknown operators cancel. Its exact logical state is

```math
|\psi_{\mathcal R}(\epsilon)\rangle
=e^{-i\Phi_{\mathcal R}(\epsilon)Z_L/2}|+_L\rangle,
\qquad
\Phi_{\mathcal R}(\epsilon)
=\sum_{i=1}^L\sigma_{i-1}
\mathbf1_{\{\sigma_i=\sigma_{i-1}\}}
\theta_{g_i}(\epsilon).
```

For example, a five-cell sequence “stay, flip, stay, flip, stay” has phase $`2\theta_a(\epsilon)-\theta_b(\epsilon)`$ and probability $`q_a(\epsilon)^2p_a(\epsilon)q_b(\epsilon)p_b(\epsilon)`$. The phase has no unknown direction, but both this phase function and the record probability depend on frequency. Recording a function does not reveal its value at the unknown frequency. It supplies a known response curve for the terminal measurement.

This is an exact finite-strength statement. A no-flip cell generally accumulates $`\theta_g(\epsilon)`$, not $`\epsilon h`$. Matching a Markovian parity-transition probability at compensation would not establish equality of the phases or their frequency derivatives.

## 11. What two couplings change globally

The [microscopic theorem](../science/microscopic_global_precision.md) fixes one positive-width identifiable interval $`\Omega=[\omega_0-E,\omega_0+E]`$ for the entire experiment. It does not shrink with $`n`$. The risk is the worst-case mean-square frequency error over that interval and every shared direction. The same fixed coupling must be used in all pooled trials of the single-coupling benchmark.

A simple one-cell calibration already gives a uniform inverse-linear upper bound. Measure $`Y_L`$ after an even parity result, assigning the score $`Z=\pm1`$, and assign $`Z=0`$ after an odd result. Here $`Z`$ is a classical variable. Its mean is

```math
F(\epsilon)=\mathbb E Z
=\frac{\epsilon\sin(2Rh)}{2R}.
```

This likelihood is independent of $`\phi`$. On a sufficient band, $`F'(\epsilon)\ge\kappa>0`$. Thus clip the empirical mean to $`F([-E,E])`$ and invert $`F`$. The inverse is Lipschitz and the score is bounded, yielding mean-square error at most $`1/(n\kappa^2)`$. The [calibration proof](../science/microscopic_identifiability.md) also supplies exponential confidence bounds. Every odd outcome and every reset consumes a cell and its applicable contact.

Why can no more elaborate boundary controller improve the fixed-coupling order? Write $`K_0=aI-ibZ_S`$, $`K_1=-icN_\phi`$ and $`p=c^2`$. Along the mathematical nuisance curve

```math
\phi'(\epsilon)=\frac{ab'-ba'}p,
```

the exact physical Kraus derivative overlap vanishes. The corresponding adaptive channel bound is linear in cell count, uniformly on the band. Integrating this information bound against a smooth prior gives a worst-case risk lower bound for biased as well as unbiased estimators. The proof curve selects a difficult subfamily of allowed unknown parameters; it does not add a physical frequency dependence to the bath. The [bounded-loss closure](../science/microscopic_global_precision.md#global-risk-under-controlled-limits) extends that global lower bound to the stipulated operational limits without invoking continuity of Fisher information.

The two-coupling upper bound needs more than cancellation. Some even-ending records have poor signed phase sensitivity. The construction accepts only even records whose known frozen derivative reward is sufficiently positive. Distinct couplings give a positive drift; continuity supplies a fixed band on which every accepted phase satisfies

```math
\alpha L\le\Phi'_{\mathcal R}(v)\le\beta L
\qquad (|v|\le E),
```

for fixed positive constants. The acceptance probability is uniformly bounded below for sufficiently long blocks. The gate is a function of the observed record and fixed hardware, never of the unknown frequency. Its [analytic proof](../science/recorded_phase_estimation.md#a-two-state-parity-gate) controls the whole band and the nonstationary parity chain. Positive average drift or positive local Fisher information alone would not supply these guarantees.

## 12. Resolve ambiguity with the recorded functions

A steep phase can wind around the circle many times. The estimator must determine which winding contains the unknown frequency. The [recorded-phase construction](../science/recorded_phase_estimation.md#nested-multiscale-estimation) starts with paid one-cell calibration and then uses block lengths $`L_k=2^kL_0`$.

At each stage let $`c`$ be the center of the current residual-frequency interval. For an accepted record, choose the terminal logical observable

```math
\cos(\Phi_{\mathcal R}(c))Y_L
-\sin(\Phi_{\mathcal R}(c))X_L.
```

Its outcome $`Y=\pm1`$ has conditional mean

```math
\mathbb E[Y\mid\mathcal R]
=\sin\bigl(\Phi_{\mathcal R}(\epsilon)
-\Phi_{\mathcal R}(c)\bigr).
```

The preceding interval is narrow enough that every accepted sine response stays on one monotone branch. For the actual records collected, average their known response functions and invert that average at the observed sample mean, clipping first to its image. This uses the functions that were observed, not an average phase computed with a guessed record distribution.

Each block starts from a fresh preparation with independent bath cells. Within a stage its policy is fixed and does not adapt to earlier terminal outcomes. Conditional on all of that stage's records, the readouts are therefore independent and their average conditional mean is exactly the averaged response at the true frequency. Concentration can be applied conditionally and then integrated over the frequency-dependent record law. No derivative of that law or assumption that it is constant is needed.

Intersect each new confidence interval with the previous one, including on failure branches. If the first wrong refinement is at scale $`L_k`$, later estimates remain inside the last valid interval, so the eventual error is only of order $`L_k^{-1}`$. Early stages receive more repetitions, making their more damaging failures rarer. A tapered allocation with $`r_k=O(K-k+1)`$ has deterministic total cell cost

```math
B_K=N_0(K)+\sum_{k=1}^K r_kL_k=O(L_K),
```

including the coarse calibration and every rejected block. The weighted failure errors sum to $`O(L_K^{-2})`$. Choosing the largest feasible depth therefore gives $`O(n^{-2})`$ global risk without a logarithmic overhead. Multiscale phase estimation and the first-failure principle are inherited methods; the observed nonlinear functions, their conditional concentration and the uniform record gate are the extra work required by this instrument.

The implementation combines parity extraction, readout, re-preparation and setting changes at the same boundary into the permitted instrument. Finishing before cell $`n`$ pays that early readout as a contact and retains the classical estimate through the rest of the charged horizon. It uses at most $`n-1`$ nonterminal contacts overall. The estimate changes terminal readout bases, never $`\omega_0`$. Together with the separate signal-generator lower bound, this establishes the matching global orders

```math
R_g^*(n)=\Theta(n^{-1}),
\qquad
R_{\{g_a,g_b\}}^*(n)=\Theta(n^{-2}).
```

The constants depend on the fixed hardware and sufficient band. The theorem does not give a maximal band or an optimal global coefficient.

## 13. Separate strength control from temporal access

The coupling comparison permits boundary contacts only. Its converse does not apply if the controller can interrupt a collision. The companion [global contact theorem](https://github.com/GoGoKo699/Markovian-Resolution-Limit/blob/main/science/global_contact_precision.md) keeps one fixed coupling but allows at most $`m`$ inside-cell contacts within $`n-1`$ total contacts. An exact midpoint pulse creates an echoed temporal setting. Choosing between echoed and plain cells provides usable records for the same estimator, while an activity-budget nuisance bound constrains every permitted adaptive controller. The resulting risk is of order $`1/[h^2(n+m^2)]`$ on a fixed sufficient band.

Both types of contact must be paid. For example, using at most $`Q=\min\{m,\lfloor(n-1)/2\rfloor\}`$ cells for the temporal construction leaves room for at most $`Q`$ inside-cell pulses and $`Q`$ boundary instruments, including early readout. The full duration is still $`nh`$. The baseline calibration using plain cells supplies the inverse-linear option. This is why counting only pulses would misstate the resource law.

The companion [timing theorem](https://github.com/GoGoKo699/Markovian-Resolution-Limit/blob/main/science/timing_precision.md) adds an observation distinction. A supplied known systematic displacement preserves pure conditional records and permits quadratic global precision through the appropriate plain/pulsed menu when the interior-contact allowance is linear in the horizon. Learning an unknown displacement is not included. Hidden independent two-point jitter instead mixes two odd-branch operations that parity does not distinguish. At fixed nonzero jitter, that specified menu has inverse-linear global risk even though its pointwise classical score Fisher information at compensation can be quadratic. An accuracy scale $`d=O(h/\sqrt n)`$ is necessary for quadratic global precision when $`m=\Theta(n)`$; sufficiency is unproved.

These conclusions belong to their stated menus. Extra pulses, observed timing errors, selectable couplings or retuned compensation would change the resources. The companion's headline controlled-process discrimination law has a different task and proof; global sensing is an additional explicit-device consequence, not a reciprocal of a discrimination distance. Sharing the anchor and estimation lemma makes the connection teachable while preserving that distinction.
