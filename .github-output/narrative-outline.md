# Narrative Outline

Auto-generated from the coarse reasoning graph. Sections are grouped by connectivity (high cohesion, low coupling) and ordered by topological layer. Use this as the backbone for writing narrative summaries.

## RPA Predicts Attractive mu*

1. **RPA Predicts Attractive mu*** (prior: 0.50 → belief: 0.09)
   - → supports: rpa_vs_vdiagmc

## UEG mu_EF Table I

2. **Li Low-Temperature Lattice Assumption** (prior: 0.60 → belief: 0.69)
   - → supports: tc_li_predicted

3. **Shared DFPT Lambda Error Model** (prior: 0.78 → belief: 0.82)
   - → supports: tc_al_predicted, tc_li_predicted, tc_zn_predicted

4. **Li 9R arXiv Table II Row** (prior: 0.82 → belief: 0.83)
   - → supports: tc_li_predicted

5. **Tolmachev Log mu* Error Model** (prior: 0.80 → belief: 0.83)
   - → supports: tc_al_predicted, tc_li_predicted, tc_zn_predicted

6. **Al arXiv Table II Row** (prior: 0.90 → belief: 0.91)
   - → supports: tc_al_predicted

7. **Zn arXiv Table II Row** (prior: 0.90 → belief: 0.91)
   - → supports: tc_zn_predicted

8. **UEG mu_EF Table I** (prior: 0.90 → belief: 0.92)
   - → supports: tc_al_predicted, tc_li_predicted, tc_zn_predicted

## vDiagMC Method

9. **Homotopic Expansion** (prior: 0.88 → belief: 0.85)
   - → supports: mu_vdiagmc_values

10. **vDiagMC Method** (prior: 0.90 → belief: 0.87)
   - → supports: mu_vdiagmc_values

## UEG mu* Parameterization and Mapping

11. **UEG mu* Parameterization and Mapping** (prior: 0.85 → belief: 0.87)
   - → supports: ab_initio_workflow

## Ward Identity at q->0

12. **vDiagMC Computation of Gamma_3** (prior: 0.88 → belief: 0.88)
   - → supports: dfpt_reliable_for_simple_metals

13. **Quasiparticle Mass Near Unity** (prior: 0.92 → belief: 0.93)
   - → supports: dfpt_reliable_for_simple_metals

14. **Ward Identity at q->0** (prior: 0.98 → belief: 0.98)
   - → supports: dfpt_reliable_for_simple_metals

## Adiabatic Approximation

15. **Cross-Channel Terms Suppressed** (prior: 0.90 → belief: 0.93)
   - → supports: downfolded_bse

16. **Adiabatic Approximation** (prior: 0.95 → belief: 0.96)
   - → supports: downfolded_bse

## Downfolded BSE

17. **mu from vDiagMC: Numerical Values ★** (prior: 0.50 → belief: 0.83)
   - ← infer(homotopic_expansion, vdiagmc_method) [0.34 bits]
   - → supports: ab_initio_workflow, rpa_vs_vdiagmc

18. **Downfolded BSE ★** (prior: 0.50 → belief: 0.98)
   - ← infer(adiabatic_approx, cross_term_suppressed) [0.07 bits]
   - → supports: ab_initio_workflow, dfpt_reliable_for_simple_metals

## DFPT Reliable for Simple Metals

19. **DFPT Reliable for Simple Metals ★** (prior: 0.50 → belief: 0.96)
   - ← infer(downfolded_bse, gamma3_vdiagmc, quasiparticle_mass_near_unity, ward_identity) [0.10 bits]
   - → supports: ab_initio_workflow

## rpa_vs_vdiagmc

20. **rpa_vs_vdiagmc** (prior: 1.00 → belief: 1.00)

## Ab Initio Tc Prediction Workflow

21. **Ab Initio Tc Prediction Workflow ★** (prior: 0.50 → belief: 0.96)
   - ← infer(dfpt_reliable_for_simple_metals, downfolded_bse, mu_vdiagmc_values, ueg_pseudopotential_parameterization) [0.05 bits]
   - → supports: al_pressure_transition, tc_al_predicted, tc_li_predicted, tc_mg_na_near_qpt, tc_zn_predicted

## Tc(Zn) Ab Initio Prediction

22. **Tc(Li) Ab Initio Prediction ★** (prior: 0.50 → belief: 0.83)
   - ← infer(ab_initio_workflow, li_arxiv_table_row, li_low_temperature_lattice_assumption, shared_dfpt_lambda_error_model, tolmachev_log_mu_star_error_model, ueg_mu_ef_table_i) [0.13 bits]

23. **Al Pressure-Tc Transition ★** (prior: 0.50 → belief: 0.98)
   - ← infer(ab_initio_workflow) [0.30 bits]

24. **Na and Mg Near Quantum Phase Transition ★** (prior: 0.50 → belief: 0.98)
   - ← infer(ab_initio_workflow) [0.30 bits]

25. **Tc(Al) Ab Initio Prediction ★** (prior: 0.50 → belief: 0.99)
   - ← infer(ab_initio_workflow, al_arxiv_table_row, shared_dfpt_lambda_error_model, tolmachev_log_mu_star_error_model, ueg_mu_ef_table_i) [0.04 bits]

26. **Tc(Zn) Ab Initio Prediction ★** (prior: 0.50 → belief: 0.99)
   - ← infer(ab_initio_workflow, shared_dfpt_lambda_error_model, tolmachev_log_mu_star_error_model, ueg_mu_ef_table_i, zn_arxiv_table_row) [0.02 bits]
