---
type: question
label: main_question
aliases: [main_question]
claim_number: 15
qid: "github:superconductivity_electron_liquids::main_question"
module: motivation
exported: false
prior: null
belief: null
strategy_type: null
premise_count: 0
tags: [question, motivation]
---

# #15 核心问题：第一性原理 $\mu^*$ 与 $T_c$ (Main Question: First-Principles mu* and Tc)

库仑赝势 $\mu^*$（量化 Cooper 配对通道中有效电子-电子排斥的参数）能否以受控精度从第一性原理计算，并由此给出简单金属（如 Al, Li, Na, Mg）超导转变温度 $T_c$ 的定量预测？

## 背景

这一问题的核心在于超导理论中一个长达半个多世纪的缺口：虽然电子-声子耦合的重要性已被理解，但库仑相互作用的理论可控的第一性原理处理从未被制定。在传统 Migdal-Eliashberg 框架中，$\mu^*$ 被当作可调参数处理（经验值 0.1--0.2）。这一不确定性在预测亚开尔文超导体的 $T_c$ 时被指数放大，导致数个量级的预测误差。

最具争议的问题是 $\mu^*$ 的大小和符号。基于 RPA 的计算预测在 $r_s \gtrsim 2$ 时 $\mu^* < 0$（即库仑效应变为净吸引），但这与大量实验证据不符，且在内部也不自洽（RPA 在 $r_s \gtrsim 1$ 时不可靠）。

本文通过基于有效场论的方法——利用变分介图蒙特卡洛积出高能电子自由度——给出了对这一问题的肯定回答。

## 所属模块
[[motivation]]
