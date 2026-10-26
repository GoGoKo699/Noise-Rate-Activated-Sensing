# Physical interpretation and controlled variations

[Model](model.md) · [Proofs](precision_bounds.md) · [Related work](../references/RELATED_WORK.md)

## A scalar control of one interaction

The common-axis assumption means one physical coupling whose incoherent strength can be changed, not two unrelated baths assigned equal unknown directions. An illustrative stochastic Hamiltonian is

```math
H(t)=\frac\omega2Z+[\xi_0(t)+u(t)\xi_1(t)]N_\phi.
```

If the independent white noises satisfy $`\mathbb E[\xi_0(t)\xi_0(t')]=a\delta(t-t')`$ and $`\mathbb E[\xi_1(t)\xi_1(t')]=\kappa\delta(t-t')`$, Stratonovich Hamiltonian noise averages to

```math
\dot\rho=-i\frac\omega2[Z,\rho]
+(a+u^2\kappa)(N_\phi\rho N_\phi-\rho).
```

This follows from $`-[N_\phi,[N_\phi,\rho]]/2=N_\phi\rho N_\phi-\rho`$. Switching $`u`$ between zero and one adds noise in the error sector while preserving a strictly positive background rate. The white-noise and instantaneous-feedback limits are part of the model, not properties of arbitrary reservoirs.

### Collision realization

Let each unobserved environmental qubit enter in $`|0\rangle`$ and interact through a fixed

```math
V_\phi=e^{-i\chi N_\phi\otimes X_E}.
```

Tracing it out yields

```math
\mathcal C_\phi(\rho)=\cos^2\chi\,\rho+
\sin^2\chi\,N_\phi\rho N_\phi.
```

Independent Poisson arrivals of intensity $`\lambda`$ give the generator

```math
\lambda(\mathcal C_\phi-\mathrm{id})(\rho)
=\lambda\sin^2\chi(N_\phi\rho N_\phi-\rho).
```

Controlling arrival intensity changes the rate without changing the axis or signal. Here $`\chi`$ and the environmental input are fixed; the controller is not given coherent access to individual collisions or environmental states. This is a microscopic consistency construction, not a laboratory demonstration.

### Experimental connection and its limits

Rower et al. injected fixed-axis transverse noise into a low-frequency fluxonium qubit and modeled anisotropic transverse noise using the same qubit jump-operator structure. Their setup and model support the relevance of fixed-coupling noise injection, but not the complete unknown-axis sensing protocol. The paper also discusses noise-induced frequency shifts. See [the primary article](https://doi.org/10.1103/PhysRevA.111.032420) and [its preprint](https://arxiv.org/html/2409.12303v1).

A physical comparison must account for changes in the signal response under the rate knob. Known setting-dependent Hamiltonian offsets can be removed using the measured residence times; independently unknown offsets add nuisance parameters. Known multiplicative signal changes are covered by the general $`(s_j,\gamma_j)`$ theorem.

Coherent access to the same unknown axis is a stronger resource: a calibrated pulse can implement $`e^{-i\pi N_\phi/2}=-iN_\phi`$ without knowing $`\phi`$. The present result establishes what incoherent rate selection alone suffices to do; it does not establish its superiority over that stronger hardware capability.

## Finite-interval ideal parity measurements

There is a distinct local result when parity is checked every fixed $`\Delta>0`$ rather than continuously. During each interval keep rate $`a`$ or $`b`$ according to the last measured sector. Hidden pairs of jumps are not resolved individually.

For rate $`\gamma`$ the odd-transition probability and signed residence-time expectation, starting with sign $`\sigma`$, are

```math
p_\gamma=\frac{1-e^{-2\gamma\Delta}}2,
\qquad
\mathbb E\left[\int_0^\Delta(-1)^{n(u)}du\right]
=\sigma\frac{p_\gamma}{\gamma}.
```

The measured parity chain has transition probabilities $`p_a,p_b`$ and stationary weights $`p_b/(p_a+p_b)`$ and $`p_a/(p_a+p_b)`$. Its mean signed signal rate is

```math
v_\Delta=\frac{p_ap_b}{\Delta(p_a+p_b)}
\left(\frac1a-\frac1b\right).
```

For $`b>a`$, it is positive at every finite $`\Delta`$ and approaches $`r`$ as $`\Delta\to0`$.

To obtain a local information statement, compensate a fixed nominal frequency $`\omega_0`$ and differentiate the residual frequency $`\epsilon=\omega-\omega_0`$ at zero. Finish in the even sector, allowing $`O(\log T)`$ checks for the final return and counting deadline failures. Each hidden trajectory then has an even total jump count, so its unknown direction cancels. Its logical channel is a mixture of rotations $`e^{-i\epsilon DZ_L/2}`$.

At $`\epsilon=0`$, a logical $`Y_L`$ readout has outcome probabilities $`1/2`$ and derivative magnitude $`\mathbb E[D\mid\text{success}]/2`$. The resulting efficient information is

```math
p_{\rm success}\bigl(\mathbb E[D\mid\text{success}]\bigr)^2
=v_\Delta^2T^2+o(T^2).
```

The parity chain is mixing; its additive reward has mean $`v_\Delta T+O(1)`$ and variance $`O(T)`$. A logarithmic finishing margin makes the return failure negligible. No knowledge of $`\phi`$ is used.

This is an attainable **local** coefficient at a compensated operating point, not a claim that $`v_\Delta^2`$ is the globally optimized coefficient over finite-cadence controls. Away from compensation, unobserved residence times cause dephasing. The exact stopped-channel and global-estimation proofs assume ideal continuous syndrome timing. Measurement errors, directional drift, and independently unknown setting-dependent axes are not represented by the finite-interval calculation.

## Bounded microscopic dynamics and the retained record

The [microscopic sensing calculation](microscopic_sensing.md) specifies a bounded two-rate collision device and derives its own local quadratic-information coefficient at finite cadence. The Hamiltonian retains the signal throughout every collision, and the unknown transverse axis is shared by both settings. All environmental qubits are initialized at time zero and retained after use.

The companion [controlled-record analysis](https://github.com/GoGoKo699/Markovian-Resolution-Limit/blob/main/science/sensing_bridge.md) supplies two different guarantees. The probability of an all-even parity record witnesses model disagreement when checks resolve bounded microscopic motion. Conversely, for measurements and rate choices at collision boundaries, a parameter-uniform error bound compares the complete finite sensing experiment with its Markovian prediction. That bound transfers bounded-loss risk for the same protocol and estimator; it does not transfer Fisher information.

The microscopic local coefficient is proved directly, rather than inferred from agreement of the channels at the compensated frequency. Neither this attainment result nor the record-discrimination witness proves that rate diversity improves the optimal microscopic risk: the strongest fixed-rate protocol on the same hardware must also be analyzed. Finite measurement duration, ancilla noise, and controller work remain outside these ideal-instrument calculations.

## The load-bearing boundaries

The exact cancellation requires successive errors to share an involutory operator anticommuting with the signal. The independent-axis converse in [the proofs](precision_bounds.md#independent-setting-dependent-directions) shows that this restriction changes the ultimate precision law, rather than being a cosmetic simplification.

The theorem concerns sensor exposure with ideal control and storage. It does not include a bound on control energy, bath-engineering expense, error in the classical timing record, or readout infidelity. These define a different physical resource model. Noise-assisted correction is established prior work; the attributed contribution here is the unknown-axis obstruction, its controlled-rate removal, and the matching precision coefficient.
