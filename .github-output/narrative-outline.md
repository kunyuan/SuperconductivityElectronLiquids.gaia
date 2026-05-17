# Narrative Outline

Auto-generated from the coarse reasoning graph. Sections are grouped by connectivity (high cohesion, low coupling) and ordered by topological layer. Use this as the backbone for writing narrative summaries.

## Phenomenological ME Theory Limitations

1. **Phenomenological ME Theory Limitations** (prior: 0.50 → belief: 0.15)
   - → supports: tc_al_likelihood, tc_li_likelihood, tc_zn_likelihood

## RPA Predicts Attractive mu*

2. **RPA Predicts Attractive mu*** (prior: 0.50 → belief: 0.25)
   - → supports: rpa_vs_vdiagmc

## Li is Bulk Superconducting

3. **Li Resistive Anomaly Is Not Bulk SC** (prior: 0.50 → belief: 0.25)
   - → supports: ?

4. **Li is Bulk Superconducting** (prior: 0.50 → belief: 0.75)
   - → supports: tc_li_predicted, ?

## Ward Identity at q->0

5. **Homotopic Expansion** (prior: 0.50 → belief: 0.46)
   - → supports: mu_vdiagmc_values

6. **vDiagMC Method** (prior: 0.50 → belief: 0.53)
   - → supports: dfpt_reliable_for_simple_metals, mu_vdiagmc_values

7. **Quasiparticle Mass Near Unity** (prior: 0.92 → belief: 0.93)
   - → supports: dfpt_reliable_for_simple_metals

8. **Ward Identity at q->0** (prior: 0.98 → belief: 0.99)
   - → supports: dfpt_reliable_for_simple_metals

## UEG mu* Parameterization and Mapping

9. **UEG mu* Parameterization and Mapping** (prior: 0.50 → belief: 0.53)
   - → supports: ab_initio_workflow

## Adiabatic Approximation

10. **Cross-Channel Terms Suppressed** (prior: 0.50 → belief: 0.60)
   - → supports: downfolded_bse

11. **Adiabatic Approximation** (prior: 0.95 → belief: 0.96)
   - → supports: downfolded_bse

## Downfolded BSE

12. **mu from vDiagMC: Numerical Values ★** (prior: 0.50 → belief: 0.50)
   - ← infer(homotopic_expansion, vdiagmc_method) [0.19 bits]
   - → supports: ab_initio_workflow, rpa_vs_vdiagmc

13. **Downfolded BSE ★** (prior: 0.50 → belief: 0.89)
   - ← infer(adiabatic_approx, cross_term_suppressed) [0.22 bits]
   - → supports: ab_initio_workflow, dfpt_reliable_for_simple_metals

## 

14. **** (prior: 1.00 → belief: 1.00)

## DFPT Reliable for Simple Metals

15. **DFPT Reliable for Simple Metals ★** (prior: 0.50 → belief: 0.96)
   - ← infer(downfolded_bse, quasiparticle_mass_near_unity, vdiagmc_method, ward_identity) [0.11 bits]
   - → supports: ab_initio_workflow

## rpa_vs_vdiagmc

16. **rpa_vs_vdiagmc** (prior: 1.00 → belief: 1.00)

## Ab Initio Tc Prediction Workflow

17. **Ab Initio Tc Prediction Workflow ★** (prior: 0.50 → belief: 0.96)
   - ← infer(dfpt_reliable_for_simple_metals, downfolded_bse, mu_vdiagmc_values, ueg_pseudopotential_parameterization) [0.02 bits]
   - → supports: al_pressure_transition, tc_al_likelihood, tc_al_predicted, tc_li_likelihood, tc_li_predicted, tc_mg_na_near_qpt, tc_zn_likelihood, tc_zn_predicted

## tc_li_likelihood

18. **tc_li_predicted ★** (prior: 0.50 → belief: 0.86)
   - ← infer(ab_initio_workflow, li_is_superconducting) [0.20 bits]

19. **Na and Mg Near Quantum Phase Transition ★** (prior: 0.50 → belief: 0.98)
   - ← infer(ab_initio_workflow) [0.31 bits]

20. **Al Pressure-Tc Transition ★** (prior: 0.50 → belief: 0.98)
   - ← infer(ab_initio_workflow) [0.31 bits]

21. **tc_zn_predicted ★** (prior: 0.50 → belief: 0.98)
   - ← infer(ab_initio_workflow) [0.31 bits]

22. **tc_al_predicted ★** (prior: 0.50 → belief: 0.98)
   - ← infer(ab_initio_workflow) [0.31 bits]

23. **tc_al_likelihood ★** (prior: 1.00 → belief: 1.00)
   - ← infer(ab_initio_workflow, phenomenological_me_theory) [0.50 bits]

24. **tc_zn_likelihood ★** (prior: 1.00 → belief: 1.00)
   - ← infer(ab_initio_workflow, phenomenological_me_theory) [0.45 bits]

25. **tc_li_likelihood ★** (prior: 1.00 → belief: 1.00)
   - ← infer(ab_initio_workflow, phenomenological_me_theory) [0.26 bits]
