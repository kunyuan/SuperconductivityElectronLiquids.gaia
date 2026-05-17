# Module: s6_superconductors

### aluminum_parameters

**QID:** `github:superconductivity_electron_liquids::aluminum_parameters`
**Type:** note
**Role:** note
**Content:** Aluminum (Al): FCC crystal structure, $r_s = 2.07$, band mass $m_b = 1.05$, DFPT electron-phonon coupling $\lambda = 0.44$, logarithmic phonon frequency $\omega_{\mathrm{log}} = 320$ K, Fermi temperature $T_F = 1.3 \times 10^5$ K.

### lithium_parameters

**QID:** `github:superconductivity_electron_liquids::lithium_parameters`
**Type:** note
**Role:** note
**Content:** Lithium (Li): 9R crystal structure at low $T$ (also studied in HCP). 9R parameters: $r_s = 3.25$, $m_b = 1.75$, $\lambda = 0.34$, $\omega_{\mathrm{log}} = 242$ K, $T_F = 4.0 \times 10^4$ K. HCP parameters: $r_s = 3.19$, $m_b = 1.4$, $\lambda = 0.37$, $\omega_{\mathrm{log}} = 243$ K, $T_F = 4.1 \times 10^4$ K. Crystal structure at sub-kelvin temperatures remains debated.

### sodium_parameters

**QID:** `github:superconductivity_electron_liquids::sodium_parameters`
**Type:** note
**Role:** note
**Content:** Sodium (Na): BCC crystal structure, $r_s = 3.96$, band mass $m_b = 1.0$, DFPT electron-phonon coupling $\lambda = 0.2$, logarithmic phonon frequency $\omega_{\mathrm{log}} = 127$ K, Fermi temperature $T_F = 4.2 \times 10^4$ K. No superconductivity observed down to mK temperatures.

### magnesium_parameters

**QID:** `github:superconductivity_electron_liquids::magnesium_parameters`
**Type:** note
**Role:** note
**Content:** Magnesium (Mg): HCP crystal structure, $r_s = 2.66$, band mass $m_b = 1.02$, DFPT electron-phonon coupling $\lambda = 0.24$, logarithmic phonon frequency $\omega_{\mathrm{log}} = 269$ K, Fermi temperature $T_F = 8.0 \times 10^4$ K. No superconductivity observed down to mK temperatures.

### zinc_parameters

**QID:** `github:superconductivity_electron_liquids::zinc_parameters`
**Type:** note
**Role:** note
**Content:** Zinc (Zn): HCP crystal structure, $r_s = 2.90$, band mass $m_b = 1.0$, DFPT electron-phonon coupling $\lambda = 0.502$, logarithmic phonon frequency $\omega_{\mathrm{log}} = 111$ K, Fermi temperature $T_F = 1.21 \times 10^5$ K.

### simple_metals_weak_lattice

**QID:** `github:superconductivity_electron_liquids::simple_metals_weak_lattice`
**Type:** claim
**Role:** background
**Content:** Simple metals (Al, Li, Na, Mg, Zn) have weak lattice effects in the Coulomb pseudopotential: the difference between the crystalline $\mu^*$ and the UEG $\mu^*$ at the same $r_s$ is small (a few percent) because the nearly-free-electron character of these metals means the Fermi surface is approximately spherical and the electronic structure is well described by the homogeneous electron gas with minor crystal-field perturbations.
**Prior:** 0.90
**Belief:** 0.90
**prior_records:** [{'value': 0.9, 'source_id': 'empirical_physical_assertion', 'justification': 'The nearly-free-electron character of Al, Li, Na, Mg, Zn implies the spherical-Fermi-surface approximation holds at the few-percent level; the crystalline mu* differs from the UEG mu* by only a few percent at matched r_s.'}]
**prior:** 0.9
**prior_justification:** The nearly-free-electron character of Al, Li, Na, Mg, Zn implies the spherical-Fermi-surface approximation holds at the few-percent level; the crystalline mu* differs from the UEG mu* by only a few percent at matched r_s.
**prior_source_id:** empirical_physical_assertion

### ueg_pseudopotential_parameterization

**QID:** `github:superconductivity_electron_liquids::ueg_pseudopotential_parameterization`
**Type:** claim
**Role:** independent
**Content:** The UEG Coulomb pseudopotential $\mu_{E_F}(r_s)$ computed by vDiagMC can be parameterized as a smooth function of $r_s$ and mapped onto real materials by using the material's effective $r_s$ (determined from the valence electron density). Combined with the BTS relation to run $\mu_{E_F}$ down to the Debye scale, this provides $\mu^*(r_s)$ for any simple metal without additional adjustable parameters.
**Belief:** 0.53
**Referenced by:** deduction -> `github:superconductivity_electron_liquids::mu_available_for_simple_metals`

### mu_available_for_simple_metals

**QID:** `github:superconductivity_electron_liquids::mu_available_for_simple_metals`
**Type:** claim
**Role:** derived
**Content:** For simple metals, the Coulomb pseudopotential $\mu^*$ can be obtained from first principles without adjustable parameters: the vDiagMC-computed $\mu_{E_F}(r_s)$ for the uniform electron gas is mapped to real materials via material-specific $r_s$ and band mass, then scaled to the Debye frequency via the BTS renormalization relation.
**Belief:** 0.72
**Derived from:** deduction
**Premises:** `github:superconductivity_electron_liquids::ueg_pseudopotential_parameterization`, `github:superconductivity_electron_liquids::mu_vdiagmc_values`, `github:superconductivity_electron_liquids::bts_renormalization`
**Referenced by:** deduction -> `github:superconductivity_electron_liquids::ab_initio_workflow`

### github:superconductivity_electron_liquids::_anon_023

**QID:** `github:superconductivity_electron_liquids::_anon_023`
**Type:** claim
**Role:** orphaned
**Content:** derive warrants For simple metals, the Coulomb pseudopotential $\mu^*$ can be obtained from first principles without adjustable parameters: the vDiagMC-computed $\mu_{E_F}(r_s)$ for the uniform electron gas is mapped to real materials via material-specific $r_s$ and band mass, then scaled to the Debye frequency via the BTS renormalization relation.
**Belief:** 0.50
**generated:** True
**helper_kind:** implication_warrant
**review:** True
**relation:** {'type': 'derive', 'given': ['github:superconductivity_electron_liquids::ueg_pseudopotential_parameterization', 'github:superconductivity_electron_liquids::mu_vdiagmc_values', 'github:superconductivity_electron_liquids::bts_renormalization'], 'conclusion': 'github:superconductivity_electron_liquids::mu_available_for_simple_metals'}
**warrant:** The vDiagMC results provide $\mu_{E_F}(r_s)$ for the UEG (@mu_vdiagmc_values). The parameterization procedure (@ueg_pseudopotential_parameterization) maps these to real materials using material-specific $r_s$ and band mass, justified by the weak lattice effects in simple metals (@simple_metals_weak_lattice). The BTS relation (@bts_renormalization) scales $\mu_{E_F}$ down to $\mu^*$ at the Debye frequency — included as a premise because the material-specific $\mu^*$ is what is actually 'available' here.
**action_label:** github:superconductivity_electron_liquids::action::_anon_action_026
**pattern:** derivation
**gaia:** {'provenance': {'referenced_claims': ['bts_renormalization', 'mu_vdiagmc_values', 'simple_metals_weak_lattice', 'ueg_pseudopotential_parameterization']}}

### ab_initio_workflow

**QID:** `github:superconductivity_electron_liquids::ab_initio_workflow`
**Type:** claim
**Role:** derived
**Content:** The complete ab initio workflow for predicting $T_c$ of simple metals: (1) compute $\mu_{E_F}$ from the UEG four-point vertex via vDiagMC, (2) map to the material's $r_s$ and run down to $\mu^*$ via the BTS relation, (3) obtain $\lambda$ from DFPT, (4) solve the downfolded Eliashberg equations (or use the PCF extrapolation) to predict $T_c$. All inputs are from first principles; no adjustable parameters remain.
**Belief:** 0.96
**Derived from:** deduction
**Premises:** `github:superconductivity_electron_liquids::downfolded_bse`, `github:superconductivity_electron_liquids::mu_available_for_simple_metals`, `github:superconductivity_electron_liquids::dfpt_reliable_for_simple_metals`
**figure:** artifacts/images/13_0.jpg
**caption:** Fig. 9 | Proposed ab initio framework for electron-phonon SC beyond the weak correlation limit, showing computational pathway from fundamental parameters through correlated electrons and lattice vibrations to superconducting properties.
**Referenced by:** deduction -> `github:superconductivity_electron_liquids::al_pressure_transition`; deduction -> `github:superconductivity_electron_liquids::tc_mg_na_near_qpt`; deduction -> `github:superconductivity_electron_liquids::tc_al_predicted`; deduction -> `github:superconductivity_electron_liquids::tc_zn_predicted`; deduction -> `github:superconductivity_electron_liquids::tc_li_predicted`; infer -> `github:superconductivity_electron_liquids::tc_al_likelihood`; infer -> `github:superconductivity_electron_liquids::tc_zn_likelihood`; infer -> `github:superconductivity_electron_liquids::tc_li_likelihood`

### github:superconductivity_electron_liquids::_anon_024

**QID:** `github:superconductivity_electron_liquids::_anon_024`
**Type:** claim
**Role:** orphaned
**Content:** derive warrants The complete ab initio workflow for predicting $T_c$ of simple metals: (1) compute $\mu_{E_F}$ from the UEG four-point vertex via vDiagMC, (2) map to the material's $r_s$ and run down to $\mu^*$ via the BTS relation, (3) obtain $\lambda$ from DFPT, (4) solve the downfolded Eliashberg equations (or use the PCF extrapolation) to predict $T_c$. All inputs are from first principles; no adjustable parameters remain.
**Belief:** 0.50
**generated:** True
**helper_kind:** implication_warrant
**review:** True
**relation:** {'type': 'derive', 'given': ['github:superconductivity_electron_liquids::downfolded_bse', 'github:superconductivity_electron_liquids::mu_available_for_simple_metals', 'github:superconductivity_electron_liquids::dfpt_reliable_for_simple_metals'], 'conclusion': 'github:superconductivity_electron_liquids::ab_initio_workflow'}
**warrant:** The downfolded BSE (@downfolded_bse) provides the theoretical equation requiring two microscopic inputs: $\mu^*$ and $\lambda$. Both are now available from first principles — $\mu^*$ from the UEG parameterization (@mu_available_for_simple_metals) and $\lambda$ from validated DFPT (@dfpt_reliable_for_simple_metals). With all components determined from first principles, the workflow is complete and parameter-free.
**action_label:** github:superconductivity_electron_liquids::action::_anon_action_027
**pattern:** derivation
**gaia:** {'provenance': {'referenced_claims': ['dfpt_reliable_for_simple_metals', 'downfolded_bse', 'mu_available_for_simple_metals']}}

### al_pressure_transition

**QID:** `github:superconductivity_electron_liquids::al_pressure_transition`
**Type:** claim
**Role:** derived
**Content:** Under hydrostatic pressure, the ab initio framework predicts that aluminum's superconducting $T_c$ monotonically decreases, consistent with experimental data up to 6 GPa. The framework predicts that superconductivity in Al vanishes at approximately 60 GPa; at 20 GPa, $T_c$ is already suppressed below 1 mK.
**Belief:** 0.98
**Derived from:** deduction
**Premises:** `github:superconductivity_electron_liquids::ab_initio_workflow`
**figure:** artifacts/images/14_0.jpg
**caption:** Fig. 10 | Pressure dependence of the superconducting critical temperature in aluminum. EFT results (squares) compared with experimental data from Levy et al. and Gubser et al.

### github:superconductivity_electron_liquids::_anon_025

**QID:** `github:superconductivity_electron_liquids::_anon_025`
**Type:** claim
**Role:** orphaned
**Content:** derive warrants Under hydrostatic pressure, the ab initio framework predicts that aluminum's superconducting $T_c$ monotonically decreases, consistent with experimental data up to 6 GPa. The framework predicts that superconductivity in Al vanishes at approximately 60 GPa; at 20 GPa, $T_c$ is already suppressed below 1 mK.
**Belief:** 0.50
**generated:** True
**helper_kind:** implication_warrant
**review:** True
**relation:** {'type': 'derive', 'given': ['github:superconductivity_electron_liquids::ab_initio_workflow'], 'conclusion': 'github:superconductivity_electron_liquids::al_pressure_transition'}
**warrant:** Applying the ab initio workflow (@ab_initio_workflow) to aluminum under varying hydrostatic pressure (@aluminum_parameters): as pressure increases, $r_s$ decreases (higher electron density), modifying both $\mu^*$ and $\lambda$. The net effect is a monotonic decrease in $T_c$, accurately capturing the experimental trend from ambient to 6 GPa. Extrapolating beyond experimental data, the framework predicts SC vanishes at ~60 GPa, with $T_c < 1$ mK already at 20 GPa.
**action_label:** github:superconductivity_electron_liquids::action::_anon_action_028
**pattern:** derivation
**gaia:** {'provenance': {'referenced_claims': ['ab_initio_workflow', 'aluminum_parameters']}}

### tc_mg_na_near_qpt

**QID:** `github:superconductivity_electron_liquids::tc_mg_na_near_qpt`
**Type:** claim
**Role:** derived
**Content:** The ab initio framework predicts that sodium and magnesium have extremely low or vanishing $T_c$: for Na ($r_s = 3.96$, $\lambda = 0.2$, $\mu^* = 0.15$), the Coulomb repulsion nearly cancels the weak electron-phonon coupling, giving $T_c^{\mathrm{EFT}} = 2 \times 10^{-13}$ K (effectively no superconductivity). For Mg ($r_s = 2.66$, $\lambda = 0.24$, $\mu^* = 0.14$), $T_c^{\mathrm{EFT}} = 5 \times 10^{-5}$ K. Both materials are near the quantum phase transition between superconducting and non-superconducting ground states, where $T_c$ varies exponentially with small parameter changes.
**Belief:** 0.98
**Derived from:** deduction
**Premises:** `github:superconductivity_electron_liquids::ab_initio_workflow`
**figure:** artifacts/images/15_0.jpg
**caption:** Fig. 11 | Effective BCS coupling strength for simple metals. Na and Mg appear near the origin, indicating near-cancellation of pairing interaction.

### github:superconductivity_electron_liquids::_anon_026

**QID:** `github:superconductivity_electron_liquids::_anon_026`
**Type:** claim
**Role:** orphaned
**Content:** derive warrants The ab initio framework predicts that sodium and magnesium have extremely low or vanishing $T_c$: for Na ($r_s = 3.96$, $\lambda = 0.2$, $\mu^* = 0.15$), the Coulomb repulsion nearly cancels the weak electron-phonon coupling, giving $T_c^{\mathrm{EFT}} = 2 \times 10^{-13}$ K (effectively no superconductivity). For Mg ($r_s = 2.66$, $\lambda = 0.24$, $\mu^* = 0.14$), $T_c^{\mathrm{EFT}} = 5 \times 10^{-5}$ K. Both materials are near the quantum phase transition between superconducting and non-superconducting ground states, where $T_c$ varies exponentially with small parameter changes.
**Belief:** 0.50
**generated:** True
**helper_kind:** implication_warrant
**review:** True
**relation:** {'type': 'derive', 'given': ['github:superconductivity_electron_liquids::ab_initio_workflow'], 'conclusion': 'github:superconductivity_electron_liquids::tc_mg_na_near_qpt'}
**warrant:** Applying the ab initio workflow (@ab_initio_workflow) to sodium (@sodium_parameters) and magnesium (@magnesium_parameters): Na has $r_s = 3.96$, yielding $\mu^* = 0.15$ which nearly cancels its weak $\lambda = 0.2$, giving $T_c^{\mathrm{EFT}} = 2 \times 10^{-13}$ K (effectively no superconductivity). Mg has $r_s = 2.66$, yielding $\mu^* = 0.14$ which nearly cancels $\lambda = 0.24$, giving $T_c^{\mathrm{EFT}} = 5 \times 10^{-5}$ K. The precursory Cooper flow formalism (@precursory_cooper_flow) shows that near the quantum phase transition ($g \to 0$), $T_c = \omega_\Lambda e^{1/g}$ is exponentially sensitive to the coupling, explaining why small parameter variations can toggle between superconducting and non-superconducting ground states.
**action_label:** github:superconductivity_electron_liquids::action::_anon_action_029
**pattern:** derivation
**gaia:** {'provenance': {'referenced_claims': ['ab_initio_workflow', 'magnesium_parameters', 'precursory_cooper_flow', 'sodium_parameters']}}

### tc_al_predicted

**QID:** `github:superconductivity_electron_liquids::tc_al_predicted`
**Type:** claim
**Role:** derived
**Content:** The ab initio EFT framework predicts $T_c^{\mathrm{EFT}} = 1.14$ K for aluminum using $\lambda = 0.44$, $\mu^* = 0.13$ from vDiagMC + BTS, and $\omega_{\mathrm{log}} = 320$ K. The experimental value is $T_c^{\mathrm{exp}} = 1.2$ K.
**Belief:** 0.98
**Derived from:** deduction
**Premises:** `github:superconductivity_electron_liquids::ab_initio_workflow`

### github:superconductivity_electron_liquids::_anon_027

**QID:** `github:superconductivity_electron_liquids::_anon_027`
**Type:** claim
**Role:** orphaned
**Content:** derive warrants The ab initio EFT framework predicts $T_c^{\mathrm{EFT}} = 1.14$ K for aluminum using $\lambda = 0.44$, $\mu^* = 0.13$ from vDiagMC + BTS, and $\omega_{\mathrm{log}} = 320$ K. The experimental value is $T_c^{\mathrm{exp}} = 1.2$ K.
**Belief:** 0.50
**generated:** True
**helper_kind:** implication_warrant
**review:** True
**relation:** {'type': 'derive', 'given': ['github:superconductivity_electron_liquids::ab_initio_workflow'], 'conclusion': 'github:superconductivity_electron_liquids::tc_al_predicted'}
**warrant:** Plug Al's first-principles inputs into the McMillan estimator.
**action_label:** github:superconductivity_electron_liquids::action::tc_al_predicted
**pattern:** derivation

### tc_al_phenomenological

**QID:** `github:superconductivity_electron_liquids::tc_al_phenomenological`
**Type:** claim
**Role:** derived
**Content:** The phenomenological McMillan formula with the standard guess $\mu^* = 0.1$ predicts $T_c \approx 2.22$ K for aluminum, overestimating the experimental 1.2 K by ~85%.
**Belief:** 0.58
**Derived from:** deduction
**Premises:** `github:superconductivity_electron_liquids::phenomenological_me_theory`, `github:superconductivity_electron_liquids::mu_star_phenomenological`, `github:superconductivity_electron_liquids::dfpt_computes_lambda`

### github:superconductivity_electron_liquids::_anon_028

**QID:** `github:superconductivity_electron_liquids::_anon_028`
**Type:** claim
**Role:** orphaned
**Content:** derive warrants The phenomenological McMillan formula with the standard guess $\mu^* = 0.1$ predicts $T_c \approx 2.22$ K for aluminum, overestimating the experimental 1.2 K by ~85%.
**Belief:** 0.50
**generated:** True
**helper_kind:** implication_warrant
**review:** True
**relation:** {'type': 'derive', 'given': ['github:superconductivity_electron_liquids::phenomenological_me_theory', 'github:superconductivity_electron_liquids::mu_star_phenomenological', 'github:superconductivity_electron_liquids::dfpt_computes_lambda'], 'conclusion': 'github:superconductivity_electron_liquids::tc_al_phenomenological'}
**warrant:** McMillan with fixed empirical μ* = 0.1 applied to Al's λ, ω_log.
**action_label:** github:superconductivity_electron_liquids::action::tc_al_phenomenological
**pattern:** derivation

### tc_al_observation_binding

**QID:** `github:superconductivity_electron_liquids::tc_al_observation_binding`
**Type:** claim
**Role:** orphaned
**Content:** Experimental log Tc(Al) = log(1.2) = 0.1823.
**Prior:** 1.00
**Belief:** 1.00
**prior:** 0.999
**supported_by:** [{'action_label': 'github:superconductivity_electron_liquids::action::tc_al_observation', 'pattern': 'observation', 'warrants': ['github:superconductivity_electron_liquids::_anon_029'], 'background': ['github:superconductivity_electron_liquids::aluminum_parameters', 'github:superconductivity_electron_liquids::tc_al_experimental'], 'rationale': 'Well-established measurement: T_c(Al) = 1.2 K (@tc_al_experimental). Pin via log Tc binding so the Bayesian log-Tc likelihood comparison sees the data point.'}]
**formula_lowering:** atom
**formula_atom:** {'kind': 'equals', 'left': {'kind': 'variable', 'symbol': 'log_tc_al', 'domain': 'Real', 'value': 0.1823215567939546}, 'right': {'kind': 'constant', 'value': 0.1823215567939546, 'primitive': 'Real'}}
**formula_bindings:** [{'symbol': 'log_tc_al', 'domain': 'Real', 'value': 0.1823215567939546, 'source': 'formula'}]
**gaia:** {'provenance': {'referenced_claims': ['tc_al_experimental']}}

### github:superconductivity_electron_liquids::_anon_029

**QID:** `github:superconductivity_electron_liquids::_anon_029`
**Type:** claim
**Role:** orphaned
**Content:** observe warrants Experimental log Tc(Al) = log(1.2) = 0.1823.
**Belief:** 0.50
**generated:** True
**helper_kind:** implication_warrant
**review:** True
**relation:** {'type': 'observe', 'given': [], 'conclusion': 'github:superconductivity_electron_liquids::tc_al_observation_binding'}
**warrant:** Well-established measurement: T_c(Al) = 1.2 K (@tc_al_experimental). Pin via log Tc binding so the Bayesian log-Tc likelihood comparison sees the data point.
**action_label:** github:superconductivity_electron_liquids::action::tc_al_observation
**pattern:** observation

### eft_al_model

**QID:** `github:superconductivity_electron_liquids::eft_al_model`
**Type:** claim
**Role:** orphaned
**Content:** The complete ab initio workflow for predicting $T_c$ of simple metals: (1) compute $\mu_{E_F}$ from the UEG four-point vertex via vDiagMC, (2) map to the material's $r_s$ and run down to $\mu^*$ via the BTS relation, (3) obtain $\lambda$ from DFPT, (4) solve the downfolded Eliashberg equations (or use the PCF extrapolation) to predict $T_c$. All inputs are from first principles; no adjustable parameters remain. predicts log_tc_al under normal.
**Belief:** 0.50
**bayes:** {'role': 'prediction', 'distribution': {'kind': 'normal', 'params': {'mu': 0.13097714684141215, 'sigma': 0.22264914734375021}}, 'hypothesis': 'github:superconductivity_electron_liquids::ab_initio_workflow', 'hypotheses': ['github:superconductivity_electron_liquids::ab_initio_workflow'], 'observable': {'symbol': 'log_tc_al', 'domain': 'Real'}}
**generated:** True
**helper_kind:** predictive_model
**review:** True
**reason:** EFT prediction: μ* = 0.13 (vDiagMC + BTS) → Tc ≈ 1.14 K via McMillan. Per-material σ propagated from μ*_EFT ±5% relative precision.
**review_target:** {'action_label': 'github:superconductivity_electron_liquids::action::eft_al_model', 'pattern': 'prediction'}

### mcmillan_al_model

**QID:** `github:superconductivity_electron_liquids::mcmillan_al_model`
**Type:** claim
**Role:** orphaned
**Content:** Traditional electron-phonon superconductivity theory uses the McMillan (or Allen-Dynes) formula, with the electron-phonon coupling constant $\lambda$ and Coulomb pseudopotential $\mu^*$ as inputs to predict the superconducting transition temperature $T_c$. Since $\mu^*$ cannot be reliably computed from first principles, it is typically assigned an empirical value $\mu^* \in [0.1, 0.2]$. For materials with $T_c$ in the sub-kelvin range, the exponential sensitivity $T_c \propto \exp(-1/g)$ to $\mu^*$ causes this uncertainty to span several orders of magnitude in the predicted $T_c$, destroying predictive power. predicts log_tc_al under normal.
**Belief:** 0.50
**bayes:** {'role': 'prediction', 'distribution': {'kind': 'normal', 'params': {'mu': -0.6343926251568459, 'sigma': 1.164307803298898}}, 'hypothesis': 'github:superconductivity_electron_liquids::phenomenological_me_theory', 'hypotheses': ['github:superconductivity_electron_liquids::phenomenological_me_theory'], 'observable': {'symbol': 'log_tc_al', 'domain': 'Real'}}
**generated:** True
**helper_kind:** predictive_model
**review:** True
**reason:** Traditional McMillan: μ* ~ Uniform[0.1, 0.2] propagated through the formula gives a log-Tc Gaussian with much wider σ than the EFT model.
**review_target:** {'action_label': 'github:superconductivity_electron_liquids::action::mcmillan_al_model', 'pattern': 'prediction'}

### tc_al_likelihood

**QID:** `github:superconductivity_electron_liquids::tc_al_likelihood`
**Type:** claim
**Role:** derived
**Content:** Bayes likelihood comparison.
**Prior:** 1.00
**Belief:** 1.00
**Derived from:** infer
**Premises:** `github:superconductivity_electron_liquids::ab_initio_workflow`
**Derived from:** infer
**Premises:** `github:superconductivity_electron_liquids::phenomenological_me_theory`
**bayes:** {'role': 'comparison', 'exclusivity': 'none', 'likelihoods': {'github:superconductivity_electron_liquids::ab_initio_workflow': 0.5566297928427468, 'github:superconductivity_electron_liquids::phenomenological_me_theory': -1.3170876444417214}, 'data': ['github:superconductivity_electron_liquids::tc_al_observation_binding'], 'model': 'github:superconductivity_electron_liquids::eft_al_model', 'against': ['github:superconductivity_electron_liquids::mcmillan_al_model'], 'hypotheses': ['github:superconductivity_electron_liquids::ab_initio_workflow', 'github:superconductivity_electron_liquids::phenomenological_me_theory']}
**generated:** True
**helper_kind:** model_preference
**review:** True
**reason:** Likelihood of the observed log Tc(Al) = ln(1.2) under the EFT Normal model versus the propagated-McMillan Normal model. The EFT predictive Gaussian is both centred closer to the observation and much narrower, yielding a clear Bayes factor in favour of EFT.
**prior:** 0.999

### tc_zn_predicted

**QID:** `github:superconductivity_electron_liquids::tc_zn_predicted`
**Type:** claim
**Role:** derived
**Content:** The ab initio EFT framework predicts $T_c^{\mathrm{EFT}} = 0.995$ K for zinc using $\lambda = 0.502$, $\mu^* = 0.12$, and $\omega_{\mathrm{log}} = 111$ K. The experimental value is $T_c^{\mathrm{exp}} = 0.875$ K.
**Belief:** 0.98
**Derived from:** deduction
**Premises:** `github:superconductivity_electron_liquids::ab_initio_workflow`

### github:superconductivity_electron_liquids::_anon_030

**QID:** `github:superconductivity_electron_liquids::_anon_030`
**Type:** claim
**Role:** orphaned
**Content:** derive warrants The ab initio EFT framework predicts $T_c^{\mathrm{EFT}} = 0.995$ K for zinc using $\lambda = 0.502$, $\mu^* = 0.12$, and $\omega_{\mathrm{log}} = 111$ K. The experimental value is $T_c^{\mathrm{exp}} = 0.875$ K.
**Belief:** 0.50
**generated:** True
**helper_kind:** implication_warrant
**review:** True
**relation:** {'type': 'derive', 'given': ['github:superconductivity_electron_liquids::ab_initio_workflow'], 'conclusion': 'github:superconductivity_electron_liquids::tc_zn_predicted'}
**warrant:** Plug Zn's first-principles inputs into the McMillan estimator.
**action_label:** github:superconductivity_electron_liquids::action::tc_zn_predicted
**pattern:** derivation

### tc_zn_phenomenological

**QID:** `github:superconductivity_electron_liquids::tc_zn_phenomenological`
**Type:** claim
**Role:** derived
**Content:** The phenomenological McMillan formula with the standard guess $\mu^* = 0.1$ predicts $T_c \approx 1.37$ K for zinc, overestimating the experimental 0.875 K by ~57%.
**Belief:** 0.58
**Derived from:** deduction
**Premises:** `github:superconductivity_electron_liquids::phenomenological_me_theory`, `github:superconductivity_electron_liquids::mu_star_phenomenological`, `github:superconductivity_electron_liquids::dfpt_computes_lambda`

### github:superconductivity_electron_liquids::_anon_031

**QID:** `github:superconductivity_electron_liquids::_anon_031`
**Type:** claim
**Role:** orphaned
**Content:** derive warrants The phenomenological McMillan formula with the standard guess $\mu^* = 0.1$ predicts $T_c \approx 1.37$ K for zinc, overestimating the experimental 0.875 K by ~57%.
**Belief:** 0.50
**generated:** True
**helper_kind:** implication_warrant
**review:** True
**relation:** {'type': 'derive', 'given': ['github:superconductivity_electron_liquids::phenomenological_me_theory', 'github:superconductivity_electron_liquids::mu_star_phenomenological', 'github:superconductivity_electron_liquids::dfpt_computes_lambda'], 'conclusion': 'github:superconductivity_electron_liquids::tc_zn_phenomenological'}
**warrant:** McMillan with fixed empirical μ* = 0.1 applied to Zn's λ, ω_log.
**action_label:** github:superconductivity_electron_liquids::action::tc_zn_phenomenological
**pattern:** derivation

### tc_zn_observation_binding

**QID:** `github:superconductivity_electron_liquids::tc_zn_observation_binding`
**Type:** claim
**Role:** orphaned
**Content:** Experimental log Tc(Zn) = log(0.875) = -0.1335.
**Prior:** 1.00
**Belief:** 1.00
**prior:** 0.999
**supported_by:** [{'action_label': 'github:superconductivity_electron_liquids::action::tc_zn_observation', 'pattern': 'observation', 'warrants': ['github:superconductivity_electron_liquids::_anon_032'], 'background': ['github:superconductivity_electron_liquids::zinc_parameters', 'github:superconductivity_electron_liquids::tc_zn_experimental'], 'rationale': 'Well-established measurement: T_c(Zn) = 0.875 K (@tc_zn_experimental); pinned via log Tc binding.'}]
**formula_lowering:** atom
**formula_atom:** {'kind': 'equals', 'left': {'kind': 'variable', 'symbol': 'log_tc_zn', 'domain': 'Real', 'value': -0.13353139262452263}, 'right': {'kind': 'constant', 'value': -0.13353139262452263, 'primitive': 'Real'}}
**formula_bindings:** [{'symbol': 'log_tc_zn', 'domain': 'Real', 'value': -0.13353139262452263, 'source': 'formula'}]
**gaia:** {'provenance': {'referenced_claims': ['tc_zn_experimental']}}

### github:superconductivity_electron_liquids::_anon_032

**QID:** `github:superconductivity_electron_liquids::_anon_032`
**Type:** claim
**Role:** orphaned
**Content:** observe warrants Experimental log Tc(Zn) = log(0.875) = -0.1335.
**Belief:** 0.50
**generated:** True
**helper_kind:** implication_warrant
**review:** True
**relation:** {'type': 'observe', 'given': [], 'conclusion': 'github:superconductivity_electron_liquids::tc_zn_observation_binding'}
**warrant:** Well-established measurement: T_c(Zn) = 0.875 K (@tc_zn_experimental); pinned via log Tc binding.
**action_label:** github:superconductivity_electron_liquids::action::tc_zn_observation
**pattern:** observation

### eft_zn_model

**QID:** `github:superconductivity_electron_liquids::eft_zn_model`
**Type:** claim
**Role:** orphaned
**Content:** The complete ab initio workflow for predicting $T_c$ of simple metals: (1) compute $\mu_{E_F}$ from the UEG four-point vertex via vDiagMC, (2) map to the material's $r_s$ and run down to $\mu^*$ via the BTS relation, (3) obtain $\lambda$ from DFPT, (4) solve the downfolded Eliashberg equations (or use the PCF extrapolation) to predict $T_c$. All inputs are from first principles; no adjustable parameters remain. predicts log_tc_zn under normal.
**Belief:** 0.50
**bayes:** {'role': 'prediction', 'distribution': {'kind': 'normal', 'params': {'mu': -0.0051417433520239055, 'sigma': 0.18225082985795032}}, 'hypothesis': 'github:superconductivity_electron_liquids::ab_initio_workflow', 'hypotheses': ['github:superconductivity_electron_liquids::ab_initio_workflow'], 'observable': {'symbol': 'log_tc_zn', 'domain': 'Real'}}
**generated:** True
**helper_kind:** predictive_model
**review:** True
**reason:** EFT prediction: μ* = 0.12 (vDiagMC + BTS) → Tc ≈ 0.99 K.
**review_target:** {'action_label': 'github:superconductivity_electron_liquids::action::eft_zn_model', 'pattern': 'prediction'}

### mcmillan_zn_model

**QID:** `github:superconductivity_electron_liquids::mcmillan_zn_model`
**Type:** claim
**Role:** orphaned
**Content:** Traditional electron-phonon superconductivity theory uses the McMillan (or Allen-Dynes) formula, with the electron-phonon coupling constant $\lambda$ and Coulomb pseudopotential $\mu^*$ as inputs to predict the superconducting transition temperature $T_c$. Since $\mu^*$ cannot be reliably computed from first principles, it is typically assigned an empirical value $\mu^* \in [0.1, 0.2]$. For materials with $T_c$ in the sub-kelvin range, the exponential sensitivity $T_c \propto \exp(-1/g)$ to $\mu^*$ causes this uncertainty to span several orders of magnitude in the predicted $T_c$, destroying predictive power. predicts log_tc_zn under normal.
**Belief:** 0.50
**bayes:** {'role': 'prediction', 'distribution': {'kind': 'normal', 'params': {'mu': -0.7118955805512239, 'sigma': 0.8154605829764926}}, 'hypothesis': 'github:superconductivity_electron_liquids::phenomenological_me_theory', 'hypotheses': ['github:superconductivity_electron_liquids::phenomenological_me_theory'], 'observable': {'symbol': 'log_tc_zn', 'domain': 'Real'}}
**generated:** True
**helper_kind:** predictive_model
**review:** True
**reason:** Traditional McMillan: μ* ~ Uniform[0.1, 0.2] propagated for Zn.
**review_target:** {'action_label': 'github:superconductivity_electron_liquids::action::mcmillan_zn_model', 'pattern': 'prediction'}

### tc_zn_likelihood

**QID:** `github:superconductivity_electron_liquids::tc_zn_likelihood`
**Type:** claim
**Role:** derived
**Content:** Bayes likelihood comparison.
**Prior:** 1.00
**Belief:** 1.00
**Derived from:** infer
**Premises:** `github:superconductivity_electron_liquids::ab_initio_workflow`
**Derived from:** infer
**Premises:** `github:superconductivity_electron_liquids::phenomenological_me_theory`
**bayes:** {'role': 'comparison', 'exclusivity': 'none', 'likelihoods': {'github:superconductivity_electron_liquids::ab_initio_workflow': 0.5352961225859068, 'github:superconductivity_electron_liquids::phenomenological_me_theory': -0.9664530512987194}, 'data': ['github:superconductivity_electron_liquids::tc_zn_observation_binding'], 'model': 'github:superconductivity_electron_liquids::eft_zn_model', 'against': ['github:superconductivity_electron_liquids::mcmillan_zn_model'], 'hypotheses': ['github:superconductivity_electron_liquids::ab_initio_workflow', 'github:superconductivity_electron_liquids::phenomenological_me_theory']}
**generated:** True
**helper_kind:** model_preference
**review:** True
**reason:** Likelihood of log Tc(Zn) under EFT vs propagated-McMillan. EFT centres almost on the observation with a tight Gaussian; McMillan is offset and broad.
**prior:** 0.999

### tc_li_predicted

**QID:** `github:superconductivity_electron_liquids::tc_li_predicted`
**Type:** claim
**Role:** derived
**Content:** The ab initio EFT framework predicts $T_c^{\mathrm{EFT}} \approx 2.2e-03$ K for lithium (9R) using $\lambda = 0.34$, $\mu^* = 0.18$, and $\omega_{\mathrm{log}} = 242$ K. The large $\mu^*$ from $r_s = 3.25$ nearly cancels the moderate $\lambda$, pushing $T_c$ into the sub-mK regime. Experimental: $T_c \approx 4e-04$ K.
**Belief:** 0.86
**Derived from:** deduction
**Premises:** `github:superconductivity_electron_liquids::ab_initio_workflow`, `github:superconductivity_electron_liquids::li_is_superconducting`

### github:superconductivity_electron_liquids::_anon_033

**QID:** `github:superconductivity_electron_liquids::_anon_033`
**Type:** claim
**Role:** orphaned
**Content:** derive warrants The ab initio EFT framework predicts $T_c^{\mathrm{EFT}} \approx 2.2e-03$ K for lithium (9R) using $\lambda = 0.34$, $\mu^* = 0.18$, and $\omega_{\mathrm{log}} = 242$ K. The large $\mu^*$ from $r_s = 3.25$ nearly cancels the moderate $\lambda$, pushing $T_c$ into the sub-mK regime. Experimental: $T_c \approx 4e-04$ K.
**Belief:** 0.50
**generated:** True
**helper_kind:** implication_warrant
**review:** True
**relation:** {'type': 'derive', 'given': ['github:superconductivity_electron_liquids::ab_initio_workflow', 'github:superconductivity_electron_liquids::li_is_superconducting'], 'conclusion': 'github:superconductivity_electron_liquids::tc_li_predicted'}
**warrant:** Plug Li's first-principles inputs into the McMillan estimator; near-cancellation of g amplifies parameter sensitivity exponentially. Conditional on @li_is_superconducting because the predicted Tc value only carries operational meaning if the observed sub-mK resistive anomaly is in fact a bulk SC transition rather than a non-SC artifact.
**action_label:** github:superconductivity_electron_liquids::action::tc_li_predicted
**pattern:** derivation
**gaia:** {'provenance': {'referenced_claims': ['li_is_superconducting']}}

### tc_li_phenomenological

**QID:** `github:superconductivity_electron_liquids::tc_li_phenomenological`
**Type:** claim
**Role:** derived
**Content:** The phenomenological McMillan formula with $\mu^* = 0.1$ predicts $T_c \approx 0.35$ K for lithium, overestimating the experimental 4e-04 K by three orders of magnitude.
**Belief:** 0.56
**Derived from:** deduction
**Premises:** `github:superconductivity_electron_liquids::phenomenological_me_theory`, `github:superconductivity_electron_liquids::mu_star_phenomenological`, `github:superconductivity_electron_liquids::dfpt_computes_lambda`, `github:superconductivity_electron_liquids::li_is_superconducting`

### github:superconductivity_electron_liquids::_anon_034

**QID:** `github:superconductivity_electron_liquids::_anon_034`
**Type:** claim
**Role:** orphaned
**Content:** derive warrants The phenomenological McMillan formula with $\mu^* = 0.1$ predicts $T_c \approx 0.35$ K for lithium, overestimating the experimental 4e-04 K by three orders of magnitude.
**Belief:** 0.50
**generated:** True
**helper_kind:** implication_warrant
**review:** True
**relation:** {'type': 'derive', 'given': ['github:superconductivity_electron_liquids::phenomenological_me_theory', 'github:superconductivity_electron_liquids::mu_star_phenomenological', 'github:superconductivity_electron_liquids::dfpt_computes_lambda', 'github:superconductivity_electron_liquids::li_is_superconducting'], 'conclusion': 'github:superconductivity_electron_liquids::tc_li_phenomenological'}
**warrant:** McMillan with fixed empirical μ* = 0.1 applied to Li's λ, ω_log; conditional on @li_is_superconducting for the same reason as the EFT prediction.
**action_label:** github:superconductivity_electron_liquids::action::tc_li_phenomenological
**pattern:** derivation
**gaia:** {'provenance': {'referenced_claims': ['li_is_superconducting']}}

### tc_li_observation_binding

**QID:** `github:superconductivity_electron_liquids::tc_li_observation_binding`
**Type:** claim
**Role:** derived
**Content:** Experimental log Tc(Li) = log(4e-04) = -7.8240.
**Belief:** 0.75
**Derived from:** deduction
**Premises:** `github:superconductivity_electron_liquids::li_crystal_structure_at_low_t`
**formula_lowering:** atom
**formula_atom:** {'kind': 'equals', 'left': {'kind': 'variable', 'symbol': 'log_tc_li', 'domain': 'Real', 'value': -7.824046010856292}, 'right': {'kind': 'constant', 'value': -7.824046010856292, 'primitive': 'Real'}}
**formula_bindings:** [{'symbol': 'log_tc_li', 'domain': 'Real', 'value': -7.824046010856292, 'source': 'formula'}]

### github:superconductivity_electron_liquids::_anon_035

**QID:** `github:superconductivity_electron_liquids::_anon_035`
**Type:** claim
**Role:** orphaned
**Content:** observe warrants Experimental log Tc(Li) = log(4e-04) = -7.8240.
**Belief:** 0.50
**generated:** True
**helper_kind:** implication_warrant
**review:** True
**relation:** {'type': 'observe', 'given': ['github:superconductivity_electron_liquids::li_crystal_structure_at_low_t'], 'conclusion': 'github:superconductivity_electron_liquids::tc_li_observation_binding'}
**warrant:** Experimental T_c(Li) ≈ 4×10⁻⁴ K (@tc_li_experimental, 9R structure). Conditional on @li_crystal_structure_at_low_t — the sample's structural identification at sub-Kelvin temperature is uncertain, so the log Tc pin is conditional rather than unconditional.
**action_label:** github:superconductivity_electron_liquids::action::tc_li_observation
**pattern:** observation
**gaia:** {'provenance': {'referenced_claims': ['li_crystal_structure_at_low_t', 'tc_li_experimental']}}

### eft_li_model

**QID:** `github:superconductivity_electron_liquids::eft_li_model`
**Type:** claim
**Role:** orphaned
**Content:** The complete ab initio workflow for predicting $T_c$ of simple metals: (1) compute $\mu_{E_F}$ from the UEG four-point vertex via vDiagMC, (2) map to the material's $r_s$ and run down to $\mu^*$ via the BTS relation, (3) obtain $\lambda$ from DFPT, (4) solve the downfolded Eliashberg equations (or use the PCF extrapolation) to predict $T_c$. All inputs are from first principles; no adjustable parameters remain. predicts log_tc_li under normal.
**Belief:** 0.50
**bayes:** {'role': 'prediction', 'distribution': {'kind': 'normal', 'params': {'mu': -6.111093734288051, 'sigma': 1.0384581044882149}}, 'hypothesis': 'github:superconductivity_electron_liquids::ab_initio_workflow', 'hypotheses': ['github:superconductivity_electron_liquids::ab_initio_workflow'], 'observable': {'symbol': 'log_tc_li', 'domain': 'Real'}}
**generated:** True
**helper_kind:** predictive_model
**review:** True
**reason:** EFT prediction: μ* = 0.18 (vDiagMC + BTS) → Tc ≈ 2e-3 K. Note: σ for Li is large because the exponential sensitivity to g near the QPT magnifies any μ*_EFT uncertainty. Comparison is only meaningful given @li_is_superconducting; non-SC explanations of the resistive anomaly would invalidate the log-Tc framing.
**review_target:** {'action_label': 'github:superconductivity_electron_liquids::action::eft_li_model', 'pattern': 'prediction'}
**gaia:** {'provenance': {'referenced_claims': ['li_is_superconducting']}}

### mcmillan_li_model

**QID:** `github:superconductivity_electron_liquids::mcmillan_li_model`
**Type:** claim
**Role:** orphaned
**Content:** Traditional electron-phonon superconductivity theory uses the McMillan (or Allen-Dynes) formula, with the electron-phonon coupling constant $\lambda$ and Coulomb pseudopotential $\mu^*$ as inputs to predict the superconducting transition temperature $T_c$. Since $\mu^*$ cannot be reliably computed from first principles, it is typically assigned an empirical value $\mu^* \in [0.1, 0.2]$. For materials with $T_c$ in the sub-kelvin range, the exponential sensitivity $T_c \propto \exp(-1/g)$ to $\mu^*$ causes this uncertainty to span several orders of magnitude in the predicted $T_c$, destroying predictive power. predicts log_tc_li under normal.
**Belief:** 0.50
**bayes:** {'role': 'prediction', 'distribution': {'kind': 'normal', 'params': {'mu': -4.2281690807535455, 'sigma': 2.7990684105141512}}, 'hypothesis': 'github:superconductivity_electron_liquids::phenomenological_me_theory', 'hypotheses': ['github:superconductivity_electron_liquids::phenomenological_me_theory'], 'observable': {'symbol': 'log_tc_li', 'domain': 'Real'}}
**generated:** True
**helper_kind:** predictive_model
**review:** True
**reason:** Traditional McMillan: μ* ~ Uniform[0.1, 0.2] propagated for Li; near-QPT exponential sensitivity gives a very broad log-Tc spread. Conditional on @li_is_superconducting (same caveat as eft_li_model).
**review_target:** {'action_label': 'github:superconductivity_electron_liquids::action::mcmillan_li_model', 'pattern': 'prediction'}
**gaia:** {'provenance': {'referenced_claims': ['li_is_superconducting']}}

### tc_li_likelihood

**QID:** `github:superconductivity_electron_liquids::tc_li_likelihood`
**Type:** claim
**Role:** derived
**Content:** Bayes likelihood comparison.
**Prior:** 1.00
**Belief:** 1.00
**Derived from:** infer
**Premises:** `github:superconductivity_electron_liquids::ab_initio_workflow`
**Derived from:** infer
**Premises:** `github:superconductivity_electron_liquids::phenomenological_me_theory`
**bayes:** {'role': 'comparison', 'exclusivity': 'none', 'likelihoods': {'github:superconductivity_electron_liquids::ab_initio_workflow': -2.3171255115027525, 'github:superconductivity_electron_liquids::phenomenological_me_theory': -2.7734126402905606}, 'data': ['github:superconductivity_electron_liquids::tc_li_observation_binding'], 'model': 'github:superconductivity_electron_liquids::eft_li_model', 'against': ['github:superconductivity_electron_liquids::mcmillan_li_model'], 'hypotheses': ['github:superconductivity_electron_liquids::ab_initio_workflow', 'github:superconductivity_electron_liquids::phenomenological_me_theory']}
**generated:** True
**helper_kind:** model_preference
**review:** True
**reason:** Likelihood of log Tc(Li) under EFT vs propagated-McMillan. Li is the hard case: both predictive distributions are off by 1.3-1.7 σ, with EFT narrowly preferred — illustrating the limits of any method in the near-cancellation regime.
**prior:** 0.999
