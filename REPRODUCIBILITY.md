# Reproducibility protocol

## 1. Purpose

The code reproduces finite witnesses and exact specializations stated in *Structural Reorganization Dynamics in Dimensional-Structural Describability*.

The governing rule is conservative: executable agreement supports the displayed construction; it does not replace a general proof.

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

## 5. Deterministic outputs

The main run writes:

- `results/reproduction_summary.json`
- `results/reproduction_summary.md`

No random seed is needed because the current baseline uses exact symbolic and deterministic finite constructions.

## 6. Status of the checks

The package distinguishes four levels:

1. **Exact finite witness** - direct reproduction of a displayed countermodel or finite relation.
2. **Exact algebraic identity** - symbolic verification of an identity used by the manuscript.
3. **Representative analytic specialization** - a concrete model satisfying a more general definition or theorem hypothesis.
4. **Manuscript-only general proof** - a theorem whose full quantifiers, regularity hypotheses, or PDE estimates are not reduced to finite computation.

In particular, the symmetric-hyperbolic finite-propagation theorem remains a manuscript proof supported by standard hyperbolic PDE mathematics. The executable scalar transport check is not presented as its replacement.

## 7. Input/output paths

This baseline requires no external dataset.

Input is encoded directly as the manuscript's finite witness data in:

```text
src/reproduce_dynamics.py
```

Output begins at:

```text
results/
```

This is a proof-audit pipeline rather than an observational `raw -> derived -> theory layer` data pipeline.
