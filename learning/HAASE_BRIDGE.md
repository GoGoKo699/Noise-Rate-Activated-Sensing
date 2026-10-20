# Haase bridge: from open-system metrology to rate activation

[Learning route](README.md) · [30 milestones](MILESTONES.md) · [Overview](../README.md) · [Worked tutorial](TUTORIAL.md) · [Scientific synthesis](../science/interpretation.md)

## The educational anchor

**J. F. Haase, A. Smirne, J. Kołodyński, R. Demkowicz-Dobrzański, and S. F. Huelga, _Precision Limits in Quantum Metrology with Open Quantum Systems_, arXiv:1807.11882v4 (15 October 2018).**

[Versioned source](https://arxiv.org/abs/1807.11882v4) · [Versioned PDF](https://arxiv.org/pdf/1807.11882v4)

This tutorial review is the project's single selected educational anchor. The reading map below uses v4's printed page numbers, counting the title page as page 1. The source is linked, not copied into the repository or relicensed under its MIT license.

Start with the [worked tutorial](TUTORIAL.md). Its explanations supply the local connections; the [30-milestone map](MILESTONES.md) orders the understanding targets. Reading the entire source first is not required. The primary papers in [related work](../references/RELATED_WORK.md) remain research citations and proof dependencies, not additional educational anchors.

## Source map

| Source location | Use here |
|---|---|
| §II opening and §II.A–B, pp. 2–5; Eqs. (4)–(11) | Ramsey likelihood, information, exposure accounting |
| §III, pp. 6–7; Eqs. (24), (27)–(30) | Channels, generators, Kraus operators |
| §IV.A, p. 8; Eqs. (33)–(40) | Measurement information versus quantum information |
| §IV.B–C, pp. 8–11; Eqs. (41)–(47) | Channel bounds and attainability |
| §VI.B, pp. 19–20; Eqs. (85)–(86) | Known-noise correction with an ancilla |

Use §II.C, p. 5, only to compare probe-number scaling with time scaling. Use §II.D, pp. 5–6, for the dephasing example with the normalization note below. These are selective routes through the same source, not extra prerequisites.

## Translate the notation and the task

| Anchor notation | Repository meaning |
|---|---|
| Frequency $`\omega_0`$, Pauli matrices $`\sigma_x,\sigma_y,\sigma_z`$ | $`\omega`$ and $`X,Y,Z`$ |
| Phase $`\phi`$ in early Ramsey examples | $`\vartheta=\omega t`$, **not** our noise angle $`\phi`$ |
| Probe number $`N`$ | Fixed at one exposed sensor here; the ancilla does not sense |
| Interrogation time $`t`$, repetitions $`\nu`$, total $`T`$ | Equal-duration repeats cost $`\nu t`$; stopped times must be added explicitly |
| Classical $`F_{\rm cl}`$ and quantum $`F_Q`$ | Complete classical matrix $`J`$; efficient scalar $`\mathcal I_\omega`$; path QFI $`F_u`$ |
| $`L_{\omega_0,t}`$ in §IV.A | Symmetric logarithmic derivative, **not** a jump operator $`L_j`$ |
| $`\kappa`$ in §VI.B | An effective Hamiltonian operator, **not** our scalar parallel-noise rate |

The central comparison changes the physical time available to one sensor, not the number of exposed probes. A noiseless ancilla can store information but contributes no extra signal generator. Preparation, ideal controls, and readout have the same idealized cost convention on both sides. The [model](../science/model.md) defines the actual optimization; the anchor's parallel-channel bound is not silently substituted for the adaptive continuous-time theorem used here.

The comparison parameter $`u`$ in the converse is also not physical time. Dots on Lindblad operators there mean differentiation with respect to $`u`$. A derivative $`dF_u/dt`$ in the information-growth inequality is instead a time derivative. The [tutorial](TUTORIAL.md#7-from-a-protocol-to-an-all-strategy-bound) explains why these two derivatives appear together.

### Rate normalization when using the source

In v4, p. 6, Eq. (17) prints $`\gamma(\sigma_z\rho\sigma_z-\rho)`$, while Eq. (18) uses contrast $`e^{-\gamma t}`$. Under Pauli eigenvalues $`\pm1`$, those expressions differ by a factor of two. Directly,

```math
\frac{d\rho_{01}}{dt}=-2\kappa\rho_{01}
\quad\Longrightarrow\quad
\rho_{01}(t)=e^{-2\kappa t}\rho_{01}(0)
```

for this project's generator $`\kappa(Z\rho Z-\rho)`$. Match a *contrast decay rate* by setting it to $`2\kappa`$; match a *coefficient of the dissipator* to $`\kappa`$. Do not equate rates merely because they use the same letter. This is a local normalization check, not an assertion about an author-issued erratum. The project's [residual-dephasing formulas](../science/residual_dephasing.md) retain their existing convention.

## The bridge supplied locally

The anchor teaches the general estimation and open-system framework. The following steps belong to this project's own teaching and proof files.

| Learning step | Concrete question to resolve | Route |
|---|---|---|
| Ramsey experiment and cost | What is measured, and what does each repetition cost? | [Tutorial 1](TUTORIAL.md#1-one-qubit-one-likelihood-one-clock) |
| Logical code and error record | Why does parity reveal an error without revealing the phase? | [Tutorial 2](TUTORIAL.md#2-detect-an-error-without-reading-the-signal) |
| Shared nuisance and statistics | Why is $`J_{\omega\omega}`$ not the usable information when $`\phi`$ is unknown? | [Tutorial 3](TUTORIAL.md#3-why-a-nuisance-parameter-costs-information) → [model](../science/model.md) |
| Rate-diverse designs | How can labelled data separate two unknowns, and which design needs balancing? | [Tutorial 4–5](TUTORIAL.md#4-a-complete-rate-diversity-example) → [preset protocols](../science/preset_protocols.md) |
| Exact stopped output | What cancels on every completed path, and what is the physical cost? | [Tutorial 6](TUTORIAL.md#6-let-the-error-supply-its-own-recovery) → [stopped sensing](../science/stopped_sensing.md) |
| Universal converse | How does one parameter path constrain every allowed strategy? | [Tutorial 7](TUTORIAL.md#7-from-a-protocol-to-an-all-strategy-bound) → [theorems](../science/precision_bounds.md) |
| Global task and physical scope | What requires a global proof, and what changes the model? | [Tutorial 8–9](TUTORIAL.md#8-global-precision-is-a-separate-statement) → [global risk](../science/global_precision.md), [physical scope](../science/physical_scope.md) |

A small example explains an operation; it is not the proof of optimality. The authoritative claims remain in the specialist files. In particular, the adaptive information-growth inequality is imported from Das and colleagues, the fixed-recovery baseline is attributed to Tanggara and colleagues, and the global argument uses van Trees and multiscale estimation ingredients. Their roles are identified in [related work](../references/RELATED_WORK.md). These ingredients are explained in the project and attributed to their primary sources; they do not introduce a second educational anchor.

## Relation to the milestone map

The [background phase](MILESTONES.md#phase-i-background-and-preliminaries) builds the language needed to state the complete sensing task. The [narrative phase](MILESTONES.md#phase-ii-narrative-and-innovation) follows the fixed-rate obstruction, statistical rate separation, exact stopped output, and same-metric global comparison.

The milestone targets belong to the project, not to the source's table of contents. The source supplies foundations; the linked project proofs supply the nuisance-sensitive converses, protocol guarantees, timing law, and physical boundaries. Examples explain those connections without standing in for universal proofs.
