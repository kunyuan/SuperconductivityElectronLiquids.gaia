---
type: claim
label: tc_zn_phenomenological
aliases: [tc_zn_phenomenological]
claim_number: 14
qid: "github:superconductivity_electron_liquids::tc_zn_phenomenological"
module: motivation
exported: false
prior: 0.35
belief: 0.4115866842500226
strategy_type: null
premise_count: 0
tags: [claim, motivation]
---

# #14 锌的唯象 $T_c$ 预测

> 使用 McMillan 公式取标准值 $\mu^* = 0.1$ 时，锌的超导转变温度预测为 $T_c \approx 1.37$ K，而实验值为 0.875 K，偏差约 57%。

## 背景

锌的唯象预测与铝类似，表现出系统性的高估。$\mu^* = 0.1$ 给出 $T_c \approx 1.37$ K，比实验值 0.875 K 高 57%。这一偏差与铝的 58% 偏差高度一致，暗示唯象 $\mu^*$ 对简单金属系统性地低估了 Coulomb 排斥。本文 vDiagMC 计算给出 $\mu^*(\mathrm{Zn}) \approx 0.12$（对应 $r_s = 2.31$，经 BTS 跑动），预测 $T_c^{\mathrm{th}} = 0.874$ K，与实验几乎完全吻合。

## 来源

- **计算方法**：McMillan/Allen-Dynes 公式，$\lambda = 0.502$、$\omega_{\mathrm{log}} = 111$ K、$\mu^* = 0.1$。
- **结果**：$T_c \approx 1.37$ K，高估 57%。
- **局限性**：与铝相同，唯象 $\mu^*$ 的不确定性是预测偏差的主要来源。

## 评审

**先验概率（Prior）**：0.35
**理由**：预测 1.37 K 对比实验 0.875 K（高估 57%）；匹配度较差。
**信念度（Belief）**：0.41

## 支撑

- → [[tc_zn_predicted|#56 锌的第一性原理 $T_c$ 预测]] 经由溯因推理

## 所属模块

[[motivation|研究动机]]
