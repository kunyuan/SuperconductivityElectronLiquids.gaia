# Module: motivation

### bcs_theory

**QID:** `github:superconductivity_electron_liquids::bcs_theory`
**Type:** setting
**Role:** setting
**Content:** Bardeen-Cooper-Schrieffer (BCS) theory: phonon-mediated electron-electron attraction leads to Cooper pairing instability at the Fermi surface, providing the fundamental framework for understanding conventional superconductors.

### adiabatic_approx

**QID:** `github:superconductivity_electron_liquids::adiabatic_approx`
**Type:** claim
**Role:** independent
**Content:** In conventional metals, the typical phonon frequency (Debye frequency $\omega_D$) is much smaller than the electron Fermi energy $E_F$, i.e. $\omega_D / E_F \ll 1$ (adiabatic approximation). This energy-scale separation has three key consequences: (i) electrons adiabatically adjust to ionic motion, (ii) the electron-ion coupling can be linearized, and (iii) the space-time scale separation between electron and phonon physics permits a controlled effective field theory (EFT) treatment.
**Prior:** 0.95
**Belief:** 0.90
**Referenced by:** deduction -> `github:superconductivity_electron_liquids::me_framework`

### me_framework

**QID:** `github:superconductivity_electron_liquids::me_framework`
**Type:** claim
**Role:** derived
**Content:** Migdal-Eliashberg (ME) theory provides a rigorous treatment of the dynamic electron-phonon interaction. Under the adiabatic condition $\omega_D / E_F \ll 1$, Migdal's theorem guarantees that phonon vertex corrections are suppressed at $O(\omega_D/E_F)$, allowing the electron-phonon self-energy to be truncated at the self-consistent Fock diagram level. This justifies the ME formalism as a controlled low-energy theory for electron-phonon superconductors.
**Belief:** 0.95
**Derived from:** deduction
**Premises:** `github:superconductivity_electron_liquids::adiabatic_approx`
**figure:** artifacts/images/4_0.jpg
**caption:** Fig. 1 | Normal component of the electron self-energy approximated by the self-consistent Fock diagram with the phonon-mediated e-e interaction W^ph.
**Referenced by:** deduction -> `github:superconductivity_electron_liquids::bse_kernel_decomposition`

### bts_renormalization

**QID:** `github:superconductivity_electron_liquids::bts_renormalization`
**Type:** claim
**Role:** independent
**Content:** The Bogoliubov-Tolmachev-Shirkov (BTS) renormalization relation connects the Coulomb pseudopotential $\mu_{\omega_c}$ (a dimensionless parameter describing the effective electron-electron repulsion strength in the pairing channel) defined at different energy cutoff scales $\omega_c$: $\mu_{\omega_c} = \mu_{\omega_c'} / (1 + \mu_{\omega_c'} \ln(\omega_c'/\omega_c))$. This relation ensures that physical observables do not depend on the choice of the arbitrary cutoff scale.
**Prior:** 0.95
**Belief:** 0.99
**Referenced by:** unknown -> `github:superconductivity_electron_liquids::bts_microscopic_equivalence`

### me_downfolding_is_phenomenological

**QID:** `github:superconductivity_electron_liquids::me_downfolding_is_phenomenological`
**Type:** claim
**Role:** orphaned
**Content:** The downfolding procedure (integrating out high-energy degrees of freedom to obtain a low-energy effective theory) in traditional Migdal-Eliashberg (ME) theory is phenomenological: the Coulomb effect is replaced by a static pseudopotential $\mu^*$, ignoring corrections from Coulomb fluctuations to quasiparticle renormalization and electron-phonon coupling, as well as non-local effects of screening.
**Prior:** 0.95
**Belief:** 0.95

### phenomenological_me_theory

**QID:** `github:superconductivity_electron_liquids::phenomenological_me_theory`
**Type:** claim
**Role:** orphaned
**Content:** Traditional electron-phonon superconductivity theory uses the McMillan (or Allen-Dynes) formula, with the electron-phonon coupling constant $\lambda$ and Coulomb pseudopotential $\mu^*$ as inputs to predict the superconducting transition temperature $T_c$. Since $\mu^*$ cannot be reliably computed from first principles, it is typically assigned an empirical value $\mu^* \in [0.1, 0.2]$. For materials with $T_c$ in the sub-kelvin range, the exponential sensitivity $T_c \propto \exp(-1/g)$ to $\mu^*$ causes this uncertainty to span several orders of magnitude in the predicted $T_c$, destroying predictive power.
**Prior:** 0.95
**Belief:** 0.95

### mu_star_phenomenological

**QID:** `github:superconductivity_electron_liquids::mu_star_phenomenological`
**Type:** claim
**Role:** background
**Content:** Due to the lack of a reliable microscopic calculation, the Coulomb pseudopotential $\mu^*$ (a dimensionless parameter describing the effective Coulomb repulsion strength in the low-energy pairing channel) is typically treated as an adjustable parameter with empirical values in the range 0.1--0.2.
**Prior:** 0.95
**Belief:** 0.95

### rpa_predicts_attractive_mu

**QID:** `github:superconductivity_electron_liquids::rpa_predicts_attractive_mu`
**Type:** claim
**Role:** independent
**Content:** When treating the dynamically screened Coulomb interaction within the random phase approximation (RPA), the predicted $\mu^* < 0$ (i.e. the Coulomb effect becomes net attractive in the Cooper channel) for Wigner-Seitz radius $r_s \gtrsim 2$ ($r_s$ is proportional to the ratio of electron spacing to Bohr radius, measuring the ratio of Coulomb interaction to kinetic energy). However, RPA neglects beyond-RPA effects such as vertex corrections and self-energy renormalization for $r_s \gtrsim 1$, making its predictions unreliable in this density regime and inconsistent with extensive experimental evidence.
**Prior:** 0.50
**Belief:** 0.25
**Referenced by:** unknown -> `github:superconductivity_electron_liquids::rpa_vs_vdiagmc`

### dfpt_computes_lambda

**QID:** `github:superconductivity_electron_liquids::dfpt_computes_lambda`
**Type:** claim
**Role:** background
**Content:** Density functional perturbation theory (DFPT) computes the electron-phonon coupling constant $\lambda$ (a dimensionless parameter quantifying the phonon-mediated attraction strength at the Fermi surface) via the linear response of the Kohn-Sham ground-state energy to lattice distortions. DFPT has been validated for weakly correlated superconductors but its accuracy for strongly correlated systems is unknown.
**Prior:** 0.92
**Belief:** 0.92

### tc_al_experimental

**QID:** `github:superconductivity_electron_liquids::tc_al_experimental`
**Type:** claim
**Role:** independent
**Content:** The experimental superconducting transition temperature of aluminum (Al) is $T_c^{\mathrm{exp}} = 1.2$ K.
**Prior:** 0.99
**Belief:** 1.00
**Referenced by:** abduction -> `github:superconductivity_electron_liquids::tc_al_predicted`

### tc_li_experimental

**QID:** `github:superconductivity_electron_liquids::tc_li_experimental`
**Type:** claim
**Role:** independent
**Content:** The experimental superconducting transition temperature of lithium (Li) is $T_c^{\mathrm{exp}} \approx 4 \times 10^{-4}$ K (0.4 mK). This measurement corresponds to the 9R crystal structure; the crystal structure of lithium at ultra-low temperatures remains controversial.
**Prior:** 0.85
**Belief:** 1.00
**Referenced by:** abduction -> `github:superconductivity_electron_liquids::tc_li_predicted`

### tc_zn_experimental

**QID:** `github:superconductivity_electron_liquids::tc_zn_experimental`
**Type:** claim
**Role:** independent
**Content:** The experimental superconducting transition temperature of zinc (Zn) is $T_c^{\mathrm{exp}} = 0.875$ K.
**Prior:** 0.99
**Belief:** 1.00
**Referenced by:** abduction -> `github:superconductivity_electron_liquids::tc_zn_predicted`

### tc_al_phenomenological

**QID:** `github:superconductivity_electron_liquids::tc_al_phenomenological`
**Type:** claim
**Role:** independent
**Content:** Using the McMillan formula (an empirical formula for $T_c$ based on the electron-phonon coupling constant $\lambda$ and Coulomb pseudopotential $\mu^*$) with the standard value $\mu^* = 0.1$, the predicted superconducting transition temperature of aluminum is $T_c \approx 1.9$ K, while the experimental value is 1.2 K, a deviation of approximately 58%.
**Prior:** 0.35
**Belief:** 0.40
**Referenced by:** abduction -> `github:superconductivity_electron_liquids::tc_al_predicted`

### tc_li_phenomenological

**QID:** `github:superconductivity_electron_liquids::tc_li_phenomenological`
**Type:** claim
**Role:** independent
**Content:** Using the McMillan formula with $\mu^* = 0.1$, the predicted superconducting transition temperature of lithium is $T_c \approx 0.35$ K, while the experimental value is approximately $4 \times 10^{-4}$ K; the theory overestimates by about three orders of magnitude.
**Prior:** 0.10
**Belief:** 0.13
**Referenced by:** abduction -> `github:superconductivity_electron_liquids::tc_li_predicted`

### tc_zn_phenomenological

**QID:** `github:superconductivity_electron_liquids::tc_zn_phenomenological`
**Type:** claim
**Role:** independent
**Content:** Using the McMillan formula with the standard value $\mu^* = 0.1$, the predicted superconducting transition temperature of zinc is $T_c \approx 1.37$ K, while the experimental value is 0.875 K, a deviation of approximately 57%.
**Prior:** 0.35
**Belief:** 0.40
**Referenced by:** abduction -> `github:superconductivity_electron_liquids::tc_zn_predicted`

### main_question

**QID:** `github:superconductivity_electron_liquids::main_question`
**Type:** question
**Role:** question
**Content:** Can the Coulomb pseudopotential $\mu^*$ (the parameter quantifying effective electron-electron repulsion in the Cooper pairing channel) be computed from first principles with controlled accuracy, and can this yield quantitative predictions of the superconducting transition temperature $T_c$ for simple metals (e.g. Al, Li, Na, Mg)?
