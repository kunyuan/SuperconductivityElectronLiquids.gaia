"""Prior assignments — author-side trust anchors.

Per the v0.5 methodology, prior values are attached only to claims that
carry **explicit prior information** — experimental measurements, exact
mathematical identities, well-established theoretical frameworks, or
high-precision numerical benchmarks — not to author confidence about
derivations or descriptive claims. Every prior set below names the
specific source it draws on via ``source_id`` and a one-sentence
``justification``.

For claims whose reliability depends on a model assumption (e.g. the
vDiagMC numerical results conditional on series convergence, or the
Tc(Li) measurement conditional on the 9R structural identification),
the conditional nature is encoded *structurally* via ``observe(...,
given=premise_claim)`` in the source modules rather than baked into a
single warrant prior here.

Auto-imported by ``gaia build compile``.
"""

from gaia.engine.lang import register_prior

from .motivation import (
    adiabatic_approx,
    bcs_theory,
    tc_al_experimental,
    tc_zn_experimental,
)
from .s5_eph_coupling import quasiparticle_mass_near_unity, ward_identity
from .s6_superconductors import simple_metals_weak_lattice

# ---------------------------------------------------------------------------
# Experimental trust anchors
# ---------------------------------------------------------------------------

register_prior(
    tc_al_experimental,
    0.99,
    source_id="experimental_measurement",
    justification=(
        "Aluminium T_c = 1.2 K is a well-established laboratory value; the "
        "1% residual reserves probability for systematic / structural "
        "qualifications not formalized in this package."
    ),
)

register_prior(
    tc_zn_experimental,
    0.99,
    source_id="experimental_measurement",
    justification=(
        "Zinc T_c = 0.875 K is a well-established laboratory value; the 1% "
        "residual reserves probability for systematic qualifications."
    ),
)

# Note: tc_li_experimental intentionally has no inline prior. The reliability
# of the cited 0.4 mK measurement is conditional on the 9R structural
# identification, which is recorded structurally as
# observe(tc_li_observation_binding, given=(li_crystal_structure_at_low_t,))
# in s6_superconductors.py.

# ---------------------------------------------------------------------------
# Exact mathematical identity
# ---------------------------------------------------------------------------

register_prior(
    ward_identity,
    0.98,
    source_id="qft_exact_identity",
    justification=(
        "The Ward identity is an exact consequence of charge conservation in "
        "QED/QFT; the 2% reserve accounts for the package's framework "
        "assumptions (linearizable e-ion coupling, single-band approximation) "
        "rather than the identity itself."
    ),
)

# ---------------------------------------------------------------------------
# Theoretical frameworks (well-established, taken as background context)
# ---------------------------------------------------------------------------

register_prior(
    bcs_theory,
    0.98,
    source_id="established_theoretical_framework",
    justification=(
        "BCS theory has been the canonical framework for conventional "
        "phonon-mediated superconductors since 1957, with extensive "
        "experimental validation across simple metals, alloys, and elemental "
        "superconductors."
    ),
)

register_prior(
    adiabatic_approx,
    0.95,
    source_id="empirical_physical_scale",
    justification=(
        "For simple metals omega_D / E_F ~ 0.005, satisfying the adiabatic "
        "small-parameter condition by two orders of magnitude. Migdal's "
        "theorem has been validated across the relevant material class."
    ),
)

# ---------------------------------------------------------------------------
# Physical assertions backed by tight numerical benchmarks
# ---------------------------------------------------------------------------

register_prior(
    simple_metals_weak_lattice,
    0.90,
    source_id="empirical_physical_assertion",
    justification=(
        "The nearly-free-electron character of Al, Li, Na, Mg, Zn implies "
        "the spherical-Fermi-surface approximation holds at the few-percent "
        "level; the crystalline mu* differs from the UEG mu* by only a few "
        "percent at matched r_s."
    ),
)

register_prior(
    quasiparticle_mass_near_unity,
    0.92,
    source_id="qmc_numerical_data",
    justification=(
        "High-precision QMC and DiagMC calculations consistently show "
        "|m*/m - 1| < 5-10% for r_s in [2,5]; uncertainty reflects the "
        "spread across independent computations and material-specific band "
        "corrections."
    ),
)
