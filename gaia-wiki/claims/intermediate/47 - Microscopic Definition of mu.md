---
type: claim
label: mu_microscopic_definition
aliases: [mu_microscopic_definition]
claim_number: 47
qid: "github:superconductivity_electron_liquids::mu_microscopic_definition"
module: s3_downfolding
exported: false
prior: null
belief: 0.5438002834565999
strategy_type: deduction
premise_count: 1
tags: [claim, s3-downfolding]
---

# #47 $\mu$ 的微观定义 (Microscopic Definition of mu)

下折叠 BSE 中的库仑赝势 $\mu_{\omega_c}(\omega, \omega')$ 有一个微观定义：它由纯电子的粒子-粒子不可约四点顶点 $\tilde\Gamma^e$ 投影到费米面上确定，高能电子自由度在截断 $\omega_c$ 以上被积出。这赋予 $\mu_{\omega_c}$ 精确的含义：低能配对通道中的有效库仑排斥，经所有电子关联重整化。

## 背景

传统方法中，$\mu^*$ 被当作可调参数或通过不受控近似（如 RPA）估计。$\mu_{\omega_c}$ 的微观定义将其与可计算的量（电子液体的四点顶点函数）精确联系起来。

## 推导

**策略**: 演绎推理 (deduction)

**前提**:
- [[downfolded_bse|#43 下折叠 BSE]]

下折叠 BSE ([[downfolded_bse|#43]]) 将配对核分离为声子（$\lambda$）和库仑（$\mu_{\omega_c}$）贡献。库仑部分通过将 BSE 核中的纯电子不可约四点顶点 $\tilde{\Gamma}^e$ 投影到费米面上得到，频率积分限制在 $\omega_c$ 以上的范围由配对传播子的非相干部分处理。

具体地，有效电子-电子相互作用定义为（方程 19 下方）：
$$U^e \equiv \tilde{\Gamma}^e + \tilde{\Gamma}^e \cdot \phi \cdot \tilde{\Gamma}^e + \cdots$$

这一构造将 $\mu_{\omega_c}$ 定义为 $\tilde{\Gamma}^e$ 的泛函——编码所有非微扰库仑关联的量——在特定能标处求值，无需任何唯象输入。

在仅有电子-电子相互作用的理论中（$\lambda = 0$，$z^{\mathrm{ph}} = 1$），求解方程 22 在温度 $T$ 处给出有效排斥（方程 23）：
$$\gamma_T = \frac{\mu_{\omega_c}}{1 + \mu_{\omega_c} \ln(\omega_c/T)} \qquad (T \ll \omega_c)$$

这一排斥也可以通过费米面平均的双准粒子散射振幅定义（方程 24）：
$$\gamma_T \equiv z_e^2 N_F^* \langle \Gamma_F^e(k_F, \omega_0; k_F', \omega_0) \rangle_{k_F, k_F'}$$

右端可以被计算（例如通过 vDiagMC），使得 $\mu_{\omega_c}$ 成为可从第一性原理确定的量。

## 评审

- **Prior**: 依赖前提推断
- **Justification**: 直接从下折叠过程导出；$\mu_{\omega_c}$ 与可计算量的联系是精确的。
- **Belief**: 0.544

## 支撑

- $\to$ [[mu_scale_independence|#48 BTS 关系作为推论]] via deduction
- $\to$ [[ma_pseudopotential_justified|#49 Morel-Anderson ansatz 的正当化]] via deduction

## 意义

这是整个框架的核心结果之一：将 $\mu^*$ 从唯象参数提升为可从第一性原理计算的精确定义量。通过方程 24 与可计算的散射振幅的联系，为 vDiagMC 计算库仑赝势提供了理论基础。

## 注意事项

$\mu_{\omega_c}$ 是物理量 $\gamma_T$ 的一个重参数化（方程 23），$\gamma_T$ 本身独立于任意选择的分离能标 $\omega_c$。

## 所属模块
[[s3_downfolding]]
