"""Superconductivity in Electron Liquids (arXiv:2512.19382)

Gaia knowledge package formalizing the reasoning structure of
Cai, Wang, Zhang, Zhang, Millis, Svistunov, Prokof'ev & Chen (2025).
"""

# Section I: Introduction
from .motivation import (
    adiabatic_approx,
    bcs_theory,
    bts_renormalization,
    dfpt_computes_lambda,
    main_question,
    me_downfolding_is_phenomenological,
    me_framework,
    mu_star_phenomenological,
    phenomenological_me_theory,
    rpa_predicts_attractive_mu,
    tc_al_experimental,
    tc_al_phenomenological,
    tc_li_experimental,
    tc_li_phenomenological,
    tc_zn_experimental,
    tc_zn_phenomenological,
)

# Section II: The Model and Basic Relations
from .s2_model import (
    bse_kernel_decomposition,
    electron_phonon_action,
    precursory_cooper_flow,
)

# Section III: Downfolding the BSE
from .s3_downfolding import (
    cross_term_suppressed,
    downfolded_bse,
    downfolded_bse_toy_model,
    downfolded_me_equation,
    bts_microscopic_equivalence,
    downfolding_validity_limits,
    full_bse_toy_model,
    lambda_microscopic_definition,
    ma_pseudopotential_justified,
    mu_microscopic_definition,
    mu_scale_independence,
    pair_propagator_decomposition,
    rpa_dynamic_screening,
)

# Section IV: Coulomb Pseudopotential
from .s4_pseudopotential import (
    homotopic_expansion,
    mu_vdiagmc_values,
    rpa_vs_vdiagmc,
    ueg_vertex_challenge,
    vdiagmc_method,
)

# Section V: Electron-Phonon Coupling
from .s5_eph_coupling import (
    dfpt_eph_ansatz,
    dfpt_eph_ansatz,
    dfpt_reliable_for_simple_metals,
    eft_eph_vertex,
    eft_vertex_matches_dfpt,
    gamma3_approximation,
    gamma3_vdiagmc,
    quasiparticle_mass_near_unity,
    ward_identity,
)

# Section VI: Conventional Superconductors
from .s6_superconductors import (
    ab_initio_workflow,
    al_pressure_transition,
    mu_available_for_simple_metals,
    aluminum_parameters,
    lithium_parameters,
    magnesium_parameters,
    simple_metals_weak_lattice,
    sodium_parameters,
    tc_al_predicted,
    tc_li_predicted,
    tc_mg_na_near_qpt,
    tc_zn_predicted,
    ueg_pseudopotential_parameterization,
    zinc_parameters,
)

# Exported conclusions — cross-package interface
__all__ = [
    "ab_initio_workflow",
    "mu_vdiagmc_values",
    "dfpt_reliable_for_simple_metals",
    "tc_al_predicted",
    "tc_zn_predicted",
    "tc_li_predicted",
    "al_pressure_transition",
    "tc_mg_na_near_qpt",
    "downfolded_bse",
]
