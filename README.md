# Noise-Rate-Activated Sensing

**Noise-rate diversity can remove the precision obstruction created by an unknown error direction.**

This repository studies a qubit sensing a frequency while a fixed, unknown transverse error acts on it. A single fixed noise rate limits nuisance-adjusted information to linear growth in interrogation time, even with adaptive quantum control. Access to two strictly positive rates restores quadratic local information without calibrating the error direction. Preset rate choices suffice for that local precision law; a separate rate-feedback protocol implements an exact noiseless sensing operation at a fully charged random duration.

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

The same bounds permit arbitrary parameter-independent adaptive system–ancilla controls. The extra resource in the positive result is rate diversity, not access to the bath or a coherent drive about the unknown axis.

## Local precision and exact sensing are different guarantees

**Preset local protocols.** Apply the same sensor recovery $X$ after every detected error and retain the counts. A balanced two-block echo gives the optimal leading coefficient without adapting the rate to the syndrome. Alternatively, choose a single rate at the start of each interrogation and retain that label. The optimal randomization probability attains the same leading coefficient; a fair choice needs no numerical rate calibration and retains at least half of it. These protocols still require syndrome-triggered recovery and do not cancel the nuisance on every trajectory.

**Exact stopped sensing.** Do not correct the errors. Successive errors cancel because $N_\phi^2=I$, but reverse the sign of signal accumulation because $N_\phi ZN_\phi=-Z$. Use rate $a$ in the code sector and $b$ in the error sector, and stop when the observed signed interrogation time reaches a prescribed value $d$. Every completed run is an exact direction-independent Ramsey operation, with mean physical duration $d(b+a)/(b-a)$. Hard-deadline failures are retained.

Both constructions use one noiseless ancilla. The stopped channel supports global frequency estimation on a fixed bounded interval with mean-square error $O(T^{-2})$. That global theorem is separate from the preset protocols' local-information coefficients. A repetition of duration $T$ costs $T$ each time; repetitions are never free resources.

## Reading routes

| Purpose | Start here |
|---|---|
| Understand the mechanism and the two guarantees | [Tutorial](docs/TUTORIAL.md) |
| Check the statistical task and physical resources | [Model](docs/MODEL.md) |
| Verify the converse and optimal control coefficient | [Theorems and proofs](docs/THEOREMS.md) |
| Compare preset controls and calibration requirements | [Preset protocols](docs/PRESET_PROTOCOLS.md) |
| Check stopping costs, deadlines, and global estimation | [Stopped sensing](docs/STOPPED_SENSING.md) |
| Understand physical interpretation and finite-cadence scope | [Physical scope](docs/PHYSICAL_SCOPE.md) |
| Compare with prior work | [Related work and attribution](literature/RELATED_WORK.md) |
| Execute the checks | [Reproducibility](docs/REPRODUCIBILITY.md) |

The proofs also cover selectable signal strengths and noise rates. Exact finite-time information certificates compare the preset and stopped constructions with the universal fixed-rate bound, without claiming finite-time optimality of those particular protocols.

## Scope

The principal theorem assumes Markovian noise with one shared, stable transverse axis, rate selection that preserves the signal Hamiltonian, ideal fast syndrome extraction, and noiseless ancillary storage. Rate bounds are fixed independently of $T$; the noise is never turned off. The converse does not grant bath-output access or coherent application of the unknown error operator. Finite-interval syndrome measurements have a separate **local**, compensated-operating-point result.

The physical examples motivate the resource model; they are not demonstrations of the full protocol. The literature comparison distinguishes the precision law from established fixed-recovery sensing, noise-assisted correction, and informative-noise metrology. Executable checks supplement the proofs and are not independent scientific review.

## Reproduce

```bash
python -m pip install -r requirements.txt
python scripts/check.py
python scripts/reproduce.py
```

The second command runs deterministic algebraic checks, complete-likelihood checks, and seeded simulations. The third prints the stopped-sensing numerical example without modifying tracked files.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).

[LLM reading guide](llms.txt) · [Agent instructions](AGENTS.md) · [MIT license](LICENSE)
