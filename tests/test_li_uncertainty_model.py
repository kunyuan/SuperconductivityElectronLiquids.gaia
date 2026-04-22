from pathlib import Path

from gaia.cli._packages import (
    apply_package_priors,
    compile_loaded_package_artifact,
    load_gaia_package,
)


PACKAGE_ROOT = Path(__file__).resolve().parents[1]


def _compiled_graph():
    loaded = load_gaia_package(PACKAGE_ROOT)
    apply_package_priors(loaded)
    return compile_loaded_package_artifact(loaded).graph


def _knowledge_by_label(graph):
    return {k.label: k for k in graph.knowledges if k.label}


def _ids_for_labels(graph, *labels):
    by_label = _knowledge_by_label(graph)
    return {by_label[label].id for label in labels}


def _param_value(knowledge, name):
    for param in knowledge.parameters:
        param_name = param["name"] if isinstance(param, dict) else param.name
        if param_name == name:
            return param["value"] if isinstance(param, dict) else param.value
    raise KeyError(name)


def _strategy_by_action_label(graph, action_label):
    suffix = f"::action::{action_label}"
    for strategy in graph.strategies:
        if strategy.metadata.get("action_label", "").endswith(suffix):
            return strategy
    raise KeyError(action_label)


def test_li_prediction_exposes_lattice_and_effective_coupling_uncertainty():
    graph = _compiled_graph()
    by_label = _knowledge_by_label(graph)

    assert "dfpt_lambda_error_bounded_for_simple_metals" not in by_label
    assert "shared_dfpt_lambda_error_model" in by_label
    assert "li_low_temperature_lattice_assumption" in by_label
    assert "li_effective_coupling_error_bounded" in by_label
    assert "li_tc_prediction_robust_to_exponential_sensitivity" not in by_label

    lattice = by_label["li_low_temperature_lattice_assumption"]
    assert lattice.metadata["prior"] <= 0.7

    shared_lambda_model = by_label["shared_dfpt_lambda_error_model"]
    assert 0.7 <= shared_lambda_model.metadata["prior"] <= 0.85

    li_predicted_id = by_label["tc_li_predicted"].id
    strategies = [s for s in graph.strategies if s.conclusion == li_predicted_id]
    assert strategies

    expected_premises = _ids_for_labels(
        graph,
        "ab_initio_workflow",
        "li_low_temperature_lattice_assumption",
        "li_effective_coupling",
        "li_effective_coupling_error_bounded",
    )
    assert expected_premises.issubset(set(strategies[0].premises))


def test_material_predictions_use_computed_effective_couplings_not_extra_lambda_warrant():
    graph = _compiled_graph()
    by_label = _knowledge_by_label(graph)
    assert "dfpt_lambda_error_bounded_for_simple_metals" not in by_label

    expected_effective_couplings = {
        "tc_al_predicted": "al_effective_coupling",
        "tc_zn_predicted": "zn_effective_coupling",
        "tc_li_predicted": "li_effective_coupling",
    }
    for prediction_label, coupling_label in expected_effective_couplings.items():
        predicted_id = by_label[prediction_label].id
        strategies = [s for s in graph.strategies if s.conclusion == predicted_id]
        assert strategies, f"missing strategy for {prediction_label}"
        assert by_label[coupling_label].id in strategies[0].premises


def test_effective_coupling_is_computed_from_lambda_and_mu_star():
    graph = _compiled_graph()
    by_label = _knowledge_by_label(graph)

    for label in ("al_effective_coupling", "zn_effective_coupling", "li_effective_coupling"):
        assert label in by_label
        strategies = [s for s in graph.strategies if s.conclusion == by_label[label].id]
        assert strategies, f"missing compute strategy for {label}"
        assert strategies[0].metadata["pattern"] == "computation"
        assert len(strategies[0].premises) == 2

    li_error_id = by_label["li_effective_coupling_error_bounded"].id
    li_error_strategies = [s for s in graph.strategies if s.conclusion == li_error_id]
    assert li_error_strategies
    assert by_label["li_effective_coupling"].id in li_error_strategies[0].premises

    li_g = by_label["li_effective_coupling"]
    assert _param_value(li_g, "value") == 0.1282
    assert _param_value(li_g, "uncertainty") == 0.0757
    assert _param_value(li_g, "lower") == 0.0525
    assert _param_value(li_g, "upper") == 0.2039


def test_mu_star_uncertainty_uses_tolmachev_log_error_model():
    graph = _compiled_graph()
    by_label = _knowledge_by_label(graph)

    table_id = by_label["ueg_mu_ef_table_i"].id
    model_id = by_label["tolmachev_log_mu_star_error_model"].id

    expected = {
        "al_mu_star_input": (0.1289, 0.0179, 0.0013, 0.0166, 2.1735),
        "zn_mu_star_input": (0.1200, 0.0156, 0.0012, 0.0144, 2.9),
        "li_mu_star_input": (0.1749, 0.0375, 0.0069, 0.0306, 5.6875),
    }
    for label, (value, uncertainty, table_component, log_component, effective_rs) in expected.items():
        claim = by_label[label]
        assert _param_value(claim, "value") == value
        assert _param_value(claim, "uncertainty") == uncertainty
        assert _param_value(claim, "table_uncertainty_component") == table_component
        assert _param_value(claim, "tolmachev_log_uncertainty_component") == log_component
        assert _param_value(claim, "tolmachev_log_uncertainty") == 1.0
        assert _param_value(claim, "uncertainty_model") == "tolmachev_log_plus_table_propagation"
        assert _param_value(claim, "effective_rs") == effective_rs
        assert _param_value(claim, "source_table") == "arXiv:2512.19382v2 TeX Tables I/II"

        strategies = [s for s in graph.strategies if s.conclusion == claim.id]
        assert strategies, f"missing mu* derivation strategy for {label}"
        assert table_id in strategies[0].premises
        assert model_id in strategies[0].premises


def test_lambda_uncertainty_is_model_based_not_table_derived():
    graph = _compiled_graph()
    by_label = _knowledge_by_label(graph)

    model_id = by_label["shared_dfpt_lambda_error_model"].id
    expected = {
        "al_lambda_input": (0.44, 0.044),
        "zn_lambda_input": (0.502, 0.0502),
        "li_lambda_input": (0.34, 0.034),
    }
    for label, (value, uncertainty) in expected.items():
        claim = by_label[label]
        assert _param_value(claim, "value") == value
        assert _param_value(claim, "uncertainty") == uncertainty
        assert _param_value(claim, "uncertainty_model") == "shared_dfpt_fractional_systematic"

        strategies = [s for s in graph.strategies if s.conclusion == claim.id]
        assert strategies, f"missing lambda derivation strategy for {label}"
        assert model_id in strategies[0].premises


def test_experiment_likelihoods_are_calculated_from_log_tc_agreement():
    graph = _compiled_graph()

    by_label = _knowledge_by_label(graph)
    for label in ("tc_al_phenomenological", "tc_zn_phenomenological", "tc_li_phenomenological"):
        content = by_label[label].content
        assert "uniform" in content.lower()
        assert "0.1--0.2" in content
        assert "standard value $\\mu^* = 0.1$" not in content

    expected = {
        "infer_tc_al_ab_initio_agreement": [0.0817, 0.9183],
        "infer_tc_al_phenomenological_test": [0.7136, 0.2864],
        "infer_tc_zn_ab_initio_agreement": [0.05, 0.95],
        "infer_tc_zn_phenomenological_test": [0.6476, 0.3524],
        "infer_tc_li_ab_initio_agreement": [0.173, 0.827],
        "infer_tc_li_phenomenological_test": [0.8434, 0.1566],
    }
    for action_label, probabilities in expected.items():
        strategy = _strategy_by_action_label(graph, action_label)
        assert strategy.conditional_probabilities == probabilities
        assert "log-Tc agreement likelihood" in strategy.steps[0].reasoning
