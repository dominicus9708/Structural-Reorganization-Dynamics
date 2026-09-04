# Computational proof map — release 2.0

This map separates the revised manuscript layers and records what the executable companion reproduces.

| Layer | Manuscript result / construction | Executable support | Scope |
|---|---|---|---|
| General dynamic core | Fixed-time static recovery | `check_constant_trajectory_and_static_recovery()` | Finite instantiated slice/readout check; no Property or realized-axis data required |
| General dynamic core | Constant-trajectory extension | same check | Reproduces one nonempty constant trajectory |
| General dynamic core | Canonical fixed-background lineage | `check_canonical_lineage_coherence()` | Exact finite relation-composition check |
| General dynamic core | Finite lineage branching | `check_lineage_branching()` | Reproduces a one-to-two successor relation |
| Optional Property interface | Full property-status discipline and explicit coarse status map | `check_property_status_partition()` | Reproduces undeclared, profile-unavailable, inapplicable, prerequisite-unsatisfied, applicable-but-undefined, defined-zero, and defined-nonzero/value distinctions |
| Optional Property interface | No canonical coefficient extraction supplied by the Property Axiom System | `check_constitutive_bridge_choice()` | Two explicit bridges over the same typed property record; finite nonuniqueness witness only |
| General analytic realization | Component-term differentiation | `check_component_term_differentiation()` | Symbolically verifies a normalized polynomial specialization |
| General analytic realization | Variable-measure reference-density rule | `check_variable_measure_reference_density()` | Symbolically verifies the three-term product rule in one specialization |
| General propagation | Finite propagation definition | `check_scalar_transport_support()` | Scalar-advection support specialization |
| General propagation | Symmetric-hyperbolic finite-propagation theorem | none | General energy-domain proof remains manuscript-level |
| General characteristic analysis | First-order characteristic bound | `check_first_order_characteristic_bound()` | Exact scalar 2D advection specialization with supremum `5`; no realized-axis assumption |
| General characteristic analysis | Isotropic second-order speed need not scale with localization dimension | `check_isotropic_second_order_speed()` | Reproduces `sqrt(k/m)` for dimensions `1..8` |
| Realized-axis specialization | Smooth line path with rank transition | `check_realized_axis_rank_transition()` | Exact rank computation for the displayed `R^2` witness |
| Realized-axis specialization | No universal rank-only characteristic law | `check_rank_only_speed_counterexample()` | Exact rank-one two-speed witness |
| Realized-axis specialization | Rank / specialization-specific property independence | `check_rank_specialized_property_independence()` | Reproduces both finite countermodel directions |
| Directional descriptor | Metric covering/Shannon entropy | `check_directional_entropy()` | Exact finite discrete-metric specialization; rank is not required |
| Appendix specialization | RMS `sqrt(N)` capacity model | `check_rms_special_model()` | Exact Euclidean norm identity for `N=1..8`; not a propagation-speed law |
| General identity diagnostic | Identity-front bound | `check_identity_front_bound()` | Exact inequality instance; general infimum argument remains manuscript-level |
| General reduced readout | Aggregate-invisible component distinction | `check_aggregate_collision()` | Exact symbolic cancellation witness |
| Scalar specialization | Equal `D_w` does not imply equal dynamic state | `check_dw_collision()` | Exact integration of the manuscript's `[0,1]`, `w=1` vs `w=2x` witness |

The repository is a reproducibility and proof-audit companion rather than a formalization of the complete typed theory.
