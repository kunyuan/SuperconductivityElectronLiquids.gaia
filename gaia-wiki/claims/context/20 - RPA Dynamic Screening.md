---
type: setting
label: rpa_dynamic_screening
aliases: [rpa_dynamic_screening]
claim_number: 20
qid: "github:superconductivity_electron_liquids::rpa_dynamic_screening"
module: s3_downfolding
exported: false
prior: null
belief: null
strategy_type: null
premise_count: 0
tags: [setting, s3-downfolding]
---

# #20 RPA 动态屏蔽

> 随机相位近似（RPA）动态屏蔽 Coulomb 相互作用：$W_{\mathrm{RPA}}(\mathbf{q},\nu) = v_q / (1 - v_q \Pi^0_{\mathbf{q}\nu})$，其中 $v_q = 4\pi e^2/q^2$ 为裸 Coulomb 势，$\Pi^0$ 为非相互作用极化函数。这是在弱耦合极限（$r_s \lesssim 1$）精确的标准近似。

## 背景

RPA 是凝聚态物理中处理屏蔽效应最基本的近似。在本文中，RPA 主要用于两个场景：(i) 在玩具模型验证中作为电子不可约顶角 $\tilde{\Gamma}^e$ 的近似（论文 Fig. 5 的对比计算），(ii) 作为 DFPT 中屏蔽效应的基础。RPA 在 $r_s \lesssim 1$ 时精确，但在金属密度范围内需要超越 RPA 的顶角修正——这正是 vDiagMC 的用武之地。

## 所属模块

[[s3_downfolding|BSE 下折叠]]
