---
type: claim
label: tc_mg_na_near_qpt
aliases: [tc_mg_na_near_qpt]
claim_number: 59
qid: "github:superconductivity_electron_liquids::tc_mg_na_near_qpt"
module: s6_superconductors
exported: true
prior: null
belief: 0.7669054711867636
strategy_type: noisy_and
premise_count: 1
tags: [claim, s6-superconductors]
---

# #59 钠和镁接近量子相变 (Na and Mg Near Quantum Phase Transition)

第一性原理框架预测钠和镁具有极低或消失的 $T_c$：对于 Na（$r_s = 3.96$，$\lambda = 0.2$，$\mu^* = 0.15$），库仑排斥几乎完全对消弱的电子-声子耦合，给出 $T_c^{\mathrm{EFT}} = 2 \times 10^{-13}$ K（实际上无超导性）。对于 Mg（$r_s = 2.66$，$\lambda = 0.24$，$\mu^* = 0.14$），$T_c^{\mathrm{EFT}} = 5 \times 10^{-5}$ K。两种材料都接近超导与非超导基态之间的量子相变，$T_c$ 随微小参数变化呈指数变化。

## 背景

钠和镁在毫开尔文温度下均未观测到超导性。传统理论使用 $\mu^* = 0.1$ 预测 Na 的 $T_c \approx 6 \times 10^{-5}$ K、Mg 的 $T_c \approx 0.007$ K。

**钠的材料参数**（[[sodium_parameters|#31]]）：BCC 结构，$r_s = 3.96$，$m_b = 1.0$，$\lambda = 0.2$，$\omega_{\mathrm{log}} = 127$ K，$T_F = 4.2 \times 10^4$ K。

**镁的材料参数**（[[magnesium_parameters|#32]]）：HCP 结构，$r_s = 2.66$，$m_b = 1.02$，$\lambda = 0.24$，$\omega_{\mathrm{log}} = 269$ K，$T_F = 8.0 \times 10^4$ K。

## 推导

**策略**: noisy_and

**前提**:
- [[ab_initio_workflow|#54 第一性原理 $T_c$ 预测工作流]]

### 钠

$r_s = 3.96$，$m_b = 1.0$，vDiagMC 参数化给出 $\mu^* = 0.15$。这几乎完全对消其弱的 $\lambda = 0.2$：

有效配对耦合 $g \approx \lambda - \mu^*(1 + 0.62\lambda) = 0.2 - 0.15 \times 1.124 \approx 0.03$

极小的正 $g$ 值通过 $T_c = \omega_\Lambda e^{1/g}$（$g < 0$ 时）的指数产生天文数字级别的低 $T_c$：

$$T_c^{\mathrm{EFT}}(\mathrm{Na}) = 2 \times 10^{-13} \text{ K}$$

这实际上意味着无超导性——$T_c$ 比宇宙微波背景辐射温度还低十个量级。

### 镁

$r_s = 2.66$，$m_b = 1.02$，$\mu^* = 0.14$。$\lambda = 0.24$ 稍大于 Na，有效配对耦合也稍大：

$$T_c^{\mathrm{EFT}}(\mathrm{Mg}) = 5 \times 10^{-5} \text{ K}$$

虽然仍远低于当前实验探测极限，但比钠高约八个量级，表明镁更接近超导侧。

### 量子相变的物理图像

![[15_0.jpg]]
*Fig. 11 | 简单金属的有效 BCS 耦合强度，绘为 $-1/\ln(T_c/\omega_{\mathrm{log}})$。电子-声子耦合来自 DFPT 计算；赝势来自 vDiagMC 结果。Na 和 Mg 出现在原点附近，表明配对相互作用的近乎对消。同时展示了基于 McMillan 公式在不同 $\mu^*$ 选择下的预测线。*

前驱 Cooper 流形式 ([[precursory_cooper_flow|#17]]) 揭示了量子临界行为的关键特征：在量子相变点附近（$g \to 0$），$T_c = \omega_\Lambda e^{1/g}$ 对耦合常数呈指数敏感。这意味着：

1. **精细调谐不是必要的**：Na 和 Mg 自然地处于临界区域，无需任何参数调谐
2. **配对场感受率发散**：在正常态中，当温度降至远低于 1 K 但高于（可能不存在的）$T_c$ 时，配对场感受率 $\chi \sim \ln(T)$ 发散——这是量子临界性的标志
3. **对称性考虑**：作者注意不使用"量子临界点"一词，因为某些其他对称通道中的超导可能先于 $s$ 波

### 与唯象预测的比较

| 金属 | $\lambda$ | $\mu^*$(EFT) | $T_c^{\mathrm{EFT}}$ | $\mu^*=0.1$ 预测 |
|------|-----------|-------------|----------------------|-----------------|
| Na | 0.2 | 0.15 | $2 \times 10^{-13}$ K | $6 \times 10^{-5}$ K |
| Mg | 0.24 | 0.14 | $5 \times 10^{-5}$ K | 0.007 K |

$\mu^*$ 从 0.1 增至 0.14--0.15 造成 $T_c$ 预测降低数个量级，再次展示了指数敏感性。

## 评审

- **Prior**: 依赖前提推断
- **Justification**: 接近量子临界点意味着 $T_c$ 对参数极端敏感；预测值更多是定性而非定量。
- **Belief**: 0.767

## 意义

Na 和 Mg 接近超导-正常态量子相变的预测是一个**可实验验证的信号**：即使这些金属不超导，在远低于 1 K 的温度下，配对场感受率也应展现量子临界标度 $\chi \sim \ln(T)$。这提供了一个无需精细调谐即可研究量子临界性的实验平台。此外，这一结果表明 $\mu^*$ 的精确值不仅关乎 $T_c$ 预测——它决定了材料位于量子相变的哪一侧。

## 注意事项

1. 极低 $T_c$ 预测的定量精度有限——但定性结论（接近量子相变）更为稳健。
2. 钾 (K) 的计算预测无超导性（$\lambda = 0.11$ 太弱而 $\mu^* = 0.16$ 太大）。
3. 实验验证可聚焦于配对感受率的对数发散，而非直接测量 $T_c$。

## 所属模块
[[s6_superconductors]]
