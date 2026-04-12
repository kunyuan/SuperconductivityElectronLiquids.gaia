---
type: claim
label: mu_vdiagmc_values
aliases: [mu_vdiagmc_values]
claim_number: 37
qid: "github:superconductivity_electron_liquids::mu_vdiagmc_values"
module: s4_pseudopotential
exported: true
prior: null
belief: 0.5516060192072931
strategy_type: noisy_and
premise_count: 2
tags: [claim, s4-pseudopotential]
---

# #37 vDiagMC 计算的库仑赝势数值 (mu from vDiagMC)

vDiagMC 对均匀电子气 (UEG) 四点顶点的计算给出了费米能标处的库仑赝势：$\mu_{E_F}(r_s)$ 在金属密度范围内为正且随 $r_s$ 单调递增，近似服从 $\mu_{E_F} \approx 0.27 r_s$。TABLE I 中的代表性数值包括 $r_s = 2$（类铝）时 $\mu_{E_F} = 0.53(2)$ 和 $r_s = 3$（类锂）时 $\mu_{E_F} = 0.77(5)$。结合 BTS 关系，在 Debye 能标处得到 $\mu^* \approx 0.12$--$0.18$，与经验范围一致，但现在是从第一性原理导出的，具有百分之几的受控误差。

## 背景

库仑赝势 $\mu^*$ 是决定超导转变温度的关键参数。传统方法中 $\mu^*$ 被当作可调参数（经验值在 0.1--0.2 之间），这对于亚开尔文超导体导致预测 $T_c$ 数个量级的不确定性。问题的核心难点在于计算 UEG 的粒子-粒子不可约四点顶点函数——这是凝聚态物理中的长期挑战：裸库仑相互作用的微扰论在 $r_s \gtrsim 1$ 时发散，而 RPA 或 GW 等部分重求和忽略了关键的顶点修正。

## 推导

**策略**: noisy_and

**前提**:
- [[vdiagmc_method|#23 vDiagMC 方法]]
- [[homotopic_expansion|#24 同伦展开]]

### 第一步：微观定义到计算量的化约

$\mu_{\omega_c}$ 的微观定义 ([[mu_microscopic_definition|#47]]) 将问题化约为对均匀电子气的四点顶点 $\tilde{\Gamma}^e$ 的费米面平均。具体地，在温度 $T$ 下，有效排斥可以通过费米面平均的双准粒子散射振幅定义（方程 24）：
$$\gamma_T \equiv z_e^2 N_F^* \langle \Gamma_F^e(k_F, \omega_0; k_F', \omega_0) \rangle_{k_F, k_F'}$$

其中 $\omega_0 = \pi T$ 是最小 Matsubara 频率。

### 第二步：vDiagMC 方法

变分介图蒙特卡洛 (vDiagMC) 方法 ([[vdiagmc_method|#23]]) 提供了受控的、系统可改进的方法来计算高阶 Feynman 介图级数：

1. **重整化展开**：将裸库仑势 $v(q) = 4\pi e^2/q^2$ 重写为 Yukawa 势 $v_R(q) = 4\pi e^2/(q^2 + \lambda_R)$ 加上反项级数。屏蔽参数 $\lambda_R$ 被优化以改善收敛性。
2. **计算图表示**：高阶 Feynman 图以计算图的压缩形式表示，利用 Dyson-Schwinger 和 Parquet 方程的结构，显著减少计算冗余。
3. **Taylor 模式自动微分**：实现重整化方案的计算成本从指数降为亚指数。
4. **蒙特卡洛采样**：使用 VEGAS 自适应算法和归一化流神经网络进行高维积分。

该方法计算自能和四点顶点函数，提取准粒子残余 $z^e(\xi)$、有效质量 $m_e^*(\xi)$ 和双电子散射振幅 $\Gamma^e(\xi)$ 作为展开参数 $\xi$ 的幂级数（方程 28）：
$$\gamma_T(\xi) \equiv [z^e(\xi)]^2 \frac{m_e^*(\xi)}{m} N_F \Gamma^e(\xi) \equiv \gamma_T^{(0)} + \gamma_T^{(1)}\xi + \gamma_T^{(2)}\xi^2 + \cdots$$

### 第三步：同伦展开解决收敛问题

在低温下，级数在物理值 $\xi = 1$ 处的收敛因 $N$ 阶项中 $(\ln T)^N$ 的缩放而变得困难——这源于介图展开中嵌套的粒子-粒子泡。同伦变换 ([[homotopic_expansion|#24]]) 提供了一个物理上有动机的重组（方程 30）：
$$\mu_{\omega_c}(\xi) \equiv \frac{\gamma_T(\xi)}{1 - \gamma_T(\xi) \ln(\omega_c/T)}$$

将其展开为 $\xi$ 的幂级数（方程 29）：
$$\mu_{\omega_c}(\xi) = \mu_{\omega_c}^{(0)} + \mu_{\omega_c}^{(1)}\xi + \mu_{\omega_c}^{(2)}\xi^2 + \cdots$$

得到与温度无关的系数。$\gamma_T$ 级数（左面板）在 $0.01 E_F$ 以下展现对数发散，而 $\mu_{\omega_c}$ 级数（右面板）快速收敛到 $T \to 0$ 的极限值。

### 第四步：数值结果

在计算最优截断 $\omega_c = 0.1 E_F$ 处计算 $\mu_{\omega_c}$，然后通过 BTS 关系（方程 25）$\mu_{\omega_c} = \mu_{\omega_c'} / (1 + \mu_{\omega_c'} \ln(\omega_c'/\omega_c))$ 重标到 $E_F$。TABLE I 的完整数值结果：

| $r_s$ | 1 | 2 | 3 | 4 | 5 | 6 |
|--------|---|---|---|---|---|---|
| $\mu_{0.1E_F}$ | 0.172(4) | 0.238(4) | 0.278(6) | 0.306(15) | 0.328(12) | 0.35(3) |
| $\mu_{E_F}$ | 0.28(1) | 0.53(2) | 0.77(5) | 1.0(2) | 1.3(2) | 1.8(8) |

括号中的数字表示末位数字的估计系统误差。

![[8_0.jpg]]
*Fig. 4 | 3D UEG 的无量纲"裸"库仑赝势 $\mu_{E_F}$ 随 $r_s$ 的变化，由 vDiagMC 数据通过反转 BTS 关系提取。实线是对 vDiagMC 数据的线性拟合。在 $r_s > 0.5$ 时，vDiagMC 结果与三种标准近似（静态 RPA、Morel-Anderson、动态 RPA）出现显著偏离。注意所有曲线在 $r_s \ll 1$ 时完全一致。*

### 与既有近似的比较

vDiagMC 的 $\mu_{E_F}$ 在 $r_s = 5$ 时比 Morel-Anderson 和静态 RPA 估计大三倍。与动态 RPA 的分歧更为深刻——后者预测 $r_s > 2$ 时 $\mu_{\omega_c} < 0$（净吸引），而 vDiagMC 给出单调递增的正值。这明确表明 RPA 近似在 $r_s > 0.5$ 时失控，这从静态 RPA 和动态 RPA 结果之间的剧烈差异即可预见。

## 评审

- **Prior**: 依赖前提推断
- **Justification**: vDiagMC 方法经过系统验证；同伦展开的对数发散消除是严格的；主要不确定性来自截断/重求和的系统误差。
- **Belief**: 0.552

## 支撑

- $\to$ [[mu_available_for_simple_metals|#41 简单金属的 $\mu^*$ 可用性]] via noisy_and
- $\to$ [[ab_initio_workflow|#54 第一性原理 $T_c$ 预测工作流]] via infer

## 意义

这些结果首次从第一性原理提供了金属密度范围内库仑赝势的受控计算，消除了 $\mu^*$ 作为可调参数的需要。$\mu_{E_F}$ 远大于传统估计这一发现，解释了为何使用经验 $\mu^* = 0.1$ 的唯象方法系统性地高估亚开尔文超导体的 $T_c$。

## 注意事项

1. 计算在 UEG 模型中进行；映射到实际材料需要通过材料特定的 $r_s$ 和带质量进行参数化。
2. 系统误差随 $r_s$ 增大（$r_s = 6$ 时误差已达约 50%），限制了在低密度金属中的精度。
3. 裸赝势 $\mu_{E_F}$ 还决定了正常费米液体态对均匀配对扰动的低温响应：$\chi_0 \propto z_e^2/(m^* \mu_{E_F})$。

## 所属模块
[[s4_pseudopotential]]
