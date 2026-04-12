---
type: setting
label: pair_propagator_decomposition
aliases: [pair_propagator_decomposition]
claim_number: 18
qid: "github:superconductivity_electron_liquids::pair_propagator_decomposition"
module: s3_downfolding
exported: false
prior: null
belief: null
strategy_type: null
premise_count: 0
tags: [setting, s3-downfolding]
---

# #18 配对传播子分解

> 配对传播子（两个单粒子 Green 函数之积 $G_{k\omega}G_{-k,-\omega}$）可精确分解为低能相干部分 $\Pi_{\mathrm{BCS}}$ 和高能非相干余量 $\phi_{k\omega}$：$G_{k\omega}G_{-k,-\omega} = \Pi_{\mathrm{BCS}} + \phi_{k\omega}$。其中相干部分用准粒子权重 $z^e$、频率依赖的准粒子权重 $z_\omega^{\mathrm{ph}}$ 和重整化色散 $\epsilon_k$ 表示。这是在双电子通道中引入能量标度分离的精确数学恒等式。

## 背景

这是本文下折叠推导的数学起点（论文公式 13-14）。与传统 Wilsonian 重整化群在单电子或电子-空穴通道中引入能量标度分离不同，本文在双电子（粒子-粒子）通道中进行分解，从而保持了 Coulomb 相互作用的动态屏蔽特性，避免了先前方法中出现的未屏蔽 Coulomb 奇异性。这一技术选择是本文理论框架成功的关键。

## 所属模块

[[s3_downfolding|BSE 下折叠]]
