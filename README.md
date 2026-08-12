# Structural Reorganization Dynamics

Reproducibility and proof-audit companion for the paper **Structural Reorganization Dynamics in Dimensional-Structural Describability** by **Kwon Dominicus**.

This repository is intentionally different from the older observational consistency-validation repository. Its purpose is to reproduce finite witnesses, exact algebraic identities, countermodels, and representative analytic specializations used by the current dynamics paper.

## Scope

The executable package checks:

- constant-trajectory existence and fixed-time static recovery;
- coherence of canonical fixed-background lineage and finite lineage branching;
- smooth realized-line evolution with a rank transition at fixed channel support;
- component-term differentiation and the reference-density variable-measure product rule;
- non-uniqueness of constitutive coefficient extraction from the same static property input;
- a scalar transport finite-support specialization;
- first-order characteristic-speed computation;
- the rank-one nonunique-speed counterexample;
- dimension-independent isotropic second-order wave speed;
- the separate RMS `sqrt(N)` capacity identity;
- covering-number and Shannon-type directional entropy specializations;
- an identity-front diagnostic inequality instance;
- logical independence of realized-axis rank and a closure-associated scalar property;
- aggregate cancellation with different component states;
- undefined application versus defined zero;
- the `D_w` readout-collision witness.

The package does **not** claim to machine-prove the general symmetric-hyperbolic finite-propagation theorem or the full typed DSD framework. Those remain mathematical results and definitions in the manuscript. See `PROOF_MAP.md`.

## Repository structure

```text
src/reproduce_dynamics.py       deterministic executable checks
tests/test_reproduction.py      pytest regression tests
results/                        deterministic generated summaries
PROOF_MAP.md                    manuscript-result to executable-check map
REPRODUCIBILITY.md              run instructions and interpretation rules
requirements.txt                Python dependencies
.github/workflows/reproducibility.yml
```

## Run on Windows 11

From the repository root in PowerShell or CMD:

```powershell
python -m pip install -r requirements.txt
python "src\reproduce_dynamics.py" --output "results"
python -m pytest -q
```

Expected headline output:

```text
Structural Reorganization Dynamics reproducibility: 18/18 checks passed
```

Generated files:

```text
results\reproduction_summary.json
results\reproduction_summary.md
```

## Interpretation

A passing executable check means that the displayed finite witness, exact identity, or selected specialization is reproduced by the code. It does not promote a numerical example into a proof of a general theorem and it does not replace the manuscript's analytic hypotheses.

## Author

Kwon Dominicus  
Independent Researcher, Incheon, Republic of Korea
