"""Conventional Superconductors

Assembles the ab initio workflow for predicting Tc of simple metals, presents
the first-principles predictions for Al, Zn, Li, Na, and Mg, and confronts
them with experiment via v6 infer likelihoods.
"""

from math import exp, log, sqrt

from .v6_actions import Claim, Setting, composite, deduction, infer, noisy_and
from gaia.lang import Claim as GaiaClaim
from gaia.lang import compute, observe

from .motivation import (
    bts_renormalization,
    tc_al_experimental,
    tc_al_phenomenological,
    tc_li_experimental,
    tc_li_phenomenological,
    tc_zn_experimental,
    tc_zn_phenomenological,
)
from .s2_model import precursory_cooper_flow
from .s3_downfolding import downfolded_bse
from .s4_pseudopotential import mu_vdiagmc_values
from .s5_eph_coupling import (
    dfpt_reliable_for_simple_metals,
)


class LambdaInput(GaiaClaim):
    """The DFPT electron-phonon coupling input for {material} ({structure}) is lambda = {value} ± {uncertainty}."""

    material: str
    structure: str
    value: float
    uncertainty: float
    uncertainty_model: str
    source_table: str


class MuStarInput(GaiaClaim):
    """The Coulomb pseudopotential input for {material} ({structure}) is mu* = {value} ± {uncertainty}."""

    material: str
    structure: str
    value: float
    uncertainty: float
    uncertainty_model: str
    effective_rs: float
    running_log: float
    source_mu_ef: float
    source_mu_ef_uncertainty: float
    table_uncertainty_component: float
    tolmachev_log_uncertainty: float
    tolmachev_log_uncertainty_component: float
    source_table: str


class SimpleMetalTableRow(GaiaClaim):
    """The arXiv TeX Table II row for {material} ({structure}) gives lambda = {lambda_value}, rs = {rs}, mb = {band_mass}, TF = {fermi_temperature_k} K, and omega_log = {omega_log_k} K."""

    material: str
    structure: str
    fermi_temperature_k: float
    omega_log_k: float
    lambda_value: float
    rs: float
    band_mass: float
    source_table: str


class UegMuEfTable(GaiaClaim):
    """The arXiv TeX Table I gives UEG mu_EF(rs) values with systematic uncertainties in parentheses."""


class DfptLambdaErrorModel(GaiaClaim):
    """The shared DFPT lambda error model uses a {fractional_uncertainty} fractional systematic uncertainty for simple metals."""

    fractional_uncertainty: float
    uncertainty_model: str
    source: str


class TolmachevLogMuStarErrorModel(GaiaClaim):
    """The mu* error model treats the Tolmachev logarithm as uncertain by {log_uncertainty} logarithmic unit."""

    log_uncertainty: float
    uncertainty_model: str
    source: str


class EffectiveCoupling(GaiaClaim):
    """The effective pairing strength for {material} is g = {value} ± {uncertainty}."""

    material: str
    value: float
    uncertainty: float
    lower: float
    upper: float


UEG_MU_EF_TABLE = {
    1: (0.28, 0.01),
    2: (0.53, 0.02),
    3: (0.77, 0.05),
    4: (1.0, 0.2),
    5: (1.3, 0.2),
    6: (1.8, 0.8),
}
SOURCE_TABLES = "arXiv:2512.19382v2 TeX Tables I/II"
LIKELIHOOD_FLOOR = 0.05
LIKELIHOOD_CEILING = 0.95
PRECISE_EXPERIMENT_LOG_TC_UNCERTAINTY = 0.05
LI_EXPERIMENT_LOG_TC_UNCERTAINTY = 0.70
PHENOMENOLOGICAL_LOG_TC_UNCERTAINTY = 0.25
PHENOMENOLOGICAL_MU_STAR_MIN = 0.10
PHENOMENOLOGICAL_MU_STAR_MAX = 0.20
PHENOMENOLOGICAL_MU_STAR_SAMPLE_COUNT = 5001


def _interpolate_ueg_mu_ef(effective_rs: float) -> tuple[float, float]:
    lower_rs = max(1, min(6, int(effective_rs)))
    upper_rs = min(6, lower_rs + 1)
    if effective_rs <= 1:
        lower_rs = upper_rs = 1
    elif effective_rs >= 6:
        lower_rs = upper_rs = 6

    lower_value, lower_uncertainty = UEG_MU_EF_TABLE[lower_rs]
    upper_value, upper_uncertainty = UEG_MU_EF_TABLE[upper_rs]
    weight = 0.0 if lower_rs == upper_rs else (effective_rs - lower_rs) / (upper_rs - lower_rs)
    value = lower_value * (1 - weight) + upper_value * weight
    uncertainty = lower_uncertainty * (1 - weight) + upper_uncertainty * weight
    return value, uncertainty


def _lambda_input_from_model(
    row: SimpleMetalTableRow,
    model: DfptLambdaErrorModel,
) -> LambdaInput:
    uncertainty = row.lambda_value * model.fractional_uncertainty
    return LambdaInput(
        material=row.material,
        structure=row.structure,
        value=round(row.lambda_value, 4),
        uncertainty=round(uncertainty, 4),
        uncertainty_model=model.uncertainty_model,
        source_table=row.source_table,
    )


def _mu_star_from_ueg_table(
    row: SimpleMetalTableRow,
    _table: UegMuEfTable,
    model: TolmachevLogMuStarErrorModel,
) -> MuStarInput:
    effective_rs = row.rs * row.band_mass
    mu_ef, mu_ef_uncertainty = _interpolate_ueg_mu_ef(effective_rs)
    running_log = log(row.fermi_temperature_k / row.omega_log_k)
    denominator = 1 + mu_ef * running_log
    mu_star = mu_ef / denominator
    table_component = mu_ef_uncertainty / denominator**2
    tolmachev_component = mu_star**2 * model.log_uncertainty
    mu_star_uncertainty = table_component + tolmachev_component
    return MuStarInput(
        material=row.material,
        structure=row.structure,
        value=round(mu_star, 4),
        uncertainty=round(mu_star_uncertainty, 4),
        uncertainty_model=model.uncertainty_model,
        effective_rs=round(effective_rs, 4),
        running_log=round(running_log, 4),
        source_mu_ef=round(mu_ef, 4),
        source_mu_ef_uncertainty=round(mu_ef_uncertainty, 4),
        table_uncertainty_component=round(table_component, 4),
        tolmachev_log_uncertainty=round(model.log_uncertainty, 4),
        tolmachev_log_uncertainty_component=round(tolmachev_component, 4),
        source_table=SOURCE_TABLES,
    )


def _effective_coupling(lambda_input: LambdaInput, mu_star_input: MuStarInput) -> EffectiveCoupling:
    """Compute g = lambda - mu* (1 + 0.62 lambda)."""
    lam = lambda_input.value
    mu = mu_star_input.value
    value = lam - mu * (1 + 0.62 * lam)
    dgdlam = 1 - 0.62 * mu
    dgdmu = -(1 + 0.62 * lam)
    uncertainty = abs(dgdlam) * lambda_input.uncertainty + abs(dgdmu) * mu_star_input.uncertainty
    rounded_value = round(value, 4)
    rounded_uncertainty = round(uncertainty, 4)
    return EffectiveCoupling(
        material=lambda_input.material,
        value=rounded_value,
        uncertainty=rounded_uncertainty,
        lower=round(rounded_value - rounded_uncertainty, 4),
        upper=round(rounded_value + rounded_uncertainty, 4),
    )


def _log_tc_uncertainty_from_g(effective_coupling: EffectiveCoupling) -> float:
    """Propagate g uncertainty through log(Tc) = log(omega) - 1 / g."""
    return effective_coupling.uncertainty / (effective_coupling.value**2)


def _likelihood_from_compatibility(compatibility: float) -> tuple[float, float]:
    span = LIKELIHOOD_CEILING - LIKELIHOOD_FLOOR
    p_e_given_h = LIKELIHOOD_FLOOR + span * compatibility
    p_e_given_not_h = LIKELIHOOD_FLOOR + span * (1 - compatibility)
    return round(p_e_given_h, 4), round(p_e_given_not_h, 4)


def _log_tc_compatibility(
    *,
    predicted_tc_k: float,
    experimental_tc_k: float,
    total_log_tc_uncertainty: float,
) -> float:
    z_score = abs(log(predicted_tc_k / experimental_tc_k)) / total_log_tc_uncertainty
    return exp(-0.5 * z_score**2)


def _tc_agreement_likelihood(
    *,
    predicted_tc_k: float,
    experimental_tc_k: float,
    theory_log_tc_uncertainty: float,
    experimental_log_tc_uncertainty: float,
) -> tuple[float, float]:
    total_sigma = sqrt(theory_log_tc_uncertainty**2 + experimental_log_tc_uncertainty**2)
    compatibility = _log_tc_compatibility(
        predicted_tc_k=predicted_tc_k,
        experimental_tc_k=experimental_tc_k,
        total_log_tc_uncertainty=total_sigma,
    )
    return _likelihood_from_compatibility(compatibility)


def _mcmillan_scaled_tc(
    *,
    reference_tc_k: float,
    lambda_value: float,
    reference_mu_star: float,
    mu_star: float,
) -> float:
    def exponent(mu: float) -> float:
        denominator = lambda_value - mu * (1 + 0.62 * lambda_value)
        return -1.04 * (1 + lambda_value) / denominator

    return reference_tc_k * exp(exponent(mu_star) - exponent(reference_mu_star))


def _tc_agreement_likelihood_from_uniform_mu_star(
    *,
    reference_tc_k: float,
    lambda_value: float,
    experimental_tc_k: float,
    experimental_log_tc_uncertainty: float,
) -> tuple[float, float]:
    total_sigma = sqrt(PHENOMENOLOGICAL_LOG_TC_UNCERTAINTY**2 + experimental_log_tc_uncertainty**2)
    compatibility = 0.0
    for index in range(PHENOMENOLOGICAL_MU_STAR_SAMPLE_COUNT):
        weight = index / (PHENOMENOLOGICAL_MU_STAR_SAMPLE_COUNT - 1)
        mu_star = PHENOMENOLOGICAL_MU_STAR_MIN + weight * (
            PHENOMENOLOGICAL_MU_STAR_MAX - PHENOMENOLOGICAL_MU_STAR_MIN
        )
        predicted_tc_k = _mcmillan_scaled_tc(
            reference_tc_k=reference_tc_k,
            lambda_value=lambda_value,
            reference_mu_star=PHENOMENOLOGICAL_MU_STAR_MIN,
            mu_star=mu_star,
        )
        compatibility += _log_tc_compatibility(
            predicted_tc_k=predicted_tc_k,
            experimental_tc_k=experimental_tc_k,
            total_log_tc_uncertainty=total_sigma,
        )
    compatibility /= PHENOMENOLOGICAL_MU_STAR_SAMPLE_COUNT
    return _likelihood_from_compatibility(compatibility)


# ---------------------------------------------------------------------------
# Settings — material parameters
# ---------------------------------------------------------------------------

ueg_mu_ef_table_i = UegMuEfTable(title="UEG mu_EF Table I")
ueg_mu_ef_table_i.label = "ueg_mu_ef_table_i"
observe(
    ueg_mu_ef_table_i,
    rationale=(
        "The TeX source of arXiv:2512.19382v2 Table I lists mu_EF(rs) "
        "values and parenthesized systematic uncertainties; these values are "
        "taken from the arXiv PDF/TeX source."
    ),
)

shared_dfpt_lambda_error_model = DfptLambdaErrorModel(
    fractional_uncertainty=0.10,
    uncertainty_model="shared_dfpt_fractional_systematic",
    source=(
        "Model-based uncertainty from the UEG vertex-vs-DFPT benchmark and "
        "DFPT numerical convergence protocol; not a Table II error bar."
    ),
    title="Shared DFPT Lambda Error Model",
)
shared_dfpt_lambda_error_model.label = "shared_dfpt_lambda_error_model"
observe(
    shared_dfpt_lambda_error_model,
    rationale=(
        "The source paper gives Table II lambda values but no lambda error "
        "bars. The package therefore marks lambda uncertainty as a shared "
        "DFPT systematic model rather than a table-derived uncertainty."
    ),
)

tolmachev_log_mu_star_error_model = TolmachevLogMuStarErrorModel(
    log_uncertainty=1.0,
    uncertainty_model="tolmachev_log_plus_table_propagation",
    source=(
        "Model-based uncertainty from the BTS/Tolmachev running relation: "
        "an order-one ambiguity in the cutoff matching contributes "
        "Delta mu* approximately (mu*)^2 Delta log(E_F / omega_c), with "
        "Delta log = 1."
    ),
    title="Tolmachev Log mu* Error Model",
)
tolmachev_log_mu_star_error_model.label = "tolmachev_log_mu_star_error_model"
observe(
    tolmachev_log_mu_star_error_model,
    rationale=(
        "The arXiv table reports mu_EF uncertainties, but the mapped mu* "
        "also inherits uncertainty from the Tolmachev logarithm used to run "
        "from E_F to the phonon scale. The package therefore treats one "
        "logarithmic unit in the cutoff matching as a shared systematic."
    ),
)

al_arxiv_table_row = SimpleMetalTableRow(
    material="Al",
    structure="fcc",
    fermi_temperature_k=130_000.0,
    omega_log_k=320.0,
    lambda_value=0.44,
    rs=2.07,
    band_mass=1.05,
    source_table=SOURCE_TABLES,
    title="Al arXiv Table II Row",
)
al_arxiv_table_row.label = "al_arxiv_table_row"
observe(
    al_arxiv_table_row,
    rationale="Structured transcription from arXiv:2512.19382v2 TeX source Table II.",
)

aluminum_parameters = Setting(
    "Aluminum (Al): FCC crystal structure, $r_s = 2.07$, experimental "
    "Debye temperature $\\Theta_D \\approx 428$ K, DFPT electron-phonon "
    "coupling $\\lambda \\approx 0.44$, logarithmic phonon frequency "
    "$\\omega_{\\mathrm{log}} = 320$ K.",
    title="Aluminum Material Parameters",
)

al_lambda_input = compute(
    LambdaInput,
    fn=_lambda_input_from_model,
    given=(al_arxiv_table_row, shared_dfpt_lambda_error_model),
    label="compute_al_lambda_input",
    rationale=(
        "Use the arXiv TeX Table II Al lambda value and attach the shared "
        "DFPT lambda systematic error model."
    ),
)
al_lambda_input.label = "al_lambda_input"
al_mu_star_input = compute(
    MuStarInput,
    fn=_mu_star_from_ueg_table,
    given=(al_arxiv_table_row, ueg_mu_ef_table_i, tolmachev_log_mu_star_error_model),
    label="compute_al_mu_star_input",
    rationale=(
        "Derive Al mu* from Table I mu_EF(rs), Table II rs/mb/TF/omega_log, "
        "linear interpolation in effective rs, the BTS running relation, "
        "and the Tolmachev-log uncertainty model."
    ),
)
al_mu_star_input.label = "al_mu_star_input"
al_effective_coupling = compute(
    EffectiveCoupling,
    fn=_effective_coupling,
    given=(al_lambda_input, al_mu_star_input),
    label="compute_al_effective_coupling",
    rationale=(
        "Reduce the Al Tc calculation to the effective pairing strength "
        "$g = \\lambda - \\mu^*(1 + 0.62\\lambda)$."
    ),
)
al_effective_coupling.label = "al_effective_coupling"

li_arxiv_table_row = SimpleMetalTableRow(
    material="Li",
    structure="9R",
    fermi_temperature_k=40_000.0,
    omega_log_k=242.0,
    lambda_value=0.34,
    rs=3.25,
    band_mass=1.75,
    source_table=SOURCE_TABLES,
    title="Li 9R arXiv Table II Row",
)
li_arxiv_table_row.label = "li_arxiv_table_row"
observe(
    li_arxiv_table_row,
    rationale=(
        "Structured transcription from arXiv:2512.19382v2 TeX source "
        "Table II for the low-temperature 9R lithium row."
    ),
)

lithium_parameters = Setting(
    "Lithium (Li): the Table II low-temperature 9R row uses "
    "$r_s = 3.25$, band mass $m_b = 1.75$, DFPT/literature "
    "electron-phonon coupling $\\lambda = 0.34$, and "
    "$\\omega_{\\mathrm{log}} = 242$ K. The alternate hcp row gives "
    "$\\lambda = 0.37$ and $T_c = 0.03$ K. Crystal structure at "
    "ultra-low temperatures remains debated.",
    title="Lithium Material Parameters",
)

li_lambda_input = compute(
    LambdaInput,
    fn=_lambda_input_from_model,
    given=(li_arxiv_table_row, shared_dfpt_lambda_error_model),
    label="compute_li_lambda_input",
    rationale=(
        "Use the arXiv TeX Table II Li(9R) lambda value and attach the "
        "shared DFPT lambda systematic error model."
    ),
)
li_lambda_input.label = "li_lambda_input"
li_mu_star_input = compute(
    MuStarInput,
    fn=_mu_star_from_ueg_table,
    given=(li_arxiv_table_row, ueg_mu_ef_table_i, tolmachev_log_mu_star_error_model),
    label="compute_li_mu_star_input",
    rationale=(
        "Derive Li(9R) mu* from Table I mu_EF(rs), Table II rs/mb/TF/omega_log, "
        "linear interpolation in effective rs, the BTS running relation, "
        "and the Tolmachev-log uncertainty model."
    ),
)
li_mu_star_input.label = "li_mu_star_input"
li_effective_coupling = compute(
    EffectiveCoupling,
    fn=_effective_coupling,
    given=(li_lambda_input, li_mu_star_input),
    label="compute_li_effective_coupling",
    rationale=(
        "Reduce the Li Tc calculation to the effective pairing strength "
        "$g = \\lambda - \\mu^*(1 + 0.62\\lambda)$."
    ),
)
li_effective_coupling.label = "li_effective_coupling"

li_low_temperature_lattice_assumption = Claim(
    "The low-temperature lithium $T_c$ calculation assumes that the BCC/9R "
    "structural description and associated phonon spectrum used for the "
    "DFPT input remain adequate in the sub-kelvin regime. This assumption "
    "is uncertain because lithium's crystal structure at ultra-low "
    "temperature is experimentally debated.",
    title="Li Low-Temperature Lattice Assumption",
)

sodium_parameters = Setting(
    "Sodium (Na): BCC crystal structure, $r_s = 3.93$, experimental "
    "Debye temperature $\\Theta_D \\approx 158$ K, DFPT electron-phonon "
    "coupling $\\lambda \\approx 0.18$, logarithmic phonon frequency "
    "$\\omega_{\\mathrm{log}} \\approx 120$ K. No superconductivity "
    "observed down to mK temperatures.",
    title="Sodium Material Parameters",
)

magnesium_parameters = Setting(
    "Magnesium (Mg): HCP crystal structure, $r_s = 2.66$, experimental "
    "Debye temperature $\\Theta_D \\approx 400$ K, DFPT electron-phonon "
    "coupling $\\lambda \\approx 0.26$, logarithmic phonon frequency "
    "$\\omega_{\\mathrm{log}} \\approx 290$ K. No superconductivity "
    "observed down to mK temperatures.",
    title="Magnesium Material Parameters",
)

zinc_parameters = Setting(
    "Zinc (Zn): HCP crystal structure, $r_s = 2.90$, experimental "
    "Debye temperature $\\Theta_D \\approx 327$ K, DFPT electron-phonon "
    "coupling $\\lambda = 0.502$, logarithmic phonon frequency "
    "$\\omega_{\\mathrm{log}} = 111$ K.",
    title="Zinc Material Parameters",
)

zn_arxiv_table_row = SimpleMetalTableRow(
    material="Zn",
    structure="hcp",
    fermi_temperature_k=121_000.0,
    omega_log_k=111.0,
    lambda_value=0.502,
    rs=2.90,
    band_mass=1.0,
    source_table=SOURCE_TABLES,
    title="Zn arXiv Table II Row",
)
zn_arxiv_table_row.label = "zn_arxiv_table_row"
observe(
    zn_arxiv_table_row,
    rationale="Structured transcription from arXiv:2512.19382v2 TeX source Table II.",
)

zn_lambda_input = compute(
    LambdaInput,
    fn=_lambda_input_from_model,
    given=(zn_arxiv_table_row, shared_dfpt_lambda_error_model),
    label="compute_zn_lambda_input",
    rationale=(
        "Use the arXiv TeX Table II Zn lambda value and attach the shared "
        "DFPT lambda systematic error model."
    ),
)
zn_lambda_input.label = "zn_lambda_input"
zn_mu_star_input = compute(
    MuStarInput,
    fn=_mu_star_from_ueg_table,
    given=(zn_arxiv_table_row, ueg_mu_ef_table_i, tolmachev_log_mu_star_error_model),
    label="compute_zn_mu_star_input",
    rationale=(
        "Derive Zn mu* from Table I mu_EF(rs), Table II rs/mb/TF/omega_log, "
        "linear interpolation in effective rs, the BTS running relation, "
        "and the Tolmachev-log uncertainty model."
    ),
)
zn_mu_star_input.label = "zn_mu_star_input"
zn_effective_coupling = compute(
    EffectiveCoupling,
    fn=_effective_coupling,
    given=(zn_lambda_input, zn_mu_star_input),
    label="compute_zn_effective_coupling",
    rationale=(
        "Reduce the Zn Tc calculation to the effective pairing strength "
        "$g = \\lambda - \\mu^*(1 + 0.62\\lambda)$."
    ),
)
zn_effective_coupling.label = "zn_effective_coupling"

# ---------------------------------------------------------------------------
# Leaf claims
# ---------------------------------------------------------------------------

simple_metals_weak_lattice = Claim(
    "Simple metals (Al, Li, Na, Mg, Zn) have weak lattice effects in the "
    "Coulomb pseudopotential: the difference between the crystalline "
    "$\\mu^*$ and the UEG $\\mu^*$ at the same $r_s$ is small (a few "
    "percent) because the nearly-free-electron character of these metals "
    "means the Fermi surface is approximately spherical and the electronic "
    "structure is well described by the homogeneous electron gas with "
    "minor crystal-field perturbations.",
    title="Simple Metals Have Weak Lattice Effects",
)

ueg_pseudopotential_parameterization = Claim(
    "The UEG Coulomb pseudopotential $\\mu_{E_F}(r_s)$ computed by vDiagMC "
    "can be parameterized as a smooth function of $r_s$ and mapped onto "
    "real materials by using the material's effective $r_s$ (determined "
    "from the valence electron density). Combined with the BTS relation "
    "to run $\\mu_{E_F}$ down to the Debye scale, this provides "
    "$\\mu^*(r_s)$ for any simple metal without additional adjustable "
    "parameters.",
    title="UEG mu* Parameterization and Mapping",
)

li_effective_coupling_error_bounded = Claim(
    "For lithium, the effective pairing strength computed from "
    "$\\lambda = 0.34 \\pm 0.034$ and $\\mu^* = 0.1749 \\pm 0.0375$ is small "
    "($g = 0.1282 \\pm 0.0757$), so the transition temperature is sensitive "
    "to input errors. The propagated error remains bounded enough that the "
    "sign and smallness of $g$ remain qualitatively stable.",
    title="Li Effective Coupling Error Bound",
)

deduction(
    premises=[
        li_effective_coupling,
        li_low_temperature_lattice_assumption,
    ],
    conclusion=li_effective_coupling_error_bounded,
    reason=(
        "The computed effective coupling (@li_effective_coupling) compresses "
        "the Li $T_c$ calculation to the two inputs $\\lambda$ and $\\mu^*$. "
        "The $\\lambda$ uncertainty is already carried by the upstream "
        "DFPT lambda input model, while the Li lattice assumption is explicitly "
        "tracked (@li_low_temperature_lattice_assumption). The residual "
        "uncertainty is represented as an uncertainty on $g$."
    ),
)

# ---------------------------------------------------------------------------
# Derived claims
# ---------------------------------------------------------------------------

ab_initio_workflow = Claim(
    "The complete ab initio workflow for predicting $T_c$ of simple metals: "
    "(1) compute $\\mu_{E_F}$ from the UEG four-point vertex via vDiagMC, "
    "(2) map to the material's $r_s$ and run down to $\\mu^*$ via the BTS "
    "relation, (3) obtain $\\lambda$ from DFPT, (4) solve the downfolded "
    "Eliashberg equations (or use the PCF extrapolation) to predict $T_c$. "
    "All inputs are from first principles; no adjustable parameters remain.",
    title="Ab Initio Tc Prediction Workflow",
)

# Intermediate claim: μ* available for simple metals
mu_available_for_simple_metals = Claim(
    "For simple metals, the Coulomb pseudopotential $\\mu^*$ can be obtained "
    "from first principles without adjustable parameters: the vDiagMC-computed "
    "$\\mu_{E_F}(r_s)$ for the uniform electron gas is mapped to real materials "
    "via material-specific $r_s$ and band mass, then scaled to the Debye "
    "frequency via the BTS renormalization relation.",
    title="mu* Available for Simple Metals",
)

_s1 = noisy_and(
    premises=[ueg_pseudopotential_parameterization, mu_vdiagmc_values],
    conclusion=mu_available_for_simple_metals,
    background=[simple_metals_weak_lattice, bts_renormalization],
    reason=(
        "The vDiagMC results provide $\\mu_{E_F}(r_s)$ for the UEG "
        "(@mu_vdiagmc_values). The parameterization procedure "
        "(@ueg_pseudopotential_parameterization) maps these to real materials "
        "using material-specific $r_s$ and band mass, justified by the weak "
        "lattice effects in simple metals (@simple_metals_weak_lattice). "
        "The BTS relation (@bts_renormalization) scales $\\mu_{E_F}$ down "
        "to $\\mu^*$ at the Debye frequency."
    ),
)

_s2 = deduction(
    premises=[downfolded_bse, mu_available_for_simple_metals,
              dfpt_reliable_for_simple_metals],
    conclusion=ab_initio_workflow,
    reason=(
        "The downfolded BSE (@downfolded_bse) provides the theoretical "
        "equation requiring two microscopic inputs: $\\mu^*$ and $\\lambda$. "
        "Both are now available from first principles — $\\mu^*$ from the "
        "UEG parameterization (@mu_available_for_simple_metals) and $\\lambda$ "
        "from validated DFPT (@dfpt_reliable_for_simple_metals). With all "
        "components determined from first principles, the workflow is "
        "complete and parameter-free."
    ),
)

_composite_workflow = composite(
    premises=[downfolded_bse, mu_vdiagmc_values, dfpt_reliable_for_simple_metals,
              ueg_pseudopotential_parameterization],
    conclusion=ab_initio_workflow,
    sub_strategies=[_s1, _s2],
    background=[simple_metals_weak_lattice, bts_renormalization],
)

# ---------------------------------------------------------------------------
# Material-specific Tc predictions
# ---------------------------------------------------------------------------

tc_al_predicted = Claim(
    "The ab initio predicted superconducting transition temperature of "
    "aluminum is $T_c^{\\mathrm{th}} = 0.96$ K, in good agreement "
    "with the experimental value $T_c^{\\mathrm{exp}} = 1.2$ K. "
    "The first-principles $\\mu^*(\\mathrm{Al}) \\approx 0.13$ is obtained "
    "from the vDiagMC $\\mu_{E_F}$ at $r_s = 2.07$ via BTS renormalization.",
    title="Tc(Al) Ab Initio Prediction",
)

_strat_tc_al = noisy_and(
    premises=[ab_initio_workflow, al_effective_coupling],
    conclusion=tc_al_predicted,
    background=[aluminum_parameters],
    reason=(
        "Applying the ab initio workflow (@ab_initio_workflow) to aluminum "
        "with its material parameters (@aluminum_parameters): $r_s = 2.07$ "
        "and $m_b = 1.05$ give effective $r_s = 2.1735$ for the UEG "
        "parameterization, which the BTS relation reduces to "
        "$\\mu^* \\approx 0.13$ at $\\omega_{\\mathrm{log}} = 320$ K. "
        "Combined with the DFPT $\\lambda = 0.44$, the effective "
        "coupling calculation (@al_effective_coupling) carries the "
        "$\\lambda$ and $\\mu^*$ input uncertainties into the pairing "
        "strength entering the exponential $T_c$ dependence. The source "
        "TeX Table II reports $T_c = 0.96$ K for this parameter set."
    ),
)

tc_zn_predicted = Claim(
    "The ab initio predicted superconducting transition temperature of "
    "zinc is $T_c^{\\mathrm{th}} = 0.874$ K, consistent with "
    "the experimental value $T_c^{\\mathrm{exp}} = 0.875$ K. "
    "The first-principles $\\mu^*(\\mathrm{Zn}) \\approx 0.12$ is obtained "
    "from the vDiagMC $\\mu_{E_F}$ at $r_s = 2.90$.",
    title="Tc(Zn) Ab Initio Prediction",
)

_strat_tc_zn = noisy_and(
    premises=[ab_initio_workflow, zn_effective_coupling],
    conclusion=tc_zn_predicted,
    background=[zinc_parameters],
    reason=(
        "Applying the ab initio workflow (@ab_initio_workflow) to zinc with "
        "its material parameters (@zinc_parameters): $r_s = 2.90$ maps to "
        "$\\mu^* \\approx 0.12$ at $\\omega_{\\mathrm{log}} = 111$ K via "
        "the Table I interpolation and BTS running. Combined with "
        "$\\lambda = 0.502$ from DFPT, the effective coupling calculation "
        "(@zn_effective_coupling) carries the $\\lambda$ and $\\mu^*$ "
        "input uncertainties into the pairing strength. The "
        "source TeX Table II reports $T_c = 0.874$ K, essentially matching "
        "experiment."
    ),
)

tc_li_predicted = Claim(
    "The ab initio predicted superconducting transition temperature of "
    "lithium in the 9R row is $T_c^{\\mathrm{th}} = 5 \\times 10^{-3}$ K, "
    "while the hcp row gives $T_c^{\\mathrm{th}} = 0.03$ K and the reported "
    "experimental value is $T_c^{\\mathrm{exp}} \\approx 4 \\times 10^{-4}$ K. "
    "The large $\\mu^*(\\mathrm{Li}) \\approx 0.18$ from the rescaled "
    "$r_s = 5.6875$ nearly cancels the phonon-mediated attraction "
    "$\\lambda = 0.34$, pushing $T_c$ to very low temperatures but leaving "
    "a residual discrepancy tied to the debated low-temperature lattice structure.",
    title="Tc(Li) Ab Initio Prediction",
)

_strat_tc_li = noisy_and(
    premises=[
        ab_initio_workflow,
        li_low_temperature_lattice_assumption,
        li_effective_coupling,
        li_effective_coupling_error_bounded,
    ],
    conclusion=tc_li_predicted,
    background=[lithium_parameters],
    reason=(
        "Applying the ab initio workflow (@ab_initio_workflow) to lithium "
        "with its Table II 9R material parameters (@lithium_parameters): "
        "$r_s = 3.25$ and $m_b = 1.75$ give effective $r_s = 5.6875$, "
        "reduced to $\\mu^* \\approx 0.1749$ at "
        "$\\omega_{\\mathrm{log}} = 242$ K via BTS. Despite a moderate "
        "$\\lambda = 0.34$, the large $\\mu^*$ nearly cancels the effective "
        "pairing interaction. The Li low-temperature lattice assumption "
        "(@li_low_temperature_lattice_assumption) is tracked directly. Because "
        "$g \\simeq \\lambda - \\mu^*(1 + 0.62\\lambda)$ is small, the "
        "computed effective coupling (@li_effective_coupling) and its "
        "bounded-error claim (@li_effective_coupling_error_bounded) carry the "
        "input uncertainty explicitly."
    ),
)

al_pressure_transition = Claim(
    "Under hydrostatic pressure, the ab initio framework predicts that "
    "aluminum's superconducting $T_c$ initially increases as pressure "
    "stiffens phonon frequencies (increasing $\\omega_{\\mathrm{log}}$) "
    "while $\\lambda$ and $\\mu^*$ change modestly, before eventually "
    "decreasing at very high pressures when $\\lambda$ is suppressed. "
    "This non-monotonic behavior is consistent with experimental "
    "pressure studies.",
    title="Al Pressure-Tc Transition",
)

_strat_al_pressure = noisy_and(
    premises=[ab_initio_workflow],
    conclusion=al_pressure_transition,
    background=[aluminum_parameters],
    reason=(
        "Applying the ab initio workflow (@ab_initio_workflow) to aluminum "
        "under varying hydrostatic pressure (@aluminum_parameters): as "
        "pressure increases, the lattice stiffens, raising phonon frequencies "
        "and $\\omega_{\\mathrm{log}}$. The $r_s$ decreases modestly "
        "(higher electron density), slightly reducing $\\mu^*$ via the "
        "vDiagMC parameterization. The electron-phonon coupling $\\lambda$ "
        "from DFPT varies non-monotonically. The net effect is an initial "
        "increase in $T_c$ followed by a decrease at high pressures, "
        "reflecting the competition between the prefactor "
        "$\\omega_{\\mathrm{log}}$ and the exponential sensitivity to the "
        "effective coupling $\\lambda - \\mu^*(1 + 0.62\\lambda)$."
    ),
)

tc_mg_na_near_qpt = Claim(
    "The ab initio framework predicts that sodium and magnesium have "
    "extremely low or vanishing $T_c$: for Na ($r_s = 3.93$, "
    "$\\lambda \\approx 0.18$), the large $\\mu^*$ exceeds the weak "
    "electron-phonon coupling, giving net repulsion in the pairing "
    "channel and no superconductivity. For Mg ($r_s = 2.66$, "
    "$\\lambda \\approx 0.26$), $T_c$ is in the sub-nanokelvin regime. "
    "Both materials are near the quantum phase transition between "
    "superconducting and non-superconducting ground states, where "
    "$T_c$ varies exponentially with small parameter changes.",
    title="Na and Mg Near Quantum Phase Transition",
)

_strat_mg_na_qpt = noisy_and(
    premises=[ab_initio_workflow],
    conclusion=tc_mg_na_near_qpt,
    background=[magnesium_parameters, sodium_parameters, precursory_cooper_flow],
    reason=(
        "Applying the ab initio workflow (@ab_initio_workflow) to sodium "
        "(@sodium_parameters) and magnesium (@magnesium_parameters): Na has "
        "$r_s = 3.93$, yielding $\\mu^* \\approx 0.18$ which exceeds its "
        "weak $\\lambda \\approx 0.18$, placing Na in the net-repulsive "
        "regime with no Cooper instability. Mg has $r_s = 2.66$, yielding "
        "$\\mu^* \\approx 0.13$ which nearly cancels $\\lambda \\approx 0.26$, "
        "pushing $T_c$ to unobservably low temperatures. The precursory "
        "Cooper flow formalism (@precursory_cooper_flow) shows that near "
        "the quantum phase transition ($g \\to 0$), $T_c = \\omega_\\Lambda "
        "e^{1/g}$ is exponentially sensitive to the coupling, explaining why "
        "small parameter variations can toggle between superconducting and "
        "non-superconducting ground states."
    ),
)

# ---------------------------------------------------------------------------
# Likelihood inferences: comparing predictions with experiment
# ---------------------------------------------------------------------------

_al_ab_initio_likelihood = _tc_agreement_likelihood(
    predicted_tc_k=0.96,
    experimental_tc_k=1.2,
    theory_log_tc_uncertainty=_log_tc_uncertainty_from_g(al_effective_coupling),
    experimental_log_tc_uncertainty=PRECISE_EXPERIMENT_LOG_TC_UNCERTAINTY,
)
_al_phenomenological_likelihood = _tc_agreement_likelihood_from_uniform_mu_star(
    reference_tc_k=1.9,
    lambda_value=al_lambda_input.value,
    experimental_tc_k=1.2,
    experimental_log_tc_uncertainty=PRECISE_EXPERIMENT_LOG_TC_UNCERTAINTY,
)
_zn_ab_initio_likelihood = _tc_agreement_likelihood(
    predicted_tc_k=0.874,
    experimental_tc_k=0.875,
    theory_log_tc_uncertainty=_log_tc_uncertainty_from_g(zn_effective_coupling),
    experimental_log_tc_uncertainty=PRECISE_EXPERIMENT_LOG_TC_UNCERTAINTY,
)
_zn_phenomenological_likelihood = _tc_agreement_likelihood_from_uniform_mu_star(
    reference_tc_k=1.37,
    lambda_value=zn_lambda_input.value,
    experimental_tc_k=0.875,
    experimental_log_tc_uncertainty=PRECISE_EXPERIMENT_LOG_TC_UNCERTAINTY,
)
_li_ab_initio_likelihood = _tc_agreement_likelihood(
    predicted_tc_k=5e-3,
    experimental_tc_k=4e-4,
    theory_log_tc_uncertainty=_log_tc_uncertainty_from_g(li_effective_coupling),
    experimental_log_tc_uncertainty=LI_EXPERIMENT_LOG_TC_UNCERTAINTY,
)
_li_phenomenological_likelihood = _tc_agreement_likelihood_from_uniform_mu_star(
    reference_tc_k=0.35,
    lambda_value=li_lambda_input.value,
    experimental_tc_k=4e-4,
    experimental_log_tc_uncertainty=LI_EXPERIMENT_LOG_TC_UNCERTAINTY,
)

infer(
    hypothesis=tc_al_predicted,
    evidence=tc_al_experimental,
    p_e_given_h=_al_ab_initio_likelihood[0],
    p_e_given_not_h=_al_ab_initio_likelihood[1],
    label="infer_tc_al_ab_initio_agreement",
    reason=(
        "The experimental $T_c(\\mathrm{Al}) = 1.2$ K (@tc_al_experimental) "
        "is well reproduced by the ab initio prediction "
        "$T_c^{\\mathrm{th}} = 0.96$ K (@tc_al_predicted), which "
        "uses no adjustable parameters. The phenomenological comparison "
        "(@tc_al_phenomenological) treats the traditional empirical "
        "$\\mu^*$ choice as a uniform 0.1--0.2 range; its $\\mu^* = 0.1$ "
        "endpoint gives 1.9 K, but the full range is broad. The ab initio "
        "approach provides a better explanation because it determines "
        "$\\mu^*$ from first principles rather than using an adjustable "
        "empirical band, and the resulting $\\mu^* \\approx 0.13$ correctly "
        "reduces $T_c$ to the experimental range. The infer CPT is filled "
        "by the log-Tc agreement likelihood computed from the prediction, "
        "experiment, and propagated log-Tc uncertainty."
    ),
)

infer(
    hypothesis=tc_al_phenomenological,
    evidence=tc_al_experimental,
    p_e_given_h=_al_phenomenological_likelihood[0],
    p_e_given_not_h=_al_phenomenological_likelihood[1],
    label="infer_tc_al_phenomenological_test",
    reason=(
        "The experimental $T_c(\\mathrm{Al}) = 1.2$ K (@tc_al_experimental) "
        "is compatible with part of the phenomenological estimate "
        "(@tc_al_phenomenological), but only after marginalizing over the "
        "adjustable $\\mu^* \\in [0.1, 0.2]$ band. The infer CPT is filled "
        "by the log-Tc agreement likelihood averaged over a uniform "
        "$\\mu^*$ phenomenological prediction."
    ),
)

infer(
    hypothesis=tc_zn_predicted,
    evidence=tc_zn_experimental,
    p_e_given_h=_zn_ab_initio_likelihood[0],
    p_e_given_not_h=_zn_ab_initio_likelihood[1],
    label="infer_tc_zn_ab_initio_agreement",
    reason=(
        "The experimental $T_c(\\mathrm{Zn}) = 0.875$ K (@tc_zn_experimental) "
        "is consistent with the ab initio prediction "
        "$T_c^{\\mathrm{th}} = 0.874$ K (@tc_zn_predicted). "
        "The phenomenological comparison (@tc_zn_phenomenological) treats "
        "the empirical $\\mu^*$ choice as a uniform 0.1--0.2 range; its "
        "$\\mu^* = 0.1$ endpoint gives 1.37 K, while higher $\\mu^*$ values "
        "lower the predicted $T_c$. The ab initio $\\mu^* \\approx 0.12$ "
        "from $r_s = 2.90$ captures the Coulomb repulsion in Zn from "
        "first principles, bringing the prediction into agreement with "
        "experiment. The infer CPT is filled by the log-Tc agreement "
        "likelihood computed from the prediction, experiment, and "
        "propagated log-Tc uncertainty."
    ),
)

infer(
    hypothesis=tc_zn_phenomenological,
    evidence=tc_zn_experimental,
    p_e_given_h=_zn_phenomenological_likelihood[0],
    p_e_given_not_h=_zn_phenomenological_likelihood[1],
    label="infer_tc_zn_phenomenological_test",
    reason=(
        "The experimental $T_c(\\mathrm{Zn}) = 0.875$ K (@tc_zn_experimental) "
        "falls inside the broad phenomenological estimate "
        "(@tc_zn_phenomenological), but that agreement depends on the "
        "adjustable $\\mu^* \\in [0.1, 0.2]$ choice. The infer CPT is filled "
        "by the log-Tc agreement likelihood averaged over a uniform "
        "$\\mu^*$ phenomenological prediction."
    ),
)

infer(
    hypothesis=tc_li_predicted,
    evidence=tc_li_experimental,
    p_e_given_h=_li_ab_initio_likelihood[0],
    p_e_given_not_h=_li_ab_initio_likelihood[1],
    label="infer_tc_li_ab_initio_agreement",
    reason=(
        "The experimental $T_c(\\mathrm{Li}) \\approx 4 \\times 10^{-4}$ K "
        "(@tc_li_experimental) is closer to the ab initio prediction "
        "$T_c^{\\mathrm{th}} = 5 \\times 10^{-3}$ K for the 9R row "
        "(@tc_li_predicted) than to the phenomenological estimate, but it "
        "still sits roughly one order of magnitude lower than the Table II "
        "prediction. "
        "The phenomenological comparison (@tc_li_phenomenological) treats "
        "$\\mu^*$ as uniform over 0.1--0.2: the $\\mu^* = 0.1$ endpoint gives "
        "$\\approx 0.35$ K, while the high-$\\mu^*$ tail can reach the "
        "sub-millikelvin scale. The dramatic improvement of the ab initio "
        "approach is that the first-principles $\\mu^* \\approx 0.18$ for "
        "lithium lands in this high-$\\mu^*$ regime without empirical tuning. "
        "The remaining gap is represented by the explicit lithium lattice "
        "assumption and the propagated effective-coupling uncertainty. The "
        "infer CPT is filled by the log-Tc agreement likelihood, with a "
        "larger experimental log-Tc uncertainty for the disputed low-"
        "temperature Li structure."
    ),
)

infer(
    hypothesis=tc_li_phenomenological,
    evidence=tc_li_experimental,
    p_e_given_h=_li_phenomenological_likelihood[0],
    p_e_given_not_h=_li_phenomenological_likelihood[1],
    label="infer_tc_li_phenomenological_test",
    reason=(
        "The experimental $T_c(\\mathrm{Li}) \\approx 4 \\times 10^{-4}$ K "
        "(@tc_li_experimental) can be reached by the high-$\\mu^*$ tail of "
        "the phenomenological estimate (@tc_li_phenomenological), but the "
        "uniform 0.1--0.2 $\\mu^*$ range spans more than three orders of "
        "magnitude in $T_c$. The infer CPT is filled by the log-Tc agreement "
        "likelihood averaged over a uniform $\\mu^*$ phenomenological "
        "prediction."
    ),
)
