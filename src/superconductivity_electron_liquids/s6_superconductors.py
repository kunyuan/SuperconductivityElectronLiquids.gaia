"""Conventional Superconductors

Assembles the ab initio workflow for predicting Tc of simple metals, presents
the first-principles predictions for Al, Zn, Li, Na, and Mg, and confronts
them with experiment via abduction.
"""

from gaia.lang import abduction, claim, composite, deduction, noisy_and, setting

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
from .s5_eph_coupling import dfpt_reliable_for_simple_metals

# ---------------------------------------------------------------------------
# Settings — material parameters
# ---------------------------------------------------------------------------

aluminum_parameters = setting(
    "Aluminum (Al): FCC crystal structure, $r_s = 2.07$, experimental "
    "Debye temperature $\\Theta_D \\approx 428$ K, DFPT electron-phonon "
    "coupling $\\lambda \\approx 0.44$, logarithmic phonon frequency "
    "$\\omega_{\\mathrm{log}} \\approx 300$ K.",
    title="Aluminum Material Parameters",
)

lithium_parameters = setting(
    "Lithium (Li): BCC (or 9R at low $T$) crystal structure, "
    "$r_s = 3.25$, experimental Debye temperature "
    "$\\Theta_D \\approx 344$ K, DFPT electron-phonon coupling "
    "$\\lambda \\approx 0.41$ (BCC), logarithmic phonon frequency "
    "$\\omega_{\\mathrm{log}} \\approx 250$ K. Crystal structure at "
    "sub-kelvin temperatures remains debated.",
    title="Lithium Material Parameters",
)

sodium_parameters = setting(
    "Sodium (Na): BCC crystal structure, $r_s = 3.93$, experimental "
    "Debye temperature $\\Theta_D \\approx 158$ K, DFPT electron-phonon "
    "coupling $\\lambda \\approx 0.18$, logarithmic phonon frequency "
    "$\\omega_{\\mathrm{log}} \\approx 120$ K. No superconductivity "
    "observed down to mK temperatures.",
    title="Sodium Material Parameters",
)

magnesium_parameters = setting(
    "Magnesium (Mg): HCP crystal structure, $r_s = 2.66$, experimental "
    "Debye temperature $\\Theta_D \\approx 400$ K, DFPT electron-phonon "
    "coupling $\\lambda \\approx 0.26$, logarithmic phonon frequency "
    "$\\omega_{\\mathrm{log}} \\approx 290$ K. No superconductivity "
    "observed down to mK temperatures.",
    title="Magnesium Material Parameters",
)

zinc_parameters = setting(
    "Zinc (Zn): HCP crystal structure, $r_s = 2.31$, experimental "
    "Debye temperature $\\Theta_D \\approx 327$ K, DFPT electron-phonon "
    "coupling $\\lambda \\approx 0.43$, logarithmic phonon frequency "
    "$\\omega_{\\mathrm{log}} \\approx 200$ K.",
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
)

# ---------------------------------------------------------------------------
# Derived claims
# ---------------------------------------------------------------------------

ab_initio_workflow = claim(
    "The complete ab initio workflow for predicting $T_c$ of simple metals: "
    "(1) compute $\\mu_{E_F}$ from the UEG four-point vertex via vDiagMC, "
    "(2) map to the material's $r_s$ and run down to $\\mu^*$ via the BTS "
    "relation, (3) obtain $\\lambda$ from DFPT, (4) solve the downfolded "
    "Eliashberg equations (or use the PCF extrapolation) to predict $T_c$. "
    "All inputs are from first principles; no adjustable parameters remain.",
    title="Ab Initio Tc Prediction Workflow",
)

# Intermediate claim: μ* available for simple metals
mu_available_for_simple_metals = claim(
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

tc_al_predicted = claim(
    "The ab initio predicted superconducting transition temperature of "
    "aluminum is $T_c^{\\mathrm{th}} = 1.1 \\pm 0.3$ K, in good agreement "
    "with the experimental value $T_c^{\\mathrm{exp}} = 1.2$ K. "
    "The first-principles $\\mu^*(\\mathrm{Al}) \\approx 0.11$ is obtained "
    "from the vDiagMC $\\mu_{E_F}$ at $r_s = 2.07$ via BTS renormalization.",
    title="Tc(Al) Ab Initio Prediction",
)

_strat_tc_al = noisy_and(
    premises=[ab_initio_workflow],
    conclusion=tc_al_predicted,
    background=[aluminum_parameters],
    reason=(
        "Applying the ab initio workflow (@ab_initio_workflow) to aluminum "
        "with its material parameters (@aluminum_parameters): $r_s = 2.07$ "
        "gives $\\mu_{E_F} \\approx 0.22$ from the vDiagMC parameterization, "
        "which the BTS relation reduces to $\\mu^* \\approx 0.11$ at the "
        "Debye scale. Combined with the DFPT $\\lambda \\approx 0.44$ and "
        "$\\omega_{\\mathrm{log}} \\approx 300$ K, solving the Eliashberg "
        "equations yields $T_c = 1.1 \\pm 0.3$ K, where the uncertainty "
        "reflects the vDiagMC error bars on $\\mu_{E_F}$ propagated through "
        "the exponentially sensitive $T_c$ formula."
    ),
)

tc_zn_predicted = claim(
    "The ab initio predicted superconducting transition temperature of "
    "zinc is $T_c^{\\mathrm{th}} = 0.7 \\pm 0.3$ K, consistent with "
    "the experimental value $T_c^{\\mathrm{exp}} = 0.875$ K. "
    "The first-principles $\\mu^*(\\mathrm{Zn}) \\approx 0.12$ is obtained "
    "from the vDiagMC $\\mu_{E_F}$ at $r_s = 2.31$.",
    title="Tc(Zn) Ab Initio Prediction",
)

_strat_tc_zn = noisy_and(
    premises=[ab_initio_workflow],
    conclusion=tc_zn_predicted,
    background=[zinc_parameters],
    reason=(
        "Applying the ab initio workflow (@ab_initio_workflow) to zinc with "
        "its material parameters (@zinc_parameters): $r_s = 2.31$ gives "
        "$\\mu_{E_F} \\approx 0.25$ from the vDiagMC parameterization, "
        "reduced to $\\mu^* \\approx 0.12$ at the Debye scale via BTS. "
        "Combined with $\\lambda \\approx 0.43$ and "
        "$\\omega_{\\mathrm{log}} \\approx 200$ K from DFPT, the predicted "
        "$T_c = 0.7 \\pm 0.3$ K agrees with experiment within uncertainty."
    ),
)

tc_li_predicted = claim(
    "The ab initio predicted superconducting transition temperature of "
    "lithium is $T_c^{\\mathrm{th}} \\lesssim 10^{-3}$ K (sub-millikelvin), "
    "consistent with the experimental observation "
    "$T_c^{\\mathrm{exp}} \\approx 4 \\times 10^{-4}$ K. The large "
    "$\\mu^*(\\mathrm{Li}) \\approx 0.16$ from $r_s = 3.25$ almost "
    "completely cancels the phonon-mediated attraction $\\lambda \\approx 0.41$, "
    "pushing $T_c$ to extremely low temperatures.",
    title="Tc(Li) Ab Initio Prediction",
)

_strat_tc_li = noisy_and(
    premises=[ab_initio_workflow],
    conclusion=tc_li_predicted,
    background=[lithium_parameters],
    reason=(
        "Applying the ab initio workflow (@ab_initio_workflow) to lithium "
        "with its material parameters (@lithium_parameters): $r_s = 3.25$ "
        "gives $\\mu_{E_F} \\approx 0.32$ from the vDiagMC parameterization, "
        "reduced to $\\mu^* \\approx 0.16$ at the Debye scale via BTS. "
        "Despite a moderate $\\lambda \\approx 0.41$ from DFPT, the large "
        "$\\mu^*$ nearly cancels the effective pairing interaction, making "
        "the dimensionless coupling $g = \\lambda - \\mu^* \\approx 0.25$ "
        "very small. The exponential sensitivity $T_c \\propto \\exp(-1/g)$ "
        "then drives $T_c$ to the sub-millikelvin regime, consistent with "
        "the experimental value."
    ),
)

al_pressure_transition = claim(
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

tc_mg_na_near_qpt = claim(
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
# Abductions: comparing ab initio predictions with experiment
# ---------------------------------------------------------------------------

abduction(
    tc_al_experimental,
    tc_al_predicted,
    tc_al_phenomenological,
    reason=(
        "The experimental $T_c(\\mathrm{Al}) = 1.2$ K (@tc_al_experimental) "
        "is well reproduced by the ab initio prediction "
        "$T_c^{\\mathrm{th}} = 1.1 \\pm 0.3$ K (@tc_al_predicted), which "
        "uses no adjustable parameters. The phenomenological prediction "
        "(@tc_al_phenomenological) using $\\mu^* = 0.1$ gives 1.9 K, "
        "overestimating by 58%. The ab initio approach provides a better "
        "explanation because it determines $\\mu^*$ from first principles "
        "rather than using an ad hoc value, and the resulting $\\mu^* \\approx "
        "0.11$ is close to but slightly above the standard guess, correctly "
        "reducing $T_c$ to the experimental range."
    ),
)

abduction(
    tc_zn_experimental,
    tc_zn_predicted,
    tc_zn_phenomenological,
    reason=(
        "The experimental $T_c(\\mathrm{Zn}) = 0.875$ K (@tc_zn_experimental) "
        "is consistent with the ab initio prediction "
        "$T_c^{\\mathrm{th}} = 0.7 \\pm 0.3$ K (@tc_zn_predicted). "
        "The phenomenological prediction (@tc_zn_phenomenological) using "
        "$\\mu^* = 0.1$ gives 1.37 K, overestimating by 57%. The ab initio "
        "$\\mu^* \\approx 0.12$ from $r_s = 2.31$ correctly captures the "
        "stronger Coulomb repulsion in Zn compared to the standard guess, "
        "bringing the prediction into agreement with experiment."
    ),
)

abduction(
    tc_li_experimental,
    tc_li_predicted,
    tc_li_phenomenological,
    reason=(
        "The experimental $T_c(\\mathrm{Li}) \\approx 4 \\times 10^{-4}$ K "
        "(@tc_li_experimental) is consistent with the ab initio prediction "
        "$T_c^{\\mathrm{th}} \\lesssim 10^{-3}$ K (@tc_li_predicted). "
        "The phenomenological prediction (@tc_li_phenomenological) using "
        "$\\mu^* = 0.1$ gives $\\approx 0.35$ K, overestimating by three "
        "orders of magnitude. The dramatic improvement of the ab initio "
        "approach is because the first-principles $\\mu^* \\approx 0.16$ for "
        "lithium ($r_s = 3.25$) is significantly larger than the standard "
        "guess of 0.1, reflecting the stronger Coulomb repulsion at lower "
        "electron density. In the regime where $\\lambda - \\mu^*(1+0.62\\lambda)$ "
        "is small, the exponential sensitivity amplifies this difference "
        "from $\\sim 0.06$ in $\\mu^*$ to three orders of magnitude in $T_c$."
    ),
)
