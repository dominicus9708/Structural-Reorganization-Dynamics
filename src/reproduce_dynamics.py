from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Iterable

import sympy as sp


@dataclass(frozen=True)
class CheckResult:
    name: str
    passed: bool
    manuscript_scope: str
    details: dict[str, Any]


def _serialize(value: Any) -> Any:
    if isinstance(value, sp.Basic):
        return str(sp.simplify(value))
    if isinstance(value, dict):
        return {str(k): _serialize(v) for k, v in value.items()}
    if isinstance(value, (list, tuple, set)):
        return [_serialize(v) for v in value]
    if isinstance(value, Path):
        return str(value)
    return value


def _result(name: str, passed: bool, scope: str, **details: Any) -> CheckResult:
    return CheckResult(name=name, passed=bool(passed), manuscript_scope=scope, details=_serialize(details))


def compose_relations(r_ab: set[tuple[str, str]], r_bc: set[tuple[str, str]]) -> set[tuple[str, str]]:
    return {(a, c) for a, b1 in r_ab for b2, c in r_bc if b1 == b2}


def check_constant_trajectory_and_static_recovery() -> CheckResult:
    static_state = {
        "formation_background": "B0",
        "channels": ("c1", "c2"),
        "axis_lines": ((1, 0), (0, 1)),
        "analytic_terms": (sp.Integer(2), sp.Integer(-1)),
    }
    times = (sp.Integer(0), sp.Rational(1, 2), sp.Integer(1))
    trajectory = {str(t): static_state.copy() for t in times}
    aggregates = {str(t): sum(trajectory[str(t)]["analytic_terms"], sp.Integer(0)) for t in times}
    passed = all(trajectory[str(t)] == static_state for t in times) and all(v == 1 for v in aggregates.values())
    return _result("constant_trajectory_static_recovery", passed,
                   "Propositions: constant-trajectory extension and fixed-time static recovery",
                   times=times, aggregate_at_each_time=aggregates)


def check_canonical_lineage_coherence() -> CheckResult:
    channels = {"c1", "c2", "c3"}
    ident = {(c, c) for c in channels}
    composed = compose_relations(ident, ident)
    return _result("canonical_fixed_background_lineage", composed == ident,
                   "Proposition: canonical fixed-background lineage",
                   identity_relation=sorted(ident), composition=sorted(composed))


def check_lineage_branching() -> CheckResult:
    branch = {("c", "c1"), ("c", "c2")}
    outgoing = {b for a, b in branch if a == "c"}
    return _result("finite_lineage_branching", outgoing == {"c1", "c2"} and len(branch) == 2,
                   "Toy model: finite lineage branching",
                   lineage_relation=sorted(branch), successor_count=len(outgoing))


def check_rank_transition() -> CheckResult:
    t = sp.symbols("t", real=True)
    v1 = sp.Matrix([1, 0])
    v2 = sp.Matrix([1, t])
    samples = [sp.Integer(-2), sp.Integer(-1), sp.Integer(0), sp.Integer(1), sp.Integer(2)]
    ranks = {}
    for tv in samples:
        ranks[str(tv)] = sp.Matrix.hstack(v1, v2.subs(t, tv)).rank()
    passed = ranks["0"] == 1 and all(ranks[str(tv)] == 2 for tv in samples if tv != 0)
    return _result("smooth_line_rank_transition", passed,
                   "Example: smooth line path with rank transition",
                   sampled_ranks=ranks, determinant=sp.Matrix.hstack(v1, v2).det())


def check_component_term_differentiation() -> CheckResult:
    x, t = sp.symbols("x t", real=True)
    zeta = x + t * x**2
    weight = 1 + t * (2 * x - 1)
    normalization = sp.integrate(weight, (x, 0, 1))
    term = sp.integrate(zeta * weight, (x, 0, 1))
    lhs = sp.diff(term, t)
    rhs = sp.integrate(sp.diff(zeta, t) * weight + zeta * sp.diff(weight, t), (x, 0, 1))
    difference = sp.simplify(lhs - rhs)
    return _result("component_term_differentiation", sp.simplify(normalization - 1) == 0 and difference == 0,
                   "Proposition: component-term differentiation under fixed measure",
                   normalized_weight_integral=normalization, component_term=sp.expand(term),
                   derivative=sp.expand(lhs), product_rule_integral=sp.expand(rhs), difference=difference)


def check_variable_measure_reference_density() -> CheckResult:
    x, t = sp.symbols("x t", real=True)
    zeta = 1 + t * x
    weight = 1 + t * (2 * x - 1)
    density = 1 + t * x**2
    term = sp.integrate(zeta * weight * density, (x, 0, 1))
    lhs = sp.diff(term, t)
    rhs = sp.integrate(sp.diff(zeta, t) * weight * density
                       + zeta * sp.diff(weight, t) * density
                       + zeta * weight * sp.diff(density, t), (x, 0, 1))
    difference = sp.simplify(lhs - rhs)
    return _result("variable_measure_reference_density", difference == 0,
                   "Appendix: reference-density derivative with variable measure",
                   component_term=sp.expand(term), derivative=sp.expand(lhs),
                   three_term_integral=sp.expand(rhs), difference=difference)


def check_constitutive_nonuniqueness() -> CheckResult:
    property_value = sp.Integer(1)
    coeff_a = 2 * property_value
    coeff_b = 5 * property_value
    return _result("constitutive_bridge_nonuniqueness", coeff_a != coeff_b,
                   "Proposition: no dynamic coefficient determination from a property label/value alone",
                   same_static_property=property_value, bridge_A_output=coeff_a, bridge_B_output=coeff_b)


def check_scalar_transport_support() -> CheckResult:
    beta = sp.Rational(3, 2)
    initial = (sp.Integer(-1), sp.Integer(1))
    times = [sp.Integer(0), sp.Rational(1, 2), sp.Integer(1), sp.Integer(2)]
    rows = []
    passed = True
    for tv in times:
        shifted = (initial[0] + beta * tv, initial[1] + beta * tv)
        cone = (initial[0] - abs(beta) * tv, initial[1] + abs(beta) * tv)
        contained = shifted[0] >= cone[0] and shifted[1] <= cone[1]
        passed = passed and bool(contained)
        rows.append({"t": tv, "translated_support": shifted, "speed_cone": cone, "contained": bool(contained)})
    return _result("scalar_transport_finite_support", passed,
                   "Analytic specialization of the finite-propagation definition for u_t + beta u_x = 0",
                   beta=beta, checks=rows)


def check_first_order_characteristic_bound() -> CheckResult:
    a1, a2 = sp.Integer(3), sp.Integer(4)
    cchar = sp.sqrt(a1**2 + a2**2)
    sample_dirs = [(1, 0), (0, 1), (sp.Rational(3, 5), sp.Rational(4, 5))]
    speeds = [abs(sp.simplify(a1 * n1 + a2 * n2)) for n1, n2 in sample_dirs]
    return _result("first_order_characteristic_bound", cchar == 5 and max(speeds) == 5,
                   "Section: first-order characteristic upper bound",
                   transport_vector=(a1, a2), exact_supremum=cchar, sampled_directional_speeds=speeds)


def check_rank_only_speed_counterexample() -> CheckResult:
    rank = 1
    beta_a, beta_b = sp.Integer(1), sp.Integer(3)
    return _result("rank_one_nonunique_characteristic_speed", rank == 1 and abs(beta_a) != abs(beta_b),
                   "Proposition: no universal rank-only characteristic law",
                   realized_axis_rank=rank, model_A_speed=abs(beta_a), model_B_speed=abs(beta_b))


def check_isotropic_second_order_speed() -> CheckResult:
    m, k = sp.Integer(4), sp.Integer(9)
    expected = sp.sqrt(k / m)
    dimensions = list(range(1, 9))
    speeds = {d: expected for d in dimensions}
    passed = all(sp.simplify(v - sp.Rational(3, 2)) == 0 for v in speeds.values())
    return _result("dimension_independent_isotropic_wave_speed", passed,
                   "Countermodel: isotropic second-order characteristic speed does not obey universal sqrt(N) scaling",
                   m=m, k=k, dimensions=dimensions, speed_by_dimension=speeds)


def check_rms_special_model() -> CheckResult:
    c0 = sp.Integer(3)
    rows = {}
    passed = True
    for n in range(1, 9):
        norm = sp.sqrt(sum(c0**2 for _ in range(n)))
        expected = sp.sqrt(n) * c0
        ok = sp.simplify(norm - expected) == 0
        rows[n] = {"norm": norm, "sqrtN_c0": expected, "match": ok}
        passed = passed and ok
    return _result("rms_sqrtN_special_model", passed, "Appendix: RMS directional special model", c0=c0, cases=rows)


def discrete_covering_number(cardinality: int, epsilon: float) -> int | None:
    if cardinality <= 0:
        return None
    return cardinality if epsilon < 1.0 else 1


def shannon_entropy(probabilities: Iterable[sp.Rational]) -> sp.Expr:
    value = sp.Integer(0)
    for p in probabilities:
        if p != 0:
            value -= p * sp.log(p)
    return sp.simplify(value)


def check_directional_entropy() -> CheckResult:
    m_small = discrete_covering_number(4, 0.5)
    m_large = discrete_covering_number(4, 1.0)
    empty = discrete_covering_number(0, 0.5)
    s_uniform = shannon_entropy([sp.Rational(1, 4)] * 4)
    s_concentrated = shannon_entropy([sp.Integer(1), sp.Integer(0), sp.Integer(0), sp.Integer(0)])
    passed = m_small == 4 and m_large == 1 and empty is None and sp.simplify(s_uniform - sp.log(4)) == 0 and s_concentrated == 0
    return _result("directional_entropy_resolution_and_distribution", passed,
                   "Section: covering-number and distributional directional entropy",
                   covering_number_epsilon_0_5=m_small, covering_number_epsilon_1_0=m_large,
                   empty_direction_space_status="undefined" if empty is None else empty,
                   max_entropy_epsilon_0_5=sp.log(m_small), max_entropy_epsilon_1_0=sp.log(m_large),
                   uniform_shannon=s_uniform, concentrated_shannon=s_concentrated)


def check_identity_front_bound() -> CheckResult:
    ell, delta_t, c_info = sp.Integer(6), sp.Integer(3), sp.Rational(5, 2)
    c_front = ell / delta_t
    return _result("identity_front_bound", c_front <= c_info,
                   "Proposition: identity-front diagnostic rate is bounded by an admissible infimal propagation bound under stated assumptions",
                   distance=ell, arrival_time=delta_t, identity_front_rate=c_front, c_info=c_info)


def check_rank_closure_independence() -> CheckResult:
    e1, e2, e3 = sp.eye(3).col(0), sp.eye(3).col(1), sp.eye(3).col(2)
    rank_fixed = sp.Matrix.hstack(e1, e2, e3).rank()
    closure_a, closure_b = 0, 1
    rank_at_0 = sp.Matrix.hstack(sp.Matrix([1, 0]), sp.Matrix([1, 0])).rank()
    rank_at_1 = sp.Matrix.hstack(sp.Matrix([1, 0]), sp.Matrix([1, 1])).rank()
    fixed_closure = 0
    passed = rank_fixed == 3 and closure_a != closure_b and rank_at_0 == 1 and rank_at_1 == 2 and fixed_closure == 0
    return _result("rank_closure_logical_independence", passed,
                   "Countermodels: closure-associated property change at fixed rank and rank change at fixed closure-associated property",
                   fixed_rank=rank_fixed, closure_values=(closure_a, closure_b),
                   rank_transition=(rank_at_0, rank_at_1), fixed_closure_value=fixed_closure)


def check_aggregate_collision() -> CheckResult:
    t = sp.symbols("t", real=True)
    f, g = t + 1, t**2 + 2
    aggregate_u, aggregate_v = sp.simplify(f - f), sp.simplify(g - g)
    component_difference = sp.simplify(f - g)
    return _result("same_aggregate_different_component_state", aggregate_u == 0 and aggregate_v == 0 and component_difference != 0,
                   "Proposition/toy model: aggregate cancellation does not erase component-resolved distinction",
                   aggregate_U=aggregate_u, aggregate_V=aggregate_v, component_difference=component_difference)


def check_undefined_vs_defined_zero() -> CheckResult:
    state_1 = {"status": "undefined", "value": None}
    state_2 = {"status": "defined_zero", "value": 0}
    return _result("undefined_vs_defined_zero", state_1 != state_2,
                   "Toy model: status data distinguish undefined application from defined zero",
                   typed_state_t1=state_1, typed_state_t2=state_2, zero_padded_values=(0, 0))


def check_dw_collision() -> CheckResult:
    x = sp.symbols("x", real=True)
    alpha, w_u, w_v = sp.Integer(1), sp.Integer(1), 2 * x
    norm_u = sp.integrate(w_u, (x, 0, 1))
    norm_v = sp.integrate(w_v, (x, 0, 1))
    d_u = sp.integrate(alpha * w_u, (x, 0, 1))
    d_v = sp.integrate(alpha * w_v, (x, 0, 1))
    passed = norm_u == norm_v == 1 and d_u == d_v == 1 and sp.simplify(w_u - w_v) != 0
    return _result("Dw_readout_collision", passed,
                   "Proposition: equal D_w(t) does not imply equal component-resolved dynamic state",
                   weight_U=str(w_u), weight_V=str(w_v), normalized_integrals=(norm_u, norm_v), Dw_values=(d_u, d_v))


def run_all_checks() -> list[CheckResult]:
    return [
        check_constant_trajectory_and_static_recovery(),
        check_canonical_lineage_coherence(),
        check_lineage_branching(),
        check_rank_transition(),
        check_component_term_differentiation(),
        check_variable_measure_reference_density(),
        check_constitutive_nonuniqueness(),
        check_scalar_transport_support(),
        check_first_order_characteristic_bound(),
        check_rank_only_speed_counterexample(),
        check_isotropic_second_order_speed(),
        check_rms_special_model(),
        check_directional_entropy(),
        check_identity_front_bound(),
        check_rank_closure_independence(),
        check_aggregate_collision(),
        check_undefined_vs_defined_zero(),
        check_dw_collision(),
    ]


def render_markdown(results: list[CheckResult]) -> str:
    passed = sum(r.passed for r in results)
    lines = [
        "# Structural Reorganization Dynamics - reproducibility summary", "",
        f"Passed: **{passed}/{len(results)}** executable checks.", "",
        "These checks reproduce finite witnesses, algebraic identities, and representative specializations from the manuscript. They do not replace the manuscript proofs of general analytic theorems.", "",
        "| Check | Status | Manuscript scope |", "|---|---:|---|",
    ]
    for r in results:
        lines.append(f"| `{r.name}` | {'PASS' if r.passed else 'FAIL'} | {r.manuscript_scope} |")
    lines.extend(["", "## Detailed outputs", ""])
    for r in results:
        lines.extend([f"### {r.name}", "", f"Status: **{'PASS' if r.passed else 'FAIL'}**", "", "```json",
                      json.dumps(_serialize(r.details), indent=2, ensure_ascii=False, sort_keys=True), "```", ""])
    return "\n".join(lines)


def write_outputs(output_dir: Path) -> list[CheckResult]:
    output_dir.mkdir(parents=True, exist_ok=True)
    results = run_all_checks()
    payload = {
        "schema_version": 1,
        "paper": "Structural Reorganization Dynamics in Dimensional-Structural Describability",
        "author": "Kwon Dominicus",
        "all_passed": all(r.passed for r in results),
        "passed": sum(r.passed for r in results),
        "total": len(results),
        "checks": [asdict(r) | {"details": _serialize(r.details)} for r in results],
    }
    (output_dir / "reproduction_summary.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    (output_dir / "reproduction_summary.md").write_text(render_markdown(results) + "\n", encoding="utf-8")
    return results


def main() -> int:
    parser = argparse.ArgumentParser(description="Reproduce finite proof-audit checks for Structural Reorganization Dynamics.")
    parser.add_argument("--output", type=Path, default=Path("results"))
    args = parser.parse_args()
    results = write_outputs(args.output)
    failed = [r.name for r in results if not r.passed]
    print(f"Structural Reorganization Dynamics reproducibility: {len(results) - len(failed)}/{len(results)} checks passed")
    for r in results:
        print(f"[{'PASS' if r.passed else 'FAIL'}] {r.name}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
