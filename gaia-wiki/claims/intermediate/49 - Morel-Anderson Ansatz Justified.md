---
type: claim
label: ma_pseudopotential_justified
aliases: [ma_pseudopotential_justified]
claim_number: 49
qid: "github:superconductivity_electron_liquids::ma_pseudopotential_justified"
module: s3_downfolding
exported: false
prior: null
belief: 0.7713563414448433
strategy_type: deduction
premise_count: 1
tags: [claim, s3-downfolding]
---

# #49 Morel-Anderson ansatz 的微观正当化 (Morel-Anderson Ansatz Justified)

Morel-Anderson 常数赝势 ansatz——将 $\mu_{\omega_c}$ 视为近似频率无关——在微观上是正当的：四点顶点 $\tilde\Gamma^e$ 在电子能标（$E_F$）上变化，远大于声子能标（$\omega_D$）。在低能窗口 $|\omega|, |\omega'| < \omega_c \ll E_F$ 内，库仑核实际上是常数，验证了 Eliashberg 理论中传统的常数 $\mu^*$ 处理。

## 背景

Morel 和 Anderson (1962) 首先引入了以单一数值 $\mu^*$ 描述配对通道中有效库仑排斥的概念。这一处理的正当性依赖于 $\mu^*$ 的频率依赖性可忽略——但长期以来缺乏严格的微观论证。

## 推导

**策略**: 演绎推理 (deduction)

**前提**:
- [[mu_microscopic_definition|#47 $\mu$ 的微观定义]]

$\mu_{\omega_c}$ 的微观定义 ([[mu_microscopic_definition|#47]]) 表明它由电子四点顶点 $\tilde{\Gamma}^e$ 决定，后者在 $E_F$ 的能标上变化。在低能窗口 $|\omega|, |\omega'| < \omega_c$（其中 $\omega_c \ll E_F$）内，$\tilde{\Gamma}^e$ 的频率依赖性可忽略，因此：

$$\mu_{\omega_c}(\omega, \omega') \approx \mu_{\omega_c} = \text{常数}$$

这为 Morel-Anderson ansatz ([[mu_star_phenomenological|#06]]) 提供了第一性原理正当化。正当化的关键在于能标层级 $\omega_c \ll E_F$ 的维持。

## 评审

- **Prior**: 依赖前提推断
- **Justification**: 能标分离论证直截了当；主要假设（$\tilde{\Gamma}^e$ 在 $E_F$ 尺度上变化）在简单金属中成立。
- **Belief**: 0.771

## 意义

在微观层面上正当化了一个被使用了60多年的唯象 ansatz。这一结果不仅验证了传统做法，还明确了其适用范围——当能标层级被破坏时（如在具有接近费米能的集体激发的系统中），常数 $\mu^*$ 处理可能失效。

## 注意事项

对于具有在声子能标附近的软集体激发的系统，$\tilde{\Gamma}^e$ 可能在较低能标上展现显著频率依赖性，使 Morel-Anderson ansatz 不再适用。

## 所属模块
[[s3_downfolding]]
