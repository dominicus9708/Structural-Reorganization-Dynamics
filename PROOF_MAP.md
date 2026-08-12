# Computational proof map

This map separates what the executable companion reproduces from what remains a manuscript proof or definition.

| Manuscript result / construction | Executable support | Scope |
|---|---|---|
| Fixed-time static recovery | `check_constant_trajectory_and_static_recovery()` | Finite instantiated slice/readout check; general proposition remains manuscript-level |
| Constant-trajectory extension | same check | Reproduces a nonempty constant trajectory |
| Canonical fixed-background lineage | `check_canonical_lineage_coherence()` | Exact finite relation-composition check |
| Finite lineage branching | `check_lineage_branching()` | Reproduces the displayed one-to-two successor relation |
| Smooth line path with rank transition | `check_rank_transition()` | Exact rank computation for the displayed `R^2` witness |
| Component-term differentiation | `check_component_term_differentiation()` | Symbolically verifies a normalized polynomial specialization |
| Variable-measure reference-density rule | `check_variable_measure_reference_density()` | Symbolically verifies the three-term product rule in one specialization |
| No coefficient determination from labels/data alone | `check_constitutive_nonuniqueness()` | Two explicit bridges over identical static property input |
| Finite propagation definition | `check_scalar_transport_support()` | Analytic scalar-advection support specialization only |
| Symmetric-hyperbolic finite-propagation theorem | none | General energy-domain proof remains in the manuscript and cited hyperbolic PDE literature |
| First-order characteristic bound | `check_first_order_characteristic_bound()` | Exact scalar 2D advection specialization with supremum `5` |
| No universal rank-only characteristic law | `check_rank_only_speed_counterexample()` | Exact rank-one two-speed witness |
| Dimension-independent isotropic wave speed | `check_isotropic_second_order_speed()` | Reproduces `sqrt(k/m)` for dimensions `1..8` |
| RMS `sqrt(N)` capacity model | `check_rms_special_model()` | Exact Euclidean norm identity for `N=1..8` |
| Directional covering/Shannon entropy | `check_directional_entropy()` | Exact finite discrete-metric specialization; not thermodynamic entropy |
| Identity-front bound | `check_identity_front_bound()` | Exact inequality instance; general infimum proof remains manuscript-level |
| Rank / closure-property independence | `check_rank_closure_independence()` | Reproduces both displayed finite countermodel directions |
| Aggregate-invisible component distinction | `check_aggregate_collision()` | Exact symbolic cancellation witness |
| Undefined vs defined zero | `check_undefined_vs_defined_zero()` | Typed-status witness showing failure of zero padding |
| Equal `D_w` does not imply equal dynamic state | `check_dw_collision()` | Exact integration of the manuscript's `[0,1]`, `w=1` vs `w=2x` witness |

The repository is therefore a **reproducibility and proof-audit companion**, not an automated formalization of the entire theory.
