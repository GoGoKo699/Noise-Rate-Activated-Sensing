# Understanding the sensing mechanism

[Overview](../README.md) · [Precise model](MODEL.md) · [Proofs](THEOREMS.md)

## The starting question

A qubit accumulates a phase proportional to an unknown frequency. Noise occasionally flips it about some axis in the transverse plane. The axis is stable, but its angle is unknown. Detecting that an error occurred does not automatically tell us which coherent recovery to apply.

Knowing the angle and learning the angle during the experiment are different resources. When it is known, recovery after every error preserves ordinary noiseless phase accumulation. When it is continuously unknown, its uncertainty can imitate a change of signal frequency. The fixed-rate theorem bounds all adaptive strategies, including those trying to learn and correct simultaneously. The [model](MODEL.md) explains the statistical distinction.

## Two errors know how to cancel

Write the unknown error as $N_\phi=\cos\phi\,X+\sin\phi\,Y$. Even without knowing $\phi$, we know that $N_\phi^2=I$. Letting the same error occur twice returns the sensor to the original sector.

But the signal changes sign in between: $N_\phi ZN_\phi=-Z$. If the first waiting interval lasts $\tau_+$ and the second lasts $\tau_-$, the resulting phase is

$$
\omega(\tau_+-\tau_-),
$$

not $\omega(\tau_++\tau_-)$. Two errors remove the unknown angle, but can also undo the signal we wanted.

## An ancilla records the sector, not the answer

Store the logical amplitudes in $|00\rangle$ and $|11\rangle$. A transverse sensor error moves them to the odd-parity sector. A parity measurement distinguishes even from odd without distinguishing the two logical amplitudes. It therefore reveals the sign with which the signal currently accumulates without measuring the unknown phase.

No recovery pulse is required after a jump. Keep a classical clock whose sign is positive in the code and negative in the error sector.

## Increase the noise in the error sector

Use rate $a$ while the clock runs forward and rate $b>a$ while it runs backward. The backward intervals are shorter on average. The long-time fraction of useful signed interrogation is

$$
r=\frac{b-a}{b+a}.
$$

The word “increase” matters: $a$ remains positive. We are not turning the noise off, and we do not need infinitely strong correction. The bounded ratio between two positive rates creates a net signal drift.

The contribution is not the generic observation that extra noise can help correction. The [literature comparison](../literature/RELATED_WORK.md) explains that precedent. The precision result identifies when this extra control removes an unknown-direction obstruction and how much useful phase can optimally accumulate.

## Stop the signed clock, not the physical clock

Choose a desired effective interrogation time $d$. Stop when the signed clock first reaches it. At that instant the sensor is in the code and the output is exactly the ordinary Ramsey operation of duration $d$.

The physical duration is random. Its mean is $d/r$, not $d$. At equal rates the same stopping rule eventually succeeds, but its mean duration is infinite. This is why successful postselected output alone is not a precision claim.

For $a=1$, $b=3$, and $d=4$ in consistent units, $r=1/2$, the mean duration is 8, and the duration variance is 12. Each completed Ramsey experiment has local information 16. A deadline must count unfinished runs too; the finite-time result does so explicitly.

## What to distinguish when reading the proofs

**Physical time and effective time:** $T$ is the charged exposure; $d$ is the signed phase-accumulation time.

**Known and unknown direction:** target-only Fisher information does not include the nuisance penalty. The fixed-rate converse uses a joint change of frequency and angle.

**Local information and global accuracy:** a Ramsey fringe has phase ambiguity. The global theorem uses several effective times to resolve it; the optimal local coefficient is a separate result.

**Rate control and coherent access:** a device able to apply the unknown error coherently has a stronger resource than a device able only to change its random occurrence rate.

**Shared axis and generic unknown noise:** the error need not be calibrated, but it must retain the stated algebraic structure. Independent unknown axes across settings obey a linear-information converse.

## Specialist reading path

Continue with [the model](MODEL.md), then the nuisance-path converse in [theorems](THEOREMS.md), and finally the first-passage calculation in [stopped sensing](STOPPED_SENSING.md). The [physical scope](PHYSICAL_SCOPE.md) separates the ideal result, finite-interval local result, and implementation assumptions. [Reproducibility](REPRODUCIBILITY.md) maps each calculation to executable checks.
