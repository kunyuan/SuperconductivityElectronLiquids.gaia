---
type: claim
label: dfpt_reliable_for_simple_metals
aliases: [dfpt_reliable_for_simple_metals]
claim_number: 53
qid: "github:superconductivity_electron_liquids::dfpt_reliable_for_simple_metals"
module: s5_eph_coupling
exported: true
prior: null
belief: 0.7474476451714931
strategy_type: deduction
premise_count: 2
tags: [claim, s5-eph-coupling]
---

# #53 DFPT 对简单金属的可靠性 (DFPT Reliable for Simple Metals)

对于简单金属，密度泛函微扰理论 (DFPT) 计算的电子-声子耦合常数 $\lambda$ 是可靠的：EFT 顶点与 DFPT 表达式在顶点层面吻合，准粒子态密度 $N_F^*$ 几乎等于能带态密度 $N_F^{(0)}$，因此 $\lambda_{\mathrm{EFT}} \approx \lambda_{\mathrm{DFPT}}$，修正在百分之几的量级。

## 背景

电子-声子耦合常数 $\lambda$ 量化了费米面上准粒子之间的声子介导吸引。当前最先进的第一性原理方法，如 DFPT，通过计算基态能量对晶格畸变的响应来求 $\lambda$。对于弱关联超导体，DFPT 已被验证，但对于关联系统，强重整化效应可能改变有效电子-声子相互作用，DFPT 的精度未经测试。本节回答的核心问题是：EFT 框架在什么条件下、以什么精度与 DFPT 的结果一致？

## 推导

**策略**: 演绎推理 (deduction)，经由复合推理 (composite) 分两步完成

**前提**:
- [[eft_vertex_matches_dfpt|#52 EFT 顶点与 DFPT 吻合]]
- [[quasiparticle_mass_near_unity|#28 准粒子质量接近 1]]

### 第一步：顶点层面的吻合

EFT 表达式给出电子-声子耦合顶点为（方程 32）：
$$g_\kappa(k, q) \equiv g_{\kappa q}^{(0)} \frac{z^e}{\epsilon_q} \Gamma_3^e(k, q)$$

其中 $g^{(0)}$ 是裸电子-声子耦合，$\epsilon_q$ 是电子介电函数，$\Gamma_3^e$ 是电子三点顶点修正。

DFPT 的 Kohn-Sham 表达式为（方程 33）：
$$g^{\mathrm{KS}}(q) = \frac{g_q^{(0)}}{1 - (v_q + f_{\mathrm{xc}}) \chi_0^e(q)}$$

其中 $f_{\mathrm{xc}}$ 是 LDA 中的交换关联核，$\chi_0^e$ 是 Lindhard 函数。

利用 $\Gamma_3^e \approx m^*/m$（[[gamma3_approximation|#38]]）和 Migdal 关系 $z^e \approx m/m^*$，乘积 $z^e \cdot \Gamma_3^e \approx 1$。因此 $g(k,q) \approx g_0(k,q)$，经屏蔽后精确给出 DFPT 的 Kohn-Sham 表达式。

通过 vDiagMC 在 UEG 中对 $r_s \in [1,5]$ 的计算，验证了（方程 34）：
$$z^e \frac{v_q}{\epsilon_q} \Gamma_3^e(k;q) \approx \frac{v_q}{1 - (v_q + f_{\mathrm{xc}}) \chi_0^e(q)}$$

对费米面上相关的动量转移 $|q| \leq 2k_F$ 成立，残余的 $k$ 依赖性很弱。

![[12_0.jpg]]
*Fig. 8 | UEG 中角分辨电子-声子顶点修正的比较：vDiagMC 数据点 vs DFPT 线。数据展示了 $z^{\mathrm{qp}} N_F W_q^{\mathrm{qp}} \Gamma_3^{\mathrm{qp}}(k,q)$。DFPT ansatz 基于 Lindhard 函数和 LDA 交换关联核。对所有 $r_s$ 值和入射/出射电子动量之间的角度 $\theta$ 都观察到良好的一致性，除了反向散射区域 $\theta \approx \pi$ 附近。*

图 8 中，介图的吻合尤为引人注目：尽管 $z^e$、$\epsilon_q$ 和 $\Gamma_3^e$ 各自都有大的相互作用修正，但它们的乘积涉及相互作用效应的**显著对消**，最终结果被 DFPT 表达式非常精确地近似。介图上，准粒子权重 $z^e$ 的电子-电子贡献被电子-声子顶点的重整化 $\Gamma_3^e$ 有效对消。这一对消在长波长极限（$q \to 0$）是精确的，而数值结果表明在整个费米面相关动量转移范围内都以出色的精度成立。

### 第二步：从顶点吻合到 $\lambda$ 吻合

得到 $\lambda$ 需要将电子-声子矩阵元与态密度结合（方程 31）：
$$\lambda = N_F \sum_\kappa \left\langle \frac{g_\kappa^2(k, q)}{\omega_{\kappa,q}^2} \right\rangle_{\mathrm{FS}}$$

EFT 使用准粒子态密度 $N_F^*$，而 DFPT 使用能带态密度 $N_F^{(0)}$。由于 $m^*/m \approx 1$（[[quasiparticle_mass_near_unity|#28]]）——高精度 QMC/DiagMC 计算表明在 $r_s \leq 5$ 时偏差小于 1%——两个态密度几乎相同：
$$N_F^* \approx N_F^{(0)}$$

因此：
$$\lambda_{\mathrm{EFT}} \approx \lambda_{\mathrm{DFPT}}$$

修正在百分之几的量级。

## 评审

- **Prior**: 依赖前提推断
- **Justification**: 结论建立在两个独立的数值验证之上（顶点吻合 + 质量接近 1），每个都有 vDiagMC 的直接数值支持。
- **Belief**: 0.747

## 支撑

- $\to$ [[ab_initio_workflow|#54 第一性原理 $T_c$ 预测工作流]] via deduction

## 意义

这一结果为在 EFT 框架中使用 DFPT 计算的 $\lambda$ 提供了严格的理论基础。对于简单金属（Li, Na, Mg, Al, Zn），可以直接使用 DFPT 的电子-声子耦合值，无需额外的多体修正。这极大简化了第一性原理工作流中声子部分的计算。

## 注意事项

1. 验证限于 UEG 模型中 $r_s \in [1, 5]$ 的范围；对于具有复杂能带结构的强关联系统（如过渡金属中的半芯电子），DFPT 的精度仍是一个需要进一步研究的开放问题。
2. 反向散射区域 $\theta \approx \pi$ 的不一致源于 Cooper 通道的对数发散，但这一区域对 $\lambda$ 的费米面平均贡献有限。
3. $z^e \cdot \Gamma_3^e \approx 1$ 的对消虽然在长波长极限精确成立，但其在有限动量下的有效性需要逐材料验证。

## 所属模块
[[s5_eph_coupling]]
