# superconductivity-electron-liquids-gaia

Gaia knowledge package: Superconductivity in Electron Liquids (arXiv:2512.19382)

[![Interactive Paper](https://img.shields.io/badge/📖_Interactive_Paper-GitHub_Pages-blue)](https://kunyuan.github.io/SuperconductivityElectronLiquids.gaia/)
[![Knowledge Reference](https://img.shields.io/badge/📚_Reference-Wiki-green)](https://github.com/kunyuan/SuperconductivityElectronLiquids.gaia/wiki)

## Overview

```mermaid
graph TD
    downfolded_bse["Downfolded BSE ★ (0.50 → 0.76)"]:::exported
    mu_vdiagmc_values["mu from vDiagMC: Numerical Values ★ (0.50 → 0.50)"]:::exported
    dfpt_reliable_for_simple_metals["DFPT Reliable for Simple Metals ★ (0.50 → 0.86)"]:::exported
    ab_initio_workflow["Ab Initio Tc Prediction Workflow ★ (0.50 → 0.99)"]:::exported
    tc_al_predicted["Tc(Al) Ab Initio Prediction ★ (0.50 → 0.93)"]:::exported
    tc_zn_predicted["Tc(Zn) Ab Initio Prediction ★ (0.50 → 0.93)"]:::exported
    tc_li_predicted["Tc(Li) Ab Initio Prediction ★ (0.50 → 0.96)"]:::exported
    al_pressure_transition["Al Pressure-Tc Transition ★ (0.50 → 0.79)"]:::exported
    tc_mg_na_near_qpt["Na and Mg Near Quantum Phase Transition ★ (0.50 → 0.79)"]:::exported
    strat_20(["deduction"])
    downfolded_bse --> strat_20
    dfpt_reliable_for_simple_metals --> strat_20
    strat_20 --> ab_initio_workflow
    strat_21(["infer"]):::weak
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
    oper_1{{"⊗"}}:::contra
    rpa_predicts_attractive_mu["RPA Predicts Attractive mu#ast; (0.50 → 0.25)"]:::premise
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

## Conclusions

| Label | Content | Belief |
|-------|---------|--------|
| ab_initio_workflow | The complete ab initio workflow for predicting $T_c$ of simple metals: (1) co... | 0.99 |
| al_pressure_transition | Under hydrostatic pressure, the ab initio framework predicts that aluminum's ... | 0.79 |
| dfpt_reliable_for_simple_metals | For simple metals, the DFPT calculation of the electron-phonon coupling const... | 0.86 |
| downfolded_bse | The frequency-only downfolded Bethe-Salpeter equation: the full momentum-freq... | 0.76 |
| mu_vdiagmc_values | vDiagMC calculations of the UEG four-point vertex yield the Coulomb pseudopot... | 0.50 |
| tc_al_predicted | The ab initio predicted superconducting transition temperature of aluminum is... | 0.93 |
| tc_li_predicted | The ab initio predicted superconducting transition temperature of lithium is ... | 0.96 |
| tc_mg_na_near_qpt | The ab initio framework predicts that sodium and magnesium have extremely low... | 0.79 |
| tc_zn_predicted | The ab initio predicted superconducting transition temperature of zinc is $T_... | 0.93 |

<!-- content:start -->
<!-- content:end -->
