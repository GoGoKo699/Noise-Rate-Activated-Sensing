# Working in this repository

The authorized project is `GoGoKo699/Noise-Rate-Activated-Sensing`. Modify only this repository. Other project repositories are read-only unless separately authorized in the appropriate context.

## Read the science first

Start with [README](README.md), [model](docs/MODEL.md), and [theorems](docs/THEOREMS.md). Read [stopped sensing](docs/STOPPED_SENSING.md) for timing and global estimation, [physical scope](docs/PHYSICAL_SCOPE.md) for resource assumptions, and [attribution](literature/RELATED_WORK.md) before describing novelty. Use [llms.txt](llms.txt) as a question-to-file map.

Keep the main distinctions intact: continuous unknown direction versus a finite promise; efficient nuisance-adjusted information versus a target-only matrix entry; hard physical time versus effective signed time; local precision versus global risk; shared-axis incoherent rate selection versus bath access or coherent application of the unknown error. Retain failures in all time-budget comparisons. Treat finite-interval syndrome extraction as the local compensated result actually proved.

The full proofs live in the documents, and executable checks support specified finite identities. Passing tests, repeated assistant review, and a finished repository do not establish independent replication or priority. Attribute the channel bound, noise-assisted feedback, and phase-estimation methods to their sources.

## Make changes coherently

Inspect the current default-branch head and relevant open pull requests before writing. Pin the base; preserve concurrent work and the existing MIT license. Use a focused branch and pull request, without force-pushing. Recheck the base and head before merging, inspect the actual diff, run `python scripts/check.py`, and verify the remote merge. Report only checks actually executed. A missing local checkout is not evidence of a broken remote repository.

Present the repository as a scientific record, not a development diary. Keep assumptions, attribution, claim scope, and reproducibility visible. Avoid progress dashboards, speculative task catalogues, duplicate derivations, and publication-target messaging. Do not add a manuscript, public release, or visibility change as routine maintenance.

Use GitHub-native Markdown with supported dollar-delimited mathematics. Keep equations out of headings and complicated tables, avoid undefined macros, and inspect rendered pages when changing mathematical display. Source checks alone do not establish correct hosting-renderer output.

## Learning and coaching

The settled educational anchor is **Haase et al., arXiv:1807.11882v4**. Read the [learning guide](docs/LEARNING_GUIDE.md) for the source map, notation hazards, project-specific bridges, and readiness domains. Keep one educational anchor; primary research citations do not become additional assigned textbooks. Do not reopen the source choice without a substantive reason. Preserve the project's rate normalization rather than copying inconsistent source formulas, and do not replace time resources by probe-number resources.

For an explicitly requested coaching session, teach directly from the [worked tutorial](docs/TUTORIAL.md) and its linked proofs, without making prior reading a condition. Use Revise → Learn → Test, one selection-only question at a time, targeted revision after mistakes, and evidence-based readiness. Prefer actual clickable answer controls when available; never describe plain-text options as interactive. Do not start unsolicited quizzes during repository maintenance.
