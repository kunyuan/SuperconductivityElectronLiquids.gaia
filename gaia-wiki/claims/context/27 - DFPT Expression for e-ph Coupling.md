---
type: claim
label: dfpt_eph_ansatz
aliases: [dfpt_eph_ansatz]
claim_number: 27
qid: "github:superconductivity_electron_liquids::dfpt_eph_ansatz"
module: s5_eph_coupling
exported: false
prior: 0.9
belief: 0.9
strategy_type: null
premise_count: 0
tags: [claim, s5-eph-coupling]
---

# #27 DFPT 电子-声子耦合表达式

> DFPT 电子-声子耦合表达式 $g^{\mathrm{DFPT}}(k, q) = \sqrt{\omega_q / 2} \, \langle k+q | \delta V_{\mathrm{KS}} / \delta u_q | k \rangle$ 隐含假设超越 Kohn-Sham 平均场的顶角修正已被交换-关联泛函吸收。该 ansatz 的精度取决于 DFT 能多好地捕捉相关顶角修正。

## 背景

DFPT 计算 $\lambda$ 的核心表达式是论文公式 33：$g^{\mathrm{KS}}(\mathbf{q}) = g_{\mathbf{q}}^{(0)} / [1 - (v_{\mathbf{q}} + f_{xc})\chi_0^e(\mathbf{q})]$，其中 $f_{xc}$ 为局域密度近似（LDA）下的交换-关联核。这一表达式将电子-声子耦合视为 Kohn-Sham 势对晶格畸变的线性响应，仅依赖于转移动量 $\mathbf{q}$，不含入射电子动量 $\mathbf{k}$ 的依赖。本文证明，在 UEG 中 EFT 顶角的残余 $\mathbf{k}$ 依赖在数值上很弱，可安全忽略。

## 评审

**先验概率（Prior）**：0.90
**理由**：标准 DFPT 表达式。
**信念度（Belief）**：0.90

## 所属模块

[[s5_eph_coupling|电子-声子耦合]]
