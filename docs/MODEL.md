# Model and statistical task

[Overview](../README.md) · [Proofs](THEOREMS.md) · [Stopped sensing](STOPPED_SENSING.md)

## Parameters and normalization

There is one exposed sensor qubit, with Pauli operators $X,Y,Z$. In setting $j$,

$$
H_j=\frac{s_j\omega}{2}Z,
\qquad L_j=\sqrt{\gamma_j}\,N_\phi,
\qquad N_\phi=\cos\phi\,X+\sin\phi\,Y.
$$

The master equation is $\dot\rho=-i[H_j,\rho]+L_j\rho L_j^\dagger-\{L_j^\dagger L_j,\rho\}/2$. In the main rate-only case, $s_j=1$ and $\gamma_j\in[a,b]$, where $0<a<b<\infty$. The finite-setting extension permits real known $s_j$ and positive known $\gamma_j$.

The target $\omega$ has units of inverse time. The angle $\phi$ is a fixed unknown point on a circle of period $\pi$ for the dissipator; a local coordinate suffices for its derivative. It is not redrawn at each jump or promised to lie in a finite set. The same $\phi$ applies to every setting. All fixed constants, including $a,b$, are independent of the time budget.

The factor $1/2$ in $H_j$ matters: noiseless rate-only sensing has optimal local information $T^2$. A source using $H=\theta Z$ instead has $\omega=2\theta$ and $\mathcal I_\omega=\mathcal I_\theta/4$.

## Allowed operations

Preparation, arbitrary parameter-independent system–ancilla operations, adaptive measurements, classical record processing, and noiseless ancillary storage are permitted. The signal and noise act trivially on the ancillas. Controls may depend on past outcomes and on a fixed nominal operating point; their settings are held fixed when differentiating parameters. The upper bounds allow arbitrarily large ancillary spaces and fast operations. The constructions need only one noiseless ancilla.

The additional rate resource is **classical selection of the scalar strength of the same Lindblad operator**. It includes selection based on a measured syndrome. It is not direct measurement of environmental outputs, coherent superposition of different bath implementations, or coherent access to a Hamiltonian proportional to the unknown $N_\phi$.

The ideal monitored construction is the continuous-syndrome limit of system–ancilla parity measurements. It does not assume an otherwise inaccessible environment record. For an initial logical state in the even-parity code, $Z$ preserves parity and $N_\phi$ flips it; thus ideal parity measurements identify the jump times without revealing the logical amplitudes.

Control, readout, and storage are ideal resources, rather than thermodynamic or hardware-cost models. Their common idealization is used in both sides of the precision comparison. The extra resource on the constructive side is bounded rate selection.

## Charged time and failures

$T$ is a hard physical exposure budget for one sensor, including calibration, waiting for errors, and unsuccessful attempts. Multiple sensing stages share that budget. No parallel-sensor factor is hidden in $T$.

When a logical output is ready, a parameter-independent decoding transfers it to the noiseless ancilla. Remaining noise on the now-discarded sensor is irrelevant. An unfinished run at the deadline is retained as an explicit failure. Assigning it a parameter-independent output can only reduce information and is legitimate for a lower bound.

A stopping time and its mean are not interchangeable with a hard deadline. The [stopped protocol](STOPPED_SENSING.md) first solves the exact duration law and then imposes a deadline.

## Information in the presence of a nuisance

For the complete classical outcome $x$ of a protocol and readout, let $J$ be its Fisher information matrix for $(\omega,\phi)$. Define the efficient information

$$
\mathcal I_\omega(J)=\inf_{c\in\mathbb R}
\begin{pmatrix}1&c\end{pmatrix}
J\begin{pmatrix}1\\c\end{pmatrix}.
$$

When $J_{\phi\phi}>0$, this is

$$
\mathcal I_\omega=J_{\omega\omega}
-\frac{J_{\omega\phi}^2}{J_{\phi\phi}}.
$$

The infimum definition also covers a singular nuisance block. If the outcome is independent of $\phi$, it reduces to $J_{\omega\omega}$; if the target score lies in the nuisance-score span, it is zero. For several nuisance parameters, replace $c$ by a vector.

A regular locally unbiased target estimator obeys, at the operating point,

$$
\mathbb E[\widehat\omega]=\omega,
\qquad \partial_\omega\mathbb E[\widehat\omega]=1,
\qquad \partial_\phi\mathbb E[\widehat\omega]=0.
$$

Its variance is at least $1/\mathcal I_\omega$ for the complete experiment. This statement is local, and is not an unrestricted finite-sample or global mean-square-error theorem. Independent repetitions contribute their exposure and information normally.

$\mathcal I_\omega^*(T)$ is the supremum over the allowed protocols and final measurements at budget $T$. The proofs bound any such measurement through a one-parameter submodel and the quantum Fisher information of its full classical–quantum output. They do not identify the target-only entry of a quantum Fisher matrix with an achievable multiparameter precision.

For a flagged successful pure Ramsey operation of known signed time $D$, equatorial readout has local information $D^2$. Randomizing and recording the equatorial angle avoids isolated zero-probability readout points. When the duration record is parameter-independent and the output is independent of $\phi$, the unconditional information is the success-weighted expectation of $D^2$.

## The nuisance-path argument

Hold a candidate protocol fixed and restrict its unknown parameters to

$$
\omega(u)=\omega_0+u,
\qquad \phi(u)=\phi_0+cu.
$$

For every chosen $c$, efficient target information is no greater than the classical information along this path, which is no greater than its output quantum Fisher information $F_u$. Equivalently, a locally unbiased target estimator remains locally unbiased for $u$ along the path.

The noise is not physically assumed to encode the target frequency. The path is a mathematical comparison submodel of a two-parameter experiment. This distinction is important when comparing with informative-noise metrology.

The foundations and closest noise model are attributed in [related work](../literature/RELATED_WORK.md).
