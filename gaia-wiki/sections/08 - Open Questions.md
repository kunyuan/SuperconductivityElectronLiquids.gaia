---
type: section
section_number: 8
title: "开放问题与研究路线图"
tags: [section, open-questions]
---

# 08 - 开放问题与研究路线图

## 概要

这个知识包构建了一个从第一性原理预测简单金属超导 $T_c$ 的完整框架，其核心价值在于消除了库仑赝势 $\mu^*$ 的唯象不确定性。然而，推理图清晰地显示这一框架的"完整性"是有条件的——它依赖于一系列近似，每一个都有明确的适用边界。要让知识包真正完整，最需要补充的是**对下折叠近似本身的独立验证**——不是在 RPA 玩具模型中，而是在包含精确顶点修正的真实计算中。这是目前推理链中最薄弱的一环（downfolded BSE belief 仅 0.33），也是信息价值最高的单一改进。

从更宏观的视角看，论文建立的框架目前严格限制在简单金属——弱晶格势、近自由电子、三维、$\omega_D/E_F \ll 1$。将其推广到过渡金属、二维材料、氢化物等体系需要突破多个理论和计算瓶颈，每一个都构成独立的研究方向。

## 核心科学问题

- [[main_question|#15 main_question]]: 库仑赝势 $\mu^*$ 能否从第一性原理以受控精度计算？这能否产生对简单金属 $T_c$ 的定量预测？论文对这一问题给出了肯定的回答——但推理图显示回答的可信度因环节而异：$\mu^*$ 的可计算性（中等可信），$T_c$ 预测的准确性（高可信度，主要来自实验验证），整个理论框架的严格性（有待加强）。

## 实验空白

**锂的低温晶体结构**。锂在超低温下的晶体结构（9R vs HCP vs 其他）仍有争议，这直接影响 $\lambda$ 和 $\mu^*$ 的输入值。论文的两种结构给出 $T_c$ 相差近两个数量级（$5 \times 10^{-3}$ K vs $0.03$ K），说明晶体结构的不确定性是目前限制锂 $T_c$ 预测的首要因素。高分辨率低温 X 射线或中子衍射实验可以解决这一问题，从而将锂从一个模糊的验证案例变成一个干净的基准。这一空白直接影响 [[tc_li_predicted]]（belief 0.90）和 [[tc_li_experimental]]（belief 0.94）的可靠性。

**铝高压超导的实验延伸**。论文预测铝的超导在约 60 GPa 消失，但现有实验数据只到 6 GPa。将高压超导测量延伸到 20--60 GPa 范围，可以直接检验或否证框架最具标志性的新预测之一。这对 [[al_pressure_transition]]（belief 0.77）有直接影响——如果实验观测到超导在 60 GPa 附近消失（或不消失），belief 将发生重大更新。

**钠和镁的量子临界标度**。论文预测钠和镁处于超导-正常态量子相变附近，配对场感应率 $\chi \sim \ln(T)$ 应在 10 K 以下显现。这一量子临界标度行为无需微调，可以通过精密的低温配对场感应率测量来验证。如果观测到，它将为 $\mu^*$ 和 $\lambda$ 的精细平衡提供直接的实验证据。这一空白影响 [[tc_mg_na_near_qpt]]（belief 0.77）。

**准粒子有效质量的独立测量**。$m^*/m \approx 1$ 是连接 EFT 和 DFPT 的 $\lambda$ 的关键桥梁（[[quasiparticle_mass_near_unity]]，belief 0.88）。de Haas-van Alphen 或 ARPES 实验可以在简单金属中独立测量 $m^*/m$，为这一假设提供直接的实验约束。

## 计算空白

**超越 RPA 的下折叠验证**。目前对下折叠近似的数值验证仅使用 RPA 作为电子顶点的近似（玩具模型，Fig. 5）。需要用 vDiagMC 计算的精确四点顶点重复全 BSE vs 下折叠 BSE 的对比，在多个 $r_s$ 值下（特别是 $r_s \geq 3$，对应锂和钠的密度区间）检验下折叠近似的精度。这是目前信息价值最高的单一计算改进，直接影响 [[downfolded_bse]]（belief 0.33）和所有下游 claim。

**交叉项的直接数值评估**。[[cross_term_suppressed]]（belief 0.50）是整个推理链中最大的单一不确定性来源之一。通过在精确的多体框架中直接计算 $\tilde\Gamma^e \cdot \phi \cdot W^{\mathrm{ph}}$ 交叉项的贡献——而不是依赖等离子体极模型的解析估计——可以将这一 claim 的 belief 大幅提升（或发现它实际上不够小）。

**vDiagMC 在 $r_s > 5$ 时的收敛性**。论文声称 vDiagMC "validated at $r_s \leq 5$"，但锂的有效 $r_s \approx 5.7$ 已超出这一范围。在 $r_s = 5$--$8$ 区间系统地测试图解级数的收敛性，将澄清锂 $T_c$ 预测偏差的一个可能来源。这影响 [[vdiagmc_method]]（belief 0.84）和 [[mu_vdiagmc_values]]（belief 0.55）。

**带质量修正的系统研究**。UEG 到材料映射中的带质量修正 $r_s \to (m_b/m) r_s$ 是一个关键步骤，但其精度从未被系统验证。通过对已知简单金属进行 DFT+DMFT 计算来独立估计准粒子质量，可以交叉验证从能带曲率提取的 $m_b$ 值。这直接影响 [[ueg_pseudopotential_parameterization]]（belief 0.85）和 [[mu_available_for_simple_metals]]（belief 0.41）。

**Eliashberg 方程的完整频率依赖求解**。论文使用 PCF 外推预测 $T_c$，但完整频率依赖的 Eliashberg 方程求解可以提供额外的交叉验证——特别是对于 $\lambda$ 接近 $\mu^*$ 的精细平衡体系（锂、钠、镁），两种方法可能给出略有不同的 $T_c$。

## 理论空白

**二维系统的下折叠**。论文明确指出，在二维电子气中等离子体模式无隙（$\omega_p \propto \sqrt{q}$），交叉项压低论证失效。Simonato, Katsnelson, Rosner (2023) 已指出层状超导体中非局域库仑相互作用需要更仔细的处理。这严重限制了框架对碱金属插层石墨烯、过渡金属二硫化物等层状超导体的适用性。需要发展新的理论方案来处理二维中 $\omega_c/\omega_p$ 不再是小参数的情况。这是 [[downfolding_validity_limits]]（belief 0.92）中明确标记的失效模式。

**非局域 $\mu^*$ 的处理**。Morel-Anderson 常赝势假设（[[ma_pseudopotential_justified]]，belief 0.77）在简单金属中由能量尺度分离保证，但在具有强 Van Hove 奇点或平带的材料中，费米面附近的态密度变化剧烈，$\mu^*$ 可能具有显著的频率和动量依赖性。发展处理非局域 $\mu^*$ 的理论是将框架推广到非简单金属的先决条件。

**强电子-声子耦合体系**。论文的框架要求 $\omega_D/E_F \ll 1$，但在高压氢化物（$\omega_D/E_F \sim 0.1$）中这一条件不满足。更一般地，Migdal 定理在强耦合极限失效时，BSE 核的分解 $\tilde\Gamma = \tilde\Gamma^e + W^{\mathrm{ph}}$ 不再精确——需要包含更高阶的 phonon vertex corrections。Esterlis et al. (2018) 和 Chubukov et al. (2020) 已系统地讨论了 ME 理论崩溃的条件。这一限制影响 [[adiabatic_approx]]（belief 0.71）和 [[bse_kernel_decomposition]]（belief 0.78）。

**Umklapp 散射的系统处理**。论文假设简单金属中 Umklapp 散射可以忽略，但对于某些材料（特别是 HCP 结构的锌和镁），Umklapp 过程可能对费米面平均的准粒子散射振幅产生非平凡贡献。论文附录 A 提供了一般化的 $(\mathbf{k}, \mathbf{G})$ 形式体系，但实际计算中并未使用。需要在多带框架中评估 Umklapp 对 $\mu^*$ 的修正。

## 影响分析

按推理图中的"信息价值"（即改善该空白对多少下游结论的 belief 产生正面影响）排序：

1. **超越 RPA 的下折叠验证**（影响范围最广）：直接提升 [[downfolded_bse]]（0.33）的 belief，进而级联影响 [[lambda_microscopic_definition]]（0.50）、[[mu_microscopic_definition]]（0.54）、[[downfolded_me_equation]]（0.66）、[[ab_initio_workflow]]（0.96）以及全部 6 个 $T_c$ 预测。

2. **交叉项的直接数值评估**（影响次广）：直接影响 [[cross_term_suppressed]]（0.50），通过下折叠 BSE 级联影响全部下游。如果确认交叉项确实不到 1%，belief 将大幅上升；如果发现达到 5%，则需要修正整个框架。

3. **vDiagMC 在高 $r_s$ 的系统验证**：直接影响 [[mu_vdiagmc_values]]（0.55），进而影响 [[mu_available_for_simple_metals]]（0.41）和全部 $T_c$ 预测。对锂的预测改善最为关键。

4. **锂晶体结构的实验确定**：直接影响 [[tc_li_predicted]]（0.90）和 [[tc_li_experimental]]（0.94）。虽然影响范围窄（仅锂），但信息价值高——它可以将锂从一个模糊案例变成精确的基准验证。

5. **铝高压超导实验**：直接影响 [[al_pressure_transition]]（0.77）。这是一个纯粹的新预测验证——目前框架的高压外推没有实验约束。

## 建议的下一步

1. **[高影响/中等难度] 用精确顶点验证下折叠**。在 $r_s = 2$、3、4 下，用 vDiagMC 计算的精确四点顶点（而非 RPA）作为 BSE 核，对比全 BSE 和下折叠 BSE 的 $T_c$。这需要将现有的 vDiagMC 代码与全 BSE 求解器耦合，计算量大但技术上可行。预期成果：要么确认下折叠在 $r_s \leq 4$ 范围内精确到 1% 以内（将 [[downfolded_bse]] 的 belief 从 0.33 提升到 0.7+），要么量化出系统偏差并建议修正。

2. **[高影响/低难度] 直接计算交叉项**。在 UEG 中使用 vDiagMC 数值地评估 $\tilde\Gamma^e \cdot \phi \cdot W^{\mathrm{ph}}$ 交叉项与主要项的比值，覆盖 $r_s \in [1, 5]$。这利用现有的 vDiagMC 基础设施，可能只需几周的计算时间。预期成果：给出交叉项大小的精确上界，直接提升 [[cross_term_suppressed]] 的 belief。

3. **[中等影响/低难度] 锂低温晶体结构的实验确定**。与实验组合作，在 sub-mK 温度下对锂进行高分辨率结构表征。这不需要新的理论发展，但需要极低温实验技术。预期成果：消除锂 $T_c$ 预测中的最大非理论不确定性。

4. **[中等影响/高难度] 发展二维系统的下折叠理论**。针对等离子体模式无隙的二维电子气，发展新的能量尺度分离方案——可能需要放弃完全的 Coulomb-phonon 解耦，转而使用部分解耦或非微扰方法。这是一个开放的理论问题，难度高但影响深远——成功后框架可以推广到层状超导体。

5. **[低影响/中等难度] 铝高压超导实验到 20+ GPa**。利用金刚石对顶砧技术将铝的超导测量延伸到 20 GPa 以上。如果 $T_c$ 在 20 GPa 时确实低于 1 mK（如论文预测），现有技术可能无法直接观测到超导转变，但可以通过配对场感应率的压力依赖性间接验证。预期成果：铝高压预测的首次实验检验。

## 叶前提（知识空洞）

| # | Claim | 模块 | 内容 |
|---|-------|------|------|
| 02 | [[adiabatic_approx]] | [[motivation]] | 绝热近似：$\omega_D / E_F \ll 1$ |
| 03 | [[bts_renormalization]] | [[motivation]] | BTS 重正化关系 |
| 04 | [[me_downfolding_is_phenomenological]] | [[motivation]] | ME 下折叠的唯象性 |
| 05 | [[phenomenological_me_theory]] | [[motivation]] | 唯象 ME 理论的局限性 |
| 06 | [[mu_star_phenomenological]] | [[motivation]] | $\mu^*$ 作为唯象参数 |
| 07 | [[rpa_predicts_attractive_mu]] | [[motivation]] | RPA 预测吸引的 $\mu^*$ |
| 08 | [[dfpt_computes_lambda]] | [[motivation]] | DFPT 计算 $\lambda$ |
| 09 | [[tc_al_experimental]] | [[motivation]] | 铝实验 $T_c = 1.2$ K |
| 10 | [[tc_li_experimental]] | [[motivation]] | 锂实验 $T_c \approx 4 \times 10^{-4}$ K |
| 11 | [[tc_zn_experimental]] | [[motivation]] | 锌实验 $T_c = 0.875$ K |
| 12 | [[tc_al_phenomenological]] | [[motivation]] | 铝唯象 $T_c \approx 1.9$ K |
| 13 | [[tc_li_phenomenological]] | [[motivation]] | 锂唯象 $T_c \approx 0.35$ K |
| 14 | [[tc_zn_phenomenological]] | [[motivation]] | 锌唯象 $T_c \approx 1.37$ K |
| 15 | [[main_question]] | [[motivation]] | 核心科学问题 |
| 16 | [[electron_phonon_action]] | [[s2_model]] | 电子-声子作用量分解 |
| 17 | [[precursory_cooper_flow]] | [[s2_model]] | 前驱 Cooper 流 |
| 19 | [[cross_term_suppressed]] | [[s3_downfolding]] | 交叉通道项被压低 |
| 21 | [[downfolding_validity_limits]] | [[s3_downfolding]] | 下折叠适用范围 |
| 22 | [[ueg_vertex_challenge]] | [[s4_pseudopotential]] | UEG 四点顶点的计算挑战 |
| 23 | [[vdiagmc_method]] | [[s4_pseudopotential]] | vDiagMC 方法 |
| 24 | [[homotopic_expansion]] | [[s4_pseudopotential]] | Homotopic 展开 |
| 25 | [[ward_identity]] | [[s5_eph_coupling]] | Ward 恒等式 |
| 26 | [[gamma3_vdiagmc]] | [[s5_eph_coupling]] | vDiagMC 计算 $\Gamma_3$ |
| 27 | [[dfpt_eph_ansatz]] | [[s5_eph_coupling]] | DFPT 电子-声子表达式 |
| 28 | [[quasiparticle_mass_near_unity]] | [[s5_eph_coupling]] | 准粒子质量接近裸质量 |
| 34 | [[simple_metals_weak_lattice]] | [[s6_superconductors]] | 简单金属弱晶格效应 |
| 35 | [[ueg_pseudopotential_parameterization]] | [[s6_superconductors]] | UEG $\mu^*$ 参数化和映射 |
| 40 | [[rpa_vs_vdiagmc]] | [[s4_pseudopotential]] | RPA 与 vDiagMC 的矛盾 |
| 51 | [[bts_microscopic_equivalence]] | [[s3_downfolding]] | BTS 微观等价性 |
