"""Introduction: Motivation and Background.

Establishes the theoretical context (BCS / Migdal-Eliashberg) and the
phenomenological limitations of traditional approaches to predicting
superconducting Tc, motivating the need for a first-principles treatment
of the Coulomb pseudopotential.
"""

from gaia.engine.lang import claim, derive, exclusive, infer, observe, question

# ---------------------------------------------------------------------------
# Framework claims (axiomatic but probabilistic; carry an inline prior)
# ---------------------------------------------------------------------------

bcs_theory = claim(
    "Bardeen-Cooper-Schrieffer (BCS) theory: phonon-mediated electron-electron "
    "attraction leads to Cooper pairing instability at the Fermi surface, providing "
    "the fundamental framework for understanding conventional superconductors.",
    title="BCS Theory",
)

# ---------------------------------------------------------------------------
# Leaf claims (no derivation; priors carried inline)
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
        "caption": (
            "Fig. 1 | Normal component of the electron self-energy approximated "
            "by the self-consistent Fock diagram with the phonon-mediated e-e "
            "interaction W^ph."
        ),
    },
)

derive(
    me_framework,
    given=(adiabatic_approx,),
    background=[bcs_theory],
    rationale=(
        "The adiabatic condition $\\omega_D/E_F \\ll 1$ (@adiabatic_approx) "
        "ensures that the ratio of ionic to electronic energy scales is small. "
        "Migdal's theorem then proves that phonon vertex corrections beyond "
        "the self-consistent Fock level are suppressed by $O(\\omega_D/E_F)$, "
        "establishing the Migdal-Eliashberg formalism as a controlled "
        "approximation built on the BCS pairing mechanism (@bcs_theory)."
    ),
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

# Three "phenomenological" claims are logically chained, not independent:
# mu_star being a fitted parameter (root) implies the downfolding procedure
# itself is phenomenological (it bakes in a static μ* without microscopic
# anchoring), which together with the exponential Tc sensitivity implies
# the McMillan/Allen-Dynes framework loses predictive power. Without this
# chain the three claims are redundant restatements; wiring them via
# derive() makes the dependency explicit.

derive(
    me_downfolding_is_phenomenological,
    given=(mu_star_phenomenological,),
    rationale=(
        "Because $\\mu^*$ is treated as an empirical adjustable parameter "
        "rather than computed from first principles "
        "(@mu_star_phenomenological), the downfolding procedure in "
        "traditional Migdal-Eliashberg theory is necessarily phenomenological: "
        "the Coulomb effect is replaced by a single static value with no "
        "microscopic underpinning, and corrections from Coulomb fluctuations "
        "to quasiparticle renormalization and electron-phonon coupling are "
        "absent because the phenomenological closure provides no mechanism "
        "to compute them."
    ),
)

derive(
    phenomenological_me_theory,
    given=(me_downfolding_is_phenomenological,),
    rationale=(
        "Given the phenomenological character of the downfolding "
        "(@me_downfolding_is_phenomenological), the resulting McMillan / "
        "Allen-Dynes formula inherits the uncertainty in $\\mu^*$. The "
        "dimensionless coupling $g = \\lambda - \\mu^*(1 + 0.62\\lambda)$ "
        "appears exponentially in $T_c \\propto \\exp(-1/g)$, so the "
        "empirical $\\mu^*$ range $[0.1, 0.2]$ amplifies into orders-of-"
        "magnitude uncertainty in predicted $T_c$ for sub-Kelvin "
        "superconductors — destroying predictive power precisely where "
        "first-principles $\\mu^*$ would matter most."
    ),
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
# Experimental Tc observations
# ---------------------------------------------------------------------------

tc_al_experimental = claim(
    "The experimental superconducting transition temperature of aluminum (Al) "
    "is $T_c^{\\mathrm{exp}} = 1.2$ K.",
    title="Tc(Al) Experimental",
)

tc_li_experimental = claim(
    "The experimental superconducting transition temperature of lithium (Li) "
    "is $T_c^{\\mathrm{exp}} \\approx 4 \\times 10^{-4}$ K (0.4 mK). "
    "This measurement corresponds to the 9R crystal structure.",
    title="Tc(Li) Experimental",
)

tc_zn_experimental = claim(
    "The experimental superconducting transition temperature of zinc (Zn) "
    "is $T_c^{\\mathrm{exp}} = 0.875$ K.",
    title="Tc(Zn) Experimental",
)

# Premise capturing the dominant source of uncertainty in the Li Tc input:
# at ultra-low temperatures the lithium crystal structure (9R vs HCP vs other)
# is debated. The Tc(Li) observation in s6 is therefore declared *conditional*
# on this premise — without an a-priori prior on the premise itself, BP lets
# downstream evidence (Bayes likelihood vs ab initio prediction) decide its
# belief rather than the author handwaving a value.
li_crystal_structure_at_low_t = claim(
    "Lithium's crystal structure at sub-kelvin temperatures is debated. "
    "Measurements consistent with the 9R polytype are typically cited, but "
    "the structural identification at the sample where $T_c \\approx 4 "
    "\\times 10^{-4}$ K was inferred is not independently established. The "
    "Tc(Li) experimental input therefore assumes 9R is the relevant phase.",
    title="Li 9R Structural Assumption at Sub-Kelvin T",
)

# ---------------------------------------------------------------------------
# Li "is it actually superconducting?" discrimination layer.
#
# The lab observed a resistivity drop at ~0.4 mK. There are two competing
# explanations for that datum: a genuine bulk SC transition, or a non-SC
# anomaly (filamentary SC / surface effects / contact artifacts / structural
# transition under sub-mK extreme conditions).  Because the gold-standard
# Meissner-Ochsenfeld experiment has *not* been performed on this sample,
# the latter possibility cannot be ruled out.
#
# Encoded structurally as:
#   (1) two mutually exclusive hypothesis claims (no inline prior),
#   (2) the actual zero-resistance observation pinned via observe(),
#   (3) infer(...) with asymmetric P(e|h)/P(e|¬h) for that evidence,
#       giving a modest Bayes factor (~3x for Li),
#   (4) a *hypothetical* Meissner observation claim with the much stronger
#       BF wired via infer(...) — but NOT observed, so it sits in the
#       graph as a dormant edge ready to be activated if the experiment
#       is ever performed,
#   (5) a question() node recording the open inquiry status.
# ---------------------------------------------------------------------------

li_is_superconducting = claim(
    "Li in the 9R structure undergoes a genuine bulk superconducting "
    "transition at $T_c \\approx 4 \\times 10^{-4}$ K. The Cooper pair "
    "condensate is bulk (not filamentary or surface), and the observed "
    "resistive anomaly reflects this true SC state.",
    title="Li is Bulk Superconducting",
)

li_anomaly_not_sc = claim(
    "The resistive anomaly observed in Li 9R at $\\sim 0.4$ mK is "
    "*not* a bulk superconducting transition: it could be filamentary "
    "SC on grain boundaries / impurity phases, surface superconductivity, "
    "measurement / contact artifacts amplified at sub-mK temperatures, "
    "a structural transition that mimics a SC signature, or another "
    "phenomenon of the extreme sub-mK regime.",
    title="Li Resistive Anomaly Is Not Bulk SC",
)

exclusive(
    li_is_superconducting,
    li_anomaly_not_sc,
    rationale=(
        "A specific sample either undergoes bulk SC or it does not. The "
        "two interpretive hypotheses for the observed resistive anomaly "
        "are mutually exclusive."
    ),
    label="li_sc_hypothesis_exclusive",
)

# Evidence #1: zero resistance was actually measured (observe + infer).
li_zero_resistance_observed = claim(
    "Resistivity of the Li 9R sample drops sharply to below the measurement "
    "noise floor at $T \\approx 0.4$ mK (Schwarz et al. and follow-ups).",
    title="Li Resistance Drop at ~0.4 mK",
)
observe(
    li_zero_resistance_observed,
    background=[li_crystal_structure_at_low_t],
    rationale=(
        "The resistive drop is the actual laboratory observation cited as "
        "evidence for SC in Li at sub-mK temperatures. Pin via observe()."
    ),
    label="li_zero_r_observation",
)

infer(
    li_zero_resistance_observed,
    hypothesis=li_is_superconducting,
    p_e_given_h=0.90,
    p_e_given_not_h=0.30,
    rationale=(
        "Bulk SC almost always (>0.9) produces a sharp resistive drop to "
        "below the noise floor, but in the sub-mK extreme regime the "
        "non-SC alternative (filamentary SC, surface effects, contact "
        "artifacts, structural transitions) can also produce such a "
        "signature with non-negligible probability (~0.3). Bayes factor "
        "~3x supports SC — informative but far from decisive."
    ),
    label="li_zero_r_supports_sc",
)

# Evidence #2: Meissner-Ochsenfeld experiment was NOT performed.
# The claim is declared so the graph contains the structural edge, but
# observe() is deliberately omitted: an unpinned evidence node carries
# no force on BP until someone actually runs the experiment and pins it.
li_meissner_observed = claim(
    "Meissner-Ochsenfeld expulsion of magnetic flux is observed for the "
    "Li 9R sample at sub-K temperatures, confirming bulk SC.",
    title="Li Meissner Observation (hypothetical)",
)

infer(
    li_meissner_observed,
    hypothesis=li_is_superconducting,
    p_e_given_h=0.99,
    p_e_given_not_h=0.005,
    rationale=(
        "Meissner expulsion is essentially unique to bulk SC (BF ~200x). "
        "The structural infer() edge sits in the graph as a dormant "
        "discriminator: while li_meissner_observed remains unpinned the "
        "factor exerts no force on the SC hypothesis posterior. If the "
        "Meissner experiment is performed and observed (positive), simply "
        "add observe(li_meissner_observed) and BP propagates the strong "
        "evidence; if observed null, the factor flips against SC."
    ),
    label="li_meissner_would_support_sc",
)

li_meissner_inquiry = question(
    "Has the Meissner-Ochsenfeld experiment been performed on the Li 9R "
    "sample at sub-K temperatures? This is the gold-standard discriminator "
    "between genuine bulk SC and the various non-SC explanations (BF ~200x "
    "if positive; near-decisive ruling-out if null). The package currently "
    "records no public data on this measurement.",
    targets=[li_meissner_observed, li_is_superconducting, li_anomaly_not_sc],
    title="Missing Meissner Experiment for Li 9R",
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
