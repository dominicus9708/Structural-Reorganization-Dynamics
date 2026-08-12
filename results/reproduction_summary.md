# Structural Reorganization Dynamics - reproducibility summary

Passed: **18/18** executable checks.

These checks reproduce finite witnesses, algebraic identities, and representative specializations from the manuscript. They do not replace the manuscript proofs of general analytic theorems.

| Check | Status | Manuscript scope |
|---|---:|---|
| `constant_trajectory_static_recovery` | PASS | Propositions: constant-trajectory extension and fixed-time static recovery |
| `canonical_fixed_background_lineage` | PASS | Proposition: canonical fixed-background lineage |
| `finite_lineage_branching` | PASS | Toy model: finite lineage branching |
| `smooth_line_rank_transition` | PASS | Example: smooth line path with rank transition |
| `component_term_differentiation` | PASS | Proposition: component-term differentiation under fixed measure |
| `variable_measure_reference_density` | PASS | Appendix: reference-density derivative with variable measure |
| `constitutive_bridge_nonuniqueness` | PASS | Proposition: no dynamic coefficient determination from a property label/value alone |
| `scalar_transport_finite_support` | PASS | Analytic specialization of the finite-propagation definition for `u_t + beta u_x = 0` |
| `first_order_characteristic_bound` | PASS | Section: first-order characteristic upper bound |
| `rank_one_nonunique_characteristic_speed` | PASS | Proposition: no universal rank-only characteristic law |
| `dimension_independent_isotropic_wave_speed` | PASS | Countermodel: isotropic second-order characteristic speed does not obey universal `sqrt(N)` scaling |
| `rms_sqrtN_special_model` | PASS | Appendix: RMS directional special model |
| `directional_entropy_resolution_and_distribution` | PASS | Section: covering-number and distributional directional entropy |
| `identity_front_bound` | PASS | Proposition: identity-front diagnostic rate is bounded by an admissible infimal propagation bound under stated assumptions |
| `rank_closure_logical_independence` | PASS | Countermodels: closure-associated property change at fixed rank and rank change at fixed closure-associated property |
| `same_aggregate_different_component_state` | PASS | Proposition/toy model: aggregate cancellation does not erase component-resolved distinction |
| `undefined_vs_defined_zero` | PASS | Toy model: status data distinguish undefined application from defined zero |
| `Dw_readout_collision` | PASS | Proposition: equal `D_w(t)` does not imply equal component-resolved dynamic state |

## Key exact outputs

- Rank-transition witness: determinant `t`, rank `1` at `t=0`, rank `2` at every sampled nonzero time.
- Component-term derivative: both sides reduce to `t/3 + 1/2`.
- Variable-measure derivative: both sides reduce to `9*t**2/20 + 7*t/6 + 5/6`.
- First-order characteristic example: transport vector `(3,4)` gives exact supremum `5`.
- Rank-one counterexample: identical rank `1`, speeds `1` and `3`.
- Isotropic second-order countermodel: `m=4`, `k=9` gives speed `3/2` for dimensions `1..8`.
- RMS special model: `||v||_2 = sqrt(N)c_0` reproduced exactly for `N=1..8`.
- Directional finite metric example: covering number `4` at `epsilon=0.5`, `1` at `epsilon=1`, empty direction space remains undefined.
- Identity-front example: `ell=6`, `Delta t=3` gives `c_front=2 <= c_info=5/2`.
- Rank/closure independence: fixed rank `3` with closure values `0` and `1`; fixed closure `0` with ranks `1` and `2`.
- Aggregate collision: both aggregate values vanish while component functions differ.
- `D_w` collision: weights `1` and `2x` are distinct but both normalize to `1` and both give `D_w=1` on `[0,1]` with local scaling exponent `1`.

The full machine-readable details are in `reproduction_summary.json` and can be regenerated with `python src/reproduce_dynamics.py --output results`.
