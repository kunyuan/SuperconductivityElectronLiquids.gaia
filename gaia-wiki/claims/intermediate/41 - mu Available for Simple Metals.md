---
type: claim
label: mu_available_for_simple_metals
aliases: [mu_available_for_simple_metals]
claim_number: 41
qid: "github:superconductivity_electron_liquids::mu_available_for_simple_metals"
module: s6_superconductors
exported: false
prior: null
belief: 0.41189145326887094
strategy_type: noisy_and
premise_count: 2
tags: [claim, s6-superconductors]
---

# #41 简单金属的 $\mu^*$ 可用性 (mu* Available for Simple Metals)

对于简单金属，库仑赝势 $\mu^*$ 可以无需可调参数地从第一性原理获得：vDiagMC 计算的均匀电子气 $\mu_{E_F}(r_s)$ 通过材料特定的 $r_s$ 和带质量映射到实际材料，然后通过 BTS 重整化关系降标到 Debye 频率。

## 背景

从 UEG 的计算结果到实际材料预测的桥梁需要两个步骤：(1) 将 UEG 参数化映射到材料，(2) 从费米能降标到 Debye 频率。

## 推导

**策略**: noisy_and

**前提**:
- [[ueg_pseudopotential_parameterization|#35 UEG $\mu^*$ 参数化和映射]]
- [[mu_vdiagmc_values|#37 vDiagMC 计算的库仑赝势]]

vDiagMC 结果提供了 UEG 的 $\mu_{E_F}(r_s)$ ([[mu_vdiagmc_values|#37]])。参数化程序 ([[ueg_pseudopotential_parameterization|#35]]) 利用材料特定的 $r_s$（由价电子密度确定）和带质量 $m_b$（从 $\Gamma$ 点能带色散提取）将这些值映射到实际材料。带质量有效地重标 $r_s$：$r_s \to (m_b/m) r_s$。

映射的正当化依据是简单金属中弱的晶格效应 ([[simple_metals_weak_lattice|#34]])——近自由电子特性意味着费米面近似球对称，电子结构可以被具有微小晶体场微扰的均匀电子气良好描述。

BTS 关系 ([[bts_renormalization|#03]]) 将 $\mu_{E_F}$ 降标到 Debye 频率处的 $\mu^*$，完成了从微观计算到 Eliashberg 方程输入的转换。

## 评审

- **Prior**: 依赖前提推断
- **Justification**: UEG 到材料的映射是主要的不确定性来源（特别是带质量修正）。
- **Belief**: 0.412

## 支撑

- $\to$ [[ab_initio_workflow|#54 第一性原理 $T_c$ 预测工作流]] via deduction

## 意义

建立了从 UEG 微观计算到实际材料应用的完整桥梁，使第一性原理 $\mu^*$ 成为可行的实用工具。

## 注意事项

1. 映射假设传导电子可以用 UEG 近似，不适用于强晶格势材料。
2. 带质量的提取引入了额外的不确定性——特别是对于具有复杂能带结构的材料。
3. UEG 中有效质量重整化很小（$m^*/m$ 偏差在子百分比水平），假设实际材料也如此，即 $m_b$ 可以解释为真正的准粒子有效质量。

## 所属模块
[[s6_superconductors]]
