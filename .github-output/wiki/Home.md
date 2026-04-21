# superconductivity_electron_liquids

## Modules

- [motivation](Module-motivation) (16 nodes)
- [s2_model](Module-s2-model) (3 nodes)
- [s3_downfolding](Module-s3-downfolding) (14 nodes)
- [s4_pseudopotential](Module-s4-pseudopotential) (5 nodes)
- [s5_eph_coupling](Module-s5-eph-coupling) (10 nodes)
- [s6_superconductors](Module-s6-superconductors) (35 nodes)
- [Root](Module-Root) (0 nodes)

## Claim Index

| Label | Type | Module | Belief |
|-------|------|--------|--------|
| bcs_theory | setting | motivation | — |
| adiabatic_approx | claim | motivation | 0.96 |
| me_framework | claim | motivation | 0.97 |
| bts_renormalization | claim | motivation | 1.00 |
| me_downfolding_is_phenomenological | claim | motivation | 0.95 |
| phenomenological_me_theory | claim | motivation | 0.95 |
| mu_star_phenomenological | claim | motivation | 0.99 |
| rpa_predicts_attractive_mu | claim | motivation | 0.13 |
| dfpt_computes_lambda | claim | motivation | 0.99 |
| tc_al_experimental | claim | motivation | 0.99 |
| tc_li_experimental | claim | motivation | 0.85 |
| tc_zn_experimental | claim | motivation | 0.99 |
| tc_al_phenomenological | claim | motivation | 1.00 |
| tc_li_phenomenological | claim | motivation | 1.00 |
| tc_zn_phenomenological | claim | motivation | 1.00 |
| main_question | question | motivation | — |
| electron_phonon_action | claim | s2_model | 0.95 |
| bse_kernel_decomposition | claim | s2_model | 0.98 |
| precursory_cooper_flow | claim | s2_model | 0.90 |
| pair_propagator_decomposition | setting | s3_downfolding | — |
| cross_term_suppressed | claim | s3_downfolding | 0.93 |
| rpa_dynamic_screening | setting | s3_downfolding | — |
| full_bse_toy_model | claim | s3_downfolding | 0.99 |
| downfolded_bse_toy_model | claim | s3_downfolding | 0.99 |
| downfolding_validity_limits | claim | s3_downfolding | 0.92 |
| downfolded_bse | claim | s3_downfolding | 0.96 |
|  | claim | s3_downfolding | 1.00 |
| downfolded_me_equation | claim | s3_downfolding | 0.97 |
| lambda_microscopic_definition | claim | s3_downfolding | 0.96 |
| mu_microscopic_definition | claim | s3_downfolding | 0.98 |
| mu_scale_independence | claim | s3_downfolding | 1.00 |
| bts_microscopic_equivalence | claim | s3_downfolding | 1.00 |
| ma_pseudopotential_justified | claim | s3_downfolding | 0.96 |
| ueg_vertex_challenge | claim | s4_pseudopotential | 0.95 |
| vdiagmc_method | claim | s4_pseudopotential | 0.87 |
| homotopic_expansion | claim | s4_pseudopotential | 0.84 |
| mu_vdiagmc_values | claim | s4_pseudopotential | 0.75 |
| rpa_vs_vdiagmc | claim | s4_pseudopotential | 1.00 |
| ward_identity | claim | s5_eph_coupling | 0.98 |
| gamma3_vdiagmc | claim | s5_eph_coupling | 0.88 |
| dfpt_eph_ansatz | claim | s5_eph_coupling | 0.90 |
| quasiparticle_mass_near_unity | claim | s5_eph_coupling | 0.92 |
| eft_eph_vertex | claim | s5_eph_coupling | 0.97 |
| gamma3_approximation | claim | s5_eph_coupling | 0.86 |
| gamma3_interpolation_test_valid | claim | s5_eph_coupling | 0.90 |
| gamma3_evidence_independent | claim | s5_eph_coupling | 0.93 |
| eft_vertex_matches_dfpt | claim | s5_eph_coupling | 0.88 |
| dfpt_reliable_for_simple_metals | claim | s5_eph_coupling | 0.87 |
| aluminum_parameters | setting | s6_superconductors | — |
| lithium_parameters | setting | s6_superconductors | — |
| sodium_parameters | setting | s6_superconductors | — |
| magnesium_parameters | setting | s6_superconductors | — |
| zinc_parameters | setting | s6_superconductors | — |
| simple_metals_weak_lattice | claim | s6_superconductors | 0.90 |
| ueg_pseudopotential_parameterization | claim | s6_superconductors | 0.85 |
| ab_initio_workflow | claim | s6_superconductors | 0.80 |
| mu_available_for_simple_metals | claim | s6_superconductors | 0.78 |
| tc_al_predicted | claim | s6_superconductors | 0.84 |
| tc_zn_predicted | claim | s6_superconductors | 0.84 |
| tc_li_predicted | claim | s6_superconductors | 0.82 |
| al_pressure_transition | claim | s6_superconductors | 0.82 |
| tc_mg_na_near_qpt | claim | s6_superconductors | 0.82 |
| tc_al_abinitio_outperforms_phenomenological | claim | s6_superconductors | 0.83 |
| tc_al_comparison_valid | claim | s6_superconductors | 0.95 |
|  | claim | s6_superconductors | 1.00 |
|  | claim | s6_superconductors | 1.00 |
|  | claim | s6_superconductors | 1.00 |
|  | claim | s6_superconductors | 1.00 |
|  | claim | s6_superconductors | 1.00 |
| tc_zn_abinitio_outperforms_phenomenological | claim | s6_superconductors | 0.86 |
| tc_zn_comparison_valid | claim | s6_superconductors | 0.97 |
|  | claim | s6_superconductors | 1.00 |
|  | claim | s6_superconductors | 1.00 |
|  | claim | s6_superconductors | 1.00 |
|  | claim | s6_superconductors | 1.00 |
|  | claim | s6_superconductors | 1.00 |
| tc_li_abinitio_outperforms_phenomenological | claim | s6_superconductors | 0.79 |
| tc_li_comparison_valid | claim | s6_superconductors | 0.88 |
|  | claim | s6_superconductors | 1.00 |
|  | claim | s6_superconductors | 1.00 |
|  | claim | s6_superconductors | 1.00 |
|  | claim | s6_superconductors | 1.00 |
|  | claim | s6_superconductors | 1.00 |
