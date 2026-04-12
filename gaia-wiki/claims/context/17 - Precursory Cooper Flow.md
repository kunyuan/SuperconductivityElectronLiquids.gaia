---
type: claim
label: precursory_cooper_flow
aliases: [precursory_cooper_flow]
claim_number: 17
qid: "github:superconductivity_electron_liquids::precursory_cooper_flow"
module: s2_model
exported: false
prior: 0.9
belief: 0.9
strategy_type: null
premise_count: 0
tags: [claim, s2-model]
---

# #17 前驱 Cooper 流

> Fermi 面上反常顶角函数的低频极限 $\Lambda_0$ 满足普适标度关系（前驱 Cooper 流，PCF）：$\Lambda_0 = 1/(1 + g\ln(\omega_\Lambda/T)) + O(T)$，其中 $g$ 为无量纲耦合常数（$g < 0$ 对应净吸引），$\omega_\Lambda$ 为有效高能截断。当 $g < 0$ 时，$\Lambda_0$ 在 $T_c = \omega_\Lambda e^{1/g}$ 处发散；通过在正常态计算并外推，可预测 $T_c$。

## 背景

PCF 方法是本文 ab initio 工作流的关键计算工具。与传统方法（在 $T_c$ 附近求解线性化 gap 方程或追踪最大本征值 $h(T)$ 的温度依赖）相比，PCF 有两个显著优势：(i) 仅需在 $T \gg T_c$ 的几个温度点计算反常顶角，然后利用精确标度律外推至 $T_c$；(ii) 对于强排斥体系，$h(T)$ 的外推不可靠，而 PCF 标度律（公式 10）是精确的。这使得 PCF 能够预测极低的 $T_c$（如 Li 的亚毫开尔文 $T_c$）和量子相变点，远超常规 ME 方法的能力范围。

## 评审

**先验概率（Prior）**：0.90
**理由**：已在先前工作中验证。
**信念度（Belief）**：0.90

## 所属模块

[[s2_model|模型与基本关系]]
