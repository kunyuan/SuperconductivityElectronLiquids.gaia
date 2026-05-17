# Narrative Outline

Auto-generated from the coarse reasoning graph. Sections are grouped by connectivity (high cohesion, low coupling) and ordered by topological layer. Use this as the backbone for writing narrative summaries.

## Li is Bulk Superconducting

1. **Li Resistive Anomaly Is Not Bulk SC** (prior: 0.50 → belief: 0.25)
   - → supports: ?

2. **Li is Bulk Superconducting** (prior: 0.50 → belief: 0.75)
   - → supports: tc_li_predicted, ?

## RPA Predicts Attractive mu*

3. **RPA Predicts Attractive mu*** (prior: 0.50 → belief: 0.25)
   - → supports: rpa_vs_vdiagmc

## mu* as Phenomenological Parameter

4. **mu* as Phenomenological Parameter** (prior: 0.50 → belief: 0.31)
   - → supports: tc_al_likelihood, tc_li_likelihood, tc_zn_likelihood

## Ward Identity at q->0

5. **Homotopic Expansion** (prior: 0.50 → belief: 0.46)
   - → supports: mu_vdiagmc_values

6. **UEG mu* Parameterization and Mapping** (prior: 0.50 → belief: 0.53)
   - → supports: ab_initio_workflow

7. **vDiagMC Method** (prior: 0.50 → belief: 0.54)
   - → supports: mu_vdiagmc_values, dfpt_reliable_for_simple_metals

8. **Quasiparticle Mass Near Unity** (prior: 0.92 → belief: 0.93)
   - → supports: dfpt_reliable_for_simple_metals

9. **BTS Relation as Corollary** (prior: 0.50 → belief: 0.97)
   - → supports: bts_microscopic_equivalence

10. **BTS Renormalization Relation** (prior: 0.50 → belief: 0.97)
   - → supports: ab_initio_workflow, mu_vdiagmc_values, bts_microscopic_equivalence

11. **Ward Identity at q->0** (prior: 0.98 → belief: 0.99)
   - → supports: dfpt_reliable_for_simple_metals

## Adiabatic Approximation

12. **Cross-Channel Terms Suppressed** (prior: 0.50 → belief: 0.59)
   - → supports: downfolded_bse

13. **Adiabatic Approximation** (prior: 0.95 → belief: 0.96)
   - → supports: downfolded_bse

## Downfolded BSE

14. **Downfolded BSE ★** (prior: 0.50 → belief: 0.89)
   - ← infer(adiabatic_approx, cross_term_suppressed) [0.24 bits]
   - → supports: ab_initio_workflow, mu_vdiagmc_values, dfpt_reliable_for_simple_metals

## bts_microscopic_equivalence

15. **bts_microscopic_equivalence** (prior: 1.00 → belief: 1.00)

##

16. **** (prior: 1.00 → belief: 1.00)

## DFPT Reliable for Simple Metals

17. **mu from vDiagMC: Numerical Values ★** (prior: 0.50 → belief: 0.49)
   - ← infer(bts_renormalization, downfolded_bse, homotopic_expansion, vdiagmc_method) [0.07 bits]
   - → supports: ab_initio_workflow, rpa_vs_vdiagmc

18. **DFPT Reliable for Simple Metals ★** (prior: 0.50 → belief: 0.96)
   - ← infer(downfolded_bse, quasiparticle_mass_near_unity, vdiagmc_method, ward_identity) [0.11 bits]
   - → supports: ab_initio_workflow

## Ab Initio Tc Prediction Workflow

19. **rpa_vs_vdiagmc** (prior: 1.00 → belief: 1.00)

20. **Ab Initio Tc Prediction Workflow ★** (prior: 0.50 → belief: 0.96)
   - ← infer(bts_renormalization, dfpt_reliable_for_simple_metals, downfolded_bse, mu_vdiagmc_values, ueg_pseudopotential_parameterization) [0.01 bits]
   - → supports: al_pressure_transition, tc_al_likelihood, tc_al_predicted, tc_li_likelihood, tc_li_predicted, tc_mg_na_near_qpt, tc_zn_likelihood, tc_zn_predicted

## tc_li_likelihood

21. **tc_li_predicted ★** (prior: 0.50 → belief: 0.86)
   - ← infer(ab_initio_workflow, li_is_superconducting) [0.20 bits]

22. **tc_al_predicted ★** (prior: 0.50 → belief: 0.98)
   - ← infer(ab_initio_workflow) [0.31 bits]

23. **Na and Mg Near Quantum Phase Transition ★** (prior: 0.50 → belief: 0.98)
   - ← infer(ab_initio_workflow) [0.31 bits]

24. **tc_zn_predicted ★** (prior: 0.50 → belief: 0.98)
   - ← infer(ab_initio_workflow) [0.31 bits]

25. **Al Pressure-Tc Transition ★** (prior: 0.50 → belief: 0.98)
   - ← infer(ab_initio_workflow) [0.31 bits]

26. **tc_al_likelihood ★** (prior: 1.00 → belief: 1.00)
   - ← infer(ab_initio_workflow, mu_star_phenomenological) [0.58 bits]

27. **tc_zn_likelihood ★** (prior: 1.00 → belief: 1.00)
   - ← infer(ab_initio_workflow, mu_star_phenomenological) [0.50 bits]

28. **tc_li_likelihood ★** (prior: 1.00 → belief: 1.00)
   - ← infer(ab_initio_workflow, mu_star_phenomenological) [0.25 bits]
