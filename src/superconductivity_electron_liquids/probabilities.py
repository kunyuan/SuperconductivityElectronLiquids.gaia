"""Numerical layer: McMillan formula + per-material parameters + propagated moments.

This module is the bridge between the qualitative DSL (claim/derive) and the
quantitative Bayes layer (:mod:`gaia.engine.bayes`).  It exposes:

* :func:`mcmillan_tc` — the closed-form Allen-Dynes / McMillan estimator
  ``T_c(λ, μ*, ω_log)``.
* ``MATERIAL_PARAMS`` — per-material ``λ``, ``ω_log``, ``μ*_EFT``,
  ``T_c^exp`` (the numerical content that used to live inside the old
  ``setting()`` blocks in :mod:`s6_superconductors`).
* :func:`mcmillan_log_tc_moments` — propagates the traditional
  ``μ* ~ Uniform[0.1, 0.2]`` prior through :func:`mcmillan_tc` and returns the
  mean / stddev of ``log T_c``.  Used as the predictive distribution of the
  phenomenological model.
* ``EFT_LOG_SIGMA`` — author-set Gaussian noise around the ab initio
  ``log T_c`` point estimate.
* ``log_tc_al`` / ``log_tc_zn`` / ``log_tc_li`` — :class:`Variable` handles
  for the three observed quantities.

Per the migration plan, the three ``support(...)`` McMillan warrants in
:mod:`s6_superconductors` and the three ``compare(...)`` / ``abduction(...)``
ab-initio-vs-phenomenological triples are replaced by structured
:func:`bayes.model` / :func:`bayes.likelihood` blocks that consume this
module.
"""

from __future__ import annotations

import math
from typing import TypedDict

from gaia.engine.lang import Real, Variable


# ---------------------------------------------------------------------------
# McMillan / Allen-Dynes Tc estimator
# ---------------------------------------------------------------------------


def mcmillan_tc(lambda_: float, mu_star: float, omega_log: float) -> float:
    """Allen-Dynes / McMillan ``T_c`` estimator (in K).

    Args:
        lambda_: dimensionless electron-phonon coupling.
        mu_star: Coulomb pseudopotential.
        omega_log: logarithmic average phonon frequency (in K).

    Returns:
        The predicted ``T_c`` in K.  Returns ``+0`` when the dimensionless
        coupling ``g = λ − μ*(1 + 0.62 λ)`` is non-positive (i.e. the
        Cooper instability is absent under these parameters).
    """
    g = lambda_ - mu_star * (1.0 + 0.62 * lambda_)
    if g <= 0.0:
        return 0.0
    return omega_log / 1.2 * math.exp(-1.04 * (1.0 + lambda_) / g)


# ---------------------------------------------------------------------------
# Per-material parameters (formerly inside setting() blocks)
# ---------------------------------------------------------------------------


class MaterialParams(TypedDict):
    """DFPT + ab initio μ* + experimental Tc bundle for a single material."""

    lam: float        # DFPT electron-phonon coupling λ
    omega_log: float  # logarithmic phonon average ω_log [K]
    mu_eft: float     # ab initio μ* from vDiagMC + BTS
    tc_exp: float     # experimental Tc [K]


MATERIAL_PARAMS: dict[str, MaterialParams] = {
    "al": {"lam": 0.44, "omega_log": 320.0, "mu_eft": 0.13, "tc_exp": 1.2},
    "zn": {"lam": 0.502, "omega_log": 111.0, "mu_eft": 0.12, "tc_exp": 0.875},
    "li": {"lam": 0.34, "omega_log": 242.0, "mu_eft": 0.18, "tc_exp": 4.0e-4},
}


# ---------------------------------------------------------------------------
# Propagation of μ* uncertainty into log Tc
# ---------------------------------------------------------------------------


def mcmillan_log_tc_moments(
    mat: MaterialParams,
    mu_grid: tuple[float, ...] = (0.10, 0.125, 0.15, 0.175, 0.20),
) -> tuple[float, float]:
    """Propagate ``μ* ~ Uniform[mu_grid_min, mu_grid_max]`` through McMillan.

    Returns Gaussian moments ``(mean, stddev)`` of ``log T_c`` matched to the
    sampled distribution.  This is the traditional theory's predictive
    distribution: the ``μ*`` uncertainty is genuine epistemic ignorance and
    propagates through the exponential ``T_c`` formula into a broad log-Tc
    spread.
    """
    log_tcs: list[float] = []
    for mu in mu_grid:
        tc = mcmillan_tc(mat["lam"], mu, mat["omega_log"])
        # Floor at a tiny positive Tc so the log is well-defined even when
        # the dimensionless coupling g → 0+.
        log_tcs.append(math.log(max(tc, 1e-30)))
    n = len(log_tcs)
    mean = sum(log_tcs) / n
    var = sum((x - mean) ** 2 for x in log_tcs) / n
    return mean, math.sqrt(var)


# ---------------------------------------------------------------------------
# EFT noise scale (per-material, propagated from μ*_EFT precision)
# ---------------------------------------------------------------------------

#: Author-chosen 1σ uncertainty on ``μ*_EFT`` from the vDiagMC + BTS pipeline.
#: vDiagMC error bars on the UEG ``μ_{E_F}`` reach a few percent (see TABLE I
#: in Cai et al.); the BTS scaling preserves that relative precision.
MU_EFT_REL_SIGMA: float = 0.05

#: Material-independent residual floor (lambda / omega_log / DFPT method
#: error not captured by the μ* uncertainty alone).
EFT_LOG_SIGMA_FLOOR: float = 0.15


def eft_log_tc_sigma(material: str) -> float:
    """Per-material 1σ on ``log T_c^EFT`` propagated from ``μ*_EFT`` precision.

    The dominant non-trivial uncertainty in the EFT prediction is the
    residual ``μ*`` error; near the quantum phase transition (``g → 0``) this
    is exponentially amplified, so a fixed 10%-on-Tc floor would be
    over-confident for low-Tc cases like Li.  We perturb ``μ*_EFT`` by
    ``±MU_EFT_REL_SIGMA`` and read off the resulting log-Tc spread, in
    quadrature with a residual floor.
    """
    p = MATERIAL_PARAMS[material]
    mu_lo = p["mu_eft"] * (1.0 - MU_EFT_REL_SIGMA)
    mu_hi = p["mu_eft"] * (1.0 + MU_EFT_REL_SIGMA)
    log_lo = math.log(max(mcmillan_tc(p["lam"], mu_lo, p["omega_log"]), 1e-30))
    log_hi = math.log(max(mcmillan_tc(p["lam"], mu_hi, p["omega_log"]), 1e-30))
    mu_sigma = abs(log_hi - log_lo) / 2.0
    return math.sqrt(mu_sigma * mu_sigma + EFT_LOG_SIGMA_FLOOR * EFT_LOG_SIGMA_FLOOR)


# ---------------------------------------------------------------------------
# Observable quantities (continuous, log-Tc domain)
#
# The ``value`` is the experimentally measured ``log T_c`` for the material;
# Bayesian likelihoods consume this through ``bayes.model(observable=...)``.
# ---------------------------------------------------------------------------

log_tc_al = Variable(
    symbol="log_tc_al",
    domain=Real,
    value=math.log(MATERIAL_PARAMS["al"]["tc_exp"]),
)
log_tc_zn = Variable(
    symbol="log_tc_zn",
    domain=Real,
    value=math.log(MATERIAL_PARAMS["zn"]["tc_exp"]),
)
log_tc_li = Variable(
    symbol="log_tc_li",
    domain=Real,
    value=math.log(MATERIAL_PARAMS["li"]["tc_exp"]),
)


# ---------------------------------------------------------------------------
# Convenience: per-material precomputed distribution parameters
# ---------------------------------------------------------------------------


def eft_log_tc_mean(material: str) -> float:
    """log Tc^EFT for a material, using ``μ*_EFT`` from MATERIAL_PARAMS."""
    p = MATERIAL_PARAMS[material]
    return math.log(max(mcmillan_tc(p["lam"], p["mu_eft"], p["omega_log"]), 1e-30))


def eft_log_tc_normal(material: str) -> tuple[float, float]:
    """Convenience: (mean, sigma) for the EFT log-Tc Gaussian."""
    return eft_log_tc_mean(material), eft_log_tc_sigma(material)
