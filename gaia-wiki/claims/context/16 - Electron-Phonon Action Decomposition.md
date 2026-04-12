---
type: claim
label: electron_phonon_action
aliases: [electron_phonon_action]
claim_number: 16
qid: "github:superconductivity_electron_liquids::electron_phonon_action"
module: s2_model
exported: false
prior: 0.95
belief: 0.95
strategy_type: null
premise_count: 0
tags: [claim, s2-model]
---

# #16 电子-声子作用量分解

> 电子-声子耦合体系的有效作用量可分解为 $S = S_e + S_{\mathrm{ph}} + S_{e\text{-ph}} + S_{\mathrm{CT}} + O(\sqrt{m/M})$，其中 $m$ 为电子质量，$M$ 为离子质量。$S_e$ 是无任何近似的完整多电子作用量，$S_{\mathrm{ph}}$ 描述具有物理色散的声子，$S_{e\text{-ph}}$ 是电子密度与离子位移的耦合，$S_{\mathrm{CT}}$ 是反项——扣除已包含在物理声子色散中的静态电子极化贡献以防止双重计数。

## 背景

这是论文的理论出发点（公式 1-4），基于标准有效场论分解。与 DFT 方法不同，本文保留完整的多电子作用量 $S_e$ 而非用近似交换-关联势替代，因此能捕捉电子-电子相互作用的动态效应。反项 $S_{\mathrm{CT}}$ 的引入是关键技术细节：由于使用物理（已屏蔽）声子色散 $\omega_{\kappa\mathbf{q}}$，必须扣除微扰展开中重复计算的静态电子极化贡献。

## 评审

**先验概率（Prior）**：0.95
**理由**：标准 EFT 分解。
**信念度（Belief）**：0.95

## 所属模块

[[s2_model|模型与基本关系]]
