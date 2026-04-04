"""Section V -- Electron-Phonon Coupling from Band Theory.

Shows that individual many-body corrections to the effective electron-phonon
coupling are large but nearly cancel, validating DFPT for simple metals.
Proposes Ward identity as the underlying explanation.
"""

from gaia.lang import abduction, claim, noisy_and

PROVENANCE = [{"package_id": "paper:2512.19382", "version": "2024"}]

individual_corrections_large = claim(
    "在有效场论（EFT）框架中，电子-电子相互作用对准粒子权重 $z^e$ 的修正、"
    "对屏蔽 Coulomb 相互作用 $v_q/\\varepsilon_q$ 的修正、以及对电子-声子"
    "顶点 $\\Gamma_3^e$ 的修正各自都很大，单独考虑时会显著偏离自由电子结果。",
    title="各项多体修正均很大",
    provenance=PROVENANCE,
)

corrections_cancel = claim(
    "尽管各项修正单独很大，它们在有效电子-声子耦合中几乎精确抵消："
    "$z^e \\cdot v_q/\\varepsilon_q \\cdot \\Gamma_3^e(k; q) \\approx "
    "v_q / [1 - (v_q + f_{xc}) \\cdot \\chi_0^e(q)]$，其中左侧是包含所有"
    "多体修正的 EFT 结果，右侧是基于线性响应理论的密度泛函微扰理论"
    "（DFPT）结果。图形化地说，电子-电子相互作用对准粒子权重 $z^e$ "
    "的贡献被电子-声子顶点重整化 $\\Gamma_3^e$ 有效抵消。",
    title="多体修正近精确抵消",
    provenance=PROVENANCE,
)

dfpt_validated_numerically = claim(
    "通过变分图形蒙特卡洛方法在 $r_s \\in [1, 5]$ 区间的数值验证，"
    "EFT 与 DFPT 在 Fermi 面上所有相关动量传递（$|q| \\leq 2k_F$）"
    "范围内给出近乎完全一致的有效电子-声子耦合 $\\lambda$ 值。",
    title="EFT 与 DFPT 数值一致",
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
    title="DFPT 对简单金属可靠",
    provenance=PROVENANCE,
)

ward_identity_hypothesis = claim(
    "Ward 恒等式和电子-声子顶点的规范不变性强制要求自能、屏蔽和顶点修正"
    "在长波极限下系统性地互相抵消。DFPT 中各项大修正的近精确抵消不是"
    "数值巧合，而是守恒律约束多体修正在物理可观测量中组合方式的必然结果。",
    title="Ward 恒等式解释抵消",
)

# ── Reasoning ──

derive_dfpt_reliable = noisy_and(
    premises=[individual_corrections_large, corrections_cancel, dfpt_validated_numerically],
    conclusion=dfpt_reliable_for_simple_metals,
    reason="各项多体修正单独很大，但在有效耦合中几乎精确抵消，"
    "并通过 VDiagMC 的逐点数值验证确认 → DFPT 对简单金属可靠。",
)

explain_dfpt_cancellation = abduction(
    observation=corrections_cancel,
    hypothesis=ward_identity_hypothesis,
    reason="各项修正的近精确抵消不是数值巧合，而是 Ward 恒等式"
    "约束多体修正在物理可观测量中组合方式的必然结果。",
)
