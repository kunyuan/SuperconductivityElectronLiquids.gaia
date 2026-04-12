---
type: claim
label: adiabatic_approx
aliases: [adiabatic_approx]
claim_number: 2
qid: "github:superconductivity_electron_liquids::adiabatic_approx"
module: motivation
exported: false
prior: 0.95
belief: 0.7140281707359465
strategy_type: null
premise_count: 0
tags: [claim, motivation]
---

# #02 绝热近似

> 在常规金属中，典型声子频率（Debye 频率 $\omega_D$）远小于电子 Fermi 能 $E_F$，即 $\omega_D / E_F \ll 1$（绝热近似）。这一能量标度分离带来三个关键后果：(i) 电子绝热地跟随离子运动而调整，(ii) 电子-离子耦合可以被线性化，(iii) 电子物理与声子物理之间的时空标度分离使得有控制的有效场论（EFT）处理成为可能。

## 背景

绝热近似是 Migdal-Eliashberg 理论的基石。对于简单金属（如 Al、Li、Zn），$\omega_D / E_F \sim 0.005$，远满足绝热条件。Migdal 定理在此条件下保证声子顶角修正被 $O(\omega_D / E_F)$ 压低，从而可以将电子-声子自能截断在自洽 Fock 图的水平。这一能量标度分离也是 Fermi 液体理论与 Wilsonian 重整化群在超导问题中得以应用的理论基础。

## 来源

- **理论基础**：Migdal 定理 (1958) 从电子-声子耦合的微扰论出发，证明了在 $m/M \ll 1$（电子质量远小于离子质量）条件下声子顶角修正的压低。
- **定量验证**：对于论文关注的简单金属，$\omega_D / E_F$ 典型值为 $\sim 0.005$，绝热参数极小。
- **已知局限**：该近似在高压氢化物（$\omega_D / E_F \sim 0.1$）、强关联材料（准粒子图像失效）、以及二维体系（无隙等离激元模式）中可能失效。

## 评审

**先验概率（Prior）**：0.95
**理由**：$\omega_D/E_F \sim 0.005$ 对简单金属成立；Migdal 定理已被广泛验证。
**信念度（Belief）**：0.71

## 支撑

- → [[me_framework|#36 Migdal-Eliashberg 框架]] 经由演绎推理

## 所属模块

[[motivation|研究动机]]
