# superconductivity-electron-liquids-gaia

Gaia knowledge package: Superconductivity in Electron Liquids (arXiv:2512.19382)

[![Interactive Paper](https://img.shields.io/badge/📖_Interactive_Paper-GitHub_Pages-blue)](https://kunyuan.github.io/SuperconductivityElectronLiquids.gaia/) [![Knowledge Reference](https://img.shields.io/badge/📚_Reference-Wiki-green)](https://github.com/kunyuan/SuperconductivityElectronLiquids.gaia/wiki)

## Overview

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
    downfolded_bse["★ Downfolded BSE\n(→ 0.76)"]:::exported
    vdiagmc_method["vDiagMC Method\n(0.90 → 0.83)"]:::premise
    homotopic_expansion["Homotopic Expansion\n(0.88 → 0.79)"]:::premise
    mu_vdiagmc_values["★ mu from vDiagMC: Numerical Values\n(→ 0.50)"]:::exported
    ward_identity["Ward Identity at q->0\n(0.98 → 1.00)"]:::premise
    gamma3_vdiagmc["vDiagMC Computation of Gamma_3\n(0.88 → 1.00)"]:::premise
    quasiparticle_mass_near_unity["Quasiparticle Mass Near Unity\n(0.92 → 0.86)"]:::premise
    dfpt_reliable_for_simple_metals["★ DFPT Reliable for Simple Metals\n(→ 0.86)"]:::exported
    ueg_pseudopotential_parameterization["UEG mu#ast; Parameterization and Mapping\n(0.85 → 0.83)"]:::premise
    ab_initio_workflow["★ Ab Initio Tc Prediction Workflow\n(→ 0.99)"]:::exported
    tc_al_predicted["★ Tc(Al) Ab Initio Prediction\n(→ 0.93)"]:::exported
    tc_zn_predicted["★ Tc(Zn) Ab Initio Prediction\n(→ 0.93)"]:::exported
    tc_li_predicted["★ Tc(Li) Ab Initio Prediction\n(→ 0.96)"]:::exported
    al_pressure_transition["★ Al Pressure-Tc Transition\n(→ 0.79)"]:::exported
    tc_mg_na_near_qpt["★ Na and Mg Near Quantum Phase Transition\n(→ 0.79)"]:::exported
    ab_initio_workflow --> al_pressure_transition
    ab_initio_workflow --> tc_al_predicted
    tc_al_experimental --> tc_al_predicted
    tc_al_phenomenological --> tc_al_predicted
    ab_initio_workflow --> tc_li_predicted
    tc_li_experimental --> tc_li_predicted
    tc_li_phenomenological --> tc_li_predicted
    ab_initio_workflow --> tc_mg_na_near_qpt
    ab_initio_workflow --> tc_zn_predicted
    tc_zn_experimental --> tc_zn_predicted
    tc_zn_phenomenological --> tc_zn_predicted
    adiabatic_approx --> downfolded_bse
    cross_term_suppressed --> downfolded_bse
    dfpt_reliable_for_simple_metals --> ab_initio_workflow
    downfolded_bse --> ab_initio_workflow
    mu_vdiagmc_values --> ab_initio_workflow
    ueg_pseudopotential_parameterization --> ab_initio_workflow
    downfolded_bse --> dfpt_reliable_for_simple_metals
    gamma3_vdiagmc --> dfpt_reliable_for_simple_metals
    quasiparticle_mass_near_unity --> dfpt_reliable_for_simple_metals
    ward_identity --> dfpt_reliable_for_simple_metals
    homotopic_expansion --> mu_vdiagmc_values
    vdiagmc_method --> mu_vdiagmc_values

    classDef premise fill:#ddeeff,stroke:#4488bb,color:#333
    classDef exported fill:#d4edda,stroke:#28a745,stroke-width:2px,color:#333
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
