# Noise-Rate-Activated Sensing

**Noise-rate diversity can remove the precision obstruction created by an unknown error direction.**

Part of **Quantum Noise under Control**, alongside [**Markovian Resolution Limit**](https://github.com/GoGoKo699/Markovian-Resolution-Limit). This repository studies noise-strength selection; its sister studies temporal resolution and access inside microscopic interactions.

This repository studies frequency estimation with a shared, continuously unknown transverse error direction. Its principal result compares one positive coupling with a menu of two at finite microscopic strength, with calibration, repetitions and failed records charged.

A separate Markovian analysis proves the same change of global scaling and identifies sharp local information coefficients. Preset rate choices attain the local optimum; rate feedback supplies an exact direction-independent stopped sensing operation with its random duration fully charged. These are complementary guarantees, each with its own proof. The [scientific synthesis](science/interpretation.md#principal-argument-and-supporting-results) separates the principal microscopic argument from its supporting results and the companion's temporal-access claims.

## Explanatory report

Read the [complete explanatory report (PDF)](learning/report/Noise_Rate_Activated_Sensing_Report.pdf) for a self-contained account from quantum-clock basics to the global precision separation, its proof and its physical limits. It introduces the required quantum and statistical ideas as they arise, with worked examples and explanations of the formulas.

## Global precision at finite microscopic strength

The [collision theorem](science/microscopic_global_precision.md) fixes a cell duration $`h`$, nominal compensation and two couplings $`0<g_a<g_b<\pi/(4h)`$. Over $`n`$ cells, all controls occur at boundaries and use at most $`n-1`$ nonterminal contacts. On one fixed, nonshrinking identifiable frequency interval,

```math
R_g^*(n)=\Theta(n^{-1})\quad(g=g_a\text{ or }g_b),
\qquad
R_{\{g_a,g_b\}}^*(n)=\Theta(n^{-2}).
```

The shared unknown direction cancels exactly in retained even-parity records. Their known nonlinear phase functions support [global estimation with recorded phases](science/recorded_phase_estimation.md), using paid calibration, nested intervals and a deterministic multiscale schedule. Only measurement bases adapt to earlier estimates; the physical compensation stays fixed. A smooth nuisance curve gives the matching fixed-coupling lower bound against all allowed adaptive boundary controllers. Optimal global constants and maximal bandwidth are not asserted.

## The Markovian counterpart

The sensor evolves as

```math
\frac{d\rho}{dt}=-i\frac{\omega}{2}[Z,\rho]
+\gamma\left(N_\phi\rho N_\phi-\rho\right),
\qquad N_\phi=\cos\phi\,X+\sin\phi\,Y.
```

The target is $`\omega`$; $`\phi`$ is an arbitrary, fixed, continuously valued nuisance parameter shared by the settings and pooled trials. Write $`\mathcal I_\omega^*(T)`$ for the best local classical Fisher information after eliminating that nuisance, with all sensor exposure charged to the physical deadline $`T`$.

At a fixed rate $`\gamma>0`$,

```math
\mathcal I_\omega^*(T)\le \frac{T}{\gamma},
\qquad
\lim_{T\to\infty}\frac{\mathcal I_\omega^*(T)}{T}=\frac1\gamma.
```

With classical selection $`\gamma(t)\in[a,b]`$ for the same error operator, where $`0<a<b`$,

```math
\lim_{T\to\infty}\frac{\mathcal I_\omega^*(T)}{T^2}
=\left(\frac{b-a}{b+a}\right)^2.
```

The same bounds permit arbitrary parameter-independent adaptive system–ancilla controls. The extra resource in the positive result is rate diversity, not access to the bath or a coherent drive about the unknown axis. For global minimax mean-square error $`R_{\mathcal A}^*(T;\Omega)`$ over a fixed interval $`\Omega`$,

```math
R_{\mathrm{fixed}}^*(T;\Omega)=\Theta(T^{-1}),
\qquad R_{[a,b]}^*(T;\Omega)=\Theta(T^{-2}).
```

The endpoint menu $`\{a,b\}`$ suffices for attainment; its finite-time risk and the interval-menu risk are distinguished in the [global-risk proof](science/global_precision.md). That proof does not infer this result from a local Cramér–Rao bound. It supplies lower bounds valid for biased estimators and matching upper scalings. Optimal global constants are not asserted.

## Local precision and exact sensing are different guarantees

**Preset local protocols.** Apply the same sensor recovery $`X`$ after every detected error and retain the counts. A balanced two-block echo gives the optimal leading coefficient without adapting the rate to the syndrome. Alternatively, choose a single rate at the start of each interrogation and retain that label. The optimal randomization probability attains the same leading coefficient; a fair choice needs no numerical rate calibration and retains at least half of it. These protocols still require syndrome-triggered recovery and do not cancel the nuisance on every trajectory.

**Exact stopped sensing.** Do not correct the errors. Successive errors cancel because $`N_\phi^2=I`$, but reverse the sign of signal accumulation because $`N_\phi ZN_\phi=-Z`$. Use rate $`a`$ in the code sector and $`b`$ in the error sector, and stop when the observed signed interrogation time reaches a prescribed value $`d`$. Every completed run is an exact direction-independent Ramsey operation, with mean physical duration $`d(b+a)/(b-a)`$. Hard-deadline failures are retained.

Both constructions use one noiseless ancilla. The stopped channel supports the global upper scaling by resolving phase ambiguity at several prescribed effective times. That theorem is separate from the preset protocols' local-information coefficients. A repetition of duration $`T`$ costs $`T`$ each time; repetitions are never free resources.

## Learn the project

Both sister repositories use **Ángel Rivas and Susana F. Huelga, _Open Quantum Systems: An Introduction_ (2012), arXiv:1104.5242v2**, as their single common educational anchor. The [source bridge](learning/ANCHOR.md) connects its channels, generators and microscopic dynamics to this sensing problem. The [worked tutorial](learning/TUTORIAL.md) supplies the estimation, nuisance and recorded-phase arguments that the source does not teach. Selective reading is sufficient; research citations remain distinct from the anchor.

The [30-milestone map](learning/MILESTONES.md) has **13 background/preliminaries** and **17 narrative/innovation** targets. Its principal route reaches the finite-strength global coupling separation, with the Markovian coefficients and stopped channel as separately proved counterparts. The companion's [learning route](https://github.com/GoGoKo699/Markovian-Resolution-Limit/blob/main/learning/ANCHOR.md) uses the same foundation for the resolution law, global contact budget and timing distinction. Each repository retains its own project-defined thirty targets.

## Read the science

The [scientific entrypoint](science/README.md) is the complete topic index. The principal reading routes are:

| Purpose | Start here |
|---|---|
| Follow the principal finite-strength proof | [Collision instrument](science/microscopic_sensing.md) → [Identifiability](science/microscopic_identifiability.md) → [Recorded-phase estimator](science/recorded_phase_estimation.md) → [Global theorem](science/microscopic_global_precision.md) |
| Follow the Markovian counterpart | [Model](science/model.md) → [Local bounds](science/precision_bounds.md) → [Stopped sensing](science/stopped_sensing.md) → [Global theorem](science/global_precision.md) |
| Compare guarantees and resource assumptions | [Scientific synthesis](science/interpretation.md) · [Physical scope](science/physical_scope.md) |
| Check attribution or reproduce calculations | [Related work](references/RELATED_WORK.md) · [Verification](verification/README.md) |

## Scope

The Markovian theorem assumes one shared, stable transverse axis, rate selection that preserves the signal Hamiltonian, ideal fast syndrome extraction, and noiseless ancillary storage. Rate bounds are fixed independently of $`T`$; the noise is never turned off. The converse does not grant bath-output access, indefinite causal order, or coherent application of the unknown error operator. Finite-interval syndrome measurements have a separate **local**, compensated-operating-point result.

A [bounded collision realization](science/microscopic_sensing.md) has [exact optimal local coefficients](science/microscopic_precision.md) and the separate [global separation](science/microscopic_global_precision.md) above. The boundary restriction matters: the companion [global contact theorem](https://github.com/GoGoKo699/Markovian-Resolution-Limit/blob/main/science/global_contact_precision.md) permits at most $`m`$ contacts inside cells while keeping at most $`n-1`$ total contacts. At one fixed coupling it proves worst-case risk of order $`1/[h^2(n+m^2)]`$ on a suitable fixed band. Its estimator uses a menu of echoed and untouched cells, with complete records and all costs charged. This is an additional temporal resource.

[Clock resonances](https://github.com/GoGoKo699/Markovian-Resolution-Limit/blob/main/science/sensing_bridge.md#frequency-aliases-of-the-collision-clock) make some distinct frequencies indistinguishable to every fixed-coupling boundary-only controller, so the fixed-band qualification is substantive. For the companion's restricted menu of plain cells and one-pulse echoes, [timing information](https://github.com/GoGoKo699/Markovian-Resolution-Limit/blob/main/science/timing_precision.md) also matters: a supplied known fixed displacement preserves quadratic global order on a suitable band with a linear inside-cell contact allowance. Learning the offset is not included. Fixed nonzero hidden independent two-point jitter instead gives inverse-time optimal global risk, despite quadratic local information at compensation. The jitter converse does not cover extra interior pulses or coupling selection.

An additional unobserved parallel dephasing rate $`\kappa>0`$ changes the asymptotic bound to $`\mathcal I_\omega^*(T)\le T/(4\kappa)`$. The [quantified finite-time example](science/residual_dephasing.md#a-certified-finite-time-advantage-with-nonzero-dephasing) retains an advantage at nonzero $`\kappa`$; it is not a fault-tolerance theorem. The physical examples motivate the resource model rather than demonstrate the full protocol. The literature comparison distinguishes these results from established fixed-recovery sensing, noise-assisted correction, and informative-noise metrology.

## Reproduce

```bash
python -m pip install -r requirements.txt
python scripts/check.py
python scripts/check_reproducibility.py
python scripts/reproduce.py
python scripts/reproduce_evidence.py
```

The checks cover algebra, complete likelihoods, timing laws, risk-bound ingredients, and finite-advantage certificates. The two example commands print results without modifying files unless an output path is explicitly supplied. Tests supplement the proofs; they are not independent scientific review.

## Purpose and contact

The project is currently under collaboration. For questions, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).

[LLM reading guide](llms.txt) · [Agent instructions](AGENTS.md) · [MIT license](LICENSE)
