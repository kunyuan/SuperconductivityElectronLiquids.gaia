---
type: overview
tags: [overview]
---

# 电子液体中的超导性 — 推理图总览

**论文**：*Superconductivity in Electron Liquids: Precision Many-Body Treatment of Coulomb Interaction*
Xiansheng Cai, Tao Wang, Shuai Zhang, Tiantian Zhang, Andrew Millis, Boris V. Svistunov, Nikolay V. Prokof'ev, and Kun Chen (2026)

## 摘要

超导发现一个多世纪以来，常规金属中超导的理论仍不完整。虽然电子-声子耦合的关键作用已被理解，但 Coulomb 相互作用的理论可控第一性原理处理尚未建立。现有 ab initio 计算中广泛使用的下折叠近似基于将 Coulomb 相互作用唯象地替换为排斥赝势 $\mu^*$，而动态 Coulomb 相互作用对电子-声子耦合影响的模糊性也长期未解。

本文通过基于变分图解蒙特卡罗（vDiagMC）积掉高能电子自由度的有效场论方法解决了这些局限。将该理论应用于均匀电子气（UEG），建立了实施下折叠近似、定义赝势、并通过电子顶角函数表达动态 Coulomb 相互作用对电子-声子耦合影响的定量微观程序。

关键发现包括：(i) 裸赝势 $\mu_{E_F}$ 显著大于传统唯象估计（在 $r_s = 5$ 时大 3 倍）；(ii) DFPT 计算的 $\lambda$ 对简单金属高度可靠；(iii) 对 Al、Zn 的 $T_c$ 预测与实验精确吻合，锂的预测改善了数个数量级；(iv) 预测 Al 在 ~60 GPa 压力下发生超导-正常态转变，Na 和 Mg 接近类似量子临界点。

```mermaid
graph TD
    downfolded_bse["下折叠 BSE (0.50 → 0.33)"]:::exported
    bts_microscopic_equivalence["BTS 微观等价性 (0.50 → 1.00)"]:::derived
    mu_vdiagmc_values["vDiagMC mu 数值 (0.50 → 0.55)"]:::exported
    dfpt_reliable_for_simple_metals["DFPT 对简单金属可靠 (0.50 → 0.75)"]:::exported
    ab_initio_workflow["Ab initio Tc 预测工作流 (0.50 → 0.96)"]:::exported
    tc_al_predicted["Tc(Al) 预测 (0.50 → 0.90)"]:::exported
    tc_zn_predicted["Tc(Zn) 预测 (0.50 → 0.90)"]:::exported
    tc_li_predicted["Tc(Li) 预测 (0.50 → 0.90)"]:::exported
    al_pressure_transition["Al 压力-Tc 转变 (0.50 → 0.77)"]:::exported
    tc_mg_na_near_qpt["Na/Mg 近量子相变 (0.50 → 0.77)"]:::exported
    strat_20(["演绎"])
    downfolded_bse --> strat_20
    dfpt_reliable_for_simple_metals --> strat_20
    strat_20 --> ab_initio_workflow
    strat_21(["推断"]):::weak
    downfolded_bse --> strat_21
    mu_vdiagmc_values --> strat_21
    dfpt_reliable_for_simple_metals --> strat_21
    strat_21 --> ab_initio_workflow
    strat_22(["noisy_and"]):::weak
    ab_initio_workflow --> strat_22
    strat_22 --> tc_al_predicted
    strat_23(["noisy_and"]):::weak
    ab_initio_workflow --> strat_23
    strat_23 --> tc_zn_predicted
    strat_24(["noisy_and"]):::weak
    ab_initio_workflow --> strat_24
    strat_24 --> tc_li_predicted
    strat_25(["noisy_and"]):::weak
    ab_initio_workflow --> strat_25
    strat_25 --> al_pressure_transition
    strat_26(["noisy_and"]):::weak
    ab_initio_workflow --> strat_26
    strat_26 --> tc_mg_na_near_qpt
    oper_0{{"≡"}}
    mu_scale_independence["BTS 关系推论 (0.50 → 0.98)"]:::derived
    mu_scale_independence --- oper_0
    bts_renormalization["BTS 重整化关系 (0.95 → 0.98)"]:::premise
    bts_renormalization --- oper_0
    oper_0 --- bts_microscopic_equivalence
    oper_1{{"⊗"}}:::contra
    rpa_predicts_attractive_mu["RPA 预测吸引性 mu (0.50 → 0.23)"]:::premise
    rpa_predicts_attractive_mu --- oper_1
    mu_vdiagmc_values --- oper_1

    classDef setting fill:#f0f0f0,stroke:#999,color:#333
    classDef premise fill:#ddeeff,stroke:#4488bb,color:#333
    classDef derived fill:#ddffdd,stroke:#44bb44,color:#333
    classDef question fill:#fff3dd,stroke:#cc9944,color:#333
    classDef background fill:#f5f5f5,stroke:#bbb,stroke-dasharray: 5 5,color:#333
    classDef orphan fill:#fff,stroke:#ccc,stroke-dasharray: 5 5,color:#333
    classDef exported fill:#d4edda,stroke:#28a745,stroke-width:2px,color:#333
    classDef weak fill:#fff9c4,stroke:#f9a825,stroke-dasharray: 5 5,color:#333
    classDef contra fill:#ffebee,stroke:#c62828,color:#333
```
