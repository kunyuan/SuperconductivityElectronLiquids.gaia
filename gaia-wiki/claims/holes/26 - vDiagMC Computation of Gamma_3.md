---
type: claim
label: gamma3_vdiagmc
aliases: [gamma3_vdiagmc]
claim_number: 26
qid: "github:superconductivity_electron_liquids::gamma3_vdiagmc"
module: s5_eph_coupling
exported: false
prior: 0.88
belief: 0.9545830446193447
strategy_type: null
premise_count: 0
tags: [claim, s5-eph-coupling]
---

# #26 vDiagMC 计算的 $\Gamma_3$

> vDiagMC 对 UEG 三点顶角 $\Gamma_3^e(k, q)$ 在有限动量转移 $q$ 处的计算表明：在金属密度 $r_s \in [2, 4]$ 下，对于 Fermi 球内的动量（$|k|, |k+q| \lesssim k_F$），顶角修正是温和的（10--20% 水平）。修正随 $q$ 平滑变化，可在 Ward 恒等式极限（$q \to 0$）和大 $q$ 渐近行为之间精确插值。

![[10_0.jpg]]

## 背景

确定电子-声子顶角修正 $\Gamma_3^e$ 在有限动量转移下的行为，对于评估 DFPT 计算 $\lambda$ 的可靠性至关重要。论文 Fig. 8 展示了 vDiagMC 数据点与 DFPT 预测曲线的系统性对比：对于 $r_s \in [1, 5]$ 的所有密度和 Fermi 面上所有散射角 $\theta$（入射动量 $\mathbf{k}$ 与出射动量 $\mathbf{k}+\mathbf{q}$ 之间的夹角），准粒子电子-声子顶角 $z^e \Gamma_3^e(\mathbf{k}, \mathbf{q}) / \epsilon_\mathbf{q}$ 与 DFPT 的 Kohn-Sham 屏蔽势表达式吻合良好。唯一的例外是后向散射区域 $\theta \approx \pi$，在此处图级数对 Cooper 通道的对数发散较为敏感。总体而言，$z^e$、$\epsilon_\mathbf{q}$ 和 $\Gamma_3^e$ 各自都有很大的相互作用修正，但它们的乘积中存在显著的抵消效应。

## 来源

- **计算方法**：vDiagMC 对 UEG 三点顶角函数的高阶微扰计算。
- **系统不确定性**：源于图截断（达到 $n \sim 7$ 阶）和级数外推；方法已在自能和其他量上验证。
- **定量精度**：对于 $|\mathbf{q}| \leq 2k_F$ 的 Fermi 面相关动量转移，顶角修正在 10--20% 水平，且随 $q$ 平滑变化。
- **与 Ward 恒等式一致性**：在 $q \to 0$ 极限与精确的 Ward 恒等式结果吻合。

## 评审

**先验概率（Prior）**：0.88
**理由**：系统不确定性来自截断；方法在其他量上已验证。
**信念度（Belief）**：0.95

## 支撑

- → [[gamma3_approximation|#38 $\Gamma_3$ 近似]] 经由溯因推理
- → [[gamma3_approximation|#38 $\Gamma_3$ 近似]] 经由归纳推理

## 所属模块

[[s5_eph_coupling|电子-声子耦合]]
