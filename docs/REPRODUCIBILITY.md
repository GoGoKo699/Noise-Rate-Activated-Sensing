# Reproducibility

[Overview](../README.md) · [Proofs](THEOREMS.md) · [Stopped calculations](../src/nras.py) · [Preset calculations](../src/preset.py)

## Commands

Use Python 3.11 or later. From the repository root:

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
python scripts/check.py
python scripts/reproduce.py
```

Installation needs the package index. The checks and example run offline afterward, with no external dataset or credentials. The example prints JSON and does not change files unless an explicit `--output` path is supplied. To write a separate local result:

```bash
python scripts/reproduce.py --output /tmp/nras-example.json
```

The [recorded stopped-sensing example](../results/example.json) includes parameters, seeds, sample counts, and dependency versions. Sampling output can depend on library versions; analytical quantities are the comparison targets. Tests use fixed seeds and stated numerical tolerances rather than requiring identical floating-point output across platforms.

## Coverage

| Calculation | Check |
|---|---|
| Unknown-error algebra and recovery phase | Pauli identities and direct matrix multiplication |
| Nuisance-path cancellation | Numerical operator tests, symbolic identities, and a convergent family of exactly trace-preserving short steps |
| Exact uncorrected trajectory phase | 500 random chronological products, including odd endpoints |
| Optimal selectable-setting coefficient | 500 random families compared with a separate linear program |
| Collision-induced channel | Explicit environment trace versus the analytic channel |
| First-passage law | Backward equations, symbolic moments, and 30,000 event samples |
| Deadline resource accounting | 20,000 samples, retaining failures at their full deadline cost |
| Symmetric signed time and finite-interval drift | Independent tilted and augmented generator calculations |
| Preset echo phase | 300 direct two-qubit trajectory products with recovery and logical echo |
| Preset classical Fisher matrices | Finite differences of full count-and-readout likelihoods, including unknown-rate score blocks |
| Calibration dependence | Exact balanced law, fixed-imbalance crossover, root-time tolerance, and common-versus-differential rate errors |
| Random rate diversity | Finite-time law, fair-choice guarantee, probability sensitivity, and 300 maximizing-pair comparisons |
| Common nuisance versus independent directions | Pool-then-eliminate check and an explicit separate-nuisance comparison |
| Input and stopping domains | Invalid-input rejection and an event guard that raises rather than discarding trajectories |

The scientific suite contains 53 tests: 33 in `tests/test_nras.py` and 20 in `tests/test_preset.py`. `scripts/check.py` also checks local links, document anchors, and basic mathematics delimiters. The GitHub workflow runs the same command for pull requests and the main branch.

The complete-likelihood checks sum Poisson counts with cutoffs leaving less than $10^{-14}$ tail probability at their tested parameters. They finite-difference outcome probabilities rather than inserting analytical scores into the Fisher formula. This is a finite numerical cross-check, not proof of universal precision scaling. The short-step check verifies the coefficients used in the inherited channel bound, not a new proof of that general bound.

## A preset example

The rate units below set $a=1$, $b=3$. At $T=100$, a balanced echo has local information 2500. An echo with fractions 0.76 and 0.24 has information about 2440.20. At $T=10000$, the same fixed imbalance reduces its coefficient $\mathcal I/T^2$ to about 0.0228943, whereas the balanced value remains 0.25. A fair recorded choice of one rate approaches coefficient 0.2 without balancing.

Run these deterministic formulas with:

```bash
PYTHONPATH=src python -c 'from preset import echo_information, mixture_information; T=10000; print(echo_information(1,3,.76*T,.24*T)/T**2, mixture_information([1,1],[1,3],[.5,.5],T)/T**2)'
```

These are local-information values for the specified complete experiments. A random-rate interrogation of duration $T$ costs $T$ on each repetition. No global risk is inferred from the coefficient.

## Interpreting results

The event simulator samples exact alternating exponential waiting times. A failed run is returned with `completed=False` and physical time equal to the deadline. An event-count guard raises an error rather than silently discarding long trajectories. Equal-rate simulations require a deadline because the untruncated first-passage mean is infinite.

The source code models ideal rate control and syndrome timing. The finite-cadence function computes the separately proved local signed drift; it does not simulate faulty readout or claim global robustness. The global frequency-estimation theorem is an analytical reduction in [stopped sensing](STOPPED_SENSING.md), not a conclusion inferred from samples or from the preset Fisher matrices.

Numerical and symbolic checks test specified expressions. They do not establish independent scientific replication, bibliographic priority, or correct appearance in GitHub's hosting renderer. Mathematical display should additionally be inspected on the rendered README, tutorial, and representative proof pages.
