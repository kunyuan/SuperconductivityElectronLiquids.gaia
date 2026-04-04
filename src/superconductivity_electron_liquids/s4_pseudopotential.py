"""Section IV -- Coulomb Pseudopotential from First Principles.

Describes the challenge of computing the Cooper-channel vertex for the UEG,
the homotopic expansion trick for low-temperature convergence, and the
variational diagrammatic Monte Carlo (vDiagMC) method.
"""

from gaia.lang import claim, noisy_and

from .motivation import electron_gas_model
from .s3_downfolding import mu_vdiagmc_values, pseudopotential_scale_relation

PROVENANCE = [{"package_id": "paper:2512.19382", "version": "2024"}]

ueg_vertex_challenge = claim(
    "尽管均匀电子气相对于真实材料更简单，但在 $r_s > 1$ 的密度下精确计算"
    "其 Cooper 通道的 Coulomb 赝势仍是重大挑战。传统的基态方法"
    "（变分蒙特卡洛和扩散蒙特卡洛）无法获取 $r_s > 1$ 时所需的四点"
    "顶点函数，而变分图形蒙特卡洛方法可以在弱耦合以外的区间直接计算"
    "所需的顶点函数。",
    title="电子气顶点计算挑战",
    provenance=PROVENANCE,
)

homotopic_expansion = claim(
    "在低温下，标准微扰展开的第 $n$ 阶项按 $(\\ln T)^n$ 标度，导致 "
    "$T \\to 0$ 时对数发散。为解决此收敛问题，引入同伦变换将温度依赖的"
    "散射振幅 $\\gamma_T(\\xi)$ 转化为温度无关的赝势："
    "$\\mu_{\\omega_c}(\\xi) = \\gamma_T(\\xi) / "
    "[1 - \\gamma_T(\\xi) \\, \\xi \\ln(\\omega_c / T)]$，展开为 "
    "$\\mu_{\\omega_c}(\\xi) = \\mu_{\\omega_c}^{(0)} + \\mu_{\\omega_c}^{(1)}\\xi "
    "+ \\mu_{\\omega_c}^{(2)}\\xi^2 + \\cdots$，其系数不依赖温度。该变换"
    "利用 Cooper 对数的标度性质，产生恰好抵消发散 $\\ln(\\omega_c/T)$ "
    "行为的反项，使级数在所有温度下快速收敛，从而可靠提取 $\\mu_{E_F}$ 的值。",
    title="同伦展开消除对数发散",
    provenance=PROVENANCE,
)

vdiagmc_method = claim(
    "变分图形蒙特卡洛方法采用重整化策略，将均匀电子气视为带反项的"
    "重整化 Yukawa Fermi 气体，将裸参数展开为幂级数 "
    "$\\mu = \\mu_R + \\delta\\mu_1 \\xi + \\delta\\mu_2 \\xi^2 + \\cdots$，"
    "物理结果对应 $\\xi = 1$。Feynman 图表示为利用 Dyson-Schwinger 和 "
    "Parquet 方程的计算图，实现了场论重整化方案的高效实现。屏蔽参数 "
    "$\\lambda_R$ 经过优化以改善收敛性。",
    title="变分图形蒙特卡洛方法",
    provenance=PROVENANCE,
)

# ── Reasoning ──

derive_mu_values = noisy_and(
    premises=[vdiagmc_method, homotopic_expansion, ueg_vertex_challenge],
    conclusion=mu_vdiagmc_values,
    background=[electron_gas_model, pseudopotential_scale_relation],
    reason="在均匀电子气上用 VDiagMC 计算四点顶点函数，"
    "同伦展开解决低温收敛问题，BTS 标度关系保证尺度一致性，"
    "共同得到 $\\mu_{E_F}$ 的精确值。",
)
