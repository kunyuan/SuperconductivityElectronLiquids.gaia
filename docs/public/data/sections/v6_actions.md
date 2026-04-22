# Module: v6_actions

### adiabatic_approx

**QID:** `github:superconductivity_electron_liquids::adiabatic_approx`
**Type:** claim
**Role:** independent
**Content:** In conventional metals, the typical phonon frequency (Debye frequency $\omega_D$) is much smaller than the electron Fermi energy $E_F$, i.e. $\omega_D / E_F \ll 1$ (adiabatic approximation). This energy-scale separation has three key consequences: (i) electrons adiabatically adjust to ionic motion, (ii) the electron-ion coupling can be linearized, and (iii) the space-time scale separation between electron and phonon physics permits a controlled effective field theory (EFT) treatment.
**Prior:** 0.95
**Belief:** 0.96
**prior:** 0.95
**prior_justification:** omega_D/E_F is small for conventional simple metals.
**grounding:** {'kind': 'source_fact', 'rationale': 'Authored scientific assertion imported from the electron-liquids package.', 'source_refs': [], 'action_label': 'github:superconductivity_electron_liquids::action::_anon_action_000', 'pattern': 'observation'}
**Referenced by:** deduction -> `github:superconductivity_electron_liquids::me_framework`

### me_framework

**QID:** `github:superconductivity_electron_liquids::me_framework`
**Type:** claim
**Role:** derived
**Content:** Migdal-Eliashberg (ME) theory provides a rigorous treatment of the dynamic electron-phonon interaction. Under the adiabatic condition $\omega_D / E_F \ll 1$, Migdal's theorem guarantees that phonon vertex corrections are suppressed at $O(\omega_D/E_F)$, allowing the electron-phonon self-energy to be truncated at the self-consistent Fock diagram level. This justifies the ME formalism as a controlled low-energy theory for electron-phonon superconductors.
**Belief:** 0.98
**Derived from:** deduction
**Premises:** `github:superconductivity_electron_liquids::adiabatic_approx`
**grounding:** {'kind': 'source_fact', 'rationale': 'Authored scientific assertion imported from the electron-liquids package.', 'source_refs': [], 'action_label': 'github:superconductivity_electron_liquids::action::_anon_action_001', 'pattern': 'observation'}
**Referenced by:** deduction -> `github:superconductivity_electron_liquids::bse_kernel_decomposition`

### bts_renormalization

**QID:** `github:superconductivity_electron_liquids::bts_renormalization`
**Type:** claim
**Role:** independent
**Content:** The Bogoliubov-Tolmachev-Shirkov (BTS) renormalization relation connects the Coulomb pseudopotential $\mu_{\omega_c}$ (a dimensionless parameter describing the effective electron-electron repulsion strength in the pairing channel) defined at different energy cutoff scales $\omega_c$: $\mu_{\omega_c} = \mu_{\omega_c'} / (1 + \mu_{\omega_c'} \ln(\omega_c'/\omega_c))$. This relation ensures that physical observables do not depend on the choice of the arbitrary cutoff scale.
**Prior:** 0.95
**Belief:** 1.00
**prior:** 0.95
**prior_justification:** Standard BTS renormalization relation.
**grounding:** {'kind': 'source_fact', 'rationale': 'Authored scientific assertion imported from the electron-liquids package.', 'source_refs': [], 'action_label': 'github:superconductivity_electron_liquids::action::_anon_action_003', 'pattern': 'observation'}
**Referenced by:** unknown -> `github:superconductivity_electron_liquids::bts_microscopic_equivalence`

### me_downfolding_is_phenomenological

**QID:** `github:superconductivity_electron_liquids::me_downfolding_is_phenomenological`
**Type:** claim
**Role:** orphaned
**Content:** The downfolding procedure (integrating out high-energy degrees of freedom to obtain a low-energy effective theory) in traditional Migdal-Eliashberg (ME) theory is phenomenological: the Coulomb effect is replaced by a static pseudopotential $\mu^*$, ignoring corrections from Coulomb fluctuations to quasiparticle renormalization and electron-phonon coupling, as well as non-local effects of screening.
**Prior:** 0.95
**Belief:** 0.95
**prior:** 0.95
**prior_justification:** Established limitation of phenomenological ME downfolding.
**grounding:** {'kind': 'source_fact', 'rationale': 'Authored scientific assertion imported from the electron-liquids package.', 'source_refs': [], 'action_label': 'github:superconductivity_electron_liquids::action::_anon_action_004', 'pattern': 'observation'}

### phenomenological_me_theory

**QID:** `github:superconductivity_electron_liquids::phenomenological_me_theory`
**Type:** claim
**Role:** orphaned
**Content:** Traditional electron-phonon superconductivity theory uses the McMillan (or Allen-Dynes) formula, with the electron-phonon coupling constant $\lambda$ and Coulomb pseudopotential $\mu^*$ as inputs to predict the superconducting transition temperature $T_c$. Since $\mu^*$ cannot be reliably computed from first principles, it is typically assigned an empirical value $\mu^* \in [0.1, 0.2]$. For materials with $T_c$ in the sub-kelvin range, the exponential sensitivity $T_c \propto \exp(-1/g)$ to $\mu^*$ causes this uncertainty to span several orders of magnitude in the predicted $T_c$, destroying predictive power.
**Prior:** 0.95
**Belief:** 0.95
**prior:** 0.95
**prior_justification:** Standard description of McMillan/Allen-Dynes limitations.
**grounding:** {'kind': 'source_fact', 'rationale': 'Authored scientific assertion imported from the electron-liquids package.', 'source_refs': [], 'action_label': 'github:superconductivity_electron_liquids::action::_anon_action_005', 'pattern': 'observation'}

### mu_star_phenomenological

**QID:** `github:superconductivity_electron_liquids::mu_star_phenomenological`
**Type:** claim
**Role:** background
**Content:** Due to the lack of a reliable microscopic calculation, the Coulomb pseudopotential $\mu^*$ (a dimensionless parameter describing the effective Coulomb repulsion strength in the low-energy pairing channel) is typically treated as an adjustable parameter with empirical values in the range 0.1--0.2.
**Prior:** 0.95
**Belief:** 0.95
**prior:** 0.95
**prior_justification:** Standard treatment of mu* as an adjustable parameter.
**grounding:** {'kind': 'source_fact', 'rationale': 'Authored scientific assertion imported from the electron-liquids package.', 'source_refs': [], 'action_label': 'github:superconductivity_electron_liquids::action::_anon_action_006', 'pattern': 'observation'}

### rpa_predicts_attractive_mu

**QID:** `github:superconductivity_electron_liquids::rpa_predicts_attractive_mu`
**Type:** claim
**Role:** independent
**Content:** When treating the dynamically screened Coulomb interaction within the random phase approximation (RPA), the predicted $\mu^* < 0$ (i.e. the Coulomb effect becomes net attractive in the Cooper channel) for Wigner-Seitz radius $r_s \gtrsim 2$ ($r_s$ is proportional to the ratio of electron spacing to Bohr radius, measuring the ratio of Coulomb interaction to kinetic energy). However, RPA neglects beyond-RPA effects such as vertex corrections and self-energy renormalization for $r_s \gtrsim 1$, making its predictions unreliable in this density regime and inconsistent with extensive experimental evidence.
**Prior:** 0.50
**Belief:** 0.09
**prior:** 0.5
**prior_justification:** RPA calculation is reproducible but physically unreliable at larger r_s.
**grounding:** {'kind': 'source_fact', 'rationale': 'Authored scientific assertion imported from the electron-liquids package.', 'source_refs': [], 'action_label': 'github:superconductivity_electron_liquids::action::_anon_action_007', 'pattern': 'observation'}
**Referenced by:** unknown -> `github:superconductivity_electron_liquids::rpa_vs_vdiagmc`

### dfpt_computes_lambda

**QID:** `github:superconductivity_electron_liquids::dfpt_computes_lambda`
**Type:** claim
**Role:** background
**Content:** Density functional perturbation theory (DFPT) computes the electron-phonon coupling constant $\lambda$ (a dimensionless parameter quantifying the phonon-mediated attraction strength at the Fermi surface) via the linear response of the Kohn-Sham ground-state energy to lattice distortions. DFPT has been validated for weakly correlated superconductors but its accuracy for strongly correlated systems is unknown.
**Prior:** 0.92
**Belief:** 0.92
**prior:** 0.92
**prior_justification:** DFPT is established for weakly correlated metals.
**grounding:** {'kind': 'source_fact', 'rationale': 'Authored scientific assertion imported from the electron-liquids package.', 'source_refs': [], 'action_label': 'github:superconductivity_electron_liquids::action::_anon_action_008', 'pattern': 'observation'}

### tc_al_experimental

**QID:** `github:superconductivity_electron_liquids::tc_al_experimental`
**Type:** claim
**Role:** derived
**Content:** The experimental superconducting transition temperature of aluminum (Al) is $T_c^{\mathrm{exp}} = 1.2$ K.
**Prior:** 0.99
**Belief:** 1.00
**Derived from:** infer
**Premises:** `github:superconductivity_electron_liquids::tc_al_predicted`
**Derived from:** infer
**Premises:** `github:superconductivity_electron_liquids::tc_al_phenomenological`
**prior:** 0.99
**prior_justification:** Well-established aluminum transition temperature.
**grounding:** {'kind': 'source_fact', 'rationale': 'Authored scientific assertion imported from the electron-liquids package.', 'source_refs': [], 'action_label': 'github:superconductivity_electron_liquids::action::_anon_action_009', 'pattern': 'observation'}

### tc_li_experimental

**QID:** `github:superconductivity_electron_liquids::tc_li_experimental`
**Type:** claim
**Role:** derived
**Content:** The experimental superconducting transition temperature of lithium (Li) is $T_c^{\mathrm{exp}} \approx 4 \times 10^{-4}$ K (0.4 mK). This measurement corresponds to the 9R crystal structure; the crystal structure of lithium at ultra-low temperatures remains controversial.
**Prior:** 0.85
**Belief:** 0.78
**Derived from:** infer
**Premises:** `github:superconductivity_electron_liquids::tc_li_predicted`
**Derived from:** infer
**Premises:** `github:superconductivity_electron_liquids::tc_li_phenomenological`
**prior:** 0.85
**prior_justification:** Lithium transition is affected by low-temperature structure uncertainty.
**grounding:** {'kind': 'source_fact', 'rationale': 'Authored scientific assertion imported from the electron-liquids package.', 'source_refs': [], 'action_label': 'github:superconductivity_electron_liquids::action::_anon_action_010', 'pattern': 'observation'}

### tc_zn_experimental

**QID:** `github:superconductivity_electron_liquids::tc_zn_experimental`
**Type:** claim
**Role:** derived
**Content:** The experimental superconducting transition temperature of zinc (Zn) is $T_c^{\mathrm{exp}} = 0.875$ K.
**Prior:** 0.99
**Belief:** 1.00
**Derived from:** infer
**Premises:** `github:superconductivity_electron_liquids::tc_zn_predicted`
**Derived from:** infer
**Premises:** `github:superconductivity_electron_liquids::tc_zn_phenomenological`
**prior:** 0.99
**prior_justification:** Well-established zinc transition temperature.
**grounding:** {'kind': 'source_fact', 'rationale': 'Authored scientific assertion imported from the electron-liquids package.', 'source_refs': [], 'action_label': 'github:superconductivity_electron_liquids::action::_anon_action_011', 'pattern': 'observation'}

### tc_al_phenomenological

**QID:** `github:superconductivity_electron_liquids::tc_al_phenomenological`
**Type:** claim
**Role:** independent
**Content:** Using the McMillan formula (an empirical formula for $T_c$ based on the electron-phonon coupling constant $\lambda$ and Coulomb pseudopotential $\mu^*$), and treating the traditional empirical $\mu^*$ choice as uniformly distributed over 0.1--0.2, the predicted superconducting transition temperature of aluminum spans roughly $0.071$--$1.9$ K. The experimental value 1.2 K lies inside this broad interval, illustrating that the conventional prediction has adjustable rather than first-principles $\mu^*$ content.
**Prior:** 0.90
**Belief:** 0.78
**prior:** 0.9
**prior_justification:** McMillan calculation with conventional uniform mu* range is straightforward.
**grounding:** {'kind': 'source_fact', 'rationale': 'Authored scientific assertion imported from the electron-liquids package.', 'source_refs': [], 'action_label': 'github:superconductivity_electron_liquids::action::_anon_action_012', 'pattern': 'observation'}
**Referenced by:** infer -> `github:superconductivity_electron_liquids::tc_al_experimental`

### tc_li_phenomenological

**QID:** `github:superconductivity_electron_liquids::tc_li_phenomenological`
**Type:** claim
**Role:** independent
**Content:** Using the McMillan formula and treating the traditional empirical $\mu^*$ choice as uniformly distributed over 0.1--0.2, the predicted superconducting transition temperature of lithium spans roughly $1.3 \times 10^{-4}$--$0.35$ K. The experimental value is approximately $4 \times 10^{-4}$ K, so the range can cover the measurement only near its high-$\mu^*$ tail; the broad interval shows that the conventional prediction is dominated by the adjustable $\mu^*$ choice.
**Prior:** 0.90
**Belief:** 0.70
**prior:** 0.9
**prior_justification:** McMillan calculation with conventional uniform mu* range is straightforward.
**grounding:** {'kind': 'source_fact', 'rationale': 'Authored scientific assertion imported from the electron-liquids package.', 'source_refs': [], 'action_label': 'github:superconductivity_electron_liquids::action::_anon_action_013', 'pattern': 'observation'}
**Referenced by:** infer -> `github:superconductivity_electron_liquids::tc_li_experimental`

### tc_zn_phenomenological

**QID:** `github:superconductivity_electron_liquids::tc_zn_phenomenological`
**Type:** claim
**Role:** independent
**Content:** Using the McMillan formula and treating the traditional empirical $\mu^*$ choice as uniformly distributed over 0.1--0.2, the predicted superconducting transition temperature of zinc spans roughly $0.137$--$1.37$ K. The experimental value 0.875 K lies inside this broad interval, again indicating that the conventional prediction depends strongly on the empirical $\mu^*$ selection.
**Prior:** 0.90
**Belief:** 0.83
**prior:** 0.9
**prior_justification:** McMillan calculation with conventional uniform mu* range is straightforward.
**grounding:** {'kind': 'source_fact', 'rationale': 'Authored scientific assertion imported from the electron-liquids package.', 'source_refs': [], 'action_label': 'github:superconductivity_electron_liquids::action::_anon_action_014', 'pattern': 'observation'}
**Referenced by:** infer -> `github:superconductivity_electron_liquids::tc_zn_experimental`

### electron_phonon_action

**QID:** `github:superconductivity_electron_liquids::electron_phonon_action`
**Type:** claim
**Role:** background
**Content:** The effective action of the electron-phonon coupled system can be decomposed as $S = S_e + S_{\mathrm{ph}} + S_{e\text{-ph}} + S_{\mathrm{CT}} + O(\sqrt{m/M})$, where $m$ is the electron mass and $M$ is the ion mass. $S_e$ is the complete many-electron action without any approximation, $S_{\mathrm{ph}}$ describes phonons with physical dispersion, $S_{e\text{-ph}}$ is the coupling between electron density and ionic displacement, and $S_{\mathrm{CT}}$ is a counterterm that subtracts the static electron polarization contribution already included in the physical phonon dispersion to prevent double counting.
**Prior:** 0.95
**Belief:** 0.95
**prior:** 0.95
**prior_justification:** Standard effective action decomposition.
**grounding:** {'kind': 'source_fact', 'rationale': 'Authored scientific assertion imported from the electron-liquids package.', 'source_refs': [], 'action_label': 'github:superconductivity_electron_liquids::action::_anon_action_015', 'pattern': 'observation'}

### bse_kernel_decomposition

**QID:** `github:superconductivity_electron_liquids::bse_kernel_decomposition`
**Type:** claim
**Role:** derived
**Content:** The kernel of the Bethe-Salpeter equation (BSE) can be decomposed into the purely electronic particle-particle irreducible four-point vertex $\tilde\Gamma^e$ (encoding all non-perturbative Coulomb effects) and the phonon-mediated effective electron-electron interaction $W^{\mathrm{ph}}$: $\tilde\Gamma = \tilde\Gamma^e + W^{\mathrm{ph}} + O(\omega_D/E_F)$. Migdal's theorem ensures that higher-order phonon vertex corrections are suppressed by the adiabatic small parameter.
**Belief:** 0.99
**Derived from:** deduction
**Premises:** `github:superconductivity_electron_liquids::me_framework`
**grounding:** {'kind': 'source_fact', 'rationale': 'Authored scientific assertion imported from the electron-liquids package.', 'source_refs': [], 'action_label': 'github:superconductivity_electron_liquids::action::_anon_action_016', 'pattern': 'observation'}
**Referenced by:** deduction -> `github:superconductivity_electron_liquids::full_bse_toy_model`; deduction -> `github:superconductivity_electron_liquids::downfolded_bse`

### precursory_cooper_flow

**QID:** `github:superconductivity_electron_liquids::precursory_cooper_flow`
**Type:** claim
**Role:** background
**Content:** The low-frequency limit of the anomalous vertex function on the Fermi surface $\Lambda_0$ obeys a universal scaling relation (precursory Cooper flow, PCF): $\Lambda_0 = 1/(1 + g\ln(\omega_\Lambda/T)) + O(T)$, where $g$ is the dimensionless coupling constant ($g < 0$ corresponds to net attraction) and $\omega_\Lambda$ is an effective high-energy cutoff. When $g < 0$, $\Lambda_0$ diverges at $T_c = \omega_\Lambda e^{1/g}$; by computing in the normal state and extrapolating, one can predict $T_c$.
**Prior:** 0.90
**Belief:** 0.90
**prior:** 0.9
**prior_justification:** Normal-state extrapolation has been checked in the source work.
**grounding:** {'kind': 'source_fact', 'rationale': 'Authored scientific assertion imported from the electron-liquids package.', 'source_refs': [], 'action_label': 'github:superconductivity_electron_liquids::action::_anon_action_018', 'pattern': 'observation'}

### cross_term_suppressed

**QID:** `github:superconductivity_electron_liquids::cross_term_suppressed`
**Type:** claim
**Role:** independent
**Content:** Cross terms mixing Coulomb and phonon channels are suppressed by the plasma frequency $\omega_p$, at order $O(\omega_c^2/\omega_p^2)$, where $\omega_c$ is an intermediate energy cutoff satisfying $\omega_D \ll \omega_c \ll E_F$. For most three-dimensional metals $\omega_c/\omega_p \lesssim 0.1$, so cross terms contribute no more than 1%.
**Prior:** 0.90
**Belief:** 0.93
**prior:** 0.9
**prior_justification:** Plasmon-scale estimate suppresses cross-channel terms.
**grounding:** {'kind': 'source_fact', 'rationale': 'Authored scientific assertion imported from the electron-liquids package.', 'source_refs': [], 'action_label': 'github:superconductivity_electron_liquids::action::_anon_action_019', 'pattern': 'observation'}
**Referenced by:** deduction -> `github:superconductivity_electron_liquids::downfolded_bse`

### full_bse_toy_model

**QID:** `github:superconductivity_electron_liquids::full_bse_toy_model`
**Type:** claim
**Role:** derived
**Content:** For a toy model with aluminum-like parameters (Wigner-Seitz radius $r_s = 1.92$, adiabatic ratio $\omega_D/E_F = 0.005$), numerically solving the full frequency-momentum dependent Bethe-Salpeter equation (BSE) — using RPA dynamically screened Coulomb interaction as the electron irreducible vertex plus a model phonon interaction, without any downfolding approximation — yields a superconducting transition temperature $T_c^{\mathrm{full}}/T_F = 10^{-5.668}$, where $T_F$ is the Fermi temperature.
**Belief:** 1.00
**Derived from:** deduction
**Premises:** `github:superconductivity_electron_liquids::bse_kernel_decomposition`
**grounding:** {'kind': 'source_fact', 'rationale': 'Authored scientific assertion imported from the electron-liquids package.', 'source_refs': [], 'action_label': 'github:superconductivity_electron_liquids::action::_anon_action_020', 'pattern': 'observation'}
**Referenced by:** unknown -> `github:superconductivity_electron_liquids::_anon_000`

### downfolded_bse_toy_model

**QID:** `github:superconductivity_electron_liquids::downfolded_bse_toy_model`
**Type:** claim
**Role:** derived
**Content:** For the same toy model (aluminum-like parameters $r_s = 1.92$, $\omega_D/E_F = 0.005$), solving the downfolded frequency-only Bethe-Salpeter equation yields $T_c^{\mathrm{approx}}/T_F = 10^{-5.667}$, where $T_F$ is the Fermi temperature.
**Belief:** 1.00
**Derived from:** deduction
**Premises:** `github:superconductivity_electron_liquids::downfolded_bse`
**grounding:** {'kind': 'source_fact', 'rationale': 'Authored scientific assertion imported from the electron-liquids package.', 'source_refs': [], 'action_label': 'github:superconductivity_electron_liquids::action::_anon_action_022', 'pattern': 'observation'}
**Referenced by:** unknown -> `github:superconductivity_electron_liquids::_anon_000`

### github:superconductivity_electron_liquids::_anon_000

**QID:** `github:superconductivity_electron_liquids::_anon_000`
**Type:** claim
**Role:** structural
**Content:** For a toy model with aluminum-like parameters (Wigner-Seitz radius $r_s = 1.92$, adiabatic ratio $\omega_D/E_F = 0.005$), numerically solving the full frequency-momentum dependent Bethe-Salpeter equation (BSE) — using RPA dynamically screened Coulomb interaction as the electron irreducible vertex plus a model phonon interaction, without any downfolding approximation — yields a superconducting transition temperature $T_c^{\mathrm{full}}/T_F = 10^{-5.668}$, where $T_F$ is the Fermi temperature. and For the same toy model (aluminum-like parameters $r_s = 1.92$, $\omega_D/E_F = 0.005$), solving the downfolded frequency-only Bethe-Salpeter equation yields $T_c^{\mathrm{approx}}/T_F = 10^{-5.667}$, where $T_F$ is the Fermi temperature. are equivalent.
**Belief:** 1.00
**generated:** True
**helper_kind:** equivalence_result
**review:** True

### downfolding_validity_limits

**QID:** `github:superconductivity_electron_liquids::downfolding_validity_limits`
**Type:** claim
**Role:** orphaned
**Content:** The downfolded EFT-ME framework's applicability conditions and failure modes: (i) the adiabatic parameter $\omega_D/E_F \ll 1$ must hold, (ii) the intermediate cutoff $\omega_c$ must satisfy $\omega_D \ll \omega_c \ll E_F$ with $\omega_c/\omega_p \ll 1$, and (iii) the framework breaks down for strongly non-adiabatic systems (e.g. high-$T_c$ hydrides where $\omega_D/E_F \sim 0.1$) and for strongly correlated materials where the quasiparticle picture fails.
**Prior:** 0.92
**Belief:** 0.92
**prior:** 0.92
**prior_justification:** Applicability limits are well characterized by scale separation.
**grounding:** {'kind': 'source_fact', 'rationale': 'Authored scientific assertion imported from the electron-liquids package.', 'source_refs': [], 'action_label': 'github:superconductivity_electron_liquids::action::_anon_action_024', 'pattern': 'observation'}

### downfolded_bse

**QID:** `github:superconductivity_electron_liquids::downfolded_bse`
**Type:** claim
**Role:** derived
**Content:** The frequency-only downfolded Bethe-Salpeter equation: the full momentum-frequency BSE kernel reduces to a one-dimensional integral equation in Matsubara frequency, with an effective kernel $K(\omega, \omega') = \lambda(\omega, \omega') - \mu_{\omega_c}(\omega, \omega')$, where the phonon-mediated attraction $\lambda$ and Coulomb pseudopotential $\mu_{\omega_c}$ are microscopically defined. The momentum integration is absorbed into the density of states, and the pair propagator's coherent part generates the BCS logarithm that drives the Cooper instability.
**Belief:** 0.98
**Derived from:** deduction
**Premises:** `github:superconductivity_electron_liquids::cross_term_suppressed`, `github:superconductivity_electron_liquids::bse_kernel_decomposition`
**grounding:** {'kind': 'source_fact', 'rationale': 'Authored scientific assertion imported from the electron-liquids package.', 'source_refs': [], 'action_label': 'github:superconductivity_electron_liquids::action::_anon_action_025', 'pattern': 'observation'}
**Referenced by:** deduction -> `github:superconductivity_electron_liquids::downfolded_bse_toy_model`; deduction -> `github:superconductivity_electron_liquids::downfolded_me_equation`; deduction -> `github:superconductivity_electron_liquids::lambda_microscopic_definition`; deduction -> `github:superconductivity_electron_liquids::mu_microscopic_definition`; deduction -> `github:superconductivity_electron_liquids::ab_initio_workflow`

### downfolded_me_equation

**QID:** `github:superconductivity_electron_liquids::downfolded_me_equation`
**Type:** claim
**Role:** derived
**Content:** At the superconducting critical temperature $T_c$, the downfolded Bethe-Salpeter equation reduces to the traditional linearized Migdal-Eliashberg (ME) gap equation: $\Delta_\omega = \pi T_c \sum_{|\omega'|<\omega_c} (\lambda_{\omega\omega'} - \mu^*) \frac{z_{\omega'}^{\mathrm{ph}}}{|\omega'|} \Delta_{\omega'}$. As $T \to T_c$, the anomalous vertex diverges as $\Lambda_{k\omega} \sim \Delta_{k\omega}/(T - T_c)$, causing the source term $\eta$ to become irrelevant. The diverging prefactor $(T - T_c)^{-1}$ cancels between the two sides of the equation, yielding the gap equation with $\mu^* \equiv \mu_{\omega_c}$. This establishes the microscopic foundation for the ME equation with precise definitions of $\mu^*$ and $\lambda$ in terms of electron vertex functions.
**Belief:** 0.99
**Derived from:** deduction
**Premises:** `github:superconductivity_electron_liquids::downfolded_bse`
**grounding:** {'kind': 'source_fact', 'rationale': 'Authored scientific assertion imported from the electron-liquids package.', 'source_refs': [], 'action_label': 'github:superconductivity_electron_liquids::action::_anon_action_028', 'pattern': 'observation'}

### lambda_microscopic_definition

**QID:** `github:superconductivity_electron_liquids::lambda_microscopic_definition`
**Type:** claim
**Role:** derived
**Content:** The electron-phonon coupling $\lambda(\omega, \omega')$ in the downfolded BSE has a microscopic definition: it is the Fermi-surface average of the phonon-mediated interaction $W^{\mathrm{ph}}$ weighted by quasiparticle renormalization factors $z^e$ and $z_\omega^{\mathrm{ph}}$. This definition reduces to the standard Eliashberg $\lambda$ in the adiabatic limit but retains dynamical corrections from the electron self-energy.
**Belief:** 0.99
**Derived from:** deduction
**Premises:** `github:superconductivity_electron_liquids::downfolded_bse`
**grounding:** {'kind': 'source_fact', 'rationale': 'Authored scientific assertion imported from the electron-liquids package.', 'source_refs': [], 'action_label': 'github:superconductivity_electron_liquids::action::_anon_action_030', 'pattern': 'observation'}
**Referenced by:** deduction -> `github:superconductivity_electron_liquids::eft_eph_vertex`

### mu_microscopic_definition

**QID:** `github:superconductivity_electron_liquids::mu_microscopic_definition`
**Type:** claim
**Role:** derived
**Content:** The Coulomb pseudopotential $\mu_{\omega_c}(\omega, \omega')$ in the downfolded BSE has a microscopic definition: it is determined by the purely electronic particle-particle irreducible four-point vertex $\tilde\Gamma^e$ projected onto the Fermi surface, with the high-energy electronic degrees of freedom integrated out above the cutoff $\omega_c$. This gives $\mu_{\omega_c}$ a precise meaning as the effective Coulomb repulsion in the low-energy pairing channel, renormalized by all electronic correlations.
**Belief:** 0.99
**Derived from:** deduction
**Premises:** `github:superconductivity_electron_liquids::downfolded_bse`
**grounding:** {'kind': 'source_fact', 'rationale': 'Authored scientific assertion imported from the electron-liquids package.', 'source_refs': [], 'action_label': 'github:superconductivity_electron_liquids::action::_anon_action_032', 'pattern': 'observation'}
**Referenced by:** deduction -> `github:superconductivity_electron_liquids::mu_scale_independence`; deduction -> `github:superconductivity_electron_liquids::ma_pseudopotential_justified`

### mu_scale_independence

**QID:** `github:superconductivity_electron_liquids::mu_scale_independence`
**Type:** claim
**Role:** derived
**Content:** The BTS renormalization relation $\mu_{\omega_c} = \mu_{\omega_c'} / (1 + \mu_{\omega_c'} \ln(\omega_c'/\omega_c))$ emerges as a corollary of the microscopic definition of $\mu_{\omega_c}$: changing the cutoff $\omega_c$ reshuffles contributions between the explicit Coulomb kernel and the Cooper logarithm in the BCS propagator, leaving the physical $T_c$ invariant. This provides a microscopic derivation of the originally phenomenological BTS relation.
**Belief:** 1.00
**Derived from:** deduction
**Premises:** `github:superconductivity_electron_liquids::mu_microscopic_definition`
**grounding:** {'kind': 'source_fact', 'rationale': 'Authored scientific assertion imported from the electron-liquids package.', 'source_refs': [], 'action_label': 'github:superconductivity_electron_liquids::action::_anon_action_034', 'pattern': 'observation'}
**Referenced by:** unknown -> `github:superconductivity_electron_liquids::bts_microscopic_equivalence`

### bts_microscopic_equivalence

**QID:** `github:superconductivity_electron_liquids::bts_microscopic_equivalence`
**Type:** claim
**Role:** structural
**Content:** The BTS renormalization relation $\mu_{\omega_c} = \mu_{\omega_c'} / (1 + \mu_{\omega_c'} \ln(\omega_c'/\omega_c))$ emerges as a corollary of the microscopic definition of $\mu_{\omega_c}$: changing the cutoff $\omega_c$ reshuffles contributions between the explicit Coulomb kernel and the Cooper logarithm in the BCS propagator, leaving the physical $T_c$ invariant. This provides a microscopic derivation of the originally phenomenological BTS relation. and The Bogoliubov-Tolmachev-Shirkov (BTS) renormalization relation connects the Coulomb pseudopotential $\mu_{\omega_c}$ (a dimensionless parameter describing the effective electron-electron repulsion strength in the pairing channel) defined at different energy cutoff scales $\omega_c$: $\mu_{\omega_c} = \mu_{\omega_c'} / (1 + \mu_{\omega_c'} \ln(\omega_c'/\omega_c))$. This relation ensures that physical observables do not depend on the choice of the arbitrary cutoff scale. are equivalent.
**Belief:** 1.00
**generated:** True
**helper_kind:** equivalence_result
**review:** True

### ma_pseudopotential_justified

**QID:** `github:superconductivity_electron_liquids::ma_pseudopotential_justified`
**Type:** claim
**Role:** derived
**Content:** The Morel-Anderson constant-pseudopotential ansatz — treating $\mu_{\omega_c}$ as approximately frequency-independent — is microscopically justified: the four-point vertex $\tilde\Gamma^e$ varies on electronic energy scales ($E_F$), which are much larger than the phonon scale ($\omega_D$). Within the low-energy window $|\omega|, |\omega'| < \omega_c \ll E_F$, the Coulomb kernel is effectively constant, validating the traditional constant-$\mu^*$ treatment used in Eliashberg theory.
**Belief:** 1.00
**Derived from:** deduction
**Premises:** `github:superconductivity_electron_liquids::mu_microscopic_definition`
**grounding:** {'kind': 'source_fact', 'rationale': 'Authored scientific assertion imported from the electron-liquids package.', 'source_refs': [], 'action_label': 'github:superconductivity_electron_liquids::action::_anon_action_037', 'pattern': 'observation'}

### ueg_vertex_challenge

**QID:** `github:superconductivity_electron_liquids::ueg_vertex_challenge`
**Type:** claim
**Role:** background
**Content:** Computing the particle-particle irreducible four-point vertex $\tilde\Gamma^e$ of the uniform electron gas (UEG) is a long-standing challenge: perturbation theory in the bare Coulomb interaction diverges for $r_s \gtrsim 1$, and partial resummations (RPA, GW) miss crucial vertex corrections. A controlled, systematically improvable method is needed to evaluate $\tilde\Gamma^e$ in the metallic density range $r_s \in [1, 6]$.
**Prior:** 0.95
**Belief:** 0.95
**prior:** 0.95
**prior_justification:** Recognized difficulty of the UEG four-point vertex.
**grounding:** {'kind': 'source_fact', 'rationale': 'Authored scientific assertion imported from the electron-liquids package.', 'source_refs': [], 'action_label': 'github:superconductivity_electron_liquids::action::_anon_action_039', 'pattern': 'observation'}

### vdiagmc_method

**QID:** `github:superconductivity_electron_liquids::vdiagmc_method`
**Type:** claim
**Role:** independent
**Content:** Variational diagrammatic Monte Carlo (vDiagMC) provides a controlled, systematically improvable method for computing Feynman diagrammatic series to high order: (i) bold-line (self-consistent) resummation avoids infrared divergences in individual diagrams, (ii) stochastic sampling of diagram topologies and internal variables accesses orders unreachable by deterministic methods, (iii) the series can be extrapolated to infinite order with controlled error bars. For the UEG, vDiagMC achieves reliable convergence of the irreducible vertex in the metallic density range.
**Prior:** 0.90
**Belief:** 0.87
**prior:** 0.9
**prior_justification:** Controlled diagrammatic method in the metallic density range.
**grounding:** {'kind': 'source_fact', 'rationale': 'Authored scientific assertion imported from the electron-liquids package.', 'source_refs': [], 'action_label': 'github:superconductivity_electron_liquids::action::_anon_action_040', 'pattern': 'observation'}
**Referenced by:** deduction -> `github:superconductivity_electron_liquids::mu_vdiagmc_values`

### homotopic_expansion

**QID:** `github:superconductivity_electron_liquids::homotopic_expansion`
**Type:** claim
**Role:** independent
**Content:** The homotopic transformation provides a physically motivated reorganization of the diagrammatic series: by continuously deforming the bare Coulomb interaction $v(q)$ into a form that incorporates partial screening at each perturbative order, the series convergence is dramatically improved. This allows the vDiagMC calculation to reach converged results for the four-point vertex at metallic densities with modest diagram orders ($n \lesssim 7$).
**Prior:** 0.88
**Belief:** 0.85
**prior:** 0.88
**prior_justification:** Series reorganization improves convergence with some analyticity assumptions.
**grounding:** {'kind': 'source_fact', 'rationale': 'Authored scientific assertion imported from the electron-liquids package.', 'source_refs': [], 'action_label': 'github:superconductivity_electron_liquids::action::_anon_action_041', 'pattern': 'observation'}
**Referenced by:** deduction -> `github:superconductivity_electron_liquids::mu_vdiagmc_values`

### mu_vdiagmc_values

**QID:** `github:superconductivity_electron_liquids::mu_vdiagmc_values`
**Type:** claim
**Role:** derived
**Content:** vDiagMC calculations of the UEG four-point vertex yield the Coulomb pseudopotential at the Fermi energy scale: $\mu_{E_F}(r_s)$ is positive and monotonically increasing with $r_s$ in the metallic density range. Representative values include $\mu_{E_F} \approx 0.21$ at $r_s = 2$ (aluminum-like) and $\mu_{E_F} \approx 0.33$ at $r_s = 3.3$ (lithium-like). These results, combined with the BTS relation, yield $\mu^* \approx 0.10$--$0.15$ at the Debye scale, consistent with the empirical range but now derived from first principles with controlled error bars of a few percent.
**Belief:** 0.83
**Derived from:** deduction
**Premises:** `github:superconductivity_electron_liquids::vdiagmc_method`, `github:superconductivity_electron_liquids::homotopic_expansion`
**grounding:** {'kind': 'source_fact', 'rationale': 'Authored scientific assertion imported from the electron-liquids package.', 'source_refs': [], 'action_label': 'github:superconductivity_electron_liquids::action::_anon_action_042', 'pattern': 'observation'}
**Referenced by:** deduction -> `github:superconductivity_electron_liquids::mu_available_for_simple_metals`; unknown -> `github:superconductivity_electron_liquids::rpa_vs_vdiagmc`

### rpa_vs_vdiagmc

**QID:** `github:superconductivity_electron_liquids::rpa_vs_vdiagmc`
**Type:** claim
**Role:** structural
**Content:** When treating the dynamically screened Coulomb interaction within the random phase approximation (RPA), the predicted $\mu^* < 0$ (i.e. the Coulomb effect becomes net attractive in the Cooper channel) for Wigner-Seitz radius $r_s \gtrsim 2$ ($r_s$ is proportional to the ratio of electron spacing to Bohr radius, measuring the ratio of Coulomb interaction to kinetic energy). However, RPA neglects beyond-RPA effects such as vertex corrections and self-energy renormalization for $r_s \gtrsim 1$, making its predictions unreliable in this density regime and inconsistent with extensive experimental evidence. and vDiagMC calculations of the UEG four-point vertex yield the Coulomb pseudopotential at the Fermi energy scale: $\mu_{E_F}(r_s)$ is positive and monotonically increasing with $r_s$ in the metallic density range. Representative values include $\mu_{E_F} \approx 0.21$ at $r_s = 2$ (aluminum-like) and $\mu_{E_F} \approx 0.33$ at $r_s = 3.3$ (lithium-like). These results, combined with the BTS relation, yield $\mu^* \approx 0.10$--$0.15$ at the Debye scale, consistent with the empirical range but now derived from first principles with controlled error bars of a few percent. contradict.
**Belief:** 1.00
**generated:** True
**helper_kind:** contradiction_result
**review:** True

### ward_identity

**QID:** `github:superconductivity_electron_liquids::ward_identity`
**Type:** claim
**Role:** independent
**Content:** An exact Ward identity relates the three-point electron-phonon vertex $\Gamma_3^e(k, q)$ to the electron self-energy in the long-wavelength limit $q \to 0$: $\lim_{q \to 0} \Gamma_3^e(k, q) = 1 - \partial\Sigma(k)/\partial\epsilon_k$. This identity is a consequence of charge conservation and provides an exact constraint on vertex corrections at zero momentum transfer.
**Prior:** 0.98
**Belief:** 0.98
**prior:** 0.98
**prior_justification:** Exact identity from charge conservation.
**grounding:** {'kind': 'source_fact', 'rationale': 'Authored scientific assertion imported from the electron-liquids package.', 'source_refs': [], 'action_label': 'github:superconductivity_electron_liquids::action::_anon_action_045', 'pattern': 'observation'}
**Referenced by:** deduction -> `github:superconductivity_electron_liquids::gamma3_approximation`

### gamma3_vdiagmc

**QID:** `github:superconductivity_electron_liquids::gamma3_vdiagmc`
**Type:** claim
**Role:** independent
**Content:** vDiagMC computation of the three-point vertex $\Gamma_3^e(k, q)$ of the UEG at finite momentum transfer $q$ shows that vertex corrections are modest (10--20% level) for momenta within the Fermi sphere ($|k|, |k+q| \lesssim k_F$) at metallic densities $r_s \in [2, 4]$. The corrections vary smoothly with $q$ and can be accurately interpolated between the Ward-identity limit ($q \to 0$) and the large-$q$ asymptotic behavior.
**Prior:** 0.88
**Belief:** 0.88
**prior:** 0.88
**prior_justification:** Finite-order vDiagMC evidence for modest three-point vertex corrections.
**grounding:** {'kind': 'source_fact', 'rationale': 'Authored scientific assertion imported from the electron-liquids package.', 'source_refs': [], 'action_label': 'github:superconductivity_electron_liquids::action::_anon_action_046', 'pattern': 'observation'}
**Referenced by:** deduction -> `github:superconductivity_electron_liquids::gamma3_approximation`

### dfpt_eph_ansatz

**QID:** `github:superconductivity_electron_liquids::dfpt_eph_ansatz`
**Type:** claim
**Role:** background
**Content:** The DFPT expression for the electron-phonon coupling $g^{\mathrm{DFPT}}(k, q) = \sqrt{\omega_q / 2} \, \langle k+q | \delta V_{\mathrm{KS}} / \delta u_q | k \rangle$ implicitly assumes that vertex corrections to the electron-phonon coupling beyond the Kohn-Sham mean-field level are absorbed into the exchange-correlation functional. The accuracy of this ansatz depends on how well DFT captures the relevant vertex corrections.
**Prior:** 0.90
**Belief:** 0.90
**prior:** 0.9
**prior_justification:** Standard DFPT electron-phonon vertex expression.
**grounding:** {'kind': 'source_fact', 'rationale': 'Authored scientific assertion imported from the electron-liquids package.', 'source_refs': [], 'action_label': 'github:superconductivity_electron_liquids::action::_anon_action_047', 'pattern': 'observation'}

### quasiparticle_mass_near_unity

**QID:** `github:superconductivity_electron_liquids::quasiparticle_mass_near_unity`
**Type:** claim
**Role:** independent
**Content:** For simple metals at metallic densities ($r_s \in [2, 4]$), the quasiparticle effective mass ratio $m^*/m \approx 1$ (deviations less than 5--10%). This near-unity mass ratio means that the quasiparticle renormalization factor $z^e \approx 1/(1 + \lambda_e)$ primarily reflects the frequency-dependent self-energy rather than momentum-dependent mass enhancement, simplifying the mapping between microscopic and DFPT-level electron-phonon coupling.
**Prior:** 0.92
**Belief:** 0.93
**prior:** 0.92
**prior_justification:** QMC/DiagMC evidence for weak mass renormalization in simple metals.
**grounding:** {'kind': 'source_fact', 'rationale': 'Authored scientific assertion imported from the electron-liquids package.', 'source_refs': [], 'action_label': 'github:superconductivity_electron_liquids::action::_anon_action_048', 'pattern': 'observation'}
**Referenced by:** deduction -> `github:superconductivity_electron_liquids::dfpt_reliable_for_simple_metals`

### eft_eph_vertex

**QID:** `github:superconductivity_electron_liquids::eft_eph_vertex`
**Type:** claim
**Role:** derived
**Content:** The EFT expression for the electron-phonon coupling vertex $g(k, q) = z^e \cdot \Gamma_3^e(k, q) \cdot g_0(k, q)$ factorizes the full vertex into a quasiparticle renormalization factor $z^e$, the electronic three-point vertex correction $\Gamma_3^e$, and the bare electron-phonon matrix element $g_0$. The corresponding $\lambda$ in the downfolded BSE is the Fermi-surface average of $|g(k, q)|^2$ weighted by the phonon propagator.
**Belief:** 0.99
**Derived from:** deduction
**Premises:** `github:superconductivity_electron_liquids::lambda_microscopic_definition`
**grounding:** {'kind': 'source_fact', 'rationale': 'Authored scientific assertion imported from the electron-liquids package.', 'source_refs': [], 'action_label': 'github:superconductivity_electron_liquids::action::_anon_action_049', 'pattern': 'observation'}
**Referenced by:** deduction -> `github:superconductivity_electron_liquids::eft_vertex_matches_dfpt`

### gamma3_approximation

**QID:** `github:superconductivity_electron_liquids::gamma3_approximation`
**Type:** claim
**Role:** derived
**Content:** The three-point vertex $\Gamma_3^e(k, q)$ for states within the Fermi sphere can be accurately approximated by interpolation between two controlled limits: (i) the exact Ward identity at $q \to 0$ giving $\Gamma_3^e = 1 - \partial\Sigma/\partial\epsilon_k = m^*/m$, and (ii) the vDiagMC results at finite $q$ showing smooth, modest variations. For simple metals, this yields $\Gamma_3^e \approx m^*/m$ to within 10--15% across the relevant momentum range.
**Belief:** 0.93
**Derived from:** deduction
**Premises:** `github:superconductivity_electron_liquids::ward_identity`, `github:superconductivity_electron_liquids::gamma3_vdiagmc`
**grounding:** {'kind': 'source_fact', 'rationale': 'Authored scientific assertion imported from the electron-liquids package.', 'source_refs': [], 'action_label': 'github:superconductivity_electron_liquids::action::_anon_action_051', 'pattern': 'observation'}
**Referenced by:** deduction -> `github:superconductivity_electron_liquids::eft_vertex_matches_dfpt`

### eft_vertex_matches_dfpt

**QID:** `github:superconductivity_electron_liquids::eft_vertex_matches_dfpt`
**Type:** claim
**Role:** derived
**Content:** In the uniform electron gas at densities $r_s \in [1,5]$, the EFT electron-phonon vertex $g(\mathbf{k},\mathbf{q}) = g^{(0)}_{\mathbf{q}} \cdot (z^e/\epsilon_{\mathbf{q}}) \cdot \Gamma_3^e(\mathbf{k};\mathbf{q})$ is numerically well approximated by the DFPT Kohn-Sham screened potential $g^{\mathrm{KS}}(\mathbf{q}) = g^{(0)}_{\mathbf{q}} / [1 - (v_{\mathbf{q}} + f_{xc})\chi_0^e(\mathbf{q})]$ for Fermi-surface-relevant momentum transfers $|\mathbf{q}| \leq 2k_F$, with weak residual $\mathbf{k}$-dependence.
**Belief:** 0.97
**Derived from:** deduction
**Premises:** `github:superconductivity_electron_liquids::eft_eph_vertex`, `github:superconductivity_electron_liquids::gamma3_approximation`
**grounding:** {'kind': 'source_fact', 'rationale': 'Authored scientific assertion imported from the electron-liquids package.', 'source_refs': [], 'action_label': 'github:superconductivity_electron_liquids::action::_anon_action_053', 'pattern': 'observation'}
**Referenced by:** deduction -> `github:superconductivity_electron_liquids::dfpt_reliable_for_simple_metals`

### dfpt_reliable_for_simple_metals

**QID:** `github:superconductivity_electron_liquids::dfpt_reliable_for_simple_metals`
**Type:** claim
**Role:** derived
**Content:** For simple metals, the DFPT calculation of the electron-phonon coupling constant $\lambda$ is reliable: the EFT vertex matches the DFPT expression at the vertex level, and the quasiparticle density of states $N_F^*$ nearly equals the band density of states $N_F^{(0)}$, so $\lambda_{\mathrm{EFT}} \approx \lambda_{\mathrm{DFPT}}$ with corrections at the few-percent level.
**Belief:** 0.96
**Derived from:** deduction
**Premises:** `github:superconductivity_electron_liquids::eft_vertex_matches_dfpt`, `github:superconductivity_electron_liquids::quasiparticle_mass_near_unity`
**grounding:** {'kind': 'source_fact', 'rationale': 'Authored scientific assertion imported from the electron-liquids package.', 'source_refs': [], 'action_label': 'github:superconductivity_electron_liquids::action::_anon_action_054', 'pattern': 'observation'}
**Referenced by:** deduction -> `github:superconductivity_electron_liquids::ab_initio_workflow`

### li_low_temperature_lattice_assumption

**QID:** `github:superconductivity_electron_liquids::li_low_temperature_lattice_assumption`
**Type:** claim
**Role:** independent
**Content:** The low-temperature lithium $T_c$ calculation assumes that the BCC/9R structural description and associated phonon spectrum used for the DFPT input remain adequate in the sub-kelvin regime. This assumption is uncertain because lithium's crystal structure at ultra-low temperature is experimentally debated.
**Prior:** 0.60
**Belief:** 0.69
**prior:** 0.6
**prior_justification:** Lithium's sub-kelvin lattice structure is debated, so this assumption is deliberately conservative.
**grounding:** {'kind': 'source_fact', 'rationale': 'Authored scientific assertion imported from the electron-liquids package.', 'source_refs': [], 'action_label': 'github:superconductivity_electron_liquids::action::_anon_action_068', 'pattern': 'observation'}
**Referenced by:** deduction -> `github:superconductivity_electron_liquids::li_effective_coupling_error_bounded`; deduction -> `github:superconductivity_electron_liquids::tc_li_predicted`

### simple_metals_weak_lattice

**QID:** `github:superconductivity_electron_liquids::simple_metals_weak_lattice`
**Type:** claim
**Role:** background
**Content:** Simple metals (Al, Li, Na, Mg, Zn) have weak lattice effects in the Coulomb pseudopotential: the difference between the crystalline $\mu^*$ and the UEG $\mu^*$ at the same $r_s$ is small (a few percent) because the nearly-free-electron character of these metals means the Fermi surface is approximately spherical and the electronic structure is well described by the homogeneous electron gas with minor crystal-field perturbations.
**Prior:** 0.90
**Belief:** 0.90
**prior:** 0.9
**prior_justification:** Simple metals are close to nearly-free-electron systems.
**grounding:** {'kind': 'source_fact', 'rationale': 'Authored scientific assertion imported from the electron-liquids package.', 'source_refs': [], 'action_label': 'github:superconductivity_electron_liquids::action::_anon_action_073', 'pattern': 'observation'}

### ueg_pseudopotential_parameterization

**QID:** `github:superconductivity_electron_liquids::ueg_pseudopotential_parameterization`
**Type:** claim
**Role:** independent
**Content:** The UEG Coulomb pseudopotential $\mu_{E_F}(r_s)$ computed by vDiagMC can be parameterized as a smooth function of $r_s$ and mapped onto real materials by using the material's effective $r_s$ (determined from the valence electron density). Combined with the BTS relation to run $\mu_{E_F}$ down to the Debye scale, this provides $\mu^*(r_s)$ for any simple metal without additional adjustable parameters.
**Prior:** 0.85
**Belief:** 0.87
**prior:** 0.85
**prior_justification:** UEG-to-material mapping is plausible with residual band-structure uncertainty.
**grounding:** {'kind': 'source_fact', 'rationale': 'Authored scientific assertion imported from the electron-liquids package.', 'source_refs': [], 'action_label': 'github:superconductivity_electron_liquids::action::_anon_action_074', 'pattern': 'observation'}
**Referenced by:** deduction -> `github:superconductivity_electron_liquids::mu_available_for_simple_metals`

### li_effective_coupling_error_bounded

**QID:** `github:superconductivity_electron_liquids::li_effective_coupling_error_bounded`
**Type:** claim
**Role:** derived
**Content:** For lithium, the effective pairing strength computed from $\lambda = 0.34 \pm 0.034$ and $\mu^* = 0.1749 \pm 0.0375$ is small ($g = 0.1282 \pm 0.0757$), so the transition temperature is sensitive to input errors. The propagated error remains bounded enough that the sign and smallness of $g$ remain qualitatively stable.
**Prior:** 0.68
**Belief:** 0.88
**Derived from:** deduction
**Premises:** `github:superconductivity_electron_liquids::li_effective_coupling`, `github:superconductivity_electron_liquids::li_low_temperature_lattice_assumption`
**prior:** 0.68
**prior_justification:** Li effective coupling is small, so lambda and mu* error propagation is consequential.
**grounding:** {'kind': 'source_fact', 'rationale': 'Authored scientific assertion imported from the electron-liquids package.', 'source_refs': [], 'action_label': 'github:superconductivity_electron_liquids::action::_anon_action_075', 'pattern': 'observation'}
**Referenced by:** deduction -> `github:superconductivity_electron_liquids::tc_li_predicted`

### ab_initio_workflow

**QID:** `github:superconductivity_electron_liquids::ab_initio_workflow`
**Type:** claim
**Role:** derived
**Content:** The complete ab initio workflow for predicting $T_c$ of simple metals: (1) compute $\mu_{E_F}$ from the UEG four-point vertex via vDiagMC, (2) map to the material's $r_s$ and run down to $\mu^*$ via the BTS relation, (3) obtain $\lambda$ from DFPT, (4) solve the downfolded Eliashberg equations (or use the PCF extrapolation) to predict $T_c$. All inputs are from first principles; no adjustable parameters remain.
**Belief:** 0.96
**Derived from:** deduction
**Premises:** `github:superconductivity_electron_liquids::downfolded_bse`, `github:superconductivity_electron_liquids::mu_available_for_simple_metals`, `github:superconductivity_electron_liquids::dfpt_reliable_for_simple_metals`
**grounding:** {'kind': 'source_fact', 'rationale': 'Authored scientific assertion imported from the electron-liquids package.', 'source_refs': [], 'action_label': 'github:superconductivity_electron_liquids::action::_anon_action_077', 'pattern': 'observation'}
**Referenced by:** deduction -> `github:superconductivity_electron_liquids::tc_al_predicted`; deduction -> `github:superconductivity_electron_liquids::tc_zn_predicted`; deduction -> `github:superconductivity_electron_liquids::tc_li_predicted`; deduction -> `github:superconductivity_electron_liquids::al_pressure_transition`; deduction -> `github:superconductivity_electron_liquids::tc_mg_na_near_qpt`

### mu_available_for_simple_metals

**QID:** `github:superconductivity_electron_liquids::mu_available_for_simple_metals`
**Type:** claim
**Role:** derived
**Content:** For simple metals, the Coulomb pseudopotential $\mu^*$ can be obtained from first principles without adjustable parameters: the vDiagMC-computed $\mu_{E_F}(r_s)$ for the uniform electron gas is mapped to real materials via material-specific $r_s$ and band mass, then scaled to the Debye frequency via the BTS renormalization relation.
**Belief:** 0.89
**Derived from:** deduction
**Premises:** `github:superconductivity_electron_liquids::ueg_pseudopotential_parameterization`, `github:superconductivity_electron_liquids::mu_vdiagmc_values`
**grounding:** {'kind': 'source_fact', 'rationale': 'Authored scientific assertion imported from the electron-liquids package.', 'source_refs': [], 'action_label': 'github:superconductivity_electron_liquids::action::_anon_action_078', 'pattern': 'observation'}
**Referenced by:** deduction -> `github:superconductivity_electron_liquids::ab_initio_workflow`

### tc_al_predicted

**QID:** `github:superconductivity_electron_liquids::tc_al_predicted`
**Type:** claim
**Role:** derived
**Content:** The ab initio predicted superconducting transition temperature of aluminum is $T_c^{\mathrm{th}} = 0.96$ K, in good agreement with the experimental value $T_c^{\mathrm{exp}} = 1.2$ K. The first-principles $\mu^*(\mathrm{Al}) \approx 0.13$ is obtained from the vDiagMC $\mu_{E_F}$ at $r_s = 2.07$ via BTS renormalization.
**Belief:** 0.99
**Derived from:** deduction
**Premises:** `github:superconductivity_electron_liquids::ab_initio_workflow`, `github:superconductivity_electron_liquids::al_effective_coupling`
**grounding:** {'kind': 'source_fact', 'rationale': 'Authored scientific assertion imported from the electron-liquids package.', 'source_refs': [], 'action_label': 'github:superconductivity_electron_liquids::action::_anon_action_081', 'pattern': 'observation'}
**Referenced by:** infer -> `github:superconductivity_electron_liquids::tc_al_experimental`

### tc_zn_predicted

**QID:** `github:superconductivity_electron_liquids::tc_zn_predicted`
**Type:** claim
**Role:** derived
**Content:** The ab initio predicted superconducting transition temperature of zinc is $T_c^{\mathrm{th}} = 0.874$ K, consistent with the experimental value $T_c^{\mathrm{exp}} = 0.875$ K. The first-principles $\mu^*(\mathrm{Zn}) \approx 0.12$ is obtained from the vDiagMC $\mu_{E_F}$ at $r_s = 2.90$.
**Belief:** 0.99
**Derived from:** deduction
**Premises:** `github:superconductivity_electron_liquids::ab_initio_workflow`, `github:superconductivity_electron_liquids::zn_effective_coupling`
**grounding:** {'kind': 'source_fact', 'rationale': 'Authored scientific assertion imported from the electron-liquids package.', 'source_refs': [], 'action_label': 'github:superconductivity_electron_liquids::action::_anon_action_083', 'pattern': 'observation'}
**Referenced by:** infer -> `github:superconductivity_electron_liquids::tc_zn_experimental`

### tc_li_predicted

**QID:** `github:superconductivity_electron_liquids::tc_li_predicted`
**Type:** claim
**Role:** derived
**Content:** The ab initio predicted superconducting transition temperature of lithium in the 9R row is $T_c^{\mathrm{th}} = 5 \times 10^{-3}$ K, while the hcp row gives $T_c^{\mathrm{th}} = 0.03$ K and the reported experimental value is $T_c^{\mathrm{exp}} \approx 4 \times 10^{-4}$ K. The large $\mu^*(\mathrm{Li}) \approx 0.18$ from the rescaled $r_s = 5.6875$ nearly cancels the phonon-mediated attraction $\lambda = 0.34$, pushing $T_c$ to very low temperatures but leaving a residual discrepancy tied to the debated low-temperature lattice structure.
**Belief:** 0.83
**Derived from:** deduction
**Premises:** `github:superconductivity_electron_liquids::ab_initio_workflow`, `github:superconductivity_electron_liquids::li_low_temperature_lattice_assumption`, `github:superconductivity_electron_liquids::li_effective_coupling`, `github:superconductivity_electron_liquids::li_effective_coupling_error_bounded`
**grounding:** {'kind': 'source_fact', 'rationale': 'Authored scientific assertion imported from the electron-liquids package.', 'source_refs': [], 'action_label': 'github:superconductivity_electron_liquids::action::_anon_action_085', 'pattern': 'observation'}
**Referenced by:** infer -> `github:superconductivity_electron_liquids::tc_li_experimental`

### al_pressure_transition

**QID:** `github:superconductivity_electron_liquids::al_pressure_transition`
**Type:** claim
**Role:** derived
**Content:** Under hydrostatic pressure, the ab initio framework predicts that aluminum's superconducting $T_c$ initially increases as pressure stiffens phonon frequencies (increasing $\omega_{\mathrm{log}}$) while $\lambda$ and $\mu^*$ change modestly, before eventually decreasing at very high pressures when $\lambda$ is suppressed. This non-monotonic behavior is consistent with experimental pressure studies.
**Belief:** 0.98
**Derived from:** deduction
**Premises:** `github:superconductivity_electron_liquids::ab_initio_workflow`
**grounding:** {'kind': 'source_fact', 'rationale': 'Authored scientific assertion imported from the electron-liquids package.', 'source_refs': [], 'action_label': 'github:superconductivity_electron_liquids::action::_anon_action_087', 'pattern': 'observation'}

### tc_mg_na_near_qpt

**QID:** `github:superconductivity_electron_liquids::tc_mg_na_near_qpt`
**Type:** claim
**Role:** derived
**Content:** The ab initio framework predicts that sodium and magnesium have extremely low or vanishing $T_c$: for Na ($r_s = 3.93$, $\lambda \approx 0.18$), the large $\mu^*$ exceeds the weak electron-phonon coupling, giving net repulsion in the pairing channel and no superconductivity. For Mg ($r_s = 2.66$, $\lambda \approx 0.26$), $T_c$ is in the sub-nanokelvin regime. Both materials are near the quantum phase transition between superconducting and non-superconducting ground states, where $T_c$ varies exponentially with small parameter changes.
**Belief:** 0.98
**Derived from:** deduction
**Premises:** `github:superconductivity_electron_liquids::ab_initio_workflow`
**grounding:** {'kind': 'source_fact', 'rationale': 'Authored scientific assertion imported from the electron-liquids package.', 'source_refs': [], 'action_label': 'github:superconductivity_electron_liquids::action::_anon_action_089', 'pattern': 'observation'}

### github:superconductivity_electron_liquids::_anon_001

**QID:** `github:superconductivity_electron_liquids::_anon_001`
**Type:** claim
**Role:** orphaned
**Content:** The experimental superconducting transition temperature of aluminum (Al) is $T_c^{\mathrm{exp}} = 1.2$ K. statistically supports The ab initio predicted superconducting transition temperature of aluminum is $T_c^{\mathrm{th}} = 0.96$ K, in good agreement with the experimental value $T_c^{\mathrm{exp}} = 1.2$ K. The first-principles $\mu^*(\mathrm{Al}) \approx 0.13$ is obtained from the vDiagMC $\mu_{E_F}$ at $r_s = 2.07$ via BTS renormalization..
**Belief:** 0.50
**generated:** True
**helper_kind:** statistical_support
**review:** True

### github:superconductivity_electron_liquids::_anon_002

**QID:** `github:superconductivity_electron_liquids::_anon_002`
**Type:** claim
**Role:** orphaned
**Content:** The experimental superconducting transition temperature of aluminum (Al) is $T_c^{\mathrm{exp}} = 1.2$ K. statistically supports Using the McMillan formula (an empirical formula for $T_c$ based on the electron-phonon coupling constant $\lambda$ and Coulomb pseudopotential $\mu^*$), and treating the traditional empirical $\mu^*$ choice as uniformly distributed over 0.1--0.2, the predicted superconducting transition temperature of aluminum spans roughly $0.071$--$1.9$ K. The experimental value 1.2 K lies inside this broad interval, illustrating that the conventional prediction has adjustable rather than first-principles $\mu^*$ content..
**Belief:** 0.50
**generated:** True
**helper_kind:** statistical_support
**review:** True

### github:superconductivity_electron_liquids::_anon_003

**QID:** `github:superconductivity_electron_liquids::_anon_003`
**Type:** claim
**Role:** orphaned
**Content:** The experimental superconducting transition temperature of zinc (Zn) is $T_c^{\mathrm{exp}} = 0.875$ K. statistically supports The ab initio predicted superconducting transition temperature of zinc is $T_c^{\mathrm{th}} = 0.874$ K, consistent with the experimental value $T_c^{\mathrm{exp}} = 0.875$ K. The first-principles $\mu^*(\mathrm{Zn}) \approx 0.12$ is obtained from the vDiagMC $\mu_{E_F}$ at $r_s = 2.90$..
**Belief:** 0.50
**generated:** True
**helper_kind:** statistical_support
**review:** True

### github:superconductivity_electron_liquids::_anon_004

**QID:** `github:superconductivity_electron_liquids::_anon_004`
**Type:** claim
**Role:** orphaned
**Content:** The experimental superconducting transition temperature of zinc (Zn) is $T_c^{\mathrm{exp}} = 0.875$ K. statistically supports Using the McMillan formula and treating the traditional empirical $\mu^*$ choice as uniformly distributed over 0.1--0.2, the predicted superconducting transition temperature of zinc spans roughly $0.137$--$1.37$ K. The experimental value 0.875 K lies inside this broad interval, again indicating that the conventional prediction depends strongly on the empirical $\mu^*$ selection..
**Belief:** 0.50
**generated:** True
**helper_kind:** statistical_support
**review:** True

### github:superconductivity_electron_liquids::_anon_005

**QID:** `github:superconductivity_electron_liquids::_anon_005`
**Type:** claim
**Role:** orphaned
**Content:** The experimental superconducting transition temperature of lithium (Li) is $T_c^{\mathrm{exp}} \approx 4 \times 10^{-4}$ K (0.4 mK). This measurement corresponds to the 9R crystal structure; the crystal structure of lithium at ultra-low temperatures remains controversial. statistically supports The ab initio predicted superconducting transition temperature of lithium in the 9R row is $T_c^{\mathrm{th}} = 5 \times 10^{-3}$ K, while the hcp row gives $T_c^{\mathrm{th}} = 0.03$ K and the reported experimental value is $T_c^{\mathrm{exp}} \approx 4 \times 10^{-4}$ K. The large $\mu^*(\mathrm{Li}) \approx 0.18$ from the rescaled $r_s = 5.6875$ nearly cancels the phonon-mediated attraction $\lambda = 0.34$, pushing $T_c$ to very low temperatures but leaving a residual discrepancy tied to the debated low-temperature lattice structure..
**Belief:** 0.50
**generated:** True
**helper_kind:** statistical_support
**review:** True

### github:superconductivity_electron_liquids::_anon_006

**QID:** `github:superconductivity_electron_liquids::_anon_006`
**Type:** claim
**Role:** orphaned
**Content:** The experimental superconducting transition temperature of lithium (Li) is $T_c^{\mathrm{exp}} \approx 4 \times 10^{-4}$ K (0.4 mK). This measurement corresponds to the 9R crystal structure; the crystal structure of lithium at ultra-low temperatures remains controversial. statistically supports Using the McMillan formula and treating the traditional empirical $\mu^*$ choice as uniformly distributed over 0.1--0.2, the predicted superconducting transition temperature of lithium spans roughly $1.3 \times 10^{-4}$--$0.35$ K. The experimental value is approximately $4 \times 10^{-4}$ K, so the range can cover the measurement only near its high-$\mu^*$ tail; the broad interval shows that the conventional prediction is dominated by the adjustable $\mu^*$ choice..
**Belief:** 0.50
**generated:** True
**helper_kind:** statistical_support
**review:** True
