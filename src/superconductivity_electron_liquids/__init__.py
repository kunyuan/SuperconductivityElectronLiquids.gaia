"""
Formalization: "Superconductivity in Electron Liquids: A Precision Many-Body Treatment"
arXiv: 2512.19382v1

核心论证：Coulomb 赝势 $\\mu^*$ 可通过变分图形蒙特卡洛方法从第一性原理精确计算，
消除超导理论中的关键唯象参数，实现对简单金属超导转变温度 $T_c$ 的定量可靠预测。
"""

from gaia.lang import (
    claim,
    setting,
    question,
    noisy_and,
    contradiction,
    # deduction,  # has bug, use noisy_and instead
    abduction,
)

PROVENANCE = [{"package_id": "paper:2512.19382", "version": "2024"}]

# ══════════════════════════════════════════════════════════════
# Section I — Introduction
# ══════════════════════════════════════════════════════════════

# ── Settings（不可被质疑的背景事实）──

bcs_framework = setting(
    "Bardeen-Cooper-Schrieffer (BCS) 理论将传统超导解释为声子交换介导的"
    "电子 Cooper 配对所产生的宏观量子态。该理论需要输入净有效电子-电子"
    "相互作用强度，即声子介导的吸引耦合与屏蔽 Coulomb 排斥之间的平衡。"
)

migdal_eliashberg = setting(
    "Migdal-Eliashberg (ME) 框架通过在实频率轴上求解电子自能的自洽方程，"
    "将 BCS 理论推广到强耦合区间。然而，该框架将 Coulomb 赝势 $\\mu^*$ "
    "作为唯象参数处理，通常通过拟合实验测量的超导转变温度 $T_c$ 来确定。"
    "对拟合参数的依赖限制了框架的预测能力，尤其是对于亚开尔文超导体，"
    "$\\mu^*$ 的微小变化会导致 $T_c$ 发生数量级变化。"
)

# ── Claims（可被质疑、需要论证的命题）──

adiabatic_approx = claim(
    "在传统金属中，Debye 频率 $\\omega_D$ 远小于 Fermi 能量 $E_F$"
    "（$\\omega_D / E_F \\ll 1$），建立了电子和声子能量尺度的分离。"
    "这一绝热条件由 Migdal（1958）首先利用，证明了电子-声子顶点修正"
    "是小量，从而允许向低能有效理论投影。",
    provenance=[{"package_id": "paper:migdal-1958", "version": "1958"}],
)

electron_gas_model = claim(
    "均匀电子气（jellium 模型）在金属密度区间（Wigner-Seitz 半径 "
    "$r_s = 2$ 至 $6$）是简单金属理论的标准参考系统。其性质通过局域密度"
    "近似支撑了密度泛函理论，使其成为第一性原理多体方法的天然检验平台。"
)

# ── Question ──

main_question = question(
    "Coulomb 赝势 $\\mu^*$——Migdal-Eliashberg 超导理论中的关键唯象参数"
    "——能否从第一性原理以可控精度计算？将第一性原理 $\\mu^*$ 值代入 "
    "Eliashberg 框架后，能否对简单金属的超导转变温度 $T_c$ 给出定量"
    "可靠的预测？"
)

# ══════════════════════════════════════════════════════════════
# Section II — The Model and Basic Relations
# ══════════════════════════════════════════════════════════════

electron_phonon_action = claim(
    "电子-声子系统的总作用量可严格分解为 "
    "$S = S_e[\\bar{\\psi}, \\psi] + S_{ph}[u] + S_{e\\text{-}ph}[\\bar{\\psi}, \\psi, u] + S_{CT}[u]$，"
    "其中 $S_e$ 描述无近似的多电子相互作用，$S_{ph}$ 描述具有物理色散 "
    "$\\omega_{\\kappa q}$ 的声子，$S_{e\\text{-}ph}$ 通过密度-位移形式"
    "捕获电子-声子耦合，$S_{CT}$ 是反项，减去已包含在物理声子谱中的"
    "静态屏蔽。引入反项 $S_{CT}$ 确保微扰展开中声子传播子保持物理性质"
    "且不发生重复计数。",
    provenance=PROVENANCE,
)

bse_kernel_decomposition = claim(
    "超导不稳定性通过反常顶点函数 $\\Lambda_{k\\omega}$ 满足的 "
    "Bethe-Salpeter 方程检测。BSE 积分核可严格分解为纯电子粒子-粒子"
    "相互作用 $\\tilde{\\Gamma}^e$ 与声子介导的吸引 $W^{ph}$ 两部分："
    "$\\tilde{\\Gamma} = \\tilde{\\Gamma}^e + W^{ph} + O(\\omega_D / E_F)$，"
    "其中误差项由 Migdal 定理控制，在绝热极限下可忽略。此分解是后续将 "
    "Coulomb 和声子通道独立处理的理论基础。",
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
    provenance=PROVENANCE,
)

# ══════════════════════════════════════════════════════════════
# Section III — Downfolding the BSE
# ══════════════════════════════════════════════════════════════

# ── III.1 理论框架 ──

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
    "$r_s \\geq 1$，该比值约为 0.1 或更小，保证了两个通道可独立处理。"
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

# ── III.2 赝势 ──

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

# ── III.3 数值验证 ──

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

# ══════════════════════════════════════════════════════════════
# Section IV — Coulomb Pseudopotential from First Principles
# ══════════════════════════════════════════════════════════════

ueg_vertex_challenge = claim(
    "尽管均匀电子气相对于真实材料更简单，但在 $r_s > 1$ 的密度下精确计算"
    "其 Cooper 通道的 Coulomb 赝势仍是重大挑战。传统的基态方法"
    "（变分蒙特卡洛和扩散蒙特卡洛）无法获取 $r_s > 1$ 时所需的四点"
    "顶点函数，而变分图形蒙特卡洛方法可以在弱耦合以外的区间直接计算"
    "所需的顶点函数。",
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
    provenance=PROVENANCE,
)

vdiagmc_method = claim(
    "变分图形蒙特卡洛方法采用重整化策略，将均匀电子气视为带反项的"
    "重整化 Yukawa Fermi 气体，将裸参数展开为幂级数 "
    "$\\mu = \\mu_R + \\delta\\mu_1 \\xi + \\delta\\mu_2 \\xi^2 + \\cdots$，"
    "物理结果对应 $\\xi = 1$。Feynman 图表示为利用 Dyson-Schwinger 和 "
    "Parquet 方程的计算图，实现了场论重整化方案的高效实现。屏蔽参数 "
    "$\\lambda_R$ 经过优化以改善收敛性。",
    provenance=PROVENANCE,
)

# ══════════════════════════════════════════════════════════════
# Section V — Electron-Phonon Coupling from Band Theory
# ══════════════════════════════════════════════════════════════

individual_corrections_large = claim(
    "在有效场论（EFT）框架中，电子-电子相互作用对准粒子权重 $z^e$ 的修正、"
    "对屏蔽 Coulomb 相互作用 $v_q/\\varepsilon_q$ 的修正、以及对电子-声子"
    "顶点 $\\Gamma_3^e$ 的修正各自都很大，单独考虑时会显著偏离自由电子结果。",
    provenance=PROVENANCE,
)

corrections_cancel = claim(
    "尽管各项修正单独很大，它们在有效电子-声子耦合中几乎精确抵消："
    "$z^e \\cdot v_q/\\varepsilon_q \\cdot \\Gamma_3^e(k; q) \\approx "
    "v_q / [1 - (v_q + f_{xc}) \\cdot \\chi_0^e(q)]$，其中左侧是包含所有"
    "多体修正的 EFT 结果，右侧是基于线性响应理论的密度泛函微扰理论"
    "（DFPT）结果。图形化地说，电子-电子相互作用对准粒子权重 $z^e$ "
    "的贡献被电子-声子顶点重整化 $\\Gamma_3^e$ 有效抵消。",
    provenance=PROVENANCE,
)

dfpt_validated_numerically = claim(
    "通过变分图形蒙特卡洛方法在 $r_s \\in [1, 5]$ 区间的数值验证，"
    "EFT 与 DFPT 在 Fermi 面上所有相关动量传递（$|q| \\leq 2k_F$）"
    "范围内给出近乎完全一致的有效电子-声子耦合 $\\lambda$ 值。",
    provenance=PROVENANCE,
)

dfpt_reliable_for_simple_metals = claim(
    "密度泛函微扰理论（DFPT）对简单金属的电子-声子耦合常数 $\\lambda$ "
    "给出定量可靠的结果。这一结论由变分图形蒙特卡洛方法在 "
    "$r_s \\in [1,5]$ 区间的逐点基准测试确立：尽管准粒子权重 $z^e$、"
    "屏蔽和顶点修正各自偏离自由电子值很大，它们在有效耦合中几乎精确抵消，"
    "使得 DFPT 的线性响应结果与包含所有多体效应的有效场论结果一致。"
    "这意味着计算真实材料的 $T_c$ 时可直接使用现有的 DFPT 代码获取"
    "电子-声子耦合，而无需完整的多体计算。",
    provenance=PROVENANCE,
)

ward_identity_hypothesis = claim(
    "Ward 恒等式和电子-声子顶点的规范不变性强制要求自能、屏蔽和顶点修正"
    "在长波极限下系统性地互相抵消。DFPT 中各项大修正的近精确抵消不是"
    "数值巧合，而是守恒律约束多体修正在物理可观测量中组合方式的必然结果。"
)

# ══════════════════════════════════════════════════════════════
# Section VI — Conventional Superconductors
# ══════════════════════════════════════════════════════════════

# ── 材料参数（Settings）──

aluminum_parameters = setting(
    "铝（Al）的材料参数：Wigner-Seitz 半径 $r_s = 2.07$，"
    "Debye 温度 $\\Theta_D = 428$ K，"
    "实验超导转变温度 $T_c^{exp} = 1.175$ K。"
)

lithium_parameters = setting(
    "锂（Li）的材料参数：Wigner-Seitz 半径 $r_s = 3.25$，"
    "Debye 温度 $\\Theta_D = 344$ K，"
    "实验超导转变温度 $T_c^{exp} \\approx 0.4$ K。"
)

magnesium_parameters = setting(
    "镁（Mg）的材料参数：Wigner-Seitz 半径 $r_s = 2.66$，"
    "Debye 温度 $\\Theta_D = 400$ K，实验上未观测到超导转变。"
)

sodium_parameters = setting(
    "钠（Na）的材料参数：Wigner-Seitz 半径 $r_s = 3.93$，"
    "Debye 温度 $\\Theta_D = 158$ K，实验上未观测到超导转变。"
)

# ── VI.1 工作流 ──

ab_initio_workflow = claim(
    "一套完整的第一性原理超导 $T_c$ 预测工作流由三个组件集成构成："
    "（1）由变分图形蒙特卡洛方法计算的均匀电子气 Coulomb 赝势 $\\mu^*$，"
    "通过 Bogoliubov-Tolmachev-Shirkov 关系标度到适当的能量截断；"
    "（2）由密度泛函微扰理论（DFPT）计算的电子-声子耦合常数 $\\lambda$，"
    "其可靠性已通过多体基准测试验证；（3）前驱 Cooper 流方法，通过在 "
    "$T_c$ 以上多个温度求解 downfolded BSE 并利用普适标度律外推确定 "
    "$T_c$。该工作流不含任何可调参数。",
    provenance=PROVENANCE,
)

# ── VI.2 Tc 预测 ──

tc_aluminum = claim(
    "第一性原理预测铝的超导转变温度为 $T_c = 1.31$ K，实验值为 1.175 K。"
    "此前 Migdal-Eliashberg 理论使用经验 $\\mu^*$ 预测约 2.4 K，"
    "偏高约两倍。新框架将理论-实验偏差从约 100% 缩小到约 11%。",
    given=[ab_initio_workflow],
    background=[aluminum_parameters],
    provenance=PROVENANCE,
)

tc_lithium = claim(
    "第一性原理预测锂的超导转变温度为 $T_c = 0.38$ K，"
    "实验值约为 0.4–0.5 K。此前理论使用经验 $\\mu^*$ 的预测值偏高了"
    "三个数量级。这一长期存在的巨大偏差在新框架下得到解决，"
    "是该方法预测能力最戏剧性的展示。",
    given=[ab_initio_workflow],
    background=[lithium_parameters],
    provenance=PROVENANCE,
)

tc_mg_na_near_qpt = claim(
    "第一性原理计算预测镁和钠处于正常态-超导态量子相变的临界点附近，"
    "其 $T_c$ 极低（低于 10 K 区间）。这使它们成为研究超导量子临界"
    "标度行为的候选材料。",
    given=[ab_initio_workflow],
    background=[magnesium_parameters, sodium_parameters],
    provenance=PROVENANCE,
)

al_pressure_transition = claim(
    "理论预测铝在压力增加到约 60 GPa 以上时会经历从超导态到正常态的"
    "压力诱导量子相变。这是一个可实验验证的预测。",
    given=[ab_initio_workflow],
    background=[aluminum_parameters],
    provenance=PROVENANCE,
)

tc_improvement_over_phenomenological = claim(
    "与基于唯象 $\\mu^*$ 的传统方法相比，该第一性原理框架对亚开尔文"
    "超导体的 $T_c$ 预测实现了数量级的改进。改进的根本原因是用变分"
    "图形蒙特卡洛方法精确计算的 $\\mu_{E_F}$ 替代了拟合参数，消除了 "
    "$\\mu^*$ 微小变化导致 $T_c$ 数量级变化的不稳定性。",
    provenance=PROVENANCE,
)

# ══════════════════════════════════════════════════════════════
# 推理链（从结论倒推）
# ══════════════════════════════════════════════════════════════

# ── 第零层：Section III 内部推理 ──

# pair_propagator_decomposition + cross_term_suppressed → downfolded_bse
derive_downfolded_bse = noisy_and(
    premises=[pair_propagator_decomposition, cross_term_suppressed, adiabatic_approx],
    conclusion=downfolded_bse,
    steps=[{
        "reasoning": "配对传播子的相干/非相干分解提供了降标的数学基础，"
        "交叉项被 $\\omega_c^2/\\omega_p^2$ 压制保证了 Coulomb 和声子通道"
        "可独立处理，两者结合推导出仅依赖频率的 Fermi 面 BSE。",
        "premises": [pair_propagator_decomposition, cross_term_suppressed],
        "conclusion": downfolded_bse,
    }],
    reason="从配对传播子分解和交叉项压制推导出 downfolded BSE",
)

# ── 第零层：Section II → precursory_cooper_flow ──

derive_pcf = noisy_and(
    premises=[bse_kernel_decomposition, electron_phonon_action, adiabatic_approx],
    conclusion=precursory_cooper_flow,
    steps=[{
        "reasoning": "作用量的严格分解保证了电子-声子耦合的正确处理，"
        "BSE 积分核的 Coulomb/声子分离在绝热近似下成立，"
        "由此推导出反常顶点函数的普适对数标度律。",
        "premises": [bse_kernel_decomposition, electron_phonon_action, adiabatic_approx],
        "conclusion": precursory_cooper_flow,
    }],
    reason="从作用量分解、BSE 核分解和绝热近似推导出前驱 Cooper 流标度律",
)

# ── 第一层：三个工作流组件的来源 ──

# vdiagmc_method + homotopic_expansion + ueg_vertex_challenge → mu_vdiagmc_values
derive_mu_values = noisy_and(
    premises=[vdiagmc_method, homotopic_expansion, ueg_vertex_challenge],
    conclusion=mu_vdiagmc_values,
    steps=[{
        "reasoning": "传统方法无法计算 $r_s > 1$ 的顶点函数"
        "（ueg_vertex_challenge），变分图形蒙特卡洛方法提供了计算能力"
        "（vdiagmc_method），同伦展开解决了低温收敛问题"
        "（homotopic_expansion），三者共同使得 $\\mu_{E_F}$ 的精确计算成为可能。",
        "premises": [vdiagmc_method, homotopic_expansion, ueg_vertex_challenge],
        "conclusion": mu_vdiagmc_values,
    }],
    reason="三项方法论进展共同支撑 μ 值的精确计算",
)

# individual_corrections_large + corrections_cancel + dfpt_validated_numerically
#   → dfpt_reliable_for_simple_metals
derive_dfpt_reliable = noisy_and(
    premises=[individual_corrections_large, corrections_cancel, dfpt_validated_numerically],
    conclusion=dfpt_reliable_for_simple_metals,
    steps=[{
        "reasoning": "观察到各项多体修正单独很大（individual_corrections_large），"
        "但在有效耦合中几乎精确抵消（corrections_cancel），并通过变分图形"
        "蒙特卡洛方法的逐点数值验证确认了这一抵消（dfpt_validated_numerically），"
        "从而演绎出 DFPT 对简单金属给出可靠的电子-声子耦合。",
        "premises": [individual_corrections_large, corrections_cancel,
                     dfpt_validated_numerically],
        "conclusion": dfpt_reliable_for_simple_metals,
    }],
    reason="大修正互相抵消 + 数值验证 → DFPT 可靠",
)

# ── 第二层：三组件 → 工作流 ──

# mu_vdiagmc_values + dfpt_reliable_for_simple_metals + precursory_cooper_flow
#   → ab_initio_workflow
derive_workflow = noisy_and(
    premises=[mu_vdiagmc_values, dfpt_reliable_for_simple_metals, precursory_cooper_flow],
    conclusion=ab_initio_workflow,
    steps=[{
        "reasoning": "变分图形蒙特卡洛方法提供精确的 $\\mu^*$，DFPT 提供"
        "可靠的电子-声子耦合 $\\lambda$，前驱 Cooper 流提供高效的 $T_c$ "
        "确定方法，三个独立验证的组件组合成无可调参数的第一性原理工作流。",
        "premises": [mu_vdiagmc_values, dfpt_reliable_for_simple_metals,
                     precursory_cooper_flow],
        "conclusion": ab_initio_workflow,
    }],
    reason="三个独立组件集成为完整的第一性原理工作流",
)

# ── 第三层：工作流 + 材料参数 → 各金属 Tc ──

# ── 第三层：具体预测 → 终极结论 ──
# （各金属 Tc 预测已通过 given=[ab_initio_workflow] 自动连接）

derive_improvement = noisy_and(
    premises=[tc_aluminum, tc_lithium],
    conclusion=tc_improvement_over_phenomenological,
    steps=[{
        "reasoning": "铝的预测将偏差从 100% 缩小到 11%，锂的预测解决了"
        "三个数量级的偏差，两个具体案例共同支撑了该框架相对唯象方法的"
        "数量级改进这一总结论。",
        "premises": [tc_aluminum, tc_lithium],
        "conclusion": tc_improvement_over_phenomenological,
    }],
    reason="两个实验验证共同支撑总结论",
)

# ── 横向：矛盾 ──

mu_rpa_vdiagmc_contradiction = contradiction(
    mu_vdiagmc_values,
    rpa_predicts_negative_mu,
    reason="变分图形蒙特卡洛方法计算得到 $\\mu_{E_F}$ 在所有金属密度下均为正"
    "且远大于 RPA 估计，而动态 RPA 对 $r_s > 2$ 预测 $\\mu^*$ 为负"
    "（净吸引）。两种方法对赝势的符号和量级给出不兼容的结果，"
    "表明 RPA 在这些密度下对 Cooper 通道赝势的计算已经失效。",
)

# ── 横向：溯因 ──

explain_dfpt_cancellation = abduction(
    observation=corrections_cancel,
    hypothesis=ward_identity_hypothesis,
    steps=[{
        "reasoning": "各项修正的近精确抵消不是数值巧合，而是反映了守恒律"
        "（Ward 恒等式）对多体修正在物理可观测量中组合方式的约束。",
    }],
    reason="解释为什么 DFPT 修正量互相抵消",
)


# ══════════════════════════════════════════════════════════════
# Exports
# ══════════════════════════════════════════════════════════════

__all__ = [
    # Section I — Settings
    "bcs_framework",
    "migdal_eliashberg",
    # Section I — Claims
    "adiabatic_approx",
    "electron_gas_model",
    # Section I — Question
    "main_question",
    # Section II
    "electron_phonon_action",
    "bse_kernel_decomposition",
    "precursory_cooper_flow",
    # Section III
    "pair_propagator_decomposition",
    "cross_term_suppressed",
    "downfolded_bse",
    "pseudopotential_scale_relation",
    "mu_vdiagmc_values",
    "rpa_predicts_negative_mu",
    "downfolding_validated",
    "downfolding_limitations",
    # Section IV
    "ueg_vertex_challenge",
    "homotopic_expansion",
    "vdiagmc_method",
    # Section V
    "individual_corrections_large",
    "corrections_cancel",
    "dfpt_validated_numerically",
    "dfpt_reliable_for_simple_metals",
    "ward_identity_hypothesis",
    # Section VI — Settings
    "aluminum_parameters",
    "lithium_parameters",
    "magnesium_parameters",
    "sodium_parameters",
    # Section VI — Claims
    "ab_initio_workflow",
    "tc_aluminum",
    "tc_lithium",
    "tc_mg_na_near_qpt",
    "al_pressure_transition",
    "tc_improvement_over_phenomenological",
    # Reasoning
    "derive_downfolded_bse",
    "derive_pcf",
    "derive_mu_values",
    "derive_dfpt_reliable",
    "derive_workflow",
    "derive_improvement",
    "mu_rpa_vdiagmc_contradiction",
    "explain_dfpt_cancellation",
]
