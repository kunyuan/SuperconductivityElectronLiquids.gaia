"""The Model and Basic Relations

Establishes the formal field-theoretic framework: the electron-phonon action,
the Bethe-Salpeter equation kernel decomposition, and the precursory Cooper flow
that connects the normal-state four-point vertex to the superconducting Tc.
"""

from gaia.lang import claim

# ---------------------------------------------------------------------------
# Claims — all leaf nodes (no strategies)
# ---------------------------------------------------------------------------

electron_phonon_action = claim(
    "The effective action of the electron-phonon coupled system can be "
    "decomposed as $S = S_e + S_{\\mathrm{ph}} + S_{e\\text{-ph}} + "
    "S_{\\mathrm{CT}} + O(\\sqrt{m/M})$, where $m$ is the electron mass "
    "and $M$ is the ion mass. $S_e$ is the complete many-electron action "
    "without any approximation, $S_{\\mathrm{ph}}$ describes phonons with "
    "physical dispersion, $S_{e\\text{-ph}}$ is the coupling between "
    "electron density and ionic displacement, and $S_{\\mathrm{CT}}$ is a "
    "counterterm that subtracts the static electron polarization contribution "
    "already included in the physical phonon dispersion to prevent double "
    "counting.",
    title="Electron-Phonon Action Decomposition",
)
electron_phonon_action.label = "electron_phonon_action"

bse_kernel_decomposition = claim(
    "The kernel of the Bethe-Salpeter equation (BSE) can be decomposed into "
    "the purely electronic particle-particle irreducible four-point vertex "
    "$\\tilde\\Gamma^e$ (encoding all non-perturbative Coulomb effects) and "
    "the phonon-mediated effective electron-electron interaction "
    "$W^{\\mathrm{ph}}$: $\\tilde\\Gamma = \\tilde\\Gamma^e + "
    "W^{\\mathrm{ph}} + O(\\omega_D/E_F)$. Migdal's theorem ensures that "
    "higher-order phonon vertex corrections are suppressed by the adiabatic "
    "small parameter.",
    title="BSE Kernel Decomposition",
)
bse_kernel_decomposition.label = "bse_kernel_decomposition"

precursory_cooper_flow = claim(
    "The low-frequency limit of the anomalous vertex function on the Fermi "
    "surface $\\Lambda_0$ obeys a universal scaling relation (precursory "
    "Cooper flow, PCF): $\\Lambda_0 = 1/(1 + g\\ln(\\omega_\\Lambda/T)) "
    "+ O(T)$, where $g$ is the dimensionless coupling constant ($g < 0$ "
    "corresponds to net attraction) and $\\omega_\\Lambda$ is an effective "
    "high-energy cutoff. When $g < 0$, $\\Lambda_0$ diverges at "
    "$T_c = \\omega_\\Lambda e^{1/g}$; by computing in the normal state "
    "and extrapolating, one can predict $T_c$.",
    title="Precursory Cooper Flow",
)
precursory_cooper_flow.label = "precursory_cooper_flow"
