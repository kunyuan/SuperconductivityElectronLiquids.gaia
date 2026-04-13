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
**Belief:** 0.90
**prior:** 0.9
**prior_justification:** Well-supported.

### ueg_pseudopotential_parameterization

**QID:** `github:superconductivity_electron_liquids::ueg_pseudopotential_parameterization`
**Type:** claim
**Role:** independent
**Content:** The UEG Coulomb pseudopotential $\mu_{E_F}(r_s)$ computed by vDiagMC can be parameterized as a smooth function of $r_s$ and mapped onto real materials by using the material's effective $r_s$ (determined from the valence electron density). Combined with the BTS relation to run $\mu_{E_F}$ down to the Debye scale, this provides $\mu^*(r_s)$ for any simple metal without additional adjustable parameters.
**Belief:** 0.86
**prior:** 0.85
**prior_justification:** Mapping procedure reasonable; band-mass correction adds uncertainty.
**Referenced by:** support -> `github:superconductivity_electron_liquids::mu_available_for_simple_metals`; infer -> `github:superconductivity_electron_liquids::ab_initio_workflow`

### ab_initio_workflow

**QID:** `github:superconductivity_electron_liquids::ab_initio_workflow`
**Type:** claim
**Role:** derived
**Content:** The complete ab initio workflow for predicting $T_c$ of simple metals: (1) compute $\mu_{E_F}$ from the UEG four-point vertex via vDiagMC, (2) map to the material's $r_s$ and run down to $\mu^*$ via the BTS relation, (3) obtain $\lambda$ from DFPT, (4) solve the downfolded Eliashberg equations (or use the PCF extrapolation) to predict $T_c$. All inputs are from first principles; no adjustable parameters remain.
**Belief:** 1.00
**Derived from:** deduction
**Premises:** `github:superconductivity_electron_liquids::downfolded_bse`, `github:superconductivity_electron_liquids::mu_available_for_simple_metals`, `github:superconductivity_electron_liquids::dfpt_reliable_for_simple_metals`
**Derived from:** infer
**Premises:** `github:superconductivity_electron_liquids::downfolded_bse`, `github:superconductivity_electron_liquids::mu_vdiagmc_values`, `github:superconductivity_electron_liquids::dfpt_reliable_for_simple_metals`, `github:superconductivity_electron_liquids::ueg_pseudopotential_parameterization`
**figure:** artifacts/images/13_0.jpg
**caption:** Fig. 9 | Proposed ab initio framework for electron-phonon SC beyond the weak correlation limit, showing computational pathway from fundamental parameters through correlated electrons and lattice vibrations to superconducting properties.
**gaia:** {'provenance': {'referenced_claims': ['dfpt_reliable_for_simple_metals', 'downfolded_bse', 'mu_available_for_simple_metals']}}
**Referenced by:** support -> `github:superconductivity_electron_liquids::tc_al_predicted`; support -> `github:superconductivity_electron_liquids::tc_zn_predicted`; support -> `github:superconductivity_electron_liquids::tc_li_predicted`; support -> `github:superconductivity_electron_liquids::al_pressure_transition`; support -> `github:superconductivity_electron_liquids::tc_mg_na_near_qpt`; abduction -> `github:superconductivity_electron_liquids::_anon_002`; abduction -> `github:superconductivity_electron_liquids::_anon_004`; abduction -> `github:superconductivity_electron_liquids::_anon_006`

### mu_available_for_simple_metals

**QID:** `github:superconductivity_electron_liquids::mu_available_for_simple_metals`
**Type:** claim
**Role:** derived
**Content:** For simple metals, the Coulomb pseudopotential $\mu^*$ can be obtained from first principles without adjustable parameters: the vDiagMC-computed $\mu_{E_F}(r_s)$ for the uniform electron gas is mapped to real materials via material-specific $r_s$ and band mass, then scaled to the Debye frequency via the BTS renormalization relation.
**Belief:** 0.46
**Derived from:** support
**Premises:** `github:superconductivity_electron_liquids::ueg_pseudopotential_parameterization`, `github:superconductivity_electron_liquids::mu_vdiagmc_values`
**gaia:** {'provenance': {'referenced_claims': ['bts_renormalization', 'mu_vdiagmc_values', 'simple_metals_weak_lattice', 'ueg_pseudopotential_parameterization']}}
**Referenced by:** deduction -> `github:superconductivity_electron_liquids::ab_initio_workflow`

### tc_al_predicted

**QID:** `github:superconductivity_electron_liquids::tc_al_predicted`
**Type:** claim
**Role:** derived
**Content:** The ab initio predicted superconducting transition temperature of aluminum is $T_c^{\mathrm{EFT}} = 0.96$ K, in good agreement with the experimental value $T_c^{\mathrm{exp}} = 1.2$ K. The first-principles $\mu^*(\mathrm{Al}) = 0.13$ is obtained from the vDiagMC $\mu_{E_F}$ at $r_s = 2.07$ (with band mass $m_b = 1.05$) via BTS renormalization.
**Belief:** 0.99
**Derived from:** support
**Premises:** `github:superconductivity_electron_liquids::ab_initio_workflow`
**figure:** artifacts/images/14_0.jpg
**caption:** Fig. 10 | Pressure dependence of the superconducting critical temperature in aluminum. EFT results (squares) compared with experimental data from Levy et al. and Gubser et al.
**gaia:** {'provenance': {'referenced_claims': ['ab_initio_workflow', 'aluminum_parameters']}}
**Referenced by:** compare -> `github:superconductivity_electron_liquids::_anon_002`; abduction -> `github:superconductivity_electron_liquids::_anon_002`

### tc_zn_predicted

**QID:** `github:superconductivity_electron_liquids::tc_zn_predicted`
**Type:** claim
**Role:** derived
**Content:** The ab initio predicted superconducting transition temperature of zinc is $T_c^{\mathrm{EFT}} = 0.874$ K, in excellent agreement with the experimental value $T_c^{\mathrm{exp}} = 0.875$ K. The first-principles $\mu^*(\mathrm{Zn}) = 0.12$ is obtained from the vDiagMC $\mu_{E_F}$ at $r_s = 2.90$ (with band mass $m_b = 1.0$) via BTS renormalization.
**Belief:** 0.99
**Derived from:** support
**Premises:** `github:superconductivity_electron_liquids::ab_initio_workflow`
**figure:** artifacts/images/15_0.jpg
**caption:** Fig. 11 | Effective BCS coupling strength for simple metals. E-ph couplings from DFPT; pseudopotentials from vDiagMC. Includes Al, Zn, Li, Na, Mg predictions.
**gaia:** {'provenance': {'referenced_claims': ['ab_initio_workflow', 'zinc_parameters']}}
**Referenced by:** compare -> `github:superconductivity_electron_liquids::_anon_004`; abduction -> `github:superconductivity_electron_liquids::_anon_004`

### tc_li_predicted

**QID:** `github:superconductivity_electron_liquids::tc_li_predicted`
**Type:** claim
**Role:** derived
**Content:** The ab initio predicted superconducting transition temperature of lithium (9R structure) is $T_c^{\mathrm{EFT}} = 5 \times 10^{-3}$ K, within an order of magnitude of the experimental observation $T_c^{\mathrm{exp}} \approx 4 \times 10^{-4}$ K. The large $\mu^*(\mathrm{Li}) = 0.18$ from $r_s = 3.25$ (with band mass $m_b = 1.75$) almost completely cancels the phonon-mediated attraction $\lambda = 0.34$, pushing $T_c$ to extremely low temperatures. The HCP structure gives $T_c^{\mathrm{EFT}} = 0.03$ K with $\mu^* = 0.17$ and $\lambda = 0.37$.
**Belief:** 0.25
**Derived from:** support
**Premises:** `github:superconductivity_electron_liquids::ab_initio_workflow`
**figure:** artifacts/images/15_0.jpg
**caption:** Fig. 11 | Effective BCS coupling strength for simple metals. E-ph couplings from DFPT; pseudopotentials from vDiagMC. Includes Al, Zn, Li, Na, Mg predictions.
**gaia:** {'provenance': {'referenced_claims': ['ab_initio_workflow', 'lithium_parameters']}}
**Referenced by:** compare -> `github:superconductivity_electron_liquids::_anon_006`; abduction -> `github:superconductivity_electron_liquids::_anon_006`

### al_pressure_transition

**QID:** `github:superconductivity_electron_liquids::al_pressure_transition`
**Type:** claim
**Role:** derived
**Content:** Under hydrostatic pressure, the ab initio framework predicts that aluminum's superconducting $T_c$ monotonically decreases, consistent with experimental data up to 6 GPa. The framework predicts that superconductivity in Al vanishes at approximately 60 GPa; at 20 GPa, $T_c$ is already suppressed below 1 mK.
**Belief:** 0.80
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
**Belief:** 0.80
**Derived from:** support
**Premises:** `github:superconductivity_electron_liquids::ab_initio_workflow`
**figure:** artifacts/images/15_0.jpg
**caption:** Fig. 11 | Effective BCS coupling strength for simple metals. Na and Mg appear near the origin, indicating near-cancellation of pairing interaction.
**gaia:** {'provenance': {'referenced_claims': ['ab_initio_workflow', 'magnesium_parameters', 'precursory_cooper_flow', 'sodium_parameters']}}

### github:superconductivity_electron_liquids::_anon_002

**QID:** `github:superconductivity_electron_liquids::_anon_002`
**Type:** claim
**Role:** derived
**Content:** compare(The ab initio predicted superconducting transition temperature of aluminum is $T_c^{\mathrm{EFT}} = 0.96$ K, in good agreement with the experimental value $T_c^{\mathrm{exp}} = 1.2$ K. The first-principles $\mu^*(\mathrm{Al}) = 0.13$ is obtained from the vDiagMC $\mu_{E_F}$ at $r_s = 2.07$ (with band mass $m_b = 1.05$) via BTS renormalization., Using the McMillan formula (an empirical formula for $T_c$ based on the electron-phonon coupling constant $\lambda$ and Coulomb pseudopotential $\mu^*$) with the standard value $\mu^* = 0.1$, the predicted superconducting transition temperature of aluminum is $T_c \approx 1.9$ K, while the experimental value is 1.2 K, a deviation of approximately 58%., The experimental superconducting transition temperature of aluminum (Al) is $T_c^{\mathrm{exp}} = 1.2$ K.)
**Belief:** 1.00
**Derived from:** compare
**Premises:** `github:superconductivity_electron_liquids::tc_al_predicted`, `github:superconductivity_electron_liquids::tc_al_phenomenological`, `github:superconductivity_electron_liquids::tc_al_experimental`
**Derived from:** abduction
**Premises:** `github:superconductivity_electron_liquids::ab_initio_workflow`, `github:superconductivity_electron_liquids::dfpt_computes_lambda`, `github:superconductivity_electron_liquids::mu_star_phenomenological`, `github:superconductivity_electron_liquids::tc_al_predicted`, `github:superconductivity_electron_liquids::tc_al_phenomenological`, `github:superconductivity_electron_liquids::tc_al_experimental`
**helper_kind:** comparison_claim
**generated:** True
**gaia:** {'provenance': {'referenced_claims': ['tc_al_experimental', 'tc_al_phenomenological', 'tc_al_predicted']}}

### github:superconductivity_electron_liquids::_anon_003

**QID:** `github:superconductivity_electron_liquids::_anon_003`
**Type:** claim
**Role:** orphaned
**Content:** abduction_validity(support, support, compare)
**Belief:** 0.50
**helper_kind:** composition_validity
**generated:** True
**warrant:** The experimental $T_c(\mathrm{Al}) = 1.2$ K (@tc_al_experimental) is well reproduced by the ab initio prediction $T_c^{\mathrm{EFT}} = 0.96$ K (@tc_al_predicted), which uses no adjustable parameters. The phenomenological prediction (@tc_al_phenomenological) using $\mu^* = 0.1$ gives 1.9 K, overestimating by 58%. The ab initio approach provides a better explanation because it determines $\mu^*$ from first principles rather than using an ad hoc value, and the resulting $\mu^* = 0.13$ is above the standard guess of 0.1, correctly reducing $T_c$ toward the experimental value.

### github:superconductivity_electron_liquids::_anon_004

**QID:** `github:superconductivity_electron_liquids::_anon_004`
**Type:** claim
**Role:** derived
**Content:** compare(The ab initio predicted superconducting transition temperature of zinc is $T_c^{\mathrm{EFT}} = 0.874$ K, in excellent agreement with the experimental value $T_c^{\mathrm{exp}} = 0.875$ K. The first-principles $\mu^*(\mathrm{Zn}) = 0.12$ is obtained from the vDiagMC $\mu_{E_F}$ at $r_s = 2.90$ (with band mass $m_b = 1.0$) via BTS renormalization., Using the McMillan formula with the standard value $\mu^* = 0.1$, the predicted superconducting transition temperature of zinc is $T_c \approx 1.37$ K, while the experimental value is 0.875 K, a deviation of approximately 57%., The experimental superconducting transition temperature of zinc (Zn) is $T_c^{\mathrm{exp}} = 0.875$ K.)
**Belief:** 1.00
**Derived from:** compare
**Premises:** `github:superconductivity_electron_liquids::tc_zn_predicted`, `github:superconductivity_electron_liquids::tc_zn_phenomenological`, `github:superconductivity_electron_liquids::tc_zn_experimental`
**Derived from:** abduction
**Premises:** `github:superconductivity_electron_liquids::ab_initio_workflow`, `github:superconductivity_electron_liquids::dfpt_computes_lambda`, `github:superconductivity_electron_liquids::mu_star_phenomenological`, `github:superconductivity_electron_liquids::tc_zn_predicted`, `github:superconductivity_electron_liquids::tc_zn_phenomenological`, `github:superconductivity_electron_liquids::tc_zn_experimental`
**helper_kind:** comparison_claim
**generated:** True
**gaia:** {'provenance': {'referenced_claims': ['tc_zn_experimental', 'tc_zn_phenomenological', 'tc_zn_predicted']}}

### github:superconductivity_electron_liquids::_anon_005

**QID:** `github:superconductivity_electron_liquids::_anon_005`
**Type:** claim
**Role:** orphaned
**Content:** abduction_validity(support, support, compare)
**Belief:** 0.50
**helper_kind:** composition_validity
**generated:** True
**warrant:** The experimental $T_c(\mathrm{Zn}) = 0.875$ K (@tc_zn_experimental) is in excellent agreement with the ab initio prediction $T_c^{\mathrm{EFT}} = 0.874$ K (@tc_zn_predicted). The phenomenological prediction (@tc_zn_phenomenological) using $\mu^* = 0.1$ gives 1.37 K, overestimating by 57%. The ab initio $\mu^* = 0.12$ from $r_s = 2.90$ correctly captures the Coulomb repulsion strength in Zn, bringing the prediction into near-exact agreement with experiment.

### github:superconductivity_electron_liquids::_anon_006

**QID:** `github:superconductivity_electron_liquids::_anon_006`
**Type:** claim
**Role:** derived
**Content:** compare(The ab initio predicted superconducting transition temperature of lithium (9R structure) is $T_c^{\mathrm{EFT}} = 5 \times 10^{-3}$ K, within an order of magnitude of the experimental observation $T_c^{\mathrm{exp}} \approx 4 \times 10^{-4}$ K. The large $\mu^*(\mathrm{Li}) = 0.18$ from $r_s = 3.25$ (with band mass $m_b = 1.75$) almost completely cancels the phonon-mediated attraction $\lambda = 0.34$, pushing $T_c$ to extremely low temperatures. The HCP structure gives $T_c^{\mathrm{EFT}} = 0.03$ K with $\mu^* = 0.17$ and $\lambda = 0.37$., Using the McMillan formula with $\mu^* = 0.1$, the predicted superconducting transition temperature of lithium is $T_c \approx 0.35$ K, while the experimental value is approximately $4 \times 10^{-4}$ K; the theory overestimates by about three orders of magnitude., The experimental superconducting transition temperature of lithium (Li) is $T_c^{\mathrm{exp}} \approx 4 \times 10^{-4}$ K (0.4 mK). This measurement corresponds to the 9R crystal structure; the crystal structure of lithium at ultra-low temperatures remains controversial.)
**Belief:** 1.00
**Derived from:** compare
**Premises:** `github:superconductivity_electron_liquids::tc_li_predicted`, `github:superconductivity_electron_liquids::tc_li_phenomenological`, `github:superconductivity_electron_liquids::tc_li_experimental`
**Derived from:** abduction
**Premises:** `github:superconductivity_electron_liquids::ab_initio_workflow`, `github:superconductivity_electron_liquids::dfpt_computes_lambda`, `github:superconductivity_electron_liquids::mu_star_phenomenological`, `github:superconductivity_electron_liquids::tc_li_predicted`, `github:superconductivity_electron_liquids::tc_li_phenomenological`, `github:superconductivity_electron_liquids::tc_li_experimental`
**helper_kind:** comparison_claim
**generated:** True
**gaia:** {'provenance': {'referenced_claims': ['tc_li_experimental', 'tc_li_phenomenological', 'tc_li_predicted']}}

### github:superconductivity_electron_liquids::_anon_007

**QID:** `github:superconductivity_electron_liquids::_anon_007`
**Type:** claim
**Role:** orphaned
**Content:** abduction_validity(support, support, compare)
**Belief:** 0.50
**helper_kind:** composition_validity
**generated:** True
**warrant:** The experimental $T_c(\mathrm{Li}) \approx 4 \times 10^{-4}$ K (@tc_li_experimental) is within an order of magnitude of the ab initio prediction $T_c^{\mathrm{EFT}} = 5 \times 10^{-3}$ K (@tc_li_predicted, 9R structure). The phenomenological prediction (@tc_li_phenomenological) using $\mu^* = 0.1$ gives $\approx 0.35$ K, overestimating by three orders of magnitude. The dramatic improvement of the ab initio approach is because the first-principles $\mu^* = 0.18$ for lithium ($r_s = 3.25$, $m_b = 1.75$) is significantly larger than the standard guess of 0.1, reflecting the stronger Coulomb repulsion at lower electron density. In the regime where $\lambda - \mu^*(1+0.62\lambda)$ is small, the exponential sensitivity amplifies the $\mu^*$ difference from 0.08 to nearly three orders of magnitude in $T_c$.
