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
    "Aluminum (Al): FCC crystal structure, $r_s = 2.07$, band mass "
    "$m_b = 1.05$, DFPT electron-phonon coupling $\\lambda = 0.44$, "
    "logarithmic phonon frequency $\\omega_{\\mathrm{log}} = 320$ K, "
    "Fermi temperature $T_F = 1.3 \\times 10^5$ K.",
    title="Aluminum Material Parameters",
)

lithium_parameters = setting(
    "Lithium (Li): 9R crystal structure at low $T$ (also studied in "
    "HCP). 9R parameters: $r_s = 3.25$, $m_b = 1.75$, $\\lambda = 0.34$, "
    "$\\omega_{\\mathrm{log}} = 242$ K, $T_F = 4.0 \\times 10^4$ K. "
    "HCP parameters: $r_s = 3.19$, $m_b = 1.4$, $\\lambda = 0.37$, "
    "$\\omega_{\\mathrm{log}} = 243$ K, $T_F = 4.1 \\times 10^4$ K. "
    "Crystal structure at sub-kelvin temperatures remains debated.",
    title="Lithium Material Parameters",
)

sodium_parameters = setting(
    "Sodium (Na): BCC crystal structure, $r_s = 3.96$, band mass "
    "$m_b = 1.0$, DFPT electron-phonon coupling $\\lambda = 0.2$, "
    "logarithmic phonon frequency $\\omega_{\\mathrm{log}} = 127$ K, "
    "Fermi temperature $T_F = 4.2 \\times 10^4$ K. No superconductivity "
    "observed down to mK temperatures.",
    title="Sodium Material Parameters",
)

magnesium_parameters = setting(
    "Magnesium (Mg): HCP crystal structure, $r_s = 2.66$, band mass "
    "$m_b = 1.02$, DFPT electron-phonon coupling $\\lambda = 0.24$, "
    "logarithmic phonon frequency $\\omega_{\\mathrm{log}} = 269$ K, "
    "Fermi temperature $T_F = 8.0 \\times 10^4$ K. No superconductivity "
    "observed down to mK temperatures.",
    title="Magnesium Material Parameters",
)

zinc_parameters = setting(
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
    metadata={
        "figure": "artifacts/images/13_0.jpg",
        "caption": "Fig. 9 | Proposed ab initio framework for electron-phonon SC beyond the weak correlation limit, showing computational pathway from fundamental parameters through correlated electrons and lattice vibrations to superconducting properties.",
    },
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
    "aluminum is $T_c^{\\mathrm{EFT}} = 0.96$ K, in good agreement "
    "with the experimental value $T_c^{\\mathrm{exp}} = 1.2$ K. "
    "The first-principles $\\mu^*(\\mathrm{Al}) = 0.13$ is obtained "
    "from the vDiagMC $\\mu_{E_F}$ at $r_s = 2.07$ (with band mass "
    "$m_b = 1.05$) via BTS renormalization.",
    title="Tc(Al) Ab Initio Prediction",
    metadata={
        "figure": "artifacts/images/14_0.jpg",
        "caption": "Fig. 10 | Pressure dependence of the superconducting critical temperature in aluminum. EFT results (squares) compared with experimental data from Levy et al. and Gubser et al.",
    },
)

_strat_tc_al = noisy_and(
    premises=[ab_initio_workflow],
    conclusion=tc_al_predicted,
    background=[aluminum_parameters],
    reason=(
        "Applying the ab initio workflow (@ab_initio_workflow) to aluminum "
        "with its material parameters (@aluminum_parameters): $r_s = 2.07$ "
        "with band mass $m_b = 1.05$ gives $\\mu^* = 0.13$ from the vDiagMC "
        "parameterization via BTS renormalization. Combined with the DFPT "
        "$\\lambda = 0.44$ and $\\omega_{\\mathrm{log}} = 320$ K, solving "
        "the Eliashberg equations yields $T_c^{\\mathrm{EFT}} = 0.96$ K, "
        "in good agreement with the experimental value of 1.2 K."
    ),
)

tc_zn_predicted = claim(
    "The ab initio predicted superconducting transition temperature of "
    "zinc is $T_c^{\\mathrm{EFT}} = 0.874$ K, in excellent agreement "
    "with the experimental value $T_c^{\\mathrm{exp}} = 0.875$ K. "
    "The first-principles $\\mu^*(\\mathrm{Zn}) = 0.12$ is obtained "
    "from the vDiagMC $\\mu_{E_F}$ at $r_s = 2.90$ (with band mass "
    "$m_b = 1.0$) via BTS renormalization.",
    title="Tc(Zn) Ab Initio Prediction",
    metadata={
        "figure": "artifacts/images/15_0.jpg",
        "caption": "Fig. 11 | Effective BCS coupling strength for simple metals. E-ph couplings from DFPT; pseudopotentials from vDiagMC. Includes Al, Zn, Li, Na, Mg predictions.",
    },
)

_strat_tc_zn = noisy_and(
    premises=[ab_initio_workflow],
    conclusion=tc_zn_predicted,
    background=[zinc_parameters],
    reason=(
        "Applying the ab initio workflow (@ab_initio_workflow) to zinc with "
        "its material parameters (@zinc_parameters): $r_s = 2.90$ with "
        "band mass $m_b = 1.0$ gives $\\mu^* = 0.12$ via BTS. "
        "Combined with $\\lambda = 0.502$ and "
        "$\\omega_{\\mathrm{log}} = 111$ K from DFPT, the predicted "
        "$T_c^{\\mathrm{EFT}} = 0.874$ K is in excellent agreement with "
        "the experimental value of 0.875 K."
    ),
)

tc_li_predicted = claim(
    "The ab initio predicted superconducting transition temperature of "
    "lithium (9R structure) is $T_c^{\\mathrm{EFT}} = 5 \\times 10^{-3}$ K, "
    "within an order of magnitude of the experimental observation "
    "$T_c^{\\mathrm{exp}} \\approx 4 \\times 10^{-4}$ K. The large "
    "$\\mu^*(\\mathrm{Li}) = 0.18$ from $r_s = 3.25$ (with band mass "
    "$m_b = 1.75$) almost completely cancels the phonon-mediated attraction "
    "$\\lambda = 0.34$, pushing $T_c$ to extremely low temperatures. "
    "The HCP structure gives $T_c^{\\mathrm{EFT}} = 0.03$ K with "
    "$\\mu^* = 0.17$ and $\\lambda = 0.37$.",
    title="Tc(Li) Ab Initio Prediction",
    metadata={
        "figure": "artifacts/images/15_0.jpg",
        "caption": "Fig. 11 | Effective BCS coupling strength for simple metals. E-ph couplings from DFPT; pseudopotentials from vDiagMC. Includes Al, Zn, Li, Na, Mg predictions.",
    },
)

_strat_tc_li = noisy_and(
    premises=[ab_initio_workflow],
    conclusion=tc_li_predicted,
    background=[lithium_parameters],
    reason=(
        "Applying the ab initio workflow (@ab_initio_workflow) to lithium "
        "(9R structure) with its material parameters (@lithium_parameters): "
        "$r_s = 3.25$ with band mass $m_b = 1.75$ gives $\\mu^* = 0.18$ "
        "via BTS. Despite a moderate $\\lambda = 0.34$ from DFPT, the large "
        "$\\mu^*$ nearly cancels the effective pairing interaction, making "
        "the dimensionless coupling $g = \\lambda - \\mu^*(1+0.62\\lambda)$ "
        "very small. The exponential sensitivity $T_c \\propto \\exp(-1/g)$ "
        "drives $T_c$ to $5 \\times 10^{-3}$ K, within an order of "
        "magnitude of the experimental value $4 \\times 10^{-4}$ K."
    ),
)

al_pressure_transition = claim(
    "Under hydrostatic pressure, the ab initio framework predicts that "
    "aluminum's superconducting $T_c$ monotonically decreases, consistent "
    "with experimental data up to 6 GPa. The framework predicts that "
    "superconductivity in Al vanishes at approximately 60 GPa; at 20 GPa, "
    "$T_c$ is already suppressed below 1 mK.",
    title="Al Pressure-Tc Transition",
    metadata={
        "figure": "artifacts/images/14_0.jpg",
        "caption": "Fig. 10 | Pressure dependence of the superconducting critical temperature in aluminum. EFT results (squares) compared with experimental data from Levy et al. and Gubser et al.",
    },
)

_strat_al_pressure = noisy_and(
    premises=[ab_initio_workflow],
    conclusion=al_pressure_transition,
    background=[aluminum_parameters],
    reason=(
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
    metadata={
        "figure": "artifacts/images/15_0.jpg",
        "caption": "Fig. 11 | Effective BCS coupling strength for simple metals. Na and Mg appear near the origin, indicating near-cancellation of pairing interaction.",
    },
)

_strat_mg_na_qpt = noisy_and(
    premises=[ab_initio_workflow],
    conclusion=tc_mg_na_near_qpt,
    background=[magnesium_parameters, sodium_parameters, precursory_cooper_flow],
    reason=(
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
        "$T_c^{\\mathrm{EFT}} = 0.96$ K (@tc_al_predicted), which "
        "uses no adjustable parameters. The phenomenological prediction "
        "(@tc_al_phenomenological) using $\\mu^* = 0.1$ gives 1.9 K, "
        "overestimating by 58%. The ab initio approach provides a better "
        "explanation because it determines $\\mu^*$ from first principles "
        "rather than using an ad hoc value, and the resulting $\\mu^* = "
        "0.13$ is above the standard guess of 0.1, correctly "
        "reducing $T_c$ toward the experimental value."
    ),
)

abduction(
    tc_zn_experimental,
    tc_zn_predicted,
    tc_zn_phenomenological,
    reason=(
        "The experimental $T_c(\\mathrm{Zn}) = 0.875$ K (@tc_zn_experimental) "
        "is in excellent agreement with the ab initio prediction "
        "$T_c^{\\mathrm{EFT}} = 0.874$ K (@tc_zn_predicted). "
        "The phenomenological prediction (@tc_zn_phenomenological) using "
        "$\\mu^* = 0.1$ gives 1.37 K, overestimating by 57%. The ab initio "
        "$\\mu^* = 0.12$ from $r_s = 2.90$ correctly captures the "
        "Coulomb repulsion strength in Zn, "
        "bringing the prediction into near-exact agreement with experiment."
    ),
)

abduction(
    tc_li_experimental,
    tc_li_predicted,
    tc_li_phenomenological,
    reason=(
        "The experimental $T_c(\\mathrm{Li}) \\approx 4 \\times 10^{-4}$ K "
        "(@tc_li_experimental) is within an order of magnitude of the ab "
        "initio prediction $T_c^{\\mathrm{EFT}} = 5 \\times 10^{-3}$ K "
        "(@tc_li_predicted, 9R structure). The phenomenological prediction "
        "(@tc_li_phenomenological) using $\\mu^* = 0.1$ gives $\\approx 0.35$ K, "
        "overestimating by three orders of magnitude. The dramatic improvement "
        "of the ab initio approach is because the first-principles "
        "$\\mu^* = 0.18$ for lithium ($r_s = 3.25$, $m_b = 1.75$) is "
        "significantly larger than the standard guess of 0.1, reflecting "
        "the stronger Coulomb repulsion at lower electron density. In the "
        "regime where $\\lambda - \\mu^*(1+0.62\\lambda)$ is small, the "
        "exponential sensitivity amplifies the $\\mu^*$ difference from "
        "0.08 to nearly three orders of magnitude in $T_c$."
    ),
)
