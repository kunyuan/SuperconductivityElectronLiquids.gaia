---
type: claim
label: tc_zn_experimental
aliases: [tc_zn_experimental]
claim_number: 11
qid: "github:superconductivity_electron_liquids::tc_zn_experimental"
module: motivation
exported: false
prior: 0.99
belief: 0.9981688001425907
strategy_type: null
premise_count: 0
tags: [claim, motivation]
---

# #11 锌的实验超导转变温度

> 锌（Zn）的实验超导转变温度为 $T_c^{\mathrm{exp}} = 0.875$ K。

## 背景

锌是 HCP 结构的简单金属，其 $T_c = 0.875$ K 处于亚开尔文范围，是检验第一性原理 $T_c$ 预测精度的重要基准。与铝类似，唯象 McMillan 公式（$\mu^* = 0.1$）给出 $T_c \approx 1.37$ K，比实验值高估约 57%。本文使用 vDiagMC 计算的 $\mu^*(\mathrm{Zn}) \approx 0.12$（对应 $r_s = 2.31$）得到 $T_c^{\mathrm{th}} = 0.874$ K，与实验值几乎完美吻合。

## 来源

- **实验方法**：标准低温电阻率测量。
- **精度**：$T_c = 0.875$ K 精确到 $\pm 0.005$ K。
- **再现性**：已充分建立的实验测量。

## 评审

**先验概率（Prior）**：0.99
**理由**：已充分建立的实验测量。
**信念度（Belief）**：1.00

## 支撑

- → [[tc_zn_predicted|#56 锌的第一性原理 $T_c$ 预测]] 经由溯因推理

## 所属模块

[[motivation|研究动机]]
