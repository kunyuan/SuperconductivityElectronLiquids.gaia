---
type: claim
label: full_bse_toy_model
aliases: [full_bse_toy_model]
claim_number: 42
qid: "github:superconductivity_electron_liquids::full_bse_toy_model"
module: s3_downfolding
exported: false
prior: null
belief: 0.7573869766027367
strategy_type: noisy_and
premise_count: 1
tags: [claim, s3-downfolding]
---

# #42 完整 BSE 玩具模型结果 (Full BSE Toy Model Result)

对于具有类铝参数（Wigner-Seitz 半径 $r_s = 1.92$，绝热比 $\omega_D/E_F = 0.005$）的玩具模型，数值求解完整的频率-动量依赖 Bethe-Salpeter 方程 (BSE)——使用 RPA 动态屏蔽库仑相互作用作为电子不可约顶点加上模型声子相互作用，不做任何下折叠近似——给出超导转变温度 $T_c^{\mathrm{full}}/T_F = 10^{-5.668}$。

## 背景

为了验证下折叠近似的精度，需要一个完整 BSE 的精确数值基准。玩具模型使用 RPA 动态屏蔽作为 $\tilde{\Gamma}^e$ 的近似，声子介导相互作用取模型形式（方程 26）：
$$W_{q\nu}^{\mathrm{ph}} = -\frac{g/N_F}{1 + (q/2k_F)^2} \frac{\omega_q^2}{\nu^2 + \omega_q^2}$$

声子色散 $\omega_q^2 = \omega_D^2 (q/k_F)^2/(1 + (q/k_F)^2)$，耦合强度 $g = 0.4$。

## 推导

**策略**: noisy_and

**前提**:
- [[bse_kernel_decomposition|#39 BSE 核分解]]

利用 BSE 核分解 ([[bse_kernel_decomposition|#39]])，将电子四点顶点近似为 RPA 动态屏蔽库仑相互作用 $W_{\mathrm{RPA}} = v_q/(1 - v_q \Pi_{q\nu}^0)$（[[rpa_dynamic_screening|#20]]），在 $r_s = 1.92$、$\omega_D/E_F = 0.005$ 的参数下数值求解完整的频率-动量 BSE。通过前驱 Cooper 流分析得到 $T_c^{\mathrm{full}}/T_F = 10^{-5.668}$。

![[8_1.jpg]]
*Fig. 5 | 完整和下折叠 BSE 的前驱 Cooper 流解的比较。在 $r_s = 1.92$（代表性铝参数）的中等关联情况下，$T_c^{\mathrm{full}}/T_F = 10^{-5.668}$ 与 $T_c^{\mathrm{approx}}/T_F = 10^{-5.667}$（差异 ~0.2%），确认了下折叠近似的有效性。*

## 评审

- **Prior**: 依赖前提推断
- **Justification**: 良好控制的数值计算。
- **Belief**: 0.757

## 支撑

- $\to$ [[downfolded_bse_toy_model|#44 下折叠 BSE 玩具模型结果]] via abduction

## 意义

提供了下折叠近似验证所需的精确数值基准。

## 注意事项

使用 RPA 作为 $\tilde{\Gamma}^e$ 的近似在 $r_s \gtrsim 1$ 时本身不精确，但作为验证下折叠近似的数值基准是充分的——因为比较的是同一近似下完整 BSE 和下折叠 BSE 的差异。

## 所属模块
[[s3_downfolding]]
