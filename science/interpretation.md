# Scientific synthesis

[Overview](../README.md) · [Model](model.md) · [Attribution](../references/RELATED_WORK.md)

## The question and the contribution

Does a stable but continuously unknown error direction impose a fundamental precision cost, even when each known direction is individually correctable? If so, which additional control removes that cost without calibrating the direction?

For one sensor with Hamiltonian $`H=\omega Z/2`$ and transverse Lindblad operator $`L=\sqrt\gamma(\cos\phi X+\sin\phi Y)`$, the answer depends on access to the scalar rate. The fixed-rate and rate-diverse experiments permit the same parameter-independent ancillary control and ideal measurements. The direction remains common and unknown. Two distinct strictly positive rates constitute the additional resource; neither a noise-free setting nor an unknown-axis coherent drive is supplied.

The central scientific statement is a change in the optimal precision law. It is established both for nuisance-adjusted local information and for global worst-case mean-square error over a fixed bounded frequency interval. Preset protocols attain the local coefficient. A monitored stopped protocol implements an exact nuisance-independent quantum channel and supplies the global upper bound.

## Claim and proof map

| Result | Precise statement | Authoritative derivation |
|---|---|---|
| Fixed-rate limitation | Local information is at most $`T/\gamma`$, with tight leading coefficient $`1/\gamma`$ | [Theorems 1 and converse](precision_bounds.md) |
| Rate-diverse local optimum | Leading coefficient is $`r^2`$, with $`r=(b-a)/(b+a)`$ | [Theorem 2](precision_bounds.md) and [preset likelihoods](preset_protocols.md) |
| Selectable-setting criterion | A positive quadratic coefficient exists exactly when the known ratios $`s_j/\gamma_j`$ differ | [Theorem 3](precision_bounds.md) |
| Global precision separation | Minimax risk is $`\Theta(T^{-1})`$ at fixed rate and $`\Theta(T^{-2})`$ with rate access | [Global-risk theorem](global_precision.md) |
| Exact sensing operation | Each completed stop at signed time $`d`$ realizes $`e^{-i\omega dZ_L/2}`$ independently of $`\phi`$ | [Stopped sensing](stopped_sensing.md) |
| Charged timing | Exact first-passage transform, finite mean $`d/r`$, exponential tails, and hard-deadline accounting | [Stopped sensing](stopped_sensing.md) |
| Calibration distinction | A balanced echo is sensitive to differential imbalance; a fair recorded rate choice retains at least half the optimal local coefficient without numerical rate calibration | [Preset protocols](preset_protocols.md) |
| Shared-direction boundary | Independently unknown setting directions obey a linear-information converse | [Independent-axis bound](precision_bounds.md#independent-setting-dependent-directions) |
| Finite-cadence result | Ideal measurements at fixed intervals retain a positive quadratic local coefficient at a compensated operating point | [Physical scope](physical_scope.md#finite-interval-ideal-parity-measurements) |
| Residual parallel noise | A positive parallel rate restores a linear ceiling, while a quantified finite-time rate-diversity advantage remains | [Residual dephasing](residual_dephasing.md) |

## Two mechanisms, not two versions of the same guarantee

**Statistical separation.** Fixed recovery $`X`$ after every detected transverse error produces the phase $`\omega T-2\phi N`$. One rate makes the leading frequency and direction scores nearly parallel. Rate diversity separates their directions. Average the complete labelled Fisher matrices before eliminating the common nuisance; the reverse order would describe a different statistical problem. The rate-selection probabilities and every repetition have their stated physical costs. Quadratic local information does not, by itself, resolve global phase ambiguity.

**Exact channel cancellation.** Leave the errors uncorrected. Since $`N_\phi^2=I`$ and $`N_\phi ZN_\phi=-Z`$, the syndrome records a signed signal clock. Increasing the rate in the error sector gives that clock positive drift. Stopping at a prescribed signed time cancels the unknown error on every completed trajectory. Its waiting-time distribution, rather than an uncharged success condition, determines the physical cost. At equal rates the mean first-passage time is infinite, consistently with the fixed-rate obstruction.

These mechanisms support one resource distinction. Rate feedback is sufficient for the exact stopped channel, but is not necessary for the leading local optimum. The latter should not be described as an intrinsically syndrome-conditioned bath-control effect.

## The upper-bound chain

Along the mathematical nuisance path $`(\omega,\phi)=(\omega_c+u,\phi_c+cu)`$, the inherited adaptive channel-growth bound has zero-gauge coefficients

```math
A_j=c^2\gamma_j I,
\qquad B_j=(s_j/2-c\gamma_j)Z.
```

At one rate, a single $`c`$ cancels every coherent contribution. With a common direction and distinct signal-to-rate ratios, no such cancellation is possible across the settings. Minimizing the worst residual gives the pairwise optimum proved in Theorem 3. The explicit local constructions attain it. Applying the uniform path bounds to a compact smooth prior gives the global minimax lower bounds without assuming unbiasedness. The multiscale stopped-channel schedule gives the global upper scaling.

The channel inequality, nuisance-parameter projection, statistical design, van Trees argument, and multiscale phase-estimation technique are inherited tools. The particular obstruction, controlled removal, matching coefficient, and fully costed stopped operation are the combined results proved here. The [primary-source comparison](../references/RELATED_WORK.md) makes those attribution boundaries explicit.

## Physical interpretation and assumptions

A scalar rate knob can represent changing the intensity of one fixed noisy coupling or the arrival rate of unobserved identical collisions. The illustrative constructions preserve the same unknown operator. They are not a demonstration of the complete protocol in a device. Signal changes, coherent access, additional baths, and finite monitoring have to be assessed in their actual access model.

Known system pulses do not silently provide independent control of an unknown signal coupling. For example, conjugation by $`X`$ flips $`Z`$ but also maps $`N_\phi`$ to $`N_{-\phi}`$. It therefore does not implement the selectable pair $`(s,\gamma)=(1,\gamma),(-1,\gamma)`$ while preserving the same arbitrary unknown direction. Such conjugated controls are already included in the converse.

The physically essential assumptions are a common stable transverse direction, a specified signal response under the rate knob, and ideal ancillary measurement/control in the principal theorem. Known setting-dependent Hamiltonian offsets can be compensated. If instead every setting has a free unknown additive frequency offset $`\delta_j`$, the family $`H_j=(s_j\omega+\delta_j)Z/2`$ is invariant under $`\omega\mapsto\omega+u`$, $`\delta_j\mapsto\delta_j-s_ju`$; the target is then unidentifiable without another constraint. That is a different statistical model, not a small uncharged calibration error.

Strict asymptotic quadratic scaling also excludes an uncorrectable parallel error of fixed positive strength. Its explicit linear ceiling and finite-time advantage window are included rather than hidden behind a robustness claim. No assertion of general fault tolerance, arbitrary unknown-noise correction, or optimal global constant is made.

## Evidence and use

The proof files contain the complete analytic chain. The [reproducibility guide](../verification/README.md) maps finite identities and numerical cross-checks to executable tests; the [deterministic evidence table](../results/evidence.json) supplies reproducible examples without external data. This synthesis is a map of scientific results and their scope, not a substitute for those proofs or an independent expert endorsement.
