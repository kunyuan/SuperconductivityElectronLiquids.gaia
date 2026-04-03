"""Self-review for the superconductivity electron liquids package.

Review 原则：只对推理链最底层的独立前提（没有 given、不是任何 strategy
的 conclusion）给出 prior。推导结论的 belief 完全由 BP 从前提传播。
"""

from gaia.review import (
    ReviewBundle,
    review_claim,
    review_generated_claim,
    review_strategy,
)

from .. import (
    # 独立前提 — Section I
    adiabatic_approx,
    electron_gas_model,
    # 独立前提 — Section II
    electron_phonon_action,
    bse_kernel_decomposition,
    # 独立前提 — Section III
    pair_propagator_decomposition,
    cross_term_suppressed,
    pseudopotential_scale_relation,
    rpa_predicts_negative_mu,
    downfolding_validated,
    downfolding_limitations,
    # 独立前提 — Section IV
    ueg_vertex_challenge,
    homotopic_expansion,
    vdiagmc_method,
    # 独立前提 — Section V
    individual_corrections_large,
    corrections_cancel,
    dfpt_validated_numerically,
    ward_identity_hypothesis,
    # 推导结论（需要中性 prior=0.5 满足 validator 要求，belief 由 BP 传播）
    precursory_cooper_flow,
    downfolded_bse,
    mu_vdiagmc_values,
    dfpt_reliable_for_simple_metals,
    ab_initio_workflow,
    # Strategies（用于 strategy review）
    derive_downfolded_bse,
    derive_pcf,
    derive_mu_values,
    derive_dfpt_reliable,
    derive_workflow,
    derive_improvement,
    explain_dfpt_cancellation,
    # 推导结论的 claim（只需 strategy review，不需要独立 prior）
    tc_aluminum,
    tc_lithium,
    tc_mg_na_near_qpt,
    al_pressure_transition,
    tc_improvement_over_phenomenological,
)

REVIEW = ReviewBundle(
    source_id="self_review",
    model="human-expert-assessment",
    objects=[
        # ════════════════════════════════════════════
        # 独立前提的 Prior
        # ════════════════════════════════════════════

        # Section I — 基础假设
        review_claim(adiabatic_approx, prior=0.95,
                     justification="绝热近似在传统金属中广泛成立，Migdal 定理已被大量验证。"),
        review_claim(electron_gas_model, prior=0.90,
                     justification="均匀电子气通过 LDA 支撑了 DFT 的成功，是公认的简单金属参考系统。"),

        # Section II — 理论框架
        review_claim(electron_phonon_action, prior=0.90,
                     justification="作用量分解在附录 A 中有完整推导，反项构造避免重复计数的论证严格。"),
        review_claim(bse_kernel_decomposition, prior=0.88,
                     justification="BSE 核的 Coulomb/声子分解依赖 Migdal 定理，误差项有明确量级估计。"),

        # Section III — Downfolding
        review_claim(pair_propagator_decomposition, prior=0.88,
                     justification="配对传播子分解是标准的 Wilsonian 重整化群操作，数学上严格。"),
        review_claim(cross_term_suppressed, prior=0.82,
                     justification="交叉项压制依赖 $\\omega_c^2/\\omega_p^2 \\lesssim 0.01$，对大多数金属成立。"),
        review_claim(pseudopotential_scale_relation, prior=0.92,
                     justification="BTS 关系是重整化群的标准结果，已在文献中广泛验证。"),
        review_claim(rpa_predicts_negative_mu, prior=0.50,
                     justification="动态 RPA 对 $r_s > 2$ 预测负 $\\mu^*$ 是文献已知结果，"
                     "但物理合理性受到本文质疑。设 0.5 反映不确定性。"),
        review_claim(downfolding_validated, prior=0.88,
                     justification="0.2% 的精度差异通过显式数值对比获得，基准测试令人信服。"),
        review_claim(downfolding_limitations, prior=0.90,
                     justification="适用性边界论证清晰，三类失效体系的物理机制明确。"),

        # Section IV — VDiagMC 方法
        review_claim(ueg_vertex_challenge, prior=0.92,
                     justification="传统 QMC 方法无法获取四点顶点函数是该领域公认的技术限制。"),
        review_claim(homotopic_expansion, prior=0.85,
                     justification="同伦展开的收敛改善在论文图 7 中有数值展示，级数快速收敛。"),
        review_claim(vdiagmc_method, prior=0.88,
                     justification="VDiagMC 是已验证的方法，Parquet 方程和重整化策略有坚实理论基础。"),

        # Section V — DFPT 验证
        review_claim(individual_corrections_large, prior=0.90,
                     justification="各项修正的大小在 VDiagMC 计算中直接可见，是数值事实。"),
        review_claim(corrections_cancel, prior=0.88,
                     justification="抵消在 $r_s \\in [1,5]$ 和 $|q| \\leq 2k_F$ 范围内数值验证。"),
        review_claim(dfpt_validated_numerically, prior=0.88,
                     justification="EFT 与 DFPT 的逐点数值一致性是直接计算结果。"),
        review_claim(ward_identity_hypothesis, prior=0.70,
                     justification="Ward 恒等式在 QFT 中已确立，但其在 DFPT 抵消中的具体角色"
                     "尚未被严格证明对所有金属成立。"),

        # ════════════════════════════════════════════
        # 推导结论 — 中性 prior（validator 要求，belief 由 BP 传播）
        # ════════════════════════════════════════════
        review_claim(precursory_cooper_flow, prior=0.5,
                     justification="推导结论，belief 由前提通过 BP 传播。"),
        review_claim(downfolded_bse, prior=0.5,
                     justification="推导结论，belief 由前提通过 BP 传播。"),
        review_claim(mu_vdiagmc_values, prior=0.5,
                     justification="推导结论，belief 由前提通过 BP 传播。"),
        review_claim(dfpt_reliable_for_simple_metals, prior=0.5,
                     justification="推导结论，belief 由前提通过 BP 传播。"),
        review_claim(ab_initio_workflow, prior=0.5,
                     justification="推导结论，belief 由前提通过 BP 传播。"),
        review_claim(tc_aluminum, prior=0.5,
                     justification="推导结论，belief 由前提通过 BP 传播。"),
        review_claim(tc_lithium, prior=0.5,
                     justification="推导结论，belief 由前提通过 BP 传播。"),
        review_claim(tc_mg_na_near_qpt, prior=0.5,
                     justification="推导结论，belief 由前提通过 BP 传播。"),
        review_claim(al_pressure_transition, prior=0.5,
                     justification="推导结论，belief 由前提通过 BP 传播。"),
        review_claim(tc_improvement_over_phenomenological, prior=0.5,
                     justification="推导结论，belief 由前提通过 BP 传播。"),

        # ════════════════════════════════════════════
        # Strategy reviews（条件概率）
        # ════════════════════════════════════════════

        # 显式定义的 noisy_and 策略
        review_strategy(derive_downfolded_bse, conditional_probability=0.92,
                        justification="配对传播子分解 + 交叉项压制 + 绝热近似 → downfolded BSE。"),
        review_strategy(derive_pcf, conditional_probability=0.88,
                        justification="作用量分解 + BSE 核分解 + 绝热近似 → PCF 标度律。"),
        review_strategy(derive_mu_values, conditional_probability=0.90,
                        justification="三项方法论进展共同使 μ 值精确计算成为可能。"),
        review_strategy(derive_dfpt_reliable, conditional_probability=0.90,
                        justification="大修正抵消 + 数值验证 → DFPT 对简单金属可靠。"),
        review_strategy(derive_workflow, conditional_probability=0.88,
                        justification="三个独立组件集成为无参数工作流。"),
        review_strategy(derive_improvement, conditional_probability=0.92,
                        justification="铝和锂的成功预测直接支撑总结论。"),

        # claim(..., given=[...]) 自动创建的 noisy_and 策略
        review_strategy(tc_aluminum.strategy, conditional_probability=0.90,
                        justification="工作流应用于铝的材料参数给出 Tc 预测。"),
        review_strategy(tc_lithium.strategy, conditional_probability=0.90,
                        justification="工作流应用于锂的材料参数给出 Tc 预测。"),
        review_strategy(tc_mg_na_near_qpt.strategy, conditional_probability=0.85,
                        justification="工作流对镁钠的外推可信度稍低。"),
        review_strategy(al_pressure_transition.strategy, conditional_probability=0.80,
                        justification="压力效应预测涉及额外近似。"),
        review_strategy(tc_improvement_over_phenomenological.strategy,
                        conditional_probability=0.92,
                        justification="两个成功案例充分支撑总结论。"),

        # abduction — formalized
        review_strategy(explain_dfpt_cancellation,
                        justification="溯因推理：Ward 恒等式解释 DFPT 抵消。"),

        # ════════════════════════════════════════════
        # Generated claim review (abduction interface)
        # ════════════════════════════════════════════
        review_generated_claim(explain_dfpt_cancellation, "alternative_explanation",
                               prior=0.25,
                               justification="替代解释（数值巧合）不合理，抵消在整个参数范围内系统性成立。"),
    ],
)
