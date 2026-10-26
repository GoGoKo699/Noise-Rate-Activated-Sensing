# Working in this repository

The authorized project is `GoGoKo699/Noise-Rate-Activated-Sensing`. Modify only this repository. Other project repositories are read-only unless separately authorized in the appropriate context.

## Read the science first

Start with [README](README.md) and the [scientific synthesis](science/interpretation.md). Read [microscopic global precision](science/microscopic_global_precision.md) and [recorded-phase estimation](science/recorded_phase_estimation.md) for the principal finite-strength claim. The [Markovian model](science/model.md), [local theorems](science/precision_bounds.md) and [stopped sensing](science/stopped_sensing.md) supply its separately proved counterpart. Consult [physical scope](science/physical_scope.md) for resource assumptions and [attribution](references/RELATED_WORK.md) before describing novelty. Use [llms.txt](llms.txt) as a question-to-file map.

Keep the main distinctions intact: continuous unknown direction versus a finite promise; efficient nuisance-adjusted information versus a target-only matrix entry; hard physical time versus effective signed time; local precision versus global risk; shared-axis incoherent rate selection versus bath access or coherent application of the unknown error. Retain failures in all time-budget comparisons. Treat finite-interval syndrome extraction as the local compensated result actually proved.

The full proofs live in the documents, and executable checks support specified finite identities. Passing tests, repeated assistant review, and a finished repository do not establish independent replication or priority. Attribute the channel bound, noise-assisted feedback, and phase-estimation methods to their sources.

## Make changes coherently

Inspect the current default-branch head and relevant open pull requests before writing. Pin the base; preserve concurrent work and the existing MIT license. Use a focused branch and pull request, without force-pushing. Recheck the base and head before merging, inspect the actual diff, run `python scripts/check.py`, and verify the remote merge. Report only checks actually executed. A missing local checkout is not evidence of a broken remote repository.

Present the repository as a scientific record, not a development diary. Keep assumptions, attribution, claim scope, and reproducibility visible. Avoid progress dashboards, speculative task catalogues, duplicate derivations, and publication-target messaging. Do not add a manuscript, public release, or visibility change as routine maintenance.

Use GitHub-native math fences for display equations and protected dollar/backtick spans for inline equations. Bare dollar delimiters have corrupted escapes, stars, and matrix rows in this repository’s hosted output; do not reintroduce them. Use the checked upright named-function notation rather than the rejected operatorname macro. Keep equations out of headings and complicated tables, avoid undefined macros, and inspect rendered pages when changing mathematical display. Source checks alone do not establish correct hosting-renderer output.

## Shared learning material

The common educational anchor for both sister projects is **Rivas and Huelga, Open Quantum Systems: An Introduction, arXiv:1104.5242v2**. The [source bridge](learning/ANCHOR.md) owns this repository's section map, notation translations and local statistical connections. The [30-milestone map](learning/MILESTONES.md) has 13 background and 17 narrative targets, defined by the project and shared by every reader. Preserve one educational anchor; primary research citations are not additional assigned textbooks. Do not replace physical time by probe number or change the established rate normalization.

Keep the common milestones, source bridge, and scientific examples in `learning/`. Personal coaching procedures, answer keys, assessments, and learner progress stay outside this repository. Maintenance does not start lessons or certify anyone's understanding.

## Repository structure

`science/` holds the connected topic-based account, `learning/` the shared learning route, `references/` the primary-source comparison and bibliography, and `verification/` the verification guide. Preserve the established executable paths in `src/`, `scripts/`, `tests/`, and `results/`. Give each scientific result one authoritative home and update every incoming link when moving it. Do not recreate the superseded `docs/` or `literature/` entrypoints as duplicate accounts.

The explanatory report PDF is in `learning/report/` and its matching self-contained LaTeX is in `learning/source/`. The README report entry links only the PDF; the verification guide owns compilation instructions. Preserve source/PDF agreement, build with pdfLaTeX from TeX Live 2025, require the fresh output and final log, and inspect all pages after meaningful changes. Keep private preparation records and unpublished manuscript material outside public branches and artifacts. The report supplements the canonical science and attribution; it does not replace them.

Run `python scripts/check.py` and `python scripts/check_reproducibility.py`. The first includes the 30-milestone dependency and shared-content checks. When public pages change, run the hosted browser audit on the immutable proposed commit and inspect its screenshots before making a rendering-readiness claim. Record the actual checked revision and scope in the pull request, not a scientific progress dashboard.
