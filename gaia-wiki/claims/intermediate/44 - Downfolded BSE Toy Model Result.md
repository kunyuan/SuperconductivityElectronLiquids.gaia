---
type: claim
label: downfolded_bse_toy_model
aliases: [downfolded_bse_toy_model]
claim_number: 44
qid: "github:superconductivity_electron_liquids::downfolded_bse_toy_model"
module: s3_downfolding
exported: false
prior: null
belief: 0.3198662563385336
strategy_type: abduction
premise_count: 2
tags: [claim, s3-downfolding]
---

# #44 下折叠 BSE 玩具模型结果 (Downfolded BSE Toy Model Result)

对于同一玩具模型（类铝参数 $r_s = 1.92$，$\omega_D/E_F = 0.005$），求解下折叠的仅频率 Bethe-Salpeter 方程给出 $T_c^{\mathrm{approx}}/T_F = 10^{-5.667}$。

## 背景

这一计算是下折叠近似的直接验证：使用简化的仅频率 BSE 方程是否能准确再现完整动量-频率 BSE 的结果？

## 推导

**策略**: 溯因推理 (abduction)

**前提**:
- [[full_bse_toy_model|#42 完整 BSE 玩具模型结果]]
- 替代解释 (alternative_explanation)

完整 BSE 数值解给出 $T_c^{\mathrm{full}}/T_F = 10^{-5.668}$ ([[full_bse_toy_model|#42]])，下折叠 BSE 给出 $T_c^{\mathrm{approx}}/T_F = 10^{-5.667}$。两者仅差 0.2%，表明下折叠近似对传统金属参数是定量精确的。

![[8_1.jpg]]
*Fig. 5 | 完整和下折叠 BSE 的前驱 Cooper 流解的比较。当近似有效时，两个解遵循相同的普适对数标度，在 Debye 频率以下完美对齐。*

当下折叠近似成立时，完整解和简化解遵循相同的普适对数标度律（前驱 Cooper 流），在 Debye 频率以下完美对齐。

## 评审

- **Prior**: 依赖前提推断
- **Justification**: 0.2% 的吻合几乎不留替代解释的空间（替代解释 prior = 0.10）。
- **Belief**: 0.320

## 意义

0.2% 的定量精度直接验证了下折叠近似——将完整的动量-频率 BSE 约化为仅频率方程——在传统金属参数下是安全的。

## 注意事项

验证仅覆盖 $r_s = 1.92$ 的参数。对于极端密度（天体物理对象中的 $r_s \ll 1$）或二维系统（等离子体模式无能隙），下折叠的精度需要另行评估。

## 所属模块
[[s3_downfolding]]
