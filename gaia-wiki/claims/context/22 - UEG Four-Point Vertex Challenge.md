---
type: claim
label: ueg_vertex_challenge
aliases: [ueg_vertex_challenge]
claim_number: 22
qid: "github:superconductivity_electron_liquids::ueg_vertex_challenge"
module: s4_pseudopotential
exported: false
prior: 0.95
belief: 0.95
strategy_type: null
premise_count: 0
tags: [claim, s4-pseudopotential]
---

# #22 UEG 四点顶角的计算挑战

> 计算均匀电子气（UEG）的粒子-粒子不可约四点顶角 $\tilde\Gamma^e$ 是一个长期未解的挑战：基于裸 Coulomb 相互作用的微扰论在 $r_s \gtrsim 1$ 时发散，而部分重求和（RPA、GW）遗漏了关键的顶角修正。需要一种有控制的、可系统改进的方法来评估金属密度范围 $r_s \in [1, 6]$ 内的 $\tilde\Gamma^e$。

## 背景

四点顶角 $\tilde\Gamma^e$ 是确定 Coulomb 赝势 $\mu^*$ 的核心量。在金属密度范围内，现有方法均有根本局限：变分 QMC 和扩散 QMC 是基态方法，无法直接获取顶角函数；GW 近似忽略了顶角修正；T 矩阵近似虽被提出但属于不受控近似。vDiagMC 正是为解决此问题而发展的。

## 评审

**先验概率（Prior）**：0.95
**理由**：公认的计算挑战。
**信念度（Belief）**：0.95

## 所属模块

[[s4_pseudopotential|Coulomb 赝势]]
