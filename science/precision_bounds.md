# Precision bounds and their attainment

[Model](model.md) · [Preset protocols](preset_protocols.md) · [Stopped protocol](stopped_sensing.md) · [Attribution](../references/RELATED_WORK.md)

All information statements use the nuisance-adjusted classical-information definition in the model. Results are for one sensor and the stated ideal controls, not for direct bath access.

## Theorem 1 — Fixed rate

For $`H=\omega Z/2`$, $`L=\sqrt\gamma N_\phi`$, and an arbitrary continuously unknown fixed $`\phi`$,

```math
\mathcal I_\omega^*(T)\le\min\{T^2,T/\gamma\},
\qquad
\lim_{T\to\infty}\frac{\mathcal I_\omega^*(T)}{T}=\frac1\gamma.
```

The bound covers adaptive learning, interleaved correction, retained measurement records, and noiseless quantum memory. It does not apply to a promised finite set of directions or to an exactly known direction.

## Theorem 2 — Controlled rate

If the same unknown error operator is available at any classically selected rate in $`[a,b]`$, with $`0<a<b<\infty`$, then

```math
\lim_{T\to\infty}\frac{\mathcal I_\omega^*(T)}{T^2}=r^2,
\qquad r=\frac{b-a}{b+a}.
```

The endpoints suffice. Preset protocols with a fixed $`X`$ recovery after each detected error attain this leading local coefficient; syndrome-conditioned bath-rate selection is not necessary. A separate stopped protocol uses rate feedback but no error-recovery pulses and gives an exact direction-independent Ramsey channel on success. The different output and calibration guarantees are compared in [preset protocols](preset_protocols.md#relation-to-stopped-sensing).

## Theorem 3 — Selectable signal and noise strengths

For a finite set of settings $`(s_j,\gamma_j)`$ from the model, define

```math
v_* =\max_{i,j}
\frac{|s_i\gamma_j-s_j\gamma_i|}{\gamma_i+\gamma_j}.
```

Then

```math
\lim_{T\to\infty}\frac{\mathcal I_\omega^*(T)}{T^2}=v_*^2.
```

Quadratic information growth with positive coefficient is possible precisely when the ratios $`s_j/\gamma_j`$ are not all equal. At zero coefficient, the stronger bound is

```math
\mathcal I_\omega^*(T)\le T\max_j\frac{s_j^2}{\gamma_j}.
```

Thus merely speeding up the signal and noise proportionally does not activate quadratic growth. The maximization includes $`i=j`$; a single setting has $`v_*=0`$.

## Proof of the converses

### The inherited channel bound

For a differentiable one-parameter Markovian model, use the zero-gauge specialization of the information-growth bound in Das, Górecki, and Demkowicz-Dobrzański, Eqs. (2), (4), and (5) of [the cited paper](https://arxiv.org/html/2404.03954v2):

```math
\frac{dF}{dt}\le4\left(\|A\|+\|B\|\sqrt F\right),
```

```math
A=\dot L^\dagger\dot L,
\qquad
B=\dot H-\frac i2\left(\dot L^\dagger L-L^\dagger\dot L\right).
```

A dot here is a parameter derivative, not a time derivative. For several Lindblad operators, sum the corresponding terms. A permissible gauge suffices for an upper bound; optimality of that gauge is not assumed.

Parameter-independent controls preserve this upper bound. For an adaptively selected setting, include the classical controller and record as orthogonal blocks. The controlled Hamiltonian is block diagonal, and jump operators can be taken as the setting projectors tensored with the corresponding $`L_j`$. Thus $`A`$ and $`B`$ are block diagonal with blocks $`A_j,B_j`$. Taking the largest operator norms over settings gives a uniform bound, including all recorded outcomes. The policy is held fixed along the parameter path; parameter dependence of the outcomes does not give the policy an oracle. Ideal measurements, feedback operations, and resets are parameter-independent channels. This argument applies to time-discretized protocols and their ideal fast-control limit with fixed bounded rates.

### The common nuisance path

Along $`\omega=\omega_0+u`$, $`\phi=\phi_0+cu`$, direct Pauli multiplication gives

```math
(\partial_\phi N_\phi)N_\phi=-iZ,
\qquad
N_\phi(\partial_\phi N_\phi)=iZ,
```

and therefore, in every setting,

```math
A_j=c^2\gamma_j I,
\qquad
B_j=\left(\frac{s_j}{2}-c\gamma_j\right)Z.
```

For a single unit-strength setting, choose $`c=1/(2\gamma)`$. Then $`B=0`$, $`A=I/(4\gamma)`$, and $`F_u(T)\le T/\gamma`$. The [nuisance-path argument](model.md#the-nuisance-path-argument) bounds efficient target information by this quantity. Choosing $`c=0`$ instead gives $`F_u(T)\le T^2`$.

For rates in $`[a,b]`$, choose $`c=1/(a+b)`$. Uniformly in the selected rate,

```math
\|A\|\le\frac b{(a+b)^2},
\qquad \|B\|\le\frac r2.
```

Consequently $`F'\le4b/(a+b)^2+2r\sqrt F`$, which implies $`\limsup F(T)/T^2\le r^2`$.

For completeness, if $`F'\le C+2v\sqrt F`$ and $`v>0`$, the comparison solution, with $`y=\sqrt F`$, satisfies

```math
t=\frac yv-\frac{C}{2v^2}\log\left(1+\frac{2vy}{C}\right)
```

when $`C>0`$. Hence $`y=vt+O(\log t)`$. If $`C=0`$, use $`F\le v^2t^2`$; if $`v=0`$, use $`F\le Ct`$. Initial parameter-independent preparation has $`F(0)=0`$.

### The minimax coefficient

For finitely many settings let

```math
v(c)=\max_j|s_j-2c\gamma_j|.
```

The growth bound with $`C=4c^2\max_j\gamma_j`$ gives a leading coefficient at most $`v(c)^2`$. To minimize it, observe that $`v(c)\le v`$ is equivalent to a common intersection of intervals

```math
\frac{s_j-v}{2\gamma_j}\le c\le
\frac{s_j+v}{2\gamma_j}.
```

Intervals on the real line have a common intersection exactly when every lower endpoint is no greater than every upper endpoint. Rearranging gives

```math
s_i\gamma_j-s_j\gamma_i\le v(\gamma_i+\gamma_j)
\quad\text{for all }i,j.
```

Taking both orderings proves $`\min_c v(c)=v_*`$. If every ratio is the same $`k`$, choose $`c=k/2`$ to obtain the stated linear bound.

## Attainment with preset controls

For a single rate, fixed recovery $`X`$ and the retained count give

```math
\mathcal I_\omega(T)=\frac{T^2}{1+\gamma T}.
```

This particular protocol and formula are inherited from Tanggara et al., Eq. (A29), after converting their Hamiltonian normalization. Together with the converse, it proves the tight linear coefficient in Theorem 1. The protocol is reconstructed from its complete classical likelihood in [preset protocols](preset_protocols.md).

For settings $`i,j`$, select one at the beginning of an interrogation with probabilities

```math
p_i=\frac{\gamma_j}{\gamma_i+\gamma_j},
\qquad p_j=\frac{\gamma_i}{\gamma_i+\gamma_j},
```

retain the label, and use that setting for the entire duration $`T`$. Fixed recovery and a recorded equatorial readout have efficient information

```math
\frac{\mathcal I_\omega(T)}{T^2}
=\mathbb E[s^2]
-\frac{\mathbb E[s\gamma]^2}{\mathbb E[\gamma^2]+\mathbb E[\gamma]/T}
\longrightarrow
\left(\frac{s_i\gamma_j-s_j\gamma_i}{\gamma_i+\gamma_j}\right)^2.
```

The expectations are over the retained setting label. The formula follows by averaging the full Fisher matrix before eliminating the common nuisance. Its derivation, unknown-rate extension, and local-versus-global boundary are in [preset protocols](preset_protocols.md#general-selectable-settings). Choosing a maximizing pair proves Theorems 2 and 3. In the rate-only case, the balanced two-block echo additionally gives $`r^2T^2`$ exactly at finite $`T`$.

## Attainment by leaving the errors uncorrected

The stopped construction has a stronger channel guarantee than the preset local-information protocols. Encode a logical qubit as $`|0_L\rangle=|00\rangle`$, $`|1_L\rangle=|11\rangle`$, with the sensor first. Measure parity ideally, but do not apply a recovery after an error.

Let $`n(t)`$ count detected jumps. For any trajectory define the signal-weighted signed time

```math
D_s(t)=\int_0^t(-1)^{n(u)}s_{j(u)}\,du.
```

Repeatedly moving $`N_\phi`$ through the signal rotations gives the exact sensor unitary

```math
U(t)=N_\phi^{n(t)}\exp[-i\omega D_s(t)Z/2].
```

Because $`L_j^\dagger L_j=\gamma_j I`$, the jump likelihoods are state-, $`\omega`$-, and $`\phi`$-independent for this protocol. Normalized no-jump propagation contains only the signal rotation. At an even count the unknown operator disappears, giving an exact logical Ramsey output with known $`D_s`$.

For unit signal strength, using $`a`$ in the even sector and $`b`$ in the odd sector gives a signed-time drift $`r`$. Stopping at a prescribed signed time implements an exact Ramsey channel. Its duration law, hard-deadline attainment of $`r^2`$, and global-estimation guarantee are proved in [stopped sensing](stopped_sensing.md). The unknown angle cancels on every completed trajectory, unlike in the preset protocols.

## Independent setting-dependent directions

If setting $`j`$ instead has its own independently unknown $`\phi_j`$, choose the nuisance path

```math
\phi_j(u)=\phi_{j0}+\frac{s_j}{2\gamma_j}u.
```

Then every $`B_j`$ vanishes and $`A_j=s_j^2I/(4\gamma_j)`$. For the enlarged nuisance family,

```math
\mathcal I_\omega^*(T)\le T\max_j\frac{s_j^2}{\gamma_j}.
```

This converse explains why a shared unknown interaction is essential. It does not treat known inter-setting angular offsets as independent unknown parameters.

## What the checks establish

The code verifies the Pauli identities, nuisance-path cancellation, continuous coefficients from exactly trace-preserving short steps, direct trajectory products, complete classical likelihoods, minimax formula against a separate linear program, and timing formulas. These are checks of specified finite identities. The proofs above establish universal and asymptotic statements; a finite numerical sample does not.
