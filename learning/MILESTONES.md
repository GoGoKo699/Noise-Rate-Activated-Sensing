# Project understanding map: 30 milestones

This map defines exactly **30 milestones** for understanding noise-rate-activated sensing. It is defined by the scientific project and shared by every reader, including an LLM. It records conceptual targets and dependencies, not assessments or personal progress.

The allocation is **13 background/preliminaries milestones** and **17 narrative/innovation milestones**. The background joins open-system dynamics, recorded instruments, nuisance statistics and physical resource accounting. The narrative leads through the principal finite-strength global separation, then uses the separately proved Markovian results to explain the mechanism and the companion results to identify the limits of boundary-only access.

The single educational anchor shared with **Markovian Resolution Limit** is **Ángel Rivas and Susana F. Huelga, _Open Quantum Systems: An Introduction_, arXiv:1104.5242v2**. The [anchor bridge](ANCHOR.md) supplies the selective source map and notation translations. It supplies common foundations, not the global estimation theorem or the full controlled-process formalism. Those connections are taught in the [worked tutorial](TUTORIAL.md) and justified in the topic-based proof files. Primary research dependencies remain research citations rather than additional educational anchors.

## Route through the project

| Phase | Milestones | Connection established |
|---|---|---|
| Background/preliminaries | M01–M08 | States, microscopic evolution, channels, generators, instruments and parity encoding |
| Background/preliminaries | M09–M13 | Shared nuisance, local information, global risk and the complete resource comparison |
| Narrative/innovation | M14–M17 | Exact finite-strength instrument, fixed-band calibration and adaptive global converses |
| Narrative/innovation | M18–M22 | Direction cancellation, uniform record gates and a fully charged global estimator |
| Narrative/innovation | M23–M26 | Markovian obstruction, local rate diversity, exact stopped sensing and global counterpart |
| Narrative/innovation | M27–M30 | Temporal access, timing information, attribution and the complete scientific meaning |

The two repositories use the same foundational text but retain distinct project-specific milestone maps. Here the central question concerns choosing the strength of one noisy coupling. The companion's central question concerns temporal resolution of bounded microscopic dynamics. Each prerequisite below points to an earlier milestone; M13 and M30 integrate their respective phases.

## Phase I: background and preliminaries

### M01 States, outcomes and a protected reference

**Central question.** Which state determines the observable data when a sensor has both an environment and an ancilla?

**Understanding target.** Distinguish the exposed sensor, inaccessible bath and protected reference. Interpret density operators, partial traces and Born probabilities, including a sensor entangled with its reference.

**Prerequisites.** None within this map.

**Story role.** This fixes the physical systems and observations used by every protocol and converse.

**Conceptual connection.** Protected memory can preserve correlations and records without becoming a second exposed signal generator or an accessible bath.

**Canonical sources.** [Rivas–Huelga, §§3–4.1](ANCHOR.md#source-map); [one-qubit likelihood](TUTORIAL.md#1-one-qubit-one-likelihood-one-clock); [allowed operations](../science/model.md#allowed-operations).

### M02 Frequency, unitary evolution and fixed compensation

**Central question.** How does an unknown frequency enter the microscopic dynamics?

**Understanding target.** Relate $`H=\omega Z/2`$ to the phase rotation $`e^{-i\omega tZ/2}`$. Interpret the residual frequency $`\epsilon=\omega-\omega_0`$ when the physical compensation $`\omega_0`$ is fixed.

**Prerequisites.** [M01](#m01-states-outcomes-and-a-protected-reference)

**Story role.** This identifies the target and the Hamiltonian convention before introducing noise.

**Conceptual connection.** An estimate changes the controller's information. It does not change the compensating Hamiltonian unless the access model explicitly supplies that action.

**Canonical sources.** [Rivas–Huelga, §3](ANCHOR.md#source-map); [notation and resources](ANCHOR.md#notation-and-resource-conventions); [microscopic hardware](../science/microscopic_sensing.md#one-shared-interaction-and-a-fixed-measurement-clock).

### M03 Reduced channels and microscopic dilations

**Central question.** What does a channel specify, and what additional structure does its dilation retain?

**Understanding target.** Connect a completely positive trace-preserving map, its Kraus operators and a joint unitary with an initially independent bath. Keep equality valid on inputs entangled with a private reference.

**Prerequisites.** [M01](#m01-states-outcomes-and-a-protected-reference), [M02](#m02-frequency-unitary-evolution-and-fixed-compensation)

**Story role.** This supplies the language for deriving an exact collision channel.

**Conceptual connection.** Equal endpoint channels need not imply equal responses to interventions during the joint interaction. Tracing an inaccessible spent bath is an analytical operation, not a physical reset.

**Canonical sources.** [Rivas–Huelga, §§4.1–4.2](ANCHOR.md#source-map); [exact collision instrument](../science/microscopic_sensing.md#exact-parity-conditioned-cell-channel); [companion controlled-process distinction](https://github.com/GoGoKo699/Markovian-Resolution-Limit/blob/main/science/interpretation.md#a-decay-curve-does-not-specify-a-controlled-process).

### M04 Instruments and complete experimental records

**Central question.** How are a recorded outcome and the quantum state left after it described together?

**Understanding target.** Treat each measurement outcome as a completely positive branch map with its probability in its trace. Keep setting labels, parity outcomes, terminal measurements and failure flags in the complete experiment.

**Prerequisites.** [M03](#m03-reduced-channels-and-microscopic-dilations)

**Story role.** This defines the data available to feedback and estimation.

**Conceptual connection.** Conditioning on an observed record is legitimate analysis of a labelled experiment; discarding its probability or charging only successful records changes the task.

**Canonical sources.** [Channel background and the locally supplied instrument bridge](ANCHOR.md#what-is-supplied-locally); [allowed operations](../science/model.md#allowed-operations); [microscopic resources](../science/microscopic_global_precision.md#statistical-task-and-resources).

### M05 Generators, Markov approximations and rate normalization

**Central question.** How does a reduced noise law relate to its microscopic realization?

**Understanding target.** Connect a Lindblad generator to its semigroup and distinguish a microscopic approximation from an exact finite-duration collision. Separate the coefficient of a dissipator from the resulting coherence-decay rate.

**Prerequisites.** [M02](#m02-frequency-unitary-evolution-and-fixed-compensation), [M03](#m03-reduced-channels-and-microscopic-dilations), [M04](#m04-instruments-and-complete-experimental-records)

**Story role.** This keeps the Markovian and finite-strength theorems in their respective models.

**Conceptual connection.** For $`\kappa(Z\rho Z-\rho)`$, the coherence decays as $`e^{-2\kappa t}`$. A weak-coupling identification of parameters does not transfer a global estimator or an adaptive converse for free.

**Canonical sources.** [Rivas–Huelga, §§5.2 and 6](ANCHOR.md#source-map); [rate normalization](ANCHOR.md#rate-normalization); [physical realization and scope](../science/physical_scope.md).

### M06 Physical time, collision clocks and counted contacts

**Central question.** Which resources are fixed and which actions consume the experimental budget?

**Understanding target.** Charge every cell, repetition, calibration attempt and failed record to the hard horizon $`T=nh`$. Distinguish boundary instruments from contacts inside a cell, and count an early readout even when its result is stored afterward.

**Prerequisites.** [M04](#m04-instruments-and-complete-experimental-records), [M05](#m05-generators-markov-approximations-and-rate-normalization)

**Story role.** This supplies the common accounting needed to compare attainable errors.

**Conceptual connection.** A boundary may combine several operations into one instrument, but moving it inside a collision changes physical access. No protocol gains free time by finishing early.

**Canonical sources.** [Statistical task and resources](../science/microscopic_global_precision.md#statistical-task-and-resources); [charged calibration](../science/microscopic_identifiability.md#every-calibration-cell-and-readout-is-charged); [continuous-time accounting](../science/model.md#charged-time-and-failures).

### M07 A shared continuous error direction

**Central question.** Which features of an unknown error operator are known and usable?

**Understanding target.** Explain $`N_\phi=\cos\phi X+\sin\phi Y`$, $`N_\phi^2=I`$ and $`N_\phi ZN_\phi=-Z`$. The same arbitrary continuous angle is shared across settings and repeated trials.

**Prerequisites.** [M02](#m02-frequency-unitary-evolution-and-fixed-compensation), [M05](#m05-generators-markov-approximations-and-rate-normalization)

**Story role.** This identifies the structural promise behind the obstruction and its removal.

**Conceptual connection.** Knowing the error family differs from knowing its direction. Two identical flips undo the unknown axis, while their intervening signal rotation changes sign.

**Canonical sources.** [Parameters and normalization](../science/model.md#parameters-and-normalization); [transverse error algebra](TUTORIAL.md#2-detect-an-error-without-reading-the-signal); [shared microscopic interaction](../science/microscopic_sensing.md#one-shared-interaction-and-a-fixed-measurement-clock).

### M08 Parity encoding without reading the signal

**Central question.** How can the controller observe an error without measuring the logical phase?

**Understanding target.** Track the even code sector and odd error sector of a sensor–ancilla encoding. Explain why parity identifies the sector while preserving the unknown logical amplitudes.

**Prerequisites.** [M04](#m04-instruments-and-complete-experimental-records), [M06](#m06-physical-time-collision-clocks-and-counted-contacts), [M07](#m07-a-shared-continuous-error-direction)

**Story role.** This constructs the system-side record used by both coupling selection and phase readout.

**Conceptual connection.** The syndrome comes from a permitted system–memory instrument. Direct observation of bath outputs would be a different resource.

**Canonical sources.** [Worked parity encoding](TUTORIAL.md#2-detect-an-error-without-reading-the-signal); [exact parity-conditioned channel](../science/microscopic_sensing.md#exact-parity-conditioned-cell-channel); [instrument background](ANCHOR.md#what-is-supplied-locally).

### M09 Likelihood scores and local information

**Central question.** What does Fisher information measure about an actual recorded experiment?

**Understanding target.** Interpret a likelihood derivative as a score and its second moment as local distinguishability. Include the parameter dependence of every retained record, not only the final phase measurement.

**Prerequisites.** [M04](#m04-instruments-and-complete-experimental-records), [M08](#m08-parity-encoding-without-reading-the-signal)

**Story role.** This introduces the statistical tool used in the converses and local companion results.

**Conceptual connection.** A steep phase fringe gives local sensitivity but does not identify which fringe produced an outcome. Information alone is not the error of a global estimator.

**Canonical sources.** [Scores and Fisher matrices](TUTORIAL.md#3-why-a-nuisance-parameter-costs-information); [local and global distinction](../science/interpretation.md); [statistical bridge](ANCHOR.md#what-is-supplied-locally).

### M10 Shared nuisance and efficient information

**Central question.** Which apparent frequency sensitivity remains useful when the error angle is unknown?

**Understanding target.** Project the target score away from the nuisance score. Pool the full Fisher matrices of labelled experiments before eliminating their common nuisance, and distinguish this from using the target diagonal entry alone.

**Prerequisites.** [M07](#m07-a-shared-continuous-error-direction), [M09](#m09-likelihood-scores-and-local-information)

**Story role.** This explains the nuisance-induced precision obstruction.

**Conceptual connection.** Rate labels can separate two score directions even when the labels themselves contain no information about frequency. Giving each setting an independent unknown axis defines a different model.

**Canonical sources.** [Information with a nuisance](../science/model.md#information-in-the-presence-of-a-nuisance); [worked projection](TUTORIAL.md#3-why-a-nuisance-parameter-costs-information); [independent setting directions](../science/precision_bounds.md#independent-setting-dependent-directions).

### M11 Adaptive strategies and converse bounds

**Central question.** How can a bound constrain controls and learning procedures that have not been explicitly constructed?

**Understanding target.** Separate a measurement's Fisher information, an output-state quantum information bound and a bound for every permitted adaptive strategy. Interpret a joint frequency–nuisance path as a mathematical submodel with the same fixed controller.

**Prerequisites.** [M06](#m06-physical-time-collision-clocks-and-counted-contacts), [M10](#m10-shared-nuisance-and-efficient-information)

**Story role.** This distinguishes a limitation of one recovery from a model-wide obstruction.

**Conceptual connection.** Learning the nuisance does not evade a converse that already allows outcome-dependent controls. The proof's nuisance path is not a physical claim that the bath tracks the unknown frequency.

**Canonical sources.** [Nuisance-path argument](../science/model.md#the-nuisance-path-argument); [inherited channel bound](../science/precision_bounds.md#the-inherited-channel-bound); [general bound comparisons](../references/RELATED_WORK.md#non-markovian-correction-and-controlled-process-metrology).

### M12 Identifiability and global estimation risk

**Central question.** What makes a frequency estimate accurate over an entire fixed interval?

**Understanding target.** Define worst-case mean-square error over a nonshrinking frequency band and the shared nuisance. Distinguish identifiability, local sensitivity and an estimator's global risk; allow biased estimators and retain localization failures.

**Prerequisites.** [M09](#m09-likelihood-scores-and-local-information), [M11](#m11-adaptive-strategies-and-converse-bounds)

**Story role.** This establishes the principal comparison metric.

**Conceptual connection.** A smooth prior on a difficult subfamily yields a minimax lower bound without being a promise supplied to the controller. Phase ambiguity requires a separate attaining construction.

**Canonical sources.** [Microscopic statistical task](../science/microscopic_global_precision.md#statistical-task-and-resources); [fixed-band identification](../science/microscopic_identifiability.md); [global-risk distinction](TUTORIAL.md#8-global-precision-is-a-separate-statement).

### M13 The complete strength-control comparison

**Central question.** What changes when the controller receives a menu of two positive couplings?

**Understanding target.** State the fixed clock, nominal compensation, distinct positive couplings, common unknown axis, accessible records and boundary-only control class. Every fixed-coupling trial uses the same chosen coupling; all trials and contacts are charged.

**Prerequisites.** [M06](#m06-physical-time-collision-clocks-and-counted-contacts), [M08](#m08-parity-encoding-without-reading-the-signal), [M10](#m10-shared-nuisance-and-efficient-information), [M12](#m12-identifiability-and-global-estimation-risk)

**Story role.** This assembles the background into the principal finite-strength task.

**Conceptual connection.** Classical selection between two fixed strengths is the additional resource. Weakening the coupling with the budget, turning noise off, accessing the bath or retuning compensation is not included.

**Canonical sources.** [Statistical task and resources](../science/microscopic_global_precision.md#statistical-task-and-resources); [principal scientific argument](../science/interpretation.md#principal-argument-and-supporting-results).

## Phase II: narrative and innovation

### M14 The exact finite-strength collision instrument

**Central question.** What quantum operation and probability does each parity outcome produce during a real collision?

**Understanding target.** Derive $`K_0=aI-ibZ`$ and $`K_1=-icN_\phi`$ from simultaneous signal and bath coupling. Normalize the no-flip branch to a known frequency-dependent rotation and retain the exact flip probability.

**Prerequisites.** [M13](#m13-the-complete-strength-control-comparison)

**Story role.** This begins the principal argument directly from microscopic dynamics.

**Conceptual connection.** No small-cell approximation or operating-point substitution is needed to identify the conditional instrument. Off-compensation records generally change their probabilities as well as their phases.

**Canonical sources.** [Exact parity-conditioned cell channel](../science/microscopic_sensing.md#exact-parity-conditioned-cell-channel); [bounded collision example](TUTORIAL.md#10-from-a-bounded-collision-to-an-observed-phase).

### M15 One fixed identifiable band and paid calibration

**Central question.** On which frequency interval can the same physical device support uniform identification and later refinement?

**Understanding target.** Use the nuisance-independent three-outcome experiment, a uniformly invertible mean signal and its concentration bound. Choose one sufficiently small positive-width band that also satisfies the later phase-gate conditions, independently of the budget.

**Prerequisites.** [M12](#m12-identifiability-and-global-estimation-risk), [M14](#m14-the-exact-finite-strength-collision-instrument)

**Story role.** This supplies a legitimate global domain and the estimator's charged initial localization.

**Conceptual connection.** A sufficient band is not a maximal bandwidth claim. Fixed-clock aliases obstruct broader promises, and localization does not retune the compensating Hamiltonian.

**Canonical sources.** [Exact calibration experiment](../science/microscopic_identifiability.md#an-exact-three-outcome-experiment); [risk and confidence](../science/microscopic_identifiability.md#repetition-risk-and-confidence); [common band](../science/microscopic_global_precision.md#one-fixed-band-for-both-designs).

### M16 A curved nuisance path at one fixed coupling

**Central question.** Why can no permitted adaptive boundary strategy recover quadratic information at a fixed coupling?

**Understanding target.** Follow the smooth frequency-dependent nuisance curve that cancels the physical Kraus derivative overlap throughout the band. Relate the remaining bounded squared derivative to a linear information bound for arbitrary protected-memory strategies.

**Prerequisites.** [M11](#m11-adaptive-strategies-and-converse-bounds), [M14](#m14-the-exact-finite-strength-collision-instrument)

**Story role.** This supplies the microscopic all-strategy obstruction.

**Conceptual connection.** Uniform positivity of the flip probability keeps the curve regular. The converse includes attempts to learn the direction, resets, setting-independent boundary controls and retained failures.

**Canonical sources.** [Fixed-coupling nuisance curve](../science/microscopic_global_precision.md#the-fixed-coupling-nuisance-curve); [local coefficient comparison](../science/microscopic_precision.md#the-optimal-fixed-coupling-coefficient).

### M17 Global lower bounds and operational limits

**Central question.** How does the uniform information obstruction become a risk statement for biased estimators and limiting controllers?

**Understanding target.** Apply a smooth fixed prior along the nuisance curve to obtain inverse-linear risk. Use a separate fixed-angle signal-generator bound for inverse-square risk with a menu. Pass global lower bounds through clipped, quantized loss and event-probability convergence.

**Prerequisites.** [M15](#m15-one-fixed-identifiable-band-and-paid-calibration), [M16](#m16-a-curved-nuisance-path-at-one-fixed-coupling)

**Story role.** This establishes the lower directions in the same global metric used for attainment.

**Conceptual connection.** The two lower bounds use different comparison paths. The direct bounded-loss closure does not assume continuity of Fisher information or enlarge the controller class.

**Canonical sources.** [Uniform bounds to risk](../science/microscopic_global_precision.md#from-uniform-information-bounds-to-risk-bounds); [global-risk closure](../science/microscopic_global_precision.md#global-risk-under-controlled-limits).

### M18 Exact cancellation in retained even records

**Central question.** How can two strengths produce useful signal while cancelling an arbitrary shared error direction?

**Understanding target.** Choose the weaker coupling in the even sector and the stronger in the odd sector. Pair the unknown-axis flips in an even-ending record and reconstruct its exact signed sum of known nonlinear no-flip phases.

**Prerequisites.** [M07](#m07-a-shared-continuous-error-direction), [M14](#m14-the-exact-finite-strength-collision-instrument)

**Story role.** This supplies the attaining mechanism that strength selection makes possible.

**Conceptual connection.** The complete observed record identifies a phase function; it is not replaced by an unobserved mixture or a prescribed noiseless Ramsey duration. The record law remains frequency dependent.

**Canonical sources.** [Retained even-parity construction](../science/microscopic_global_precision.md#attainment-with-retained-even-parity-records); [two-coupling explanation](TUTORIAL.md#11-what-two-couplings-change-globally).

### M19 A uniform gate for useful phase records

**Central question.** Which observed records have enough sensitivity everywhere on the promised band?

**Understanding target.** Use even endpoint parity and a threshold on the recorded frozen derivative to define acceptance without knowing the parameters. Combine positive drift, a controlled transient and a variance bound to obtain a uniform positive acceptance probability and a derivative proportional to block length for every accepted phase curve.

**Prerequisites.** [M15](#m15-one-fixed-identifiable-band-and-paid-calibration), [M18](#m18-exact-cancellation-in-retained-even-records)

**Story role.** This upgrades exact cancellation to a uniformly usable estimation resource.

**Conceptual connection.** Average drift alone is insufficient. The accepted record must certify sensitivity across the whole fixed interval, while rejected records retain their full physical cost.

**Canonical sources.** [Two-state parity gate](../science/recorded_phase_estimation.md#a-two-state-parity-gate); [uniform acceptance](../science/recorded_phase_estimation.md#uniform-acceptance-probability); [uniform sensitivity](../science/recorded_phase_estimation.md#uniform-phase-sensitivity-on-accepted-records).

### M20 Conditional inversion of the observed phase functions

**Central question.** How can an estimator use nonlinear phases when the distribution of those phases depends on frequency?

**Understanding target.** Condition on the actual records of freshly reset blocks. Choose each terminal quadrature relative to the current interval center, then invert the empirical average of the known conditional mean functions with clipping on that interval.

**Prerequisites.** [M09](#m09-likelihood-scores-and-local-information), [M19](#m19-a-uniform-gate-for-useful-phase-records)

**Story role.** This turns the retained quantum states into a valid statistical refinement step.

**Conceptual connection.** Conditional readout concentration does not freeze record probabilities. Within a stage the policy ignores preceding terminal bits, preserving the independence used by the proof; changing the readout basis does not change physical compensation.

**Canonical sources.** [One refinement](../science/recorded_phase_estimation.md#one-refinement); [conditional concentration](../science/recorded_phase_estimation.md#conditional-concentration); [recorded-function tutorial](TUTORIAL.md#12-resolve-ambiguity-with-the-recorded-functions).

### M21 Multiscale ambiguity resolution with a hard budget

**Central question.** How do local refinements give inverse-square worst-case error without a free success condition or logarithmic overhead?

**Understanding target.** Combine paid coarse localization, dyadic block lengths, tapered repetitions and nested confidence intervals. Bound the damage from the first failed stage and sum its contribution to mean-square error; charge every attempted block.

**Prerequisites.** [M17](#m17-global-lower-bounds-and-operational-limits), [M20](#m20-conditional-inversion-of-the-observed-phase-functions)

**Story role.** This supplies the global upper bound with deterministic total duration.

**Conceptual connection.** The largest feasible scale is proportional to the budget because the repetition taper has finite weighted cost. A long successful block alone would not resolve ambiguity or bound failed-run risk.

**Canonical sources.** [Nested multiscale estimation](../science/recorded_phase_estimation.md#nested-multiscale-estimation); [global risk and cost](../science/recorded_phase_estimation.md#global-risk-and-deterministic-cost); [inherited phase-estimation methods](../references/RELATED_WORK.md#phase-estimation-and-stopping-background).

### M22 The finite-strength global separation

**Central question.** What exact comparison follows after the converse and estimator are put under one resource convention?

**Understanding target.** State $`R_g^*(n)=\Theta(n^{-1})`$ at either fixed coupling and $`R_{\{g_a,g_b\}}^*(n)=\Theta(n^{-2})`$ for the two-strength menu, on the same fixed band uniformly over the unknown axis. Account for at most $`n-1`$ nonterminal boundary instruments and the full duration $`nh`$.

**Prerequisites.** [M17](#m17-global-lower-bounds-and-operational-limits), [M21](#m21-multiscale-ambiguity-resolution-with-a-hard-budget)

**Story role.** This completes the principal microscopic argument.

**Conceptual connection.** The fixed-coupling calibration estimator matches the inverse-linear lower order. The menu estimator matches the inverse-square generator ceiling. Neither global constant is identified with a sharp local coefficient.

**Canonical sources.** [Global precision theorem](../science/microscopic_global_precision.md#global-precision-theorem); [attainment and contact accounting](../science/microscopic_global_precision.md#attainment-with-retained-even-parity-records); [scope](../science/microscopic_global_precision.md#scope-of-the-separation).

### M23 The Markovian fixed-rate counterpart

**Central question.** How does the nuisance obstruction appear in an ideal continuous-time noise law?

**Understanding target.** Reconstruct the inherited fixed-recovery phase $`\omega T-2\phi N`$ and its nuisance-adjusted information $`T^2/(1+\gamma T)`$. Follow the independent all-strategy argument giving $`\mathcal I_\omega^*(T)\le T/\gamma`$ and the matching leading coefficient.

**Prerequisites.** [M10](#m10-shared-nuisance-and-efficient-information), [M16](#m16-a-curved-nuisance-path-at-one-fixed-coupling), [M22](#m22-the-finite-strength-global-separation)

**Story role.** This provides a transparent analytic counterpart to the microscopic obstruction.

**Conceptual connection.** Fixed recovery is an attributed attaining component, not the proof that every strategy is limited. The continuous-time converse is proved in its own control model.

**Canonical sources.** [Fixed-rate theorem](../science/precision_bounds.md#theorem-1--fixed-rate); [preset attainment](../science/precision_bounds.md#attainment-with-preset-controls); [closest prior model](../references/RELATED_WORK.md#closest-noise-model).

### M24 Preset rate diversity and the sharp local coefficient

**Central question.** Which rate choices remove the local nuisance penalty, and which choices need feedback or calibration?

**Understanding target.** Pool labelled experiments at two positive rates and recover the optimal coefficient $`[(b-a)/(b+a)]^2`$. Distinguish calibrated optimal design, a fair recorded choice and balanced echo; identify unequal signal-to-rate ratios as the broader selectable-setting criterion.

**Prerequisites.** [M23](#m23-the-markovian-fixed-rate-counterpart)

**Story role.** This separates local statistical design from the exact cancellation construction.

**Conceptual connection.** Preset rate selection can attain the leading local optimum even though recovery responds to detected errors. It does not implement a nuisance-independent quantum channel on each trajectory or prove global attainability by itself.

**Canonical sources.** [Controlled-rate and selectable-setting theorems](../science/precision_bounds.md); [preset protocols](../science/preset_protocols.md); [complete rate-diversity example](TUTORIAL.md#4-a-complete-rate-diversity-example).

### M25 Exact stopped sensing and charged random duration

**Central question.** Can the observed noise itself supply a direction-independent sensing operation?

**Understanding target.** Leave errors uncorrected, track the signed signal clock and stop at a prescribed positive signed time. Explain exact cancellation at completion, the positive drift from rate feedback, and the distinction between finite mean duration, tail control and a hard deadline.

**Prerequisites.** [M06](#m06-physical-time-collision-clocks-and-counted-contacts), [M18](#m18-exact-cancellation-in-retained-even-records), [M24](#m24-preset-rate-diversity-and-the-sharp-local-coefficient)

**Story role.** This supplies the exact operation used in the continuous-time global counterpart.

**Conceptual connection.** Equal rates give an infinite mean first-passage time. Eventual completion or conditioning on success cannot substitute for charged physical time and retained deadline failures.

**Canonical sources.** [Protocol and exact output](../science/stopped_sensing.md#protocol-and-exact-output); [first-passage law](../science/stopped_sensing.md#first-passage-law); [random-duration accounting](../science/stopped_sensing.md#charge-the-random-physical-durations).

### M26 The continuous-time global counterpart

**Central question.** How do the Markovian local and exact-channel results support their own global separation?

**Understanding target.** Combine uniform nuisance-path lower bounds, a paid fixed-rate estimator and a multiscale stopped-channel schedule to obtain inverse-linear versus inverse-quadratic risk at a hard time budget. Keep deadline failures and biased estimators in the comparison.

**Prerequisites.** [M17](#m17-global-lower-bounds-and-operational-limits), [M21](#m21-multiscale-ambiguity-resolution-with-a-hard-budget), [M25](#m25-exact-stopped-sensing-and-charged-random-duration)

**Story role.** This completes the separately proved Markovian explanation of the same resource distinction.

**Conceptual connection.** The stopped channel has a prescribed effective phase duration; microscopic blocks provide observed nonlinear phase functions instead. Each model needs its own attaining argument and cannot borrow global risk from a local information formula.

**Canonical sources.** [Global continuous-time theorem](../science/global_precision.md); [stopped global estimator](../science/stopped_sensing.md#global-estimation-on-a-bounded-interval); [two mechanisms](../science/interpretation.md#two-mechanisms-not-two-versions-of-the-same-guarantee).

### M27 Temporal access as a separate resource

**Central question.** What changes when the same fixed coupling becomes accessible inside collisions?

**Understanding target.** State the companion law $`R^*_{n,m}=\Theta([h^2(n+m^2)]^{-1})`$ with at most $`m`$ inside-cell contacts and $`n-1`$ total contacts. Identify the echoed/plain menu, charged frame corrections and early readout, and the hard activity budget in the adaptive converse.

**Prerequisites.** [M06](#m06-physical-time-collision-clocks-and-counted-contacts), [M22](#m22-the-finite-strength-global-separation), [M26](#m26-the-continuous-time-global-counterpart)

**Story role.** This locates the boundary-only separation within the sisters' common resource question.

**Conceptual connection.** The companion theorem uses the shared recorded-phase estimator but supplies a different physical instrument and converse. It neither weakens the boundary-only lower bound nor follows merely by taking a reciprocal local-information expression.

**Canonical sources.** [Companion global contact theorem](https://github.com/GoGoKo699/Markovian-Resolution-Limit/blob/main/science/global_contact_precision.md); [local contact comparison](../science/microscopic_precision.md#limited-access-inside-collision-cells); [strength and temporal access](TUTORIAL.md#13-separate-strength-control-from-temporal-access).

### M28 Known displacement and hidden timing jitter

**Central question.** Which timing information preserves an exact useful record, and which uncertainty changes the available channel?

**Understanding target.** Distinguish a supplied known fixed pulse displacement from independent unobserved two-point jitter. With a linear inside-cell contact allowance, the former retains quadratic global order on a sufficient fixed band; fixed nonzero hidden jitter gives inverse-linear global risk for the stated plain/one-pulse menu despite quadratic pointwise information at compensation.

**Prerequisites.** [M20](#m20-conditional-inversion-of-the-observed-phase-functions), [M27](#m27-temporal-access-as-a-separate-resource)

**Story role.** This supplies the principal limitation of the companion temporal construction.

**Conceptual connection.** The worst-case obstruction uses a prior away from compensation. The shrinking-jitter condition is necessary only; learning an unknown offset, supplying its hidden record or adding stronger control changes the problem.

**Canonical sources.** [Companion timing theorem](https://github.com/GoGoKo699/Markovian-Resolution-Limit/blob/main/science/timing_precision.md); [timing scope in the synthesis](../science/interpretation.md#physical-interpretation-and-assumptions).

### M29 Model boundaries, attribution and evidence

**Central question.** Which conclusions belong to the model, which to a construction, and which ingredients are inherited?

**Understanding target.** Keep shared-axis stability, fixed hardware, sufficient bandwidth, ideal instruments and protected memory explicit. Identify the general channel bounds, nuisance statistics and multiscale methods as inherited tools, and distinguish analytic theorems from finite numerical checks and expert judgment.

**Prerequisites.** [M23](#m23-the-markovian-fixed-rate-counterpart), [M26](#m26-the-continuous-time-global-counterpart), [M28](#m28-known-displacement-and-hidden-timing-jitter)

**Story role.** This prevents the combined story from becoming an unrestricted noise-correction or timing theorem.

**Conceptual connection.** A limitation of one echo or calibration procedure is not a universal impossibility. Conversely, independent setting directions or an uncorrectable parallel noise component can change the model's attainable law; those qualifications cannot be hidden in a robustness claim.

**Canonical sources.** [Claim-level attribution](../references/RELATED_WORK.md#contribution-boundary); [physical scope](../science/physical_scope.md); [parallel dephasing](../science/residual_dephasing.md); [verification limits](../verification/README.md).

### M30 The complete scientific story

**Central question.** What does noise-strength control enable when the frequency and continuous noise direction are initially unknown?

**Understanding target.** Reconstruct the fixed-strength global comparison from its exact instrument, identifiable band, nuisance-curve lower bounds and paid recorded-phase estimator. Explain the separately proved Markovian counterpart and the companion's distinct temporal-access and timing results without combining incompatible resource classes.

**Prerequisites.** [M22](#m22-the-finite-strength-global-separation), [M29](#m29-model-boundaries-attribution-and-evidence)

**Story role.** This integrates the full dependency chain into one defensible explanation of the paper and its relationship to its sister.

**Conceptual connection.** Noise strength and temporal access are different ways to change the experiment. Their consequences must be established through an attainable global risk law with the actual records and full resource costs, rather than inferred from a favorable local sensitivity.

**Canonical sources.** [Scientific synthesis](../science/interpretation.md); [principal global theorem](../science/microscopic_global_precision.md); [shared estimation lemma](../science/recorded_phase_estimation.md); [companion scientific story](https://github.com/GoGoKo699/Markovian-Resolution-Limit/blob/main/science/interpretation.md).
