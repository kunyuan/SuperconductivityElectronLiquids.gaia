---
type: claim
label: tc_al_phenomenological
aliases: [tc_al_phenomenological]
claim_number: 12
qid: "github:superconductivity_electron_liquids::tc_al_phenomenological"
module: motivation
exported: false
prior: 0.35
belief: 0.4115866842500226
strategy_type: null
premise_count: 0
tags: [claim, motivation]
---

# #12 铝的唯象 $T_c$ 预测

> 使用 McMillan 公式（基于电子-声子耦合常数 $\lambda$ 和 Coulomb 赝势 $\mu^*$ 的经验公式）取标准值 $\mu^* = 0.1$ 时，铝的超导转变温度预测为 $T_c \approx 1.9$ K，而实验值为 1.2 K，偏差约 58%。

## 背景

McMillan 公式 $T_c = \frac{\omega_{\mathrm{log}}}{1.2} \exp\left[-\frac{1.04(1+\lambda)}{\lambda - \mu^*(1+0.62\lambda)}\right]$ 是超导材料设计中最常用的半经验公式。其中 $\mu^*$ 的选取决定了预测精度：取 $\mu^* = 0.1$ 时，铝的 $T_c$ 被高估 58%；取 $\mu^* = 0.2$ 则严重低估。这一敏感性说明唯象 $\mu^*$ 缺乏预测能力。作为对比，本文通过 vDiagMC 从第一性原理得到 $\mu^*(\mathrm{Al}) \approx 0.13$（对应 $r_s = 2.07$），预测 $T_c^{\mathrm{th}} = 0.96$ K，与实验值 1.2 K 在误差范围内一致。

## 来源

- **计算方法**：McMillan/Allen-Dynes 经验公式，输入 $\lambda = 0.44$（DFPT）、$\omega_{\mathrm{log}} = 320$ K、$\mu^* = 0.1$。
- **结果**：$T_c \approx 1.9$ K，高估 58%。
- **局限性**：$\mu^*$ 是唯象参数，其"标准"值 0.1 缺乏微观基础；对于低 $T_c$ 超导体，$T_c$ 对 $\mu^*$ 的指数灵敏度使得预测误差可达数个数量级。

## 评审

**先验概率（Prior）**：0.35
**理由**：预测 1.9 K 对比实验 1.2 K（高估 58%）；匹配度较差。此处 prior 衡量"唯象理论能否单独解释实验 $T_c$"，偏差过大故取低值。
**信念度（Belief）**：0.41

## 支撑

- → [[tc_al_predicted|#55 铝的第一性原理 $T_c$ 预测]] 经由溯因推理

## 所属模块

[[motivation|研究动机]]
