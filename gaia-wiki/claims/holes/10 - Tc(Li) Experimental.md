---
type: claim
label: tc_li_experimental
aliases: [tc_li_experimental]
claim_number: 10
qid: "github:superconductivity_electron_liquids::tc_li_experimental"
module: motivation
exported: false
prior: 0.85
belief: 0.9387427013314529
strategy_type: null
premise_count: 0
tags: [claim, motivation]
---

# #10 锂的实验超导转变温度

> 锂（Li）的实验超导转变温度为 $T_c^{\mathrm{exp}} \approx 4 \times 10^{-4}$ K（0.4 mK）。该测量对应于 9R 晶体结构；锂在超低温下的晶体结构仍有争议。

## 背景

锂是最轻的金属元素，其超导转变温度极低（亚毫开尔文），长期以来对传统理论构成严峻挑战。使用唯象 McMillan 公式（$\mu^* = 0.1$）预测的 $T_c \approx 0.35$ K 比实验值高出约三个数量级，这是常规超导理论中最大的偏差之一。锂超导的核心困难在于：(i) 其较大的 $r_s = 3.25$ 导致 Coulomb 赝势 $\mu^*$ 显著增大，几乎完全抵消了声子介导的吸引 $\lambda \approx 0.41$；(ii) 在超低温下锂从 BCC 结构转变为 9R 或其他复杂结构，且确切的晶体结构仍有争议，为理论预测引入额外不确定性。

## 来源

- **实验方法**：超低温电阻率测量，需使用稀释制冷机达到亚毫开尔文温度。
- **精度**：实验值 $T_c \approx 4 \times 10^{-4}$ K 本身有较大不确定性（约一个数量级），部分源于晶体结构的不确定性。
- **已知局限**：超低温下锂的晶体结构（9R、HCP、或其他）仍有争议；不同结构对 $\lambda$ 和 $T_c$ 有显著影响。

## 评审

**先验概率（Prior）**：0.85
**理由**：超低温下晶体结构有争议。
**信念度（Belief）**：0.94

## 支撑

- → [[tc_li_predicted|#57 锂的第一性原理 $T_c$ 预测]] 经由溯因推理

## 所属模块

[[motivation|研究动机]]
