# Noise-Rate-Activated Sensing

**Noise-rate diversity can remove the precision obstruction created by an unknown error direction.**

This repository studies a qubit sensing a frequency while a fixed, unknown transverse error acts on it. A single fixed noise rate limits nuisance-adjusted information to linear growth in interrogation time, even with adaptive quantum control. Access to two strictly positive rates restores quadratic local information without calibrating the error direction. Preset rate choices suffice for that local precision law; a separate rate-feedback protocol implements an exact noiseless sensing operation at a fully charged random duration.

The global comparison uses the same squared-error criterion on both sides: over a fixed bounded frequency interval, optimal worst-case risk scales as inverse time at one fixed rate and as inverse time squared with rate access. It allows biased estimators and counts every trial and failed stop.

## The result

The sensor evolves as

$$
\frac{d\rho}{dt}=-i\frac{\omega}{2}[Z,\rho]
+\gamma\left(N_\phi\rho N_\phi-\rho\right),
\qquad N_\phi=\cos\phi\,X+\sin\phi\,Y.
$$

The target is $\omega$; $\phi$ is an arbitrary, fixed, continuously valued nuisance parameter shared by the settings and pooled trials. Write $\mathcal I_\omega^*(T)$ for the best local classical Fisher information after eliminating that nuisance, with all sensor exposure charged to the physical deadline $T$.

At a fixed rate $\gamma>0$,

$$
\mathcal I_\omega^*(T)\le \frac{T}{\gamma},
\qquad
\lim_{T\to\infty}\frac{\mathcal I_\omega^*(T)}{T}=\frac1\gamma.
$$

With classical access to the same error operator at rates $0<a<b$,

$$
\lim_{T\to\infty}\frac{\mathcal I_\omega^*(T)}{T^2}
=\left(\frac{b-a}{b+a}\right)^2.
$$

The same bounds permit arbitrary parameter-independent adaptive system–ancilla controls. The extra resource in the positive result is rate diversity, not access to the bath or a coherent drive about the unknown axis. For global minimax mean-square error $R(T;\Omega)$ over a fixed interval $\Omega$,

$$
R_{\mathrm{fixed}}(T;\Omega)=\Theta(T^{-1}),
\qquad R_{[a,b]}(T;\Omega)=\Theta(T^{-2}).
$$

The [global-risk proof](docs/GLOBAL_RISK.md) does not infer this result from a local Cramér–Rao bound. It supplies lower bounds valid for biased estimators and matching upper scalings. Optimal global constants are not asserted.

## Local precision and exact sensing are different guarantees

**Preset local protocols.** Apply the same sensor recovery $X$ after every detected error and retain the counts. A balanced two-block echo gives the optimal leading coefficient without adapting the rate to the syndrome. Alternatively, choose a single rate at the start of each interrogation and retain that label. The optimal randomization probability attains the same leading coefficient; a fair choice needs no numerical rate calibration and retains at least half of it. These protocols still require syndrome-triggered recovery and do not cancel the nuisance on every trajectory.

**Exact stopped sensing.** Do not correct the errors. Successive errors cancel because $N_\phi^2=I$, but reverse the sign of signal accumulation because $N_\phi ZN_\phi=-Z$. Use rate $a$ in the code sector and $b$ in the error sector, and stop when the observed signed interrogation time reaches a prescribed value $d$. Every completed run is an exact direction-independent Ramsey operation, with mean physical duration $d(b+a)/(b-a)$. Hard-deadline failures are retained.

Both constructions use one noiseless ancilla. The stopped channel supports the global upper scaling by resolving phase ambiguity at several prescribed effective times. That theorem is separate from the preset protocols' local-information coefficients. A repetition of duration $T$ costs $T$ each time; repetitions are never free resources.

## Learning anchor

The single educational anchor is **Haase et al., _Precision Limits in Quantum Metrology with Open Quantum Systems_, arXiv:1807.11882v4**. The [learning guide](docs/LEARNING_GUIDE.md) maps its sections and notation to the project; the [worked tutorial](docs/TUTORIAL.md) supplies the bridge from Ramsey likelihoods to nuisance elimination, rate diversity, stopped channels, and global precision. No whole-book prerequisite is imposed. Primary research citations remain separate from this educational anchor.

## Reading routes

| Purpose | Start here |
|---|---|
| See the complete scientific claim and proof map | [Scientific synthesis](docs/SCIENTIFIC_SYNTHESIS.md) |
| Learn from the selected anchor | [Section and notation map](docs/LEARNING_GUIDE.md) → [Worked tutorial](docs/TUTORIAL.md) |
| Check the statistical task and physical resources | [Model](docs/MODEL.md) |
| Verify local optimality and the selectable-setting criterion | [Theorems and proofs](docs/THEOREMS.md) |
| Compare the same global error criterion | [Global precision](docs/GLOBAL_RISK.md) |
| Compare preset controls and calibration requirements | [Preset protocols](docs/PRESET_PROTOCOLS.md) |
| Check exact channels, stopping costs, and global achievability | [Stopped sensing](docs/STOPPED_SENSING.md) |
| Check physical assumptions and a quantitative imperfection | [Physical scope](docs/PHYSICAL_SCOPE.md) · [Residual dephasing](docs/RESIDUAL_DEPHASING.md) |
| Compare with prior work | [Related work and attribution](literature/RELATED_WORK.md) |
| Execute the checks and reproduce the examples | [Reproducibility](docs/REPRODUCIBILITY.md) |

## Scope

The principal theorem assumes Markovian noise with one shared, stable transverse axis, rate selection that preserves the signal Hamiltonian, ideal fast syndrome extraction, and noiseless ancillary storage. Rate bounds are fixed independently of $T$; the noise is never turned off. The converse does not grant bath-output access, indefinite causal order, or coherent application of the unknown error operator. Finite-interval syndrome measurements have a separate **local**, compensated-operating-point result.

An additional unobserved parallel dephasing rate $\kappa>0$ changes the asymptotic bound to $\mathcal I_\omega^*(T)\le T/(4\kappa)$. The [quantified finite-time example](docs/RESIDUAL_DEPHASING.md#a-certified-finite-time-advantage-with-nonzero-dephasing) retains an advantage at nonzero $\kappa$; it is not a fault-tolerance theorem. The physical examples motivate the resource model rather than demonstrate the full protocol. The literature comparison distinguishes these results from established fixed-recovery sensing, noise-assisted correction, and informative-noise metrology.

## Reproduce

```bash
python -m pip install -r requirements.txt
python scripts/check.py
python scripts/reproduce.py
python scripts/reproduce_evidence.py
```

The checks cover algebra, complete likelihoods, timing laws, risk-bound ingredients, and finite-advantage certificates. The two example commands print results without modifying files unless an output path is explicitly supplied. Tests supplement the proofs; they are not independent scientific review.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).

[LLM reading guide](llms.txt) · [Agent instructions](AGENTS.md) · [MIT license](LICENSE)
