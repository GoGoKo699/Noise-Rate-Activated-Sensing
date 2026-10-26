# Reproducibility

[Scientific synthesis](../science/interpretation.md) · [Stopped calculations](../src/nras.py) · [Preset calculations](../src/preset.py) · [Risk calculations](../src/risk.py)

## Commands

Use Python 3.11 or later. From the repository root:

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
python scripts/check.py
python scripts/check_reproducibility.py
python scripts/reproduce.py
python scripts/reproduce_evidence.py
```

Package installation needs the package index. The scientific checks and examples run offline afterward, with no external dataset or credentials. Both example commands print JSON without modifying tracked files. Supplying `--output` explicitly writes a separate result:

```bash
python scripts/reproduce_evidence.py --output /tmp/nras-evidence.json
```

The [stopped-sensing example](../results/example.json) records parameters, seeds, sample counts, and dependency versions. Sampling output can depend on library versions. The [evidence table](../results/evidence.json) evaluates exact analytical expressions for the local protocols, global-risk bounds, and residual-dephasing certificate; it is not a table of simulated global errors or finite-time optima. Its generator is `scripts/reproduce_evidence.py`.

The [regeneration check](../scripts/check_reproducibility.py) runs both producers and compares the complete result structures and numbers, with relative tolerance `1e-10` and absolute tolerance `1e-14`. Runtime-version metadata is allowed to report the actual installed versions rather than reproduce an earlier environment label. The [verification workflow](../.github/workflows/check.yml) runs the suite and regeneration on Python 3.11 and 3.13, then checks that no tracked files were modified.

## Coverage

The suite contains 99 tests: 36 in `tests/test_nras.py`, 20 in `tests/test_preset.py`, 20 in `tests/test_risk.py`, 7 in `tests/test_learning.py`, 8 offline serialization/regeneration checks in `tests/test_rendering.py`, and 8 shared-structure checks in `tests/test_structure.py`. The GitHub workflow executes `python scripts/check.py`, which also checks local links, anchors, and basic mathematics delimiters.

| Calculation | Check |
|---|---|
| Unknown-error algebra and recovery phase | Pauli identities and direct matrix products |
| Nuisance-path coefficients | Symbolic and numerical operators, including exactly trace-preserving short-step limits |
| Uncorrected trajectories | 500 random chronological products, including odd endpoints |
| Optimal selectable-setting coefficient | 500 random setting families compared with an independent linear program |
| Collision-induced channel | Explicit environment trace versus the analytical channel |
| First-passage distribution | Backward equations, symbolic moments, and 30,000 event samples |
| Timing at numerical limits | High-precision comparisons for nearly equal rates and short exposures; large positive Laplace parameters |
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
| Evidence regeneration | Both recorded examples regenerated and compared with numerical tolerances |
| Shared learning structure | Exactly 30 ordered milestones, 13/17 allocation, fields, earlier dependencies, source links, and final integration |
| Reader routes and boundaries | Canonical topic paths, retained anchor, absence of personal coaching procedures, and complete hosted-page selection |

The likelihood checks use Poisson cutoffs with tail probability below $`10^{-14}`$ at their tested parameters. They finite-difference actual outcome probabilities rather than substituting analytical scores into an information formula. Seeded checks use stated tolerances instead of requiring identical floating-point results across all package versions.

The [worked tutorial](../learning/TUTORIAL.md) uses the same physical and statistical conventions. Its seven finite checks run as part of the suite; passing them validates those calculations, not a reader's understanding or the source PDF. The selected-source normalization note is in the [learning guide](../learning/HAASE_BRIDGE.md#rate-normalization-when-using-the-source).

The shared-structure checks validate the milestone count, declared dependencies, required fields, navigation, and separation from personal coaching records. They do not establish teaching effectiveness, comprehension, or scientific truth. The scientific implementations and their existing example tests use the same executable paths as before.

## Shared microscopic verification

The [bounded-collision sensing proof](../science/microscopic_sensing.md) has a
shared finite check in the companion repository:
[verify_sensing_bridge.py](https://github.com/GoGoKo699/Markovian-Resolution-Limit/blob/main/verification/verify_sensing_bridge.py).
That script compares the direct joint unitary with the analytic Kraus
instrument, propagates complete adaptive parity records, and compares the
local terminal-readout derivative with an independent classical reward
recursion. It also checks the companion complete-record error and survival
bounds. Run `python verification/run_all.py` from the
Markovian-Resolution-Limit checkout to execute it and compare its recorded
quantities. It is separate from this repository's 99-test suite.

The shared checks support the specified microscopic local result. They do
not establish a global-risk separation or a converse against arbitrary
fixed-rate microscopic control.

## Reading the numerical examples

In the preset table, rate units set $`a=1`$, $`b=3`$. A balanced echo has local information $`T^2/4`$. A fixed timing imbalance uses fractions 0.76 and 0.24; its coefficient eventually falls as described by the exact calibration law. A fair recorded rate choice instead approaches coefficient $`1/5`$. The column labelled `optimal_leading_design_information` uses probability $`3/4`$: it optimizes the leading coefficient, not necessarily the finite-time information.

The residual-dephasing example has $`\kappa/a=0.01`$ and $`aT=10`$. The specified imperfect protocol has information approximately $`12.16635/a^2`$, exceeding the ideal fixed-rate upper bound $`10/a^2`$. The threshold $`\log(400/231)/40`$ belongs to this finite-time local comparison, not to a general hardware or fault-tolerance specification.

The global table uses $`\Omega=[-1,1]`$ and prior half-width $`h=1/2`$. Its lower and upper columns are analytical bounds, not equalities. The full minimax proof is in [global precision](../science/global_precision.md); the optimal global constant is not inferred from the table.

## Hosted mathematical rendering

The separate [hosted-rendering workflow](../.github/workflows/render.yml) opens the actual public GitHub pages in Chromium at the inspected commit. It compares formula counts with the source, checks that the mathematics has rendered, reports parser errors, checks matrix row counts and unparsed delimiters, and captures full-page screenshots of the README, all Markdown pages in `science/`, `learning/`, `references/`, and `verification/`. It runs on same-repository documentation pull requests or by manual dispatch. It neither uses a substitute local Markdown renderer nor publishes a release.

For the same check from a complete checkout, with network access:

```bash
python -m pip install 'playwright>=1.49,<2'
python -m playwright install chromium
python scripts/check_rendering.py --ref "$(git rev-parse HEAD)" --output /tmp/nras-rendering
```

The CI browser installs Latin Modern Math and STIX fonts for native MathML. On Debian/Ubuntu, the equivalent setup is `sudo apt-get install fonts-lmodern fonts-stix`; other systems can use the [MathML font guidance](https://developer.mozilla.org/en-US/docs/Web/MathML/Guides/Fonts). No stylesheet or formula replacement is injected into GitHub. These fonts and browser packages are optional for the scientific checks; they support the separate visual audit. The output directory contains the report, hosted HTML, screenshots, and (in CI) an archive of the exact inspected sources; CI retains its artifact for 14 days. Network failure, missing formulas, or uninitialized mathematics is not a successful rendering check. Screenshots still require visual inspection for clipping, bra–ket notation, table layout, and unintended emphasis: automated DOM checks do not establish visual quality or scientific correctness.

## Interpretation and implementation boundaries

The stopped simulator samples exact alternating exponential waits. An unfinished run returns `completed=False` and physical time equal to the deadline. The event-count guard raises instead of discarding long trajectories. Equal-rate sampling requires a deadline because the untruncated first-passage mean is infinite.

All implementations retain the resource assumptions of their documents. Finite-cadence signed drift is a local compensated result, not a faulty-readout simulation or a global theorem. Residual dephasing describes one unobserved parallel channel with otherwise ideal operations. The global upper scaling follows from the stopped-channel and multiscale proofs, not from a preset Fisher matrix or the sampled no-jump baseline.

Tests establish their documented finite identities and implementation properties. They do not substitute for the universal proofs, independent scientific review, or a priority assessment. The source check rejects bare dollar math and the unsupported named-operator macro found by the hosted audit. Use GitHub math fences for displayed formulas and protected dollar/backtick spans for inline formulas; the browser additionally verifies formula counts and matrix row structure. Source-level syntax checks alone do not certify GitHub's hosted mathematical rendering; use the separate browser check and screenshot inspection above.
