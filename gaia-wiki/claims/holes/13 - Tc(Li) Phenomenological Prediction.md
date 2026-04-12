---
type: claim
label: tc_li_phenomenological
aliases: [tc_li_phenomenological]
claim_number: 13
qid: "github:superconductivity_electron_liquids::tc_li_phenomenological"
module: motivation
exported: false
prior: 0.1
belief: 0.1282696894393228
strategy_type: null
premise_count: 0
tags: [claim, motivation]
---

# #13 锂的唯象 $T_c$ 预测

> 使用 McMillan 公式取 $\mu^* = 0.1$ 时，锂的超导转变温度预测为 $T_c \approx 0.35$ K，而实验值约为 $4 \times 10^{-4}$ K；理论高估约三个数量级。

## 背景

锂的唯象 $T_c$ 预测是常规超导理论中最严重的失败案例。$\mu^* = 0.1$ 给出 $T_c \approx 0.35$ K，比实验值 $\sim 4 \times 10^{-4}$ K 高出近 1000 倍。锂的 $r_s = 3.25$ 处于较大值，vDiagMC 计算的裸赝势 $\mu_{E_F} \approx 0.77$（$r_s = 3$ 时）远大于唯象假设值，BTS 跑动后 $\mu^* \approx 0.16$--$0.18$，几乎完全抵消声子介导吸引 $\lambda \approx 0.34$--$0.41$，将 $T_c$ 压低至亚毫开尔文。这一案例充分体现了精确 $\mu^*$ 对低 $T_c$ 超导体预测的决定性作用。

## 来源

- **计算方法**：McMillan/Allen-Dynes 公式，$\lambda = 0.34$（9R 结构）、$\omega_{\mathrm{log}} = 242$ K、$\mu^* = 0.1$。
- **结果**：$T_c \approx 0.35$ K，高估约三个数量级。
- **根本原因**：唯象 $\mu^* = 0.1$ 严重低估了锂中的 Coulomb 排斥，实际 $\mu^* \approx 0.16$--$0.18$。

## 评审

**先验概率（Prior）**：0.10
**理由**：预测 0.35 K 对比实验 $4 \times 10^{-4}$ K（高估三个数量级）；匹配度极差。
**信念度（Belief）**：0.13

## 支撑

- → [[tc_li_predicted|#57 锂的第一性原理 $T_c$ 预测]] 经由溯因推理

## 所属模块

[[motivation|研究动机]]
