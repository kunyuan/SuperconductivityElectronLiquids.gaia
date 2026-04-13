"""Leaf claim priors — package input interface.

Each entry maps a leaf claim (not derived by any strategy) to its
prior probability and a one-line justification. These are injected
into claim metadata by ``gaia compile`` and read by the lowering
layer during inference.
"""

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
from .s3_downfolding import (
    cross_term_suppressed,
    downfolding_validity_limits,
)
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
    simple_metals_weak_lattice,
    ueg_pseudopotential_parameterization,
)

PRIORS: dict = {
    # Fundamental physics
    adiabatic_approx: (0.95, "omega_D/E_F ~ 0.005 for simple metals; Migdal theorem validated."),
    bts_renormalization: (0.95, "Standard RG result (1958), widely verified."),
    ward_identity: (0.98, "Exact QFT identity from charge conservation."),
    cross_term_suppressed: (0.90, "omega_c^2/omega_p^2 <= 0.01; conservative plasmon-pole estimate."),

    # Computational methods
    vdiagmc_method: (0.90, "Rigorous Feynman diagram expansion; validated at r_s <= 5."),
    homotopic_expansion: (0.88, "Log-divergence cure rigorous; conformal-map relies on analyticity."),
    gamma3_vdiagmc: (0.88, "Systematic uncertainty from truncation; method validated elsewhere."),
    quasiparticle_mass_near_unity: (0.92, "High-precision QMC/DiagMC: m*/m < 1% deviation for r_s <= 5."),
    ueg_pseudopotential_parameterization: (0.85, "Mapping procedure reasonable; band-mass correction adds uncertainty."),

    # RPA prediction
    rpa_predicts_attractive_mu: (0.50, "RPA calc correct; physical content uncertain at r_s > 1."),

    # Experimental Tc
    tc_al_experimental: (0.99, "Well-established measurement."),
    tc_zn_experimental: (0.99, "Well-established measurement."),
    tc_li_experimental: (0.85, "Crystal structure controversial at ultra-low T."),

    # Phenomenological Tc — priors reflect explanatory power (how well they match
    # experiment), not calculation correctness.
    tc_al_phenomenological: (0.35, "Predicts 1.9K vs experiment 1.2K (58% overestimate); poor match."),
    tc_zn_phenomenological: (0.35, "Predicts 1.37K vs experiment 0.875K (57% overestimate); poor match."),
    tc_li_phenomenological: (0.10, "Predicts 0.35K vs experiment 4e-4K (3 orders too high); very poor match."),

    # Background / orphaned claims
    ueg_vertex_challenge: (0.95, "Recognized challenge."),
    me_downfolding_is_phenomenological: (0.95, "Well-known limitation."),
    mu_star_phenomenological: (0.95, "Established practice."),
    phenomenological_me_theory: (0.95, "Accurate description."),
    simple_metals_weak_lattice: (0.90, "Well-supported."),
    dfpt_computes_lambda: (0.92, "Established methodology."),
    electron_phonon_action: (0.95, "Standard EFT decomposition."),
    downfolding_validity_limits: (0.92, "Well-characterized."),
    precursory_cooper_flow: (0.90, "Verified in prior work."),
    dfpt_eph_ansatz: (0.90, "Standard DFPT expression."),
}
