# Module: motivation

### bcs_theory

**QID:** `github:superconductivity_electron_liquids::bcs_theory`
**Type:** claim
**Role:** background
**Content:** Bardeen-Cooper-Schrieffer (BCS) theory: phonon-mediated electron-electron attraction leads to Cooper pairing instability at the Fermi surface, providing the fundamental framework for understanding conventional superconductors.
**Prior:** 0.98
**Belief:** 0.98
**prior_records:** [{'value': 0.98, 'source_id': 'established_theoretical_framework', 'justification': 'BCS theory has been the canonical framework for conventional phonon-mediated superconductors since 1957, with extensive experimental validation across simple metals, alloys, and elemental superconductors.'}]
**prior:** 0.98
**prior_justification:** BCS theory has been the canonical framework for conventional phonon-mediated superconductors since 1957, with extensive experimental validation across simple metals, alloys, and elemental superconductors.
**prior_source_id:** established_theoretical_framework

### adiabatic_approx

**QID:** `github:superconductivity_electron_liquids::adiabatic_approx`
**Type:** claim
**Role:** independent
**Content:** In conventional metals, the typical phonon frequency (Debye frequency $\omega_D$) is much smaller than the electron Fermi energy $E_F$, i.e. $\omega_D / E_F \ll 1$ (adiabatic approximation). This energy-scale separation has three key consequences: (i) electrons adiabatically adjust to ionic motion, (ii) the electron-ion coupling can be linearized, and (iii) the space-time scale separation between electron and phonon physics permits a controlled effective field theory (EFT) treatment.
**Prior:** 0.95
**Belief:** 0.76
**prior_records:** [{'value': 0.95, 'source_id': 'empirical_physical_scale', 'justification': "For simple metals omega_D / E_F ~ 0.005, satisfying the adiabatic small-parameter condition by two orders of magnitude. Migdal's theorem has been validated across the relevant material class."}]
**prior:** 0.95
**prior_justification:** For simple metals omega_D / E_F ~ 0.005, satisfying the adiabatic small-parameter condition by two orders of magnitude. Migdal's theorem has been validated across the relevant material class.
**prior_source_id:** empirical_physical_scale
**Referenced by:** deduction -> `github:superconductivity_electron_liquids::me_framework`

### me_framework

**QID:** `github:superconductivity_electron_liquids::me_framework`
**Type:** claim
**Role:** derived
**Content:** Migdal-Eliashberg (ME) theory provides a rigorous treatment of the dynamic electron-phonon interaction. Under the adiabatic condition $\omega_D / E_F \ll 1$, Migdal's theorem guarantees that phonon vertex corrections are suppressed at $O(\omega_D/E_F)$, allowing the electron-phonon self-energy to be truncated at the self-consistent Fock diagram level. This justifies the ME formalism as a controlled low-energy theory for electron-phonon superconductors.
**Belief:** 0.80
**Derived from:** deduction
**Premises:** `github:superconductivity_electron_liquids::adiabatic_approx`
**figure:** artifacts/images/4_0.jpg
**caption:** Fig. 1 | Normal component of the electron self-energy approximated by the self-consistent Fock diagram with the phonon-mediated e-e interaction W^ph.
**Referenced by:** deduction -> `github:superconductivity_electron_liquids::bse_kernel_decomposition`

### github:superconductivity_electron_liquids::_anon_000

**QID:** `github:superconductivity_electron_liquids::_anon_000`
**Type:** claim
**Role:** orphaned
**Content:** derive warrants Migdal-Eliashberg (ME) theory provides a rigorous treatment of the dynamic electron-phonon interaction. Under the adiabatic condition $\omega_D / E_F \ll 1$, Migdal's theorem guarantees that phonon vertex corrections are suppressed at $O(\omega_D/E_F)$, allowing the electron-phonon self-energy to be truncated at the self-consistent Fock diagram level. This justifies the ME formalism as a controlled low-energy theory for electron-phonon superconductors.
**Belief:** 0.50
**generated:** True
**helper_kind:** implication_warrant
**review:** True
**relation:** {'type': 'derive', 'given': ['github:superconductivity_electron_liquids::adiabatic_approx'], 'conclusion': 'github:superconductivity_electron_liquids::me_framework'}
**warrant:** The adiabatic condition $\omega_D/E_F \ll 1$ (@adiabatic_approx) ensures that the ratio of ionic to electronic energy scales is small. Migdal's theorem then proves that phonon vertex corrections beyond the self-consistent Fock level are suppressed by $O(\omega_D/E_F)$, establishing the Migdal-Eliashberg formalism as a controlled approximation built on the BCS pairing mechanism (@bcs_theory).
**action_label:** github:superconductivity_electron_liquids::action::_anon_action_000
**pattern:** derivation
**gaia:** {'provenance': {'referenced_claims': ['adiabatic_approx', 'bcs_theory']}}

### bts_renormalization

**QID:** `github:superconductivity_electron_liquids::bts_renormalization`
**Type:** claim
**Role:** independent
**Content:** The Bogoliubov-Tolmachev-Shirkov (BTS) renormalization relation connects the Coulomb pseudopotential $\mu_{\omega_c}$ (a dimensionless parameter describing the effective electron-electron repulsion strength in the pairing channel) defined at different energy cutoff scales $\omega_c$: $\mu_{\omega_c} = \mu_{\omega_c'} / (1 + \mu_{\omega_c'} \ln(\omega_c'/\omega_c))$. This relation ensures that physical observables do not depend on the choice of the arbitrary cutoff scale.
**Belief:** 0.58
**Referenced by:** deduction -> `github:superconductivity_electron_liquids::mu_vdiagmc_values`; deduction -> `github:superconductivity_electron_liquids::mu_available_for_simple_metals`; unknown -> `github:superconductivity_electron_liquids::bts_microscopic_equivalence`

### me_downfolding_is_phenomenological

**QID:** `github:superconductivity_electron_liquids::me_downfolding_is_phenomenological`
**Type:** claim
**Role:** derived
**Content:** The downfolding procedure (integrating out high-energy degrees of freedom to obtain a low-energy effective theory) in traditional Migdal-Eliashberg (ME) theory is phenomenological: the Coulomb effect is replaced by a static pseudopotential $\mu^*$, ignoring corrections from Coulomb fluctuations to quasiparticle renormalization and electron-phonon coupling, as well as non-local effects of screening.
**Belief:** 0.19
**Derived from:** deduction
**Premises:** `github:superconductivity_electron_liquids::mu_star_phenomenological`
**Referenced by:** deduction -> `github:superconductivity_electron_liquids::phenomenological_me_theory`

### phenomenological_me_theory

**QID:** `github:superconductivity_electron_liquids::phenomenological_me_theory`
**Type:** claim
**Role:** derived
**Content:** Traditional electron-phonon superconductivity theory uses the McMillan (or Allen-Dynes) formula, with the electron-phonon coupling constant $\lambda$ and Coulomb pseudopotential $\mu^*$ as inputs to predict the superconducting transition temperature $T_c$. Since $\mu^*$ cannot be reliably computed from first principles, it is typically assigned an empirical value $\mu^* \in [0.1, 0.2]$. For materials with $T_c$ in the sub-kelvin range, the exponential sensitivity $T_c \propto \exp(-1/g)$ to $\mu^*$ causes this uncertainty to span several orders of magnitude in the predicted $T_c$, destroying predictive power.
**Belief:** 0.31
**Derived from:** deduction
**Premises:** `github:superconductivity_electron_liquids::me_downfolding_is_phenomenological`
**Referenced by:** deduction -> `github:superconductivity_electron_liquids::tc_al_phenomenological`; deduction -> `github:superconductivity_electron_liquids::tc_zn_phenomenological`; deduction -> `github:superconductivity_electron_liquids::tc_li_phenomenological`; infer -> `github:superconductivity_electron_liquids::tc_al_likelihood`; infer -> `github:superconductivity_electron_liquids::tc_zn_likelihood`; infer -> `github:superconductivity_electron_liquids::tc_li_likelihood`

### mu_star_phenomenological

**QID:** `github:superconductivity_electron_liquids::mu_star_phenomenological`
**Type:** claim
**Role:** independent
**Content:** Due to the lack of a reliable microscopic calculation, the Coulomb pseudopotential $\mu^*$ (a dimensionless parameter describing the effective Coulomb repulsion strength in the low-energy pairing channel) is typically treated as an adjustable parameter with empirical values in the range 0.1--0.2.
**Belief:** 0.07
**Referenced by:** deduction -> `github:superconductivity_electron_liquids::me_downfolding_is_phenomenological`; deduction -> `github:superconductivity_electron_liquids::tc_al_phenomenological`; deduction -> `github:superconductivity_electron_liquids::tc_zn_phenomenological`; deduction -> `github:superconductivity_electron_liquids::tc_li_phenomenological`

### github:superconductivity_electron_liquids::_anon_001

**QID:** `github:superconductivity_electron_liquids::_anon_001`
**Type:** claim
**Role:** orphaned
**Content:** derive warrants The downfolding procedure (integrating out high-energy degrees of freedom to obtain a low-energy effective theory) in traditional Migdal-Eliashberg (ME) theory is phenomenological: the Coulomb effect is replaced by a static pseudopotential $\mu^*$, ignoring corrections from Coulomb fluctuations to quasiparticle renormalization and electron-phonon coupling, as well as non-local effects of screening.
**Belief:** 0.50
**generated:** True
**helper_kind:** implication_warrant
**review:** True
**relation:** {'type': 'derive', 'given': ['github:superconductivity_electron_liquids::mu_star_phenomenological'], 'conclusion': 'github:superconductivity_electron_liquids::me_downfolding_is_phenomenological'}
**warrant:** Because $\mu^*$ is treated as an empirical adjustable parameter rather than computed from first principles (@mu_star_phenomenological), the downfolding procedure in traditional Migdal-Eliashberg theory is necessarily phenomenological: the Coulomb effect is replaced by a single static value with no microscopic underpinning, and corrections from Coulomb fluctuations to quasiparticle renormalization and electron-phonon coupling are absent because the phenomenological closure provides no mechanism to compute them.
**action_label:** github:superconductivity_electron_liquids::action::_anon_action_001
**pattern:** derivation
**gaia:** {'provenance': {'referenced_claims': ['mu_star_phenomenological']}}

### github:superconductivity_electron_liquids::_anon_002

**QID:** `github:superconductivity_electron_liquids::_anon_002`
**Type:** claim
**Role:** orphaned
**Content:** derive warrants Traditional electron-phonon superconductivity theory uses the McMillan (or Allen-Dynes) formula, with the electron-phonon coupling constant $\lambda$ and Coulomb pseudopotential $\mu^*$ as inputs to predict the superconducting transition temperature $T_c$. Since $\mu^*$ cannot be reliably computed from first principles, it is typically assigned an empirical value $\mu^* \in [0.1, 0.2]$. For materials with $T_c$ in the sub-kelvin range, the exponential sensitivity $T_c \propto \exp(-1/g)$ to $\mu^*$ causes this uncertainty to span several orders of magnitude in the predicted $T_c$, destroying predictive power.
**Belief:** 0.50
**generated:** True
**helper_kind:** implication_warrant
**review:** True
**relation:** {'type': 'derive', 'given': ['github:superconductivity_electron_liquids::me_downfolding_is_phenomenological'], 'conclusion': 'github:superconductivity_electron_liquids::phenomenological_me_theory'}
**warrant:** Given the phenomenological character of the downfolding (@me_downfolding_is_phenomenological), the resulting McMillan / Allen-Dynes formula inherits the uncertainty in $\mu^*$. The dimensionless coupling $g = \lambda - \mu^*(1 + 0.62\lambda)$ appears exponentially in $T_c \propto \exp(-1/g)$, so the empirical $\mu^*$ range $[0.1, 0.2]$ amplifies into orders-of-magnitude uncertainty in predicted $T_c$ for sub-Kelvin superconductors — destroying predictive power precisely where first-principles $\mu^*$ would matter most.
**action_label:** github:superconductivity_electron_liquids::action::_anon_action_002
**pattern:** derivation
**gaia:** {'provenance': {'referenced_claims': ['me_downfolding_is_phenomenological']}}

### rpa_predicts_attractive_mu

**QID:** `github:superconductivity_electron_liquids::rpa_predicts_attractive_mu`
**Type:** claim
**Role:** independent
**Content:** When treating the dynamically screened Coulomb interaction within the random phase approximation (RPA), the predicted $\mu^* < 0$ (i.e. the Coulomb effect becomes net attractive in the Cooper channel) for Wigner-Seitz radius $r_s \gtrsim 2$ ($r_s$ is proportional to the ratio of electron spacing to Bohr radius, measuring the ratio of Coulomb interaction to kinetic energy). However, RPA neglects beyond-RPA effects such as vertex corrections and self-energy renormalization for $r_s \gtrsim 1$, making its predictions unreliable in this density regime and inconsistent with extensive experimental evidence.
**Belief:** 0.35
**Referenced by:** unknown -> `github:superconductivity_electron_liquids::rpa_vs_vdiagmc`

### dfpt_computes_lambda

**QID:** `github:superconductivity_electron_liquids::dfpt_computes_lambda`
**Type:** claim
**Role:** independent
**Content:** Density functional perturbation theory (DFPT) computes the electron-phonon coupling constant $\lambda$ (a dimensionless parameter quantifying the phonon-mediated attraction strength at the Fermi surface) via the linear response of the Kohn-Sham ground-state energy to lattice distortions. DFPT has been validated for weakly correlated superconductors but its accuracy for strongly correlated systems is unknown.
**Belief:** 0.47
**Referenced by:** deduction -> `github:superconductivity_electron_liquids::tc_al_phenomenological`; deduction -> `github:superconductivity_electron_liquids::tc_zn_phenomenological`; deduction -> `github:superconductivity_electron_liquids::tc_li_phenomenological`

### tc_al_experimental

**QID:** `github:superconductivity_electron_liquids::tc_al_experimental`
**Type:** claim
**Role:** orphaned
**Content:** The experimental superconducting transition temperature of aluminum (Al) is $T_c^{\mathrm{exp}} = 1.2$ K.
**Prior:** 0.99
**Belief:** 0.99
**prior_records:** [{'value': 0.99, 'source_id': 'experimental_measurement', 'justification': 'Aluminium T_c = 1.2 K is a well-established laboratory value; the 1% residual reserves probability for systematic / structural qualifications not formalized in this package.'}]
**prior:** 0.99
**prior_justification:** Aluminium T_c = 1.2 K is a well-established laboratory value; the 1% residual reserves probability for systematic / structural qualifications not formalized in this package.
**prior_source_id:** experimental_measurement

### tc_li_experimental

**QID:** `github:superconductivity_electron_liquids::tc_li_experimental`
**Type:** claim
**Role:** background
**Content:** The experimental superconducting transition temperature of lithium (Li) is $T_c^{\mathrm{exp}} \approx 4 \times 10^{-4}$ K (0.4 mK). This measurement corresponds to the 9R crystal structure.
**Belief:** 0.50

### tc_zn_experimental

**QID:** `github:superconductivity_electron_liquids::tc_zn_experimental`
**Type:** claim
**Role:** orphaned
**Content:** The experimental superconducting transition temperature of zinc (Zn) is $T_c^{\mathrm{exp}} = 0.875$ K.
**Prior:** 0.99
**Belief:** 0.99
**prior_records:** [{'value': 0.99, 'source_id': 'experimental_measurement', 'justification': 'Zinc T_c = 0.875 K is a well-established laboratory value; the 1% residual reserves probability for systematic qualifications.'}]
**prior:** 0.99
**prior_justification:** Zinc T_c = 0.875 K is a well-established laboratory value; the 1% residual reserves probability for systematic qualifications.
**prior_source_id:** experimental_measurement

### li_crystal_structure_at_low_t

**QID:** `github:superconductivity_electron_liquids::li_crystal_structure_at_low_t`
**Type:** claim
**Role:** independent
**Content:** Lithium's crystal structure at sub-kelvin temperatures is debated. Measurements consistent with the 9R polytype are typically cited, but the structural identification at the sample where $T_c \approx 4 \times 10^{-4}$ K was inferred is not independently established. The Tc(Li) experimental input therefore assumes 9R is the relevant phase.
**Belief:** 0.33
**Referenced by:** deduction -> `github:superconductivity_electron_liquids::tc_li_observation_binding`

### li_is_superconducting

**QID:** `github:superconductivity_electron_liquids::li_is_superconducting`
**Type:** claim
**Role:** independent
**Content:** Li in the 9R structure undergoes a genuine bulk superconducting transition at $T_c \approx 4 \times 10^{-4}$ K. The Cooper pair condensate is bulk (not filamentary or surface), and the observed resistive anomaly reflects this true SC state.
**Belief:** 0.71
**Referenced by:** infer -> `github:superconductivity_electron_liquids::li_zero_resistance_observed`; infer -> `github:superconductivity_electron_liquids::li_meissner_observed`; deduction -> `github:superconductivity_electron_liquids::tc_li_predicted`; deduction -> `github:superconductivity_electron_liquids::tc_li_phenomenological`; unknown -> `github:superconductivity_electron_liquids::_anon_003`

### li_anomaly_not_sc

**QID:** `github:superconductivity_electron_liquids::li_anomaly_not_sc`
**Type:** claim
**Role:** independent
**Content:** The resistive anomaly observed in Li 9R at $\sim 0.4$ mK is *not* a bulk superconducting transition: it could be filamentary SC on grain boundaries / impurity phases, surface superconductivity, measurement / contact artifacts amplified at sub-mK temperatures, a structural transition that mimics a SC signature, or another phenomenon of the extreme sub-mK regime.
**Belief:** 0.29
**Referenced by:** unknown -> `github:superconductivity_electron_liquids::_anon_003`

### github:superconductivity_electron_liquids::_anon_003

**QID:** `github:superconductivity_electron_liquids::_anon_003`
**Type:** claim
**Role:** structural
**Content:** exactly one of Li in the 9R structure undergoes a genuine bulk superconducting transition at $T_c \approx 4 \times 10^{-4}$ K. The Cooper pair condensate is bulk (not filamentary or surface), and the observed resistive anomaly reflects this true SC state. and The resistive anomaly observed in Li 9R at $\sim 0.4$ mK is *not* a bulk superconducting transition: it could be filamentary SC on grain boundaries / impurity phases, surface superconductivity, measurement / contact artifacts amplified at sub-mK temperatures, a structural transition that mimics a SC signature, or another phenomenon of the extreme sub-mK regime. is true.
**Belief:** 1.00
**generated:** True
**helper_kind:** complement_result
**review:** True

### li_zero_resistance_observed

**QID:** `github:superconductivity_electron_liquids::li_zero_resistance_observed`
**Type:** claim
**Role:** derived
**Content:** Resistivity of the Li 9R sample drops sharply to below the measurement noise floor at $T \approx 0.4$ mK (Schwarz et al. and follow-ups).
**Prior:** 1.00
**Belief:** 1.00
**Derived from:** infer
**Premises:** `github:superconductivity_electron_liquids::li_is_superconducting`
**prior:** 0.999
**supported_by:** [{'action_label': 'github:superconductivity_electron_liquids::action::li_zero_r_observation', 'pattern': 'observation', 'warrants': ['github:superconductivity_electron_liquids::_anon_004'], 'background': ['github:superconductivity_electron_liquids::li_crystal_structure_at_low_t'], 'rationale': 'The resistive drop is the actual laboratory observation cited as evidence for SC in Li at sub-mK temperatures. Pin via observe().'}]

### github:superconductivity_electron_liquids::_anon_004

**QID:** `github:superconductivity_electron_liquids::_anon_004`
**Type:** claim
**Role:** orphaned
**Content:** observe warrants Resistivity of the Li 9R sample drops sharply to below the measurement noise floor at $T \approx 0.4$ mK (Schwarz et al. and follow-ups).
**Belief:** 0.50
**generated:** True
**helper_kind:** implication_warrant
**review:** True
**relation:** {'type': 'observe', 'given': [], 'conclusion': 'github:superconductivity_electron_liquids::li_zero_resistance_observed'}
**warrant:** The resistive drop is the actual laboratory observation cited as evidence for SC in Li at sub-mK temperatures. Pin via observe().
**action_label:** github:superconductivity_electron_liquids::action::li_zero_r_observation
**pattern:** observation

### github:superconductivity_electron_liquids::_anon_005

**QID:** `github:superconductivity_electron_liquids::_anon_005`
**Type:** claim
**Role:** orphaned
**Content:** Resistivity of the Li 9R sample drops sharply to below the measurement noise floor at $T \approx 0.4$ mK (Schwarz et al. and follow-ups). statistically supports Li in the 9R structure undergoes a genuine bulk superconducting transition at $T_c \approx 4 \times 10^{-4}$ K. The Cooper pair condensate is bulk (not filamentary or surface), and the observed resistive anomaly reflects this true SC state..
**Belief:** 0.50
**generated:** True
**helper_kind:** likelihood
**review:** True
**relation:** {'type': 'infer', 'hypothesis': 'github:superconductivity_electron_liquids::li_is_superconducting', 'evidence': 'github:superconductivity_electron_liquids::li_zero_resistance_observed', 'p_e_given_h': 0.9, 'p_e_given_not_h': 0.3}
**action_label:** github:superconductivity_electron_liquids::action::li_zero_r_supports_sc
**pattern:** inference

### li_meissner_observed

**QID:** `github:superconductivity_electron_liquids::li_meissner_observed`
**Type:** claim
**Role:** derived
**Content:** Meissner-Ochsenfeld expulsion of magnetic flux is observed for the Li 9R sample at sub-K temperatures, confirming bulk SC.
**Belief:** 0.71
**Derived from:** infer
**Premises:** `github:superconductivity_electron_liquids::li_is_superconducting`

### github:superconductivity_electron_liquids::_anon_006

**QID:** `github:superconductivity_electron_liquids::_anon_006`
**Type:** claim
**Role:** orphaned
**Content:** Meissner-Ochsenfeld expulsion of magnetic flux is observed for the Li 9R sample at sub-K temperatures, confirming bulk SC. statistically supports Li in the 9R structure undergoes a genuine bulk superconducting transition at $T_c \approx 4 \times 10^{-4}$ K. The Cooper pair condensate is bulk (not filamentary or surface), and the observed resistive anomaly reflects this true SC state..
**Belief:** 0.50
**generated:** True
**helper_kind:** likelihood
**review:** True
**relation:** {'type': 'infer', 'hypothesis': 'github:superconductivity_electron_liquids::li_is_superconducting', 'evidence': 'github:superconductivity_electron_liquids::li_meissner_observed', 'p_e_given_h': 0.99, 'p_e_given_not_h': 0.005}
**action_label:** github:superconductivity_electron_liquids::action::li_meissner_would_support_sc
**pattern:** inference

### li_meissner_inquiry

**QID:** `github:superconductivity_electron_liquids::li_meissner_inquiry`
**Type:** question
**Role:** question
**Content:** Has the Meissner-Ochsenfeld experiment been performed on the Li 9R sample at sub-K temperatures? This is the gold-standard discriminator between genuine bulk SC and the various non-SC explanations (BF ~200x if positive; near-decisive ruling-out if null). The package currently records no public data on this measurement.

### main_question

**QID:** `github:superconductivity_electron_liquids::main_question`
**Type:** question
**Role:** question
**Content:** Can the Coulomb pseudopotential $\mu^*$ (the parameter quantifying effective electron-electron repulsion in the Cooper pairing channel) be computed from first principles with controlled accuracy, and can this yield quantitative predictions of the superconducting transition temperature $T_c$ for simple metals (e.g. Al, Li, Na, Mg)?
