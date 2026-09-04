# Reproducibility protocol — release 2.0

## 1. Purpose

The code reproduces finite witnesses and exact analytic specializations stated in the revised *Structural Reorganization Dynamics in Dimensional-Structural Describability*.

Release 2.0 mirrors the manuscript hierarchy: the general dynamic core does not require a Property model or realized-axis geometry; those are optional interfaces when the selected model uses them.

## 2. Environment

Recommended:

- Python 3.11 or newer
- SymPy 1.12+
- pytest 8+

Install from the repository root:

```powershell
python -m pip install -r requirements.txt
```

## 3. Main run

```powershell
python "src\reproduce_dynamics.py" --output "results"
```

The command exits with code `0` only when every declared check passes.

## 4. Regression tests

```powershell
python -m pytest -q
```

The release-2.0 baseline is:

```text
Structural Reorganization Dynamics 2.0 reproducibility: 18/18 checks passed
```

## 5. Deterministic outputs

The main run writes:

- `results/reproduction_summary.json`
- `results/reproduction_summary.md`

No random seed is needed because the baseline uses exact symbolic and deterministic finite constructions.

## 6. Layer discipline

Checks are interpreted in three principal layers.

1. **General dynamic/analytic core** — Formation-fixed trajectories, lineage, analytic terms, propagation, characteristic analysis, metric-direction entropy, identity diagnostics, and reduced readouts.
2. **Optional Property interface** — typed Property Axiom System statuses and explicitly supplied constitutive bridges.
3. **Optional realized-axis specialization** — line motion, realized-axis rank, and rank-restricted countermodels.

A check in a specialization is not promoted to a universal statement about every DSD dynamic model.

## 7. Status of executable evidence

The package distinguishes four levels:

1. **Exact finite witness** — direct reproduction of a displayed countermodel or finite relation.
2. **Exact algebraic identity** — symbolic verification of an identity used by the manuscript.
3. **Representative analytic specialization** — a concrete model satisfying a more general definition or theorem hypothesis.
4. **Manuscript-only general proof** — a theorem whose full quantifiers, regularity hypotheses, or PDE estimates are not reduced to finite computation.

The symmetric-hyperbolic finite-propagation theorem remains a manuscript proof. The scalar transport check is a specialization of the propagation definition, not a replacement proof.

## 8. Input/output paths

This baseline requires no external dataset.

Input is encoded directly as finite witness data in:

```text
src/reproduce_dynamics.py
```

Output begins at:

```text
results/
```

This is a proof-audit pipeline rather than an observational data pipeline.
