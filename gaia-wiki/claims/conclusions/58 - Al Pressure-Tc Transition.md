---
type: claim
label: al_pressure_transition
aliases: [al_pressure_transition]
claim_number: 58
qid: "github:superconductivity_electron_liquids::al_pressure_transition"
module: s6_superconductors
exported: true
prior: null
belief: 0.7669054711867636
strategy_type: noisy_and
premise_count: 1
tags: [claim, s6-superconductors]
---

# #58 铝的压力-$T_c$ 转变 (Al Pressure-Tc Transition)

在静水压力下，第一性原理框架预测铝的超导 $T_c$ 单调递减，与高达 6 GPa 的实验数据一致。框架预测铝的超导性在约 60 GPa 时消失；在 20 GPa 时，$T_c$ 已被压低至 1 mK 以下。

## 背景

铝在常压下 $T_c = 1.2$ K。实验测量（Levy 等人 1964，Gubser 等人 1975）表明 $T_c$ 随压力增大而降低，数据覆盖至约 6 GPa。高压下 $T_c$ 的行为——特别是超导性是否完全消失——是一个未解决的实验问题。

## 推导

**策略**: noisy_and

**前提**:
- [[ab_initio_workflow|#54 第一性原理 $T_c$ 预测工作流]]

### 压力效应的物理机制

随着静水压力增加：
1. 晶格常数减小，电子密度增大，$r_s$ 降低
2. $r_s$ 降低使 $\mu_{E_F}$ 减小（vDiagMC 参数化中 $\mu_{E_F} \approx 0.27 r_s$）
3. 然而，$\lambda$ 也因晶格硬化而减小
4. **净效应**：$\mu^*$ 和 $\lambda$ 都减小，但它们之差（有效配对耦合 $g$）也减小，$T_c$ 因指数敏感性而急剧下降

铝的压力依赖晶格常数由 Friedli 和 Ashcroft 的状态方程拟合确定（假设无结构相变）。

### 与实验数据的比较

![[14_0.jpg]]
*Fig. 10 | 铝超导临界温度的压力依赖性。方块为 EFT 理论结果；线为眼导线。Levy 等人（菱形）和 Gubser 等人（圆形）的实验数据在常压至 6 GPa 范围内与理论良好吻合。内插图展示了高压区域的外推，预测超导性在 ~60 GPa 消失。*

在 0--6 GPa 的实验覆盖范围内，EFT 结果准确捕获了 $T_c$ 随压力递减的趋势。虽然 SCDFT 方法也给出类似的良好吻合，但 SCDFT 对库仑排斥的处理涉及顶点修正、屏蔽动力学和准粒子权重方面的不受控近似；相比之下，本方法基于严格的微观基础。

### 高压外推预测

超越实验压力极限的外推（假设无结构相变）：
- **20 GPa**：$T_c$ 已被压低到 1 mK 以下，超出当前实验技术的探测范围
- **~60 GPa**：超导性完全消失

这一预测源于电子-声子吸引和库仑排斥之间精细平衡的压力依赖性。

## 评审

- **Prior**: 依赖前提推断
- **Justification**: 常压至 6 GPa 有实验验证；高压外推增加不确定性（假设无结构相变）。
- **Belief**: 0.767

## 意义

这是一个**可测试的预测**：铝在 ~60 GPa 处超导-正常态量子相变。此预测源于库仑排斥和声子介导吸引之间的相互作用，是第一性原理框架的直接推论。此外，在 20 GPa 时 $T_c < 1$ mK 的预测意味着铝在中等压力下已实际上不再超导。

## 注意事项

1. 高压外推假设铝保持 FCC 结构——实际上铝在高压下可能发生结构相变，这将改变 $\lambda$ 和 $\mu^*$。
2. 预测的精度在高压下降低，因为 UEG 参数化在不同 $r_s$ 的插值增加了不确定性。
3. 实验验证需要将 $T_c$ 测量扩展到远超当前 6 GPa 的压力范围。

## 所属模块
[[s6_superconductors]]
