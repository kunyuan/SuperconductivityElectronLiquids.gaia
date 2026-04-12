---
type: claim
label: bse_kernel_decomposition
aliases: [bse_kernel_decomposition]
claim_number: 39
qid: "github:superconductivity_electron_liquids::bse_kernel_decomposition"
module: s2_model
exported: false
prior: null
belief: 0.7802219639796265
strategy_type: deduction
premise_count: 1
tags: [claim, s2-model]
---

# #39 BSE 核分解 (BSE Kernel Decomposition)

Bethe-Salpeter 方程 (BSE) 的核可以分解为纯电子的粒子-粒子不可约四点顶点 $\tilde\Gamma^e$（编码所有非微扰库仑效应）和声子介导的有效电子-电子相互作用 $W^{\mathrm{ph}}$：$\tilde\Gamma = \tilde\Gamma^e + W^{\mathrm{ph}} + O(\omega_D/E_F)$。Migdal 定理确保高阶声子顶点修正被绝热小参数压低。

## 背景

BSE 描述了超导配对通道中的两粒子关联。其核——两粒子不可约顶点函数 $\tilde{\Gamma}$——在一般情况下既不已知也不可处理。BSE 的核心形式为（方程 8）：
$$\Lambda_{k\omega} = \eta_{k\omega} + \int_{k'\omega'} \tilde{\Gamma}_{k\omega;k'\omega'} G_{k'\omega'} G_{-k',-\omega'} \Lambda_{k'\omega'}$$

其中 $\Lambda_{k\omega}$ 是反常顶点函数，$\eta$ 是对称性破缺源项。

## 推导

**策略**: 演绎推理 (deduction)

**前提**:
- [[me_framework|#36 Migdal-Eliashberg 框架]]

Migdal 定理 ([[me_framework|#36]]) 保证声子顶点修正被 $O(\omega_D/E_F)$ 压低。这使得完整的粒子-粒子不可约核可以分离为（方程 9）：
$$\tilde{\Gamma} = \tilde{\Gamma}^e + W^{\mathrm{ph}} + O\left(\frac{\omega_D}{E_F}\right)$$

其中：
- **$\tilde{\Gamma}^e$**：纯电子的粒子-粒子不可约四点顶点，编码所有非微扰库仑关联，独立于声子细节
- **$W^{\mathrm{ph}}$**：声子介导相互作用，包含修饰声子传播子、裸耦合、电子屏蔽和顶点修正

![[4_2.jpg]]
*Fig. 3 | 动量空间中反常顶点 $\Lambda(k, -k; q=0)$ 的自洽 Bethe-Salpeter 方程。核由纯电子的粒子-粒子不可约四点顶点 $\tilde{\Gamma}^e$ 和声子介导相互作用 $W^{\mathrm{ph}}$ 组成；根据 Migdal 定理，高阶顶点修正很小。*

![[4_1.jpg]]
*Fig. 2 | 声子介导的电子-电子相互作用 $W^{\mathrm{ph}}$ 的介图表示，由声子传播子 $D$、裸耦合 $g^{(0)}$、顶点函数 $\Gamma_3^e$ 和介电函数 $\epsilon_{q\nu}$ 组成。后两者合为屏蔽电子-声子耦合。*

这两部分间的交叉项在 $\omega_D/E_F$ 的阶上可忽略。将 BSE 与 $G$ 的 Dyson 方程以及有效声子介导耦合 $W^{\mathrm{ph}}$ 的求值结合，构成一组封闭的自洽方程。

## 评审

- **Prior**: 依赖前提推断
- **Justification**: 标准 EFT 分解，Migdal 定理条件在简单金属中充分满足。
- **Belief**: 0.780

## 支撑

- $\to$ [[full_bse_toy_model|#42 完整 BSE 玩具模型结果]] via noisy_and
- $\to$ [[downfolded_bse|#43 下折叠 BSE]] via deduction

## 意义

BSE 核分解是后续所有推导的出发点——它将不可处理的多体问题分解为可分别处理的电子和声子贡献，为系统的下折叠创造了条件。

## 注意事项

BSE 核分解在 Migdal 定理成立时有效。对于非绝热系统，$\tilde{\Gamma}^e$ 和 $W^{\mathrm{ph}}$ 之间的耦合可能不可忽略。

## 所属模块
[[s2_model]]
