"""Section VI — Conventional Superconductors.

Assembles the ab initio workflow for predicting Tc of simple metals, presents
the first-principles predictions for Al, Zn, Li, Na, and Mg, and confronts
them with experiment via three structured Bayesian likelihood comparisons
that replace the legacy ``compare`` / ``abduction`` triples.
"""

from __future__ import annotations

import math

import gaia.engine.bayes as bayes
from gaia.engine.lang import Constant, Real, claim, derive, equals, note, observe

from .motivation import (
    dfpt_computes_lambda,
    mu_star_phenomenological,
    phenomenological_me_theory,
    tc_al_experimental,
    tc_li_experimental,
    tc_zn_experimental,
)
from .probabilities import (
    MATERIAL_PARAMS,
    eft_log_tc_mean,
    eft_log_tc_sigma,
    log_tc_al,
    log_tc_li,
    log_tc_zn,
    mcmillan_log_tc_moments,
    mcmillan_tc,
)
from .s2_model import precursory_cooper_flow
from .s3_downfolding import downfolded_bse
from .s4_pseudopotential import mu_vdiagmc_values
from .s5_eph_coupling import dfpt_reliable_for_simple_metals

# ---------------------------------------------------------------------------
# Material parameter notes (formerly setting(); pure context, non-probabilistic)
# ---------------------------------------------------------------------------

aluminum_parameters = note(
    "Aluminum (Al): FCC crystal structure, $r_s = 2.07$, band mass "
    "$m_b = 1.05$, DFPT electron-phonon coupling $\\lambda = 0.44$, "
    "logarithmic phonon frequency $\\omega_{\\mathrm{log}} = 320$ K, "
    "Fermi temperature $T_F = 1.3 \\times 10^5$ K.",
    title="Aluminum Material Parameters",
)

lithium_parameters = note(
    "Lithium (Li): 9R crystal structure at low $T$ (also studied in "
    "HCP). 9R parameters: $r_s = 3.25$, $m_b = 1.75$, $\\lambda = 0.34$, "
    "$\\omega_{\\mathrm{log}} = 242$ K, $T_F = 4.0 \\times 10^4$ K. "
    "HCP parameters: $r_s = 3.19$, $m_b = 1.4$, $\\lambda = 0.37$, "
    "$\\omega_{\\mathrm{log}} = 243$ K, $T_F = 4.1 \\times 10^4$ K. "
    "Crystal structure at sub-kelvin temperatures remains debated.",
    title="Lithium Material Parameters",
)

sodium_parameters = note(
    "Sodium (Na): BCC crystal structure, $r_s = 3.96$, band mass "
    "$m_b = 1.0$, DFPT electron-phonon coupling $\\lambda = 0.2$, "
    "logarithmic phonon frequency $\\omega_{\\mathrm{log}} = 127$ K, "
    "Fermi temperature $T_F = 4.2 \\times 10^4$ K. No superconductivity "
    "observed down to mK temperatures.",
    title="Sodium Material Parameters",
)

magnesium_parameters = note(
    "Magnesium (Mg): HCP crystal structure, $r_s = 2.66$, band mass "
    "$m_b = 1.02$, DFPT electron-phonon coupling $\\lambda = 0.24$, "
    "logarithmic phonon frequency $\\omega_{\\mathrm{log}} = 269$ K, "
    "Fermi temperature $T_F = 8.0 \\times 10^4$ K. No superconductivity "
    "observed down to mK temperatures.",
    title="Magnesium Material Parameters",
)

zinc_parameters = note(
    "Zinc (Zn): HCP crystal structure, $r_s = 2.90$, band mass "
    "$m_b = 1.0$, DFPT electron-phonon coupling $\\lambda = 0.502$, "
    "logarithmic phonon frequency $\\omega_{\\mathrm{log}} = 111$ K, "
    "Fermi temperature $T_F = 1.21 \\times 10^5$ K.",
    title="Zinc Material Parameters",
)

# ---------------------------------------------------------------------------
# Leaf claims
# ---------------------------------------------------------------------------

simple_metals_weak_lattice = claim(
    "Simple metals (Al, Li, Na, Mg, Zn) have weak lattice effects in the "
    "Coulomb pseudopotential: the difference between the crystalline "
    "$\\mu^*$ and the UEG $\\mu^*$ at the same $r_s$ is small (a few "
    "percent) because the nearly-free-electron character of these metals "
    "means the Fermi surface is approximately spherical and the electronic "
    "structure is well described by the homogeneous electron gas with "
    "minor crystal-field perturbations.",
    title="Simple Metals Have Weak Lattice Effects",
    prior=0.90,
)

ueg_pseudopotential_parameterization = claim(
    "The UEG Coulomb pseudopotential $\\mu_{E_F}(r_s)$ computed by vDiagMC "
    "can be parameterized as a smooth function of $r_s$ and mapped onto "
    "real materials by using the material's effective $r_s$ (determined "
    "from the valence electron density). Combined with the BTS relation "
    "to run $\\mu_{E_F}$ down to the Debye scale, this provides "
    "$\\mu^*(r_s)$ for any simple metal without additional adjustable "
    "parameters.",
    title="UEG mu* Parameterization and Mapping",
    prior=0.85,
)

# ---------------------------------------------------------------------------
# Intermediate derived claims
# ---------------------------------------------------------------------------

mu_available_for_simple_metals = claim(
    "For simple metals, the Coulomb pseudopotential $\\mu^*$ can be obtained "
    "from first principles without adjustable parameters: the vDiagMC-computed "
    "$\\mu_{E_F}(r_s)$ for the uniform electron gas is mapped to real materials "
    "via material-specific $r_s$ and band mass, then scaled to the Debye "
    "frequency via the BTS renormalization relation.",
    title="mu* Available for Simple Metals",
    prior=0.88,
)

derive(
    mu_available_for_simple_metals,
    given=(ueg_pseudopotential_parameterization, mu_vdiagmc_values),
    background=[simple_metals_weak_lattice],
    rationale=(
        "The vDiagMC results provide $\\mu_{E_F}(r_s)$ for the UEG "
        "(@mu_vdiagmc_values). The parameterization procedure "
        "(@ueg_pseudopotential_parameterization) maps these to real materials "
        "using material-specific $r_s$ and band mass, justified by the weak "
        "lattice effects in simple metals (@simple_metals_weak_lattice). "
        "The BTS relation scales $\\mu_{E_F}$ down to $\\mu^*$ at the Debye "
        "frequency."
    ),
)

ab_initio_workflow = claim(
    "The complete ab initio workflow for predicting $T_c$ of simple metals: "
    "(1) compute $\\mu_{E_F}$ from the UEG four-point vertex via vDiagMC, "
    "(2) map to the material's $r_s$ and run down to $\\mu^*$ via the BTS "
    "relation, (3) obtain $\\lambda$ from DFPT, (4) solve the downfolded "
    "Eliashberg equations (or use the PCF extrapolation) to predict $T_c$. "
    "All inputs are from first principles; no adjustable parameters remain.",
    title="Ab Initio Tc Prediction Workflow",
    metadata={
        "figure": "artifacts/images/13_0.jpg",
        "caption": (
            "Fig. 9 | Proposed ab initio framework for electron-phonon SC "
            "beyond the weak correlation limit, showing computational pathway "
            "from fundamental parameters through correlated electrons and "
            "lattice vibrations to superconducting properties."
        ),
    },
)

derive(
    ab_initio_workflow,
    given=(downfolded_bse, mu_available_for_simple_metals, dfpt_reliable_for_simple_metals),
    rationale=(
        "The downfolded BSE (@downfolded_bse) provides the theoretical "
        "equation requiring two microscopic inputs: $\\mu^*$ and $\\lambda$. "
        "Both are now available from first principles — $\\mu^*$ from the "
        "UEG parameterization (@mu_available_for_simple_metals) and $\\lambda$ "
        "from validated DFPT (@dfpt_reliable_for_simple_metals). With all "
        "components determined from first principles, the workflow is "
        "complete and parameter-free."
    ),
)

# ---------------------------------------------------------------------------
# Qualitative predictions (Al pressure, Na/Mg QPT)
# ---------------------------------------------------------------------------

al_pressure_transition = claim(
    "Under hydrostatic pressure, the ab initio framework predicts that "
    "aluminum's superconducting $T_c$ monotonically decreases, consistent "
    "with experimental data up to 6 GPa. The framework predicts that "
    "superconductivity in Al vanishes at approximately 60 GPa; at 20 GPa, "
    "$T_c$ is already suppressed below 1 mK.",
    title="Al Pressure-Tc Transition",
    prior=0.80,
    metadata={
        "figure": "artifacts/images/14_0.jpg",
        "caption": (
            "Fig. 10 | Pressure dependence of the superconducting critical "
            "temperature in aluminum. EFT results (squares) compared with "
            "experimental data from Levy et al. and Gubser et al."
        ),
    },
)

derive(
    al_pressure_transition,
    given=(ab_initio_workflow,),
    background=[aluminum_parameters],
    rationale=(
        "Applying the ab initio workflow (@ab_initio_workflow) to aluminum "
        "under varying hydrostatic pressure (@aluminum_parameters): as "
        "pressure increases, $r_s$ decreases (higher electron density), "
        "modifying both $\\mu^*$ and $\\lambda$. The net effect is a "
        "monotonic decrease in $T_c$, accurately capturing the "
        "experimental trend from ambient to 6 GPa. Extrapolating beyond "
        "experimental data, the framework predicts SC vanishes at ~60 GPa, "
        "with $T_c < 1$ mK already at 20 GPa."
    ),
)

tc_mg_na_near_qpt = claim(
    "The ab initio framework predicts that sodium and magnesium have "
    "extremely low or vanishing $T_c$: for Na ($r_s = 3.96$, "
    "$\\lambda = 0.2$, $\\mu^* = 0.15$), the Coulomb repulsion nearly "
    "cancels the weak electron-phonon coupling, giving "
    "$T_c^{\\mathrm{EFT}} = 2 \\times 10^{-13}$ K (effectively no "
    "superconductivity). For Mg ($r_s = 2.66$, $\\lambda = 0.24$, "
    "$\\mu^* = 0.14$), $T_c^{\\mathrm{EFT}} = 5 \\times 10^{-5}$ K. "
    "Both materials are near the quantum phase transition between "
    "superconducting and non-superconducting ground states, where "
    "$T_c$ varies exponentially with small parameter changes.",
    title="Na and Mg Near Quantum Phase Transition",
    prior=0.80,
    metadata={
        "figure": "artifacts/images/15_0.jpg",
        "caption": (
            "Fig. 11 | Effective BCS coupling strength for simple metals. Na "
            "and Mg appear near the origin, indicating near-cancellation of "
            "pairing interaction."
        ),
    },
)

derive(
    tc_mg_na_near_qpt,
    given=(ab_initio_workflow,),
    background=[magnesium_parameters, sodium_parameters, precursory_cooper_flow],
    rationale=(
        "Applying the ab initio workflow (@ab_initio_workflow) to sodium "
        "(@sodium_parameters) and magnesium (@magnesium_parameters): Na has "
        "$r_s = 3.96$, yielding $\\mu^* = 0.15$ which nearly cancels its "
        "weak $\\lambda = 0.2$, giving $T_c^{\\mathrm{EFT}} = "
        "2 \\times 10^{-13}$ K (effectively no superconductivity). "
        "Mg has $r_s = 2.66$, yielding $\\mu^* = 0.14$ which nearly "
        "cancels $\\lambda = 0.24$, giving $T_c^{\\mathrm{EFT}} = "
        "5 \\times 10^{-5}$ K. The precursory Cooper flow formalism "
        "(@precursory_cooper_flow) shows that near the quantum phase "
        "transition ($g \\to 0$), $T_c = \\omega_\\Lambda e^{1/g}$ is "
        "exponentially sensitive to the coupling, explaining why small "
        "parameter variations can toggle between superconducting and "
        "non-superconducting ground states."
    ),
)

# ===========================================================================
# Quantitative Tc comparisons (Al, Zn, Li): structured Bayesian likelihood
# ===========================================================================
#
# For each material, the legacy ``compare(eft_pred, phenom_pred, exp)`` plus
# ``abduction(s_eft, s_phenom, comparison)`` triple is replaced by:
#   - ``derive`` of the EFT prediction claim from the ab initio workflow
#   - ``derive`` of the McMillan prediction claim from the phenomenological theory
#   - ``observe`` of the experimental ``log T_c``
#   - ``bayes.model`` for the EFT prediction: Normal(eft_log_tc_mean, σ_EFT)
#   - ``bayes.model`` for the McMillan prediction: Normal(mcmillan_mean, mcmillan_σ)
#     where σ is the propagated ``μ* ~ Uniform[0.1, 0.2]`` uncertainty
#   - ``bayes.likelihood`` comparing the two models against the observation


# --- Aluminum -----------------------------------------------------------

tc_al_predicted = derive(
    f"The ab initio EFT framework predicts $T_c^{{\\mathrm{{EFT}}}} = "
    f"{mcmillan_tc(MATERIAL_PARAMS['al']['lam'], MATERIAL_PARAMS['al']['mu_eft'], MATERIAL_PARAMS['al']['omega_log']):.2f}$ K "
    f"for aluminum using $\\lambda = {MATERIAL_PARAMS['al']['lam']}$, "
    f"$\\mu^* = {MATERIAL_PARAMS['al']['mu_eft']}$ from vDiagMC + BTS, "
    f"and $\\omega_{{\\mathrm{{log}}}} = {MATERIAL_PARAMS['al']['omega_log']:.0f}$ K. "
    f"The experimental value is $T_c^{{\\mathrm{{exp}}}} = "
    f"{MATERIAL_PARAMS['al']['tc_exp']}$ K.",
    given=(ab_initio_workflow,),
    background=[aluminum_parameters],
    rationale="Plug Al's first-principles inputs into the McMillan estimator.",
    label="tc_al_predicted",
)

tc_al_phenomenological = derive(
    f"The phenomenological McMillan formula with the standard guess "
    f"$\\mu^* = 0.1$ predicts $T_c \\approx "
    f"{mcmillan_tc(MATERIAL_PARAMS['al']['lam'], 0.10, MATERIAL_PARAMS['al']['omega_log']):.2f}$ K "
    f"for aluminum, overestimating the experimental "
    f"{MATERIAL_PARAMS['al']['tc_exp']} K by ~85%.",
    given=(phenomenological_me_theory, mu_star_phenomenological, dfpt_computes_lambda),
    background=[aluminum_parameters],
    rationale="McMillan with fixed empirical μ* = 0.1 applied to Al's λ, ω_log.",
    label="tc_al_phenomenological",
)

_tc_al_observation_binding = claim(
    f"Experimental log Tc(Al) = log({MATERIAL_PARAMS['al']['tc_exp']}) "
    f"= {math.log(MATERIAL_PARAMS['al']['tc_exp']):.4f}.",
    formula=equals(log_tc_al, Constant(math.log(MATERIAL_PARAMS["al"]["tc_exp"]), Real)),
)
_tc_al_observation_binding.label = "tc_al_observation_binding"

tc_al_observation = observe(
    _tc_al_observation_binding,
    background=[aluminum_parameters, tc_al_experimental],
    rationale=(
        "Well-established measurement: T_c(Al) = 1.2 K (@tc_al_experimental). "
        "Pin via log Tc binding so the Bayesian log-Tc likelihood comparison "
        "sees the data point."
    ),
    label="tc_al_observation",
)

eft_al_model = bayes.model(
    ab_initio_workflow,
    observable=log_tc_al,
    distribution=bayes.Normal(mu=eft_log_tc_mean("al"), sigma=eft_log_tc_sigma("al")),
    background=[aluminum_parameters],
    rationale=(
        "EFT prediction: μ* = 0.13 (vDiagMC + BTS) → Tc ≈ 1.14 K via McMillan. "
        "Per-material σ propagated from μ*_EFT ±5% relative precision."
    ),
    label="eft_al_model",
)

_mcmillan_al_mean, _mcmillan_al_sigma = mcmillan_log_tc_moments(MATERIAL_PARAMS["al"])
mcmillan_al_model = bayes.model(
    phenomenological_me_theory,
    observable=log_tc_al,
    distribution=bayes.Normal(mu=_mcmillan_al_mean, sigma=_mcmillan_al_sigma),
    background=[aluminum_parameters, mu_star_phenomenological],
    rationale=(
        "Traditional McMillan: μ* ~ Uniform[0.1, 0.2] propagated through the "
        "formula gives a log-Tc Gaussian with much wider σ than the EFT model."
    ),
    label="mcmillan_al_model",
)

tc_al_likelihood = bayes.likelihood(
    tc_al_observation,
    model=eft_al_model,
    against=[mcmillan_al_model],
    background=[aluminum_parameters],
    rationale=(
        "Likelihood of the observed log Tc(Al) = ln(1.2) under the EFT "
        "Normal model versus the propagated-McMillan Normal model. The EFT "
        "predictive Gaussian is both centred closer to the observation and "
        "much narrower, yielding a clear Bayes factor in favour of EFT."
    ),
    exclusivity="none",
    label="tc_al_likelihood",
)

# --- Zinc ---------------------------------------------------------------

tc_zn_predicted = derive(
    f"The ab initio EFT framework predicts $T_c^{{\\mathrm{{EFT}}}} = "
    f"{mcmillan_tc(MATERIAL_PARAMS['zn']['lam'], MATERIAL_PARAMS['zn']['mu_eft'], MATERIAL_PARAMS['zn']['omega_log']):.3f}$ K "
    f"for zinc using $\\lambda = {MATERIAL_PARAMS['zn']['lam']}$, "
    f"$\\mu^* = {MATERIAL_PARAMS['zn']['mu_eft']}$, and "
    f"$\\omega_{{\\mathrm{{log}}}} = {MATERIAL_PARAMS['zn']['omega_log']:.0f}$ K. "
    f"The experimental value is $T_c^{{\\mathrm{{exp}}}} = "
    f"{MATERIAL_PARAMS['zn']['tc_exp']}$ K.",
    given=(ab_initio_workflow,),
    background=[zinc_parameters],
    rationale="Plug Zn's first-principles inputs into the McMillan estimator.",
    label="tc_zn_predicted",
)

tc_zn_phenomenological = derive(
    f"The phenomenological McMillan formula with the standard guess "
    f"$\\mu^* = 0.1$ predicts $T_c \\approx "
    f"{mcmillan_tc(MATERIAL_PARAMS['zn']['lam'], 0.10, MATERIAL_PARAMS['zn']['omega_log']):.2f}$ K "
    f"for zinc, overestimating the experimental "
    f"{MATERIAL_PARAMS['zn']['tc_exp']} K by ~57%.",
    given=(phenomenological_me_theory, mu_star_phenomenological, dfpt_computes_lambda),
    background=[zinc_parameters],
    rationale="McMillan with fixed empirical μ* = 0.1 applied to Zn's λ, ω_log.",
    label="tc_zn_phenomenological",
)

_tc_zn_observation_binding = claim(
    f"Experimental log Tc(Zn) = log({MATERIAL_PARAMS['zn']['tc_exp']}) "
    f"= {math.log(MATERIAL_PARAMS['zn']['tc_exp']):.4f}.",
    formula=equals(log_tc_zn, Constant(math.log(MATERIAL_PARAMS["zn"]["tc_exp"]), Real)),
)
_tc_zn_observation_binding.label = "tc_zn_observation_binding"

tc_zn_observation = observe(
    _tc_zn_observation_binding,
    background=[zinc_parameters, tc_zn_experimental],
    rationale=(
        "Well-established measurement: T_c(Zn) = 0.875 K "
        "(@tc_zn_experimental); pinned via log Tc binding."
    ),
    label="tc_zn_observation",
)

eft_zn_model = bayes.model(
    ab_initio_workflow,
    observable=log_tc_zn,
    distribution=bayes.Normal(mu=eft_log_tc_mean("zn"), sigma=eft_log_tc_sigma("zn")),
    background=[zinc_parameters],
    rationale="EFT prediction: μ* = 0.12 (vDiagMC + BTS) → Tc ≈ 0.99 K.",
    label="eft_zn_model",
)

_mcmillan_zn_mean, _mcmillan_zn_sigma = mcmillan_log_tc_moments(MATERIAL_PARAMS["zn"])
mcmillan_zn_model = bayes.model(
    phenomenological_me_theory,
    observable=log_tc_zn,
    distribution=bayes.Normal(mu=_mcmillan_zn_mean, sigma=_mcmillan_zn_sigma),
    background=[zinc_parameters, mu_star_phenomenological],
    rationale="Traditional McMillan: μ* ~ Uniform[0.1, 0.2] propagated for Zn.",
    label="mcmillan_zn_model",
)

tc_zn_likelihood = bayes.likelihood(
    tc_zn_observation,
    model=eft_zn_model,
    against=[mcmillan_zn_model],
    background=[zinc_parameters],
    rationale=(
        "Likelihood of log Tc(Zn) under EFT vs propagated-McMillan. EFT "
        "centres almost on the observation with a tight Gaussian; McMillan "
        "is offset and broad."
    ),
    exclusivity="none",
    label="tc_zn_likelihood",
)

# --- Lithium ------------------------------------------------------------

tc_li_predicted = derive(
    f"The ab initio EFT framework predicts $T_c^{{\\mathrm{{EFT}}}} \\approx "
    f"{mcmillan_tc(MATERIAL_PARAMS['li']['lam'], MATERIAL_PARAMS['li']['mu_eft'], MATERIAL_PARAMS['li']['omega_log']):.1e}$ K "
    f"for lithium (9R) using $\\lambda = {MATERIAL_PARAMS['li']['lam']}$, "
    f"$\\mu^* = {MATERIAL_PARAMS['li']['mu_eft']}$, and "
    f"$\\omega_{{\\mathrm{{log}}}} = {MATERIAL_PARAMS['li']['omega_log']:.0f}$ K. "
    f"The large $\\mu^*$ from $r_s = 3.25$ nearly cancels the moderate "
    f"$\\lambda$, pushing $T_c$ into the sub-mK regime. Experimental: "
    f"$T_c \\approx {MATERIAL_PARAMS['li']['tc_exp']:.0e}$ K.",
    given=(ab_initio_workflow,),
    background=[lithium_parameters],
    rationale=(
        "Plug Li's first-principles inputs into the McMillan estimator; "
        "near-cancellation of g amplifies parameter sensitivity exponentially."
    ),
    label="tc_li_predicted",
)

tc_li_phenomenological = derive(
    f"The phenomenological McMillan formula with $\\mu^* = 0.1$ predicts "
    f"$T_c \\approx "
    f"{mcmillan_tc(MATERIAL_PARAMS['li']['lam'], 0.10, MATERIAL_PARAMS['li']['omega_log']):.2f}$ K "
    f"for lithium, overestimating the experimental "
    f"{MATERIAL_PARAMS['li']['tc_exp']:.0e} K by three orders of magnitude.",
    given=(phenomenological_me_theory, mu_star_phenomenological, dfpt_computes_lambda),
    background=[lithium_parameters],
    rationale="McMillan with fixed empirical μ* = 0.1 applied to Li's λ, ω_log.",
    label="tc_li_phenomenological",
)

_tc_li_observation_binding = claim(
    f"Experimental log Tc(Li) = log({MATERIAL_PARAMS['li']['tc_exp']:.0e}) "
    f"= {math.log(MATERIAL_PARAMS['li']['tc_exp']):.4f}.",
    formula=equals(log_tc_li, Constant(math.log(MATERIAL_PARAMS["li"]["tc_exp"]), Real)),
)
_tc_li_observation_binding.label = "tc_li_observation_binding"

tc_li_observation = observe(
    _tc_li_observation_binding,
    background=[lithium_parameters, tc_li_experimental],
    rationale=(
        "Experimental T_c(Li) ≈ 4×10⁻⁴ K (@tc_li_experimental, 9R structure). "
        "The crystal structure at sub-kelvin temperatures is still debated, "
        "contributing some structural uncertainty to the comparison."
    ),
    label="tc_li_observation",
)

eft_li_model = bayes.model(
    ab_initio_workflow,
    observable=log_tc_li,
    distribution=bayes.Normal(mu=eft_log_tc_mean("li"), sigma=eft_log_tc_sigma("li")),
    background=[lithium_parameters],
    rationale=(
        "EFT prediction: μ* = 0.18 (vDiagMC + BTS) → Tc ≈ 2e-3 K. Note: σ "
        "for Li is large because the exponential sensitivity to g near the "
        "QPT magnifies any μ*_EFT uncertainty."
    ),
    label="eft_li_model",
)

_mcmillan_li_mean, _mcmillan_li_sigma = mcmillan_log_tc_moments(MATERIAL_PARAMS["li"])
mcmillan_li_model = bayes.model(
    phenomenological_me_theory,
    observable=log_tc_li,
    distribution=bayes.Normal(mu=_mcmillan_li_mean, sigma=_mcmillan_li_sigma),
    background=[lithium_parameters, mu_star_phenomenological],
    rationale=(
        "Traditional McMillan: μ* ~ Uniform[0.1, 0.2] propagated for Li; "
        "near-QPT exponential sensitivity gives a very broad log-Tc spread."
    ),
    label="mcmillan_li_model",
)

tc_li_likelihood = bayes.likelihood(
    tc_li_observation,
    model=eft_li_model,
    against=[mcmillan_li_model],
    background=[lithium_parameters],
    rationale=(
        "Likelihood of log Tc(Li) under EFT vs propagated-McMillan. Li is "
        "the hard case: both predictive distributions are off by 1.3-1.7 σ, "
        "with EFT narrowly preferred — illustrating the limits of any "
        "method in the near-cancellation regime."
    ),
    exclusivity="none",
    label="tc_li_likelihood",
)
