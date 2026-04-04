"""Electron-Phonon Coupling

Derives the EFT expression for the electron-phonon vertex, validates the DFPT
approximation for simple metals by analyzing the three-point vertex corrections
via vDiagMC and the Ward identity, and shows that quasiparticle mass renormalization
is close to unity.
"""

from gaia.lang import claim, infer

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
    "The EFT expression for the electron-phonon coupling vertex "
    "$g(k, q) = z^e \\cdot \\Gamma_3^e(k, q) \\cdot g_0(k, q)$ "
    "factorizes the full vertex into a quasiparticle renormalization "
    "factor $z^e$, the electronic three-point vertex correction "
    "$\\Gamma_3^e$, and the bare electron-phonon matrix element $g_0$. "
    "The corresponding $\\lambda$ in the downfolded BSE is the "
    "Fermi-surface average of $|g(k, q)|^2$ weighted by the phonon "
    "propagator.",
    title="EFT Electron-Phonon Vertex",
)

infer(
    premises=[lambda_microscopic_definition],
    conclusion=eft_eph_vertex,
    reason=(
        "The microscopic definition of $\\lambda$ (@lambda_microscopic_definition) "
        "involves the Fermi-surface average of $W^{\\mathrm{ph}}$ weighted by "
        "quasiparticle factors. Expanding $W^{\\mathrm{ph}}$ in terms of the "
        "phonon propagator and electron-phonon vertices, and factoring out the "
        "quasiparticle weight $z^e$ from the pair propagator coherent part, "
        "yields the EFT vertex $g(k,q) = z^e \\cdot \\Gamma_3^e(k,q) \\cdot "
        "g_0(k,q)$. The phonon-mediated interaction then becomes "
        "$W^{\\mathrm{ph}} \\propto |g|^2 D$ where $D$ is the phonon propagator, "
        "and $\\lambda$ is recovered as the Fermi-surface average of this "
        "quantity. This factorization separates the electronic correlation "
        "effects ($z^e$, $\\Gamma_3^e$) from the bare electron-ion coupling "
        "($g_0$) and lattice dynamics ($D$)."
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

infer(
    premises=[ward_identity, gamma3_vdiagmc],
    conclusion=gamma3_approximation,
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

dfpt_reliable_for_simple_metals = claim(
    "For simple metals, the DFPT calculation of the electron-phonon "
    "coupling constant $\\lambda$ is reliable: the product "
    "$z^e \\cdot \\Gamma_3^e \\approx z^e \\cdot m^*/m \\approx 1$ "
    "because $z^e \\approx m/m^*$ and $m^*/m \\approx 1$, so the vertex "
    "corrections and quasiparticle renormalization largely cancel. The "
    "remaining corrections are at the few-percent level, well within "
    "the intrinsic accuracy of DFPT for phonon frequencies and "
    "electron-phonon matrix elements in simple metals.",
    title="DFPT Reliable for Simple Metals",
)

infer(
    premises=[eft_eph_vertex, gamma3_approximation,
              quasiparticle_mass_near_unity],
    conclusion=dfpt_reliable_for_simple_metals,
    background=[dfpt_eph_ansatz, dfpt_computes_lambda],
    reason=(
        "The EFT vertex expression (@eft_eph_vertex) gives "
        "$g = z^e \\cdot \\Gamma_3^e \\cdot g_0$, so $\\lambda \\propto "
        "|z^e \\cdot \\Gamma_3^e|^2 \\cdot \\lambda_0$ where $\\lambda_0$ "
        "is the bare (DFPT-level) coupling. The approximate vertex "
        "(@gamma3_approximation) gives $\\Gamma_3^e \\approx m^*/m$, and "
        "the quasiparticle mass being near unity (@quasiparticle_mass_near_unity) "
        "means $m^*/m \\approx 1$. Since $z^e \\approx m/m^*$ by the Migdal "
        "relation, the product $z^e \\cdot \\Gamma_3^e \\approx "
        "(m/m^*)(m^*/m) = 1$. The DFPT expression (@dfpt_eph_ansatz) "
        "computes $\\lambda$ assuming this product equals unity, which is "
        "precisely what the EFT analysis confirms for simple metals. "
        "DFPT has been independently validated for these systems "
        "(@dfpt_computes_lambda). Therefore DFPT $\\lambda$ values are "
        "reliable for simple metals with corrections at the few-percent level."
    ),
)
