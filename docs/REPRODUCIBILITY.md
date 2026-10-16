# Reproducibility

[Overview](../README.md) · [Proofs](THEOREMS.md) · [Reference implementation](../src/nras.py)

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

The [recorded example](../results/example.json) includes exact parameter values, random seeds, sample counts, and dependency versions. Sampling output can depend on library versions; the analytical quantities are the comparison targets. Tests use fixed seeds and stated numerical tolerances rather than requiring identical floating-point output across platforms.

## Coverage

| Calculation | Executed check |
|---|---|
| Unknown-error algebra and recovery phase | Pauli identities and direct matrix multiplication |
| Nuisance-path cancellation | Numerical operator tests and symbolic simplification |
| Exact trajectory phase | 500 random chronological matrix products, including odd endpoints |
| Optimal selectable-setting coefficient | 500 random families compared with a separate linear program |
| Collision-induced channel | Explicit environment trace versus the analytic channel |
| First-passage law | Backward-equation identities, symbolic moments, and 30,000 event samples |
| Deadline resource accounting | 20,000 samples, retaining failures at their full deadline cost |
| Symmetric fixed-rate signed time | Finite differences of an independent tilted-generator propagator |
| Finite-interval signed drift | Augmented-generator propagation versus the closed form |
| Input domains and simulation guard | Rejection of invalid rates, parameters, and uncharged truncation |

The scientific suite contains 33 tests. `scripts/check.py` also checks local links, document anchors, and basic mathematics delimiters. The GitHub workflow runs the same command for pull requests and the main branch.

## Interpreting results

The event simulator samples the exact alternating exponential waiting times; it is not a time-discretized approximation. A failed run is returned with `completed=False` and physical time equal to the deadline. An event-count guard raises an error rather than silently discarding long trajectories. Equal-rate simulations require a deadline because the untruncated first-passage mean is infinite.

The source code models ideal rate control and syndrome timing. The finite-cadence function computes the separately proved local signed drift; it does not simulate faulty readout or claim global robustness. The global frequency-estimation theorem is an analytical reduction in [stopped sensing](STOPPED_SENSING.md), not a conclusion inferred from these samples.

Numerical and symbolic checks test the specified expressions. They do not establish universal asymptotics, independent scientific replication, bibliographic priority, or correct appearance in GitHub's hosting renderer. Mathematical display should additionally be inspected on the rendered README, tutorial, and representative proof pages.
