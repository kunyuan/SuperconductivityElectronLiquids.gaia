# Module: s6_superconductors

### aluminum_parameters

**QID:** `github:superconductivity_electron_liquids::aluminum_parameters`
**Type:** setting
**Role:** setting
**Content:** Aluminum (Al): FCC crystal structure, $r_s = 2.07$, experimental Debye temperature $\Theta_D \approx 428$ K, DFPT electron-phonon coupling $\lambda \approx 0.44$, logarithmic phonon frequency $\omega_{\mathrm{log}} \approx 300$ K.

### lithium_parameters

**QID:** `github:superconductivity_electron_liquids::lithium_parameters`
**Type:** setting
**Role:** setting
**Content:** Lithium (Li): BCC (or 9R at low $T$) crystal structure, $r_s = 3.25$, experimental Debye temperature $\Theta_D \approx 344$ K, DFPT electron-phonon coupling $\lambda \approx 0.41$ (BCC), logarithmic phonon frequency $\omega_{\mathrm{log}} \approx 250$ K. Crystal structure at sub-kelvin temperatures remains debated.

### sodium_parameters

**QID:** `github:superconductivity_electron_liquids::sodium_parameters`
**Type:** setting
**Role:** setting
**Content:** Sodium (Na): BCC crystal structure, $r_s = 3.93$, experimental Debye temperature $\Theta_D \approx 158$ K, DFPT electron-phonon coupling $\lambda \approx 0.18$, logarithmic phonon frequency $\omega_{\mathrm{log}} \approx 120$ K. No superconductivity observed down to mK temperatures.

### magnesium_parameters

**QID:** `github:superconductivity_electron_liquids::magnesium_parameters`
**Type:** setting
**Role:** setting
**Content:** Magnesium (Mg): HCP crystal structure, $r_s = 2.66$, experimental Debye temperature $\Theta_D \approx 400$ K, DFPT electron-phonon coupling $\lambda \approx 0.26$, logarithmic phonon frequency $\omega_{\mathrm{log}} \approx 290$ K. No superconductivity observed down to mK temperatures.

### zinc_parameters

**QID:** `github:superconductivity_electron_liquids::zinc_parameters`
**Type:** setting
**Role:** setting
**Content:** Zinc (Zn): HCP crystal structure, $r_s = 2.31$, experimental Debye temperature $\Theta_D \approx 327$ K, DFPT electron-phonon coupling $\lambda \approx 0.43$, logarithmic phonon frequency $\omega_{\mathrm{log}} \approx 200$ K.

### simple_metals_weak_lattice

**QID:** `github:superconductivity_electron_liquids::simple_metals_weak_lattice`
**Type:** claim
**Role:** background
**Content:** Simple metals (Al, Li, Na, Mg, Zn) have weak lattice effects in the Coulomb pseudopotential: the difference between the crystalline $\mu^*$ and the UEG $\mu^*$ at the same $r_s$ is small (a few percent) because the nearly-free-electron character of these metals means the Fermi surface is approximately spherical and the electronic structure is well described by the homogeneous electron gas with minor crystal-field perturbations.
**Prior:** 0.90
**Belief:** 0.90

### ueg_pseudopotential_parameterization

**QID:** `github:superconductivity_electron_liquids::ueg_pseudopotential_parameterization`
**Type:** claim
**Role:** independent
**Content:** The UEG Coulomb pseudopotential $\mu_{E_F}(r_s)$ computed by vDiagMC can be parameterized as a smooth function of $r_s$ and mapped onto real materials by using the material's effective $r_s$ (determined from the valence electron density). Combined with the BTS relation to run $\mu_{E_F}$ down to the Debye scale, this provides $\mu^*(r_s)$ for any simple metal without additional adjustable parameters.
**Prior:** 0.85
**Belief:** 0.83
**Referenced by:** noisy_and -> `github:superconductivity_electron_liquids::mu_available_for_simple_metals`; infer -> `github:superconductivity_electron_liquids::ab_initio_workflow`

### ab_initio_workflow

**QID:** `github:superconductivity_electron_liquids::ab_initio_workflow`
**Type:** claim
**Role:** derived
**Content:** The complete ab initio workflow for predicting $T_c$ of simple metals: (1) compute $\mu_{E_F}$ from the UEG four-point vertex via vDiagMC, (2) map to the material's $r_s$ and run down to $\mu^*$ via the BTS relation, (3) obtain $\lambda$ from DFPT, (4) solve the downfolded Eliashberg equations (or use the PCF extrapolation) to predict $T_c$. All inputs are from first principles; no adjustable parameters remain.
**Belief:** 0.99
**Derived from:** deduction
**Premises:** `github:superconductivity_electron_liquids::downfolded_bse`, `github:superconductivity_electron_liquids::mu_available_for_simple_metals`, `github:superconductivity_electron_liquids::dfpt_reliable_for_simple_metals`
**Derived from:** infer
**Premises:** `github:superconductivity_electron_liquids::downfolded_bse`, `github:superconductivity_electron_liquids::mu_vdiagmc_values`, `github:superconductivity_electron_liquids::dfpt_reliable_for_simple_metals`, `github:superconductivity_electron_liquids::ueg_pseudopotential_parameterization`
**Referenced by:** noisy_and -> `github:superconductivity_electron_liquids::tc_al_predicted`; noisy_and -> `github:superconductivity_electron_liquids::tc_zn_predicted`; noisy_and -> `github:superconductivity_electron_liquids::tc_li_predicted`; noisy_and -> `github:superconductivity_electron_liquids::al_pressure_transition`; noisy_and -> `github:superconductivity_electron_liquids::tc_mg_na_near_qpt`

### mu_available_for_simple_metals

**QID:** `github:superconductivity_electron_liquids::mu_available_for_simple_metals`
**Type:** claim
**Role:** derived
**Content:** For simple metals, the Coulomb pseudopotential $\mu^*$ can be obtained from first principles without adjustable parameters: the vDiagMC-computed $\mu_{E_F}(r_s)$ for the uniform electron gas is mapped to real materials via material-specific $r_s$ and band mass, then scaled to the Debye frequency via the BTS renormalization relation.
**Belief:** 0.40
**Derived from:** noisy_and
**Premises:** `github:superconductivity_electron_liquids::ueg_pseudopotential_parameterization`, `github:superconductivity_electron_liquids::mu_vdiagmc_values`
**Referenced by:** deduction -> `github:superconductivity_electron_liquids::ab_initio_workflow`

### tc_al_predicted

**QID:** `github:superconductivity_electron_liquids::tc_al_predicted`
**Type:** claim
**Role:** derived
**Content:** The ab initio predicted superconducting transition temperature of aluminum is $T_c^{\mathrm{th}} = 1.1 \pm 0.3$ K, in good agreement with the experimental value $T_c^{\mathrm{exp}} = 1.2$ K. The first-principles $\mu^*(\mathrm{Al}) \approx 0.11$ is obtained from the vDiagMC $\mu_{E_F}$ at $r_s = 2.07$ via BTS renormalization.
**Belief:** 0.93
**Derived from:** noisy_and
**Premises:** `github:superconductivity_electron_liquids::ab_initio_workflow`
**Derived from:** abduction
**Premises:** `github:superconductivity_electron_liquids::tc_al_experimental`, `github:superconductivity_electron_liquids::tc_al_phenomenological`

### tc_zn_predicted

**QID:** `github:superconductivity_electron_liquids::tc_zn_predicted`
**Type:** claim
**Role:** derived
**Content:** The ab initio predicted superconducting transition temperature of zinc is $T_c^{\mathrm{th}} = 0.7 \pm 0.3$ K, consistent with the experimental value $T_c^{\mathrm{exp}} = 0.875$ K. The first-principles $\mu^*(\mathrm{Zn}) \approx 0.12$ is obtained from the vDiagMC $\mu_{E_F}$ at $r_s = 2.31$.
**Belief:** 0.93
**Derived from:** noisy_and
**Premises:** `github:superconductivity_electron_liquids::ab_initio_workflow`
**Derived from:** abduction
**Premises:** `github:superconductivity_electron_liquids::tc_zn_experimental`, `github:superconductivity_electron_liquids::tc_zn_phenomenological`

### tc_li_predicted

**QID:** `github:superconductivity_electron_liquids::tc_li_predicted`
**Type:** claim
**Role:** derived
**Content:** The ab initio predicted superconducting transition temperature of lithium is $T_c^{\mathrm{th}} \lesssim 10^{-3}$ K (sub-millikelvin), consistent with the experimental observation $T_c^{\mathrm{exp}} \approx 4 \times 10^{-4}$ K. The large $\mu^*(\mathrm{Li}) \approx 0.16$ from $r_s = 3.25$ almost completely cancels the phonon-mediated attraction $\lambda \approx 0.41$, pushing $T_c$ to extremely low temperatures.
**Belief:** 0.96
**Derived from:** noisy_and
**Premises:** `github:superconductivity_electron_liquids::ab_initio_workflow`
**Derived from:** abduction
**Premises:** `github:superconductivity_electron_liquids::tc_li_experimental`, `github:superconductivity_electron_liquids::tc_li_phenomenological`

### al_pressure_transition

**QID:** `github:superconductivity_electron_liquids::al_pressure_transition`
**Type:** claim
**Role:** derived
**Content:** Under hydrostatic pressure, the ab initio framework predicts that aluminum's superconducting $T_c$ initially increases as pressure stiffens phonon frequencies (increasing $\omega_{\mathrm{log}}$) while $\lambda$ and $\mu^*$ change modestly, before eventually decreasing at very high pressures when $\lambda$ is suppressed. This non-monotonic behavior is consistent with experimental pressure studies.
**Belief:** 0.79
**Derived from:** noisy_and
**Premises:** `github:superconductivity_electron_liquids::ab_initio_workflow`

### tc_mg_na_near_qpt

**QID:** `github:superconductivity_electron_liquids::tc_mg_na_near_qpt`
**Type:** claim
**Role:** derived
**Content:** The ab initio framework predicts that sodium and magnesium have extremely low or vanishing $T_c$: for Na ($r_s = 3.93$, $\lambda \approx 0.18$), the large $\mu^*$ exceeds the weak electron-phonon coupling, giving net repulsion in the pairing channel and no superconductivity. For Mg ($r_s = 2.66$, $\lambda \approx 0.26$), $T_c$ is in the sub-nanokelvin regime. Both materials are near the quantum phase transition between superconducting and non-superconducting ground states, where $T_c$ varies exponentially with small parameter changes.
**Belief:** 0.79
**Derived from:** noisy_and
**Premises:** `github:superconductivity_electron_liquids::ab_initio_workflow`
