---
type: claim
label: downfolded_bse
aliases: [downfolded_bse]
claim_number: 43
qid: "github:superconductivity_electron_liquids::downfolded_bse"
module: s3_downfolding
exported: true
prior: null
belief: 0.3283061767769196
strategy_type: deduction
premise_count: 2
tags: [claim, s3-downfolding]
---

# #43 频率空间下折叠 Bethe-Salpeter 方程 (Downfolded BSE)

完整的动量-频率 Bethe-Salpeter 方程核可以被严格约化为仅含 Matsubara 频率的一维积分方程。其有效核为 $K(\omega, \omega') = \lambda(\omega, \omega') - \mu_{\omega_c}(\omega, \omega')$，其中声子介导的吸引 $\lambda$ 和库仑赝势 $\mu_{\omega_c}$ 均有严格的微观定义。动量积分被吸收进态密度，而配对传播子的相干部分产生驱动 Cooper 不稳定性的 BCS 对数。

## 背景

传统的 Migdal-Eliashberg 理论试图将完整的多体问题简化为费米面附近的低能有效理论，但高能电子自由度的积出（"下折叠"）一直依赖唯象处理——库仑效应被简单替换为一个静态赝势 $\mu^*$，忽略了库仑涨落对准粒子重整化和电子-声子耦合的修正。本文通过在双电子通道（而非传统的单电子或电子-空穴通道）中引入能标分离，提供了一个受控的微观下折叠方案。

## 推导

**策略**: 演绎推理 (deduction)

**前提**:
- [[cross_term_suppressed|#19 交叉通道项被压低]]
- [[bse_kernel_decomposition|#39 BSE 核分解]]

### 第一步：配对传播子的精确分解

出发点是完整的 BSE（方程 8）：
$$\Lambda_{k\omega} = \eta_{\omega} + \int_{k'\omega'} \tilde{\Gamma}_{k\omega;k'\omega'} \, G_{k'\omega'} G_{-k',-\omega'} \, \Lambda_{k'\omega'}$$

核心思想是在**双电子通道**中引入能标分离。将配对传播子（两个单粒子格林函数之积）精确分解为低能相干部分和高能非相干部分（方程 13）：
$$G_{k,\omega} G_{-k,-\omega} = \Pi_{\mathrm{BCS}} + \phi_{k\omega}$$

其中相干部分具有标准的 BCS 形式（方程 14）：
$$\Pi_{\mathrm{BCS}} = \frac{(z^e)^2}{\left(\frac{\omega}{z_\omega^{\mathrm{ph}}}\right)^2 + \epsilon_k^2} \Theta(\omega_c - |\epsilon_k|)$$

这里 $z^e$ 是来自电子-电子相互作用的准粒子权重（在相关能标上与动量和频率无关），$z_\omega^{\mathrm{ph}}$ 是来自电子-声子相互作用的频率依赖准粒子权重，$\epsilon_k$ 是经电子-电子相互作用重整化的线性化准粒子色散。非相干部分 $\phi$ 是电子液体的内在性质，在费米面附近保持正则，声子贡献为 $\mathcal{O}(\omega_D/E_F)$。

![[4_0.jpg]]
*Fig. 1 | 电子自能的正常分量由声子介导的电子-电子相互作用 $W^{\mathrm{ph}}$ 的自洽 Fock 图近似。根据 Migdal 定理，基于 $W^{\mathrm{ph}}$ 的高阶顶点修正被 $O(\omega_D/E_F)$ 压低。*

### 第二步：BSE 核的分离结构

根据 BSE 核分解 ([[bse_kernel_decomposition|#39]])，利用 Migdal 定理，BSE 核可以写为纯电子部分和声子介导部分之和：
$$\tilde{\Gamma} = \tilde{\Gamma}^e + W^{\mathrm{ph}} + O\left(\frac{\omega_D}{E_F}\right)$$

将配对传播子分解代入完整 BSE，并按频率范围将反常顶点 $\Lambda$ 分为低能分量 $\Lambda_L$（$|\omega| < \omega_c$）和高能分量 $\Lambda_H$（$|\omega| > \omega_c$），得到耦合方程组（方程 16）：
$$\Lambda_L = \eta_\omega + \tilde{\Gamma}_{LL} \Pi_{\mathrm{BCS}} \Lambda_L + \tilde{\Gamma}_{LH} \phi \Lambda_H + O\left(\frac{\omega_c^2}{\omega_p^2}\right)$$
$$\Lambda_H = \tilde{\Gamma}_{HL} \Pi_{\mathrm{BCS}} \Lambda_L + \tilde{\Gamma}_{HH} \phi \Lambda_H + O\left(\frac{\omega_c^2}{\omega_p^2}\right)$$

### 第三步：交叉项的压低与低能有效理论

关键的物理论证是：混合库仑和声子通道的交叉项被等离子体频率压低，量级为 $O(\omega_c^2/\omega_p^2)$（[[cross_term_suppressed|#19]]）。在三维金属中，$\omega_c/\omega_p \lesssim 0.1$，交叉项贡献不超过 1%。

这一压低的物理根源在于，在小动量转移和低频极限下，动态屏蔽相互作用严格遵循渐近形式（方程 15）：
$$W_{k-k',\omega-\omega'}^s = \frac{4\pi e^2}{|k-k'|^2} \frac{(\omega-\omega')^2}{(\omega-\omega')^2 + \omega_p^2}$$

如 Appendix C3 所详述，即使使用等离子体极模型（高估了相互作用在相空间中的范围），交叉项仍被 $\omega_c^2/\omega_p^2$ 压低。

忽略被压低的交叉项并消去高能部分 $\Lambda_H$，得到限制在低能窗口 $|\omega| < \omega_c$ 内的有效 BSE（方程 17）：
$$\Lambda_{k\omega} = \eta_\omega + \sum_{k',\omega'} \tilde{\Gamma}_{k\omega,k'\omega'}^{\omega_c} \Pi_{\mathrm{BCS}}(k',\omega') \Lambda_{k',\omega'}$$

其中有效顶点 $\tilde{\Gamma}^{\omega_c}$ 通过递推关系吸收了所有高能重整化效应（方程 18），并具有可分离形式（方程 19）：
$$\tilde{\Gamma}^{\omega_c} = U^e + W^{\mathrm{ph}} + O\left(\frac{\omega_D}{E_F}, \frac{\omega_c^2}{\omega_p^2}\right)$$

### 第四步：投影到费米面——频率空间方程

由于 $W^{\mathrm{ph}}$ 和 $U^e$ 都是动量和频率的正则函数，可以将所有动量投影到费米面上。对垂直于费米面的动量分量积分后，得到仅含频率的下折叠 BSE（方程 20）：

$$\Lambda_\omega = \eta_\omega + \pi T \sum_{|\omega'| < \omega_c} (\lambda_{\omega\omega'} - \mu_{\omega_c}) \frac{z_{\omega'}^{\mathrm{ph}}}{|\omega'|} \Lambda_{\omega'}$$

修正项正比于三个小参数之一：$\omega_D/E_F$、$\omega_c^2/\omega_p^2$ 或 $T/\omega_c$。

![[4_2.jpg]]
*Fig. 3 | 动量空间中反常顶点 $\Lambda(k, -k; q=0)$ 的自洽 Bethe-Salpeter 方程。核由纯电子的粒子-粒子不可约四点顶点 $\tilde{\Gamma}^e$ 和声子介导相互作用 $W^{\mathrm{ph}}$ 组成；根据 Migdal 定理，高阶顶点修正很小。*

### 关键量的微观定义

在下折叠 BSE 中，各物理量均有严格定义：

- **电子-声子耦合** $\lambda_{\omega\omega'}$：声子介导相互作用 $W^{\mathrm{ph}}$ 的费米面平均，由准粒子权重 $z^e$ 加权：
$$\lambda_{\omega\omega'} \equiv -(z^e)^2 N_F^* \langle W_{k_F - k_F', \omega-\omega'}^{\mathrm{ph}} \rangle_{k_F k_F'}$$

- **库仑赝势** $\mu_{\omega_c}$：纯电子的粒子-粒子不可约四点顶点 $\tilde{\Gamma}^e$ 投影到费米面上，高能自由度在截断 $\omega_c$ 以上被积出。尽管微观层面上库仑相互作用具有奇异的动量依赖性，投影后的有效电子-电子相互作用退化为一个赝势常数。

- **电子-声子准粒子权重** $z_\omega^{\mathrm{ph}}$：完全由 $\lambda$ 决定（方程 21）：
$$\frac{1}{z_\omega^{\mathrm{ph}}} = 1 + \frac{\pi T}{\omega} \sum_{\omega'} \frac{\omega'}{|\omega'|} \lambda_{\omega\omega'} + O\left(\frac{\omega_D}{E_F}, \frac{\omega_c^2}{\omega_p^2}\right)$$

## 评审

- **Prior**: 依赖前提推断
- **Justification**: 推导建立在三个独立的小参数之上（$\omega_D/E_F$、$\omega_c^2/\omega_p^2$、$T/\omega_c$），每一个在简单金属中都有很好的数值验证。配对传播子分解是精确的数学恒等式，不涉及近似。
- **Belief**: 0.328（受制于前提的联合概率）

## 支撑

- $\to$ [[downfolded_bse_toy_model|#44 下折叠 BSE 玩具模型结果]] via noisy_and
- $\to$ [[downfolded_me_equation|#45 下折叠 ME 能隙方程]] via deduction
- $\to$ [[lambda_microscopic_definition|#46 $\lambda$ 的微观定义]] via deduction
- $\to$ [[mu_microscopic_definition|#47 $\mu$ 的微观定义]] via deduction
- $\to$ [[ab_initio_workflow|#54 第一性原理 $T_c$ 预测工作流]] via deduction

## 意义

这一结果将完整的动量-频率 BSE 严格约化为仅含频率的一维方程，使得理论上不可处理的问题变得计算上可行。更重要的是，它为传统 Migdal-Eliashberg 方程中的 $\mu^*$ 和 $\lambda$ 赋予了严格的微观定义，消除了唯象输入的必要性。这是从 BCS/Eliashberg 半唯象框架到受控第一性原理理论的关键一步。

## 注意事项

1. 下折叠方案的有效性条件：$\omega_D/E_F \ll 1$（绝热条件）、$\omega_c/\omega_p \ll 1$（等离子体频率远大于截断）。
2. 对于强非绝热系统（如高压氢化物，$\omega_D/E_F \sim 0.1$）以及二维系统（等离子体模式无能隙），下折叠近似可能失效。
3. 在极端密度（$r_s \ll 1$，如白矮星/黑矮星内部），等离子体频率软化可能破坏能标分离。

## 所属模块
[[s3_downfolding]]
