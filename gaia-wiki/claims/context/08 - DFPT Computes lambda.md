---
type: claim
label: dfpt_computes_lambda
aliases: [dfpt_computes_lambda]
claim_number: 8
qid: "github:superconductivity_electron_liquids::dfpt_computes_lambda"
module: motivation
exported: false
prior: 0.92
belief: 0.92
strategy_type: null
premise_count: 0
tags: [claim, motivation]
---

# #08 DFPT 计算 $\lambda$

> 密度泛函微扰理论（DFPT）通过 Kohn-Sham 基态能量对晶格畸变的线性响应来计算电子-声子耦合常数 $\lambda$（量化 Fermi 面上声子介导吸引强度的无量纲参数）。DFPT 已在弱关联超导体中得到验证，但其对强关联体系的精度尚未知。

## 背景

DFPT 是当前 ab initio 超导预测的标准工具，通过 Quantum Espresso 和 EPW 等软件包实现。它利用 Kohn-Sham 势对离子位移的响应 $\delta V_{\mathbf{q}}^{\mathrm{KS}}$ 计算电子-声子矩阵元，然后 Fermi 面平均得到 $\lambda$。DFPT 的核心假设是：超越 Kohn-Sham 平均场的顶角修正已被交换-关联泛函吸收。本文的关键发现之一是，对于简单金属，EFT 顶角与 DFPT 结果在数值上高度一致，从而验证了 DFPT 在此类体系中的可靠性。

## 评审

**先验概率（Prior）**：0.92
**理由**：成熟的计算方法。
**信念度（Belief）**：0.92

## 所属模块

[[motivation|研究动机]]
