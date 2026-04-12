---
type: claim
label: rpa_predicts_attractive_mu
aliases: [rpa_predicts_attractive_mu]
claim_number: 7
qid: "github:superconductivity_electron_liquids::rpa_predicts_attractive_mu"
module: motivation
exported: false
prior: 0.5
belief: 0.2252990992227296
strategy_type: null
premise_count: 0
tags: [claim, motivation]
---

# #07 RPA 预测吸引性 $\mu^*$

> 在随机相位近似（RPA）框架内处理动态屏蔽 Coulomb 相互作用时，对于 Wigner-Seitz 半径 $r_s \gtrsim 2$（$r_s$ 正比于电子间距与 Bohr 半径之比，度量 Coulomb 相互作用与动能之比），预测 $\mu^* < 0$（即 Coulomb 效应在 Cooper 通道中变为净吸引）。然而，RPA 在 $r_s \gtrsim 1$ 时忽略了超越 RPA 的效应（如顶角修正和自能重整化），使其预测在此密度区间不可靠，并与大量实验证据矛盾。

## 背景

Takada (1978, 1993) 和 Rietschel-Sham 首先在 RPA 动态屏蔽框架内发现：Coulomb 势的动态效应可能导致 $\mu^* < 0$，从而在无声子情况下产生 s 波超导。后续研究扩展到所有配对通道后确认了这一数学结论。然而，该结果存在根本性的内部矛盾：RPA 在 $r_s \lesssim 1$ 时才是良好近似，而所预测的 Coulomb 配对出现在 $r_s \gtrsim 2$，恰恰是 RPA 已失控的区域。事实上，在 $r_s > 0.5$ 时静态 RPA 和动态 RPA 的结果已经大相径庭，这本身就说明近似已不可靠。本文通过 vDiagMC 的高阶精确计算证实，$\mu_{E_F}$ 在整个金属密度范围 $r_s \in [1, 6]$ 内始终为正且单调递增，从根本上否定了纯电子配对超导的 RPA 预测。

## 来源

- **理论来源**：RPA 动态屏蔽计算，Takada (1978, 1993)；Rietschel & Sham。
- **有效范围**：RPA 在 $r_s \lesssim 1$ 时精确；$r_s > 1$ 时顶角修正不可忽略。
- **与实验矛盾**：所有已知常规超导体的超导均需要声子介导的吸引。

## 评审

**先验概率（Prior）**：0.50
**理由**：RPA 计算在技术上正确；但其物理内容在 $r_s > 1$ 时存在根本不确定性。
**信念度（Belief）**：0.23

## 支撑

- → [[rpa_vs_vdiagmc|#40 RPA 与 vDiagMC 矛盾]] 经由矛盾关系

## 所属模块

[[motivation|研究动机]]
