# Noise-Rate-Activated Sensing

**An unknown error can supply its own recovery. Controlling its rate makes that recovery compatible with coherent sensing.**

This repository studies a qubit sensing a frequency while a fixed, unknown transverse error acts on it. A constant noise rate limits nuisance-adjusted information to linear growth in interrogation time, even with adaptive quantum control. Switching between two strictly positive rates, according to the observed error syndrome, restores quadratic growth without learning the error direction.

## The result

The sensor evolves as

$$
\frac{d\rho}{dt}=-i\frac{\omega}{2}[Z,\rho]
+\gamma\left(N_\phi\rho N_\phi-\rho\right),
\qquad N_\phi=\cos\phi\,X+\sin\phi\,Y.
$$

The target is $\omega$; $\phi$ is an arbitrary, fixed, continuously valued nuisance parameter. Write $\mathcal I_\omega^*(T)$ for the best local classical Fisher information after eliminating that nuisance, with all sensor exposure charged to the physical deadline $T$.

At a fixed rate $\gamma>0$,

$$
\mathcal I_\omega^*(T)\le \frac{T}{\gamma},
\qquad
\lim_{T\to\infty}\frac{\mathcal I_\omega^*(T)}{T}=\frac1\gamma.
$$

With syndrome-conditioned control of the same error operator at rates $0<a<b$,

$$
\lim_{T\to\infty}\frac{\mathcal I_\omega^*(T)}{T^2}
=\left(\frac{b-a}{b+a}\right)^2.
$$

The matching protocol uses one noiseless ancilla. Parity detects the error sector without reading the logical state. Successive errors cancel because $N_\phi^2=I$, but reverse the sign of signal accumulation because $N_\phi ZN_\phi=-Z$. Use rate $a$ in the code sector and $b$ in the error sector: the sensor spends more time accumulating the signal with the desired sign.

A stopping rule implements an **exact noiseless Ramsey operation** at prescribed effective time $d$, with mean physical duration $d(b+a)/(b-a)$. A hard deadline retains all failures. For rates $a$ and $3a$, a conservative finite-time certificate beats every fixed-rate-$a$ strategy whenever $aT>19$.

## Reading routes

| Purpose | Start here |
|---|---|
| Understand the mechanism | [Tutorial](docs/TUTORIAL.md) |
| Check the statistical task and physical resources | [Model](docs/MODEL.md) |
| Verify the converse and optimal control coefficient | [Theorems and proofs](docs/THEOREMS.md) |
| Check stopping costs, deadlines, and global estimation | [Stopped sensing](docs/STOPPED_SENSING.md) |
| Understand physical interpretation and finite-cadence scope | [Physical scope](docs/PHYSICAL_SCOPE.md) |
| Compare with prior work | [Related work and attribution](literature/RELATED_WORK.md) |
| Execute the checks | [Reproducibility](docs/REPRODUCIBILITY.md) |

The proofs also cover selectable signal strengths and noise rates. Global frequency estimation on a fixed bounded interval attains mean-square error $O(T^{-2})$ under the ideal monitored model. This global scaling statement is separate from the exact local-information coefficient.

## Scope

The principal theorem assumes Markovian noise with one shared, stable transverse axis, rate control that preserves the signal Hamiltonian, ideal fast syndrome extraction, and noiseless ancillary storage. Rate bounds are fixed independently of $T$; the noise is never turned off. The converse permits arbitrary parameter-independent adaptive system–ancilla operations but does not grant access to the bath or coherent application of the unknown error operator. Finite-interval syndrome measurements have a separate **local**, compensated-operating-point result.

The physical examples motivate the resource model; they are not demonstrations of the full protocol. The literature comparison distinguishes the present precision law from established noise-assisted correction and informative-noise metrology. Executable checks supplement the proofs and are not independent scientific review.

## Reproduce

```bash
python -m pip install -r requirements.txt
python scripts/check.py
python scripts/reproduce.py
```

The second command runs deterministic algebraic checks and seeded simulations. The third prints a numerical example without modifying tracked files.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).

[LLM reading guide](llms.txt) · [Agent instructions](AGENTS.md) · [MIT license](LICENSE)
