# Project understanding map: 30 milestones

This map defines exactly **30 milestones** for understanding noise-rate-activated sensing. It depends on the scientific project, not on a particular reader’s prior knowledge, and is shared by every reader, including an LLM. It records conceptual targets and scientific dependencies, not assessments or personal progress.

The allocation is **13 background/preliminaries milestones** and **17 narrative/innovation milestones**. The background needs room to connect qubit evolution, open-system dynamics, nuisance statistics, and charged random times before defining the complete task. The narrative then connects the universal obstruction, two different sensing mechanisms, optimal local information, global risk, and physical boundaries. Both phases progress from local objects or arguments to an integrated account.

The sole educational anchor is **Haase et al., _Precision Limits in Quantum Metrology with Open Quantum Systems_, arXiv:1807.11882v4**. The [Haase bridge](HAASE_BRIDGE.md) owns the selective source map and notation translations. The [worked tutorial](TUTORIAL.md) supplies examples; the topic-based scientific pages remain authoritative for exact claims and proofs. Primary research dependencies are not additional educational anchors.

## Route through the project

| Phase | Milestones | Connection established |
|---|---|---|
| Background/preliminaries | M01–M07 | Sensor evolution, noise algebra, parity encoding, and complete records |
| Background/preliminaries | M08–M13 | Nuisance information, strategy bounds, timing, and the complete local/global task |
| Narrative/innovation | M14–M19 | Fixed-rate converse, rate-diverse local optimum, and calibration tradeoffs |
| Narrative/innovation | M20–M23 | Exact trajectory cancellation and fully charged stopped sensing |
| Narrative/innovation | M24–M28 | Same-metric global separation and consequential physical boundaries |
| Narrative/innovation | M29–M30 | Attribution, evidence, and the complete scientific meaning |

Together these targets support global understanding of the project, not exhaustive mastery of every calculation or neighboring subject. Each prerequisite below refers to an earlier milestone; the final milestone integrates the full dependency chain.

## Phase I: background and preliminaries

### M01 Qubit states and recorded outcomes

**Central question.** What physical object carries the signal, and what does its measurement report?

**Understanding target.** Interpret a normalized qubit state, a density operator, and a two-outcome measurement. Connect Born probabilities to recorded data without treating a probability or a quantum state as one observed outcome.

**Prerequisites.** None within this map.

**Story role.** This establishes the physical input and output used by every sensing protocol.

**Conceptual connection.** A quantum preparation determines a distribution of classical records; it does not supply the unknown frequency as a readable label.

**Canonical sources.** [Haase §II](HAASE_BRIDGE.md#source-map); [Ramsey probabilities](TUTORIAL.md#1-one-qubit-one-likelihood-one-clock).

### M02 Frequency and coherent phase accumulation

**Central question.** How does an unknown frequency enter a qubit experiment?

**Understanding target.** Read the Hamiltonian $`H=\omega Z/2`$ and the rotation $`e^{-i\omega tZ/2}`$. Distinguish a frequency, its dimensionless accumulated phase, and the transverse noise angle.

**Prerequisites.** [M01](#m01-qubit-states-and-recorded-outcomes)

**Story role.** This identifies the target parameter before noise or statistical bounds are introduced.

**Conceptual connection.** The factor of one half fixes the noiseless information scale; copying a different Hamiltonian convention changes numerical constants.

**Canonical sources.** [Haase notation translation](HAASE_BRIDGE.md#translate-the-notation-and-the-task); [parameter normalization](../science/model.md#parameters-and-normalization).

### M03 Interrogation and the physical time budget

**Central question.** Which experimental actions contribute to the sensing budget?

**Understanding target.** Distinguish one coherent interrogation from repeated shorter trials. Count the duration of every trial and distinguish exposed sensor time from noiseless ancillary storage.

**Prerequisites.** [M02](#m02-frequency-and-coherent-phase-accumulation)

**Story role.** This supplies the common resource unit for later comparisons.

**Conceptual connection.** Information adds across independent trials, but so does their exposure. Changing probe number is not the same as increasing one sensor’s time budget.

**Canonical sources.** [Haase §II.A–C](HAASE_BRIDGE.md#source-map); [charged time](../science/model.md#charged-time-and-failures); [repeated Ramsey trials](TUTORIAL.md#1-one-qubit-one-likelihood-one-clock).

### M04 Markovian noise and rate normalization

**Central question.** What does a Lindblad rate specify about the sensor’s evolution?

**Understanding target.** Connect a channel, its continuous-time generator, and a jump operator. Separate the coefficient of a dissipator from the resulting coherence-decay rate.

**Prerequisites.** [M01](#m01-qubit-states-and-recorded-outcomes), [M02](#m02-frequency-and-coherent-phase-accumulation)

**Story role.** This defines the noise dynamics before discussing correction.

**Conceptual connection.** For the stated Pauli convention, parallel dephasing with coefficient $`\kappa`$ has contrast $`e^{-2\kappa t}`$. Equal symbols across sources need not denote equal rates.

**Canonical sources.** [Haase §III](HAASE_BRIDGE.md#source-map); [source normalization](HAASE_BRIDGE.md#rate-normalization-when-using-the-source); [generator](../science/model.md#parameters-and-normalization).

### M05 The algebra of an unknown transverse error

**Central question.** Which properties of the error remain available without knowing its direction?

**Understanding target.** Explain $`N_\phi^2=I`$ and $`N_\phi ZN_\phi=-Z`$ for a fixed transverse Pauli direction. Separate structural knowledge of the error family from calibration of its continuous angle.

**Prerequisites.** [M02](#m02-frequency-and-coherent-phase-accumulation), [M04](#m04-markovian-noise-and-rate-normalization)

**Story role.** This isolates the algebra that later permits both recovery and exact cancellation.

**Conceptual connection.** Two identical errors undo each other, but the signal changes sign between them. A continuously unknown direction is not a finite list of known alternatives.

**Canonical sources.** [Transverse error and code](TUTORIAL.md#2-detect-an-error-without-reading-the-signal); [parameter family](../science/model.md#parameters-and-normalization).

### M06 A noiseless ancilla and parity encoding

**Central question.** How can an error be detected without reading the signal phase?

**Understanding target.** Track the logical amplitudes in the even-parity code and in the odd error sector. Explain why measuring parity reveals the sector without distinguishing the logical basis amplitudes.

**Prerequisites.** [M01](#m01-qubit-states-and-recorded-outcomes), [M05](#m05-the-algebra-of-an-unknown-transverse-error)

**Story role.** This constructs the system-side syndrome measurement used by the protocols.

**Conceptual connection.** The ancilla helps preserve and read the logical state but does not contribute another exposed signal generator.

**Canonical sources.** [Haase §VI.B](HAASE_BRIDGE.md#source-map); [worked parity encoding](TUTORIAL.md#2-detect-an-error-without-reading-the-signal); [allowed operations](../science/model.md#allowed-operations).

### M07 Jump records and retained experimental labels

**Central question.** Which records are observable in the stated model?

**Understanding target.** Distinguish a system-side parity record from direct access to environmental outputs. Relate $`L^\dagger L=\gamma I`$ to state-independent counts in the stated protocol, and retain the setting, count, readout angle, outcome, and failure flag when relevant.

**Prerequisites.** [M04](#m04-markovian-noise-and-rate-normalization), [M06](#m06-a-noiseless-ancilla-and-parity-encoding)

**Story role.** This specifies the data on which every likelihood and stopping rule is built.

**Conceptual connection.** Discarding a label changes the experiment. Assuming an accessible bath record would change the resource model rather than improve its data processing.

**Canonical sources.** [Allowed operations](../science/model.md#allowed-operations); [complete preset readout](../science/preset_protocols.md#common-readout-and-the-order-of-nuisance-elimination).

### M08 Likelihood scores and local information

**Central question.** What does Fisher information say about nearby parameter values?

**Understanding target.** Interpret a likelihood derivative as a score and its second moment as local distinguishability. Distinguish information in a specified measurement from the actual error of an estimator on one run.

**Prerequisites.** [M01](#m01-qubit-states-and-recorded-outcomes), [M02](#m02-frequency-and-coherent-phase-accumulation), [M07](#m07-jump-records-and-retained-experimental-labels)

**Story role.** This supplies the classical statistical language for the noise-direction penalty.

**Conceptual connection.** A steep Ramsey fringe provides local sensitivity but still has phase ambiguity; a large information value is not a globally accurate estimate.

**Canonical sources.** [Haase §II.A–B](HAASE_BRIDGE.md#source-map); [scores and Fisher matrix](TUTORIAL.md#3-why-a-nuisance-parameter-costs-information).

### M09 A shared nuisance and efficient information

**Central question.** Which part of apparent frequency sensitivity survives an unknown noise angle?

**Understanding target.** Interpret efficient information as the target score after projection away from nuisance scores. Pool the full Fisher matrices of labelled experiments before eliminating their common nuisance.

**Prerequisites.** [M08](#m08-likelihood-scores-and-local-information)

**Story role.** This defines the local precision quantity optimized by the project.

**Conceptual connection.** Treating each label as having an independent direction, or using only the target diagonal entry, answers a different statistical question.

**Canonical sources.** [Efficient information and pooling](../science/model.md#information-in-the-presence-of-a-nuisance); [worked nuisance projection](TUTORIAL.md#3-why-a-nuisance-parameter-costs-information).

### M10 Quantum information and strategy bounds

**Central question.** How can a bound cover measurements and controls not explicitly constructed?

**Understanding target.** Separate the Fisher information of an actual readout, the quantum Fisher information of its output, and an upper bound on all allowed controlled channels. Identify the assumptions of the imported bound.

**Prerequisites.** [M04](#m04-markovian-noise-and-rate-normalization), [M08](#m08-likelihood-scores-and-local-information), [M09](#m09-a-shared-nuisance-and-efficient-information)

**Story role.** This establishes the distinction between a protocol calculation and a converse.

**Conceptual connection.** Parameter-independent controls can use previous outcomes without receiving an oracle for the unknown parameters. The adaptive time bound is not obtained by relabelling a probe-number bound.

**Canonical sources.** [Haase §IV.A–C](HAASE_BRIDGE.md#source-map); [nuisance-path argument](../science/model.md#the-nuisance-path-argument); [inherited channel bound](../science/precision_bounds.md#the-inherited-channel-bound).

### M11 Random waiting times and stopping costs

**Central question.** When is a successful random-duration operation a finite-resource procedure?

**Understanding target.** Distinguish a stopping rule, its physical duration, its expectation, and a hard deadline. Interpret a tail bound and the cost of explicitly retained failures.

**Prerequisites.** [M03](#m03-interrogation-and-the-physical-time-budget), [M07](#m07-jump-records-and-retained-experimental-labels)

**Story role.** This prepares the resource accounting needed for stopped sensing.

**Conceptual connection.** Almost-sure eventual completion need not have finite mean cost. Success-conditioned precision cannot omit the exposure of failed or unfinished attempts.

**Canonical sources.** [Charged time and failures](../science/model.md#charged-time-and-failures); [stopped-time example](TUTORIAL.md#6-let-the-error-supply-its-own-recovery).

### M12 Local precision and global estimation risk

**Central question.** Why does a bounded-interval estimation task require more than local information?

**Understanding target.** Distinguish locally unbiased variance bounds from worst-case mean-square error allowing biased estimators. Explain phase ambiguity, fixed prior support, and the different roles of lower bounds and explicit global procedures.

**Prerequisites.** [M08](#m08-likelihood-scores-and-local-information), [M09](#m09-a-shared-nuisance-and-efficient-information), [M10](#m10-quantum-information-and-strategy-bounds), [M11](#m11-random-waiting-times-and-stopping-costs)

**Story role.** This joins the statistical and timing prerequisites before the full task is stated.

**Conceptual connection.** Multiple interrogation scales resolve ambiguity; a smooth prior can establish a minimax lower bound without giving that prior to the controller.

**Canonical sources.** [Global distinction](TUTORIAL.md#8-global-precision-is-a-separate-statement); [global statistical task](../science/global_precision.md#statistical-task-and-theorem); [biased-estimator bound](../science/global_precision.md#a-bound-valid-for-biased-estimators).

### M13 The complete operational comparison

**Central question.** What precisely changes between the fixed-rate and rate-diverse experiments?

**Understanding target.** State the target, shared continuous nuisance, positive fixed rate bounds, retained data, ideal controls, and charged physical time. Distinguish the local-information, exact-channel, and global-risk tasks.

**Prerequisites.** [M03](#m03-interrogation-and-the-physical-time-budget), [M06](#m06-a-noiseless-ancilla-and-parity-encoding), [M07](#m07-jump-records-and-retained-experimental-labels), [M09](#m09-a-shared-nuisance-and-efficient-information), [M10](#m10-quantum-information-and-strategy-bounds), [M11](#m11-random-waiting-times-and-stopping-costs), [M12](#m12-local-precision-and-global-estimation-risk)

**Story role.** This completes the background phase by assembling one common comparison model.

**Conceptual connection.** Rate diversity is the added resource; bath-output access, a coherent unknown-axis drive, free repetitions, and a known nuisance are not silently added with it.

**Canonical sources.** [Complete model](../science/model.md); [question and contribution](../science/interpretation.md#the-question-and-the-contribution).

## Phase II: narrative and innovation

### M14 The phase left by fixed recovery

**Central question.** Why does returning the sensor to its code not fully correct its sensing phase?

**Understanding target.** Use $`XN_\phi=e^{i\phi Z}`$ to reconstruct the complete count-conditioned phase and the inherited fixed-rate information $`T^2/(1+\gamma T)`$. Keep the noise direction as a nuisance.

**Prerequisites.** [M13](#m13-the-complete-operational-comparison)

**Story role.** This starts the narrative with a concrete, attributed component rather than a universal claim.

**Conceptual connection.** Known recovery pulses can restore parity while leaving a coherent nuisance phase. The target-only Fisher entry overstates usable information.

**Canonical sources.** [Fixed-recovery readout](../science/preset_protocols.md#common-readout-and-the-order-of-nuisance-elimination); [single-rate attainment](../science/precision_bounds.md#attainment-with-preset-controls); [closest predecessor](../references/RELATED_WORK.md#closest-noise-model).

### M15 The all-strategy fixed-rate obstruction

**Central question.** Why can a different adaptive learning-and-correction strategy not evade the fixed-rate law?

**Understanding target.** Follow the joint frequency-and-angle path, its cancellation of the coherent growth term, and the resulting bound $`\mathcal I_\omega^*(T)\le T/\gamma`$. Identify why this covers the full allowed model.

**Prerequisites.** [M10](#m10-quantum-information-and-strategy-bounds), [M13](#m13-the-complete-operational-comparison), [M14](#m14-the-phase-left-by-fixed-recovery)

**Story role.** This elevates the component limitation into a universal converse with a matching leading coefficient.

**Conceptual connection.** The nuisance path is a proof device, not a physical assertion that the bath encodes the frequency. A failed calibration protocol alone would not prove this result.

**Canonical sources.** [Theorem 1 and its proof](../science/precision_bounds.md#theorem-1--fixed-rate); [common nuisance path](../science/precision_bounds.md#the-common-nuisance-path); [tutorial converse](TUTORIAL.md#7-from-a-protocol-to-an-all-strategy-bound).

### M16 The optimal selectable-setting ceiling

**Central question.** What prevents one nuisance direction from cancelling the signal in every setting?

**Understanding target.** Interpret the minimax residual $`\min_c\max_j|s_j-2c\gamma_j|`$ and its pairwise expression. Recognize why unequal signal-to-rate ratios, not a proportional speed-up, permit a positive quadratic coefficient.

**Prerequisites.** [M15](#m15-the-all-strategy-fixed-rate-obstruction)

**Story role.** This identifies the control resource and its universal leading ceiling before proving attainment.

**Conceptual connection.** The interval-intersection argument turns a many-setting optimization into a pairwise criterion, while preserving one common nuisance parameter.

**Canonical sources.** [Theorem 3](../science/precision_bounds.md#theorem-3--selectable-signal-and-noise-strengths); [minimax derivation](../science/precision_bounds.md#the-minimax-coefficient).

### M17 Statistical separation by recorded rate diversity

**Central question.** How can two noisy labelled experiments separate the same two unknown parameters?

**Understanding target.** Reconstruct the random-rate likelihood and average its full Fisher matrices before nuisance elimination. Explain why one constant rate per interrogation can suffice for quadratic local information.

**Prerequisites.** [M09](#m09-a-shared-nuisance-and-efficient-information), [M14](#m14-the-phase-left-by-fixed-recovery), [M16](#m16-the-optimal-selectable-setting-ceiling)

**Story role.** This supplies the simplest statistical mechanism attaining the rate-diverse scaling.

**Conceptual connection.** The rate label alone carries no target information. It identifies differing nuisance responses, and both the label and count record must remain available.

**Canonical sources.** [Recorded random rate](../science/preset_protocols.md#a-recorded-random-choice-of-one-rate); [complete numerical example](TUTORIAL.md#4-a-complete-rate-diversity-example).

### M18 Optimal design and calibration-free local scaling

**Central question.** Which design choices need calibrated rates, and which guarantees do not?

**Understanding target.** Connect the maximizing pair and its probabilities to the universal coefficient. Distinguish exact leading optimization from the fair choice’s constant-factor guarantee, and explain the orthogonal unknown-rate score block.

**Prerequisites.** [M16](#m16-the-optimal-selectable-setting-ceiling), [M17](#m17-statistical-separation-by-recorded-rate-diversity)

**Story role.** This closes the matching local theorem and determines its actual calibration requirements.

**Conceptual connection.** A fair choice needs no numerical rate estimate to be designed, but inference still uses the retained counts. Local information is not a global guarantee for one randomly chosen branch.

**Canonical sources.** [Optimal and fair choices](../science/preset_protocols.md#optimal-and-calibration-free-choices); [unknown-rate blocks](../science/preset_protocols.md#also-treating-the-numerical-rates-as-unknown); [general setting attainment](../science/preset_protocols.md#general-selectable-settings).

### M19 The balanced echo and its specific limitation

**Central question.** What does balancing expected counts achieve, and what does an imbalance destroy?

**Understanding target.** Derive the role of signed time, count mean, and count variance in the two-block echo. Distinguish finite-time statistical orthogonality from cancellation on each trajectory, and track the differential-balancing crossover.

**Prerequisites.** [M14](#m14-the-phase-left-by-fixed-recovery), [M17](#m17-statistical-separation-by-recorded-rate-diversity), [M18](#m18-optimal-design-and-calibration-free-local-scaling)

**Story role.** This compares a second local construction without mistaking its calibration weakness for a universal obstruction.

**Conceptual connection.** Common multiplicative rate error preserves balance; fixed differential error can remove the echo’s quadratic scaling. The recorded random-rate construction avoids that time-amplified penalty.

**Canonical sources.** [Echo and calibration](../science/preset_protocols.md#two-block-echo); [timing imbalance](../science/preset_protocols.md#timing-imbalance-and-its-crossover); [worked echo](TUTORIAL.md#5-what-the-preset-echo-trades-for-balance).

### M20 Two uncorrected errors and the signed clock

**Central question.** What remains of the unknown direction when errors are left uncorrected?

**Understanding target.** Track the chronological trajectory identity and the signed interrogation time. Explain why an even count removes the unknown operator while retaining the signal’s signed residence times.

**Prerequisites.** [M05](#m05-the-algebra-of-an-unknown-transverse-error), [M06](#m06-a-noiseless-ancilla-and-parity-encoding), [M14](#m14-the-phase-left-by-fixed-recovery)

**Story role.** This begins the exact-channel mechanism, distinct from statistical nuisance separation.

**Conceptual connection.** Identical involutory errors can supply their own recovery, but equal physical time in the two sectors would cancel the desired signal as well.

**Canonical sources.** [Uncorrected trajectory identity](../science/precision_bounds.md#attainment-by-leaving-the-errors-uncorrected); [paired-error example](TUTORIAL.md#6-let-the-error-supply-its-own-recovery).

### M21 Rate feedback and an exact stopped operation

**Central question.** How can the signed clock implement a prescribed noiseless sensing operation?

**Understanding target.** Explain the positive signed drift from a lower rate in the code sector and a higher rate in the error sector. Identify why the first upward crossing of a target signed time has even parity and gives the same Ramsey channel on every completion.

**Prerequisites.** [M11](#m11-random-waiting-times-and-stopping-costs), [M20](#m20-two-uncorrected-errors-and-the-signed-clock)

**Story role.** This converts trajectory cancellation into an exact operational output.

**Conceptual connection.** The stopping rule requires the syndrome timing but not the numerical rates or the unknown direction. Its exact channel guarantee does not yet bound its physical cost.

**Canonical sources.** [Stopped protocol and output](../science/stopped_sensing.md#protocol-and-exact-output); [comparison of guarantees](../science/preset_protocols.md#relation-to-stopped-sensing).

### M22 First-passage law and the equal-rate boundary

**Central question.** How much physical time does the exact stopped operation require?

**Understanding target.** Interpret the two-state backward equations, outgoing boundary, Laplace transform, mean, variance, and exponential tail. Explain why equal rates still permit eventual completion but have infinite mean duration.

**Prerequisites.** [M11](#m11-random-waiting-times-and-stopping-costs), [M21](#m21-rate-feedback-and-an-exact-stopped-operation)

**Story role.** This determines whether the exact operation is a finite-cost sensing resource.

**Conceptual connection.** A fixed effective interrogation time and a random physical completion time are different quantities. The equal-rate limit is consistent with, not a counterexample to, the converse.

**Canonical sources.** [First-passage proof](../science/stopped_sensing.md#first-passage-law); [timing checks](../verification/README.md#coverage).

### M23 Hard deadlines and finite-time advantage

**Central question.** Does the advantage remain after every unfinished run is charged?

**Understanding target.** Explain the sublinear deadline margin, success-weighted information, and the separate finite-time certificate. Distinguish sufficient thresholds from an optimized finite-time optimum.

**Prerequisites.** [M15](#m15-the-all-strategy-fixed-rate-obstruction), [M18](#m18-optimal-design-and-calibration-free-local-scaling), [M22](#m22-first-passage-law-and-the-equal-rate-boundary)

**Story role.** This connects the exact stopped channel back to the same physical budget as the universal comparison.

**Conceptual connection.** No success-only normalization or unlimited waiting is used; preset and stopped protocols retain different output and timing guarantees even when their leading local coefficients match.

**Canonical sources.** [Hard-deadline attainment](../science/stopped_sensing.md#a-hard-deadline-and-the-optimal-local-coefficient); [finite-time separation](../science/stopped_sensing.md#a-finite-time-separation); [preset comparison](../science/preset_protocols.md#relation-to-stopped-sensing).

### M24 Global lower bounds without unbiasedness

**Central question.** How can a nuisance-path information bound constrain every estimator’s global risk?

**Understanding target.** Follow the compact smooth prior, integration-by-parts identity, and uniform path bound in the van Trees argument. Distinguish lower bounds from different path priors and avoid inferring an optimal global constant from the local coefficient.

**Prerequisites.** [M12](#m12-local-precision-and-global-estimation-risk), [M15](#m15-the-all-strategy-fixed-rate-obstruction), [M16](#m16-the-optimal-selectable-setting-ceiling), [M23](#m23-hard-deadlines-and-finite-time-advantage)

**Story role.** This places the negative and positive resource models under one global performance criterion.

**Conceptual connection.** The prior is a minimax proof device. Bias, adaptivity, and learning during sensing do not invalidate the uniform lower-bound argument.

**Canonical sources.** [Biased-estimator argument](../science/global_precision.md#a-bound-valid-for-biased-estimators); [fixed-rate bound](../science/global_precision.md#fixed-rate-lower-bound); [controlled-rate bound](../science/global_precision.md#controlled-rate-lower-bound).

### M25 Global achievability and the same-metric separation

**Central question.** Which explicit procedures attain the global scalings at a hard total deadline?

**Understanding target.** Connect paid no-error trials to the fixed-rate upper scaling and multiscale exact stopped operations to controlled-rate phase unwrapping. Account for the sum of all physical durations and a bounded fallback on failure.

**Prerequisites.** [M12](#m12-local-precision-and-global-estimation-risk), [M22](#m22-first-passage-law-and-the-equal-rate-boundary), [M23](#m23-hard-deadlines-and-finite-time-advantage), [M24](#m24-global-lower-bounds-without-unbiasedness)

**Story role.** This completes the global precision theorem with matching achievable and unavoidable exponents.

**Conceptual connection.** The result is a separation in worst-case mean-square error, not a substitution of a preset Fisher matrix for a global estimator. Optimal global constants remain distinct.

**Canonical sources.** [Fixed-rate upper scaling](../science/global_precision.md#a-matching-fixed-rate-upper-scaling); [multiscale stopped construction](../science/stopped_sensing.md#global-estimation-on-a-bounded-interval); [complete global comparison](../science/global_precision.md#controlled-rate-upper-scaling).

### M26 Physical access and the shared-axis condition

**Central question.** When does a physical rate knob provide the resource in the theorem?

**Understanding target.** Connect scalar noise injection and unobserved collision intensity to one shared interaction. Distinguish coherent access, independent setting-dependent axes, known signal changes, and unrestricted unknown frequency offsets.

**Prerequisites.** [M13](#m13-the-complete-operational-comparison), [M16](#m16-the-optimal-selectable-setting-ceiling), [M18](#m18-optimal-design-and-calibration-free-local-scaling), [M21](#m21-rate-feedback-and-an-exact-stopped-operation), [M25](#m25-global-achievability-and-the-same-metric-separation)

**Story role.** This translates the precision laws into explicit physical requirements and exclusions.

**Conceptual connection.** A known pulse generally changes both the signal and the unknown noise axis. Free unknown offsets can make the target unidentifiable; unrelated unknown axes restore a linear ceiling.

**Canonical sources.** [Physical realizations](../science/physical_scope.md#a-scalar-control-of-one-interaction); [independent-axis converse](../science/precision_bounds.md#independent-setting-dependent-directions); [resource interpretation](../science/interpretation.md#physical-interpretation-and-assumptions).

### M27 Finite measurement cadence and local scope

**Central question.** What survives when parity is checked at fixed intervals?

**Understanding target.** Interpret the sampled parity chain and its nonzero mean signed drift. Explain the compensated operating point and why hidden residence times prevent importing the exact continuous-monitoring global proof.

**Prerequisites.** [M21](#m21-rate-feedback-and-an-exact-stopped-operation), [M23](#m23-hard-deadlines-and-finite-time-advantage), [M26](#m26-physical-access-and-the-shared-axis-condition)

**Story role.** This separates one proved monitoring variation from claims of general implementation robustness.

**Conceptual connection.** Ideal finite-interval measurements are not faulty readout. A positive local coefficient at compensation does not establish global accuracy away from it.

**Canonical sources.** [Finite-cadence derivation](../science/physical_scope.md#finite-interval-ideal-parity-measurements).

### M28 Residual parallel noise and a finite advantage window

**Central question.** How can finite advantage coexist with the loss of strict asymptotic scaling?

**Understanding target.** Connect parallel dephasing to the Lindblad-span ceiling and to the exact contrast reduction for the prescribed readout. Interpret the nonzero-noise finite-time certificate without turning it into a fault-tolerance threshold.

**Prerequisites.** [M04](#m04-markovian-noise-and-rate-normalization), [M18](#m18-optimal-design-and-calibration-free-local-scaling), [M25](#m25-global-achievability-and-the-same-metric-separation), [M26](#m26-physical-access-and-the-shared-axis-condition), [M27](#m27-finite-measurement-cadence-and-local-scope)

**Story role.** This makes a consequential imperfection quantitative within the complete resource account.

**Conceptual connection.** A positive fixed uncorrectable parallel rate eventually enforces a linear ceiling, yet an explicitly charged protocol can still beat the ideal fixed-rate benchmark at finite time.

**Canonical sources.** [Parallel-noise converse](../science/residual_dephasing.md#every-fixed-positive-parallel-rate-restores-a-linear-ceiling); [finite certificate](../science/residual_dephasing.md#a-certified-finite-time-advantage-with-nonzero-dephasing).

### M29 Attribution and the strength of the evidence

**Central question.** Which ingredients are inherited, and which claims are supported by proofs or finite checks?

**Understanding target.** Identify the known-noise framework, fixed-recovery baseline, channel bound, noise-assisted feedback, van Trees method, and multiscale estimation as attributed ingredients. Separate the combined precision result from those methods and from physical implementation claims.

**Prerequisites.** [M15](#m15-the-all-strategy-fixed-rate-obstruction), [M18](#m18-optimal-design-and-calibration-free-local-scaling), [M25](#m25-global-achievability-and-the-same-metric-separation), [M28](#m28-residual-parallel-noise-and-a-finite-advantage-window)

**Story role.** This joins the scientific story to its provenance and reproducibility boundaries.

**Conceptual connection.** Passing tests checks specified identities and code behavior; it does not certify universal laws, exhaustive priority, independent validation, or a reader’s understanding.

**Canonical sources.** [Related work](../references/RELATED_WORK.md); [verification coverage and limits](../verification/README.md); [synthesis](../science/interpretation.md#evidence-and-use).

### M30 The complete scientific story

**Central question.** What does rate control change about sensing with a continuously unknown error direction?

**Understanding target.** Explain the shared task, universal fixed-rate obstruction, matching local rate-diverse law, exact stopped channel, same-metric global separation, and essential physical boundaries as one connected argument.

**Prerequisites.** [M18](#m18-optimal-design-and-calibration-free-local-scaling), [M19](#m19-the-balanced-echo-and-its-specific-limitation), [M23](#m23-hard-deadlines-and-finite-time-advantage), [M25](#m25-global-achievability-and-the-same-metric-separation), [M26](#m26-physical-access-and-the-shared-axis-condition), [M27](#m27-finite-measurement-cadence-and-local-scope), [M28](#m28-residual-parallel-noise-and-a-finite-advantage-window), [M29](#m29-attribution-and-the-strength-of-the-evidence)

**Story role.** This completes the narrative phase and the project-wide understanding map.

**Conceptual connection.** Statistical nuisance separation and trajectory-wise cancellation support different guarantees. Their common significance is a rigorously specified distinction between knowing an error direction and controlling its rate, not a general claim that noise improves every sensor.

**Canonical sources.** [Scientific synthesis](../science/interpretation.md); [claim-to-proof map](../science/interpretation.md#claim-and-proof-map); [scientific entrypoint](../science/README.md).
