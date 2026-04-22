"""Author priors for the v6 electron-liquids sandbox package."""

from .motivation import (
    adiabatic_approx,
    bts_renormalization,
    dfpt_computes_lambda,
    me_downfolding_is_phenomenological,
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
from .s2_model import electron_phonon_action, precursory_cooper_flow
from .s3_downfolding import cross_term_suppressed, downfolding_validity_limits
from .s4_pseudopotential import (
    homotopic_expansion,
    ueg_vertex_challenge,
    vdiagmc_method,
)
from .s5_eph_coupling import (
    dfpt_eph_ansatz,
    gamma3_vdiagmc,
    quasiparticle_mass_near_unity,
    ward_identity,
)
from .s6_superconductors import (
    al_arxiv_table_row,
    li_effective_coupling_error_bounded,
    li_arxiv_table_row,
    li_low_temperature_lattice_assumption,
    simple_metals_weak_lattice,
    shared_dfpt_lambda_error_model,
    tolmachev_log_mu_star_error_model,
    ueg_pseudopotential_parameterization,
    ueg_mu_ef_table_i,
    zn_arxiv_table_row,
)


PRIORS = {
    adiabatic_approx: (0.95, "omega_D/E_F is small for conventional simple metals."),
    bts_renormalization: (0.95, "Standard BTS renormalization relation."),
    ward_identity: (0.98, "Exact identity from charge conservation."),
    cross_term_suppressed: (0.90, "Plasmon-scale estimate suppresses cross-channel terms."),
    vdiagmc_method: (0.90, "Controlled diagrammatic method in the metallic density range."),
    homotopic_expansion: (0.88, "Series reorganization improves convergence with some analyticity assumptions."),
    gamma3_vdiagmc: (0.88, "Finite-order vDiagMC evidence for modest three-point vertex corrections."),
    quasiparticle_mass_near_unity: (0.92, "QMC/DiagMC evidence for weak mass renormalization in simple metals."),
    ueg_pseudopotential_parameterization: (0.85, "UEG-to-material mapping is plausible with residual band-structure uncertainty."),
    rpa_predicts_attractive_mu: (0.50, "RPA calculation is reproducible but physically unreliable at larger r_s."),
    tc_al_experimental: (0.99, "Well-established aluminum transition temperature."),
    tc_zn_experimental: (0.99, "Well-established zinc transition temperature."),
    tc_li_experimental: (0.85, "Lithium transition is affected by low-temperature structure uncertainty."),
    tc_al_phenomenological: (0.90, "McMillan calculation with conventional uniform mu* range is straightforward."),
    tc_li_phenomenological: (0.90, "McMillan calculation with conventional uniform mu* range is straightforward."),
    tc_zn_phenomenological: (0.90, "McMillan calculation with conventional uniform mu* range is straightforward."),
    ueg_vertex_challenge: (0.95, "Recognized difficulty of the UEG four-point vertex."),
    me_downfolding_is_phenomenological: (0.95, "Established limitation of phenomenological ME downfolding."),
    mu_star_phenomenological: (0.95, "Standard treatment of mu* as an adjustable parameter."),
    phenomenological_me_theory: (0.95, "Standard description of McMillan/Allen-Dynes limitations."),
    simple_metals_weak_lattice: (0.90, "Simple metals are close to nearly-free-electron systems."),
    dfpt_computes_lambda: (0.92, "DFPT is established for weakly correlated metals."),
    ueg_mu_ef_table_i: (0.90, "arXiv TeX Table I is the numerical source for mu_EF values and uncertainties."),
    shared_dfpt_lambda_error_model: (
        0.78,
        "Lambda uncertainty is model-based because Table II reports values without error bars.",
    ),
    tolmachev_log_mu_star_error_model: (
        0.80,
        "mu* uncertainty includes a shared Tolmachev-log cutoff-matching systematic.",
    ),
    al_arxiv_table_row: (0.90, "Structured transcription from arXiv TeX Table II."),
    zn_arxiv_table_row: (0.90, "Structured transcription from arXiv TeX Table II."),
    li_arxiv_table_row: (
        0.82,
        "Structured transcription from the Li(9R) row, with residual structural uncertainty.",
    ),
    li_low_temperature_lattice_assumption: (
        0.60,
        "Lithium's sub-kelvin lattice structure is debated, so this assumption is deliberately conservative.",
    ),
    li_effective_coupling_error_bounded: (
        0.68,
        "Li effective coupling is small, so lambda and mu* error propagation is consequential.",
    ),
    electron_phonon_action: (0.95, "Standard effective action decomposition."),
    downfolding_validity_limits: (0.92, "Applicability limits are well characterized by scale separation."),
    precursory_cooper_flow: (0.90, "Normal-state extrapolation has been checked in the source work."),
    dfpt_eph_ansatz: (0.90, "Standard DFPT electron-phonon vertex expression."),
}
