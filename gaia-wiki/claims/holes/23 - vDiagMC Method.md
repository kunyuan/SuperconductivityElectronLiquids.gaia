---
type: claim
label: vdiagmc_method
aliases: [vdiagmc_method]
claim_number: 23
qid: "github:superconductivity_electron_liquids::vdiagmc_method"
module: s4_pseudopotential
exported: false
prior: 0.9
belief: 0.8441952419591435
strategy_type: null
premise_count: 0
tags: [claim, s4-pseudopotential]
---

# #23 变分图解蒙特卡罗方法（vDiagMC）

> 变分图解蒙特卡罗（vDiagMC）提供了一种有控制的、可系统改进的高阶 Feynman 图级数计算方法：(i) 粗线（自洽）重求和避免了单个图的红外发散，(ii) 对图拓扑和内部变量的随机采样可达到确定性方法无法企及的高阶，(iii) 级数可外推至无穷阶并具有受控误差条。对于均匀电子气（UEG），vDiagMC 在金属密度范围内实现了不可约顶角函数的可靠收敛。

## 背景

计算 UEG 的粒子-粒子不可约四点顶角 $\tilde{\Gamma}^e$ 长期以来是凝聚态物理的核心难题。在 $r_s > 1$ 时，基于裸 Coulomb 相互作用的微扰论发散，而 RPA 和 GW 等部分重求和遗漏了关键的顶角修正。vDiagMC 的核心思想是优化微扰展开的起始点——将裸 Coulomb 相互作用 $v(q) = 4\pi e^2/q^2$ 重新表示为 Yukawa 相互作用 $v_R(q) = 4\pi e^2/(q^2 + \lambda_R)$ 加上反项级数，其中屏蔽参数 $\lambda_R$ 经过优化以改善收敛性。然后通过随机采样高阶 Feynman 图（借助计算图压缩和 Taylor 模式自动微分加速），对物理量进行逐阶计算和外推。

## 来源

- **方法论文献**：Refs. [63-70]（论文原文引用），涵盖 vDiagMC 方法的发展历程和技术细节。
- **验证范围**：在 $r_s \leq 5$ 范围内，vDiagMC 的自能、有效质量、密度和自旋磁化率结果与独立的 QMC 和 DiagMC 计算一致。
- **数值实现**：采用计算图表示 + VEGAS 自适应蒙特卡罗 + 归一化流神经网络重要性采样，支持 CPU/GPU 并行。
- **已知局限**：在 $r_s > 5$ 时收敛性下降；依赖于 $\gamma_T(\xi)$ 作为 $\xi$ 的函数的解析性假设。

## 评审

**先验概率（Prior）**：0.90
**理由**：严格的 Feynman 图展开；在 $r_s \leq 5$ 范围内已验证。
**信念度（Belief）**：0.84

## 支撑

- → [[mu_vdiagmc_values|#37 vDiagMC 计算的 $\mu$ 数值]] 经由 noisy_and 推理

## 所属模块

[[s4_pseudopotential|Coulomb 赝势]]
