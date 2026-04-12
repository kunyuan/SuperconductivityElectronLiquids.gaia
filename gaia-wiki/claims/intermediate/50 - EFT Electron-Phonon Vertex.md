---
type: claim
label: eft_eph_vertex
aliases: [eft_eph_vertex]
claim_number: 50
qid: "github:superconductivity_electron_liquids::eft_eph_vertex"
module: s5_eph_coupling
exported: false
prior: null
belief: 0.6622555419995318
strategy_type: deduction
premise_count: 1
tags: [claim, s5-eph-coupling]
---

# #50 EFT 电子-声子顶点 (EFT Electron-Phonon Vertex)

EFT 电子-声子耦合顶点的表达式 $g(k, q) = z^e \cdot \Gamma_3^e(k, q) \cdot g_0(k, q)$ 将完整顶点因式分解为准粒子重整化因子 $z^e$、电子三点顶点修正 $\Gamma_3^e$ 和裸电子-声子矩阵元 $g_0$。下折叠 BSE 中对应的 $\lambda$ 是 $|g(k,q)|^2$ 由声子传播子加权的费米面平均。

## 背景

裸电子-声子耦合 $g_q^{(0)}$ 描述的是裸电子和声子之间的相互作用。但在多体理论中，实际的准粒子-声子耦合需要考虑电子关联的效应——屏蔽（通过介电函数 $\epsilon_q$）和顶点修正（通过三点顶点 $\Gamma_3^e$），以及准粒子权重（$z^e$）。

## 推导

**策略**: 演绎推理 (deduction)

**前提**:
- [[lambda_microscopic_definition|#46 $\lambda$ 的微观定义]]

$\lambda$ 的微观定义 ([[lambda_microscopic_definition|#46]]) 涉及 $W^{\mathrm{ph}}$ 的费米面平均，由准粒子因子加权。将 $W^{\mathrm{ph}}$ 展开为声子传播子和电子-声子顶点的乘积，并从配对传播子的相干部分分离出准粒子权重 $z^e$，得到 EFT 顶点（方程 32）：

$$g_\kappa(k, q) \equiv g_{\kappa q}^{(0)} \frac{z^e}{\epsilon_q} \Gamma_3^e(k, q)$$

其中组合 $z^e \Gamma_3^e(k,q)$ 可以解释为准粒子顶点修正——被电子-电子关联修饰的准粒子间的电子-声子耦合。

对应的 $\lambda$ 为（方程 31）：
$$\lambda = N_F \sum_\kappa \left\langle \frac{g_\kappa^2(k, q)}{\omega_{\kappa,q}^2} \right\rangle_{\mathrm{FS}}$$

## 评审

- **Prior**: 依赖前提推断
- **Justification**: 直接的因式分解，无额外近似。
- **Belief**: 0.662

## 支撑

- $\to$ [[eft_vertex_matches_dfpt|#52 EFT 顶点与 DFPT 吻合]] via deduction

## 意义

EFT 顶点表达式提供了将微观量（$z^e$、$\Gamma_3^e$）与可测量/可计算量联系的桥梁。它明确了准粒子权重因子在电子-声子耦合中的正确位置，解决了文献中长期存在的歧义。

## 注意事项

裸耦合 $g_q^{(0)}$ 在 $q \to 0$ 时发散为 $q v_q$（纵向模式），但经屏蔽后变为正则。与横向模式的耦合一般正则，在自由电子极限中消失。

## 所属模块
[[s5_eph_coupling]]
