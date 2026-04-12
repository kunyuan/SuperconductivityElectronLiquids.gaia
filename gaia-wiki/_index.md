# 电子液体中的超导性

本知识包形式化了论文 *Superconductivity in Electron Liquids* (Cai, Wang, Zhang, Zhang, Millis, Svistunov, Prokof'ev, Chen, 2026) 的核心论证结构。论文建立了一个严格的第一性原理框架，通过变分图解蒙特卡罗（vDiagMC）方法从微观哈密顿量出发精确计算 Coulomb 赝势 $\mu^*$ 和电子-声子耦合 $\lambda$，消除了传统 Migdal-Eliashberg 理论中的唯象参数，实现了对简单金属超导转变温度 $T_c$ 的无自由参数预测。

IR hash: `sha256:a0e59a769...`

## 统计

| 指标 | 数量 |
|------|------|
| 知识节点 | 78（69 命题，8 设定，1 问题） |
| 推理策略 | 30 |
| 算符 | 2 |
| 章节 | 8 |
| 导出结论 | 9 |

## 章节

| # | 章节 | 命题数 |
|---|------|--------|
| 01 | [[motivation|研究动机]] | 16 |
| 02 | [[s2_model|模型与基本关系]] | 3 |
| 03 | [[s3_downfolding|BSE 下折叠]] | 13 |
| 04 | [[s4_pseudopotential|Coulomb 赝势]] | 5 |
| 05 | [[s5_eph_coupling|电子-声子耦合]] | 8 |
| 06 | [[s6_superconductors|常规超导体]] | 14 |
| 07 | [[weak-points|薄弱环节]] | 10 |
| 08 | [[open-questions|开放问题]] | 30 |

## 命题索引

| # | 命题 | 类型 | 章节 | 信念 |
|---|------|------|------|------|
| 01 | [[bcs_theory]] | setting | [[motivation|研究动机]] | — |
| 02 | [[adiabatic_approx]] | claim | [[motivation|研究动机]] | 0.71 |
| 03 | [[bts_renormalization]] | claim | [[motivation|研究动机]] | 0.98 |
| 04 | [[me_downfolding_is_phenomenological]] | claim | [[motivation|研究动机]] | 0.95 |
| 05 | [[phenomenological_me_theory]] | claim | [[motivation|研究动机]] | 0.95 |
| 06 | [[mu_star_phenomenological]] | claim | [[motivation|研究动机]] | 0.95 |
| 07 | [[rpa_predicts_attractive_mu]] | claim | [[motivation|研究动机]] | 0.23 |
| 08 | [[dfpt_computes_lambda]] | claim | [[motivation|研究动机]] | 0.92 |
| 09 | [[tc_al_experimental]] | claim | [[motivation|研究动机]] | 1.00 |
| 10 | [[tc_li_experimental]] | claim | [[motivation|研究动机]] | 0.94 |
| 11 | [[tc_zn_experimental]] | claim | [[motivation|研究动机]] | 1.00 |
| 12 | [[tc_al_phenomenological]] | claim | [[motivation|研究动机]] | 0.41 |
| 13 | [[tc_li_phenomenological]] | claim | [[motivation|研究动机]] | 0.13 |
| 14 | [[tc_zn_phenomenological]] | claim | [[motivation|研究动机]] | 0.41 |
| 15 | [[main_question]] | question | [[motivation|研究动机]] | — |
| 16 | [[electron_phonon_action]] | claim | [[s2_model|模型]] | 0.95 |
| 17 | [[precursory_cooper_flow]] | claim | [[s2_model|模型]] | 0.90 |
| 18 | [[pair_propagator_decomposition]] | setting | [[s3_downfolding|下折叠]] | — |
| 19 | [[cross_term_suppressed]] | claim | [[s3_downfolding|下折叠]] | 0.50 |
| 20 | [[rpa_dynamic_screening]] | setting | [[s3_downfolding|下折叠]] | — |
| 21 | [[downfolding_validity_limits]] | claim | [[s3_downfolding|下折叠]] | 0.92 |
| 22 | [[ueg_vertex_challenge]] | claim | [[s4_pseudopotential|赝势]] | 0.95 |
| 23 | [[vdiagmc_method]] | claim | [[s4_pseudopotential|赝势]] | 0.84 |
| 24 | [[homotopic_expansion]] | claim | [[s4_pseudopotential|赝势]] | 0.81 |
| 25 | [[ward_identity]] | claim | [[s5_eph_coupling|电声耦合]] | 0.99 |
| 26 | [[gamma3_vdiagmc]] | claim | [[s5_eph_coupling|电声耦合]] | 0.95 |
| 27 | [[dfpt_eph_ansatz]] | claim | [[s5_eph_coupling|电声耦合]] | 0.90 |
| 28 | [[quasiparticle_mass_near_unity]] | claim | [[s5_eph_coupling|电声耦合]] | 0.88 |
| 29 | [[aluminum_parameters]] | setting | [[s6_superconductors|超导体]] | — |
| 30 | [[lithium_parameters]] | setting | [[s6_superconductors|超导体]] | — |
| 31 | [[sodium_parameters]] | setting | [[s6_superconductors|超导体]] | — |
| 32 | [[magnesium_parameters]] | setting | [[s6_superconductors|超导体]] | — |
| 33 | [[zinc_parameters]] | setting | [[s6_superconductors|超导体]] | — |
| 34 | [[simple_metals_weak_lattice]] | claim | [[s6_superconductors|超导体]] | 0.90 |
| 35 | [[ueg_pseudopotential_parameterization]] | claim | [[s6_superconductors|超导体]] | 0.85 |
| 36 | [[me_framework]] | claim | [[motivation|研究动机]] | 0.75 |
| 37 | [[mu_vdiagmc_values]] ★ | claim | [[s4_pseudopotential|赝势]] | 0.55 |
| 38 | [[gamma3_approximation]] | claim | [[s5_eph_coupling|电声耦合]] | 0.62 |
| 39 | [[bse_kernel_decomposition]] | claim | [[s2_model|模型]] | 0.78 |
| 40 | [[rpa_vs_vdiagmc]] | claim | [[s4_pseudopotential|赝势]] | 1.00 |
| 41 | [[mu_available_for_simple_metals]] | claim | [[s6_superconductors|超导体]] | 0.41 |
| 42 | [[full_bse_toy_model]] | claim | [[s3_downfolding|下折叠]] | 0.76 |
| 43 | [[downfolded_bse]] ★ | claim | [[s3_downfolding|下折叠]] | 0.33 |
| 44 | [[downfolded_bse_toy_model]] | claim | [[s3_downfolding|下折叠]] | 0.32 |
| 45 | [[downfolded_me_equation]] | claim | [[s3_downfolding|下折叠]] | 0.66 |
| 46 | [[lambda_microscopic_definition]] | claim | [[s3_downfolding|下折叠]] | 0.50 |
| 47 | [[mu_microscopic_definition]] | claim | [[s3_downfolding|下折叠]] | 0.54 |
| 48 | [[mu_scale_independence]] | claim | [[s3_downfolding|下折叠]] | 0.98 |
| 49 | [[ma_pseudopotential_justified]] | claim | [[s3_downfolding|下折叠]] | 0.77 |
| 50 | [[eft_eph_vertex]] | claim | [[s5_eph_coupling|电声耦合]] | 0.66 |
| 51 | [[bts_microscopic_equivalence]] | claim | [[s3_downfolding|下折叠]] | 1.00 |
| 52 | [[eft_vertex_matches_dfpt]] | claim | [[s5_eph_coupling|电声耦合]] | 0.58 |
| 53 | [[dfpt_reliable_for_simple_metals]] ★ | claim | [[s5_eph_coupling|电声耦合]] | 0.75 |
| 54 | [[ab_initio_workflow]] ★ | claim | [[s6_superconductors|超导体]] | 0.96 |
| 55 | [[tc_al_predicted]] ★ | claim | [[s6_superconductors|超导体]] | 0.90 |
| 56 | [[tc_zn_predicted]] ★ | claim | [[s6_superconductors|超导体]] | 0.90 |
| 57 | [[tc_li_predicted]] ★ | claim | [[s6_superconductors|超导体]] | 0.90 |
| 58 | [[al_pressure_transition]] ★ | claim | [[s6_superconductors|超导体]] | 0.77 |
| 59 | [[tc_mg_na_near_qpt]] ★ | claim | [[s6_superconductors|超导体]] | 0.77 |

## 阅读路径

[[motivation|研究动机]] → [[s2_model|模型与基本关系]] → [[s3_downfolding|BSE 下折叠]] → [[s4_pseudopotential|Coulomb 赝势]] → [[s5_eph_coupling|电子-声子耦合]] → [[s6_superconductors|常规超导体]] → [[weak-points|薄弱环节]] → [[open-questions|开放问题]]

## 快速链接

- [[overview|推理图总览]] — 推理图可视化
- [[beliefs|信念状态总览]] — 完整信念表
- [[holes|叶前提]] — 证据基础
