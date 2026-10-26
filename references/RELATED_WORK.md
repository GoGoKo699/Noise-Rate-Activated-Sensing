# Related work and attribution

[Overview](../README.md) · [Scientific synthesis](../science/interpretation.md) · [Bibliography](references.bib)

This comparison uses primary papers and identifies preprints as such. It separates inherited methods from the precision statements proved here. The core unknown-direction pages and channel-bound coefficients were checked on 16 October 2026; the focused non-Markovian and global-estimation comparisons below were checked on 26 October 2026. It is a targeted comparison, not an exhaustive priority guarantee.

## Closest noise model

**Tanggara, Conlon, Gorshkov, and Bharti, “Optimal noisy sequential multiparameter quantum sensing,” arXiv:2609.30398v1 (2026).** [Paper](https://arxiv.org/abs/2609.30398v1)

Section V.B.2, p. 16, uses the fixed continuously unknown transverse direction and explicitly distinguishes it from a finite-set promise. Appendix A.3 and A.4 analyze calibration-based and fixed-recovery protocols. The paper leaves the general-strategy scaling question open. The present fixed-rate converse applies to all operations in the stated continuous-time resource model; the positive theorem adds a rate-control resource. Their Hamiltonian convention is $`H=\theta Z`$, whereas this repository uses $`H=\omega Z/2`$, so comparisons use $`\omega=2\theta`$.

The fixed recovery $`X`$, count-conditioned phase, and complete-record single-rate information $`T^2/(1+\gamma T)`$ are inherited from Appendix A.4(a), Eqs. (A19)–(A29), pp. 26–27. They supply an attaining protocol for the linear coefficient once the universal converse is established. The [preset protocols](../science/preset_protocols.md) combine that building block with distinct rates. Averaging full Fisher matrices before eliminating a shared nuisance is ordinary statistical design, not a new metrological formalism. The [global-risk proof](../science/global_precision.md) extends the fixed-rate limitation to biased estimators in a worst-case task and compares it with the stopped-channel upper bound in the same metric.

## Bound and estimation foundations

**Demkowicz-Dobrzański and Maccone, “Using entanglement against noise in quantum metrology,” Physical Review Letters 113, 250801 (2014).** [Paper](https://doi.org/10.1103/PhysRevLett.113.250801) · [Author version](https://arxiv.org/abs/1407.2934v3)

The channel-extension bound for arbitrary adaptive, ancilla-assisted sequences, including its linear form when the Kraus derivative overlap vanishes, is established in Eq. (9). The [microscopic precision proof](../science/microscopic_precision.md) supplies the finite-step purification argument for the present collision channel, with one shared nuisance path across all selected settings. Its exact coefficients and boundary-clock assumptions are derived here; the general adaptive bound is inherited.

**Das, Górecki, and Demkowicz-Dobrzański, “Universal time scalings of sensitivity in Markovian quantum metrology,” Physical Review A 111, L020403 (2025).** [Paper](https://doi.org/10.1103/PhysRevA.111.L020403) · [Equations](https://arxiv.org/html/2404.03954v2)

The adaptive information-growth inequality and its operators, including parameter-dependent noise, are inherited from Eqs. (2), (4), and (5). The zero-gauge nuisance-path substitution and matching constructions are worked out here. The general channel-bound method is not a contribution of this repository. The residual-parallel-noise bound uses a different explicit gauge of this same established inequality.

**Zhou, Zhang, Preskill, and Jiang, “Achieving the Heisenberg limit in quantum metrology using quantum error correction,” Nature Communications 9, 78 (2018).** [Paper](https://doi.org/10.1038/s41467-017-02510-3)

The known-noise Hamiltonian-not-in-Lindblad-span criterion and noiseless-ancilla control framework are established background. A known transverse direction is correctable, whereas parallel noise places the signal in the Lindblad span. Neither fact removes a continuously unknown nuisance direction from the experiment.

**Abbasgholinejad et al., “Error-corrected function estimation advantage in multiparameter Hamiltonians,” arXiv:2609.16226v1 (2026).** [Paper](https://arxiv.org/abs/2609.16226v1)

Reduction of function estimation to one-parameter embeddings and correction of nuisance Hamiltonian parameters are close methodological precedents. Here the nuisance rotates the Lindblad operator, and the controlled family produces the explicit rate-contrast law. Neither nuisance elimination nor embedding optimization is claimed as a newly invented general method.

**Gill and Levit, “Applications of the van Trees inequality: a Bayesian Cramér–Rao bound,” Bernoulli 1, 59–79 (1995).** [Paper](https://projecteuclid.org/journals/bernoulli/volume-1/issue-1-2/Applications-of-the-van-Trees-inequality--a-Bayesian-Cram%C3%A9r/bj/1186078362.full)

Using a smooth compact prior on a difficult submodel to obtain a minimax lower bound is an established statistical technique. The global-risk proof supplies the scalar integration-by-parts argument explicitly. Its application to the uniform sensing nuisance-path bound is not a new Bayesian inequality. The path prior is a proof device, not a distribution of angles assumed by the physical protocol.

## Non-Markovian correction and controlled-process metrology

<a id="mann2025nonmarkovian"></a>
**Mann, Cao, Laflamme, and Zhou, “Quantum Error Corrected Non-Markovian Metrology,” PRX Quantum 6, 030321 (2025).** [Paper](https://doi.org/10.1103/wfyl-wtz3) · [Compared version](https://arxiv.org/html/2503.07745v2)

Section III derives sufficient conditions for quadratic quantum Fisher information in a hidden Markov model with an inaccessible environment. Theorem 3 assumes perfect, arbitrarily fast error correction; some subsequent guarantees are stated as a quadratic limsup. The statistical formulation uses the quantum Cramér–Rao bound for repeated experiments. Non-Markovian error correction and recovery of quadratic information are therefore established precedents. The [microscopic global theorem](../science/microscopic_global_precision.md) instead keeps the collision duration and two positive couplings fixed and proves worst-case risk on one nonshrinking interval, uniformly over a shared unknown direction. Its resource restriction and global attainability argument are additional requirements, not consequences of the non-Markovian correction criteria.

<a id="altherr2021nonmarkovian"></a>
**Altherr and Yang, “Quantum metrology for non-Markovian processes,” Physical Review Letters 127, 060501 (2021).** [Paper](https://doi.org/10.1103/PhysRevLett.127.060501) · [Compared version](https://arxiv.org/html/2103.02619v2)

Theorem 1, Eq. (8), and Algorithm 1 characterize and optimize quantum-comb Fisher information over probe controls. Appendix B studies collision examples, including an elementary step that factors a signal gate and an interaction gate. This establishes a general framework for control-enhanced non-Markovian metrology. Here the signal acts during the bounded interaction, and only collision-boundary controls are available in the rate-menu comparison. An optimized local comb information value does not by itself supply a global estimator, a nuisance-uniform risk bound or the one-versus-two-coupling separation. The [temporal-access companion](https://github.com/GoGoKo699/Markovian-Resolution-Limit/blob/main/science/global_contact_precision.md) treats access inside the same microscopic interactions as a separate resource.

<a id="kurdzialek2025correlated"></a>
**Kurdziałek, Albarelli, and Demkowicz-Dobrzański, “Universal bounds for quantum metrology in the presence of correlated noise,” Physical Review Letters 135, 130801 (2025).** [Paper](https://doi.org/10.1103/jy3v-wkcb) · [Compared version](https://arxiv.org/html/2410.01881v3)

Equations (5)–(7) give adaptive-information recurrences and asymptotic bounds; the subsequent quantum-comb construction treats temporal and spatial correlations. Its general bounds need not be tight. This is a close converse framework, alongside the channel-extension sources above. The present nuisance-curve calculation supplies an explicit linear bound for the fixed-coupling microscopic channel on a frequency subinterval, and the established van Trees method turns it into a minimax obstruction. The matching global upper bound requires the separate [recorded-phase estimator](../science/recorded_phase_estimation.md). Neither the general adaptive bound nor reciprocal local information alone establishes that risk statement.

## Noise-assisted recovery is established

**Cardona, Sarlette, and Rouchon, “Continuous-time Quantum Error Correction with Noise-assisted Quantum Feedback,” arXiv:1902.00115v4 (2019).** [Paper](https://arxiv.org/abs/1902.00115v4)

The authors introduce Brownian control with state-estimate-dependent gains to stabilize a three-qubit bit-flip code. Adding stochastic driving to encourage recovery is a direct conceptual predecessor. The present contribution concerns an unknown error axis, preservation of an unknown signal, a universal fixed-rate obstruction, and an optimal precision coefficient—not the invention of noise-assisted feedback.

**Reiter, Sørensen, Zoller, and Muschik, “Dissipative quantum error correction and application to quantum sensing with trapped ions,” Nature Communications 8, 1822 (2017).** [Paper](https://doi.org/10.1038/s41467-017-01895-5)

Engineered dissipation for protected sensing is established. The present monitored protocol and nuisance-sensitive bound use different resources; the broad claim that dissipation can benefit quantum sensing is not new.

**Kwon, Fischer, Lee, and Jiang, “Restoring Heisenberg scaling in time via autonomous quantum error correction,” arXiv:2504.13168v3 (2026 revision).** [Preprint](https://arxiv.org/abs/2504.13168v3) · [Published article](https://doi.org/10.1038/s41534-026-01268-1)

Their sufficient-condition framework uses engineered autonomous correction, with a commuting-noise condition and quantified approximation over a chosen interval. Our anticommuting-noise protocol uses ideal monitoring and a noiseless ancilla. These are different resource models; no practical superiority of either protocol follows from this comparison.

## Informative noise is a different resource

**Chen, Chen, Liu, Miao, and Yuan, “Quantum Metrology Enhanced by Leveraging Informative Noise with Error Correction,” Physical Review Letters 133, 190801 (2024).** [Paper](https://doi.org/10.1103/PhysRevLett.133.190801)

This work exploits noise carrying information about the estimated parameter. In the physical model here, $`L_j`$ and $`\gamma_j`$ do not encode the target $`\omega`$; the target is in the Hamiltonian. The artificial joint parameter path used for a converse does not change that physical distinction.

## Environmental and higher-order access

**Albarelli, Rossi, Tamascelli, and Genoni, “Restoring Heisenberg scaling in noisy quantum metrology by monitoring the environment,” Quantum 2, 110 (2018).** [Paper](https://doi.org/10.22331/q-2018-12-03-110)

Environmental monitoring is an established metrological resource. That work studies continuously monitored environments of noisy probes, including scaling in the number of probes. The present time-scaling converse excludes direct bath-output access; its constructive record is obtained from parameter-independent sensor–ancilla parity measurements. The different access and scaling variables must be stated rather than interpreting environmental-monitoring results as a contradiction or claiming to invent monitored sensing.

**Xu, Deng, Zheng, Xiao, and Zeng, “Noise-Resilient Heisenberg-limited Quantum Sensing via Indefinite-Causal-Order Error Correction,” arXiv:2601.01404v1 (2026).** [Paper](https://arxiv.org/html/2601.01404v1)

This proposal uses coherently controlled order between controls and noisy evolution, and in some constructions controlled Hamiltonian time direction. Its unknown-noise claims therefore concern a different access model. The present bounds cover ordinary causally ordered adaptive channels and classical rate selection, not those higher-order resources. This distinction follows from its stated superchannel construction; it is not an independent verification or refutation of that paper's full claims.

## Physical control precedents

**Rower et al., “Qubit-state purity oscillations from anisotropic transverse noise,” Physical Review A 111, 032420 (2025).** [Paper](https://doi.org/10.1103/PhysRevA.111.032420) · [Model and supplement](https://arxiv.org/html/2409.12303v1)

The fluxonium noise-injection experiment is a precedent for fixed-axis transverse noise. Its frequency-shift discussion makes clear why the signal response under rate modulation must be checked. It is not an implementation of the stopped protocol or a demonstration of a device restricted to incoherent rate access.

**Pechen and Rabitz, “Teaching the environment to control quantum systems,” Physical Review A 73, 062102 (2006).** [Paper](https://doi.org/10.1103/PhysRevA.73.062102)

Incoherent environment control is an established resource. This supports distinguishing a reservoir-intensity knob from a coherent system drive; it does not certify the precise shared-axis resource on a particular device.

## Phase-estimation and stopping background

**Hoeffding, “Probability inequalities for sums of bounded random variables,” Journal of the American Statistical Association 58, 13–30 (1963).** [Paper](https://doi.org/10.1080/01621459.1963.10500830)

Concentration of bounded independent observations is an inherited statistical ingredient. The [microscopic calibration theorem](../science/microscopic_identifiability.md) applies it to a complete three-outcome experiment, including failed parity outcomes, after deriving an explicit inverse-Lipschitz response on a fixed frequency band. Its concentration inequality is not a new statistical bound.

**Higgins et al., “Demonstrating Heisenberg-limited unambiguous phase estimation without adaptive measurements,” New Journal of Physics 11, 073023 (2009).** [Paper](https://doi.org/10.1088/1367-2630/11/7/073023) · [Compared version](https://arxiv.org/abs/0809.3308v4)

Section 4, pp. 9–10, uses dyadic interrogation lengths, tapered repetitions and first-failed-stage error accounting to establish global Heisenberg scaling. Multiscale ambiguity resolution and this allocation principle are inherited methods. The continuous-time [global result](../science/global_precision.md) transfers such reasoning to exact stopped Ramsey operations and includes deadline failures.

The finite-strength [recorded-phase lemma](../science/recorded_phase_estimation.md) adds a conditional argument for observed, nonlinear phase functions whose record probabilities may depend on the unknown frequency. It inverts the actual retained functions, proves uniform sensitivity on a fixed interval, and charges calibration, every attempted block and all failed records. The [microscopic theorem](../science/microscopic_global_precision.md) verifies these conditions uniformly over the shared unknown direction. Adapting a terminal measurement basis uses the observed record and earlier estimates; it does not retune physical compensation. These additional steps connect the microscopic construction to global risk rather than infer it from local Fisher information.

**Gneiting, Rozhkov, and Nori, “Jump-time unraveling of Markovian open quantum systems,” Physical Review A 104, 062212 (2021).** [Paper](https://doi.org/10.1103/PhysRevA.104.062212)

Conditioning open-system dynamics on jump counts is established. Count-conditioned evolution and first-passage methods are not claimed as new formalisms. The specific shared-axis-cancelling sensing operation and its physical-time precision law are the statements at issue here.

## Contribution boundary

The central contribution is the combination of a nuisance-sensitive all-strategy converse, its removal by bounded shared-axis rate diversity, a matching local coefficient, and an exact stopped channel with charged timing and a same-metric global precision separation. The finite-strength microscopic comparison independently establishes inverse-time versus inverse-time-squared worst-case risk on a sufficient fixed frequency band, using one versus two fixed positive couplings, boundary-only controls and unchanged compensation. Its constants depend on the fixed hardware and band; neither maximal bandwidth nor optimal global constants are asserted. Residual-dephasing and imperfect-control results retain their separately stated scope. None of these claims asserts correction of arbitrary uncharacterized noise, an experimental demonstration, a fault-tolerance threshold, or exhaustive bibliographic priority.
