# superconductivity-electron-liquids-gaia

Gaia knowledge package: Superconductivity in Electron Liquids (arXiv:2512.19382)

<!-- badges:start -->
<!-- badges:end -->

## Overview

```mermaid
---
config:
  flowchart:
    rankSpacing: 80
    nodeSpacing: 30
---
graph TB
    adiabatic_approx["Adiabatic Approximation\n(0.95 → 0.96)"]:::premise
    cross_term_suppressed["Cross-Channel Terms Suppressed\n(0.90 → 0.93)"]:::premise
    downfolded_bse["★ Downfolded BSE\n(0.50 → 0.96)"]:::exported
    vdiagmc_method["vDiagMC Method\n(0.90 → 0.87)"]:::premise
    homotopic_expansion["Homotopic Expansion\n(0.88 → 0.84)"]:::premise
    mu_vdiagmc_values["★ mu from vDiagMC: Numerical Values\n(0.50 → 0.75)"]:::exported
    ward_identity["Ward Identity at q->0\n(0.98 → 0.98)"]:::premise
    gamma3_vdiagmc["vDiagMC Computation of Gamma_3\n(0.88 → 0.88)"]:::premise
    quasiparticle_mass_near_unity["Quasiparticle Mass Near Unity\n(0.92 → 0.92)"]:::premise
    gamma3_interpolation_test_valid["Gamma_3 Interpolation Test Valid\n(0.90 → 0.90)"]:::premise
    gamma3_evidence_independent["Gamma_3 Evidence Independence\n(0.93 → 0.93)"]:::premise
    dfpt_reliable_for_simple_metals["★ DFPT Reliable for Simple Metals\n(0.50 → 0.87)"]:::exported
    ueg_pseudopotential_parameterization["UEG mu#ast; Parameterization and Mapping\n(0.85 → 0.85)"]:::premise
    ab_initio_workflow["★ Ab Initio Tc Prediction Workflow\n(0.50 → 0.80)"]:::exported
    tc_al_predicted["★ Tc(Al) Ab Initio Prediction\n(0.50 → 0.84)"]:::exported
    tc_zn_predicted["★ Tc(Zn) Ab Initio Prediction\n(0.50 → 0.84)"]:::exported
    tc_li_predicted["★ Tc(Li) Ab Initio Prediction\n(0.50 → 0.82)"]:::exported
    al_pressure_transition["★ Al Pressure-Tc Transition\n(0.50 → 0.82)"]:::exported
    tc_mg_na_near_qpt["★ Na and Mg Near Quantum Phase Transition\n(0.50 → 0.82)"]:::exported
    rpa_vs_vdiagmc["rpa_vs_vdiagmc\n(0.95 → 1.00)"]:::premise
    rpa_predicts_attractive_mu["RPA Predicts Attractive mu#ast;\n(0.50 → 0.13)"]:::premise
    strat_0(["infer"]):::weak
    ab_initio_workflow --> strat_0
    strat_0 --> al_pressure_transition
    strat_1(["infer"]):::weak
    ab_initio_workflow --> strat_1
    strat_1 --> tc_al_predicted
    strat_2(["infer"]):::weak
    ab_initio_workflow --> strat_2
    strat_2 --> tc_li_predicted
    strat_3(["infer"]):::weak
    ab_initio_workflow --> strat_3
    strat_3 --> tc_mg_na_near_qpt
    strat_4(["infer"]):::weak
    ab_initio_workflow --> strat_4
    strat_4 --> tc_zn_predicted
    strat_5(["infer"]):::weak
    adiabatic_approx --> strat_5
    cross_term_suppressed --> strat_5
    strat_5 --> downfolded_bse
    strat_6(["infer"]):::weak
    dfpt_reliable_for_simple_metals --> strat_6
    downfolded_bse --> strat_6
    mu_vdiagmc_values --> strat_6
    ueg_pseudopotential_parameterization --> strat_6
    strat_6 --> ab_initio_workflow
    strat_7(["infer"]):::weak
    downfolded_bse --> strat_7
    gamma3_evidence_independent --> strat_7
    gamma3_interpolation_test_valid --> strat_7
    gamma3_vdiagmc --> strat_7
    quasiparticle_mass_near_unity --> strat_7
    ward_identity --> strat_7
    strat_7 --> dfpt_reliable_for_simple_metals
    strat_8(["infer"]):::weak
    homotopic_expansion --> strat_8
    vdiagmc_method --> strat_8
    strat_8 --> mu_vdiagmc_values
    oper_0{{"⊗"}}:::contra
    rpa_predicts_attractive_mu --- oper_0
    mu_vdiagmc_values --- oper_0
    oper_0 --- rpa_vs_vdiagmc

    classDef premise fill:#ddeeff,stroke:#4488bb,color:#333
    classDef exported fill:#d4edda,stroke:#28a745,stroke-width:2px,color:#333
    classDef weak fill:#fff9c4,stroke:#f9a825,stroke-dasharray: 5 5,color:#333
    classDef contra fill:#ffebee,stroke:#c62828,color:#333
```

## Conclusions

| Label | Content | Prior | Belief |
|-------|---------|-------|--------|
| ab_initio_workflow | The complete ab initio workflow for predicting $T_c$ of simple metals: (1) co... | 0.50 | 0.80 |
| al_pressure_transition | Under hydrostatic pressure, the ab initio framework predicts that aluminum's ... | 0.50 | 0.82 |
| dfpt_reliable_for_simple_metals | For simple metals, the DFPT calculation of the electron-phonon coupling const... | 0.50 | 0.87 |
| downfolded_bse | The frequency-only downfolded Bethe-Salpeter equation: the full momentum-freq... | 0.50 | 0.96 |
| mu_vdiagmc_values | vDiagMC calculations of the UEG four-point vertex yield the Coulomb pseudopot... | 0.50 | 0.75 |
| tc_al_predicted | The ab initio EFT predicted superconducting transition temperature of aluminu... | 0.50 | 0.84 |
| tc_li_predicted | The ab initio EFT predicted superconducting transition temperature of lithium... | 0.50 | 0.82 |
| tc_mg_na_near_qpt | The ab initio framework predicts that sodium and magnesium have extremely low... | 0.50 | 0.82 |
| tc_zn_predicted | The ab initio EFT predicted superconducting transition temperature of zinc (Z... | 0.50 | 0.84 |

<!-- content:start -->
<!-- content:end -->
