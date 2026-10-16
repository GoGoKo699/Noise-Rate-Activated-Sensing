# Related work and attribution

[Overview](../README.md) · [Model](../docs/MODEL.md) · [Bibliography](references.bib)

The source comparison below uses primary papers, with preprints identified as such. It distinguishes inherited tools and mechanisms from the precision statements proved in this repository. Bibliographic and source-content checks were made on 16 October 2026. This is a targeted comparison, not an exhaustive priority guarantee.

## Closest noise model

**Tanggara, Conlon, Gorshkov, and Bharti, “Optimal noisy sequential multiparameter quantum sensing,” arXiv:2609.30398v1 (2026).** [Paper](https://arxiv.org/abs/2609.30398v1)

Section V.B.2, p. 16, uses the fixed continuously unknown transverse direction and explicitly distinguishes it from a finite-set promise. Appendix A.3 and A.4 analyze calibration-based and fixed-recovery protocols. The paper leaves the general-strategy scaling question open. The present fixed-rate converse applies to all operations in the stated continuous-time resource model; the positive theorem adds a rate-control resource. Their Hamiltonian convention is $H=\theta Z$, whereas this repository uses $H=\omega Z/2$. The two sensing tasks should be compared with $\omega=2\theta$.

## Bound and estimation foundations

**Das, Górecki, and Demkowicz-Dobrzański, “Universal time scalings of sensitivity in Markovian quantum metrology,” Physical Review A 111, L020403 (2025).** [Paper](https://doi.org/10.1103/PhysRevA.111.L020403) · [Equations](https://arxiv.org/html/2404.03954v2)

The adaptive information-growth inequality and its operators, including parameter-dependent noise, are inherited from Eqs. (2), (4), and (5). The zero-gauge nuisance-path substitution and matching constructions are worked out here. The general channel-bound method is not a contribution of this repository.

**Zhou, Zhang, Preskill, and Jiang, “Achieving the Heisenberg limit in quantum metrology using quantum error correction,” Nature Communications 9, 78 (2018).** [Paper](https://doi.org/10.1038/s41467-017-02510-3)

The known-noise Hamiltonian-not-in-Lindblad-span criterion and noiseless-ancilla control framework are established background. For a known transverse direction the present qubit signal is correctable. That fact does not remove a continuously unknown nuisance direction from the experiment.

**Abbasgholinejad et al., “Error-corrected function estimation advantage in multiparameter Hamiltonians,” arXiv:2609.16226v1 (2026).** [Paper](https://arxiv.org/abs/2609.16226v1)

Reduction of function estimation to one-parameter embeddings and correction of nuisance Hamiltonian parameters are close methodological precedents. Here the nuisance rotates the Lindblad operator, and the controlled family produces the explicit rate-contrast law. Neither nuisance elimination nor embedding optimization should be claimed as a newly invented general method.

## Noise-assisted recovery is established

**Cardona, Sarlette, and Rouchon, “Continuous-time Quantum Error Correction with Noise-assisted Quantum Feedback,” arXiv:1902.00115v4 (2019).** [Paper](https://arxiv.org/abs/1902.00115v4)

The authors introduce Brownian control with state-estimate-dependent gains to stabilize a three-qubit bit-flip code. Adding stochastic driving to encourage recovery is therefore a direct conceptual predecessor. The present result concerns an unknown error axis, preservation of an unknown signal, a universal fixed-rate obstruction, and an exact optimal precision coefficient—not the invention of noise-assisted feedback.

**Reiter, Sørensen, Zoller, and Muschik, “Dissipative quantum error correction and application to quantum sensing with trapped ions,” Nature Communications 8, 1822 (2017).** [Paper](https://doi.org/10.1038/s41467-017-01895-5)

Engineered dissipation for protected sensing is established. The present monitored protocol and nuisance-sensitive bound use different resources; the broad claim that dissipation can benefit quantum sensing is not new.

**Kwon, Fischer, Lee, and Jiang, “Restoring Heisenberg scaling in time via autonomous quantum error correction,” arXiv:2504.13168v3 (2026 revision).** [Preprint](https://arxiv.org/abs/2504.13168v3) · [Published article](https://doi.org/10.1038/s41534-026-01268-1)

Their sufficient-condition framework uses engineered autonomous correction, with a commuting-noise condition and quantified approximation over a chosen time interval. Our anticommuting-noise protocol uses ideal monitoring and a noiseless ancilla. These are different resource models, so the comparison does not establish practical superiority of either protocol.

## Informative noise is a different resource

**Chen, Chen, Liu, Miao, and Yuan, “Quantum Metrology Enhanced by Leveraging Informative Noise with Error Correction,” Physical Review Letters 133, 190801 (2024).** [Paper](https://doi.org/10.1103/PhysRevLett.133.190801)

This work exploits noise carrying information about the estimated parameter. In the physical model here, $L_j$ and $\gamma_j$ do not encode the target $\omega$; the target is in the Hamiltonian. The artificial joint parameter path used for a converse does not change that physical distinction.

## Physical control precedents

**Rower et al., “Qubit-state purity oscillations from anisotropic transverse noise,” Physical Review A 111, 032420 (2025).** [Paper](https://doi.org/10.1103/PhysRevA.111.032420) · [Model and supplement](https://arxiv.org/html/2409.12303v1)

The fluxonium noise-injection experiment is a precedent for fixed-axis transverse noise. Its supplementary frequency-shift discussion makes clear why unchanged signal response must be checked. It is not an implementation of the stopped protocol or a demonstration of a device restricted to incoherent rate access.

**Pechen and Rabitz, “Teaching the environment to control quantum systems,” Physical Review A 73, 062102 (2006).** [Paper](https://doi.org/10.1103/PhysRevA.73.062102)

Incoherent environment control is an established control resource. This supports distinguishing a reservoir-intensity knob from a coherent system drive; it does not certify the precise shared-axis resource on a particular device.

## Phase-estimation and stopping background

**Higgins et al., “Demonstrating Heisenberg-limited unambiguous phase estimation without adaptive measurements,” New Journal of Physics 11, 073023 (2009).** [Paper](https://doi.org/10.1088/1367-2630/11/7/073023) · [Preprint](https://arxiv.org/abs/0809.3308)

Multiscale interrogation for resolving phase ambiguity is inherited background. The global result here transfers such reasoning to exact stopped Ramsey operations and includes deadline failures. An elementary schedule and its risk bound are supplied in the proof notes.

**Gneiting, Rozhkov, and Nori, “Jump-time unraveling of Markovian open quantum systems,” Physical Review A 104, 062212 (2021).** [Paper](https://doi.org/10.1103/PhysRevA.104.062212)

Conditioning open-system dynamics on jump counts is established. Count-conditioned evolution and first-passage methods are not claimed as new formalisms. The specific shared-axis-cancelling sensing operation and its physical-time precision law are the statements at issue here.

## Contribution boundary

The central contribution is the combination of a nuisance-sensitive all-strategy converse, its removal by bounded shared-axis rate control, a matching optimal coefficient, and an exact stopped channel with charged timing and global-risk consequences. The finite-interval result is local and separately scoped. None of these statements asserts correction of arbitrary uncharacterized noise, fault-tolerant implementation, or exhaustive bibliographic priority.
