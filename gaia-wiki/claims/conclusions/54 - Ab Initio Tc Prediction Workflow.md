---
type: claim
label: ab_initio_workflow
aliases: [ab_initio_workflow]
claim_number: 54
qid: "github:superconductivity_electron_liquids::ab_initio_workflow"
module: s6_superconductors
exported: true
prior: null
belief: 0.9585800640635338
strategy_type: deduction
premise_count: 3
tags: [claim, s6-superconductors]
---

# #54 第一性原理 $T_c$ 预测工作流 (Ab Initio Tc Prediction Workflow)

完整的第一性原理工作流预测简单金属的 $T_c$：(1) 通过 vDiagMC 从 UEG 四点顶点计算 $\mu_{E_F}$，(2) 映射到材料的 $r_s$ 并通过 BTS 关系降标到 $\mu^*$，(3) 从 DFPT 获取 $\lambda$，(4) 求解下折叠 Eliashberg 方程（或使用 PCF 外推）预测 $T_c$。所有输入均来自第一性原理，不含可调参数。

## 背景

传统的电子-声子超导理论使用 McMillan（或 Allen-Dynes）公式，以 $\lambda$ 和 $\mu^*$ 作为输入来预测 $T_c$。由于 $\mu^*$ 无法从第一性原理可靠计算，通常被赋予经验值 $\mu^* \in [0.1, 0.2]$。对于亚开尔文 $T_c$ 的材料，$T_c \propto \exp(-1/g)$ 对 $\mu^*$ 的指数敏感性使得预测不确定性跨越数个量级。本工作流消除了这一唯象输入。

## 推导

**策略**: 演绎推理 (deduction)，经由复合推理 (composite) 分两步完成

**前提**:
- [[downfolded_bse|#43 下折叠 BSE]]
- [[mu_available_for_simple_metals|#41 简单金属的 $\mu^*$ 可用性]]
- [[dfpt_reliable_for_simple_metals|#53 DFPT 对简单金属的可靠性]]

### 工作流总览

![[13_0.jpg]]
*Fig. 9 | 超越弱关联极限的电子-声子超导第一性原理框架。多电子性质（蓝色框）——准粒子态密度 $N_F^*$、准粒子权重 $z_e$、密度-密度关联函数以及费米面上的三点 ($\Gamma_3^e$) 和四点 ($\Gamma_4^e$) 顶点函数——通过高阶变分介图蒙特卡洛计算。这些量作为声子介导吸引（红色框）和库仑赝势的输入。$\mu^*$ 从费米面平均的 Cooper 通道准粒子散射推导。临界温度和能隙函数通过正常相中反常顶点的前驱 Cooper 流计算。*

工作流沿两个互联方向进行：关联电子部分（蓝色框）和声子相关部分（红色框）：

**关联电子部分**：计算三个关键量
1. **密度-密度关联函数** $\chi^e(q)$
2. **准粒子顶点修正**（经介电函数屏蔽）$z^e \Gamma_3^e(k, q)/\epsilon_q$
3. **费米面平均的静态准粒子散射振幅** $z_e^2 N_F^* \langle \Gamma_q^e \rangle_{\mathrm{FS}}$——提取 $\mu^*$ 的关键

**声子部分**：
- 关联电子的输出 $\chi^e$ 和 $z^e \Gamma_3^e$ 输入声子部分
- 有效质量密度用于声子色散重整化
- $z^e \Gamma_3^e$ 处理被电子关联修饰的准粒子间电子-声子相互作用的屏蔽和重整化

**最终组装**：将 $\lambda$ 和 $\mu^*$ 代入下折叠 ME/BSE 方程，求解得到 $T_c$、频率依赖的反常顶点 $\Lambda(\omega)$ 和临界点处的超导能隙函数 $\Delta(\omega)$。

### 第一步：$\mu^*$ 的第一性原理确定

vDiagMC 的 UEG 计算提供了 $\mu_{E_F}(r_s)$ ([[mu_vdiagmc_values|#37]])。参数化程序 ([[ueg_pseudopotential_parameterization|#35]]) 利用材料特定的 $r_s$ 和带质量将其映射到实际材料，正当化依据是简单金属中弱的晶格效应 ([[simple_metals_weak_lattice|#34]])。BTS 关系将 $\mu_{E_F}$ 降标到 Debye 频率处的 $\mu^*$。

具体映射方法：将金属的能带结构用 UEG 模型拟合。UEG 密度设为传导电子密度；裸质量从 $\Gamma$ 点能带色散的曲率提取为带质量 $m_b$。$m_b$ 有效地重标 $r_s$ 参数：$r_s \to (m_b/m) r_s$。然后在重标的 $r_s$ 值处插值预算的 UEG 赝势结果。

### 第二步：$\lambda$ 的第一性原理确定

EFT 顶点与 DFPT 的吻合 ([[dfpt_reliable_for_simple_metals|#53]]) 确保 DFPT 计算的 $\lambda$ 可以直接使用。具体使用 Quantum ESPRESSO 的 DFPT 方法和 EPW 包计算电子-声子耦合（详见 Section VI.A）。

### 第三步：前驱 Cooper 流预测 $T_c$

下折叠 BSE ([[downfolded_bse|#43]]) 提供理论方程。关键优势在于使用**前驱 Cooper 流** (PCF) 方法：在 $T \gg T_c$ 的正常态计算反常顶点，利用普适标度关系（方程 10）：
$$\Lambda_0 = \frac{1}{1 + g \ln(\omega_\Lambda/T)} + \mathcal{O}(T)$$

通过在多个 $T > T_c$ 处计算 $\Lambda_0$ 并按 PCF 标度外推，准确预测 $T_c$ 而无需在 $T_c$ 处直接求解——这对极低 $T_c$ 超导体至关重要，因为传统方法需要极密的计算网格。

## 评审

- **Prior**: 依赖前提推断
- **Justification**: 工作流的每个组件都有独立的第一性原理验证；主要不确定性在 UEG 到材料的映射步骤。
- **Belief**: 0.959

## 支撑

- $\to$ [[tc_al_predicted|#55 $T_c$(Al) 第一性原理预测]] via noisy_and
- $\to$ [[tc_zn_predicted|#56 $T_c$(Zn) 第一性原理预测]] via noisy_and
- $\to$ [[tc_li_predicted|#57 $T_c$(Li) 第一性原理预测]] via noisy_and
- $\to$ [[al_pressure_transition|#58 Al 压力-$T_c$ 转变]] via noisy_and
- $\to$ [[tc_mg_na_near_qpt|#59 Na 和 Mg 接近量子相变]] via noisy_and

## 意义

这是首个不含可调参数的电子-声子超导第一性原理框架。通过将库仑赝势的微观计算、DFPT 电子-声子耦合的验证和前驱 Cooper 流方法结合，该工作流能够预测低温超导性和量子相变点——这远超传统 Migdal-Eliashberg 方法的能力范围。

## 注意事项

1. 工作流基于两个假设：(i) 芯带和传导带被大能隙分开，(ii) 传导电子经历的晶格势较弱，允许忽略 Umklapp 散射。
2. 不适用于具有强晶格势（如 Be）、显著芯电子贡献（如 Fe, Cu）、强自旋-轨道耦合（如 Ta）、费米面附近平带（如 Ca）或高 $T_c$（$T_c \gg 1$ K，如 Pb）的材料。
3. 该框架原则上适用于任何具有良好定义的费米面准粒子和大声子/电子能标分离的关联材料，但将高阶介图和重整化推广到复杂能带结构是重大技术挑战。

## 所属模块
[[s6_superconductors]]
