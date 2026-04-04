"""Section I — Introduction: Background, motivation, and research question."""

from gaia.lang import claim, question, setting

PROVENANCE = [{"package_id": "paper:2512.19382", "version": "2024"}]

bcs_framework = setting(
    "Bardeen-Cooper-Schrieffer (BCS) 理论将传统超导解释为声子交换介导的"
    "电子 Cooper 配对所产生的宏观量子态。该理论需要输入净有效电子-电子"
    "相互作用强度，即声子介导的吸引耦合与屏蔽 Coulomb 排斥之间的平衡。",
    title="BCS 超导理论框架",
)

migdal_eliashberg = setting(
    "Migdal-Eliashberg (ME) 框架通过在实频率轴上求解电子自能的自洽方程，"
    "将 BCS 理论推广到强耦合区间。然而，该框架将 Coulomb 赝势 $\\mu^*$ "
    "作为唯象参数处理，通常通过拟合实验测量的超导转变温度 $T_c$ 来确定。"
    "对拟合参数的依赖限制了框架的预测能力，尤其是对于亚开尔文超导体，"
    "$\\mu^*$ 的微小变化会导致 $T_c$ 发生数量级变化。",
    title="Migdal-Eliashberg 框架",
)

adiabatic_approx = claim(
    "在传统金属中，Debye 频率 $\\omega_D$ 远小于 Fermi 能量 $E_F$"
    "（$\\omega_D / E_F \\ll 1$），建立了电子和声子能量尺度的分离。"
    "这一绝热条件由 Migdal（1958）首先利用，证明了电子-声子顶点修正"
    "是小量，从而允许向低能有效理论投影。",
    title="绝热近似与 Migdal 定理",
    provenance=[{"package_id": "paper:migdal-1958", "version": "1958"}],
)

electron_gas_model = claim(
    "均匀电子气（jellium 模型）在金属密度区间（Wigner-Seitz 半径 "
    "$r_s = 2$ 至 $6$）是简单金属理论的标准参考系统。其性质通过局域密度"
    "近似支撑了密度泛函理论，使其成为第一性原理多体方法的天然检验平台。",
    title="均匀电子气模型",
)

main_question = question(
    "Coulomb 赝势 $\\mu^*$——Migdal-Eliashberg 超导理论中的关键唯象参数"
    "——能否从第一性原理以可控精度计算？将第一性原理 $\\mu^*$ 值代入 "
    "Eliashberg 框架后，能否对简单金属的超导转变温度 $T_c$ 给出定量"
    "可靠的预测？",
    title="第一性原理计算 Coulomb 赝势",
)
