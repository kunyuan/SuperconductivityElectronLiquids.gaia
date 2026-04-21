"""Introduction: Motivation and Background

Establishes the theoretical context (BCS/Migdal-Eliashberg) and the phenomenological
limitations of traditional approaches to predicting superconducting Tc, motivating the
need for a first-principles treatment of the Coulomb pseudopotential.
"""

from gaia.lang import ParameterizedClaim, claim, deduction, question, setting


class TcValue(ParameterizedClaim):
    template = (
        "The {role} superconducting transition temperature of {material}"
        "{structure} is {value_K} K. {detail}"
    )

    material: str
    role: str
    structure: str
    value_K: float
    detail: str

# ---------------------------------------------------------------------------
# Settings — background frameworks
# ---------------------------------------------------------------------------

bcs_theory = setting(
    "Bardeen-Cooper-Schrieffer (BCS) theory: phonon-mediated electron-electron "
    "attraction leads to Cooper pairing instability at the Fermi surface, providing "
    "the fundamental framework for understanding conventional superconductors.",
    title="BCS Theory",
)

# ---------------------------------------------------------------------------
# Claims — leaf nodes (no strategies)
# ---------------------------------------------------------------------------

adiabatic_approx = claim(
    "In conventional metals, the typical phonon frequency (Debye frequency "
    "$\\omega_D$) is much smaller than the electron Fermi energy $E_F$, i.e. "
    "$\\omega_D / E_F \\ll 1$ (adiabatic approximation). This energy-scale "
    "separation has three key consequences: (i) electrons adiabatically adjust "
    "to ionic motion, (ii) the electron-ion coupling can be linearized, and "
    "(iii) the space-time scale separation between electron and phonon physics "
    "permits a controlled effective field theory (EFT) treatment.",
    title="Adiabatic Approximation",
)

me_framework = claim(
    "Migdal-Eliashberg (ME) theory provides a rigorous treatment of the dynamic "
    "electron-phonon interaction. Under the adiabatic condition "
    "$\\omega_D / E_F \\ll 1$, Migdal's theorem guarantees that phonon vertex "
    "corrections are suppressed at $O(\\omega_D/E_F)$, allowing the "
    "electron-phonon self-energy to be truncated at the self-consistent Fock "
    "diagram level. This justifies the ME formalism as a controlled low-energy "
    "theory for electron-phonon superconductors.",
    title="Migdal-Eliashberg Framework",
    metadata={
        "figure": "artifacts/images/4_0.jpg",
        "caption": "Fig. 1 | Normal component of the electron self-energy approximated by the self-consistent Fock diagram with the phonon-mediated e-e interaction W^ph.",
    },
)

deduction(
    premises=[adiabatic_approx],
    conclusion=me_framework,
    background=[bcs_theory],
    reason=(
        "The adiabatic condition $\\omega_D/E_F \\ll 1$ (@adiabatic_approx) "
        "ensures that the ratio of ionic to electronic energy scales is small. "
        "Migdal's theorem then proves that phonon vertex corrections beyond "
        "the self-consistent Fock level are suppressed by $O(\\omega_D/E_F)$, "
        "establishing the Migdal-Eliashberg formalism as a controlled "
        "approximation built on the BCS pairing mechanism (@bcs_theory)."
    ),
    prior=0.97,
)

bts_renormalization = claim(
    "The Bogoliubov-Tolmachev-Shirkov (BTS) renormalization relation connects "
    "the Coulomb pseudopotential $\\mu_{\\omega_c}$ (a dimensionless parameter "
    "describing the effective electron-electron repulsion strength in the "
    "pairing channel) defined at different energy cutoff scales $\\omega_c$: "
    "$\\mu_{\\omega_c} = \\mu_{\\omega_c'} / "
    "(1 + \\mu_{\\omega_c'} \\ln(\\omega_c'/\\omega_c))$. "
    "This relation ensures that physical observables do not depend on the "
    "choice of the arbitrary cutoff scale.",
    title="BTS Renormalization Relation",
)

me_downfolding_is_phenomenological = claim(
    "The downfolding procedure (integrating out high-energy degrees of freedom "
    "to obtain a low-energy effective theory) in traditional Migdal-Eliashberg "
    "(ME) theory is phenomenological: the Coulomb effect is replaced by a "
    "static pseudopotential $\\mu^*$, ignoring corrections from Coulomb "
    "fluctuations to quasiparticle renormalization and electron-phonon "
    "coupling, as well as non-local effects of screening.",
    title="ME Downfolding is Phenomenological",
)

phenomenological_me_theory = claim(
    "Traditional electron-phonon superconductivity theory uses the McMillan "
    "(or Allen-Dynes) formula, with the electron-phonon coupling constant "
    "$\\lambda$ and Coulomb pseudopotential $\\mu^*$ as inputs to predict the "
    "superconducting transition temperature $T_c$. Since $\\mu^*$ cannot be "
    "reliably computed from first principles, it is typically assigned an "
    "empirical value $\\mu^* \\in [0.1, 0.2]$. For materials with $T_c$ in "
    "the sub-kelvin range, the exponential sensitivity "
    "$T_c \\propto \\exp(-1/g)$ to $\\mu^*$ causes this uncertainty to span "
    "several orders of magnitude in the predicted $T_c$, destroying "
    "predictive power.",
    title="Phenomenological ME Theory Limitations",
)

mu_star_phenomenological = claim(
    "Due to the lack of a reliable microscopic calculation, the Coulomb "
    "pseudopotential $\\mu^*$ (a dimensionless parameter describing the "
    "effective Coulomb repulsion strength in the low-energy pairing channel) "
    "is typically treated as an adjustable parameter with empirical values "
    "in the range 0.1--0.2.",
    title="mu* as Phenomenological Parameter",
)

rpa_predicts_attractive_mu = claim(
    "When treating the dynamically screened Coulomb interaction within the "
    "random phase approximation (RPA), the predicted $\\mu^* < 0$ "
    "(i.e. the Coulomb effect becomes net attractive in the Cooper channel) "
    "for Wigner-Seitz radius $r_s \\gtrsim 2$ ($r_s$ is proportional to "
    "the ratio of electron spacing to Bohr radius, measuring the ratio of "
    "Coulomb interaction to kinetic energy). However, RPA neglects "
    "beyond-RPA effects such as vertex corrections and self-energy "
    "renormalization for $r_s \\gtrsim 1$, making its predictions unreliable "
    "in this density regime and inconsistent with extensive experimental "
    "evidence.",
    title="RPA Predicts Attractive mu*",
)

dfpt_computes_lambda = claim(
    "Density functional perturbation theory (DFPT) computes the "
    "electron-phonon coupling constant $\\lambda$ (a dimensionless parameter "
    "quantifying the phonon-mediated attraction strength at the Fermi surface) "
    "via the linear response of the Kohn-Sham ground-state energy to lattice "
    "distortions. DFPT has been validated for weakly correlated superconductors "
    "but its accuracy for strongly correlated systems is unknown.",
    title="DFPT Computes lambda",
)

# ---------------------------------------------------------------------------
# Claims — experimental Tc values
# ---------------------------------------------------------------------------

tc_al_experimental = TcValue(
    material="aluminum (Al)",
    role="experimental",
    structure="",
    value_K=1.2,
    detail="This value is the experimental target used in the Al comparison.",
    title="Tc(Al) Experimental",
)

tc_li_experimental = TcValue(
    material="lithium (Li)",
    role="experimental",
    structure="",
    value_K=4e-4,
    detail=(
        "This value is approximately 0.4 mK and corresponds to the 9R "
        "crystal structure; the crystal structure of lithium at ultra-low "
        "temperatures remains controversial."
    ),
    title="Tc(Li) Experimental",
)

tc_zn_experimental = TcValue(
    material="zinc (Zn)",
    role="experimental",
    structure="",
    value_K=0.875,
    detail="This value is the experimental target used in the Zn comparison.",
    title="Tc(Zn) Experimental",
)

# ---------------------------------------------------------------------------
# Claims — phenomenological Tc predictions
# ---------------------------------------------------------------------------

tc_al_phenomenological = TcValue(
    material="aluminum (Al)",
    role="phenomenological McMillan predicted",
    structure="",
    value_K=1.9,
    detail=(
        "This uses the standard empirical value mu* = 0.1; the experimental "
        "value is 1.2 K, giving a deviation of approximately 58%."
    ),
    title="Tc(Al) Phenomenological Prediction",
)

tc_li_phenomenological = TcValue(
    material="lithium (Li)",
    role="phenomenological McMillan predicted",
    structure="",
    value_K=0.35,
    detail=(
        "This uses mu* = 0.1; the experimental value is approximately "
        "4e-4 K, so the theory overestimates by about three orders of magnitude."
    ),
    title="Tc(Li) Phenomenological Prediction",
)

tc_zn_phenomenological = TcValue(
    material="zinc (Zn)",
    role="phenomenological McMillan predicted",
    structure="",
    value_K=1.37,
    detail=(
        "This uses the standard empirical value mu* = 0.1; the experimental "
        "value is 0.875 K, giving a deviation of approximately 57%."
    ),
    title="Tc(Zn) Phenomenological Prediction",
)

# ---------------------------------------------------------------------------
# Question
# ---------------------------------------------------------------------------

main_question = question(
    "Can the Coulomb pseudopotential $\\mu^*$ (the parameter quantifying "
    "effective electron-electron repulsion in the Cooper pairing channel) "
    "be computed from first principles with controlled accuracy, and can "
    "this yield quantitative predictions of the superconducting transition "
    "temperature $T_c$ for simple metals (e.g. Al, Li, Na, Mg)?",
    title="Main Question: First-Principles mu* and Tc",
)
