# Reproducibility

[Scientific synthesis](SCIENTIFIC_SYNTHESIS.md) · [Stopped calculations](../src/nras.py) · [Preset calculations](../src/preset.py) · [Risk calculations](../src/risk.py)

## Commands

Use Python 3.11 or later. From the repository root:

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
python scripts/check.py
python scripts/reproduce.py
python scripts/reproduce_evidence.py
```

Package installation needs the package index. The checks and examples run offline afterward, with no external dataset or credentials. Both example commands print JSON without modifying tracked files. Supplying `--output` explicitly writes a separate result:

```bash
python scripts/reproduce_evidence.py --output /tmp/nras-evidence.json
```

The [stopped-sensing example](../results/example.json) records parameters, seeds, sample counts, and dependency versions. Sampling output can depend on library versions. The [evidence table](../results/evidence.json) evaluates exact analytical expressions for the local protocols, global-risk bounds, and residual-dephasing certificate; it is not a table of simulated global errors or finite-time optima. Its generator is `scripts/reproduce_evidence.py`.

## Coverage

The scientific suite contains 80 tests: 33 in `tests/test_nras.py`, 20 in `tests/test_preset.py`, 20 in `tests/test_risk.py`, and 7 in `tests/test_learning.py`. The GitHub workflow executes `python scripts/check.py`, which also checks local links, anchors, and basic mathematics delimiters.

| Calculation | Check |
|---|---|
| Unknown-error algebra and recovery phase | Pauli identities and direct matrix products |
| Nuisance-path coefficients | Symbolic and numerical operators, including exactly trace-preserving short-step limits |
| Uncorrected trajectories | 500 random chronological products, including odd endpoints |
| Optimal selectable-setting coefficient | 500 random setting families compared with an independent linear program |
| Collision-induced channel | Explicit environment trace versus the analytical channel |
| First-passage distribution | Backward equations, symbolic moments, and 30,000 event samples |
| Hard-deadline accounting | 20,000 samples retaining every failed run at full deadline cost |
| Symmetric signed time and finite-cadence drift | Independent tilted and augmented generator calculations |
| Preset echo | 300 direct two-qubit trajectories with recovery and logical echo |
| Complete preset likelihoods | Finite differences including unknown-rate score blocks |
| Calibration and rate diversity | Crossover identities, probability sensitivity, fair-choice bound, and 300 maximizing-pair comparisons |
| Nuisance pooling | Common versus independent direction blocks |
| Global-risk ingredients | Compact prior normalization and information, integration by parts, ODE supersolution, and binomial inverse moments |
| Fixed-rate global estimator | Seeded paid no-jump trials at five frequencies, compared with the proven upper bound |
| Parallel-dephasing readout | Angular quadrature, mixed-state likelihood finite differences, and exact superoperator factorization |
| Parallel-noise converse and finite advantage | Gauge cancellation and exact tolerance-boundary calculation |
| Physical resource identities | Simultaneous transformation of signal and noise under a known pulse; unidentifiability with free setting offsets |
| Tutorial examples | Ramsey readout, parity encoding, nuisance projection, the worked rate mixture and echo, charged repetitions, a two-error path, and the generator-to-contrast convention |
| Evidence regeneration | Deterministic table regenerated and compared with numerical tolerances |

The likelihood checks use Poisson cutoffs with tail probability below $10^{-14}$ at their tested parameters. They finite-difference actual outcome probabilities rather than substituting analytical scores into an information formula. Seeded checks use stated tolerances instead of requiring identical floating-point results across all package versions.

The [worked tutorial](TUTORIAL.md) uses the same physical and statistical conventions. Its seven finite checks run as part of the suite; passing them validates those calculations, not a reader's understanding or the source PDF. The selected-source normalization note is in the [learning guide](LEARNING_GUIDE.md#rate-normalization-when-using-the-source).

## Reading the numerical examples

In the preset table, rate units set $a=1$, $b=3$. A balanced echo has local information $T^2/4$. A fixed timing imbalance uses fractions 0.76 and 0.24; its coefficient eventually falls as described by the exact calibration law. A fair recorded rate choice instead approaches coefficient $1/5$. The column labelled `optimal_leading_design_information` uses probability $3/4$: it optimizes the leading coefficient, not necessarily the finite-time information.

The residual-dephasing example has $\kappa/a=0.01$ and $aT=10$. The specified imperfect protocol has information approximately $12.16635/a^2$, exceeding the ideal fixed-rate upper bound $10/a^2$. The threshold $\log(400/231)/40$ belongs to this finite-time local comparison, not to a general hardware or fault-tolerance specification.

The global table uses $\Omega=[-1,1]$ and prior half-width $h=1/2$. Its lower and upper columns are analytical bounds, not equalities. The full minimax proof is in [global precision](GLOBAL_RISK.md); the optimal global constant is not inferred from the table.

## Interpretation and implementation boundaries

The stopped simulator samples exact alternating exponential waits. An unfinished run returns `completed=False` and physical time equal to the deadline. The event-count guard raises instead of discarding long trajectories. Equal-rate sampling requires a deadline because the untruncated first-passage mean is infinite.

All implementations retain the resource assumptions of their documents. Finite-cadence signed drift is a local compensated result, not a faulty-readout simulation or a global theorem. Residual dephasing describes one unobserved parallel channel with otherwise ideal operations. The global upper scaling follows from the stopped-channel and multiscale proofs, not from a preset Fisher matrix or the sampled no-jump baseline.

Tests establish their documented finite identities and implementation properties. They do not substitute for the universal proofs, independent scientific review, or a priority assessment. Source-level syntax checks also do not certify GitHub's hosted mathematical rendering; that requires a separate rendered-page inspection.
