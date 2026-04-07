"""The Model and Basic Relations

Establishes the formal field-theoretic framework: the electron-phonon action,
the Bethe-Salpeter equation kernel decomposition, and the precursory Cooper flow
that connects the normal-state four-point vertex to the superconducting Tc.
"""

from gaia.lang import claim, deduction

from .motivation import me_framework

# ---------------------------------------------------------------------------
# Claims
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
    metadata={
        "figure": "artifacts/images/4_1.jpg",
        "caption": "Fig. 2 | Diagrammatic representation of the phonon-mediated e-e interaction W^ph, composed of phonon propagator D, bare coupling g^(0), vertex function Gamma_3^e, and dielectric function.",
    },
)

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
    metadata={
        "figure": "artifacts/images/4_2.jpg",
        "caption": "Fig. 3 | Self-consistent Bethe-Salpeter equation for the anomalous vertex in momentum space, with kernel consisting of the electronic four-point vertex Gamma_e and phonon-mediated interaction W^ph.",
    },
)

deduction(
    premises=[me_framework],
    conclusion=bse_kernel_decomposition,
    reason=(
        "Migdal's theorem (@me_framework) guarantees that phonon vertex "
        "corrections to the BSE kernel are suppressed at $O(\\omega_D/E_F)$. "
        "This allows the full particle-particle irreducible kernel to be "
        "separated into a purely electronic four-point vertex $\\tilde\\Gamma^e$ "
        "(which encodes all non-perturbative Coulomb correlations and is "
        "independent of phonon details) and the phonon-mediated interaction "
        "$W^{\\mathrm{ph}}$ (which includes the dressed phonon propagator, "
        "bare coupling, electronic screening, and vertex corrections). "
        "Cross terms between these two contributions are higher order in "
        "$\\omega_D/E_F$ and can be neglected."
    ),
)

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
