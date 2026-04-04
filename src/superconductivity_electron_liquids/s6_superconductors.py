"""Section VI -- Conventional Superconductors.

Assembles the ab initio workflow from vDiagMC mu*, DFPT lambda, and precursory
Cooper flow, then applies it to Al, Li, Mg, Na to predict Tc and demonstrate
improvement over phenomenological approaches.
"""

from gaia.lang import claim, noisy_and, setting

from .s2_model import precursory_cooper_flow
from .s3_downfolding import downfolding_validated, mu_vdiagmc_values
from .s5_eph_coupling import dfpt_reliable_for_simple_metals

PROVENANCE = [{"package_id": "paper:2512.19382", "version": "2024"}]

# ── Material parameters (Settings) ──

aluminum_parameters = setting(
    "铝（Al）的材料参数（Table II）：Wigner-Seitz 半径 $r_s = 2.07$，"
    "对数平均声子频率 $\\omega_{\\mathrm{log}} = 320$ K，"
    "电子-声子耦合 $\\lambda = 0.44$，"
    "实验超导转变温度 $T_c^{\\mathrm{exp}} = 1.2$ K。",
    title="铝的材料参数",
)

lithium_parameters = setting(
    "锂（Li, 9R 结构）的材料参数（Table II）：Wigner-Seitz 半径 $r_s = 3.25$，"
    "对数平均声子频率 $\\omega_{\\mathrm{log}} = 242$ K，"
    "电子-声子耦合 $\\lambda = 0.34$，"
    "实验超导转变温度 $T_c^{\\mathrm{exp}} = 4 \\times 10^{-4}$ K（0.4 mK）。",
    title="锂的材料参数",
)

magnesium_parameters = setting(
    "镁（Mg）的材料参数（Table II）：Wigner-Seitz 半径 $r_s = 2.66$，"
    "对数平均声子频率 $\\omega_{\\mathrm{log}} = 269$ K，"
    "电子-声子耦合 $\\lambda = 0.24$，实验上未观测到超导转变。",
    title="镁的材料参数",
)

sodium_parameters = setting(
    "钠（Na）的材料参数（Table II）：Wigner-Seitz 半径 $r_s = 3.96$，"
    "对数平均声子频率 $\\omega_{\\mathrm{log}} = 127$ K，"
    "电子-声子耦合 $\\lambda = 0.2$，实验上未观测到超导转变。",
    title="钠的材料参数",
)

# ── VI.1 Workflow ──

ab_initio_workflow = claim(
    "一套完整的第一性原理超导 $T_c$ 预测工作流由三个组件集成构成："
    "（1）由变分图形蒙特卡洛方法计算的均匀电子气 Coulomb 赝势 $\\mu^*$，"
    "通过 Bogoliubov-Tolmachev-Shirkov 关系标度到适当的能量截断；"
    "（2）由密度泛函微扰理论（DFPT）计算的电子-声子耦合常数 $\\lambda$，"
    "其可靠性已通过多体基准测试验证；（3）前驱 Cooper 流方法，通过在 "
    "$T_c$ 以上多个温度求解 downfolded BSE 并利用普适标度律外推确定 "
    "$T_c$。该工作流不含任何可调参数。",
    title="第一性原理 Tc 预测工作流",
    provenance=PROVENANCE,
)

# ── VI.2 Tc predictions ──

tc_al_predicted = claim(
    "第一性原理工作流预测铝的超导转变温度为 $T_c^{\\mathrm{EFT}} = 0.96$ K"
    "（Table II），与实验值 $T_c^{\\mathrm{exp}} = 1.2$ K 偏差约 20%。",
    title="铝的 Tc 第一性原理预测",
    given=[ab_initio_workflow],
    background=[aluminum_parameters],
    provenance=PROVENANCE,
)

tc_al_phenomenological = claim(
    "使用传统 McMillan 公式和标准 $\\mu^* = 0.1$ 预测铝的超导转变温度为 "
    "$T_c^{\\mu\\mathrm{MA}} = 1.9$ K（Table II），相对实验值 1.2 K 偏高约 "
    "58%。与第一性原理预测的 0.96 K（偏差 20%）相比，传统方法对铝的"
    "预测精度较低。",
    title="铝的 Tc 唯象预测",
    background=[aluminum_parameters],
    provenance=PROVENANCE,
)

tc_li_predicted = claim(
    "第一性原理工作流预测锂（9R 结构）的超导转变温度为 "
    "$T_c^{\\mathrm{EFT}} = 5 \\times 10^{-3}$ K（Table II），"
    "比实验值 $T_c^{\\mathrm{exp}} = 4 \\times 10^{-4}$ K 高约一个数量级，"
    "部分原因在于极低温下锂晶体结构的争议。",
    title="锂的 Tc 第一性原理预测",
    given=[ab_initio_workflow],
    background=[lithium_parameters],
    provenance=PROVENANCE,
)

tc_li_phenomenological = claim(
    "使用传统 McMillan 公式和标准 $\\mu^* = 0.1$ 预测锂（9R 结构）的"
    "超导转变温度为 $T_c^{\\mu\\mathrm{MA}} = 0.35$ K（Table II），"
    "相对实验值 $4 \\times 10^{-4}$ K 偏高约三个数量级。"
    "第一性原理预测的 $5 \\times 10^{-3}$ K 虽仍偏高一个数量级，"
    "但较传统方法改善了两个数量级。",
    title="锂的 Tc 唯象预测",
    background=[lithium_parameters],
    provenance=PROVENANCE,
)

tc_mg_na_near_qpt = claim(
    "第一性原理计算预测镁的 $T_c^{\\mathrm{EFT}} = 5 \\times 10^{-5}$ K、"
    "钠的 $T_c^{\\mathrm{EFT}} = 2 \\times 10^{-13}$ K（Table II），"
    "远低于当前实验探测能力。两者均处于正常态-超导态量子相变的临界点附近，"
    "配对场磁化率在 10 K 以下展现量子临界标度 $\\chi \\sim \\ln(T)$，"
    "无需精细调控参数。",
    title="镁和钠接近量子临界点",
    given=[ab_initio_workflow],
    background=[magnesium_parameters, sodium_parameters],
    provenance=PROVENANCE,
)

al_pressure_transition = claim(
    "理论预测铝在压力增加到约 60 GPa 以上时会经历从超导态到正常态的"
    "压力诱导量子相变。这是一个可实验验证的预测。",
    title="铝的压力诱导量子相变",
    given=[ab_initio_workflow],
    background=[aluminum_parameters],
    provenance=PROVENANCE,
)

tc_improvement_over_phenomenological = claim(
    "与基于唯象 $\\mu^* = 0.1$ 的 McMillan 公式相比，第一性原理框架"
    "对亚开尔文超导体的 $T_c$ 预测实现了数量级的改进："
    "铝从偏差 58% 缩小到 20%，锂从偏差三个数量级缩小到一个数量级。"
    "改进的根本原因是用变分图形蒙特卡洛方法精确计算的 $\\mu_{E_F}$ "
    "替代了拟合参数。对于 $\\mu^*$ 微小变化导致 $T_c$ 数量级变化的"
    "低温超导体，精确的 $\\mu^*$ 值尤为关键。",
    title="Tc 预测精度数量级提升",
    provenance=PROVENANCE,
)

# ── Reasoning ──

derive_workflow = noisy_and(
    premises=[mu_vdiagmc_values, dfpt_reliable_for_simple_metals,
              precursory_cooper_flow],
    conclusion=ab_initio_workflow,
    background=[downfolding_validated],
    reason="精确 $\\mu^*$ + 可靠 $\\lambda$ + PCF 方法"
    " → 无可调参数的第一性原理工作流。",
)

derive_improvement = noisy_and(
    premises=[tc_al_predicted, tc_li_predicted],
    conclusion=tc_improvement_over_phenomenological,
    background=[tc_al_phenomenological, tc_li_phenomenological],
    reason="铝（偏差 58%→20%）和锂（偏差 3 个数量级→1 个数量级）"
    "两个案例共同支撑总结论。",
)
