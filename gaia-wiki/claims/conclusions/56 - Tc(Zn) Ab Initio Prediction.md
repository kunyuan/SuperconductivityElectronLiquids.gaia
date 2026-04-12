---
type: claim
label: tc_zn_predicted
aliases: [tc_zn_predicted]
claim_number: 56
qid: "github:superconductivity_electron_liquids::tc_zn_predicted"
module: s6_superconductors
exported: true
prior: null
belief: 0.9016568687862857
strategy_type: noisy_and
premise_count: 1
tags: [claim, s6-superconductors]
---

# #56 锌的第一性原理 $T_c$ 预测 (Tc(Zn) Ab Initio Prediction)

第一性原理预测的锌超导转变温度为 $T_c^{\mathrm{EFT}} = 0.874$ K，与实验值 $T_c^{\mathrm{exp}} = 0.875$ K 几乎精确吻合。第一性原理的 $\mu^*(\mathrm{Zn}) = 0.12$ 由 vDiagMC 在 $r_s = 2.90$（带质量 $m_b = 1.0$）处的 $\mu_{E_F}$ 经 BTS 重整化得到。

## 背景

锌是 HCP 结构的简单金属。实验 $T_c = 0.875$ K 是精确测量的值。使用标准 $\mu^* = 0.1$ 的 McMillan 公式给出 $T_c \approx 1.37$ K，高估了 57%。

**锌的材料参数**（[[zinc_parameters|#33]]）：HCP 晶体结构，$r_s = 2.90$，$m_b = 1.0$，DFPT 电子-声子耦合 $\lambda = 0.502$，$\omega_{\mathrm{log}} = 111$ K，$T_F = 1.21 \times 10^5$ K。

## 推导

**策略**: noisy_and

**前提**:
- [[ab_initio_workflow|#54 第一性原理 $T_c$ 预测工作流]]

### $\mu^*$ 确定

$r_s = 2.90$，$m_b = 1.0$（无重标），在 vDiagMC 参数化中插值得到 $\mu_{E_F}$，经 BTS 降标得 $\mu^* = 0.12$。

### $\lambda$ 确定

DFPT 计算（Quantum ESPRESSO + EPW）：$\lambda = 0.502$，$\omega_{\mathrm{log}} = 111$ K。Wannier 投影使用 $s$, $p$, $d$ 轨道。HCP 结构的 $k/q$ 细网格为 $60 \times 60 \times 30$。

### 求解下折叠 BSE

将 $\mu^* = 0.12$ 和 $\lambda = 0.502$ 代入，得到：
$$T_c^{\mathrm{EFT}} = 0.874 \text{ K}$$

### 与实验和唯象预测的比较

| 方法 | $\mu^*$ | $T_c$ (K) | 偏差 |
|------|---------|-----------|------|
| 实验 | — | 0.875 | — |
| EFT (本工作) | 0.12 | 0.874 | -0.1% |
| McMillan ($\mu^*=0.1$) | 0.1 | 1.37 | +57% |

锌的结果是整个框架中最引人注目的成功案例：第一性原理预测与实验值的偏差仅 0.1%。$\mu^* = 0.12$ 比标准猜测值 0.1 略高，恰好足以将预测从 1.37 K 拉到 0.874 K。

## 评审

- **Prior**: 依赖前提推断
- **Justification**: 材料特定的应用；$r_s = 2.90$ 在 vDiagMC 验证范围内；$m_b = 1.0$ 意味着无需带质量重标。
- **Belief**: 0.902

## 意义

锌的近乎精确吻合是框架预测能力的有力验证。相比唯象方法 57% 的偏差，第一性原理方法将误差降低了近三个量级。

## 注意事项

1. $m_b = 1.0$ 的简单性使锌成为框架验证的理想案例——无需带质量修正带来的额外不确定性。
2. 锌的 $d$ 电子可能引入 UEG 描述之外的效应，但 Wannier 投影中显式包含 $d$ 轨道部分缓解了这一问题。

## 所属模块
[[s6_superconductors]]
