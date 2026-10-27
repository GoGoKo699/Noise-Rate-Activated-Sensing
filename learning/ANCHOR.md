# Shared educational anchor: Rivas and Huelga

[Learning route](README.md) · [30 milestones](MILESTONES.md) · [Worked tutorial](TUTORIAL.md) · [Scientific synthesis](../science/interpretation.md)

**Ángel Rivas and Susana F. Huelga, _Open Quantum Systems: An Introduction_**, SpringerBriefs in Physics (2012). The single educational anchor shared by the two sister projects is the open author version **[arXiv:1104.5242v2](https://arxiv.org/abs/1104.5242v2)**, dated 9 February 2012: [HTML](https://arxiv.org/html/1104.5242v2) · [PDF](https://arxiv.org/pdf/1104.5242v2) · [publisher record](https://doi.org/10.1007/978-3-642-23354-8).

The anchor supplies common language for channels, dilations, generators and microscopic reduction. In this repository the bridge asks how selecting a noisy coupling changes attainable frequency precision. The companion's [bridge from the same source](https://github.com/GoGoKo699/Markovian-Resolution-Limit/blob/main/learning/ANCHOR.md) asks how temporal access changes the distinguishability of complete controlled experiments. The two projects have their own thirty milestones; sharing an anchor does not identify their operational tasks or theorem assumptions.

Use selected sections when the corresponding concept appears. Reading the entire source first is not required. The source is linked, not copied or relicensed under the repository's MIT license. Other sources in [Related work](../references/RELATED_WORK.md), including Haase's metrology review and Milz–Modi's process tutorial, retain their research and attribution roles; they are not additional assigned educational anchors.

## Source map

Section numbers refer to the selected open version. These are foundation pointers, not claims that the source proves the local project's results.

| Source location | Foundation | Connection in this repository |
|---|---|---|
| §§2.1–2.4 | Norms, exponentials, semigroups and evolution families | Bound complete microscopic Hamiltonians and distinguish parameter differentiation from time evolution. |
| §3 | Unitary evolution and the interaction picture | Read the simultaneous signal–bath Hamiltonian in the [finite-strength model](../science/microscopic_global_precision.md#statistical-task-and-resources). |
| §§4.1–4.2 | Reduced maps, Kraus operators and dilations | Derive the [exact collision instrument](../science/microscopic_sensing.md#exact-parity-conditioned-cell-channel); protected ancillas are separate from the inaccessible bath. |
| §4.3 | Trace-norm contraction | Understand why physical processing cannot increase state distinguishability; reference-assisted channel and adaptive bounds need the additional arguments cited locally. |
| §§4.4–4.5 | Reversibility and composition of reduced maps | Separate exact endpoint channels from a claim about an intervened microscopic experiment. |
| §5.2, Theorem 5.1 and Eq. (46) | GKLS structure | Translate the [Markovian sensing generator](../science/model.md#parameters-and-normalization) and its rate convention. |
| §§6.1–6.3 | Microscopic equations and Markov limits | Understand what an approximation requires; the [finite-strength global theorem](../science/microscopic_global_precision.md) is proved directly rather than inherited from a limiting generator. |
| §6.2.7 | Failure of persistent factorization | Track conditional bath states without assuming a physical bath reset. |
| §6.4 and §§7.1–7.3 | Extensions, external driving and descriptions with memory | Locate the limitations of replacing microscopic dynamics by a reduced noise law under control. |

The common foundational route is channels and dilations → generators and rate conventions → microscopic reduction and its limits. The learning route then branches: nuisance-sensitive estimation here, controlled-process discrimination in the companion. Instruments and complete records, global estimation statistics, and adaptive resource bounds are explained in the project rather than attributed to the anchor.

## Notation and resource conventions

| In the anchor or this tutorial | Convention used in the research |
|---|---|
| System and environment $`A,B`$ | $`S,E`$; protected ancillary storage is accessible, while bath cells are not. |
| Dynamical map $`\mathcal E_{(t,s)}`$ and generator $`\mathcal L_t`$ | The Markovian counterpart uses a scalar rate $`\gamma(t)\in[a,b]`$ in its specified generator; the microscopic comparison uses an exact Hamiltonian in every cell. |
| Rates $`\gamma_k`$ and jump operators $`V_k`$ in Eq. (46) | Absorb a nonnegative rate into $`L_k=\sqrt{\gamma_k}V_k`$. Here $`L=\sqrt\gamma N_\phi`$ in the Markovian model. |
| Kraus operators $`K_\alpha`$ in §4.2 | $`K_0,K_1`$ denote exact no-flip and flip cell operators. A Kraus decomposition is not itself permission to observe the bath; parity encoding makes the stated branches accessible. |
| Time derivatives in evolution equations | Primes differentiate residual frequency at fixed $`\phi`$; dots in the converse denote total derivatives along its nuisance curve. Physical-time derivatives are written $`d/dt`$. |
| Terminal readout angle $`\vartheta`$ | A known terminal measurement setting, distinct from the unknown noise angle $`\phi`$ and the cell action $`\chi=gh`$. |
| Fixed nominal compensation $`\omega_0`$ | The microscopic target enters as $`\epsilon=\omega-\omega_0`$. Updating an estimate or readout basis does not change this Hamiltonian. |

The continuous-time rate-only model permits classical selection throughout $`[a,b]`$; the endpoint menu $`\{a,b\}`$ attains the same leading local coefficient and global risk order. The two finite-time minimax risks remain distinct, as defined in the [global task](../science/global_precision.md#statistical-task-and-theorem). Calibration uses the classical score $`W`$ and mean response $`f`$; neither is a Pauli operator or quantum Fisher information.

The global microscopic comparison fixes two distinct positive couplings, the cell length $`h`$ and a nonshrinking frequency interval. The budget is $`n`$ physical cells and at most $`n-1`$ nonterminal boundary contacts. Repetition, calibration, failed blocks and an early readout are charged. Protected storage contributes no extra signal generator. These conventions belong to the [statistical task](../science/microscopic_global_precision.md#statistical-task-and-resources), not to a substitution of time for the probe number in another metrology model.

### Rate normalization

For this repository's Pauli convention,

```math
\dot\rho=\kappa(Z\rho Z-\rho)
\quad\Longrightarrow\quad
\dot\rho_{01}=-2\kappa\rho_{01},
\qquad
\rho_{01}(t)=e^{-2\kappa t}\rho_{01}(0).
```

A dissipator coefficient and a contrast-decay rate differ here by two. Keep this convention when reading the [residual-dephasing result](../science/residual_dephasing.md) or translating the anchor's jump representation.

A useful secondary-source comparison is **Haase et al., [arXiv:1807.11882v4](https://arxiv.org/abs/1807.11882v4)**. On its printed p. 6, Eq. (17) writes $`\gamma(\sigma_z\rho\sigma_z-\rho)`$, whereas Eq. (18) uses contrast $`e^{-\gamma t}`$. With Pauli eigenvalues $`\pm1`$, these expressions use different rate normalizations. Match the dissipator coefficient to $`\kappa`$ or the contrast-decay rate to $`2\kappa`$, rather than equating symbols. This is a direct local normalization check, not an author-issued erratum or a second educational anchor.

## What is supplied locally

The [worked tutorial](TUTORIAL.md) introduces Ramsey likelihoods and the parity code before connecting the source language to the principal finite-strength result. The following steps need their own explanations and proofs:

1. **Shared nuisance and statistical task.** Complete likelihoods, efficient local information, worst-case squared error and a fixed identifiable band are different objects. See [tutorial 3](TUTORIAL.md#3-why-a-nuisance-parameter-costs-information) and the [global task](../science/microscopic_global_precision.md#statistical-task-and-resources).
2. **Exact microscopic records.** Two identical unknown transverse flips cancel, but the surviving phase depends on the observed sequence and the candidate frequency. The record probabilities also depend on frequency. See [tutorial 10](TUTORIAL.md#10-from-a-bounded-collision-to-an-observed-phase).
3. **Matching global bounds.** A uniform nuisance-curve converse constrains every allowed fixed-coupling controller. The two-coupling construction certifies record sensitivity on the whole band and resolves phase ambiguity with a fully charged estimator. See [microscopic global precision](../science/microscopic_global_precision.md) and [recorded-phase estimation](../science/recorded_phase_estimation.md).
4. **Markovian counterpart.** Sharp local coefficients, preset statistical designs and an exact stopped sensing operation have their own continuous-time proofs. The tutorial's [rate example](TUTORIAL.md#4-a-complete-rate-diversity-example) and [stopped channel](TUTORIAL.md#6-let-the-error-supply-its-own-recovery) explain those mechanisms; they do not approximate the finite-strength theorem without further work.
5. **Temporal access and timing information.** The companion owns the global contact law and the specified timing-menu limitation. The [shared-resource comparison](TUTORIAL.md#13-separate-strength-control-from-temporal-access) explains why these use a different controller class.

The [30 milestones](MILESTONES.md) organize these dependencies from local concepts to the complete scientific account. The full proofs and primary-source attribution remain in `science/` and `references/`. Learning examples, executable identity checks and internal review do not independently certify the theorems or their priority.
