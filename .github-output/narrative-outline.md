# Narrative Outline

Auto-generated from the coarse reasoning graph. Sections are grouped by connectivity (high cohesion, low coupling) and ordered by topological layer. Use this as the backbone for writing narrative summaries.

## Tc(Li) Experimental

1. **Tc(Li) Phenomenological Prediction** (prior: 0.10 → belief: 0.13)
   - → supports: tc_li_predicted

2. **Tc(Li) Experimental** (prior: 0.85 → belief: 1.00)
   - → supports: tc_li_predicted

## RPA Predicts Attractive mu*

3. **RPA Predicts Attractive mu*** (prior: 0.50 → belief: 0.25)
   - → supports: rpa_vs_vdiagmc

## Tc(Zn) Experimental

4. **Tc(Zn) Phenomenological Prediction** (prior: 0.35 → belief: 0.40)
   - → supports: tc_zn_predicted

5. **Tc(Zn) Experimental** (prior: 0.99 → belief: 1.00)
   - → supports: tc_zn_predicted

## Tc(Al) Experimental

6. **Tc(Al) Phenomenological Prediction** (prior: 0.35 → belief: 0.40)
   - → supports: tc_al_predicted

7. **Tc(Al) Experimental** (prior: 0.99 → belief: 1.00)
   - → supports: tc_al_predicted

## Adiabatic Approximation

8. **Cross-Channel Terms Suppressed** (prior: 0.90 → belief: 0.69)
   - → supports: downfolded_bse

9. **Adiabatic Approximation** (prior: 0.95 → belief: 0.90)
   - → supports: downfolded_bse

## vDiagMC Method

10. **Homotopic Expansion** (prior: 0.88 → belief: 0.79)
   - → supports: mu_vdiagmc_values

11. **vDiagMC Method** (prior: 0.90 → belief: 0.83)
   - → supports: mu_vdiagmc_values

## UEG mu* Parameterization and Mapping

12. **UEG mu* Parameterization and Mapping** (prior: 0.85 → belief: 0.83)
   - → supports: ab_initio_workflow

## Ward Identity at q->0

13. **Quasiparticle Mass Near Unity** (prior: 0.92 → belief: 0.86)
   - → supports: dfpt_reliable_for_simple_metals

14. **vDiagMC Computation of Gamma_3** (prior: 0.88 → belief: 1.00)
   - → supports: dfpt_reliable_for_simple_metals

15. **Ward Identity at q->0** (prior: 0.98 → belief: 1.00)
   - → supports: dfpt_reliable_for_simple_metals

## Downfolded BSE

16. **mu from vDiagMC: Numerical Values ★** (prior: 0.50 → belief: 0.50)
   - ← infer(homotopic_expansion, vdiagmc_method) [0.74 bits]
   - → supports: ab_initio_workflow, rpa_vs_vdiagmc

17. **Downfolded BSE ★** (prior: 0.50 → belief: 0.76)
   - ← infer(adiabatic_approx, cross_term_suppressed) [0.01 bits]
   - → supports: ab_initio_workflow, dfpt_reliable_for_simple_metals

## DFPT Reliable for Simple Metals

18. **DFPT Reliable for Simple Metals ★** (prior: 0.50 → belief: 0.86)
   - ← infer(downfolded_bse, gamma3_vdiagmc, quasiparticle_mass_near_unity, ward_identity) [0.00 bits]
   - → supports: ab_initio_workflow

## rpa_vs_vdiagmc

19. **rpa_vs_vdiagmc** (prior: 0.50 → belief: 1.00)

## Ab Initio Tc Prediction Workflow

20. **Ab Initio Tc Prediction Workflow ★** (prior: 0.50 → belief: 0.99)
   - ← infer(dfpt_reliable_for_simple_metals, downfolded_bse, mu_vdiagmc_values, ueg_pseudopotential_parameterization) [0.10 bits]
   - → supports: al_pressure_transition, tc_al_predicted, tc_li_predicted, tc_mg_na_near_qpt, tc_zn_predicted

## Tc(Li) Ab Initio Prediction

21. **Na and Mg Near Quantum Phase Transition ★** (prior: 0.50 → belief: 0.79)
   - ← infer(ab_initio_workflow) [0.60 bits]

22. **Al Pressure-Tc Transition ★** (prior: 0.50 → belief: 0.79)
   - ← infer(ab_initio_workflow) [0.60 bits]

23. **Tc(Zn) Ab Initio Prediction ★** (prior: 0.50 → belief: 0.93)
   - ← infer(ab_initio_workflow, tc_zn_experimental, tc_zn_phenomenological) [0.67 bits]

24. **Tc(Al) Ab Initio Prediction ★** (prior: 0.50 → belief: 0.93)
   - ← infer(ab_initio_workflow, tc_al_experimental, tc_al_phenomenological) [0.67 bits]

25. **Tc(Li) Ab Initio Prediction ★** (prior: 0.50 → belief: 0.96)
   - ← infer(ab_initio_workflow, tc_li_experimental, tc_li_phenomenological) [0.60 bits]
