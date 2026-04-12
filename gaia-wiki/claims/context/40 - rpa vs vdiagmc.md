---
type: claim
label: rpa_vs_vdiagmc
aliases: [rpa_vs_vdiagmc]
claim_number: 40
qid: "github:superconductivity_electron_liquids::rpa_vs_vdiagmc"
module: s4_pseudopotential
exported: false
prior: null
belief: 0.9994479446891271
strategy_type: null
premise_count: 0
tags: [claim, s4-pseudopotential]
---

# #40 RPA 与 vDiagMC 的矛盾

> not_both_true(A, B)

## 背景

这是结构性辅助命题，编码了 RPA 预测的吸引性 $\mu^*$（[[rpa_predicts_attractive_mu|#07]]）与 vDiagMC 计算的正值 $\mu$（[[mu_vdiagmc_values|#37]]）之间的逻辑矛盾。两者不可能同时为真：RPA 在 $r_s > 2$ 预测 $\mu^* < 0$，而 vDiagMC 在整个 $r_s \in [1,6]$ 范围给出 $\mu_{E_F} > 0$ 且单调递增。该矛盾关系使得 vDiagMC 证据的注入自动压低 RPA 预测的信念度。

## 所属模块

[[s4_pseudopotential|Coulomb 赝势]]
