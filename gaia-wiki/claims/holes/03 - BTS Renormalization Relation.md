---
type: claim
label: bts_renormalization
aliases: [bts_renormalization]
claim_number: 3
qid: "github:superconductivity_electron_liquids::bts_renormalization"
module: motivation
exported: false
prior: 0.95
belief: 0.9771040788329671
strategy_type: null
premise_count: 0
tags: [claim, motivation]
---

# #03 BTS 重整化关系

> Bogoliubov-Tolmachev-Shirkov (BTS) 重整化关系将定义在不同能量截断标度 $\omega_c$ 上的 Coulomb 赝势 $\mu_{\omega_c}$（描述配对通道中有效电子-电子排斥强度的无量纲参数）联系起来：$\mu_{\omega_c} = \mu_{\omega_c'} / (1 + \mu_{\omega_c'} \ln(\omega_c'/\omega_c))$。此关系确保物理可观测量不依赖于任意截断标度的选择。

## 背景

BTS 关系最早由 Bogoliubov、Tolmachev 和 Shirkov (1958-1961) 建立，是超导理论中最重要的重整化群结果之一。Cooper 通道中的对数发散 $\ln(\omega_c'/\omega_c)$ 既驱动超导配对不稳定性，也将频率无关的局域 Coulomb 排斥重整化至弱耦合极限。实际应用中，该关系允许将在 Fermi 能标度上计算的"裸"赝势 $\mu_{E_F}$ 跑动到 Debye 频率标度，得到传统 Eliashberg 理论中使用的 $\mu^*$。本文的重要贡献是从四点顶角函数的微观定义出发，给出了 BTS 关系的严格场论推导（见论文公式 25）。

## 来源

- **原始文献**：N. N. Bogoliubov, V. V. Tolmachov, D. Shirkov, *A new method in the theory of superconductivity* (1959)。
- **理论地位**：标准重整化群结果，在弱耦合区间 $\mu_{\omega_c} \ln(\omega_c/T) \ll 1$ 内精确成立。
- **验证**：已被从微扰论到数值模拟的多种方法反复验证；本文进一步在微观层面确认其成立。

## 评审

**先验概率（Prior）**：0.95
**理由**：标准重整化群结果（1958），已被广泛验证。
**信念度（Belief）**：0.98

## 支撑

- → [[bts_microscopic_equivalence|#51 BTS 微观等价性]] 经由等价关系

## 所属模块

[[motivation|研究动机]]
