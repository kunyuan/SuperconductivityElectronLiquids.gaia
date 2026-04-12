---
type: claim
label: tc_al_predicted
aliases: [tc_al_predicted]
claim_number: 55
qid: "github:superconductivity_electron_liquids::tc_al_predicted"
module: s6_superconductors
exported: true
prior: null
belief: 0.9016568687862857
strategy_type: noisy_and
premise_count: 1
tags: [claim, s6-superconductors]
---

# #55 铝的第一性原理 $T_c$ 预测 (Tc(Al) Ab Initio Prediction)

第一性原理预测的铝超导转变温度为 $T_c^{\mathrm{EFT}} = 0.96$ K，与实验值 $T_c^{\mathrm{exp}} = 1.2$ K 吻合良好。第一性原理的 $\mu^*(\mathrm{Al}) = 0.13$ 由 vDiagMC 在 $r_s = 2.07$（带质量 $m_b = 1.05$）处的 $\mu_{E_F}$ 经 BTS 重整化得到。

## 背景

铝是超导电子学的基础材料，广泛用于过渡边传感器和超导量子比特。实验 $T_c = 1.2$ K 是精确测量的值。然而，使用标准 $\mu^* = 0.1$ 的 McMillan 公式给出 $T_c \approx 1.9$ K，高估了 58%。这一偏差虽然不如锂那样戏剧性，但对于需要精确控制能隙和热噪声的量子器件设计而言仍然是显著的。

**铝的材料参数**（[[aluminum_parameters|#29]]）：FCC 晶体结构，$r_s = 2.07$，$m_b = 1.05$，DFPT 电子-声子耦合 $\lambda = 0.44$，对数平均声子频率 $\omega_{\mathrm{log}} = 320$ K，费米温度 $T_F = 1.3 \times 10^5$ K。

## 推导

**策略**: noisy_and

**前提**:
- [[ab_initio_workflow|#54 第一性原理 $T_c$ 预测工作流]]

### 第一步：确定 $\mu^*$

将 vDiagMC 的 UEG 参数化应用于铝：
- 从 DFT 计算确定传导电子密度对应的 $r_s = 2.07$
- 从 $\Gamma$ 点能带色散曲率提取带质量 $m_b = 1.05$
- 重标 $r_s \to m_b \cdot r_s \approx 2.17$
- 在 vDiagMC 预算结果中插值，得到 $\mu_{E_F}$
- 通过 BTS 关系 $\mu^* = \mu_{E_F}/(1 + \mu_{E_F} \ln(E_F/\omega_D))$ 降标到 Debye 频率
- 得到 $\mu^*(\mathrm{Al}) = 0.13$

注意 $\mu^* = 0.13$ 高于标准猜测值 0.1，这正确地增强了库仑排斥，降低了预测的 $T_c$。

### 第二步：DFPT 计算 $\lambda$

使用 Quantum ESPRESSO 和 EPW 包：
- ONCV 赝势 + PBE 泛函
- SCF 计算：能量截断 90 Ry，动量网格 $24 \times 24 \times 24$
- DFPT 声子计算：粗 $q$ 网格 $6 \times 6 \times 6$
- Wannier 函数插值到细 $k/q$ 网格 $60 \times 60 \times 60$
- 得到 $\lambda = 0.44$，$\omega_{\mathrm{log}} = 320$ K

### 第三步：求解下折叠 BSE

将 $\mu^* = 0.13$ 和 $\lambda = 0.44$ 代入下折叠 Eliashberg 方程，使用前驱 Cooper 流方法在正常态计算反常顶点并外推：

$$T_c^{\mathrm{EFT}} = 0.96 \text{ K}$$

![[14_0.jpg]]
*Fig. 10 | 铝超导临界温度的压力依赖性。方块为理论结果；线是眼导线。来自 Levy 等人和 Gubser 等人的实验数据分别以菱形和圆形标记绘出。EFT 结果在常压至 6 GPa 范围内准确捕获了实验趋势。*

### 与实验和唯象预测的比较

| 方法 | $\mu^*$ | $T_c$ (K) | 偏差 |
|------|---------|-----------|------|
| 实验 | — | 1.2 | — |
| EFT (本工作) | 0.13 | 0.96 | -20% |
| McMillan ($\mu^*=0.1$) | 0.1 | 1.9 | +58% |

第一性原理方法显著改善了预测精度。偏差从 58% 降至 20%，且方向正确（EFT 的 $\mu^*$ 大于经验值，降低了 $T_c$）。

## 评审

- **Prior**: 依赖前提推断
- **Justification**: 材料特定的应用；$r_s = 2.07$ 在 vDiagMC 验证范围内。
- **Belief**: 0.902

## 意义

铝的 $T_c$ 预测验证了整个第一性原理框架在"标准"简单金属上的定量精度。20% 的偏差主要来源于 UEG 到实际材料的映射中的近似（忽略晶格势的非球对称效应）。

## 注意事项

1. 计算假设铝的费米面近似球对称——铝实际上是多价金属，费米面跨多个布里渊区，但在扩展区方案中保持近似旋转对称。
2. 压力依赖计算使用从文献拟合的状态方程确定晶格常数。

## 所属模块
[[s6_superconductors]]
