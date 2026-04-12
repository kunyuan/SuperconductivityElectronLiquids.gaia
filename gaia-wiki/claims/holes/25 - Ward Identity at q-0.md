---
type: claim
label: ward_identity
aliases: [ward_identity]
claim_number: 25
qid: "github:superconductivity_electron_liquids::ward_identity"
module: s5_eph_coupling
exported: false
prior: 0.98
belief: 0.9924348356443314
strategy_type: null
premise_count: 0
tags: [claim, s5-eph-coupling]
---

# #25 $q \to 0$ 极限下的 Ward 恒等式

> 一个精确的 Ward 恒等式将三点电子-声子顶角 $\Gamma_3^e(k, q)$ 与电子自能在长波极限 $q \to 0$ 下联系起来：$\lim_{q \to 0} \Gamma_3^e(k, q) = 1 - \partial\Sigma(k)/\partial\epsilon_k$。该恒等式是电荷守恒的直接推论，为零动量转移处的顶角修正提供了精确约束。

![[12_0.jpg]]

## 背景

Ward 恒等式是量子场论中最基本的恒等关系之一，源于规范对称性（电荷守恒）。在均匀电子气的电子-声子问题中，它将三点顶角 $\Gamma_3^e$ 在 $q \to 0$ 极限下精确地与有效质量联系起来：$\Gamma_3^e(k_F, q \to 0) = m^*/m$。由于简单金属的 $m^*/m \approx 1$（见 [[quasiparticle_mass_near_unity|#28]]），Ward 恒等式意味着在零动量转移处顶角修正几乎为 1。这为 $\Gamma_3^e$ 在有限 $q$ 处的行为提供了一个"锚点"，与 vDiagMC 在有限 $q$ 处的数值结果（见 [[gamma3_vdiagmc|#26]]）结合，可构建覆盖整个动量范围的可靠插值。

## 来源

- **理论地位**：精确的量子场论恒等式，从电荷守恒和连续性方程直接推导。
- **普适性**：对任何带电 Fermi 体系成立，不依赖于任何近似。
- **已知局限**：仅在 $q \to 0$ 极限严格成立；向有限 $q$ 的推广需要额外信息（vDiagMC 提供）。Ward 恒等式保证极限存在，但如果极限不是一致的，实际应用可能受限。

## 评审

**先验概率（Prior）**：0.98
**理由**：源于电荷守恒的精确量子场论恒等式。
**信念度（Belief）**：0.99

## 支撑

- → [[gamma3_approximation|#38 $\Gamma_3$ 近似]] 经由溯因推理
- → [[gamma3_approximation|#38 $\Gamma_3$ 近似]] 经由归纳推理

## 所属模块

[[s5_eph_coupling|电子-声子耦合]]
