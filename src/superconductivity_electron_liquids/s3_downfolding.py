"""Downfolding the Bethe-Salpeter Equation

Derives the frequency-only downfolded BSE by decomposing the pair propagator
into coherent and incoherent parts, showing cross-channel terms are suppressed,
and obtaining microscopic definitions for lambda and mu. Validates the
downfolding against a full BSE toy-model calculation.
"""

from gaia.lang import abduction, claim, deduction, equivalence, noisy_and, setting

from .motivation import (
    adiabatic_approx,
    bts_renormalization,
    me_framework,
    mu_star_phenomenological,
)
from .s2_model import bse_kernel_decomposition, electron_phonon_action, precursory_cooper_flow

# ---------------------------------------------------------------------------
# Leaf claims (no strategies)
# ---------------------------------------------------------------------------

pair_propagator_decomposition = setting(
    "The pair propagator (product of two single-particle Green's functions "
    "$G_{k\\omega}G_{-k,-\\omega}$) can be exactly decomposed into a "
    "low-energy coherent part $\\Pi_{\\mathrm{BCS}}$ and a high-energy "
    "incoherent remainder $\\phi_{k\\omega}$: "
    "$G_{k\\omega}G_{-k,-\\omega} = \\Pi_{\\mathrm{BCS}} + \\phi_{k\\omega}$. "
    "The coherent part is expressed in terms of the quasiparticle weight "
    "$z^e$, frequency-dependent quasiparticle weight "
    "$z_\\omega^{\\mathrm{ph}}$, and renormalized dispersion $\\epsilon_k$. "
    "This is an exact mathematical identity introducing energy-scale "
    "separation in the two-electron channel.",
    title="Pair Propagator Decomposition",
)

cross_term_suppressed = claim(
    "Cross terms mixing Coulomb and phonon channels are suppressed by the "
    "plasma frequency $\\omega_p$, at order $O(\\omega_c^2/\\omega_p^2)$, "
    "where $\\omega_c$ is an intermediate energy cutoff satisfying "
    "$\\omega_D \\ll \\omega_c \\ll E_F$. For most three-dimensional metals "
    "$\\omega_c/\\omega_p \\lesssim 0.1$, so cross terms contribute no more "
    "than 1%.",
    title="Cross-Channel Terms Suppressed",
)

rpa_dynamic_screening = setting(
    "Random Phase Approximation (RPA) dynamically screened Coulomb interaction: "
    "$W_{\\mathrm{RPA}}(\\mathbf{q},\\nu) = v_q / (1 - v_q \\Pi^0_{\\mathbf{q}\\nu})$, "
    "where $v_q = 4\\pi e^2/q^2$ is the bare Coulomb potential and $\\Pi^0$ is "
    "the non-interacting polarization function. This is a standard approximation "
    "that becomes exact in the weak-coupling limit ($r_s \\lesssim 1$).",
    title="RPA Dynamic Screening",
)

full_bse_toy_model = claim(
    "For a toy model with aluminum-like parameters (Wigner-Seitz radius "
    "$r_s = 1.92$, adiabatic ratio $\\omega_D/E_F = 0.005$), numerically "
    "solving the full frequency-momentum dependent Bethe-Salpeter equation "
    "(BSE) — using RPA dynamically screened Coulomb interaction as the "
    "electron irreducible vertex plus a model phonon interaction, without any "
    "downfolding approximation — yields a superconducting transition temperature "
    "$T_c^{\\mathrm{full}}/T_F = 10^{-5.668}$, where $T_F$ is the Fermi "
    "temperature.",
    title="Full BSE Toy Model Result",
)

_strat_full_bse = noisy_and(
    premises=[bse_kernel_decomposition],
    conclusion=full_bse_toy_model,
    background=[rpa_dynamic_screening],
    reason=(
        "Using the Bethe-Salpeter equation with the kernel decomposition "
        "(@bse_kernel_decomposition) into the electronic four-point vertex "
        "(approximated by RPA dynamically screened Coulomb interaction, "
        "@rpa_dynamic_screening) and a model phonon-mediated interaction, "
        "numerically solve the full frequency-momentum BSE for a toy model "
        "at $r_s = 1.92$, $\\omega_D/E_F = 0.005$. The precursory Cooper "
        "flow analysis of the solution yields "
        "$T_c^{\\mathrm{full}}/T_F = 10^{-5.668}$."
    ),
)

downfolded_bse_toy_model = claim(
    "For the same toy model (aluminum-like parameters $r_s = 1.92$, "
    "$\\omega_D/E_F = 0.005$), solving the downfolded frequency-only "
    "Bethe-Salpeter equation yields $T_c^{\\mathrm{approx}}/T_F = "
    "10^{-5.667}$, where $T_F$ is the Fermi temperature.",
    title="Downfolded BSE Toy Model Result",
)

# Note: downfolded_bse is defined below; Python forward reference via module-level execution
# We use a lambda trick or define this infer after downfolded_bse. Moving to after downfolded_bse.

_abduction_downfolding = abduction(
    observation=full_bse_toy_model,
    hypothesis=downfolded_bse_toy_model,
    reason=(
        "The full BSE numerical solution gives "
        "$T_c^{\\mathrm{full}}/T_F = 10^{-5.668}$ (@full_bse_toy_model), "
        "while the downfolded BSE gives "
        "$T_c^{\\mathrm{approx}}/T_F = 10^{-5.667}$ "
        "(@downfolded_bse_toy_model). The two differ by only 0.2%, "
        "demonstrating that the downfolding approximation is quantitatively "
        "accurate for conventional metal parameters."
    ),
)

downfolding_validity_limits = claim(
    "The downfolded EFT-ME framework's applicability conditions and failure "
    "modes: (i) the adiabatic parameter $\\omega_D/E_F \\ll 1$ must hold, "
    "(ii) the intermediate cutoff $\\omega_c$ must satisfy "
    "$\\omega_D \\ll \\omega_c \\ll E_F$ with $\\omega_c/\\omega_p \\ll 1$, "
    "and (iii) the framework breaks down for strongly non-adiabatic systems "
    "(e.g. high-$T_c$ hydrides where $\\omega_D/E_F \\sim 0.1$) and for "
    "strongly correlated materials where the quasiparticle picture fails.",
    title="Downfolding Validity Limits",
)

# ---------------------------------------------------------------------------
# Derived claims (with infer strategies)
# ---------------------------------------------------------------------------

downfolded_bse = claim(
    "The frequency-only downfolded Bethe-Salpeter equation: the full "
    "momentum-frequency BSE kernel reduces to a one-dimensional integral "
    "equation in Matsubara frequency, with an effective kernel "
    "$K(\\omega, \\omega') = \\lambda(\\omega, \\omega') - "
    "\\mu_{\\omega_c}(\\omega, \\omega')$, where the phonon-mediated "
    "attraction $\\lambda$ and Coulomb pseudopotential $\\mu_{\\omega_c}$ "
    "are microscopically defined. The momentum integration is absorbed into "
    "the density of states, and the pair propagator's coherent part "
    "generates the BCS logarithm that drives the Cooper instability.",
    title="Downfolded BSE",
)

deduction(
    premises=[cross_term_suppressed, bse_kernel_decomposition],
    conclusion=downfolded_bse,
    background=[pair_propagator_decomposition, adiabatic_approx],
    reason=(
        "Starting from the full BSE with kernel decomposed into "
        "$\\tilde\\Gamma^e + W^{\\mathrm{ph}}$ (@bse_kernel_decomposition), "
        "we substitute the exact pair propagator decomposition "
        "(@pair_propagator_decomposition) which splits $GG$ into a BCS-like "
        "coherent piece $\\Pi_{\\mathrm{BCS}}$ and an incoherent remainder "
        "$\\phi$. The coherent piece carries the Cooper logarithm and defines "
        "the low-energy pairing channel. Momentum summation over the coherent "
        "part yields a frequency-only kernel. The cross terms mixing Coulomb "
        "and phonon channels are suppressed at $O(\\omega_c^2/\\omega_p^2)$ "
        "(@cross_term_suppressed), justifying their neglect. Under the "
        "adiabatic condition (@adiabatic_approx), residual phonon vertex "
        "corrections are negligible. The result is a one-dimensional integral "
        "equation in Matsubara frequency with microscopically defined "
        "$\\lambda$ and $\\mu_{\\omega_c}$ kernels."
    ),
)

# Now that downfolded_bse is defined, attach noisy_and for the toy model result
_strat_downfolded_bse_toy = noisy_and(
    premises=[downfolded_bse],
    conclusion=downfolded_bse_toy_model,
    background=[rpa_dynamic_screening],
    reason=(
        "Apply the downfolded frequency-only BSE (@downfolded_bse) to the same "
        "toy model (RPA dynamically screened Coulomb interaction "
        "@rpa_dynamic_screening, $r_s = 1.92$, $\\omega_D/E_F = 0.005$). "
        "Solving the frequency-only equation yields "
        "$T_c^{\\mathrm{approx}}/T_F = 10^{-5.667}$."
    ),
)

downfolded_me_equation = claim(
    "At the superconducting critical temperature $T_c$, the downfolded "
    "Bethe-Salpeter equation reduces to the traditional linearized "
    "Migdal-Eliashberg (ME) gap equation: $\\Delta_\\omega = \\pi T_c "
    "\\sum_{|\\omega'|<\\omega_c} (\\lambda_{\\omega\\omega'} - \\mu^*) "
    "\\frac{z_{\\omega'}^{\\mathrm{ph}}}{|\\omega'|} \\Delta_{\\omega'}$. "
    "As $T \\to T_c$, the anomalous vertex diverges as "
    "$\\Lambda_{k\\omega} \\sim \\Delta_{k\\omega}/(T - T_c)$, causing the "
    "source term $\\eta$ to become irrelevant. The diverging prefactor "
    "$(T - T_c)^{-1}$ cancels between the two sides of the equation, "
    "yielding the gap equation with $\\mu^* \\equiv \\mu_{\\omega_c}$. "
    "This establishes the microscopic foundation for the ME equation "
    "with precise definitions of $\\mu^*$ and $\\lambda$ in terms of "
    "electron vertex functions.",
    title="Downfolded ME Gap Equation",
)

deduction(
    premises=[downfolded_bse],
    conclusion=downfolded_me_equation,
    background=[precursory_cooper_flow],
    reason=(
        "Starting from the downfolded BSE (@downfolded_bse), consider the "
        "behavior near the Cooper instability. The precursory Cooper flow "
        "(@precursory_cooper_flow) shows that the anomalous vertex diverges "
        "as $\\Lambda \\sim \\Delta/(T - T_c)$ when $T \\to T_c$. "
        "Substituting this scaling into the downfolded BSE, the source "
        "term $\\eta$ becomes negligible compared to the diverging vertex, "
        "and the $(T - T_c)^{-1}$ prefactor cancels on both sides. "
        "The result is the linearized gap equation — identical in form to "
        "the traditional ME equation, but now with $\\mu^*$ and $\\lambda$ "
        "having precise microscopic definitions from the downfolding."
    ),
)

lambda_microscopic_definition = claim(
    "The electron-phonon coupling $\\lambda(\\omega, \\omega')$ in the "
    "downfolded BSE has a microscopic definition: it is the Fermi-surface "
    "average of the phonon-mediated interaction $W^{\\mathrm{ph}}$ weighted "
    "by quasiparticle renormalization factors $z^e$ and $z_\\omega^{\\mathrm{ph}}$. "
    "This definition reduces to the standard Eliashberg $\\lambda$ in the "
    "adiabatic limit but retains dynamical corrections from the electron "
    "self-energy.",
    title="Microscopic Definition of lambda",
)

deduction(
    premises=[downfolded_bse],
    conclusion=lambda_microscopic_definition,
    background=[electron_phonon_action],
    reason=(
        "The downfolded BSE (@downfolded_bse) expresses the pairing kernel "
        "as $K = \\lambda - \\mu_{\\omega_c}$. The phonon-mediated part "
        "$\\lambda(\\omega, \\omega')$ arises from projecting $W^{\\mathrm{ph}}$ "
        "(the phonon-mediated interaction from the electron-phonon action "
        "decomposition, @electron_phonon_action) onto the Fermi surface using "
        "the coherent part of the pair propagator. The counterterm "
        "$S_{\\mathrm{CT}}$ in the action ensures no double-counting of the "
        "static screening already included in the physical phonon dispersion. "
        "The resulting expression for $\\lambda$ involves the Fermi-surface "
        "average of $W^{\\mathrm{ph}}$ weighted by quasiparticle factors, "
        "providing a controlled microscopic definition that generalizes the "
        "standard Eliashberg coupling constant."
    ),
)

mu_microscopic_definition = claim(
    "The Coulomb pseudopotential $\\mu_{\\omega_c}(\\omega, \\omega')$ in the "
    "downfolded BSE has a microscopic definition: it is determined by the "
    "purely electronic particle-particle irreducible four-point vertex "
    "$\\tilde\\Gamma^e$ projected onto the Fermi surface, with the high-energy "
    "electronic degrees of freedom integrated out above the cutoff "
    "$\\omega_c$. This gives $\\mu_{\\omega_c}$ a precise meaning as the "
    "effective Coulomb repulsion in the low-energy pairing channel, "
    "renormalized by all electronic correlations.",
    title="Microscopic Definition of mu",
)

deduction(
    premises=[downfolded_bse],
    conclusion=mu_microscopic_definition,
    reason=(
        "The downfolded BSE (@downfolded_bse) separates the pairing kernel "
        "into phonon ($\\lambda$) and Coulomb ($\\mu_{\\omega_c}$) contributions. "
        "The Coulomb part is obtained by projecting the purely electronic "
        "irreducible four-point vertex $\\tilde\\Gamma^e$ from the BSE kernel "
        "onto the Fermi surface, with frequency integration restricted to the "
        "range above $\\omega_c$ handled by the incoherent part of the pair "
        "propagator. This construction defines $\\mu_{\\omega_c}$ as a "
        "functional of $\\tilde\\Gamma^e$ — the quantity that encodes all "
        "non-perturbative Coulomb correlations — evaluated at a specific "
        "energy scale, without any phenomenological input."
    ),
)

mu_scale_independence = claim(
    "The BTS renormalization relation $\\mu_{\\omega_c} = \\mu_{\\omega_c'} / "
    "(1 + \\mu_{\\omega_c'} \\ln(\\omega_c'/\\omega_c))$ emerges as a "
    "corollary of the microscopic definition of $\\mu_{\\omega_c}$: changing "
    "the cutoff $\\omega_c$ reshuffles contributions between the explicit "
    "Coulomb kernel and the Cooper logarithm in the BCS propagator, leaving "
    "the physical $T_c$ invariant. This provides a microscopic derivation "
    "of the originally phenomenological BTS relation.",
    title="BTS Relation as Corollary",
)

deduction(
    premises=[mu_microscopic_definition],
    conclusion=mu_scale_independence,
    reason=(
        "Given the microscopic definition of $\\mu_{\\omega_c}$ "
        "(@mu_microscopic_definition) as a Fermi-surface projection of "
        "$\\tilde\\Gamma^e$ with a cutoff at $\\omega_c$, we can examine "
        "how $\\mu$ transforms when $\\omega_c$ is varied. Shifting the "
        "cutoff from $\\omega_c'$ to $\\omega_c$ transfers spectral weight "
        "between the explicit Coulomb kernel and the BCS Cooper logarithm "
        "$\\ln(\\omega_c'/T)$ in the coherent pair propagator. Requiring "
        "that the physical observable ($T_c$) remain invariant under this "
        "reshuffling yields the BTS relation "
        "$\\mu_{\\omega_c} = \\mu_{\\omega_c'} / "
        "(1 + \\mu_{\\omega_c'} \\ln(\\omega_c'/\\omega_c))$ "
        "as an exact consequence of the downfolded theory's structure, "
        "rather than an ad hoc ansatz."
    ),
)

bts_microscopic_equivalence = equivalence(
    mu_scale_independence,
    bts_renormalization,
    reason=(
        "The microscopically derived scale-independence relation "
        "(@mu_scale_independence) and the historically known "
        "Bogoliubov-Tolmachev-Shirkov renormalization relation "
        "(@bts_renormalization) express the same mathematical identity: "
        "$\\mu_{\\omega_c} = \\mu_{\\omega_c'}/(1 + \\mu_{\\omega_c'}"
        "\\ln(\\omega_c'/\\omega_c))$. The present work provides a "
        "microscopic derivation of this relation from the downfolded BSE "
        "structure, establishing it as an exact consequence of the theory "
        "rather than a phenomenological ansatz."
    ),
)

ma_pseudopotential_justified = claim(
    "The Morel-Anderson constant-pseudopotential ansatz — treating "
    "$\\mu_{\\omega_c}$ as approximately frequency-independent — is "
    "microscopically justified: the four-point vertex $\\tilde\\Gamma^e$ "
    "varies on electronic energy scales ($E_F$), which are much larger "
    "than the phonon scale ($\\omega_D$). Within the low-energy window "
    "$|\\omega|, |\\omega'| < \\omega_c \\ll E_F$, the Coulomb kernel is "
    "effectively constant, validating the traditional constant-$\\mu^*$ "
    "treatment used in Eliashberg theory.",
    title="Morel-Anderson Ansatz Justified",
)

deduction(
    premises=[mu_microscopic_definition],
    conclusion=ma_pseudopotential_justified,
    background=[mu_star_phenomenological],
    reason=(
        "The microscopic definition of $\\mu_{\\omega_c}$ "
        "(@mu_microscopic_definition) shows it is determined by the "
        "electronic four-point vertex $\\tilde\\Gamma^e$, which varies on "
        "the scale of $E_F$. Within the low-energy window "
        "$|\\omega|, |\\omega'| < \\omega_c$ where $\\omega_c \\ll E_F$, "
        "the frequency dependence of $\\tilde\\Gamma^e$ is negligible, "
        "so $\\mu_{\\omega_c}(\\omega, \\omega') \\approx \\mu_{\\omega_c}$ "
        "becomes effectively a constant. This provides a first-principles "
        "justification for the phenomenological Morel-Anderson ansatz "
        "(@mu_star_phenomenological) that treats $\\mu^*$ as a single number "
        "rather than a frequency-dependent kernel. The justification holds "
        "precisely because the energy-scale hierarchy $\\omega_c \\ll E_F$ "
        "is maintained."
    ),
)
