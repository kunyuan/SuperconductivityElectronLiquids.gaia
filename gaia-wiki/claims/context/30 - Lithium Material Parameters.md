---
type: setting
label: lithium_parameters
aliases: [lithium_parameters]
claim_number: 30
qid: "github:superconductivity_electron_liquids::lithium_parameters"
module: s6_superconductors
exported: false
prior: null
belief: null
strategy_type: null
premise_count: 0
tags: [setting, s6-superconductors]
---

# #30 锂的材料参数

> 锂（Li）：低温下为 9R 晶体结构（也以 HCP 研究）。9R 参数：$r_s = 3.25$，$m_b = 1.75$，$\lambda = 0.34$，$\omega_{\mathrm{log}} = 242$ K，$T_F = 4.0 \times 10^4$ K。HCP 参数：$r_s = 3.19$，$m_b = 1.4$，$\lambda = 0.37$，$\omega_{\mathrm{log}} = 243$ K，$T_F = 4.1 \times 10^4$ K。亚开尔文温度下的晶体结构仍有争议。

## 背景

锂是论文中最具戏剧性的测试案例。其较大的 $r_s$ 值（9R 结构下 3.25）使 Coulomb 赝势显著增大（$\mu^* \approx 0.18$），几乎完全抵消声子吸引 $\lambda \approx 0.34$，将 $T_c$ 压至亚毫开尔文。9R 和 HCP 两种结构的参数差异导致预测 $T_c$ 有量级变化（$5 \times 10^{-3}$ K vs $0.03$ K），凸显晶体结构争议对预测的影响。

## 所属模块

[[s6_superconductors|常规超导体]]
