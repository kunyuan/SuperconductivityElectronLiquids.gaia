"""
Formalization: "Superconductivity in Electron Liquids: A Precision Many-Body Treatment"
arXiv: 2512.19382v1

核心论证：Coulomb 赝势 $\\mu^*$ 可通过变分图形蒙特卡洛方法从第一性原理精确计算，
消除超导理论中的关键唯象参数，实现对简单金属超导转变温度 $T_c$ 的定量可靠预测。
"""

from .motivation import *  # noqa: F401,F403
from .s2_model import *  # noqa: F401,F403
from .s3_downfolding import *  # noqa: F401,F403
from .s4_pseudopotential import *  # noqa: F401,F403
from .s5_eph_coupling import *  # noqa: F401,F403
from .s6_superconductors import *  # noqa: F401,F403

__all__ = [
    # Core conclusions — what this package exports
    "ab_initio_workflow",
    "tc_al_predicted",
    "tc_li_predicted",
    "tc_mg_na_near_qpt",
    "al_pressure_transition",
    "tc_improvement_over_phenomenological",
]
