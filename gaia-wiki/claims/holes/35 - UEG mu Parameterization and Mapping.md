---
type: claim
label: ueg_pseudopotential_parameterization
aliases: [ueg_pseudopotential_parameterization]
claim_number: 35
qid: "github:superconductivity_electron_liquids::ueg_pseudopotential_parameterization"
module: s6_superconductors
exported: false
prior: 0.85
belief: 0.8492381929361125
strategy_type: null
premise_count: 0
tags: [claim, s6-superconductors]
---

# #35 UEG $\mu^*$ 参数化与材料映射

> 由 vDiagMC 计算的 UEG Coulomb 赝势 $\mu_{E_F}(r_s)$ 可参数化为 $r_s$ 的光滑函数，并通过材料的有效 $r_s$（由价电子密度决定）映射到实际材料。结合 BTS 关系将 $\mu_{E_F}$ 跑动到 Debye 标度，即可无需额外可调参数地获得任意简单金属的 $\mu^*(r_s)$。

## 背景

本文建立的 UEG-材料映射程序是 ab initio 工作流的核心组件。具体步骤为：(i) 从材料的晶格常数和价电子数计算 UEG 密度参数 $r_s$；(ii) 从 $\Gamma$ 点处能带色散的曲率提取带质量 $m_b$，通过 $r_s \to (m_b/m) r_s$ 进行有效 $r_s$ 重标度；(iii) 在预计算的 $\mu_{E_F}(r_s)$ 曲线上插值（见论文 Fig. 4 和 Table I），得到 Fermi 能标度的裸赝势；(iv) 通过 BTS 关系跑动到 Debye 频率标度，得到 $\mu^*$。

论文 Table I 给出了 $r_s = 1$--$6$ 的 $\mu_{E_F}$ 精确数值：$\mu_{E_F}$ 从 $r_s = 1$ 时的 0.28 单调递增到 $r_s = 5$ 时的 1.3，显著大于静态 RPA 和 Morel-Anderson 估计（后者在 $r_s = 5$ 时低 3 倍）。

## 来源

- **数据来源**：vDiagMC 计算的 UEG 四点顶角函数，$r_s = 1$--$6$（论文 Table I、Fig. 4）。
- **映射过程**：$r_s$ 重标度 + $\mu_{E_F}$ 插值 + BTS 跑动。
- **已知局限**：带质量修正引入额外不确定性；该映射仅适用于近自由电子金属（弱晶格势），不适用于具有强 Umklapp 散射、强自旋-轨道耦合或平带结构的材料。

## 评审

**先验概率（Prior）**：0.85
**理由**：映射程序合理；带质量修正增加了一定不确定性。
**信念度（Belief）**：0.85

## 支撑

- → [[mu_available_for_simple_metals|#41 简单金属可获得 $\mu^*$]] 经由 noisy_and 推理
- → [[ab_initio_workflow|#54 第一性原理 $T_c$ 预测工作流]] 经由推断

## 所属模块

[[s6_superconductors|常规超导体]]
