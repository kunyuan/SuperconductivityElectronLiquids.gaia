---
type: claim
label: quasiparticle_mass_near_unity
aliases: [quasiparticle_mass_near_unity]
claim_number: 28
qid: "github:superconductivity_electron_liquids::quasiparticle_mass_near_unity"
module: s5_eph_coupling
exported: false
prior: 0.92
belief: 0.8800603748500563
strategy_type: null
premise_count: 0
tags: [claim, s5-eph-coupling]
---

# #28 准粒子有效质量接近 1

> 对于金属密度（$r_s \in [2, 4]$）下的简单金属，准粒子有效质量比 $m^*/m \approx 1$（偏差小于 5--10%）。这一接近 1 的质量比意味着准粒子重整化因子 $z^e \approx 1/(1 + \lambda_e)$ 主要反映频率依赖的自能而非动量依赖的质量增强，从而简化了微观与 DFPT 层面电子-声子耦合之间的映射。

## 背景

在将 EFT 电子-声子耦合 $\lambda_{\mathrm{EFT}}$ 与 DFPT 计算的 $\lambda_{\mathrm{DFPT}}$ 进行对比时，两者的关键差异在于态密度：EFT 使用准粒子态密度 $N_F^* = N_F^{(0)} \cdot m^*/m$，而 DFPT 使用能带态密度 $N_F^{(0)}$。如果 $m^*/m$ 显著偏离 1，两种方法给出的 $\lambda$ 会有不可忽略的差异。高精度 QMC 和 DiagMC 计算表明，对于 UEG 在 $r_s \leq 5$ 范围内，$m^*/m$ 的偏差在亚百分比水平，因此 $N_F^* \approx N_F^{(0)}$，尽管电子关联很强。这一结果为简单金属中使用 DFPT 计算 $\lambda$ 的可靠性提供了关键支撑。

## 来源

- **计算方法**：高精度 QMC（量子蒙特卡罗）和 DiagMC（图解蒙特卡罗）计算 UEG 准粒子色散关系。
- **精度**：$m^*/m - 1 < 1\%$，对 $r_s \leq 5$ 成立。
- **物理理解**：在 Coulomb 体系中，自能的实部（决定 $m^*$）和虚部（决定 $z^e$）之间存在部分抵消，使得有效质量保持接近裸质量。

## 评审

**先验概率（Prior）**：0.92
**理由**：高精度 QMC/DiagMC 计算显示 $r_s \leq 5$ 时 $m^*/m$ 偏差小于 1%。
**信念度（Belief）**：0.88

## 支撑

- → [[dfpt_reliable_for_simple_metals|#53 DFPT 对简单金属可靠]] 经由演绎推理
- → [[dfpt_reliable_for_simple_metals|#53 DFPT 对简单金属可靠]] 经由推断

## 所属模块

[[s5_eph_coupling|电子-声子耦合]]
