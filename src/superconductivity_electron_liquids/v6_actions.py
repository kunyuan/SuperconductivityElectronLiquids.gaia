"""Small v6 migration helpers for the electron-liquids sandbox package.

The package still keeps the original scientific narrative shape, but all
reasoning edges created here are Gaia Lang v6 actions.
"""

from __future__ import annotations

from gaia.lang import Claim as GaiaClaim
from gaia.lang import Question, Setting, contradict, derive, equal, infer as gaia_infer, observe
from gaia.lang.runtime.knowledge import Knowledge


def Claim(content: str, *args, **kwargs) -> GaiaClaim:
    claim = GaiaClaim(content, *args, **kwargs)
    observe(
        claim,
        rationale="Authored scientific assertion imported from the electron-liquids package.",
    )
    return claim


def _given(premises: list[Knowledge] | tuple[Knowledge, ...] | Knowledge | None):
    if premises is None:
        return ()
    if isinstance(premises, Knowledge):
        return (premises,)
    return tuple(premises)


def deduction(
    *,
    premises: list[Knowledge] | tuple[Knowledge, ...],
    conclusion: Claim,
    background: list[Knowledge] | None = None,
    reason: str = "",
):
    return derive(conclusion, given=_given(premises), background=background, rationale=reason)


def noisy_and(
    *,
    premises: list[Knowledge] | tuple[Knowledge, ...],
    conclusion: Claim,
    background: list[Knowledge] | None = None,
    reason: str = "",
):
    return derive(conclusion, given=_given(premises), background=background, rationale=reason)


def equivalence(a: Claim, b: Claim, *, reason: str = "", label: str | None = None):
    return equal(a, b, rationale=reason, label=label)


def contradiction(a: Claim, b: Claim, *, reason: str = ""):
    return contradict(a, b, rationale=reason)


def infer(
    *,
    hypothesis: Claim,
    evidence: Claim,
    background: list[Knowledge] | None = None,
    p_e_given_h: float = 0.9,
    p_e_given_not_h: float = 0.4,
    reason: str = "",
    label: str | None = None,
):
    return gaia_infer(
        hypothesis=hypothesis,
        evidence=evidence,
        background=list(background or []),
        p_e_given_h=p_e_given_h,
        p_e_given_not_h=p_e_given_not_h,
        rationale=reason,
        label=label,
    )


def induction(
    *,
    observations: list[Knowledge] | tuple[Knowledge, ...],
    conclusion: Claim,
    background: list[Knowledge] | None = None,
    reason: str = "",
    label: str | None = None,
):
    """Narrow v6 induction: observations/limits support a generalizing claim."""
    claim = derive(
        conclusion,
        given=_given(observations),
        background=background,
        rationale=reason,
        label=label,
    )
    if claim.supports:
        claim.supports[-1].metadata["reasoning_family"] = "induction"
    return claim


def composite(**_kwargs):
    return None
