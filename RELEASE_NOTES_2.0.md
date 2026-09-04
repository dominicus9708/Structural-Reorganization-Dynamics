# Release 2.0

Release 2.0 updates the reproducibility companion to the revised DSD dynamics hierarchy.

## Main changes

- The fixed Stage-VI Formation background is sufficient for the general dynamic core.
- The general Property Axiom System is treated as an optional downstream interface.
- Realized-axis geometry is treated as an optional specialization rather than a universal property layer.
- The constant-trajectory witness no longer contains mandatory axis-line data.
- The executable status audit now reproduces the current Property Axiom System distinctions: undeclared, profile unavailable, inapplicable, prerequisite unsatisfied, applicable but undefined, defined zero, and defined nonzero/value.
- Constitutive-bridge checks are expressed as explicit bridge choices over typed property records.
- General characteristic-speed and metric-direction entropy checks remain outside the realized-axis specialization.
- Rank transition, rank-only speed, and rank/specialized-property independence are explicitly classified as realized-axis specialization checks.
- `closure-associated` terminology in the executable baseline is replaced by specialization-specific property terminology.
- Generated summaries now use schema version 2 and record release `2.0`.

## Reproducibility baseline

```text
Structural Reorganization Dynamics 2.0 reproducibility: 18/18 checks passed
```

```text
pytest: 3 passed
```
