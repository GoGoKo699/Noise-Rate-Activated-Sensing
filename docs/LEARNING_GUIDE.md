# Learning guide: one anchor and a bridge to this project

[Overview](../README.md) · [Worked tutorial](TUTORIAL.md) · [Scientific synthesis](SCIENTIFIC_SYNTHESIS.md)

## The educational anchor

**J. F. Haase, A. Smirne, J. Kołodyński, R. Demkowicz-Dobrzański, and S. F. Huelga, _Precision Limits in Quantum Metrology with Open Quantum Systems_, arXiv:1807.11882v4 (15 October 2018).**

[Versioned source](https://arxiv.org/abs/1807.11882v4) · [Versioned PDF](https://arxiv.org/pdf/1807.11882v4)

This tutorial review is the project's single selected educational anchor. The reading map below uses v4's printed page numbers, counting the title page as page 1. The source is linked, not copied into the repository or relicensed under its MIT license.

Start with the [worked tutorial](TUTORIAL.md). Its explanations and an accompanying chat course supply prerequisites when needed; reading the entire source first is not required. The primary papers in [related work](../literature/RELATED_WORK.md) remain research citations and proof dependencies, not additional educational anchors.

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
| Frequency $\omega_0$, Pauli matrices $\sigma_x,\sigma_y,\sigma_z$ | $\omega$ and $X,Y,Z$ |
| Phase $\phi$ in early Ramsey examples | $\vartheta=\omega t$, **not** our noise angle $\phi$ |
| Probe number $N$ | Fixed at one exposed sensor here; the ancilla does not sense |
| Interrogation time $t$, repetitions $\nu$, total $T$ | Equal-duration repeats cost $\nu t$; stopped times must be added explicitly |
| Classical $F_{\rm cl}$ and quantum $F_Q$ | Complete classical matrix $J$; efficient scalar $\mathcal I_\omega$; path QFI $F_u$ |
| $L_{\omega_0,t}$ in §IV.A | Symmetric logarithmic derivative, **not** a jump operator $L_j$ |
| $\kappa$ in §VI.B | An effective Hamiltonian operator, **not** our scalar parallel-noise rate |

The central comparison changes the physical time available to one sensor, not the number of exposed probes. A noiseless ancilla can store information but contributes no extra signal generator. Preparation, ideal controls, and readout have the same idealized cost convention on both sides. The [model](MODEL.md) defines the actual optimization; the anchor's parallel-channel bound is not silently substituted for the adaptive continuous-time theorem used here.

The comparison parameter $u$ in the converse is also not physical time. Dots on Lindblad operators there mean differentiation with respect to $u$. A derivative $dF_u/dt$ in the information-growth inequality is instead a time derivative. The [tutorial](TUTORIAL.md#7-from-a-protocol-to-an-all-strategy-bound) explains why these two derivatives appear together.

### Rate normalization when using the source

In v4, p. 6, Eq. (17) prints $\gamma(\sigma_z\rho\sigma_z-\rho)$, while Eq. (18) uses contrast $e^{-\gamma t}$. Under Pauli eigenvalues $\pm1$, those expressions differ by a factor of two. Directly,

$$
\frac{d\rho_{01}}{dt}=-2\kappa\rho_{01}
\quad\Longrightarrow\quad
\rho_{01}(t)=e^{-2\kappa t}\rho_{01}(0)
$$

for this project's generator $\kappa(Z\rho Z-\rho)$. Match a *contrast decay rate* by setting it to $2\kappa$; match a *coefficient of the dissipator* to $\kappa$. Do not equate rates merely because they use the same letter. This is a local normalization check, not an assertion about an author-issued erratum. The project's [residual-dephasing formulas](RESIDUAL_DEPHASING.md) retain their existing convention.

## The bridge supplied locally

The anchor teaches the general estimation and open-system framework. The following steps belong to this project's own teaching and proof files.

| Learning step | Concrete question to resolve | Route |
|---|---|---|
| Ramsey experiment and cost | What is measured, and what does each repetition cost? | [Tutorial 1](TUTORIAL.md#1-one-qubit-one-likelihood-one-clock) |
| Logical code and error record | Why does parity reveal an error without revealing the phase? | [Tutorial 2](TUTORIAL.md#2-detect-an-error-without-reading-the-signal) |
| Shared nuisance and statistics | Why is $J_{\omega\omega}$ not the usable information when $\phi$ is unknown? | [Tutorial 3](TUTORIAL.md#3-why-a-nuisance-parameter-costs-information) → [model](MODEL.md) |
| Rate-diverse designs | How can labelled data separate two unknowns, and which design needs balancing? | [Tutorial 4–5](TUTORIAL.md#4-a-complete-rate-diversity-example) → [preset protocols](PRESET_PROTOCOLS.md) |
| Exact stopped output | What cancels on every completed path, and what is the physical cost? | [Tutorial 6](TUTORIAL.md#6-let-the-error-supply-its-own-recovery) → [stopped sensing](STOPPED_SENSING.md) |
| Universal converse | How does one parameter path constrain every allowed strategy? | [Tutorial 7](TUTORIAL.md#7-from-a-protocol-to-an-all-strategy-bound) → [theorems](THEOREMS.md) |
| Global task and physical scope | What requires a global proof, and what changes the model? | [Tutorial 8–9](TUTORIAL.md#8-global-precision-is-a-separate-statement) → [global risk](GLOBAL_RISK.md), [physical scope](PHYSICAL_SCOPE.md) |

A small example explains an operation; it is not the proof of optimality. The authoritative claims remain in the specialist files. In particular, the adaptive information-growth inequality is imported from Das and colleagues, the fixed-recovery baseline is attributed to Tanggara and colleagues, and the global argument uses van Trees and multiscale estimation ingredients. Their roles are identified in [related work](../literature/RELATED_WORK.md). No second textbook is assigned to make these steps the learner's responsibility.

## Coaching and readiness

In a requested chat course, explain the material directly using **Revise → Learn → Test**. Revise only the prerequisite currently needed, teach a manageable next step, and ask one selection-only question. Supply the explanation before testing it. A mistake triggers targeted repair and a later transfer question, rather than automatic advancement. This guide is not itself an instruction to launch a quiz during repository maintenance.

Prefer genuine native click-to-select answer controls when the interface supports them. Plain Markdown choices, disclosure triangles, or links are not answer-submission buttons. When native controls are unavailable, state that once and use a minimal selection-only fallback; do not require essays or typed derivations as a substitute. Do not claim a static repository implements an interactive tutor.

Readiness requires demonstrated understanding of six domains: physical task and charged resources; the code and conditional evolution; nuisance-adjusted statistics; the two sensing mechanisms and calibration tradeoffs; the converse and its imported premise; and local-versus-global claims with physical boundaries. For each domain, check a worked situation and a later changed situation. Resolve mistaken distinctions and revisit them in mixed questions before declaring readiness. A selection-only test can assess interpretation of a derivation without requiring the learner to type it out.

State readiness explicitly only when that evidence supports it. Reading a page, accepting the anchor, finishing a repository, or passing software tests is not evidence of the author's mastery. Source sections and project proofs remain available for discussion, not an ever-expanding assignment list.
