---
type: claim
label: eft_vertex_matches_dfpt
aliases: [eft_vertex_matches_dfpt]
claim_number: 52
qid: "github:superconductivity_electron_liquids::eft_vertex_matches_dfpt"
module: s5_eph_coupling
exported: false
prior: null
belief: 0.5846388357113955
strategy_type: deduction
premise_count: 2
tags: [claim, s5-eph-coupling]
---

# #52 EFT 顶点与 DFPT 吻合 (EFT Vertex Matches DFPT)

在均匀电子气密度 $r_s \in [1,5]$ 下，EFT 电子-声子顶点 $g(k,q) = g_q^{(0)} \cdot (z^e/\epsilon_q) \cdot \Gamma_3^e(k;q)$ 被 DFPT Kohn-Sham 屏蔽势 $g^{\mathrm{KS}}(q) = g_q^{(0)} / [1 - (v_q + f_{xc})\chi_0^e(q)]$ 很好地数值近似，适用于费米面相关动量转移 $|q| \leq 2k_F$，残余 $k$ 依赖性很弱。

## 背景

EFT 和 DFPT 对电子-声子耦合的处理本质上不同：EFT 基于多体准粒子图像，包含 $z^e$、$\Gamma_3^e$ 和精确屏蔽；DFPT 基于 Kohn-Sham 密度泛函理论，通过交换关联核 $f_{\mathrm{xc}}$ 近似处理关联效应。两者的吻合是一个非平凡的结果。

## 推导

**策略**: 演绎推理 (deduction)

**前提**:
- [[eft_eph_vertex|#50 EFT 电子-声子顶点]]
- [[gamma3_approximation|#38 费米球内 $\Gamma_3$ 的近似]]

将 $\Gamma_3^e \approx m^*/m$ ([[gamma3_approximation|#38]]) 代入 EFT 顶点表达式 ([[eft_eph_vertex|#50]]) $g = z^e \cdot \Gamma_3^e \cdot g_0$，利用 Migdal 关系 $z^e \approx m/m^*$，乘积 $z^e \cdot \Gamma_3^e \approx (m/m^*)(m^*/m) = 1$。因此 $g(k,q) \approx g_0(k,q)$，经屏蔽后精确给出 DFPT 的 Kohn-Sham 表达式（方程 34）：

$$z^e \frac{v_q}{\epsilon_q} \Gamma_3^e(k;q) \approx \frac{v_q}{1 - (v_q + f_{xc})\chi_0^e(q)}$$

介图上，电子-电子对准粒子权重 $z^e$ 的贡献被电子-声子顶点的重整化 $\Gamma_3^e$ 有效对消。这一对消在长波长极限精确成立（Ward 恒等式），vDiagMC 数值结果表明它在整个费米面相关动量转移范围内以出色精度成立。

![[12_0.jpg]]
*Fig. 8 | UEG 中角分辨电子-声子顶点修正的比较。尽管 $z^e$、$\epsilon_q$ 和 $\Gamma_3^e$ 各自都有大的相互作用修正，但它们的乘积涉及显著的对消，最终结果被 DFPT 表达式精确近似。*

## 评审

- **Prior**: 依赖前提推断
- **Justification**: vDiagMC 数值直接验证了吻合；主要不确定性在反向散射区域。
- **Belief**: 0.585

## 支撑

- $\to$ [[dfpt_reliable_for_simple_metals|#53 DFPT 对简单金属的可靠性]] via deduction

## 意义

EFT 与 DFPT 的顶点级别吻合是验证 DFPT $\lambda$ 可靠性的关键一步。这一结果将多体理论（EFT）和密度泛函方法（DFPT）在电子-声子耦合层面统一起来。

## 注意事项

吻合在反向散射区域 $\theta \approx \pi$（$q \approx 2k_F$）稍差，因为 Cooper 通道对数发散使介图级数变得敏感。

## 所属模块
[[s5_eph_coupling]]
