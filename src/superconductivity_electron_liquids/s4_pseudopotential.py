"""Coulomb Pseudopotential

Addresses the central computational challenge: evaluating the purely electronic
four-point vertex of the uniform electron gas (UEG) via variational diagrammatic
Monte Carlo (vDiagMC), obtaining numerically exact values of mu at the Fermi
energy scale, and confronting the RPA prediction of attractive mu*.
"""

from gaia.lang import claim, contradiction, support

from .motivation import bts_renormalization, rpa_predicts_attractive_mu
from .s3_downfolding import mu_microscopic_definition

# ---------------------------------------------------------------------------
# Leaf claims (no strategies)
# ---------------------------------------------------------------------------

ueg_vertex_challenge = claim(
    "Computing the particle-particle irreducible four-point vertex "
    "$\\tilde\\Gamma^e$ of the uniform electron gas (UEG) is a "
    "long-standing challenge: perturbation theory in the bare Coulomb "
    "interaction diverges for $r_s \\gtrsim 1$, and partial resummations "
    "(RPA, GW) miss crucial vertex corrections. A controlled, systematically "
    "improvable method is needed to evaluate $\\tilde\\Gamma^e$ in the "
    "metallic density range $r_s \\in [1, 6]$.",
    title="UEG Four-Point Vertex Challenge",
)

vdiagmc_method = claim(
    "Variational diagrammatic Monte Carlo (vDiagMC) provides a controlled, "
    "systematically improvable method for computing Feynman diagrammatic "
    "series to high order: (i) bold-line (self-consistent) resummation "
    "avoids infrared divergences in individual diagrams, (ii) stochastic "
    "sampling of diagram topologies and internal variables accesses orders "
    "unreachable by deterministic methods, (iii) the series can be "
    "extrapolated to infinite order with controlled error bars. For the "
    "UEG, vDiagMC achieves reliable convergence of the irreducible vertex "
    "in the metallic density range.",
    title="vDiagMC Method",
)

homotopic_expansion = claim(
    "The homotopic transformation provides a physically motivated "
    "reorganization of the diagrammatic series: by continuously deforming "
    "the bare Coulomb interaction $v(q)$ into a form that incorporates "
    "partial screening at each perturbative order, the series convergence "
    "is dramatically improved. This allows the vDiagMC calculation to "
    "reach converged results for the four-point vertex at metallic "
    "densities with modest diagram orders ($n \\lesssim 7$).",
    title="Homotopic Expansion",
    metadata={
        "figure": "artifacts/images/10_0.jpg",
        "caption": "Fig. 6 | Diagrammatic contributions to the 4-point vertex at first and second order, with Coulomb interaction re-expanded from Yukawa interaction with screening parameter lambda_R.",
    },
)

# ---------------------------------------------------------------------------
# Derived claim
# ---------------------------------------------------------------------------

mu_vdiagmc_values = claim(
    "vDiagMC calculations of the UEG four-point vertex yield the Coulomb "
    "pseudopotential at the Fermi energy scale: $\\mu_{E_F}(r_s)$ is "
    "positive and monotonically increasing with $r_s$ in the metallic "
    "density range, approximately following $\\mu_{E_F} \\approx 0.27\\, r_s$. "
    "The complete set of values (Cai et al., TABLE I), computed at "
    "$\\omega_c = 0.1\\, E_F$ and rescaled to $E_F$ via the BTS relation:\n\n"
    "| $r_s$              | 1       | 2       | 3       | 4        | 5        | 6      |\n"
    "|--------------------|---------|---------|---------|----------|----------|--------|\n"
    "| $\\mu_{0.1\\,E_F}$ | 0.172(4)| 0.238(4)| 0.278(6)| 0.306(15)| 0.328(12)| 0.35(3)|\n"
    "| $\\mu_{E_F}$       | 0.28(1) | 0.53(2) | 0.77(5) | 1.0(2)   | 1.3(2)   | 1.8(8) |\n\n"
    "Numbers in parentheses indicate the systematic uncertainty in the last "
    "digit. These results, combined with the BTS relation, yield "
    "$\\mu^\\ast \\approx 0.12\\text{--}0.18$ at the Debye scale, consistent "
    "with the empirical range but now derived from first principles with "
    "controlled error bars of a few percent. The values are dramatically "
    "larger than the static RPA, Morel-Anderson, and dynamic RPA predictions "
    "for $r_s > 0.5$ — by a factor of three at $r_s = 5$ — and resolve the "
    "long-standing contradiction between phenomenological and RPA-based "
    "treatments of the Coulomb pseudopotential.",
    title="mu from vDiagMC: Numerical Values",
    metadata={
        "figure": "artifacts/images/8_0.jpg",
        "caption": "Fig. 4 | Dimensionless bare Coulomb pseudopotential mu_EF as a function of r_s for the 3D UEG from vDiagMC data, compared with static RPA, Morel-Anderson, and dynamic RPA predictions.",
    },
)

_strat_mu_values = support(
    premises=[vdiagmc_method, homotopic_expansion],
    conclusion=mu_vdiagmc_values,
    background=[ueg_vertex_challenge, mu_microscopic_definition,
                bts_renormalization],
    reason=(
        "The microscopic definition of $\\mu_{\\omega_c}$ "
        "(@mu_microscopic_definition) reduces, for the uniform electron gas, "
        "to evaluating the particle-particle irreducible four-point vertex "
        "$\\tilde\\Gamma^e$ — a notoriously difficult quantity "
        "(@ueg_vertex_challenge). The vDiagMC method (@vdiagmc_method) "
        "provides a controlled, systematically improvable approach by "
        "stochastically sampling Feynman diagrams with bold-line propagators. "
        "The homotopic expansion (@homotopic_expansion) dramatically improves "
        "convergence by reorganizing the series through a continuous deformation "
        "of the bare interaction, enabling convergence at modest diagram orders. "
        "Together, these yield numerically exact values of $\\mu_{E_F}(r_s)$ "
        "with controlled error bars (e.g. $\\mu_{E_F} = 0.53(2)$ at $r_s = 2$). "
        "The BTS renormalization relation (@bts_renormalization) then maps "
        "$\\mu_{E_F}$ down to $\\mu^*$ at the Debye scale, producing values "
        "in the range 0.12--0.18 that are consistent with the empirical range "
        "but now microscopically grounded."
    ),
    prior=0.90,
)

# ---------------------------------------------------------------------------
# Contradiction: RPA attractive mu* vs vDiagMC repulsive mu*
# ---------------------------------------------------------------------------

rpa_vs_vdiagmc = contradiction(
    rpa_predicts_attractive_mu,
    mu_vdiagmc_values,
    reason=(
        "RPA predicts $\\mu^* < 0$ (net attraction) for $r_s \\gtrsim 2$ "
        "(@rpa_predicts_attractive_mu), whereas the vDiagMC calculation "
        "(@mu_vdiagmc_values) finds $\\mu_{E_F}$ positive and monotonically "
        "increasing with $r_s$ throughout the metallic density range, yielding "
        "$\\mu^* > 0$ at all densities. The discrepancy arises because RPA "
        "omits vertex corrections and self-energy effects that, as revealed by "
        "the controlled vDiagMC calculation, substantially increase the "
        "effective Coulomb repulsion in the Cooper channel. The vDiagMC result "
        "is systematically improvable and converged, establishing that the "
        "RPA prediction of attractive $\\mu^*$ is an artifact of the "
        "uncontrolled approximation."
    ),
    prior=0.95,
)
