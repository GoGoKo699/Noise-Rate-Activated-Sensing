# Global precision at fixed microscopic strength

[Collision instrument](microscopic_sensing.md) · [Local precision](microscopic_precision.md) · [Paid calibration](microscopic_identifiability.md) · [Recorded-phase estimation](recorded_phase_estimation.md)

For the finite-strength collision device, one fixed positive coupling has optimal worst-case squared frequency error of order inverse time, while a menu of two fixed positive couplings attains inverse time squared. The comparison holds on one fixed, nonshrinking frequency interval, uniformly over the shared unknown transverse direction. It keeps the collision clock and physical compensation fixed. An exact retained-record construction and a global nuisance-curve converse establish the two directions separately.

## Statistical task and resources

Fix $`0<g_a<g_b`$, $`h>0`$ and a nominal frequency $`\omega_0`$, with $`g_bh<\pi/4`$. In cell $`j`$, the exposed sensor and its assigned bath qubit evolve under

```math
H_j(\epsilon,\phi)
=\frac\epsilon2 Z_S\otimes I_E+g_jN_\phi\otimes X_E,
\qquad \epsilon=\omega-\omega_0.
```

The unknown angle $`\phi`$ is shared by every cell, setting and repeated trial. All bath qubits are prepared at time zero, used once and retained afterward; none is accessible. Protected ancillas, parameter-independent instruments and classical feedback are allowed at cell boundaries. Initial preparation and readout at the hard deadline $`T=nh`$ are free; there are at most $`n-1`$ nonterminal boundary contacts. Consecutive operations at one boundary form one instrument. Repetitions, resets, calibration and unsuccessful records consume their own cells and contacts.

There is no contact inside a cell, change of its duration, reset of the collision clock, noise-free signal-bearing waiting time or adaptive retuning of the compensation. A readout basis may depend on earlier data; the Hamiltonian still contains the same residual frequency. All controller functions are held fixed when differentiating unknown parameters.

In the fixed-coupling class, every exposed cell in every pooled trial uses the same specified $`g\in\{g_a,g_b\}`$. The two-coupling class may choose either member before each cell through a classical recorded control. A recorded random choice between the two couplings is already two-coupling access. Allowing the fixed-device benchmark to choose the better of the two deterministic devices does not change its scaling.

For a fixed interval $`\Omega=[\omega_0-E,\omega_0+E]`$, define

```math
R_g^*(n;\Omega)
=\inf_{\mathcal P,\widehat\omega}
\sup_{\omega\in\Omega,\phi}
\mathbb E_{\omega,\phi}^{\mathcal P}
[(\widehat\omega-\omega)^2],
```

and define $`R_{\{g_a,g_b\}}^*(n;\Omega)`$ with the two-coupling class. The infima include biased estimators and all retained outcomes. The estimator can be clipped to $`\Omega`$. The controller class includes finite adaptive instruments, their parameter-independent mixtures and the controlled operational limits described below.

## One fixed band for both designs

Write $`\chi_j=g_jh`$ and choose a fixed $`r_*`$ with $`\chi_b<r_*<\pi/4`$. First restrict

```math
0\lt E\le\frac2h\sqrt{r_*^2-\chi_b^2}.
```

Then $`R_j(\epsilon)h\le r_*`$ for both settings, where $`R_j(\epsilon)=\sqrt{g_j^2+\epsilon^2/4}`$. The full interaction norm is at most $`r_*/h`$ throughout the interval; a hardware strength budget must cover this value. Define the exact cell functions

```math
p_j(\epsilon)=\frac{g_j^2}{R_j(\epsilon)^2}
\sin^2(R_j(\epsilon)h),
\qquad q_j=1-p_j,
```

```math
\theta_j(\epsilon)
=2\arctan\!\left[
\frac{\epsilon}{2R_j(\epsilon)}
\tan(R_j(\epsilon)h)
\right],
\qquad
d_j=\theta_j'(0)=\frac{\tan\chi_j}{g_j}.
```

This phase branch is smooth on the entire interval. The no-flip operator is $`\sqrt{q_j}\exp[-i\theta_jZ_S/2]`$, while a flip is $`N_\phi`$ up to a scalar. Set

```math
\mu_0=
\frac{p_b(0)q_a(0)d_a-p_a(0)q_b(0)d_b}
{p_a(0)+p_b(0)}>0.
```

Its strict positivity is the [microscopic drift calculation](microscopic_sensing.md#positive-drift-at-every-fixed-cadence): $`q_j(0)d_j/p_j(0)=h\cot\chi_j/\chi_j`$ strictly decreases with $`\chi_j`$. For the frozen derivative reward, define

```math
\mu^0(\epsilon)
=\frac{p_b(\epsilon)q_a(\epsilon)d_a
-p_a(\epsilon)q_b(\epsilon)d_b}
{p_a(\epsilon)+p_b(\epsilon)}.
```

Choose $`E>0`$ small enough that, throughout $`[-E,E]`$,

```math
0\lt p_a(\epsilon)\lt p_b(\epsilon)\lt \frac12,
\qquad
\mu^0(\epsilon)\ge\frac34\mu_0,
\qquad
\max_{j\in\{a,b\}}|\theta_j'(\epsilon)-d_j|
\le\frac14\mu_0.
```

These are explicit conditions on known smooth one-variable functions. They hold on some positive-width interval by their strict values at zero and continuity. Fix that interval once, independently of $`n`$. This gives a sufficient band rather than maximal bandwidth or constants uniform as the two couplings approach one another. The [single-cell calibration theorem](microscopic_identifiability.md) applies on this same band with

```math
\kappa=h\cos(2r_*)>0.
```

## Global precision theorem

On any fixed band satisfying the preceding conditions,

```math
\boxed{
R_g^*(n;\Omega)=\Theta(n^{-1})
\quad(g=g_a\text{ or }g_b),
\qquad
R_{\{g_a,g_b\}}^*(n;\Omega)=\Theta(n^{-2}).
}
```

Since $`h`$ is fixed, these are equivalently inverse-time and inverse-time-squared scalings at $`T=nh`$. All constants may depend on the fixed hardware and interval. The theorem does not identify optimal global constants or equate them with the local Fisher-information coefficient.

For the fixed-coupling side, let

```math
p_{\min,g}=(gh)^2\left(\frac{\sin r_*}{r_*}\right)^2.
```

The following finite bounds hold for every $`n\ge1`$:

```math
\frac1{nh^2/p_{\min,g}+\pi^2/E^2}
\le R_g^*(n;\Omega)
\le\frac1{n\kappa^2}.
```

For the two-coupling class,

```math
\frac1{(nh)^2+\pi^2/E^2}
\le R_{\{g_a,g_b\}}^*(n;\Omega)
\le\frac C{n^2}
```

for a finite constant $`C`$ depending only on the fixed design. Increasing $`C`$ covers the finitely many budgets below the multiscale construction's starting size, using the interval midpoint as a fallback.

## The fixed-coupling nuisance curve

Fix one coupling $`g`$. Suppress its label and write the exact Kraus operators as

```math
K_0=aI-ibZ_S,
\qquad K_1=-icN_\phi,
```

```math
a=\cos(Rh),
\qquad b=\frac\epsilon{2R}\sin(Rh),
\qquad c=\frac gR\sin(Rh),
\qquad a^2+b^2+c^2=1.
```

Primes on these real functions denote residual-frequency derivatives. Put $`p=c^2`$, $`q=a^2+b^2`$ and $`s=ab'-ba'`$. Since $`p\ge p_{\min,g}>0`$, the curve

```math
\phi(\epsilon)=\phi_0+
\int_0^\epsilon\frac{s(u)}{p(u)}\,du
```

is smooth throughout a neighborhood of the band. Its angle is understood modulo $`\pi`$. This is a comparison subfamily for the worst-case risk, not a relationship imposed on the physical unknowns or information provided to the controller. Its target-frequency derivative is one.

Along this curve, using $`N_\phi\partial_\phi N_\phi=iZ_S`$ and $`\phi'=s/p`$ gives

```math
\sum_{r=0}^1K_r^\dagger\dot K_r
=i(-s+p\phi')Z_S=0,
```

```math
\sum_{r=0}^1\dot K_r^\dagger\dot K_r
=A(\epsilon)I,
\qquad
A=a'^2+b'^2+c'^2+\frac{s^2}{p}.
```

A dot includes both the frequency derivative and the derivative of the nuisance curve. Equivalently, $`s=q\theta'/2`$ and

```math
4A=\frac{p'^2}{pq}+\frac{q\theta'^2}{p}.
```

The coefficient is bounded uniformly. At fixed $`\phi`$, Duhamel's formula and $`\|\partial_\epsilon H\|=1/2`$ give $`\|\partial_\epsilon U\|\le h/2`$. Hence $`A_0=a'^2+b'^2+c'^2\le h^2/4`$. Cauchy–Schwarz gives $`s^2\le q(a'^2+b'^2)\le qA_0`$, so

```math
4A\le\frac{h^2}{p}
\le\frac{h^2}{p_{\min,g}}.
```

Dilate one cell to $`V=\sum_rK_r\otimes|r\rangle`$ and purify every boundary instrument and retained record. The relation $`V^\dagger\dot V=0`$ removes the cross term in the squared norm of the accumulated derivative. A parameter-independent boundary dilation adds no derivative. Induction over the cells therefore gives, for every allowed adaptive strategy and every point on the curve,

```math
J_\epsilon\le F_\epsilon^{\mathrm{out}}
\le4nA(\epsilon)
\le\frac{nh^2}{p_{\min,g}}.
```

The argument includes adaptive learning of the direction, arbitrary protected memory, resetting and retaining failures. Early completion can be stored until the charged deadline. A different curve is used for each fixed device; the proof does not incorrectly require a common cancelling curve for two available couplings.

## From uniform information bounds to risk bounds

Use the normalized cosine prior on the frequency coordinate,

```math
\pi_E(u)=\frac1E\cos^2\!\left(\frac{\pi u}{2E}\right),
\qquad -E\lt u\lt E,
\qquad I(\pi_E)=\frac{\pi^2}{E^2}.
```

Along the nuisance curve, the [van Trees argument](global_precision.md#a-bound-valid-for-biased-estimators) gives

```math
\sup_{\omega\in\Omega,\phi}
\mathbb E[(\widehat\omega-\omega)^2]
\ge\frac1{\mathbb E_{\pi_E}J_u+I(\pi_E)}.
```

This is valid for biased estimators. Substitution proves the stated fixed-coupling lower bound. The matching upper bound is the exact [paid single-cell calibration estimator](microscopic_identifiability.md#repetition-risk-and-confidence), which uses $`n`$ cells and $`n-1`$ boundary instruments. Thus the fixed-coupling global scaling is established without a local unbiasedness assumption.

For the two-coupling lower bound, instead keep $`\phi`$ fixed along the prior. Every selected Hamiltonian has frequency derivative $`Z_S/2`$, so the norm of the complete purified signal generator is at most $`nh/2`$. Classical coupling selection and boundary instruments do not change this bound. Therefore $`J_u\le(nh)^2`$ uniformly, and van Trees proves the displayed inverse-square lower bound. These are different comparison paths for the two lower bounds.

### Global risk under controlled limits

The global lower bounds pass directly to the stipulated operational limits through bounded loss. Fix the hardware, resource budgets, one comparison path and its prior $`\pi`$. Suppose the finite-controller laws $`P_{r,u}`$ converge to $`P_u`$ on a common measurable output space, for every event and every point $`u`$ on the prior support. This is part of the convergence required by the stated controller class. Let $`b_\pi`$ be a lower bound on Bayes risk valid for every finite controller and every estimator, such as $`[C_n+I(\pi)]^{-1}`$ when the uniform information bound is $`J_u\le C_n`$.

For any measurable estimator $`f`$ of the limiting output, first clip its values to $`\Omega`$. Quantize the clipped values to finitely many representatives in $`\Omega`$, obtaining $`f_\eta`$ with $`|f_\eta-f|\le\eta`$. The inverse images of those representatives form a fixed finite partition of the common output space, independent of $`u`$ and $`r`$. Event-probability convergence therefore gives pointwise convergence of the corresponding risks. They are bounded by $`4E^2`$, so dominated convergence under the same fixed prior yields

```math
\int\mathbb E_{P_u}[(f_\eta-\omega(u))^2]\,\pi(u)\,du
=\lim_{r\to\infty}
\int\mathbb E_{P_{r,u}}[(f_\eta-\omega(u))^2]\,\pi(u)\,du
\ge b_\pi.
```

Both estimators take values in an interval of width $`2E`$. Consequently

```math
\bigl|(f_\eta-\omega)^2-(f-\omega)^2\bigr|
\le4E\eta
\qquad(\omega\in\Omega).
```

Sending $`\eta\to0`$ proves the same Bayes lower bound for $`f`$, and hence the same minimax lower bound. This argument includes biased estimators and requires no continuity of Fisher information. It does not enlarge the stipulated controller class. A finite partition of a final output is classical postprocessing and consumes no additional system contact.

Separately, the information bounds themselves have the [derivative-controlled extension](https://github.com/GoGoKo699/Markovian-Resolution-Limit/blob/main/science/intervention_bounds.md#limits-with-controlled-parameter-derivatives) used for local precision. On a slightly larger compact frequency interval, the nuisance curve has bounded first and second derivatives. Along it, $`H'=Z_S/2+g\phi'\partial_\phi N_\phi\otimes X_E`$ and $`H''=g(\phi''\partial_\phi N_\phi-\phi'^2N_\phi)\otimes X_E`$ have uniformly bounded norms. That argument retains information bounds under the required event-probability convergence on an open neighborhood; agreement at a single parameter value is insufficient. The bounded-loss argument above makes the global risk conclusion independent of that additional information-limit step.

## Attainment with retained even-parity records

Start a block in the even code, choose $`g_a`$ after an even parity result and $`g_b`$ after an odd one, and apply no error recovery. The [exact record identity](microscopic_sensing.md#cancellation-and-the-accumulated-local-phase) gives, on every even-ending record $`\mathcal R`$,

```math
U_{\mathcal R}(\epsilon)
=\exp[-i\Phi_{\mathcal R}(\epsilon)Z_L/2],
\qquad
\Phi_{\mathcal R}(\epsilon)
=\sum_{k=1}^L\sigma_{k-1}
\mathbf1_{\{\sigma_k=\sigma_{k-1}\}}
\theta_{j(\sigma_{k-1})}(\epsilon).
```

Every unknown-axis factor cancels exactly, including away from compensation. The controller retains the whole record, whose probability generally depends on $`\epsilon`$. That probability dependence must not be replaced by its value at zero.

Let $`D_\mathcal R^0=\Phi_\mathcal R'(0)`$. Accept a block for phase readout only when it ends even and $`D_\mathcal R^0\ge\mu_0L/2`$; retain every other result as a flagged outcome at the same charged block duration. This gate depends on the observed record and known hardware, not on the unknown parameters.

The [two-state parity-gate proof](recorded_phase_estimation.md#a-two-state-parity-gate) applies with the band conditions above. In detail, put $`M=\max(d_a,d_b)`$ and $`\rho=1-\inf_{|\epsilon|\le E}(p_a+p_b)<1`$. The frozen reward has expectation at least $`\mu^0(\epsilon)L`$ and variance at most $`VL`$, where $`V=M^2[1+2/(1-\rho)]`$. The probability of an even endpoint is at least one half. For every integer $`L\ge L_0`$, with $`L_0\ge64V/\mu_0^2`$, the gate succeeds with probability at least one quarter, uniformly on the band.

Every accepted record also has a uniformly monotone known phase curve:

```math
\frac{\mu_0}{4}L
\le\Phi_\mathcal R'(\epsilon)
\le\beta L,
\qquad
\beta=\max_{j,|\epsilon|\le E}|\theta_j'(\epsilon)|\lt \infty.
```

The lower bound follows by comparing every derivative with its value at zero, using the deterministic per-cell error bound $`\mu_0/4`$. Thus acceptance certifies a whole phase curve on the interval, not merely a large derivative at one point.

The [recorded-phase estimation lemma](recorded_phase_estimation.md#recorded-phase-estimation-lemma) now supplies the global estimator. It pays for initial localization, uses geometrically increasing block lengths, and adjusts only the terminal readout angle to the phase predicted at the preceding interval center. Conditional on the actual retained records, it inverts a known monotone average readout curve. Its concentration argument therefore remains valid although the record distribution depends on frequency. Nested confidence intervals and a weighted first-failure bound give squared error $`O(4^{-K})`$ with deterministic charged cell count $`\Theta(2^K)`$. Choosing the largest schedule that fits the budget $`n`$ gives $`O(n^{-2})`$ risk.

Each boundary combines parity extraction, any completed block's terminal measurement and the next preparation into one instrument. A fixed $`n`$-cell allocation uses at most $`n-1`$ nonterminal contacts; an estimate completed early is stored until $`nh`$, with that early readout counted. No branch receives extra exposure or an uncharged repetition. The Hamiltonian compensation is unchanged throughout.

## Scope of the separation

This closes the global fixed-coupling versus two-coupling comparison for boundary-only access on the stated band. It is an exact microscopic result rather than a transfer of the Markovian global theorem through endpoint agreement or total variation. The previously proved local coefficients remain local optimality statements; the constants in the global risk theorem are not asserted to be optimal.

The bandwidth and temporal access assumptions are substantive. The companion [clock-alias obstruction](https://github.com/GoGoKo699/Markovian-Resolution-Limit/blob/main/science/sensing_bridge.md#frequency-aliases-of-the-collision-clock) prevents uniform consistency on domains containing certain resonant frequency pairs. The companion [global contact comparison](https://github.com/GoGoKo699/Markovian-Resolution-Limit/blob/main/science/global_contact_precision.md) studies what becomes attainable when the same hardware permits contacts inside collisions. It uses a different resource class and does not weaken the boundary-only converse proved here.
