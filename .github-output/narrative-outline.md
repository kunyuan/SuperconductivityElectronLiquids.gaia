# Narrative Outline

Auto-generated from the coarse reasoning graph. Sections are grouped by connectivity (high cohesion, low coupling) and ordered by topological layer. Use this as the backbone for writing narrative summaries.

## mu* as Phenomenological Parameter

1. **mu* as Phenomenological Parameter** (prior: 0.50 → belief: 0.07)
   - → supports: tc_al_likelihood, tc_li_likelihood, tc_zn_likelihood

## Adiabatic Approximation

2. **Cross-Channel Terms Suppressed** (prior: 0.50 → belief: 0.09)
   - → supports: downfolded_bse

3. **Adiabatic Approximation** (prior: 0.95 → belief: 0.76)
   - → supports: downfolded_bse

## Li is Bulk Superconducting

4. **Li Resistive Anomaly Is Not Bulk SC** (prior: 0.50 → belief: 0.29)
   - → supports: ?

5. **Li is Bulk Superconducting** (prior: 0.50 → belief: 0.71)
   - → supports: tc_li_predicted, ?

## Ward Identity at q->0

6. **vDiagMC Method** (prior: 0.50 → belief: 0.31)
   - → supports: mu_vdiagmc_values, dfpt_reliable_for_simple_metals

7. **UEG mu* Parameterization and Mapping** (prior: 0.50 → belief: 0.47)
   - → supports: ab_initio_workflow

8. **Homotopic Expansion** (prior: 0.50 → belief: 0.49)
   - → supports: mu_vdiagmc_values

9. **BTS Relation as Corollary** (prior: 0.50 → belief: 0.58)
   - → supports: bts_microscopic_equivalence

10. **BTS Renormalization Relation** (prior: 0.50 → belief: 0.58)
   - → supports: ab_initio_workflow, mu_vdiagmc_values, bts_microscopic_equivalence

11. **Quasiparticle Mass Near Unity** (prior: 0.92 → belief: 0.88)
   - → supports: dfpt_reliable_for_simple_metals

12. **Ward Identity at q->0** (prior: 0.98 → belief: 0.97)
   - → supports: dfpt_reliable_for_simple_metals

## RPA Predicts Attractive mu*

13. **RPA Predicts Attractive mu*** (prior: 0.50 → belief: 0.35)
   - → supports: rpa_vs_vdiagmc

## Downfolded BSE

14. **Downfolded BSE ★** (prior: 0.50 → belief: 0.02)
   - ← infer(adiabatic_approx, cross_term_suppressed)
   - → supports: ab_initio_workflow, mu_vdiagmc_values, dfpt_reliable_for_simple_metals

## 

15. **** (prior: 1.00 → belief: 1.00)

## bts_microscopic_equivalence

16. **bts_microscopic_equivalence** (prior: 1.00 → belief: 1.00)

## DFPT Reliable for Simple Metals

17. **mu from vDiagMC: Numerical Values ★** (prior: 0.50 → belief: 0.30)
   - ← infer(bts_renormalization, downfolded_bse, homotopic_expansion, vdiagmc_method)
   - → supports: ab_initio_workflow, rpa_vs_vdiagmc

18. **DFPT Reliable for Simple Metals ★** (prior: 0.50 → belief: 0.76)
   - ← infer(downfolded_bse, quasiparticle_mass_near_unity, vdiagmc_method, ward_identity)
   - → supports: ab_initio_workflow

## Ab Initio Tc Prediction Workflow

19. **rpa_vs_vdiagmc** (prior: 1.00 → belief: 1.00)

20. **Ab Initio Tc Prediction Workflow ★** (prior: 0.50 → belief: 0.24)
   - ← infer(bts_renormalization, dfpt_reliable_for_simple_metals, downfolded_bse, mu_vdiagmc_values, ueg_pseudopotential_parameterization)
   - → supports: al_pressure_transition, tc_al_likelihood, tc_al_predicted, tc_li_likelihood, tc_li_predicted, tc_mg_na_near_qpt, tc_zn_likelihood, tc_zn_predicted

## tc_li_likelihood

21. **tc_li_predicted ★** (prior: 0.50 → belief: 0.57)
   - ← infer(ab_initio_workflow, li_is_superconducting)

22. **Na and Mg Near Quantum Phase Transition ★** (prior: 0.50 → belief: 0.62)
   - ← infer(ab_initio_workflow)

23. **tc_al_predicted ★** (prior: 0.50 → belief: 0.62)
   - ← infer(ab_initio_workflow)

24. **Al Pressure-Tc Transition ★** (prior: 0.50 → belief: 0.62)
   - ← infer(ab_initio_workflow)

25. **tc_zn_predicted ★** (prior: 0.50 → belief: 0.62)
   - ← infer(ab_initio_workflow)

26. **tc_al_likelihood ★** (prior: 1.00 → belief: 1.00)
   - ← infer(ab_initio_workflow, mu_star_phenomenological) [0.41 bits]

27. **tc_zn_likelihood ★** (prior: 1.00 → belief: 1.00)
   - ← infer(ab_initio_workflow, mu_star_phenomenological) [0.37 bits]

28. **tc_li_likelihood ★** (prior: 1.00 → belief: 1.00)
   - ← infer(ab_initio_workflow, mu_star_phenomenological) [0.29 bits]
