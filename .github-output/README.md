# superconductivity-electron-liquids-gaia

Gaia knowledge package: Superconductivity in Electron Liquids (arXiv:2512.19382)

<!-- badges:start -->
<!-- badges:end -->

## Overview

> **Reasoning graph information gain: `4.0 bits`**
>
> <sub>Total mutual information between leaf premises and exported conclusions — measures how much the reasoning structure reduces uncertainty about the results.</sub>

```mermaid
---
config:
  flowchart:
    rankSpacing: 80
    nodeSpacing: 30
---
graph TB
    adiabatic_approx["Adiabatic Approximation\n(0.95 → 0.90)"]:::premise
    tc_al_experimental["Tc(Al) Experimental\n(0.99 → 1.00)"]:::premise
    tc_li_experimental["Tc(Li) Experimental\n(0.85 → 1.00)"]:::premise
    tc_zn_experimental["Tc(Zn) Experimental\n(0.99 → 1.00)"]:::premise
    tc_al_phenomenological["Tc(Al) Phenomenological Prediction\n(0.35 → 0.40)"]:::premise
    tc_li_phenomenological["Tc(Li) Phenomenological Prediction\n(0.10 → 0.13)"]:::premise
    tc_zn_phenomenological["Tc(Zn) Phenomenological Prediction\n(0.35 → 0.40)"]:::premise
    cross_term_suppressed["Cross-Channel Terms Suppressed\n(0.90 → 0.69)"]:::premise
    downfolded_bse["★ Downfolded BSE\n(0.50 → 0.76)"]:::exported
    vdiagmc_method["vDiagMC Method\n(0.90 → 0.83)"]:::premise
    homotopic_expansion["Homotopic Expansion\n(0.88 → 0.79)"]:::premise
    mu_vdiagmc_values["★ mu from vDiagMC: Numerical Values\n(0.50 → 0.50)"]:::exported
    ward_identity["Ward Identity at q->0\n(0.98 → 1.00)"]:::premise
    gamma3_vdiagmc["vDiagMC Computation of Gamma_3\n(0.88 → 1.00)"]:::premise
    quasiparticle_mass_near_unity["Quasiparticle Mass Near Unity\n(0.92 → 0.86)"]:::premise
    dfpt_reliable_for_simple_metals["★ DFPT Reliable for Simple Metals\n(0.50 → 0.86)"]:::exported
    ueg_pseudopotential_parameterization["UEG mu#ast; Parameterization and Mapping\n(0.85 → 0.83)"]:::premise
    ab_initio_workflow["★ Ab Initio Tc Prediction Workflow\n(0.50 → 0.99)"]:::exported
    tc_al_predicted["★ Tc(Al) Ab Initio Prediction\n(0.50 → 0.93)"]:::exported
    tc_zn_predicted["★ Tc(Zn) Ab Initio Prediction\n(0.50 → 0.93)"]:::exported
    tc_li_predicted["★ Tc(Li) Ab Initio Prediction\n(0.50 → 0.96)"]:::exported
    al_pressure_transition["★ Al Pressure-Tc Transition\n(0.50 → 0.79)"]:::exported
    tc_mg_na_near_qpt["★ Na and Mg Near Quantum Phase Transition\n(0.50 → 0.79)"]:::exported
    rpa_vs_vdiagmc["rpa_vs_vdiagmc\n(0.50 → 1.00)"]:::premise
    rpa_predicts_attractive_mu["RPA Predicts Attractive mu#ast;\n(0.50 → 0.25)"]:::premise
    strat_0(["infer\n0.60 bits"]):::weak
    ab_initio_workflow --> strat_0
    strat_0 --> al_pressure_transition
    strat_1(["infer\n0.67 bits"]):::weak
    ab_initio_workflow --> strat_1
    tc_al_experimental --> strat_1
    tc_al_phenomenological --> strat_1
    strat_1 --> tc_al_predicted
    strat_2(["infer\n0.60 bits"]):::weak
    ab_initio_workflow --> strat_2
    tc_li_experimental --> strat_2
    tc_li_phenomenological --> strat_2
    strat_2 --> tc_li_predicted
    strat_3(["infer\n0.60 bits"]):::weak
    ab_initio_workflow --> strat_3
    strat_3 --> tc_mg_na_near_qpt
    strat_4(["infer\n0.67 bits"]):::weak
    ab_initio_workflow --> strat_4
    tc_zn_experimental --> strat_4
    tc_zn_phenomenological --> strat_4
    strat_4 --> tc_zn_predicted
    strat_5(["infer\n0.01 bits"]):::weak
    adiabatic_approx --> strat_5
    cross_term_suppressed --> strat_5
    strat_5 --> downfolded_bse
    strat_6(["infer\n0.10 bits"]):::weak
    dfpt_reliable_for_simple_metals --> strat_6
    downfolded_bse --> strat_6
    mu_vdiagmc_values --> strat_6
    ueg_pseudopotential_parameterization --> strat_6
    strat_6 --> ab_initio_workflow
    strat_7(["infer\n0.00 bits"]):::weak
    downfolded_bse --> strat_7
    gamma3_vdiagmc --> strat_7
    quasiparticle_mass_near_unity --> strat_7
    ward_identity --> strat_7
    strat_7 --> dfpt_reliable_for_simple_metals
    strat_8(["infer\n0.74 bits"]):::weak
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
| ab_initio_workflow | The complete ab initio workflow for predicting $T_c$ of simple metals: (1) co... | 0.50 | 0.99 |
| al_pressure_transition | Under hydrostatic pressure, the ab initio framework predicts that aluminum's ... | 0.50 | 0.79 |
| dfpt_reliable_for_simple_metals | For simple metals, the DFPT calculation of the electron-phonon coupling const... | 0.50 | 0.86 |
| downfolded_bse | The frequency-only downfolded Bethe-Salpeter equation: the full momentum-freq... | 0.50 | 0.76 |
| mu_vdiagmc_values | vDiagMC calculations of the UEG four-point vertex yield the Coulomb pseudopot... | 0.50 | 0.50 |
| tc_al_predicted | The ab initio predicted superconducting transition temperature of aluminum is... | 0.50 | 0.93 |
| tc_li_predicted | The ab initio predicted superconducting transition temperature of lithium (9R... | 0.50 | 0.96 |
| tc_mg_na_near_qpt | The ab initio framework predicts that sodium and magnesium have extremely low... | 0.50 | 0.79 |
| tc_zn_predicted | The ab initio predicted superconducting transition temperature of zinc is $T_... | 0.50 | 0.93 |

<!-- content:start -->
<!-- content:end -->
