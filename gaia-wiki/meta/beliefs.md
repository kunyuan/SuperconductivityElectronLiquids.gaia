---
type: meta
aliases: [beliefs]
tags: [meta, beliefs]
---

# 信念状态总览

本表汇总了知识图中所有命题的先验概率（Prior）和经贝叶斯推理更新后的信念度（Belief）。信念度由 Gaia 信念传播引擎在因子图上运行 loopy BP 算法计算得到。Prior 仅对独立前提（holes）赋值，衡量该证据本身的可靠性；Belief 综合了所有推理链的约束后给出的后验估计。

| # | 标签 | 类型 | 先验 | 信念 | 角色 |
|---|------|------|------|------|------|
| 51 | [[bts_microscopic_equivalence]] | claim | — | 1.00 | 结构性 |
| 40 | [[rpa_vs_vdiagmc]] | claim | — | 1.00 | 结构性 |
| 09 | [[tc_al_experimental]] | claim | 0.99 | 1.00 | 独立前提 |
| 11 | [[tc_zn_experimental]] | claim | 0.99 | 1.00 | 独立前提 |
| 25 | [[ward_identity]] | claim | 0.98 | 0.99 | 独立前提 |
| 03 | [[bts_renormalization]] | claim | 0.95 | 0.98 | 独立前提 |
| 48 | [[mu_scale_independence]] | claim | — | 0.98 | 推导结论 |
| 54 | [[ab_initio_workflow]] | claim | — | 0.96 | 推导结论 |
| 26 | [[gamma3_vdiagmc]] | claim | 0.88 | 0.95 | 独立前提 |
| 04 | [[me_downfolding_is_phenomenological]] | claim | 0.95 | 0.95 | 孤立 |
| 05 | [[phenomenological_me_theory]] | claim | 0.95 | 0.95 | 孤立 |
| 06 | [[mu_star_phenomenological]] | claim | 0.95 | 0.95 | 背景 |
| 16 | [[electron_phonon_action]] | claim | 0.95 | 0.95 | 背景 |
| 22 | [[ueg_vertex_challenge]] | claim | 0.95 | 0.95 | 背景 |
| 10 | [[tc_li_experimental]] | claim | 0.85 | 0.94 | 独立前提 |
| 08 | [[dfpt_computes_lambda]] | claim | 0.92 | 0.92 | 背景 |
| 21 | [[downfolding_validity_limits]] | claim | 0.92 | 0.92 | 孤立 |
| 55 | [[tc_al_predicted]] | claim | — | 0.90 | 推导结论 |
| 56 | [[tc_zn_predicted]] | claim | — | 0.90 | 推导结论 |
| 17 | [[precursory_cooper_flow]] | claim | 0.90 | 0.90 | 背景 |
| 27 | [[dfpt_eph_ansatz]] | claim | 0.90 | 0.90 | 背景 |
| 34 | [[simple_metals_weak_lattice]] | claim | 0.90 | 0.90 | 背景 |
| 57 | [[tc_li_predicted]] | claim | — | 0.90 | 推导结论 |
| 28 | [[quasiparticle_mass_near_unity]] | claim | 0.92 | 0.88 | 独立前提 |
| 35 | [[ueg_pseudopotential_parameterization]] | claim | 0.85 | 0.85 | 独立前提 |
| 23 | [[vdiagmc_method]] | claim | 0.90 | 0.84 | 独立前提 |
| 24 | [[homotopic_expansion]] | claim | 0.88 | 0.81 | 独立前提 |
| 39 | [[bse_kernel_decomposition]] | claim | — | 0.78 | 推导结论 |
| 49 | [[ma_pseudopotential_justified]] | claim | — | 0.77 | 推导结论 |
| 58 | [[al_pressure_transition]] | claim | — | 0.77 | 推导结论 |
| 59 | [[tc_mg_na_near_qpt]] | claim | — | 0.77 | 推导结论 |
| 42 | [[full_bse_toy_model]] | claim | — | 0.76 | 推导结论 |
| 53 | [[dfpt_reliable_for_simple_metals]] | claim | — | 0.75 | 推导结论 |
| 36 | [[me_framework]] | claim | — | 0.75 | 推导结论 |
| 02 | [[adiabatic_approx]] | claim | 0.95 | 0.71 | 独立前提 |
| 45 | [[downfolded_me_equation]] | claim | — | 0.66 | 推导结论 |
| 50 | [[eft_eph_vertex]] | claim | — | 0.66 | 推导结论 |
| 38 | [[gamma3_approximation]] | claim | — | 0.62 | 推导结论 |
| 52 | [[eft_vertex_matches_dfpt]] | claim | — | 0.58 | 推导结论 |
| 37 | [[mu_vdiagmc_values]] | claim | — | 0.55 | 推导结论 |
| 47 | [[mu_microscopic_definition]] | claim | — | 0.54 | 推导结论 |
| 19 | [[cross_term_suppressed]] | claim | 0.90 | 0.50 | 独立前提 |
| 46 | [[lambda_microscopic_definition]] | claim | — | 0.50 | 推导结论 |
| 41 | [[mu_available_for_simple_metals]] | claim | — | 0.41 | 推导结论 |
| 12 | [[tc_al_phenomenological]] | claim | 0.35 | 0.41 | 独立前提 |
| 14 | [[tc_zn_phenomenological]] | claim | 0.35 | 0.41 | 独立前提 |
| 43 | [[downfolded_bse]] | claim | — | 0.33 | 推导结论 |
| 44 | [[downfolded_bse_toy_model]] | claim | — | 0.32 | 推导结论 |
| 07 | [[rpa_predicts_attractive_mu]] | claim | 0.50 | 0.23 | 独立前提 |
| 13 | [[tc_li_phenomenological]] | claim | 0.10 | 0.13 | 独立前提 |
| 01 | [[bcs_theory]] | setting | — | — | 设定 |
| 15 | [[main_question]] | question | — | — | 问题 |
| 18 | [[pair_propagator_decomposition]] | setting | — | — | 设定 |
| 20 | [[rpa_dynamic_screening]] | setting | — | — | 设定 |
| 29 | [[aluminum_parameters]] | setting | — | — | 设定 |
| 30 | [[lithium_parameters]] | setting | — | — | 设定 |
| 31 | [[sodium_parameters]] | setting | — | — | 设定 |
| 32 | [[magnesium_parameters]] | setting | — | — | 设定 |
| 33 | [[zinc_parameters]] | setting | — | — | 设定 |
