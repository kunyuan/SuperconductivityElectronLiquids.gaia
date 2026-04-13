# Narrative Outline

Auto-generated from the coarse reasoning graph. Sections are grouped by connectivity (high cohesion, low coupling) and ordered by topological layer. Use this as the backbone for writing narrative summaries.

## RPA Predicts Attractive mu*

1. **RPA Predicts Attractive mu*** (prior: 0.50 → belief: 0.20)
   - → supports: rpa_vs_vdiagmc

## Adiabatic Approximation

2. **Cross-Channel Terms Suppressed** (prior: 0.50 → belief: 0.41)
   - → supports: downfolded_bse

3. **Adiabatic Approximation** (prior: 0.50 → belief: 0.68)
   - → supports: downfolded_bse

## vDiagMC Method

4. **Homotopic Expansion** (prior: 0.50 → belief: 0.84)
   - → supports: mu_vdiagmc_values

5. **vDiagMC Method** (prior: 0.50 → belief: 0.86)
   - → supports: mu_vdiagmc_values

## UEG mu* Parameterization and Mapping

6. **UEG mu* Parameterization and Mapping** (prior: 0.50 → belief: 0.86)
   - → supports: ab_initio_workflow

## Ward Identity at q->0

7. **Quasiparticle Mass Near Unity** (prior: 0.50 → belief: 0.87)
   - → supports: dfpt_reliable_for_simple_metals

8. **vDiagMC Computation of Gamma_3** (prior: 0.50 → belief: 0.98)
   - → supports: dfpt_reliable_for_simple_metals

9. **Ward Identity at q->0** (prior: 0.50 → belief: 0.99)
   - → supports: dfpt_reliable_for_simple_metals

## mu from vDiagMC: Numerical Values

10. **Downfolded BSE ★** (prior: 0.50 → belief: 0.18)
   - ← infer(adiabatic_approx, cross_term_suppressed) [0.16 bits]
   - → supports: ab_initio_workflow, dfpt_reliable_for_simple_metals

11. **mu from vDiagMC: Numerical Values ★** (prior: 0.50 → belief: 0.60)
   - ← infer(homotopic_expansion, vdiagmc_method) [0.55 bits]
   - → supports: ab_initio_workflow, rpa_vs_vdiagmc

## DFPT Reliable for Simple Metals

12. **DFPT Reliable for Simple Metals ★** (prior: 0.50 → belief: 0.78)
   - ← infer(downfolded_bse, gamma3_vdiagmc, quasiparticle_mass_near_unity, ward_identity) [0.10 bits]
   - → supports: ab_initio_workflow

## rpa_vs_vdiagmc

13. **rpa_vs_vdiagmc** (prior: 1.00 → belief: 1.00)

## Ab Initio Tc Prediction Workflow

14. **Ab Initio Tc Prediction Workflow ★** (prior: 0.50 → belief: 1.00)
   - ← infer(dfpt_reliable_for_simple_metals, downfolded_bse, mu_vdiagmc_values, ueg_pseudopotential_parameterization) [0.04 bits]
   - → supports: al_pressure_transition, tc_al_predicted, tc_li_predicted, tc_mg_na_near_qpt, tc_zn_predicted

## Tc(Al) Ab Initio Prediction

15. **Tc(Li) Ab Initio Prediction ★** (prior: 0.50 → belief: 0.25)
   - ← infer(ab_initio_workflow) [0.60 bits]

16. **Al Pressure-Tc Transition ★** (prior: 0.50 → belief: 0.80)
   - ← infer(ab_initio_workflow) [0.60 bits]

17. **Na and Mg Near Quantum Phase Transition ★** (prior: 0.50 → belief: 0.80)
   - ← infer(ab_initio_workflow) [0.60 bits]

18. **Tc(Zn) Ab Initio Prediction ★** (prior: 0.50 → belief: 0.99)
   - ← infer(ab_initio_workflow) [0.67 bits]

19. **Tc(Al) Ab Initio Prediction ★** (prior: 0.50 → belief: 0.99)
   - ← infer(ab_initio_workflow) [0.67 bits]
