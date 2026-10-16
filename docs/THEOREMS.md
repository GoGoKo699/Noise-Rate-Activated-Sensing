# Precision bounds and their attainment

[Model](MODEL.md) · [Stopped protocol](STOPPED_SENSING.md) · [Attribution](../literature/RELATED_WORK.md)

All information statements use the nuisance-adjusted classical-information definition in the model. Results are for one sensor and the stated ideal controls, not for direct bath access.

## Theorem 1 — Fixed rate

For $H=\omega Z/2$, $L=\sqrt\gamma N_\phi$, and an arbitrary continuously unknown fixed $\phi$,

$$
\mathcal I_\omega^*(T)\le\min\{T^2,T/\gamma\},
\qquad
\lim_{T\to\infty}\frac{\mathcal I_\omega^*(T)}{T}=\frac1\gamma.
$$

The bound covers adaptive learning, interleaved correction, retained measurement records, and noiseless quantum memory. It does not apply to a promised finite set of directions or to an exactly known direction.

## Theorem 2 — Controlled rate

If the same unknown error operator is available at any classically selected rate in $[a,b]$, with $0<a<b<\infty$, then

$$
\lim_{T\to\infty}\frac{\mathcal I_\omega^*(T)}{T^2}=r^2,
\qquad r=\frac{b-a}{b+a}.
$$

The endpoints suffice. One noiseless ancilla, ideal syndrome measurements, and syndrome-conditioned selection of the rate attain the coefficient. No estimate of $\phi$ is needed.

## Theorem 3 — Selectable signal and noise strengths

For a finite set of settings $(s_j,\gamma_j)$ from the model, define

$$
v_* =\max_{i,j}
\frac{|s_i\gamma_j-s_j\gamma_i|}{\gamma_i+\gamma_j}.
$$

Then

$$
\lim_{T\to\infty}\frac{\mathcal I_\omega^*(T)}{T^2}=v_*^2.
$$

Quadratic information growth with positive coefficient is possible precisely when the ratios $s_j/\gamma_j$ are not all equal. At zero coefficient, the stronger bound is

$$
\mathcal I_\omega^*(T)\le T\max_j\frac{s_j^2}{\gamma_j}.
$$

Thus merely speeding up the signal and noise proportionally does not activate quadratic growth. The maximization includes $i=j$; a single setting has $v_*=0$.

## Proof of the converses

### The inherited channel bound

For a differentiable one-parameter Markovian model, use the zero-gauge specialization of the information-growth bound in Das, Górecki, and Demkowicz-Dobrzański, Eqs. (2), (4), and (5) of [the cited paper](https://arxiv.org/html/2404.03954v2):

$$
\frac{dF}{dt}\le4\left(\|A\|+\|B\|\sqrt F\right),
$$

$$
A=\dot L^\dagger\dot L,
\qquad
B=\dot H-\frac i2\left(\dot L^\dagger L-L^\dagger\dot L\right).
$$

A dot here is a parameter derivative, not a time derivative. For several Lindblad operators, sum the corresponding terms. A permissible gauge suffices for an upper bound; optimality of that gauge is not assumed.

Parameter-independent controls preserve this upper bound. For an adaptively selected setting, include the classical controller and record as orthogonal blocks. Taking the largest operator norms over settings gives a uniform bound, including all recorded outcomes. Ideal measurements and resets are parameter-independent channels and cannot create information along the comparison path.

### The common nuisance path

Along $\omega=\omega_0+u$, $\phi=\phi_0+cu$, direct Pauli multiplication gives

$$
(\partial_\phi N_\phi)N_\phi=-iZ,
\qquad
N_\phi(\partial_\phi N_\phi)=iZ,
$$

and therefore, in every setting,

$$
A_j=c^2\gamma_j I,
\qquad
B_j=\left(\frac{s_j}{2}-c\gamma_j\right)Z.
$$

For a single unit-strength setting, choose $c=1/(2\gamma)$. Then $B=0$, $A=I/(4\gamma)$, and $F_u(T)\le T/\gamma$. The [nuisance-path argument](MODEL.md#the-nuisance-path-argument) bounds efficient target information by this quantity. Choosing $c=0$ instead gives $F_u(T)\le T^2$.

For rates in $[a,b]$, choose $c=1/(a+b)$. Uniformly in the selected rate,

$$
\|A\|\le\frac b{(a+b)^2},
\qquad \|B\|\le\frac r2.
$$

Consequently $F'\le4b/(a+b)^2+2r\sqrt F$, which implies $\limsup F(T)/T^2\le r^2$.

For completeness, if $F'\le C+2v\sqrt F$ and $v>0$, the comparison solution, with $y=\sqrt F$, satisfies

$$
t=\frac yv-\frac{C}{2v^2}\log\left(1+\frac{2vy}{C}\right)
$$

when $C>0$. Hence $y=vt+O(\log t)$. If $C=0$, use $F\le v^2t^2$; if $v=0$, use $F\le Ct$. Initial parameter-independent preparation has $F(0)=0$.

### The minimax coefficient

For finitely many settings let

$$
v(c)=\max_j|s_j-2c\gamma_j|.
$$

The growth bound with $C=4c^2\max_j\gamma_j$ gives a leading coefficient at most $v(c)^2$. To minimize it, observe that $v(c)\le v$ is equivalent to a common intersection of intervals

$$
\frac{s_j-v}{2\gamma_j}\le c\le
\frac{s_j+v}{2\gamma_j}.
$$

Intervals on the real line have a common intersection exactly when every lower endpoint is no greater than every upper endpoint. Rearranging gives

$$
s_i\gamma_j-s_j\gamma_i\le v(\gamma_i+\gamma_j)
\quad\text{for all }i,j.
$$

Taking both orderings proves $\min_c v(c)=v_*$. If every ratio is the same $k$, choose $c=k/2$ to obtain the stated linear bound.

## Attainment by leaving the errors uncorrected

Encode a logical qubit as $|0_L\rangle=|00\rangle$, $|1_L\rangle=|11\rangle$, with the sensor first. Measure parity ideally, but do not apply a recovery after an error.

Let $n(t)$ count detected jumps. For any trajectory define the signal-weighted signed time

$$
D_s(t)=\int_0^t(-1)^{n(u)}s_{j(u)}\,du.
$$

Repeatedly moving $N_\phi$ through the signal rotations gives the exact sensor unitary

$$
U(t)=N_\phi^{n(t)}\exp[-i\omega D_s(t)Z/2].
$$

Because $L_j^\dagger L_j=\gamma_j I$, the jump likelihoods are state-, $\omega$-, and $\phi$-independent for this protocol. Normalized no-jump propagation contains only the signal rotation. At an even count the unknown operator disappears, giving an exact logical Ramsey output with known $D_s$.

Use setting $i$ in the even sector and $j$ in the odd sector. One complete pair has independent waiting times $W_i\sim\operatorname{Exp}(\gamma_i)$ and $W_j\sim\operatorname{Exp}(\gamma_j)$, with physical duration and reward

$$
C=W_i+W_j,
\qquad R=s_iW_i-s_jW_j.
$$

The long-time reward rate is

$$
v_{ij}=\frac{\mathbb E R}{\mathbb E C}
=\frac{s_i\gamma_j-s_j\gamma_i}{\gamma_i+\gamma_j}.
$$

The alternating two-state Markov chain is irreducible, with finite exponential holding-time moments. Its additive reward obeys $D_s(t)/t\to v_{ij}$ in mean square. This can also be seen from exponential decay of two-state correlations, which makes the reward variance $O(t)$.

For a hard deadline, run until $t_0=T-h(T)$, where $h(T)$ is a sufficiently large multiple of $\log T$ in fixed rate units. If parity is even, decode immediately. If it is odd, keep setting $j$ until the next jump or until $T$. The return failure probability is at most $e^{-\gamma_j h(T)}$. The added reward is bounded by $\max|s_j|h(T)$ on success, and successful $|D_s|\le\max|s_j|T$. Therefore failures and the finishing interval do not change the leading second moment:

$$
\mathbb E[\mathbf 1_{\mathrm{success}}D_s^2]/T^2\longrightarrow v_{ij}^2.
$$

Read out the resulting pure Ramsey state, keeping both its timing record and its success flag. Its efficient information is this success-weighted second moment. Choosing a maximizing pair proves Theorems 2 and 3. The [stopped protocol](STOPPED_SENSING.md) gives an alternative attainment with deterministic effective time.

### Tight linear coefficient at equal rates

For rate $\gamma$ in both sectors and $s=1$, start in the even sector and write $D(t)=\int_0^t(-1)^{n(u)}du$. The telegraph correlations give

$$
\mathbb E D(t)=\frac{1-e^{-2\gamma t}}{2\gamma},
\qquad
\mathbb E D(t)^2=\frac t\gamma-\frac{1-e^{-2\gamma t}}{2\gamma^2}.
$$

At time $t$, complete the next return only when parity is odd. If $J$ indicates odd parity and $W\sim\operatorname{Exp}(\gamma)$ is the independent additional wait, then $D_f=D(t)-JW$. Here

$$
\mathbb E[D(t)J]=0,
\qquad
\mathbb E D_f^2=\frac t\gamma+\frac{1-e^{-2\gamma t}}{2\gamma^2}.
$$

To impose $T$, take $t=T-h$, $h=4\log(1+\gamma T)/\gamma$, for sufficiently large $T$. Exponential-tail moments bound the discarded contribution by $o(T)$: for example $\mathbb E[(t+W)^2\mathbf1_{W>h}]=O((t+h+1/\gamma)^2e^{-\gamma h})$. The successful information is $T/\gamma-o(T)$, proving the remaining part of Theorem 1.

## Independent setting-dependent directions

If setting $j$ instead has its own independently unknown $\phi_j$, choose the nuisance path

$$
\phi_j(u)=\phi_{j0}+\frac{s_j}{2\gamma_j}u.
$$

Then every $B_j$ vanishes and $A_j=s_j^2I/(4\gamma_j)$. For the enlarged nuisance family,

$$
\mathcal I_\omega^*(T)\le T\max_j\frac{s_j^2}{\gamma_j}.
$$

This converse explains why a shared unknown interaction is essential. It does not treat known inter-setting angular offsets as independent unknown parameters.

## What the checks establish

The code verifies the Pauli identities, path cancellation, direct trajectory products, minimax formula against a separate linear program, and timing formulas. The proofs above establish universal and asymptotic statements; a finite numerical sample does not.
