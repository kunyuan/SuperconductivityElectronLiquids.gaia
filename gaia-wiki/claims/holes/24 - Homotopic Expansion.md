---
type: claim
label: homotopic_expansion
aliases: [homotopic_expansion]
claim_number: 24
qid: "github:superconductivity_electron_liquids::homotopic_expansion"
module: s4_pseudopotential
exported: false
prior: 0.88
belief: 0.8130342903509723
strategy_type: null
premise_count: 0
tags: [claim, s4-pseudopotential]
---

# #24 同伦展开

> 同伦变换提供了一种物理动机明确的图级数重组：通过将裸 Coulomb 相互作用 $v(q)$ 连续变形为在每个微扰阶都包含部分屏蔽的形式，级数收敛性得到显著改善。这使得 vDiagMC 计算能够在金属密度下以适中的图阶数（$n \lesssim 7$）获得四点顶角的收敛结果。

## 背景

在低温下直接计算准粒子散射振幅 $\gamma_T$ 的微扰级数时，第 $N$ 阶项因 Cooper 通道中嵌套的粒子-粒子泡而具有 $(\ln T)^N$ 的标度行为，导致级数在 $T < 0.01 E_F$ 时对数发散（见论文 Fig. 7 左图）。同伦展开通过定义 $\mu_{\omega_c}(\xi) = \gamma_T(\xi) / [1 - \gamma_T(\xi) \ln(\omega_c/T)]$（论文公式 30），将温度依赖的 $\gamma_T$ 级数转换为温度无关的 $\mu_{\omega_c}$ 级数。转换后各阶系数在 $T \to 0$ 时趋于常数（见论文 Fig. 7 右图），从而实现可靠的 $\mu_{E_F}$ 提取。

## 来源

- **数学基础**：假设 $\gamma_T(\xi)$ 作为辅助参数 $\xi$ 的函数具有解析性；利用保角映射技术将物理点 $\xi = 1$ 映射到收敛域内。
- **对数发散的消除**：严格——BTS 对数的反项精确对消了 $\gamma_T$ 展开中的 $(\ln T)^N$ 项。
- **收敛性验证**：论文 Fig. 7 展示了在 $r_s = 1$ 时，$\mu_{\omega_c}$ 的部分和快速收敛到明确定义的 $T \to 0$ 极限。
- **已知局限**：保角映射依赖于解析性假设；在 $r_s$ 较大时可能需要更高阶以确保收敛。

## 评审

**先验概率（Prior）**：0.88
**理由**：对数发散消除严格可靠；保角映射依赖于解析性假设。
**信念度（Belief）**：0.81

## 支撑

- → [[mu_vdiagmc_values|#37 vDiagMC 计算的 $\mu$ 数值]] 经由 noisy_and 推理

## 所属模块

[[s4_pseudopotential|Coulomb 赝势]]
