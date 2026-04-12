---
type: claim
label: lambda_microscopic_definition
aliases: [lambda_microscopic_definition]
claim_number: 46
qid: "github:superconductivity_electron_liquids::lambda_microscopic_definition"
module: s3_downfolding
exported: false
prior: null
belief: 0.4952902976694493
strategy_type: deduction
premise_count: 1
tags: [claim, s3-downfolding]
---

# #46 $\lambda$ 的微观定义 (Microscopic Definition of lambda)

下折叠 BSE 中的电子-声子耦合 $\lambda(\omega, \omega')$ 有一个微观定义：它是声子介导相互作用 $W^{\mathrm{ph}}$ 的费米面平均，由准粒子重整化因子 $z^e$ 和 $z_\omega^{\mathrm{ph}}$ 加权。该定义在绝热极限退化为标准 Eliashberg $\lambda$，但保留了来自电子自能的动力学修正。

## 背景

在传统 ME 理论中，$\lambda$ 是定量超导预测的核心输入，量化了费米面上准粒子之间的声子介导吸引。但其在微观理论中的精确定义——特别是准粒子重整化因子的放置——一直存在歧义。

## 推导

**策略**: 演绎推理 (deduction)

**前提**:
- [[downfolded_bse|#43 下折叠 BSE]]

下折叠 BSE ([[downfolded_bse|#43]]) 将配对核表示为 $K = \lambda - \mu_{\omega_c}$。声子介导部分 $\lambda(\omega, \omega')$ 产生于将 $W^{\mathrm{ph}}$（来自电子-声子作用量分解 [[electron_phonon_action|#16]] 的声子介导相互作用）通过配对传播子的相干部分投影到费米面上。

具体地（方程 20 中的定义）：
$$\lambda_{\omega\omega'} \equiv -(z^e)^2 N_F^* \langle W_{k_F - k_F', \omega-\omega'}^{\mathrm{ph}} \rangle_{k_F k_F'}$$

作用量中的反项 $S_{\mathrm{CT}}$（方程 4）确保了物理声子色散中已包含的静态屏蔽不被重复计数。$\lambda$ 的表达式涉及 $W^{\mathrm{ph}}$ 的费米面平均，由准粒子因子加权，提供了推广标准 Eliashberg 耦合常数的受控微观定义。

频率依赖的准粒子权重 $z_\omega^{\mathrm{ph}}$ 完全由 $\lambda$ 决定（方程 21），与标准 Eliashberg 公式化一致。

## 评审

- **Prior**: 依赖前提推断
- **Justification**: 直接从下折叠过程导出，定义清晰。
- **Belief**: 0.495

## 支撑

- $\to$ [[eft_eph_vertex|#50 EFT 电子-声子顶点]] via deduction

## 意义

为 $\lambda$ 提供了精确的微观定义，消除了传统 ME 理论中关于准粒子权重因子放置的歧义。

## 注意事项

该定义在低频极限 $\lambda_{\omega\omega'} z_{\omega'}^{\mathrm{ph}} \to \lambda/(1+\lambda)$ 退化为标准结果，但在一般频率下保留了动力学修正。

## 所属模块
[[s3_downfolding]]
