---
type: claim
label: gamma3_approximation
aliases: [gamma3_approximation]
claim_number: 38
qid: "github:superconductivity_electron_liquids::gamma3_approximation"
module: s5_eph_coupling
exported: false
prior: null
belief: 0.6236527120048654
strategy_type: abduction
premise_count: 2
tags: [claim, s5-eph-coupling]
---

# #38 费米球内 $\Gamma_3$ 的近似 (Approximate Gamma_3 within Fermi Sphere)

费米球内态的三点顶点 $\Gamma_3^e(k, q)$ 可以通过在两个受控极限之间插值来精确近似：(i) $q \to 0$ 处精确的 Ward 恒等式给出 $\Gamma_3^e = 1 - \partial\Sigma/\partial\epsilon_k = m^*/m$，(ii) 有限 $q$ 处的 vDiagMC 结果显示光滑、温和的变化。对于简单金属，这在相关动量范围内给出 $\Gamma_3^e \approx m^*/m$，精度在 10--15% 以内。

## 背景

三点顶点 $\Gamma_3^e$ 描述了电子关联对电子-声子耦合的修正。在 EFT 顶点 $g = z^e \cdot \Gamma_3^e \cdot g_0$ 中，$\Gamma_3^e$ 和 $z^e$ 的乘积决定了准粒子电子-声子耦合相对于裸值的修正。

## 推导

**策略**: 归纳推理 (induction)

**前提**:
- [[ward_identity|#25 Ward 恒等式 ($q \to 0$)]]
- 替代解释 (alternative_explanation)

**证据 1：Ward 恒等式**

精确的 Ward 恒等式 ([[ward_identity|#25]]) 将 $\Gamma_3^e$ 在长波长极限与电子自能联系：
$$\lim_{q \to 0} \Gamma_3^e(k, q) = 1 - \frac{\partial\Sigma(k)}{\partial\epsilon_k} = \frac{m^*}{m}$$

这是电荷守恒的精确推论，提供了 $q = 0$ 处的精确约束。

**证据 2：vDiagMC 有限 $q$ 计算**

vDiagMC 对 UEG 在 $r_s \in [2, 4]$ 的三点顶点计算 ([[gamma3_vdiagmc|#26]]) 显示：在费米球内（$|k|, |k+q| \lesssim k_F$），顶点修正在 10--20% 的水平，随 $q$ 光滑变化。

![[12_0.jpg]]
*Fig. 8 | UEG 中角分辨电子-声子顶点修正的比较：vDiagMC (点) vs DFPT (线)，显示费米面动量转移范围内的良好一致性。*

通过在精确的 $q = 0$ 约束和数值确定的有限 $q$ 行为之间插值，得到近似 $\Gamma_3^e \approx m^*/m$，捕获了主要效应（质量重整化），同时将动量依赖性的误差限制在 10--15%。

## 评审

- **Prior**: 依赖前提推断
- **Justification**: Ward 恒等式精确（QFT）；vDiagMC 有限 $q$ 结果可能有比声称更大的系统误差。
- **Belief**: 0.624

## 支撑

- $\to$ [[eft_vertex_matches_dfpt|#52 EFT 顶点与 DFPT 吻合]] via deduction

## 意义

这一近似是 EFT 顶点与 DFPT 吻合的关键环节——它与 $z^e \approx m/m^*$ 组合后给出乘积 $z^e \cdot \Gamma_3^e \approx 1$，实现了 EFT 和 DFPT 电子-声子耦合的一致。

## 注意事项

1. 近似对反向散射区域 $\theta \approx \pi$ 的精度较差（Cooper 通道对数发散使介图级数变得敏感），但这一区域对 $\lambda$ 的费米面平均贡献有限。
2. 对于具有显著有效质量增强的强关联系统，$\Gamma_3^e$ 的动量依赖性可能更强。

## 所属模块
[[s5_eph_coupling]]
