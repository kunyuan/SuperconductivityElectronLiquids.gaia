---
type: claim
label: downfolded_me_equation
aliases: [downfolded_me_equation]
claim_number: 45
qid: "github:superconductivity_electron_liquids::downfolded_me_equation"
module: s3_downfolding
exported: false
prior: null
belief: 0.6638247822116828
strategy_type: deduction
premise_count: 1
tags: [claim, s3-downfolding]
---

# #45 下折叠 ME 能隙方程 (Downfolded ME Gap Equation)

在超导临界温度 $T_c$ 处，下折叠 Bethe-Salpeter 方程退化为传统的线性化 Migdal-Eliashberg (ME) 能隙方程：$\Delta_\omega = \pi T_c \sum_{|\omega'|<\omega_c} (\lambda_{\omega\omega'} - \mu^*) \frac{z_{\omega'}^{\mathrm{ph}}}{|\omega'|} \Delta_{\omega'}$。当 $T \to T_c$ 时，反常顶点发散为 $\Lambda_{k\omega} \sim \Delta_{k\omega}/(T - T_c)$，使源项 $\eta$ 变得无关。发散前因子 $(T - T_c)^{-1}$ 在方程两侧对消，给出 $\mu^* \equiv \mu_{\omega_c}$ 的能隙方程。这建立了 ME 方程的微观基础，赋予 $\mu^*$ 和 $\lambda$ 以电子顶点函数的精确定义。

## 背景

传统的线性化 ME 能隙方程（方程 12）具有本征值形式 $h(T)\Delta = \int \tilde{\Gamma} GG \Delta$，$T_c$ 由 $h(T_c) = 1$ 确定。然而，在具有强排斥相互作用的系统中，没有简单方法可靠地外推 $h(T)$ 到低温。

## 推导

**策略**: 演绎推理 (deduction)

**前提**:
- [[downfolded_bse|#43 下折叠 BSE]]

从下折叠 BSE ([[downfolded_bse|#43]]) 出发，利用前驱 Cooper 流 ([[precursory_cooper_flow|#17]]) 的标度行为：当 $T \to T_c$ 时，反常顶点 $\Lambda_{k\omega}$ 发散为 $\Lambda_{k\omega} \sim \Delta_{k\omega}/(T - T_c)$，其中 $\Delta_{k\omega}$ 是超导能隙函数。

将此标度代入下折叠 BSE（方程 20）：
$$\frac{\Delta_\omega}{T - T_c} = \eta_\omega + \pi T_c \sum_{|\omega'|<\omega_c} (\lambda_{\omega\omega'} - \mu^*) \frac{z_{\omega'}^{\mathrm{ph}}}{|\omega'|} \frac{\Delta_{\omega'}}{T - T_c}$$

当 $T \to T_c$ 时，源项 $\eta_\omega$ 有限而顶点发散，因此 $\eta$ 相对可忽略。发散前因子 $(T - T_c)^{-1}$ 在两侧对消，得到能隙方程（方程 22）：

$$\Delta_\omega = \pi T_c \sum_{|\omega'|<\omega_c} (\lambda_{\omega\omega'} - \mu^*) \frac{z_{\omega'}^{\mathrm{ph}}}{|\omega'|} \Delta_{\omega'} + O\left(\frac{\omega_D}{E_F}, \frac{\omega_c^2}{\omega_p^2}\right)$$

其中 $\mu^* = \mu_{\omega_c}$，$\omega_* = \omega_c$。在低频极限中，$\lambda_{\omega\omega'} z_{\omega'}^{\mathrm{ph}}$ 退化为 $\lambda/(1+\lambda)$。

这与传统 ME 能隙方程形式完全一致，但现在 $\mu^*$ 和 $\lambda$ 有了从下折叠推导得到的精确微观定义。

## 评审

- **Prior**: 依赖前提推断
- **Justification**: 直接的数学推导，无额外近似。
- **Belief**: 0.664

## 意义

将传统 ME 能隙方程（方程 22）确立为下折叠 BSE 在临界温度处的特例，使半唯象方程获得了严格的微观基础。这也解释了前驱 Cooper 流 (PCF) 相对传统方法的优势——PCF 通过精确的标度律（方程 10）从高温外推 $T_c$，避免了直接在 $T_c$ 处求解。

## 注意事项

修正项正比于 $\omega_D/E_F$ 和 $\omega_c^2/\omega_p^2$，在简单金属中可忽略。

## 所属模块
[[s3_downfolding]]
