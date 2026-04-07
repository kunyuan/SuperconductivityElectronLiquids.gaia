# Module: s6_superconductors

### aluminum_parameters

**QID:** `github:superconductivity_electron_liquids::aluminum_parameters`
**Type:** setting
**Role:** setting
**Content:** Aluminum (Al): FCC crystal structure, $r_s = 2.07$, band mass $m_b = 1.05$, DFPT electron-phonon coupling $\lambda = 0.44$, logarithmic phonon frequency $\omega_{\mathrm{log}} = 320$ K, Fermi temperature $T_F = 1.3 \times 10^5$ K.

### lithium_parameters

**QID:** `github:superconductivity_electron_liquids::lithium_parameters`
**Type:** setting
**Role:** setting
**Content:** Lithium (Li): 9R crystal structure at low $T$ (also studied in HCP). 9R parameters: $r_s = 3.25$, $m_b = 1.75$, $\lambda = 0.34$, $\omega_{\mathrm{log}} = 242$ K, $T_F = 4.0 \times 10^4$ K. HCP parameters: $r_s = 3.19$, $m_b = 1.4$, $\lambda = 0.37$, $\omega_{\mathrm{log}} = 243$ K, $T_F = 4.1 \times 10^4$ K. Crystal structure at sub-kelvin temperatures remains debated.

### sodium_parameters

**QID:** `github:superconductivity_electron_liquids::sodium_parameters`
**Type:** setting
**Role:** setting
**Content:** Sodium (Na): BCC crystal structure, $r_s = 3.96$, band mass $m_b = 1.0$, DFPT electron-phonon coupling $\lambda = 0.2$, logarithmic phonon frequency $\omega_{\mathrm{log}} = 127$ K, Fermi temperature $T_F = 4.2 \times 10^4$ K. No superconductivity observed down to mK temperatures.

### magnesium_parameters

**QID:** `github:superconductivity_electron_liquids::magnesium_parameters`
**Type:** setting
**Role:** setting
**Content:** Magnesium (Mg): HCP crystal structure, $r_s = 2.66$, band mass $m_b = 1.02$, DFPT electron-phonon coupling $\lambda = 0.24$, logarithmic phonon frequency $\omega_{\mathrm{log}} = 269$ K, Fermi temperature $T_F = 8.0 \times 10^4$ K. No superconductivity observed down to mK temperatures.

### zinc_parameters

**QID:** `github:superconductivity_electron_liquids::zinc_parameters`
**Type:** setting
**Role:** setting
**Content:** Zinc (Zn): HCP crystal structure, $r_s = 2.90$, band mass $m_b = 1.0$, DFPT electron-phonon coupling $\lambda = 0.502$, logarithmic phonon frequency $\omega_{\mathrm{log}} = 111$ K, Fermi temperature $T_F = 1.21 \times 10^5$ K.

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
**figure:** artifacts/images/13_0.jpg
**caption:** Fig. 9 | Proposed ab initio framework for electron-phonon SC beyond the weak correlation limit, showing computational pathway from fundamental parameters through correlated electrons and lattice vibrations to superconducting properties.
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
**Content:** The ab initio predicted superconducting transition temperature of aluminum is $T_c^{\mathrm{EFT}} = 0.96$ K, in good agreement with the experimental value $T_c^{\mathrm{exp}} = 1.2$ K. The first-principles $\mu^*(\mathrm{Al}) = 0.13$ is obtained from the vDiagMC $\mu_{E_F}$ at $r_s = 2.07$ (with band mass $m_b = 1.05$) via BTS renormalization.
**Belief:** 0.93
**Derived from:** noisy_and
**Premises:** `github:superconductivity_electron_liquids::ab_initio_workflow`
**Derived from:** abduction
**Premises:** `github:superconductivity_electron_liquids::tc_al_experimental`, `github:superconductivity_electron_liquids::tc_al_phenomenological`
**figure:** artifacts/images/14_0.jpg
**caption:** Fig. 10 | Pressure dependence of the superconducting critical temperature in aluminum. EFT results (squares) compared with experimental data from Levy et al. and Gubser et al.

### tc_zn_predicted

**QID:** `github:superconductivity_electron_liquids::tc_zn_predicted`
**Type:** claim
**Role:** derived
**Content:** The ab initio predicted superconducting transition temperature of zinc is $T_c^{\mathrm{EFT}} = 0.874$ K, in excellent agreement with the experimental value $T_c^{\mathrm{exp}} = 0.875$ K. The first-principles $\mu^*(\mathrm{Zn}) = 0.12$ is obtained from the vDiagMC $\mu_{E_F}$ at $r_s = 2.90$ (with band mass $m_b = 1.0$) via BTS renormalization.
**Belief:** 0.93
**Derived from:** noisy_and
**Premises:** `github:superconductivity_electron_liquids::ab_initio_workflow`
**Derived from:** abduction
**Premises:** `github:superconductivity_electron_liquids::tc_zn_experimental`, `github:superconductivity_electron_liquids::tc_zn_phenomenological`
**figure:** artifacts/images/15_0.jpg
**caption:** Fig. 11 | Effective BCS coupling strength for simple metals. E-ph couplings from DFPT; pseudopotentials from vDiagMC. Includes Al, Zn, Li, Na, Mg predictions.

### tc_li_predicted

**QID:** `github:superconductivity_electron_liquids::tc_li_predicted`
**Type:** claim
**Role:** derived
**Content:** The ab initio predicted superconducting transition temperature of lithium (9R structure) is $T_c^{\mathrm{EFT}} = 5 \times 10^{-3}$ K, within an order of magnitude of the experimental observation $T_c^{\mathrm{exp}} \approx 4 \times 10^{-4}$ K. The large $\mu^*(\mathrm{Li}) = 0.18$ from $r_s = 3.25$ (with band mass $m_b = 1.75$) almost completely cancels the phonon-mediated attraction $\lambda = 0.34$, pushing $T_c$ to extremely low temperatures. The HCP structure gives $T_c^{\mathrm{EFT}} = 0.03$ K with $\mu^* = 0.17$ and $\lambda = 0.37$.
**Belief:** 0.96
**Derived from:** noisy_and
**Premises:** `github:superconductivity_electron_liquids::ab_initio_workflow`
**Derived from:** abduction
**Premises:** `github:superconductivity_electron_liquids::tc_li_experimental`, `github:superconductivity_electron_liquids::tc_li_phenomenological`
**figure:** artifacts/images/15_0.jpg
**caption:** Fig. 11 | Effective BCS coupling strength for simple metals. E-ph couplings from DFPT; pseudopotentials from vDiagMC. Includes Al, Zn, Li, Na, Mg predictions.

### al_pressure_transition

**QID:** `github:superconductivity_electron_liquids::al_pressure_transition`
**Type:** claim
**Role:** derived
**Content:** Under hydrostatic pressure, the ab initio framework predicts that aluminum's superconducting $T_c$ monotonically decreases, consistent with experimental data up to 6 GPa. The framework predicts that superconductivity in Al vanishes at approximately 60 GPa; at 20 GPa, $T_c$ is already suppressed below 1 mK.
**Belief:** 0.79
**Derived from:** noisy_and
**Premises:** `github:superconductivity_electron_liquids::ab_initio_workflow`
**figure:** artifacts/images/14_0.jpg
**caption:** Fig. 10 | Pressure dependence of the superconducting critical temperature in aluminum. EFT results (squares) compared with experimental data from Levy et al. and Gubser et al.

### tc_mg_na_near_qpt

**QID:** `github:superconductivity_electron_liquids::tc_mg_na_near_qpt`
**Type:** claim
**Role:** derived
**Content:** The ab initio framework predicts that sodium and magnesium have extremely low or vanishing $T_c$: for Na ($r_s = 3.96$, $\lambda = 0.2$, $\mu^* = 0.15$), the Coulomb repulsion nearly cancels the weak electron-phonon coupling, giving $T_c^{\mathrm{EFT}} = 2 \times 10^{-13}$ K (effectively no superconductivity). For Mg ($r_s = 2.66$, $\lambda = 0.24$, $\mu^* = 0.14$), $T_c^{\mathrm{EFT}} = 5 \times 10^{-5}$ K. Both materials are near the quantum phase transition between superconducting and non-superconducting ground states, where $T_c$ varies exponentially with small parameter changes.
**Belief:** 0.79
**Derived from:** noisy_and
**Premises:** `github:superconductivity_electron_liquids::ab_initio_workflow`
**figure:** artifacts/images/15_0.jpg
**caption:** Fig. 11 | Effective BCS coupling strength for simple metals. Na and Mg appear near the origin, indicating near-cancellation of pairing interaction.
