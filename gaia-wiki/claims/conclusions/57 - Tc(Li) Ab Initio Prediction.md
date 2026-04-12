---
type: claim
label: tc_li_predicted
aliases: [tc_li_predicted]
claim_number: 57
qid: "github:superconductivity_electron_liquids::tc_li_predicted"
module: s6_superconductors
exported: true
prior: null
belief: 0.8999288711836234
strategy_type: noisy_and
premise_count: 1
tags: [claim, s6-superconductors]
---

# #57 锂的第一性原理 $T_c$ 预测 (Tc(Li) Ab Initio Prediction)

第一性原理预测的锂（9R 结构）超导转变温度为 $T_c^{\mathrm{EFT}} = 5 \times 10^{-3}$ K，在实验观测值 $T_c^{\mathrm{exp}} \approx 4 \times 10^{-4}$ K 的一个量级范围内。大的 $\mu^*(\mathrm{Li}) = 0.18$（源于 $r_s = 3.25$，带质量 $m_b = 1.75$）几乎完全对消了声子介导吸引 $\lambda = 0.34$，将 $T_c$ 推到极低温度。HCP 结构给出 $T_c^{\mathrm{EFT}} = 0.03$ K（$\mu^* = 0.17$，$\lambda = 0.37$）。

## 背景

锂是理论物理中一个经典的困难案例。使用标准 $\mu^* = 0.1$ 的 McMillan 公式给出 $T_c \approx 0.35$ K，高估实验值三个量级。这一戏剧性偏差长期以来是凝聚态理论中最令人尴尬的定量失败之一。2007 年 Tuoriniemi 等人在常压下测量到锂的 $T_c \approx 4 \times 10^{-4}$ K (0.4 mK)，但超低温下的晶体结构仍有争议。

**锂的材料参数**（[[lithium_parameters|#30]]）：
- 9R 结构：$r_s = 3.25$，$m_b = 1.75$，$\lambda = 0.34$，$\omega_{\mathrm{log}} = 242$ K，$T_F = 4.0 \times 10^4$ K
- HCP 结构：$r_s = 3.19$，$m_b = 1.4$，$\lambda = 0.37$，$\omega_{\mathrm{log}} = 243$ K，$T_F = 4.1 \times 10^4$ K

## 推导

**策略**: noisy_and

**前提**:
- [[ab_initio_workflow|#54 第一性原理 $T_c$ 预测工作流]]

### $\mu^*$ 的关键差异

锂的 $\mu^*$ 值之所以远大于其他简单金属，源于两个因素：

1. **较高的 $r_s$**：锂的 $r_s = 3.25$，远大于铝的 2.07，对应更强的电子-电子关联。从 vDiagMC 的 $\mu_{E_F}(r_s) \approx 0.27 r_s$，$r_s = 3.25$ 给出显著更大的 $\mu_{E_F}$。

2. **大的带质量**：$m_b = 1.75$ 将有效 $r_s$ 重标为 $m_b \cdot r_s \approx 5.7$（9R 结构），进一步增大了 $\mu_{E_F}$。

经 BTS 降标得到 $\mu^* = 0.18$（9R），远大于标准猜测值 0.1。

### $T_c$ 的指数敏感性

在有效配对常数 $g = \lambda - \mu^*(1 + 0.62\lambda)$ 很小的情况下，$T_c$ 对 $g$ 表现出极端的指数敏感性：

$$T_c \propto \omega_{\mathrm{log}} \exp(-1/g)$$

对于 9R 锂：
- $\lambda = 0.34$，$\mu^* = 0.18$
- $g \approx 0.34 - 0.18 \times (1 + 0.62 \times 0.34) = 0.34 - 0.22 = 0.12$（小值）
- 指数敏感性将 $\mu^*$ 从 0.10 到 0.18 的差异放大为 $T_c$ 近三个量级的变化

| 结构 | $r_s$ | $m_b$ | $\lambda$ | $\mu^*$ | $T_c^{\mathrm{EFT}}$ (K) |
|------|--------|--------|-----------|---------|--------------------------|
| 9R | 3.25 | 1.75 | 0.34 | 0.18 | $5 \times 10^{-3}$ |
| HCP | 3.19 | 1.4 | 0.37 | 0.17 | 0.03 |

### 与实验和唯象预测的比较

| 方法 | $\mu^*$ | $T_c$ (K) | 与实验偏差 |
|------|---------|-----------|-----------|
| 实验 | — | $4 \times 10^{-4}$ | — |
| EFT 9R (本工作) | 0.18 | $5 \times 10^{-3}$ | ~10倍 |
| EFT HCP (本工作) | 0.17 | 0.03 | ~100倍 |
| McMillan ($\mu^*=0.1$) | 0.1 | 0.35 | ~1000倍 |

第一性原理方法实现了**数量级的改进**：从三个量级的偏差降至一个量级。剩余偏差部分归因于超低温下晶体结构的争议——9R 和 HCP 的预测跨越两个量级，表明 $T_c$ 对晶体结构极其敏感。

## 评审

- **Prior**: 依赖前提推断
- **Justification**: 锂的结构不确定性增加了额外风险；$r_s$ 经带质量重标后较大（~5.7），接近 vDiagMC 验证范围的边界。
- **Belief**: 0.900

## 意义

锂的案例最有力地展示了第一性原理 $\mu^*$ 的价值：正是因为 $\lambda$ 和 $\mu^*$ 几乎相消，传统唯象方法中 $\mu^*$ 的微小不确定性被指数敏感性放大为 $T_c$ 预测的灾难性失败。该结果揭示了一个重要物理图像——某些超导体具有极低 $T_c$ 不是因为 $\lambda$ 消失般小，而是因为声子介导吸引被库仑排斥几乎完全对消。

## 注意事项

1. 9R 与 HCP 预测间两个量级的差异突显了晶体结构对 $T_c$ 的重要性——通过 $m_b$ 影响 $\mu^*$。
2. 重标 $r_s \approx 5.7$ 在 vDiagMC 数据的外推区域，增加了系统不确定性。
3. 超低温下锂的晶体结构仍是活跃的实验争论，这为理论预测的精确比较设置了基本限制。

## 所属模块
[[s6_superconductors]]
