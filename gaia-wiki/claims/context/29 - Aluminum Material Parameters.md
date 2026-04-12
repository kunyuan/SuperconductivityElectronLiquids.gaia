---
type: setting
label: aluminum_parameters
aliases: [aluminum_parameters]
claim_number: 29
qid: "github:superconductivity_electron_liquids::aluminum_parameters"
module: s6_superconductors
exported: false
prior: null
belief: null
strategy_type: null
premise_count: 0
tags: [setting, s6-superconductors]
---

# #29 铝的材料参数

> 铝（Al）：FCC 晶体结构，$r_s = 2.07$，带质量 $m_b = 1.05$，DFPT 电子-声子耦合 $\lambda = 0.44$，对数声子频率 $\omega_{\mathrm{log}} = 320$ K，Fermi 温度 $T_F = 1.3 \times 10^5$ K。

## 背景

铝是本文的核心基准材料。其近自由电子特性（$r_s = 2.07$，近球形 Fermi 面）使其非常适合 UEG 模型映射。vDiagMC 给出 $\mu_{E_F} \approx 0.21$（$r_s = 2$ 时），经 BTS 跑动后 $\mu^* \approx 0.13$，预测 $T_c^{\mathrm{th}} = 0.96$ K（实验 1.2 K）。

## 所属模块

[[s6_superconductors|常规超导体]]
