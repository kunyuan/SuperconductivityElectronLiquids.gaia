"""Section II -- The Model and Basic Relations.

Establishes the electron-phonon action, BSE kernel decomposition, and the
precursory Cooper flow (PCF) method for determining Tc via universal scaling.
"""

from gaia.lang import claim, deduction

from .motivation import adiabatic_approx

PROVENANCE = [{"package_id": "paper:2512.19382", "version": "2024"}]

electron_phonon_action = claim(
    "电子-声子系统的总作用量可严格分解为 "
    "$S = S_e[\\bar{\\psi}, \\psi] + S_{ph}[u] + S_{e\\text{-}ph}[\\bar{\\psi}, \\psi, u] + S_{CT}[u]$，"
    "其中 $S_e$ 描述无近似的多电子相互作用，$S_{ph}$ 描述具有物理色散 "
    "$\\omega_{\\kappa q}$ 的声子，$S_{e\\text{-}ph}$ 通过密度-位移形式"
    "捕获电子-声子耦合，$S_{CT}$ 是反项，减去已包含在物理声子谱中的"
    "静态屏蔽。引入反项 $S_{CT}$ 确保微扰展开中声子传播子保持物理性质"
    "且不发生重复计数。",
    title="电子-声子作用量分解",
    provenance=PROVENANCE,
)

bse_kernel_decomposition = claim(
    "超导不稳定性通过反常顶点函数 $\\Lambda_{k\\omega}$ 满足的 "
    "Bethe-Salpeter 方程检测。BSE 积分核可严格分解为纯电子粒子-粒子"
    "相互作用 $\\tilde{\\Gamma}^e$ 与声子介导的吸引 $W^{ph}$ 两部分："
    "$\\tilde{\\Gamma} = \\tilde{\\Gamma}^e + W^{ph} + O(\\omega_D / E_F)$，"
    "其中误差项由 Migdal 定理控制，在绝热极限下可忽略。此分解是后续将 "
    "Coulomb 和声子通道独立处理的理论基础。",
    title="BSE 积分核分解",
    provenance=PROVENANCE,
)

precursory_cooper_flow = claim(
    "反常顶点函数在低频极限下遵循普适标度关系 "
    "$\\Lambda_0 = 1 / (1 + g \\ln(\\omega_\\Lambda / T)) + O(T)$，"
    "其中 $g$ 和 $\\omega_\\Lambda$ 是系统相关参数。对于 $g < 0$（净吸引），"
    "顶点在 $T_c = \\omega_\\Lambda \\exp(1/g)$ 处发散，标志 Cooper 不稳定性。"
    "通过在 $T_c$ 以上多个温度计算 $\\Lambda_0$ 并利用此对数标度律外推，"
    "可以避免在 $T_c$ 处进行计算困难的自洽求解而精确确定超导转变温度。"
    "该方法优于传统特征值追踪方法，因为后者在强排斥相互作用体系中"
    "缺乏可靠的外推方案。",
    title="前驱 Cooper 流方法",
    provenance=PROVENANCE,
)

# ── Reasoning ──

derive_pcf = deduction(
    premises=[bse_kernel_decomposition, electron_phonon_action, adiabatic_approx],
    conclusion=precursory_cooper_flow,
    reason="作用量的严格分解保证了电子-声子耦合的正确处理，"
    "BSE 积分核的 Coulomb/声子分离在绝热近似下成立，"
    "由此严格推导出反常顶点函数的普适对数标度律。",
)
