# Narrative Outline

Auto-generated from the coarse reasoning graph. Sections are grouped by connectivity (high cohesion, low coupling) and ordered by topological layer. Use this as the backbone for writing narrative summaries.

## RPA Predicts Attractive mu*

1. **RPA Predicts Attractive mu*** (prior: 0.50 → belief: 0.13)
   - → supports: rpa_vs_vdiagmc

## vDiagMC Method

2. **Homotopic Expansion** (prior: 0.88 → belief: 0.84)
   - → supports: mu_vdiagmc_values

3. **vDiagMC Method** (prior: 0.90 → belief: 0.87)
   - → supports: mu_vdiagmc_values

## UEG mu* Parameterization and Mapping

4. **UEG mu* Parameterization and Mapping** (prior: 0.85 → belief: 0.85)
   - → supports: ab_initio_workflow

## Ward Identity at q->0

5. **vDiagMC Computation of Gamma_3** (prior: 0.88 → belief: 0.88)
   - → supports: dfpt_reliable_for_simple_metals

6. **Gamma_3 Interpolation Test Valid** (prior: 0.90 → belief: 0.90)
   - → supports: dfpt_reliable_for_simple_metals

7. **Quasiparticle Mass Near Unity** (prior: 0.92 → belief: 0.92)
   - → supports: dfpt_reliable_for_simple_metals

8. **Gamma_3 Evidence Independence** (prior: 0.93 → belief: 0.93)
   - → supports: dfpt_reliable_for_simple_metals

9. **Ward Identity at q->0** (prior: 0.98 → belief: 0.98)
   - → supports: dfpt_reliable_for_simple_metals

## Adiabatic Approximation

10. **Cross-Channel Terms Suppressed** (prior: 0.90 → belief: 0.93)
   - → supports: downfolded_bse

11. **Adiabatic Approximation** (prior: 0.95 → belief: 0.96)
   - → supports: downfolded_bse

## Downfolded BSE

12. **mu from vDiagMC: Numerical Values ★** (prior: 0.50 → belief: 0.75)
   - ← infer(homotopic_expansion, vdiagmc_method)
   - → supports: ab_initio_workflow, rpa_vs_vdiagmc

13. **Downfolded BSE ★** (prior: 0.50 → belief: 0.96)
   - ← infer(adiabatic_approx, cross_term_suppressed)
   - → supports: ab_initio_workflow, dfpt_reliable_for_simple_metals

## DFPT Reliable for Simple Metals

14. **DFPT Reliable for Simple Metals ★** (prior: 0.50 → belief: 0.87)
   - ← infer(downfolded_bse, gamma3_evidence_independent, gamma3_interpolation_test_valid, gamma3_vdiagmc, quasiparticle_mass_near_unity, ward_identity)
   - → supports: ab_initio_workflow

## rpa_vs_vdiagmc

15. **rpa_vs_vdiagmc** (prior: 0.95 → belief: 1.00)

## Ab Initio Tc Prediction Workflow

16. **Ab Initio Tc Prediction Workflow ★** (prior: 0.50 → belief: 0.80)
   - ← infer(dfpt_reliable_for_simple_metals, downfolded_bse, mu_vdiagmc_values, ueg_pseudopotential_parameterization)
   - → supports: al_pressure_transition, tc_al_predicted, tc_li_predicted, tc_mg_na_near_qpt, tc_zn_predicted

## Tc(Zn) Ab Initio Prediction

17. **Al Pressure-Tc Transition ★** (prior: 0.50 → belief: 0.82)
   - ← infer(ab_initio_workflow)

18. **Na and Mg Near Quantum Phase Transition ★** (prior: 0.50 → belief: 0.82)
   - ← infer(ab_initio_workflow)

19. **Tc(Li) Ab Initio Prediction ★** (prior: 0.50 → belief: 0.82)
   - ← infer(ab_initio_workflow)

20. **Tc(Al) Ab Initio Prediction ★** (prior: 0.50 → belief: 0.84)
   - ← infer(ab_initio_workflow)

21. **Tc(Zn) Ab Initio Prediction ★** (prior: 0.50 → belief: 0.84)
   - ← infer(ab_initio_workflow)
