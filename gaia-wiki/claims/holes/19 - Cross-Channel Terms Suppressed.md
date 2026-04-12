---
type: claim
label: cross_term_suppressed
aliases: [cross_term_suppressed]
claim_number: 19
qid: "github:superconductivity_electron_liquids::cross_term_suppressed"
module: s3_downfolding
exported: false
prior: 0.9
belief: 0.5008292986359677
strategy_type: null
premise_count: 0
tags: [claim, s3-downfolding]
---

# #19 交叉通道项被压低

> 混合 Coulomb 和声子通道的交叉项被等离激元频率 $\omega_p$ 压低，量级为 $O(\omega_c^2/\omega_p^2)$，其中 $\omega_c$ 是满足 $\omega_D \ll \omega_c \ll E_F$ 的中间能量截断。对于大多数三维金属，$\omega_c/\omega_p \lesssim 0.1$，故交叉项贡献不超过 1%。

## 背景

下折叠（downfolding）程序能否将全 BSE 方程简化为频率-only 的有效方程，关键取决于 Coulomb 通道与声子通道之间的交叉项是否可以忽略。物理上，$\tilde{\Gamma}^e$（纯电子不可约顶角）编码了长程动态屏蔽 Coulomb 相互作用，其红外行为由 $W^s \propto (\omega - \omega')^2 / [(\omega-\omega')^2 + \omega_p^2]$ 给出（等离激元极模型）。当 $\omega_c \ll \omega_p$ 时，交叉项 $\tilde{\Gamma}^e \cdot \phi \cdot W^{\mathrm{ph}}$ 在低能子空间内被 $\omega_c^2/\omega_p^2$ 压低，使得 Coulomb 与声子通道有效解耦。在三维金属中 $\omega_p / E_F \propto 1/\sqrt{r_s}$，对 $r_s \gtrsim 1$ 的材料 $\omega_c/\omega_p \lesssim 0.1$。论文附录 C3 给出了详细推导。

## 来源

- **理论推导**：等离激元极模型给出交叉项的保守上界（论文公式 15、附录 C3）。
- **定量估计**：即使采用高估交叉项的等离激元极模型，$\omega_c^2/\omega_p^2 \leq 0.01$。
- **已知局限**：在二维电子气（无隙等离激元模式）或极低密度体系中，$\omega_p$ 软化导致交叉项不再可忽略。

## 评审

**先验概率（Prior）**：0.90
**理由**：$\omega_c^2/\omega_p^2 \leq 0.01$；等离激元极模型给出保守估计。
**信念度（Belief）**：0.50

## 支撑

- → [[downfolded_bse|#43 下折叠 BSE]] 经由演绎推理

## 所属模块

[[s3_downfolding|BSE 下折叠]]
