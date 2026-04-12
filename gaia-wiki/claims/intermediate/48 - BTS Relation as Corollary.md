---
type: claim
label: mu_scale_independence
aliases: [mu_scale_independence]
claim_number: 48
qid: "github:superconductivity_electron_liquids::mu_scale_independence"
module: s3_downfolding
exported: false
prior: null
belief: 0.9763399411065742
strategy_type: deduction
premise_count: 1
tags: [claim, s3-downfolding]
---

# #48 BTS 关系作为推论 (BTS Relation as Corollary)

BTS 重整化关系 $\mu_{\omega_c} = \mu_{\omega_c'} / (1 + \mu_{\omega_c'} \ln(\omega_c'/\omega_c))$ 作为 $\mu_{\omega_c}$ 微观定义的推论自然浮现：改变截断 $\omega_c$ 在显式库仑核和 BCS 传播子中的 Cooper 对数之间重新分配贡献，同时保持物理 $T_c$ 不变。这为最初唯象的 BTS 关系提供了微观推导。

## 背景

Bogoliubov、Tolmachev 和 Shirkov (BTS) 在 1958--1961 年首先给出了下折叠论证：同一 Cooper 对数使频率无关的局域库仑排斥在低能下被重整化到弱耦合极限。由此得到的无量纲参数后来被 Morel 和 Anderson 命名为"赝势"。传统上 BTS 关系被视为独立的唯象 ansatz。

## 推导

**策略**: 演绎推理 (deduction)

**前提**:
- [[mu_microscopic_definition|#47 $\mu$ 的微观定义]]

给定 $\mu_{\omega_c}$ 的微观定义 ([[mu_microscopic_definition|#47]]) 为 $\tilde{\Gamma}^e$ 在截断 $\omega_c$ 处的费米面投影，考察当 $\omega_c$ 变化时 $\mu$ 如何变换。

将截断从 $\omega_c'$ 移至 $\omega_c$ 时，谱权在显式库仑核和相干配对传播子中的 BCS Cooper 对数 $\ln(\omega_c'/T)$ 之间转移。要求物理可观测量（$T_c$）在这一重新分配下保持不变，即可得到 BTS 关系（方程 25）：

$$\mu_{\omega_c} = \frac{\mu_{\omega_c'}}{1 + \mu_{\omega_c'} \ln(\omega_c'/\omega_c)}$$

这是下折叠理论结构的精确推论，而非 ad hoc ansatz。

一个具有物理意义的选择是 $\omega_c = E_F$——相干电子准粒子存在的物理能标以下。$\mu_{E_F}$ 通常被解释为费米能处的赝势，或等价地，"裸"赝势——不受 BTS 重整化的赝势。

## 评审

- **Prior**: 依赖前提推断
- **Justification**: BTS 关系作为标准重整化群结果已被广泛验证（1958年）。
- **Belief**: 0.976

## 意义

将 BTS 关系从唯象 ansatz 提升为严格的微观推论。这一关系在实际计算中至关重要——它允许在计算上方便的 $\omega_c$ 处计算 $\mu$，然后精确降标到任何所需的分离能标。

## 注意事项

BTS 关系的有效性与下折叠近似本身具有相同的适用范围条件。

## 所属模块
[[s3_downfolding]]
