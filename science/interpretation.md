# Scientific synthesis

[Overview](../README.md) · [Model](model.md) · [Attribution](../references/RELATED_WORK.md)

## The question and the contribution

Does a stable but continuously unknown error direction impose a fundamental precision cost, even when each known direction is individually correctable? If so, which additional control removes that cost without calibrating the direction?

The answer is a change in the optimal global precision law under scalar noise-strength control, proved separately for a finite-strength collision device and a Markovian model. Both comparisons retain a common unknown transverse direction and the same parameter-independent ancillary control within their respective models. The additional resource is a choice of two strictly positive strengths; neither a noise-free setting nor an unknown-axis coherent drive is supplied.

## Principal argument and supporting results

The [principal microscopic theorem](microscopic_global_precision.md) gives optimal worst-case risk $`\Theta(n^{-1})`$ at either one fixed positive coupling and $`\Theta(n^{-2})`$ with two couplings, on one suitable fixed, nonshrinking frequency band. The comparison is uniform over the shared continuous direction and covers every permitted adaptive boundary strategy. Both strengths, the clock and the physical compensation remain fixed as the budget grows.

The shortest sufficient argument has three steps. First, derive the exact collision instrument and a common identifiable band. Second, show that a smooth nuisance curve forces linear information at either fixed coupling and turn that uniform bound into a minimax risk obstruction. Third, use a parameter-independent gate to select even-parity records with uniformly increasing phase, then apply the [recorded-phase estimator](recorded_phase_estimation.md) with all localization and rejected trials charged. These steps establish both sides of one global comparison; no local-to-global reciprocal inference is needed.

The main exposition needs the instrument, the obstruction, the cancellation mechanism and the global theorem. The full record-gate estimates, multiscale concentration constants, operational-limit argument and sharp local coefficient calculations belong in supporting derivations. The Markovian stopped-channel theorem is a separately proved analytic counterpart; its exact timing transform, general selectable-setting criterion and residual-dephasing calculation support the physical interpretation. None is needed as an unproved approximation step in the microscopic result.

This repository owns the coupling comparison and the shared recorded-phase estimation lemma. The companion owns the controlled-process resolution law, the global contact-budget theorem and the timing-menu limitation. The common estimator is cited there as one shared method, not presented as a second independent contribution. Temporal access illustrates a different resource and does not enlarge this paper's boundary-only control class.

Ideal instruments, protected memory, a stable shared axis and a sufficient fixed band remain material assumptions. Unknown timing-offset calibration, sufficiency for shrinking random jitter, maximal bandwidth and finite-duration instruments require additional results beyond the stated comparison.

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
| Finite-cadence Markovian result | Ideal measurements at fixed intervals retain a positive quadratic local coefficient at a compensated operating point | [Physical scope](physical_scope.md#finite-interval-ideal-parity-measurements) |
| Finite-strength global separation | One fixed coupling gives inverse-cell-count risk, while a two-coupling menu gives inverse-square risk on a common fixed band | [Microscopic global precision](microscopic_global_precision.md) |
| Estimation from retained microscopic records | Uniformly usable nonlinear phase functions give quadratic global precision with paid calibration and ambiguity resolution | [Recorded-phase estimation](recorded_phase_estimation.md) |
| Temporal access at one fixed coupling | Global risk has order $`1/[h^2(n+m^2)]`$ under the stated total and inside-cell contact budgets | [Companion global contact theorem](https://github.com/GoGoKo699/Markovian-Resolution-Limit/blob/main/science/global_contact_precision.md) |
| Specified hidden timing noise | Fixed nonzero independent two-point jitter gives inverse-time global risk for a plain/jittered-one-pulse menu, even with quadratic local information at compensation | [Companion timing theorem](https://github.com/GoGoKo699/Markovian-Resolution-Limit/blob/main/science/timing_precision.md) |
| Residual parallel noise | A positive parallel rate restores a linear ceiling, while a quantified finite-time rate-diversity advantage remains | [Residual dephasing](residual_dephasing.md) |

## Two mechanisms, not two versions of the same guarantee

**Statistical separation.** Fixed recovery $`X`$ after every detected transverse error produces the phase $`\omega T-2\phi N`$. One rate makes the leading frequency and direction scores nearly parallel. Rate diversity separates their directions. Average the complete labelled Fisher matrices before eliminating the common nuisance; the reverse order would describe a different statistical problem. The rate-selection probabilities and every repetition have their stated physical costs. Quadratic local information does not, by itself, resolve global phase ambiguity.

**Exact channel cancellation.** Leave the errors uncorrected. Since $`N_\phi^2=I`$ and $`N_\phi ZN_\phi=-Z`$, the syndrome records a signed signal clock. Increasing the rate in the error sector gives that clock positive drift. Stopping at a prescribed signed time cancels the unknown error on every completed trajectory. Its waiting-time distribution, rather than an uncharged success condition, determines the physical cost. At equal rates the mean first-passage time is infinite, consistently with the fixed-rate obstruction.

These mechanisms support one resource distinction. Rate feedback is sufficient for the exact stopped channel, but is not necessary for the leading local optimum. The latter should not be described as an intrinsically syndrome-conditioned bath-control effect.

For the microscopic device, an even number of observed flips also cancels the direction exactly. Its record specifies a nonlinear phase function, rather than a noiseless Ramsey operation at a prescribed signed duration. The [global estimator](recorded_phase_estimation.md) retains these functions, certifies their sensitivity over an entire fixed band, and measures each output relative to the phase predicted at the current classical interval center. Conditional concentration and nested intervals resolve ambiguity. This changes only terminal measurement bases; the signal Hamiltonian and nominal compensation are unchanged. Averaging the records into an unobserved mixture would describe a different experiment.

## The upper-bound chain

Along the mathematical nuisance path $`(\omega,\phi)=(\omega_c+u,\phi_c+cu)`$, the inherited adaptive channel-growth bound has zero-gauge coefficients

```math
A_j=c^2\gamma_j I,
\qquad B_j=(s_j/2-c\gamma_j)Z.
```

At one rate, a single $`c`$ cancels every coherent contribution. With a common direction and distinct signal-to-rate ratios, no such cancellation is possible across the settings. Minimizing the worst residual gives the pairwise optimum proved in Theorem 3. The explicit local constructions attain it. Applying the uniform path bounds to a compact smooth prior gives the global minimax lower bounds without assuming unbiasedness. The multiscale stopped-channel schedule gives the global upper scaling.

The channel inequality, nuisance-parameter projection, statistical design, van Trees argument, and multiscale phase-estimation technique are inherited tools. The particular obstruction, controlled removal, matching coefficient, and fully costed stopped operation are the combined results proved here. The [primary-source comparison](../references/RELATED_WORK.md) makes those attribution boundaries explicit.

The finite-strength counterpart uses a [smooth nuisance curve for the exact Kraus operators](microscopic_global_precision.md#the-fixed-coupling-nuisance-curve), rather than the continuous-time coefficients above. Its global constants are not identified with the sharp local coefficients.

## Physical interpretation and assumptions

A scalar rate knob can represent changing the intensity of one fixed noisy coupling or the arrival rate of unobserved identical collisions. The illustrative constructions preserve the same unknown operator. They are not a demonstration of the complete protocol in a device. Signal changes, coherent access, additional baths, and finite monitoring have to be assessed in their actual access model.

Known system pulses do not silently provide independent control of an unknown signal coupling. For example, conjugation by $`X`$ flips $`Z`$ but also maps $`N_\phi`$ to $`N_{-\phi}`$. It therefore does not implement the selectable pair $`(s,\gamma)=(1,\gamma),(-1,\gamma)`$ while preserving the same arbitrary unknown direction. Such conjugated controls are already included in the converse.

The physically essential assumptions are a common stable transverse direction, a specified signal response under the rate knob, and ideal ancillary measurement/control in the principal theorem. Known setting-dependent Hamiltonian offsets can be compensated. If instead every setting has a free unknown additive frequency offset $`\delta_j`$, the family $`H_j=(s_j\omega+\delta_j)Z/2`$ is invariant under $`\omega\mapsto\omega+u`$, $`\delta_j\mapsto\delta_j-s_ju`$; the target is then unidentifiable without another constraint. That is a different statistical model, not a small uncharged calibration error.

Strict asymptotic quadratic scaling also excludes an uncorrectable parallel error of fixed positive strength. Its explicit linear ceiling and finite-time advantage window are included rather than hidden behind a robustness claim. No assertion of general fault tolerance, arbitrary unknown-noise correction, or optimal global constant is made.

For the collision device, temporal access is an additional resource. The companion [global contact theorem](https://github.com/GoGoKo699/Markovian-Resolution-Limit/blob/main/science/global_contact_precision.md) allows at most $`m`$ contacts inside cells within $`n-1`$ total contacts. A menu of echoed and untouched cells attains the matching global law on a fixed band, while a nuisance-curve activity bound limits every permitted adaptive controller. This does not change the boundary-only coupling comparison.

Timing errors require a specified observation model. In the companion [plain/pulsed-cell analysis](https://github.com/GoGoKo699/Markovian-Resolution-Limit/blob/main/science/timing_precision.md), a supplied known fixed displacement preserves usable exact phase records and quadratic global order when the inside-cell allowance is linear in the horizon. No procedure for learning an unknown displacement is included. Unobserved independent two-point jitter mixes distinct odd-parity operations; the stated plain/jittered-one-pulse menu then has only inverse-time global precision at fixed nonzero jitter, even though its compensated local information can remain quadratic. That converse is restricted to the given menu. It does not cover additional interior pulses, recorded timing errors, selectable couplings or retuned compensation.

## Evidence and use

The proof files contain the complete analytic chain. The [reproducibility guide](../verification/README.md) maps finite identities and numerical cross-checks to executable tests; the [deterministic evidence table](../results/evidence.json) supplies reproducible examples without external data. This synthesis is a map of scientific results and their scope, not a substitute for those proofs or an independent expert endorsement.
