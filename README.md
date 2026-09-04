# Structural Reorganization Dynamics

Reproducibility and proof-audit companion for **Structural Reorganization Dynamics in Dimensional-Structural Describability** by **Kwon Dominicus**.

## Release 2.0

Version 2.0 follows the revised manuscript hierarchy:

1. a fixed Stage-VI Formation background supports the general dynamic core;
2. the general Property Axiom System is an optional downstream interface;
3. realized-axis geometry is an optional specialization rather than a universal property coordinate.

The executable checks are classified accordingly. General hyperbolic characteristic mathematics and metric-direction entropy remain in the analytic core, while rank-dependent checks are explicitly marked as realized-axis specializations.

## Scope

The executable package checks:

- constant-trajectory existence and fixed-time static recovery without mandatory Property or realized-axis data;
- coherence of canonical fixed-background lineage and finite lineage branching;
- the full Property Axiom System status partition and an explicit coarse dynamic status map;
- component-term differentiation and the reference-density variable-measure product rule;
- explicit constitutive-bridge choice for typed property records;
- a scalar transport finite-support specialization;
- a general first-order characteristic-speed computation;
- covering-number and Shannon-type directional entropy on a supplied metric direction space;
- an identity-front diagnostic inequality instance;
- aggregate cancellation with different component states;
- the `D_w` readout-collision witness;
- optional realized-axis checks: smooth rank transition, rank-one nonunique characteristic speed, and rank/specialized-property independence;
- isotropic second-order speed and the separate RMS `sqrt(N)` capacity identity.

General symmetric-hyperbolic finite propagation and other quantified analytic results remain manuscript proofs. `PROOF_MAP.md` records the executable/manuscript boundary.

## Repository structure

```text
src/reproduce_dynamics.py       deterministic executable checks
tests/test_reproduction.py      pytest regression tests
results/                        deterministic generated summaries
PROOF_MAP.md                    manuscript-result to executable-check map
REPRODUCIBILITY.md              run instructions and interpretation rules
RELEASE_NOTES_2.0.md            release-2.0 change summary
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
Structural Reorganization Dynamics 2.0 reproducibility: 18/18 checks passed
```

Generated files:

```text
results\reproduction_summary.json
results\reproduction_summary.md
```

## Interpretation

A passing executable check reproduces the displayed finite witness, exact identity, or selected analytic specialization. The mathematical status of each result remains the one stated in the manuscript and `PROOF_MAP.md`.

## Author

Kwon Dominicus  
Independent Researcher, Incheon, Republic of Korea
