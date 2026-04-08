"""Electron-Phonon Coupling

Derives the EFT expression for the electron-phonon vertex, validates the DFPT
approximation for simple metals by analyzing the three-point vertex corrections
via vDiagMC and the Ward identity, and shows that quasiparticle mass renormalization
is close to unity.
"""

from gaia.lang import claim, composite, deduction, induction, noisy_and

from .motivation import dfpt_computes_lambda
from .s3_downfolding import lambda_microscopic_definition

# ---------------------------------------------------------------------------
# Leaf claims (no strategies)
# ---------------------------------------------------------------------------

ward_identity = claim(
    "An exact Ward identity relates the three-point electron-phonon vertex "
    "$\\Gamma_3^e(k, q)$ to the electron self-energy in the long-wavelength "
    "limit $q \\to 0$: $\\lim_{q \\to 0} \\Gamma_3^e(k, q) = 1 - "
    "\\partial\\Sigma(k)/\\partial\\epsilon_k$. This identity is a "
    "consequence of charge conservation and provides an exact constraint "
    "on vertex corrections at zero momentum transfer.",
    title="Ward Identity at q->0",
)

gamma3_vdiagmc = claim(
    "vDiagMC computation of the three-point vertex $\\Gamma_3^e(k, q)$ of "
    "the UEG at finite momentum transfer $q$ shows that vertex corrections "
    "are modest (10--20% level) for momenta within the Fermi sphere "
    "($|k|, |k+q| \\lesssim k_F$) at metallic densities $r_s \\in [2, 4]$. "
    "The corrections vary smoothly with $q$ and can be accurately "
    "interpolated between the Ward-identity limit ($q \\to 0$) and "
    "the large-$q$ asymptotic behavior.",
    title="vDiagMC Computation of Gamma_3",
    metadata={
        "figure": "artifacts/images/12_0.jpg",
        "caption": "Fig. 8 | Comparison between the angle-resolved e-ph vertex correction in the UEG from vDiagMC (points) and DFPT (lines) for different r_s values.",
    },
)

dfpt_eph_ansatz = claim(
    "The DFPT expression for the electron-phonon coupling "
    "$g^{\\mathrm{DFPT}}(k, q) = \\sqrt{\\omega_q / 2} \\, "
    "\\langle k+q | \\delta V_{\\mathrm{KS}} / \\delta u_q | k \\rangle$ "
    "implicitly assumes that vertex corrections to the electron-phonon "
    "coupling beyond the Kohn-Sham mean-field level are absorbed into the "
    "exchange-correlation functional. The accuracy of this ansatz depends "
    "on how well DFT captures the relevant vertex corrections.",
    title="DFPT Expression for e-ph Coupling",
)

quasiparticle_mass_near_unity = claim(
    "For simple metals at metallic densities ($r_s \\in [2, 4]$), the "
    "quasiparticle effective mass ratio $m^*/m \\approx 1$ (deviations "
    "less than 5--10%). This near-unity mass ratio means that the "
    "quasiparticle renormalization factor $z^e \\approx 1/(1 + \\lambda_e)$ "
    "primarily reflects the frequency-dependent self-energy rather than "
    "momentum-dependent mass enhancement, simplifying the mapping between "
    "microscopic and DFPT-level electron-phonon coupling.",
    title="Quasiparticle Mass Near Unity",
)

# ---------------------------------------------------------------------------
# Derived claims
# ---------------------------------------------------------------------------

eft_eph_vertex = claim(
    "The EFT expression for the physical electron-phonon coupling vertex "
    "factorizes the bare coupling into a screening factor and vertex/"
    "quasiparticle renormalizations (Cai et al., Eq. 32):\n\n"
    "$$g_\\kappa(\\mathbf{k}, \\mathbf{q}) "
    "= g_{\\kappa\\mathbf{q}}^{(0)}\\, \\frac{z^e}{\\epsilon_\\mathbf{q}}\\, "
    "\\Gamma_3^e(\\mathbf{k}, \\mathbf{q}),$$\n\n"
    "where $g_{\\kappa\\mathbf{q}}^{(0)}$ is the bare e-ph matrix element, "
    "$\\epsilon_\\mathbf{q}$ is the electronic dielectric function, $z^e$ "
    "is the electronic quasiparticle weight, and $\\Gamma_3^e(\\mathbf{k}, "
    "\\mathbf{q})$ is the electronic three-point vertex correction. The "
    "combination $z^e \\Gamma_3^e(\\mathbf{k}, \\mathbf{q})$ can be "
    "interpreted as the quasiparticle vertex correction to the screened "
    "interaction. The corresponding $\\lambda$ in the downfolded BSE is "
    "the Fermi-surface average of $|g_\\kappa(\\mathbf{k}, \\mathbf{q})|^2 "
    "/ \\omega_{\\kappa,\\mathbf{q}}^2$ over phonon branches "
    "(see @lambda_microscopic_definition).",
    title="EFT Electron-Phonon Vertex",
)

# deduction: λ microscopic definition → EFT vertex expression
deduction(
    premises=[lambda_microscopic_definition],
    conclusion=eft_eph_vertex,
    reason=(
        "The microscopic definition of $\\lambda$ (@lambda_microscopic_definition) "
        "involves the Fermi-surface average of $W^{\\mathrm{ph}}$ weighted by "
        "quasiparticle factors. Expanding $W^{\\mathrm{ph}}$ in terms of the "
        "phonon propagator and electron-phonon vertices, and factoring out the "
        "quasiparticle weight $z^e$ from the pair propagator coherent part, "
        "yields the EFT vertex $g(k,q) = z^e \\cdot \\Gamma_3^e(k,q) \\cdot "
        "g_0(k,q)$."
    ),
)

gamma3_approximation = claim(
    "The three-point vertex $\\Gamma_3^e(k, q)$ for states within the "
    "Fermi sphere can be accurately approximated by interpolation between "
    "two controlled limits: (i) the exact Ward identity at $q \\to 0$ "
    "giving $\\Gamma_3^e = 1 - \\partial\\Sigma/\\partial\\epsilon_k = "
    "m^*/m$, and (ii) the vDiagMC results at finite $q$ showing smooth, "
    "modest variations. For simple metals, this yields "
    "$\\Gamma_3^e \\approx m^*/m$ to within 10--15% across the relevant "
    "momentum range.",
    title="Approximate Gamma_3 within Fermi Sphere",
)

_induction_gamma3 = induction(
    [ward_identity, gamma3_vdiagmc],
    gamma3_approximation,
    reason=(
        "The Ward identity (@ward_identity) provides the exact value of "
        "$\\Gamma_3^e$ at $q = 0$: $\\Gamma_3^e(k, 0) = m^*/m$. The vDiagMC "
        "computation (@gamma3_vdiagmc) shows that at finite $q$ within the "
        "Fermi sphere, vertex corrections remain modest (10--20%) and vary "
        "smoothly with momentum. By interpolating between the exact $q = 0$ "
        "constraint and the numerically determined finite-$q$ behavior, we "
        "obtain a reliable approximation $\\Gamma_3^e \\approx m^*/m$ that "
        "captures the dominant effect (mass renormalization) while bounding "
        "the error from momentum dependence at the 10--15% level."
    ),
)

# Intermediate claim for composite decomposition
eft_vertex_matches_dfpt = claim(
    "In the uniform electron gas at densities $r_s \\in [1,5]$, the "
    "EFT electron-phonon vertex $g(\\mathbf{k},\\mathbf{q}) = "
    "g^{(0)}_{\\mathbf{q}} \\cdot (z^e/\\epsilon_{\\mathbf{q}}) \\cdot "
    "\\Gamma_3^e(\\mathbf{k};\\mathbf{q})$ is numerically well "
    "approximated by the DFPT Kohn-Sham screened potential "
    "$g^{\\mathrm{KS}}(\\mathbf{q}) = g^{(0)}_{\\mathbf{q}} / "
    "[1 - (v_{\\mathbf{q}} + f_{xc})\\chi_0^e(\\mathbf{q})]$ "
    "for Fermi-surface-relevant momentum transfers $|\\mathbf{q}| "
    "\\leq 2k_F$, with weak residual $\\mathbf{k}$-dependence.",
    title="EFT Vertex Matches DFPT",
)

dfpt_reliable_for_simple_metals = claim(
    "For simple metals, the DFPT calculation of the electron-phonon "
    "coupling constant $\\lambda$ is reliable: the EFT vertex matches "
    "the DFPT expression at the vertex level, and the quasiparticle "
    "density of states $N_F^*$ nearly equals the band density of states "
    "$N_F^{(0)}$, so $\\lambda_{\\mathrm{EFT}} \\approx "
    "\\lambda_{\\mathrm{DFPT}}$ with corrections at the few-percent level.",
    title="DFPT Reliable for Simple Metals",
)

# Sub-step 1: EFT vertex + Γ₃ approximation → vertex-level match
_s1 = deduction(
    premises=[eft_eph_vertex, gamma3_approximation],
    conclusion=eft_vertex_matches_dfpt,
    background=[dfpt_eph_ansatz],
    reason=(
        "Substituting the approximate $\\Gamma_3^e \\approx m^*/m$ "
        "(@gamma3_approximation) into the EFT vertex expression "
        "(@eft_eph_vertex) $g = z^e \\cdot \\Gamma_3^e \\cdot g_0$, "
        "and using the Migdal relation $z^e \\approx m/m^*$, the product "
        "$z^e \\cdot \\Gamma_3^e \\approx (m/m^*)(m^*/m) = 1$. "
        "This means $g(k,q) \\approx g_0(k,q)$, which after screening "
        "gives exactly the DFPT Kohn-Sham expression (@dfpt_eph_ansatz) "
        "$g^{\\mathrm{KS}}(q)$. The vertex-level agreement holds for "
        "$|q| \\leq 2k_F$ with weak residual $k$-dependence."
    ),
)

# Sub-step 2: vertex match + mass near unity → λ match
_s2 = deduction(
    premises=[eft_vertex_matches_dfpt, quasiparticle_mass_near_unity],
    conclusion=dfpt_reliable_for_simple_metals,
    background=[dfpt_computes_lambda],
    reason=(
        "The vertex-level agreement $g \\approx g^{\\mathrm{KS}}$ "
        "(@eft_vertex_matches_dfpt) ensures the electron-phonon matrix "
        "elements match. To obtain $\\lambda$, these must be combined with "
        "the density of states: EFT uses the quasiparticle $N_F^*$ while "
        "DFPT (@dfpt_computes_lambda) uses the band $N_F^{(0)}$. Since "
        "$m^*/m \\approx 1$ (@quasiparticle_mass_near_unity), we have "
        "$N_F^* \\approx N_F^{(0)}$, and therefore "
        "$\\lambda_{\\mathrm{EFT}} \\approx \\lambda_{\\mathrm{DFPT}}$."
    ),
)

# Composite: preserves coarse view (3 premises → conclusion)
_composite_dfpt = composite(
    premises=[eft_eph_vertex, gamma3_approximation,
              quasiparticle_mass_near_unity],
    conclusion=dfpt_reliable_for_simple_metals,
    sub_strategies=[_s1, _s2],
)
