"""Self-review: prior and conditional probability assignments."""

from gaia.review import (
    ReviewBundle,
    review_claim,
    review_strategy,
)

from ..motivation import (
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
from ..s2_model import electron_phonon_action, precursory_cooper_flow
from ..s3_downfolding import (
    _strat_downfolded_bse_toy,
    _strat_full_bse,
    cross_term_suppressed,
    downfolding_validity_limits,
)
from ..s4_pseudopotential import (
    _strat_mu_values,
    homotopic_expansion,
    ueg_vertex_challenge,
    vdiagmc_method,
)
from ..s5_eph_coupling import (
    _composite_dfpt,
    _induct_gamma3,
    dfpt_eph_ansatz,
    gamma3_vdiagmc,
    quasiparticle_mass_near_unity,
    ward_identity,
)
from ..s6_superconductors import (
    _composite_workflow,
    _s1 as _strat_mu_available,
    _strat_al_pressure,
    _strat_mg_na_qpt,
    _strat_tc_al,
    _strat_tc_li,
    _strat_tc_zn,
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

# ---------------------------------------------------------------------------
# Priors — independent premises
# ---------------------------------------------------------------------------

_claim_reviews = [
    # Fundamental physics
    review_claim(adiabatic_approx, prior=0.95,
                 justification="omega_D/E_F ~ 0.005 for simple metals; Migdal theorem validated."),
    review_claim(bts_renormalization, prior=0.95,
                 justification="Standard RG result (1958), widely verified."),
    review_claim(ward_identity, prior=0.98,
                 justification="Exact QFT identity from charge conservation."),
    review_claim(cross_term_suppressed, prior=0.90,
                 justification="omega_c^2/omega_p^2 <= 0.01; conservative plasmon-pole estimate."),

    # Computational methods
    review_claim(vdiagmc_method, prior=0.90,
                 justification="Rigorous Feynman diagram expansion; validated at r_s <= 5."),
    review_claim(homotopic_expansion, prior=0.88,
                 justification="Log-divergence cure rigorous; conformal-map relies on analyticity."),
    review_claim(gamma3_vdiagmc, prior=0.88,
                 justification="Systematic uncertainty from truncation; method validated elsewhere."),
    review_claim(quasiparticle_mass_near_unity, prior=0.92,
                 justification="High-precision QMC/DiagMC: m*/m < 1% deviation for r_s <= 5."),
    review_claim(ueg_pseudopotential_parameterization, prior=0.85,
                 justification="Mapping procedure reasonable; band-mass correction adds uncertainty."),

    # RPA prediction
    review_claim(rpa_predicts_attractive_mu, prior=0.50,
                 justification="RPA calc correct; physical content uncertain at r_s > 1."),

    # Experimental Tc
    review_claim(tc_al_experimental, prior=0.99, justification="Well-established measurement."),
    review_claim(tc_zn_experimental, prior=0.99, justification="Well-established measurement."),
    review_claim(tc_li_experimental, prior=0.85,
                 justification="Crystal structure controversial at ultra-low T."),

    # Phenomenological Tc
    review_claim(tc_al_phenomenological, prior=0.90, justification="Correct uniform-mu* range calc."),
    review_claim(tc_li_phenomenological, prior=0.90, justification="Correct uniform-mu* range calc."),
    review_claim(tc_zn_phenomenological, prior=0.90, justification="Correct uniform-mu* range calc."),

    # Background-only / orphaned claims (validator requires prior for all claims)
    review_claim(ueg_vertex_challenge, prior=0.95, justification="Recognized challenge."),
    review_claim(me_downfolding_is_phenomenological, prior=0.95,
                 justification="Well-known limitation."),
    review_claim(mu_star_phenomenological, prior=0.95, justification="Established practice."),
    review_claim(phenomenological_me_theory, prior=0.95, justification="Accurate description."),
    review_claim(simple_metals_weak_lattice, prior=0.90, justification="Well-supported."),
    review_claim(dfpt_computes_lambda, prior=0.92, justification="Established methodology."),
    review_claim(ueg_mu_ef_table_i, prior=0.90,
                 justification="arXiv TeX Table I is the numerical source for mu_EF values and uncertainties."),
    review_claim(shared_dfpt_lambda_error_model, prior=0.78,
                 justification="Lambda uncertainty is a shared DFPT model, not a Table II error bar."),
    review_claim(tolmachev_log_mu_star_error_model, prior=0.80,
                 justification="mu* error includes Tolmachev-log cutoff matching uncertainty."),
    review_claim(al_arxiv_table_row, prior=0.90,
                 justification="Structured transcription from arXiv TeX Table II."),
    review_claim(zn_arxiv_table_row, prior=0.90,
                 justification="Structured transcription from arXiv TeX Table II."),
    review_claim(li_arxiv_table_row, prior=0.82,
                 justification="Li(9R) row is sourced from TeX, but low-temperature structure is debated."),
    review_claim(li_low_temperature_lattice_assumption, prior=0.60,
                 justification="Li sub-kelvin crystal structure is debated."),
    review_claim(li_effective_coupling_error_bounded, prior=0.68,
                 justification="g is small, so propagated lambda/mu* uncertainty matters."),
    review_claim(electron_phonon_action, prior=0.95, justification="Standard EFT decomposition."),
    review_claim(downfolding_validity_limits, prior=0.92, justification="Well-characterized."),
    review_claim(precursory_cooper_flow, prior=0.90, justification="Verified in prior work."),
    review_claim(dfpt_eph_ansatz, prior=0.90, justification="Standard DFPT expression."),
]

# ---------------------------------------------------------------------------
# Strategy conditional probabilities
# ---------------------------------------------------------------------------

_strategy_reviews = [
    review_strategy(_induct_gamma3,
                    conditional_probability=0.85,
                    justification="Ward identity plus vDiagMC support the interpolation."),

    # noisy_and strategies
    review_strategy(_strat_full_bse, conditional_probability=0.95,
                    justification="Well-controlled numerical computation."),
    review_strategy(_strat_downfolded_bse_toy, conditional_probability=0.95,
                    justification="Well-controlled numerical computation."),
    review_strategy(_strat_mu_values, conditional_probability=0.90,
                    justification="Systematic uncertainty from truncation/resummation."),
    review_strategy(_strat_mu_available, conditional_probability=0.88,
                    justification="UEG-to-material mapping adds uncertainty."),
    review_strategy(_strat_tc_al, conditional_probability=0.85,
                    justification="Material-specific application."),
    review_strategy(_strat_tc_zn, conditional_probability=0.85,
                    justification="Material-specific application."),
    review_strategy(_strat_tc_li, conditional_probability=0.80,
                    justification="Li structural uncertainty at low T."),
    review_strategy(_strat_al_pressure, conditional_probability=0.80,
                    justification="Extrapolation to high pressure."),
    review_strategy(_strat_mg_na_qpt, conditional_probability=0.80,
                    justification="Near quantum critical point."),

    # composite top-level CPTs (used in folded mode)
    # dfpt_reliable: 3 premises (2^3=8 entries), order: FFF,TFF,FTF,TTF,FFT,TFT,FTT,TTT
    review_strategy(_composite_dfpt,
                    conditional_probabilities=[
                        0.02, 0.05, 0.05, 0.30,  # ...F (mass not near unity)
                        0.02, 0.10, 0.10, 0.90,  # ...T (mass near unity)
                    ],
                    justification="High only when all three conditions hold."),
    # workflow: 4 premises (2^4=16 entries)
    review_strategy(_composite_workflow,
                    conditional_probabilities=[
                        0.01, 0.02, 0.02, 0.05,  # downfolded_bse=F
                        0.02, 0.03, 0.03, 0.10,  # downfolded_bse=T, ueg_param=F
                        0.01, 0.02, 0.02, 0.05,  # ...
                        0.05, 0.10, 0.15, 0.92,  # all T
                    ],
                    justification="Workflow requires all components; high only when all present."),
]

# ---------------------------------------------------------------------------
# Bundle
# ---------------------------------------------------------------------------

REVIEW = ReviewBundle(
    source_id="self_review",
    objects=_claim_reviews + _strategy_reviews,
)
