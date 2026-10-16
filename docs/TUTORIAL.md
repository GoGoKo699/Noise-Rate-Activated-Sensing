# Understanding the sensing mechanism

[Overview](../README.md) · [Precise model](MODEL.md) · [Proofs](THEOREMS.md)

## The starting question

A qubit accumulates a phase proportional to an unknown frequency. Noise occasionally flips it about some axis in the transverse plane. The axis is stable, but its angle is unknown. Detecting that an error occurred does not automatically tell us which coherent recovery to apply.

Knowing the angle and learning it during the experiment are different resources. At a single fixed rate, the angle's uncertainty can imitate a change of signal frequency. The fixed-rate theorem bounds all allowed adaptive strategies, including those trying to learn and correct simultaneously. The [model](MODEL.md) defines the statistical task.

Access to two rates changes the conclusion. There are two distinct ways to use it: separate the signal and nuisance statistically, or cancel the nuisance from each completed sensing operation.

## Detect the sector without reading the phase

Store the logical amplitudes in $|00\rangle$ and $|11\rangle$, with the sensor first. A transverse sensor error moves them to the odd-parity sector. A parity measurement distinguishes even from odd without distinguishing the two logical amplitudes. It reveals an error without measuring the unknown phase.

The protocols assume ideal fast parity measurements and one noiseless ancilla. They do not receive a free measurement of the bath.

## Separate the two unknowns using rate diversity

First consider applying a fixed sensor $X$ after every detected error. This returns the state to the code but leaves an unknown logical phase because $XN_\phi=e^{i\phi Z}$. After a duration $T$ and $n$ errors, the phase is

$$
\Theta=\omega T-2\phi n.
$$

Keeping the count matters. At one rate, the typical count is close to $\gamma T$, so changing $\phi$ closely imitates changing $\omega$. This is the statistical obstruction behind the linear-information law.

Choose rate $a$ or $b$ before each interrogation and retain which was used. The target accumulates for the same duration, but the typical error counts differ. Combining the two labelled kinds of data helps separate the two unknowns. A suitable randomization probability attains the optimal leading local coefficient

$$
r^2=\left(\frac{b-a}{b+a}\right)^2.
$$

Even an equal-probability choice retains at least half of this coefficient without knowing the numerical rates. At $a=1$, $b=3$, its coefficient is $1/5$, compared with the optimum $1/4$.

This is not a statement that the output phase no longer contains $\phi$. It is a statement about the full local Fisher information after treating $\phi$ as a nuisance. Repetitions cost their full durations, and their direction must remain shared and stable. The preset rate choice also does not eliminate syndrome-triggered recovery pulses.

## A preset echo and its calibration requirement

Another construction uses a longer low-rate block and a shorter high-rate block, with a logical echo between them. Their durations satisfy $at_a=bt_b$. Expected error counts then cancel in the target–nuisance cross-information while the signal retains time $t_a-t_b=rT$.

This gives $r^2T^2$ local information exactly at finite $T$. However, a fixed mismatch between the expected counts eventually changes the scaling back to linear. It is a balancing requirement of this particular echo, not a universal limitation: the recorded random-rate construction above avoids it. [Preset protocols](PRESET_PROTOCOLS.md) gives the exact mismatch law and also treats the numerical rates as unknown.

## Let two errors cancel instead

There is a different construction that leaves the errors uncorrected. We know $N_\phi^2=I$ even without knowing $\phi$. Two occurrences of the same error therefore cancel.

The signal changes sign between them because $N_\phi ZN_\phi=-Z$. If the first waiting interval lasts $\tau_+$ and the second lasts $\tau_-$, the phase is $\omega(\tau_+-\tau_-)$ rather than $\omega(\tau_++\tau_-)$. Keep a signed clock, positive in the code and negative in the error sector. Use rate $a$ while it runs forward and rate $b>a$ while it runs backward. The backward intervals are shorter on average.

Choose a desired effective time $d$ and stop when the signed clock first reaches it. At that instant the sensor is in the code and the output is exactly the ordinary Ramsey operation of duration $d$, independently of $\phi$. No estimate of the angle or numerical rates enters the stopping rule.

The physical duration is random, with mean $d/r$. At equal rates it eventually succeeds but has infinite mean duration. This is why a perfect postselected output alone is not a precision claim. The stopped protocol's deadline analysis charges every failed or long run.

For $a=1$, $b=3$, and $d=4$ in consistent units, the mean duration is 8 and the duration variance is 12. Each completed Ramsey experiment has local information 16. Using multiple prescribed effective times also resolves phase ambiguity, giving the separate global-estimation theorem.

## What each guarantee means

**Statistical separation:** preset designs preserve local information despite a shared nuisance. The nuisance can remain in each output state.

**Exact channel cancellation:** stopped sensing produces a direction-independent Ramsey operation on every completed trajectory. Its physical duration and failures must be charged.

**Rate knowledge:** a balanced echo needs the ratio; a fair random choice does not. Stopped-output correctness is independent of the numerical rates, while throughput guarantees need rate bounds.

**Shared axis:** two independently unknown error directions define a different nuisance model and obey a linear-information converse. Rate diversity does not correct arbitrary uncharacterized noise.

**Local and global estimation:** a large Fisher matrix does not alone resolve Ramsey phase ambiguity. The global theorem is proved using the exact stopped channel, not inferred from a random-rate local coefficient.

## Specialist reading path

Continue with [the model](MODEL.md), the converse in [theorems](THEOREMS.md), and [preset protocols](PRESET_PROTOCOLS.md). Then read [stopped sensing](STOPPED_SENSING.md) for the first-passage and global-risk arguments. [Physical scope](PHYSICAL_SCOPE.md) and [related work](../literature/RELATED_WORK.md) specify the physical and attribution boundaries. [Reproducibility](REPRODUCIBILITY.md) maps calculations to executable checks.
