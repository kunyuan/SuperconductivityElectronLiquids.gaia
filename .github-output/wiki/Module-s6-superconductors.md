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
**prior:** 0.9
**prior_justification:** Well-supported.

### ueg_pseudopotential_parameterization

**QID:** `github:superconductivity_electron_liquids::ueg_pseudopotential_parameterization`
**Type:** claim
**Role:** independent
**Content:** The UEG Coulomb pseudopotential $\mu_{E_F}(r_s)$ computed by vDiagMC can be parameterized as a smooth function of $r_s$ and mapped onto real materials by using the material's effective $r_s$ (determined from the valence electron density). Combined with the BTS relation to run $\mu_{E_F}$ down to the Debye scale, this provides $\mu^*(r_s)$ for any simple metal without additional adjustable parameters.
**Prior:** 0.85
**Belief:** 0.85
**prior:** 0.85
**prior_justification:** Mapping procedure reasonable; band-mass correction adds uncertainty.
**Referenced by:** support -> `github:superconductivity_electron_liquids::mu_available_for_simple_metals`; infer -> `github:superconductivity_electron_liquids::ab_initio_workflow`

### ab_initio_workflow

**QID:** `github:superconductivity_electron_liquids::ab_initio_workflow`
**Type:** claim
**Role:** derived
**Content:** The complete ab initio workflow for predicting $T_c$ of simple metals: (1) compute $\mu_{E_F}$ from the UEG four-point vertex via vDiagMC, (2) map to the material's $r_s$ and run down to $\mu^*$ via the BTS relation, (3) obtain $\lambda$ from DFPT, (4) solve the downfolded Eliashberg equations (or use the PCF extrapolation) to predict $T_c$. All inputs are from first principles; no adjustable parameters remain.
**Belief:** 0.80
**Derived from:** deduction
**Premises:** `github:superconductivity_electron_liquids::downfolded_bse`, `github:superconductivity_electron_liquids::mu_available_for_simple_metals`, `github:superconductivity_electron_liquids::dfpt_reliable_for_simple_metals`
**Derived from:** infer
**Premises:** `github:superconductivity_electron_liquids::downfolded_bse`, `github:superconductivity_electron_liquids::mu_vdiagmc_values`, `github:superconductivity_electron_liquids::dfpt_reliable_for_simple_metals`, `github:superconductivity_electron_liquids::ueg_pseudopotential_parameterization`
**figure:** artifacts/images/13_0.jpg
**caption:** Fig. 9 | Proposed ab initio framework for electron-phonon SC beyond the weak correlation limit, showing computational pathway from fundamental parameters through correlated electrons and lattice vibrations to superconducting properties.
**gaia:** {'provenance': {'referenced_claims': ['dfpt_reliable_for_simple_metals', 'downfolded_bse', 'mu_available_for_simple_metals']}}
**Referenced by:** support -> `github:superconductivity_electron_liquids::tc_al_predicted`; support -> `github:superconductivity_electron_liquids::tc_zn_predicted`; support -> `github:superconductivity_electron_liquids::tc_li_predicted`; support -> `github:superconductivity_electron_liquids::al_pressure_transition`; support -> `github:superconductivity_electron_liquids::tc_mg_na_near_qpt`

### mu_available_for_simple_metals

**QID:** `github:superconductivity_electron_liquids::mu_available_for_simple_metals`
**Type:** claim
**Role:** derived
**Content:** For simple metals, the Coulomb pseudopotential $\mu^*$ can be obtained from first principles without adjustable parameters: the vDiagMC-computed $\mu_{E_F}(r_s)$ for the uniform electron gas is mapped to real materials via material-specific $r_s$ and band mass, then scaled to the Debye frequency via the BTS renormalization relation.
**Belief:** 0.78
**Derived from:** support
**Premises:** `github:superconductivity_electron_liquids::ueg_pseudopotential_parameterization`, `github:superconductivity_electron_liquids::mu_vdiagmc_values`
**gaia:** {'provenance': {'referenced_claims': ['bts_renormalization', 'mu_vdiagmc_values', 'simple_metals_weak_lattice', 'ueg_pseudopotential_parameterization']}}
**Referenced by:** deduction -> `github:superconductivity_electron_liquids::ab_initio_workflow`

### tc_al_predicted

**QID:** `github:superconductivity_electron_liquids::tc_al_predicted`
**Type:** claim
**Role:** derived
**Content:** The ab initio EFT predicted superconducting transition temperature of aluminum (Al) is 0.96 K. The first-principles mu*(Al) = 0.13 is obtained from the vDiagMC mu_EF at r_s = 2.07 with band mass m_b = 1.05 via BTS renormalization.
**Belief:** 0.84
**Derived from:** support
**Premises:** `github:superconductivity_electron_liquids::ab_initio_workflow`
**figure:** artifacts/images/14_0.jpg
**caption:** Fig. 10 | Pressure dependence of the superconducting critical temperature in aluminum. EFT results (squares) compared with experimental data from Levy et al. and Gubser et al.
**claim_class:** superconductivity_electron_liquids.motivation.TcValue
**gaia:** {'provenance': {'referenced_claims': ['ab_initio_workflow', 'aluminum_parameters']}}
**Referenced by:** likelihood -> `github:superconductivity_electron_liquids::tc_al_abinitio_outperforms_phenomenological`

### tc_zn_predicted

**QID:** `github:superconductivity_electron_liquids::tc_zn_predicted`
**Type:** claim
**Role:** derived
**Content:** The ab initio EFT predicted superconducting transition temperature of zinc (Zn) is 0.874 K. The first-principles mu*(Zn) = 0.12 is obtained from the vDiagMC mu_EF at r_s = 2.90 with band mass m_b = 1.0 via BTS renormalization.
**Belief:** 0.84
**Derived from:** support
**Premises:** `github:superconductivity_electron_liquids::ab_initio_workflow`
**figure:** artifacts/images/15_0.jpg
**caption:** Fig. 11 | Effective BCS coupling strength for simple metals. E-ph couplings from DFPT; pseudopotentials from vDiagMC. Includes Al, Zn, Li, Na, Mg predictions.
**claim_class:** superconductivity_electron_liquids.motivation.TcValue
**gaia:** {'provenance': {'referenced_claims': ['ab_initio_workflow', 'zinc_parameters']}}
**Referenced by:** likelihood -> `github:superconductivity_electron_liquids::tc_zn_abinitio_outperforms_phenomenological`

### tc_li_predicted

**QID:** `github:superconductivity_electron_liquids::tc_li_predicted`
**Type:** claim
**Role:** derived
**Content:** The ab initio EFT predicted superconducting transition temperature of lithium (Li) (9R structure) is 0.005 K. The large mu*(Li) = 0.18 from r_s = 3.25 with band mass m_b = 1.75 almost completely cancels lambda = 0.34, pushing Tc to extremely low temperatures. The HCP structure gives Tc = 0.03 K with mu* = 0.17 and lambda = 0.37.
**Belief:** 0.82
**Derived from:** support
**Premises:** `github:superconductivity_electron_liquids::ab_initio_workflow`
**figure:** artifacts/images/15_0.jpg
**caption:** Fig. 11 | Effective BCS coupling strength for simple metals. E-ph couplings from DFPT; pseudopotentials from vDiagMC. Includes Al, Zn, Li, Na, Mg predictions.
**claim_class:** superconductivity_electron_liquids.motivation.TcValue
**gaia:** {'provenance': {'referenced_claims': ['ab_initio_workflow', 'lithium_parameters']}}
**Referenced by:** likelihood -> `github:superconductivity_electron_liquids::tc_li_abinitio_outperforms_phenomenological`

### al_pressure_transition

**QID:** `github:superconductivity_electron_liquids::al_pressure_transition`
**Type:** claim
**Role:** derived
**Content:** Under hydrostatic pressure, the ab initio framework predicts that aluminum's superconducting $T_c$ monotonically decreases, consistent with experimental data up to 6 GPa. The framework predicts that superconductivity in Al vanishes at approximately 60 GPa; at 20 GPa, $T_c$ is already suppressed below 1 mK.
**Belief:** 0.82
**Derived from:** support
**Premises:** `github:superconductivity_electron_liquids::ab_initio_workflow`
**figure:** artifacts/images/14_0.jpg
**caption:** Fig. 10 | Pressure dependence of the superconducting critical temperature in aluminum. EFT results (squares) compared with experimental data from Levy et al. and Gubser et al.
**gaia:** {'provenance': {'referenced_claims': ['ab_initio_workflow', 'aluminum_parameters']}}

### tc_mg_na_near_qpt

**QID:** `github:superconductivity_electron_liquids::tc_mg_na_near_qpt`
**Type:** claim
**Role:** derived
**Content:** The ab initio framework predicts that sodium and magnesium have extremely low or vanishing $T_c$: for Na ($r_s = 3.96$, $\lambda = 0.2$, $\mu^* = 0.15$), the Coulomb repulsion nearly cancels the weak electron-phonon coupling, giving $T_c^{\mathrm{EFT}} = 2 \times 10^{-13}$ K (effectively no superconductivity). For Mg ($r_s = 2.66$, $\lambda = 0.24$, $\mu^* = 0.14$), $T_c^{\mathrm{EFT}} = 5 \times 10^{-5}$ K. Both materials are near the quantum phase transition between superconducting and non-superconducting ground states, where $T_c$ varies exponentially with small parameter changes.
**Belief:** 0.82
**Derived from:** support
**Premises:** `github:superconductivity_electron_liquids::ab_initio_workflow`
**figure:** artifacts/images/15_0.jpg
**caption:** Fig. 11 | Effective BCS coupling strength for simple metals. Na and Mg appear near the origin, indicating near-cancellation of pairing interaction.
**gaia:** {'provenance': {'referenced_claims': ['ab_initio_workflow', 'magnesium_parameters', 'precursory_cooper_flow', 'sodium_parameters']}}

### tc_al_abinitio_outperforms_phenomenological

**QID:** `github:superconductivity_electron_liquids::tc_al_abinitio_outperforms_phenomenological`
**Type:** claim
**Role:** derived
**Content:** For aluminum, the ab initio EFT prediction explains the observed transition temperature better than the phenomenological McMillan prediction: $T_c^{\mathrm{EFT}} = 0.96$ K is closer to $T_c^{\mathrm{exp}} = 1.2$ K than the phenomenological value $T_c \approx 1.9$ K.
**Belief:** 0.83
**Derived from:** likelihood
**Premises:** `github:superconductivity_electron_liquids::tc_al_experimental`, `github:superconductivity_electron_liquids::tc_al_predicted`, `github:superconductivity_electron_liquids::tc_al_phenomenological`, `github:superconductivity_electron_liquids::tc_al_comparison_valid`, `github:superconductivity_electron_liquids::_anon_005`
**Reasoning:** Use the SciPy-backed Gaussian model-comparison likelihood score.

### tc_al_comparison_valid

**QID:** `github:superconductivity_electron_liquids::tc_al_comparison_valid`
**Type:** claim
**Role:** independent
**Content:** The aluminum comparison uses the same material, the same experimental $T_c$ target, and the same absolute-error criterion for the ab initio and phenomenological predictions.
**Prior:** 0.95
**Belief:** 0.95
**prior:** 0.95
**prior_justification:** Same material and absolute-error comparison criterion.
**Referenced by:** likelihood -> `github:superconductivity_electron_liquids::tc_al_abinitio_outperforms_phenomenological`

### github:superconductivity_electron_liquids::_anon_001

**QID:** `github:superconductivity_electron_liquids::_anon_001`
**Type:** claim
**Role:** independent
**Content:** The argument observed of Python function gaia.std.likelihood.gaussian_model_comparison_log_lr_claim is 1.2.
**Prior:** 1.00
**Belief:** 1.00
**generated:** True
**helper_kind:** compute_argument
**prior:** 0.999
**claim_class:** gaia.lang.dsl.claim_classes.ComputedArgument
**kind:** compute_argument
**Referenced by:** compute -> `github:superconductivity_electron_liquids::_anon_005`

### github:superconductivity_electron_liquids::_anon_002

**QID:** `github:superconductivity_electron_liquids::_anon_002`
**Type:** claim
**Role:** independent
**Content:** The argument candidate_mean of Python function gaia.std.likelihood.gaussian_model_comparison_log_lr_claim is 0.96.
**Prior:** 1.00
**Belief:** 1.00
**generated:** True
**helper_kind:** compute_argument
**prior:** 0.999
**claim_class:** gaia.lang.dsl.claim_classes.ComputedArgument
**kind:** compute_argument
**Referenced by:** compute -> `github:superconductivity_electron_liquids::_anon_005`

### github:superconductivity_electron_liquids::_anon_003

**QID:** `github:superconductivity_electron_liquids::_anon_003`
**Type:** claim
**Role:** independent
**Content:** The argument baseline_mean of Python function gaia.std.likelihood.gaussian_model_comparison_log_lr_claim is 1.9.
**Prior:** 1.00
**Belief:** 1.00
**generated:** True
**helper_kind:** compute_argument
**prior:** 0.999
**claim_class:** gaia.lang.dsl.claim_classes.ComputedArgument
**kind:** compute_argument
**Referenced by:** compute -> `github:superconductivity_electron_liquids::_anon_005`

### github:superconductivity_electron_liquids::_anon_004

**QID:** `github:superconductivity_electron_liquids::_anon_004`
**Type:** claim
**Role:** independent
**Content:** The argument sigma of Python function gaia.std.likelihood.gaussian_model_comparison_log_lr_claim is 0.3.
**Prior:** 1.00
**Belief:** 1.00
**generated:** True
**helper_kind:** compute_argument
**prior:** 0.999
**claim_class:** gaia.lang.dsl.claim_classes.ComputedArgument
**kind:** compute_argument
**Referenced by:** compute -> `github:superconductivity_electron_liquids::_anon_005`

### github:superconductivity_electron_liquids::_anon_005

**QID:** `github:superconductivity_electron_liquids::_anon_005`
**Type:** claim
**Role:** derived
**Content:** The Gaussian model-comparison log-likelihood ratio is 2.402222222222223 for observed value 1.2, candidate mean 0.96, baseline mean 1.9, and sigma 0.3.
**Belief:** 1.00
**Derived from:** compute
**Premises:** `github:superconductivity_electron_liquids::_anon_001`, `github:superconductivity_electron_liquids::_anon_002`, `github:superconductivity_electron_liquids::_anon_003`, `github:superconductivity_electron_liquids::_anon_004`
**generated:** True
**helper_kind:** likelihood_score
**module_ref:** gaia.std.likelihood.gaussian_model_comparison@v1
**score_type:** log_lr
**claim_class:** gaia.std.likelihood.GaussianModelComparisonLogLR
**kind:** likelihood_score
**function_ref:** gaia.std.likelihood.gaussian_model_comparison_log_lr_claim
**query:** {'type': 'gaussian_model_comparison', 'direction': 'candidate_over_baseline', 'value_field': 'value_K'}
**target:** github:superconductivity_electron_liquids::tc_al_abinitio_outperforms_phenomenological
**value:** 2.402222222222223
**Referenced by:** likelihood -> `github:superconductivity_electron_liquids::tc_al_abinitio_outperforms_phenomenological`

### tc_zn_abinitio_outperforms_phenomenological

**QID:** `github:superconductivity_electron_liquids::tc_zn_abinitio_outperforms_phenomenological`
**Type:** claim
**Role:** derived
**Content:** For zinc, the ab initio EFT prediction explains the observed transition temperature better than the phenomenological McMillan prediction: $T_c^{\mathrm{EFT}} = 0.874$ K is nearly identical to $T_c^{\mathrm{exp}} = 0.875$ K, while the phenomenological value $T_c \approx 1.37$ K overestimates the measurement.
**Belief:** 0.86
**Derived from:** likelihood
**Premises:** `github:superconductivity_electron_liquids::tc_zn_experimental`, `github:superconductivity_electron_liquids::tc_zn_predicted`, `github:superconductivity_electron_liquids::tc_zn_phenomenological`, `github:superconductivity_electron_liquids::tc_zn_comparison_valid`, `github:superconductivity_electron_liquids::_anon_010`
**Reasoning:** Use the SciPy-backed Gaussian model-comparison likelihood score.

### tc_zn_comparison_valid

**QID:** `github:superconductivity_electron_liquids::tc_zn_comparison_valid`
**Type:** claim
**Role:** independent
**Content:** The zinc comparison uses the same material, the same experimental $T_c$ target, and the same absolute-error criterion for the ab initio and phenomenological predictions.
**Prior:** 0.97
**Belief:** 0.97
**prior:** 0.97
**prior_justification:** Same material and near-identical experimental target comparison.
**Referenced by:** likelihood -> `github:superconductivity_electron_liquids::tc_zn_abinitio_outperforms_phenomenological`

### github:superconductivity_electron_liquids::_anon_006

**QID:** `github:superconductivity_electron_liquids::_anon_006`
**Type:** claim
**Role:** independent
**Content:** The argument observed of Python function gaia.std.likelihood.gaussian_model_comparison_log_lr_claim is 0.875.
**Prior:** 1.00
**Belief:** 1.00
**generated:** True
**helper_kind:** compute_argument
**prior:** 0.999
**claim_class:** gaia.lang.dsl.claim_classes.ComputedArgument
**kind:** compute_argument
**Referenced by:** compute -> `github:superconductivity_electron_liquids::_anon_010`

### github:superconductivity_electron_liquids::_anon_007

**QID:** `github:superconductivity_electron_liquids::_anon_007`
**Type:** claim
**Role:** independent
**Content:** The argument candidate_mean of Python function gaia.std.likelihood.gaussian_model_comparison_log_lr_claim is 0.874.
**Prior:** 1.00
**Belief:** 1.00
**generated:** True
**helper_kind:** compute_argument
**prior:** 0.999
**claim_class:** gaia.lang.dsl.claim_classes.ComputedArgument
**kind:** compute_argument
**Referenced by:** compute -> `github:superconductivity_electron_liquids::_anon_010`

### github:superconductivity_electron_liquids::_anon_008

**QID:** `github:superconductivity_electron_liquids::_anon_008`
**Type:** claim
**Role:** independent
**Content:** The argument baseline_mean of Python function gaia.std.likelihood.gaussian_model_comparison_log_lr_claim is 1.37.
**Prior:** 1.00
**Belief:** 1.00
**generated:** True
**helper_kind:** compute_argument
**prior:** 0.999
**claim_class:** gaia.lang.dsl.claim_classes.ComputedArgument
**kind:** compute_argument
**Referenced by:** compute -> `github:superconductivity_electron_liquids::_anon_010`

### github:superconductivity_electron_liquids::_anon_009

**QID:** `github:superconductivity_electron_liquids::_anon_009`
**Type:** claim
**Role:** independent
**Content:** The argument sigma of Python function gaia.std.likelihood.gaussian_model_comparison_log_lr_claim is 0.2.
**Prior:** 1.00
**Belief:** 1.00
**generated:** True
**helper_kind:** compute_argument
**prior:** 0.999
**claim_class:** gaia.lang.dsl.claim_classes.ComputedArgument
**kind:** compute_argument
**Referenced by:** compute -> `github:superconductivity_electron_liquids::_anon_010`

### github:superconductivity_electron_liquids::_anon_010

**QID:** `github:superconductivity_electron_liquids::_anon_010`
**Type:** claim
**Role:** derived
**Content:** The Gaussian model-comparison log-likelihood ratio is 3.062800000000002 for observed value 0.875, candidate mean 0.874, baseline mean 1.37, and sigma 0.2.
**Belief:** 1.00
**Derived from:** compute
**Premises:** `github:superconductivity_electron_liquids::_anon_006`, `github:superconductivity_electron_liquids::_anon_007`, `github:superconductivity_electron_liquids::_anon_008`, `github:superconductivity_electron_liquids::_anon_009`
**generated:** True
**helper_kind:** likelihood_score
**module_ref:** gaia.std.likelihood.gaussian_model_comparison@v1
**score_type:** log_lr
**claim_class:** gaia.std.likelihood.GaussianModelComparisonLogLR
**kind:** likelihood_score
**function_ref:** gaia.std.likelihood.gaussian_model_comparison_log_lr_claim
**query:** {'type': 'gaussian_model_comparison', 'direction': 'candidate_over_baseline', 'value_field': 'value_K'}
**target:** github:superconductivity_electron_liquids::tc_zn_abinitio_outperforms_phenomenological
**value:** 3.062800000000002
**Referenced by:** likelihood -> `github:superconductivity_electron_liquids::tc_zn_abinitio_outperforms_phenomenological`

### tc_li_abinitio_outperforms_phenomenological

**QID:** `github:superconductivity_electron_liquids::tc_li_abinitio_outperforms_phenomenological`
**Type:** claim
**Role:** derived
**Content:** For lithium, the ab initio EFT prediction explains the observed ultra-low transition temperature better than the phenomenological McMillan prediction: the ab initio value is within an order of magnitude of $T_c^{\mathrm{exp}} \approx 4 \times 10^{-4}$ K, while the phenomenological value $T_c \approx 0.35$ K is too high by roughly three orders of magnitude.
**Belief:** 0.79
**Derived from:** likelihood
**Premises:** `github:superconductivity_electron_liquids::tc_li_experimental`, `github:superconductivity_electron_liquids::tc_li_predicted`, `github:superconductivity_electron_liquids::tc_li_phenomenological`, `github:superconductivity_electron_liquids::tc_li_comparison_valid`, `github:superconductivity_electron_liquids::_anon_015`
**Reasoning:** Use the SciPy-backed Gaussian model-comparison likelihood score.

### tc_li_comparison_valid

**QID:** `github:superconductivity_electron_liquids::tc_li_comparison_valid`
**Type:** claim
**Role:** independent
**Content:** The lithium comparison uses the same 9R low-temperature structure target where applicable, the same experimental $T_c$ reference, and an order-of-magnitude error criterion appropriate for the ultra-low transition temperature regime.
**Prior:** 0.88
**Belief:** 0.88
**prior:** 0.88
**prior_justification:** Lithium structure uncertainty and ultra-low-T scale make comparison less clean.
**Referenced by:** likelihood -> `github:superconductivity_electron_liquids::tc_li_abinitio_outperforms_phenomenological`

### github:superconductivity_electron_liquids::_anon_011

**QID:** `github:superconductivity_electron_liquids::_anon_011`
**Type:** claim
**Role:** independent
**Content:** The argument observed of Python function gaia.std.likelihood.gaussian_model_comparison_log_lr_claim is -3.3979400086720375.
**Prior:** 1.00
**Belief:** 1.00
**generated:** True
**helper_kind:** compute_argument
**prior:** 0.999
**claim_class:** gaia.lang.dsl.claim_classes.ComputedArgument
**kind:** compute_argument
**Referenced by:** compute -> `github:superconductivity_electron_liquids::_anon_015`

### github:superconductivity_electron_liquids::_anon_012

**QID:** `github:superconductivity_electron_liquids::_anon_012`
**Type:** claim
**Role:** independent
**Content:** The argument candidate_mean of Python function gaia.std.likelihood.gaussian_model_comparison_log_lr_claim is -2.3010299956639813.
**Prior:** 1.00
**Belief:** 1.00
**generated:** True
**helper_kind:** compute_argument
**prior:** 0.999
**claim_class:** gaia.lang.dsl.claim_classes.ComputedArgument
**kind:** compute_argument
**Referenced by:** compute -> `github:superconductivity_electron_liquids::_anon_015`

### github:superconductivity_electron_liquids::_anon_013

**QID:** `github:superconductivity_electron_liquids::_anon_013`
**Type:** claim
**Role:** independent
**Content:** The argument baseline_mean of Python function gaia.std.likelihood.gaussian_model_comparison_log_lr_claim is -0.4559319556497244.
**Prior:** 1.00
**Belief:** 1.00
**generated:** True
**helper_kind:** compute_argument
**prior:** 0.999
**claim_class:** gaia.lang.dsl.claim_classes.ComputedArgument
**kind:** compute_argument
**Referenced by:** compute -> `github:superconductivity_electron_liquids::_anon_015`

### github:superconductivity_electron_liquids::_anon_014

**QID:** `github:superconductivity_electron_liquids::_anon_014`
**Type:** claim
**Role:** independent
**Content:** The argument sigma of Python function gaia.std.likelihood.gaussian_model_comparison_log_lr_claim is 1.0.
**Prior:** 1.00
**Belief:** 1.00
**generated:** True
**helper_kind:** compute_argument
**prior:** 0.999
**claim_class:** gaia.lang.dsl.claim_classes.ComputedArgument
**kind:** compute_argument
**Referenced by:** compute -> `github:superconductivity_electron_liquids::_anon_015`

### github:superconductivity_electron_liquids::_anon_015

**QID:** `github:superconductivity_electron_liquids::_anon_015`
**Type:** claim
**Role:** derived
**Content:** The Gaussian model-comparison log-likelihood ratio is 3.7260999037054043 for observed value -3.3979400086720375, candidate mean -2.3010299956639813, baseline mean -0.4559319556497244, and sigma 1.0.
**Belief:** 1.00
**Derived from:** compute
**Premises:** `github:superconductivity_electron_liquids::_anon_011`, `github:superconductivity_electron_liquids::_anon_012`, `github:superconductivity_electron_liquids::_anon_013`, `github:superconductivity_electron_liquids::_anon_014`
**generated:** True
**helper_kind:** likelihood_score
**module_ref:** gaia.std.likelihood.gaussian_model_comparison@v1
**score_type:** log_lr
**claim_class:** gaia.std.likelihood.GaussianModelComparisonLogLR
**kind:** likelihood_score
**function_ref:** gaia.std.likelihood.gaussian_model_comparison_log_lr_claim
**query:** {'type': 'gaussian_model_comparison', 'direction': 'candidate_over_baseline', 'value_field': 'value_K', 'transform': 'log10'}
**target:** github:superconductivity_electron_liquids::tc_li_abinitio_outperforms_phenomenological
**value:** 3.7260999037054043
**Referenced by:** likelihood -> `github:superconductivity_electron_liquids::tc_li_abinitio_outperforms_phenomenological`
