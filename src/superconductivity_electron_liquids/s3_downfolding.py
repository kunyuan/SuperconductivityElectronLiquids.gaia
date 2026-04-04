"""Section III -- Downfolding the BSE.

Derives the frequency-only Fermi-surface BSE via pair-propagator decomposition,
establishes the pseudopotential scale relation, presents vDiagMC mu values,
and validates the downfolding numerically.
"""

from gaia.lang import claim, contradiction, deduction

from .motivation import adiabatic_approx

PROVENANCE = [{"package_id": "paper:2512.19382", "version": "2024"}]

# ── III.1 Theoretical framework ──

pair_propagator_decomposition = claim(
    "配对传播子可严格分解为相干（低能/IR）与非相干（高能/UV）分量："
    "$G_{k,\\omega} G_{-k,-\\omega} = \\Pi_{BCS} + \\varphi_{k\\omega}$，"
    "其中相干部分 $\\Pi_{BCS} = (z^e)^2 / [(\\omega/z_\\omega^{ph})^2 "
    "+ \\varepsilon_k^2] \\cdot \\Theta(\\omega_c - |\\varepsilon_k|)$，"
    "$z^e$ 为电子-电子相互作用的准粒子权重，$z_\\omega^{ph}$ 捕获"
    "电子-声子耦合的频率依赖重整化。此分解是将全 BSE 降到低能有效"
    "理论的数学基础。",
    provenance=PROVENANCE,
)

cross_term_suppressed = claim(
    "在 downfolding 过程中，Coulomb 通道和声子通道之间的交叉耦合项"
    "（$\\tilde{\\Gamma}^e \\cdot \\varphi \\cdot W^{ph}$）被等离激元"
    "频率压制，量级为 $\\omega_c^2 / \\omega_p^2$。对于金属密度 "
    "$r_s \\geq 1$，$\\omega_c / \\omega_p \\lesssim 0.1$，"
    "故 $\\omega_c^2 / \\omega_p^2 \\lesssim 0.01$，"
    "保证了两个通道可独立处理。"
    "此压制依赖于动态屏蔽 Coulomb 相互作用在高频的渐近行为 "
    "$W^s \\propto (\\omega - \\omega')^2 / [(\\omega - \\omega')^2 + \\omega_p^2]$。",
    provenance=PROVENANCE,
)

downfolded_bse = claim(
    "消去高能模式后，完整的 BSE 可严格降标为仅依赖频率的 Fermi 面方程："
    "$\\Lambda_\\omega = \\eta_\\omega + \\pi T \\sum_{|\\omega'| < \\omega_c} "
    "(\\lambda_{\\omega\\omega'} - \\mu_{\\omega_c}) \\, z^{ph}_{\\omega'} "
    "/ |\\omega'| \\, \\Lambda_{\\omega'}$，其中有效顶点可分离为 "
    "$\\tilde{\\Gamma}^{\\omega_c} = U^e + W^{ph} + O(\\omega_D/E_F, "
    "\\, \\omega_c^2/\\omega_p^2)$，$U^e$ 为纯电子贡献且不依赖声子细节。"
    "此结果的关键意义是：尽管微观 Coulomb 相互作用具有奇异的动量依赖性"
    "和复杂的动态屏蔽，投影后的有效电子-电子相互作用退化为频率无关的"
    "赝势 $\\mu_{\\omega_c}$。",
    provenance=PROVENANCE,
)

# ── III.2 Pseudopotential ──

pseudopotential_scale_relation = claim(
    "Coulomb 赝势 $\\mu_{\\omega_c}$ 在能量尺度变换下满足 "
    "Bogoliubov-Tolmachev-Shirkov 关系："
    "$\\mu_{\\omega_c} = \\mu_{\\omega_c'} / "
    "(1 + \\mu_{\\omega_c'} \\ln(\\omega_c'/\\omega_c))$。"
    "该关系确保物理可观测量不依赖于截断尺度的选择。在 Fermi 能量处"
    "定义的'裸'赝势 $\\mu_{E_F}$ 是物理上有意义且无重整化伪影的量。",
    provenance=PROVENANCE,
)

mu_vdiagmc_values = claim(
    "利用变分图形蒙特卡洛方法计算均匀电子气在 $r_s \\in [1,6]$ 区间的 "
    "$\\mu_{E_F}$，结果为：$r_s=1$ 时 $\\mu_{E_F} = 0.28(1)$，$r_s=2$ 时 "
    "$0.53(2)$，$r_s=3$ 时 $0.77(5)$，$r_s=4$ 时 $1.0(2)$，$r_s=5$ 时 "
    "$1.3(2)$，$r_s=6$ 时 $1.8(8)$。这些值显著超出 Morel-Anderson 静态 "
    "RPA 估计值（在 $r_s=5$ 处约为三倍），差异来源于顶点修正和超越 "
    "RPA 的效应。",
    provenance=PROVENANCE,
)

rpa_predicts_negative_mu = claim(
    "动态 RPA 对 $r_s > 2$ 预测 $\\mu^*$ 为负值，意味着 Coulomb 相互作用"
    "在 Cooper 通道中变为净吸引。这一结果在物理上不合理，因为没有电子-声子"
    "耦合的纯电子系统不应出现传统超导。这表明 RPA 在这些密度下对赝势的"
    "计算已经失效。"
)

# ── III.3 Numerical validation ──

downfolding_validated = claim(
    "通过类铝参数（$r_s = 1.92$，$\\omega_D/E_F = 0.005$）的基准测试，"
    "比较完整频率-动量依赖的 BSE 解与简化的仅频率 downfolded BSE 解，"
    "两种方法得到的 $T_c$ 仅差 0.2%（$T_c^{full}/T_F = 10^{-5.668}$ vs "
    "$T_c^{approx}/T_F = 10^{-5.667}$），在 Debye 频率以下两者展现相同的"
    "普适对数标度行为。该基准验证了 downfolding 过程的定量精度。",
    provenance=PROVENANCE,
)

downfolding_limitations = claim(
    "Downfolding 框架在三类体系中不可靠：（1）超致密体系"
    "（$r_s \\lesssim 0.01$，如白矮星内部），等离激元变软；"
    "（2）二维体系，无能隙等离激元模式使尺度分离条件在任何密度下都不成立；"
    "（3）强关联材料，强关联产生的软集体激发破坏了能量尺度层级。",
    provenance=PROVENANCE,
)

# ── Reasoning ──

derive_downfolded_bse = deduction(
    premises=[pair_propagator_decomposition, cross_term_suppressed, adiabatic_approx],
    conclusion=downfolded_bse,
    reason="配对传播子的相干/非相干分解提供了降标的数学基础，"
    "交叉项被 $\\omega_c^2/\\omega_p^2$ 压制保证了 Coulomb 和声子通道"
    "可独立处理，两者结合在绝热近似下严格推导出仅依赖频率的 Fermi 面 BSE。",
)

mu_rpa_vdiagmc_contradiction = contradiction(
    mu_vdiagmc_values,
    rpa_predicts_negative_mu,
    reason="变分图形蒙特卡洛方法计算得到 $\\mu_{E_F}$ 在所有金属密度下均为正"
    "且远大于 RPA 估计，而动态 RPA 对 $r_s > 2$ 预测 $\\mu^*$ 为负"
    "（净吸引）。两种方法对赝势的符号和量级给出不兼容的结果，"
    "表明 RPA 在这些密度下对 Cooper 通道赝势的计算已经失效。",
)
