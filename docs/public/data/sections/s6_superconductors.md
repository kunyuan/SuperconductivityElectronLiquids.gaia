# Module: s6_superconductors

### ueg_mu_ef_table_i

**QID:** `github:superconductivity_electron_liquids::ueg_mu_ef_table_i`
**Type:** claim
**Role:** independent
**Content:** 
**Prior:** 0.90
**Belief:** 0.92
**prior:** 0.9
**prior_justification:** arXiv TeX Table I is the numerical source for mu_EF values and uncertainties.
**grounding:** {'kind': 'source_fact', 'rationale': 'The TeX source of arXiv:2512.19382v2 Table I lists mu_EF(rs) values and parenthesized systematic uncertainties; these values are taken from the arXiv PDF/TeX source.', 'source_refs': [], 'action_label': 'github:superconductivity_electron_liquids::action::_anon_action_057', 'pattern': 'observation'}
**Referenced by:** deduction -> `github:superconductivity_electron_liquids::al_mu_star_input`; deduction -> `github:superconductivity_electron_liquids::li_mu_star_input`; deduction -> `github:superconductivity_electron_liquids::zn_mu_star_input`

### shared_dfpt_lambda_error_model

**QID:** `github:superconductivity_electron_liquids::shared_dfpt_lambda_error_model`
**Type:** claim
**Role:** independent
**Content:** The shared DFPT lambda error model uses a 0.1 fractional systematic uncertainty for simple metals.
**Prior:** 0.78
**Belief:** 0.82
**content_template:** The shared DFPT lambda error model uses a {fractional_uncertainty} fractional systematic uncertainty for simple metals.
**prior:** 0.78
**prior_justification:** Lambda uncertainty is model-based because Table II reports values without error bars.
**grounding:** {'kind': 'source_fact', 'rationale': 'The source paper gives Table II lambda values but no lambda error bars. The package therefore marks lambda uncertainty as a shared DFPT systematic model rather than a table-derived uncertainty.', 'source_refs': [], 'action_label': 'github:superconductivity_electron_liquids::action::_anon_action_058', 'pattern': 'observation'}
**Referenced by:** deduction -> `github:superconductivity_electron_liquids::al_lambda_input`; deduction -> `github:superconductivity_electron_liquids::li_lambda_input`; deduction -> `github:superconductivity_electron_liquids::zn_lambda_input`

### tolmachev_log_mu_star_error_model

**QID:** `github:superconductivity_electron_liquids::tolmachev_log_mu_star_error_model`
**Type:** claim
**Role:** independent
**Content:** The mu* error model treats the Tolmachev logarithm as uncertain by 1.0 logarithmic unit.
**Prior:** 0.80
**Belief:** 0.83
**content_template:** The mu* error model treats the Tolmachev logarithm as uncertain by {log_uncertainty} logarithmic unit.
**prior:** 0.8
**prior_justification:** mu* uncertainty includes a shared Tolmachev-log cutoff-matching systematic.
**grounding:** {'kind': 'source_fact', 'rationale': 'The arXiv table reports mu_EF uncertainties, but the mapped mu* also inherits uncertainty from the Tolmachev logarithm used to run from E_F to the phonon scale. The package therefore treats one logarithmic unit in the cutoff matching as a shared systematic.', 'source_refs': [], 'action_label': 'github:superconductivity_electron_liquids::action::_anon_action_059', 'pattern': 'observation'}
**Referenced by:** deduction -> `github:superconductivity_electron_liquids::al_mu_star_input`; deduction -> `github:superconductivity_electron_liquids::li_mu_star_input`; deduction -> `github:superconductivity_electron_liquids::zn_mu_star_input`

### al_arxiv_table_row

**QID:** `github:superconductivity_electron_liquids::al_arxiv_table_row`
**Type:** claim
**Role:** independent
**Content:** The arXiv TeX Table II row for Al (fcc) gives lambda = 0.44, rs = 2.07, mb = 1.05, TF = 130000.0 K, and omega_log = 320.0 K.
**Prior:** 0.90
**Belief:** 0.91
**content_template:** The arXiv TeX Table II row for {material} ({structure}) gives lambda = {lambda_value}, rs = {rs}, mb = {band_mass}, TF = {fermi_temperature_k} K, and omega_log = {omega_log_k} K.
**prior:** 0.9
**prior_justification:** Structured transcription from arXiv TeX Table II.
**grounding:** {'kind': 'source_fact', 'rationale': 'Structured transcription from arXiv:2512.19382v2 TeX source Table II.', 'source_refs': [], 'action_label': 'github:superconductivity_electron_liquids::action::_anon_action_060', 'pattern': 'observation'}
**Referenced by:** deduction -> `github:superconductivity_electron_liquids::al_lambda_input`; deduction -> `github:superconductivity_electron_liquids::al_mu_star_input`

### aluminum_parameters

**QID:** `github:superconductivity_electron_liquids::aluminum_parameters`
**Type:** setting
**Role:** setting
**Content:** Aluminum (Al): FCC crystal structure, $r_s = 2.07$, experimental Debye temperature $\Theta_D \approx 428$ K, DFPT electron-phonon coupling $\lambda \approx 0.44$, logarithmic phonon frequency $\omega_{\mathrm{log}} = 320$ K.

### al_lambda_input

**QID:** `github:superconductivity_electron_liquids::al_lambda_input`
**Type:** claim
**Role:** derived
**Content:** The DFPT electron-phonon coupling input for Al (fcc) is lambda = 0.44 ± 0.044.
**Belief:** 0.88
**Derived from:** deduction
**Premises:** `github:superconductivity_electron_liquids::al_arxiv_table_row`, `github:superconductivity_electron_liquids::shared_dfpt_lambda_error_model`
**content_template:** The DFPT electron-phonon coupling input for {material} ({structure}) is lambda = {value} ± {uncertainty}.
**Referenced by:** deduction -> `github:superconductivity_electron_liquids::al_effective_coupling`

### al_mu_star_input

**QID:** `github:superconductivity_electron_liquids::al_mu_star_input`
**Type:** claim
**Role:** derived
**Content:** The Coulomb pseudopotential input for Al (fcc) is mu* = 0.1289 ± 0.0179.
**Belief:** 0.86
**Derived from:** deduction
**Premises:** `github:superconductivity_electron_liquids::al_arxiv_table_row`, `github:superconductivity_electron_liquids::ueg_mu_ef_table_i`, `github:superconductivity_electron_liquids::tolmachev_log_mu_star_error_model`
**content_template:** The Coulomb pseudopotential input for {material} ({structure}) is mu* = {value} ± {uncertainty}.
**Referenced by:** deduction -> `github:superconductivity_electron_liquids::al_effective_coupling`

### al_effective_coupling

**QID:** `github:superconductivity_electron_liquids::al_effective_coupling`
**Type:** claim
**Role:** derived
**Content:** The effective pairing strength for Al is g = 0.2759 ± 0.0633.
**Belief:** 0.92
**Derived from:** deduction
**Premises:** `github:superconductivity_electron_liquids::al_lambda_input`, `github:superconductivity_electron_liquids::al_mu_star_input`
**content_template:** The effective pairing strength for {material} is g = {value} ± {uncertainty}.
**Referenced by:** deduction -> `github:superconductivity_electron_liquids::tc_al_predicted`

### li_arxiv_table_row

**QID:** `github:superconductivity_electron_liquids::li_arxiv_table_row`
**Type:** claim
**Role:** independent
**Content:** The arXiv TeX Table II row for Li (9R) gives lambda = 0.34, rs = 3.25, mb = 1.75, TF = 40000.0 K, and omega_log = 242.0 K.
**Prior:** 0.82
**Belief:** 0.83
**content_template:** The arXiv TeX Table II row for {material} ({structure}) gives lambda = {lambda_value}, rs = {rs}, mb = {band_mass}, TF = {fermi_temperature_k} K, and omega_log = {omega_log_k} K.
**prior:** 0.82
**prior_justification:** Structured transcription from the Li(9R) row, with residual structural uncertainty.
**grounding:** {'kind': 'source_fact', 'rationale': 'Structured transcription from arXiv:2512.19382v2 TeX source Table II for the low-temperature 9R lithium row.', 'source_refs': [], 'action_label': 'github:superconductivity_electron_liquids::action::_anon_action_064', 'pattern': 'observation'}
**Referenced by:** deduction -> `github:superconductivity_electron_liquids::li_lambda_input`; deduction -> `github:superconductivity_electron_liquids::li_mu_star_input`

### lithium_parameters

**QID:** `github:superconductivity_electron_liquids::lithium_parameters`
**Type:** setting
**Role:** setting
**Content:** Lithium (Li): the Table II low-temperature 9R row uses $r_s = 3.25$, band mass $m_b = 1.75$, DFPT/literature electron-phonon coupling $\lambda = 0.34$, and $\omega_{\mathrm{log}} = 242$ K. The alternate hcp row gives $\lambda = 0.37$ and $T_c = 0.03$ K. Crystal structure at ultra-low temperatures remains debated.

### li_lambda_input

**QID:** `github:superconductivity_electron_liquids::li_lambda_input`
**Type:** claim
**Role:** derived
**Content:** The DFPT electron-phonon coupling input for Li (9R) is lambda = 0.34 ± 0.034.
**Belief:** 0.85
**Derived from:** deduction
**Premises:** `github:superconductivity_electron_liquids::li_arxiv_table_row`, `github:superconductivity_electron_liquids::shared_dfpt_lambda_error_model`
**content_template:** The DFPT electron-phonon coupling input for {material} ({structure}) is lambda = {value} ± {uncertainty}.
**Referenced by:** deduction -> `github:superconductivity_electron_liquids::li_effective_coupling`

### li_mu_star_input

**QID:** `github:superconductivity_electron_liquids::li_mu_star_input`
**Type:** claim
**Role:** derived
**Content:** The Coulomb pseudopotential input for Li (9R) is mu* = 0.1749 ± 0.0375.
**Belief:** 0.83
**Derived from:** deduction
**Premises:** `github:superconductivity_electron_liquids::li_arxiv_table_row`, `github:superconductivity_electron_liquids::ueg_mu_ef_table_i`, `github:superconductivity_electron_liquids::tolmachev_log_mu_star_error_model`
**content_template:** The Coulomb pseudopotential input for {material} ({structure}) is mu* = {value} ± {uncertainty}.
**Referenced by:** deduction -> `github:superconductivity_electron_liquids::li_effective_coupling`

### li_effective_coupling

**QID:** `github:superconductivity_electron_liquids::li_effective_coupling`
**Type:** claim
**Role:** derived
**Content:** The effective pairing strength for Li is g = 0.1282 ± 0.0757.
**Belief:** 0.88
**Derived from:** deduction
**Premises:** `github:superconductivity_electron_liquids::li_lambda_input`, `github:superconductivity_electron_liquids::li_mu_star_input`
**content_template:** The effective pairing strength for {material} is g = {value} ± {uncertainty}.
**Referenced by:** deduction -> `github:superconductivity_electron_liquids::li_effective_coupling_error_bounded`; deduction -> `github:superconductivity_electron_liquids::tc_li_predicted`

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
**Content:** Zinc (Zn): HCP crystal structure, $r_s = 2.90$, experimental Debye temperature $\Theta_D \approx 327$ K, DFPT electron-phonon coupling $\lambda = 0.502$, logarithmic phonon frequency $\omega_{\mathrm{log}} = 111$ K.

### zn_arxiv_table_row

**QID:** `github:superconductivity_electron_liquids::zn_arxiv_table_row`
**Type:** claim
**Role:** independent
**Content:** The arXiv TeX Table II row for Zn (hcp) gives lambda = 0.502, rs = 2.9, mb = 1.0, TF = 121000.0 K, and omega_log = 111.0 K.
**Prior:** 0.90
**Belief:** 0.91
**content_template:** The arXiv TeX Table II row for {material} ({structure}) gives lambda = {lambda_value}, rs = {rs}, mb = {band_mass}, TF = {fermi_temperature_k} K, and omega_log = {omega_log_k} K.
**prior:** 0.9
**prior_justification:** Structured transcription from arXiv TeX Table II.
**grounding:** {'kind': 'source_fact', 'rationale': 'Structured transcription from arXiv:2512.19382v2 TeX source Table II.', 'source_refs': [], 'action_label': 'github:superconductivity_electron_liquids::action::_anon_action_069', 'pattern': 'observation'}
**Referenced by:** deduction -> `github:superconductivity_electron_liquids::zn_lambda_input`; deduction -> `github:superconductivity_electron_liquids::zn_mu_star_input`

### zn_lambda_input

**QID:** `github:superconductivity_electron_liquids::zn_lambda_input`
**Type:** claim
**Role:** derived
**Content:** The DFPT electron-phonon coupling input for Zn (hcp) is lambda = 0.502 ± 0.0502.
**Belief:** 0.88
**Derived from:** deduction
**Premises:** `github:superconductivity_electron_liquids::zn_arxiv_table_row`, `github:superconductivity_electron_liquids::shared_dfpt_lambda_error_model`
**content_template:** The DFPT electron-phonon coupling input for {material} ({structure}) is lambda = {value} ± {uncertainty}.
**Referenced by:** deduction -> `github:superconductivity_electron_liquids::zn_effective_coupling`

### zn_mu_star_input

**QID:** `github:superconductivity_electron_liquids::zn_mu_star_input`
**Type:** claim
**Role:** derived
**Content:** The Coulomb pseudopotential input for Zn (hcp) is mu* = 0.12 ± 0.0156.
**Belief:** 0.86
**Derived from:** deduction
**Premises:** `github:superconductivity_electron_liquids::zn_arxiv_table_row`, `github:superconductivity_electron_liquids::ueg_mu_ef_table_i`, `github:superconductivity_electron_liquids::tolmachev_log_mu_star_error_model`
**content_template:** The Coulomb pseudopotential input for {material} ({structure}) is mu* = {value} ± {uncertainty}.
**Referenced by:** deduction -> `github:superconductivity_electron_liquids::zn_effective_coupling`

### zn_effective_coupling

**QID:** `github:superconductivity_electron_liquids::zn_effective_coupling`
**Type:** claim
**Role:** derived
**Content:** The effective pairing strength for Zn is g = 0.3447 ± 0.0669.
**Belief:** 0.92
**Derived from:** deduction
**Premises:** `github:superconductivity_electron_liquids::zn_lambda_input`, `github:superconductivity_electron_liquids::zn_mu_star_input`
**content_template:** The effective pairing strength for {material} is g = {value} ± {uncertainty}.
**Referenced by:** deduction -> `github:superconductivity_electron_liquids::tc_zn_predicted`
