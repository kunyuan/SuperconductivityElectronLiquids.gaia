# Module: s3_downfolding

### pair_propagator_decomposition

**QID:** `github:superconductivity_electron_liquids::pair_propagator_decomposition`
**Type:** setting
**Role:** setting
**Content:** The pair propagator (product of two single-particle Green's functions $G_{k\omega}G_{-k,-\omega}$) can be exactly decomposed into a low-energy coherent part $\Pi_{\mathrm{BCS}}$ and a high-energy incoherent remainder $\phi_{k\omega}$: $G_{k\omega}G_{-k,-\omega} = \Pi_{\mathrm{BCS}} + \phi_{k\omega}$. The coherent part is expressed in terms of the quasiparticle weight $z^e$, frequency-dependent quasiparticle weight $z_\omega^{\mathrm{ph}}$, and renormalized dispersion $\epsilon_k$. This is an exact mathematical identity introducing energy-scale separation in the two-electron channel.

### cross_term_suppressed

**QID:** `github:superconductivity_electron_liquids::cross_term_suppressed`
**Type:** claim
**Role:** independent
**Content:** Cross terms mixing Coulomb and phonon channels are suppressed by the plasma frequency $\omega_p$, at order $O(\omega_c^2/\omega_p^2)$, where $\omega_c$ is an intermediate energy cutoff satisfying $\omega_D \ll \omega_c \ll E_F$. For most three-dimensional metals $\omega_c/\omega_p \lesssim 0.1$, so cross terms contribute no more than 1%.
**Prior:** 0.90
**Belief:** 0.50
**Referenced by:** deduction -> `github:superconductivity_electron_liquids::downfolded_bse`

### rpa_dynamic_screening

**QID:** `github:superconductivity_electron_liquids::rpa_dynamic_screening`
**Type:** setting
**Role:** setting
**Content:** Random Phase Approximation (RPA) dynamically screened Coulomb interaction: $W_{\mathrm{RPA}}(\mathbf{q},\nu) = v_q / (1 - v_q \Pi^0_{\mathbf{q}\nu})$, where $v_q = 4\pi e^2/q^2$ is the bare Coulomb potential and $\Pi^0$ is the non-interacting polarization function. This is a standard approximation that becomes exact in the weak-coupling limit ($r_s \lesssim 1$).

### full_bse_toy_model

**QID:** `github:superconductivity_electron_liquids::full_bse_toy_model`
**Type:** claim
**Role:** derived
**Content:** For a toy model with aluminum-like parameters (Wigner-Seitz radius $r_s = 1.92$, adiabatic ratio $\omega_D/E_F = 0.005$), numerically solving the full frequency-momentum dependent Bethe-Salpeter equation (BSE) — using RPA dynamically screened Coulomb interaction as the electron irreducible vertex plus a model phonon interaction, without any downfolding approximation — yields a superconducting transition temperature $T_c^{\mathrm{full}}/T_F = 10^{-5.668}$, where $T_F$ is the Fermi temperature.
**Belief:** 0.76
**Derived from:** noisy_and
**Premises:** `github:superconductivity_electron_liquids::bse_kernel_decomposition`
**figure:** artifacts/images/8_1.jpg
**caption:** Fig. 5 | Comparison between the precursory Cooper flow solutions of the full and downfolded BSE for a toy model, demonstrating 0.2% agreement in Tc.
**gaia:** {'provenance': {'referenced_claims': ['bse_kernel_decomposition', 'rpa_dynamic_screening']}}
**Referenced by:** abduction -> `github:superconductivity_electron_liquids::downfolded_bse_toy_model`

### downfolded_bse_toy_model

**QID:** `github:superconductivity_electron_liquids::downfolded_bse_toy_model`
**Type:** claim
**Role:** derived
**Content:** For the same toy model (aluminum-like parameters $r_s = 1.92$, $\omega_D/E_F = 0.005$), solving the downfolded frequency-only Bethe-Salpeter equation yields $T_c^{\mathrm{approx}}/T_F = 10^{-5.667}$, where $T_F$ is the Fermi temperature.
**Belief:** 0.32
**Derived from:** abduction
**Premises:** `github:superconductivity_electron_liquids::full_bse_toy_model`, `github:superconductivity_electron_liquids::__alternative_explanation_ddfe26b1`
**Derived from:** noisy_and
**Premises:** `github:superconductivity_electron_liquids::downfolded_bse`
**gaia:** {'provenance': {'referenced_claims': ['downfolded_bse', 'downfolded_bse_toy_model', 'full_bse_toy_model', 'rpa_dynamic_screening']}}

### downfolding_validity_limits

**QID:** `github:superconductivity_electron_liquids::downfolding_validity_limits`
**Type:** claim
**Role:** orphaned
**Content:** The downfolded EFT-ME framework's applicability conditions and failure modes: (i) the adiabatic parameter $\omega_D/E_F \ll 1$ must hold, (ii) the intermediate cutoff $\omega_c$ must satisfy $\omega_D \ll \omega_c \ll E_F$ with $\omega_c/\omega_p \ll 1$, and (iii) the framework breaks down for strongly non-adiabatic systems (e.g. high-$T_c$ hydrides where $\omega_D/E_F \sim 0.1$) and for strongly correlated materials where the quasiparticle picture fails.
**Prior:** 0.92
**Belief:** 0.92

### downfolded_bse

**QID:** `github:superconductivity_electron_liquids::downfolded_bse`
**Type:** claim
**Role:** derived
**Content:** The frequency-only downfolded Bethe-Salpeter equation: the full momentum-frequency BSE kernel reduces to a one-dimensional integral equation in Matsubara frequency for the Fermi-surface-averaged anomalous vertex $\Lambda_\omega$ [@Cai2025, Eq. 20]:

$$\Lambda_\omega = \eta_\omega + \pi T \sum_{|\omega'|<\omega_c} \bigl(\lambda_{\omega\omega'} - \mu_{\omega_c}\bigr) \frac{z_{\omega'}^{\mathrm{ph}}}{|\omega'|}\, \Lambda_{\omega'}.$$

Here $\eta_\omega$ is the symmetry-breaking pair source (set to unity for numerical convenience without affecting $T_c$), $z_\omega^{\mathrm{ph}}$ is the e-ph quasiparticle weight [@Cai2025, Eq. 21], and the kernel decomposes into the phonon-mediated attraction $\lambda_{\omega\omega'}$ and the Coulomb pseudopotential $\mu_{\omega_c}$, both with microscopic definitions in terms of electron vertex functions. Corrections are bounded by three small parameters: $\omega_D/E_F$, $\omega_c^2/\omega_p^2$, and $T/\omega_c$. The momentum integration is absorbed into the density of states, and the pair propagator's coherent part generates the BCS logarithm that drives the Cooper instability.
**Belief:** 0.33
**Derived from:** deduction
**Premises:** `github:superconductivity_electron_liquids::cross_term_suppressed`, `github:superconductivity_electron_liquids::bse_kernel_decomposition`
**gaia:** {'provenance': {'cited_refs': ['Cai2025'], 'referenced_claims': ['adiabatic_approx', 'bse_kernel_decomposition', 'cross_term_suppressed', 'pair_propagator_decomposition']}}
**Referenced by:** noisy_and -> `github:superconductivity_electron_liquids::downfolded_bse_toy_model`; deduction -> `github:superconductivity_electron_liquids::downfolded_me_equation`; deduction -> `github:superconductivity_electron_liquids::lambda_microscopic_definition`; deduction -> `github:superconductivity_electron_liquids::mu_microscopic_definition`; deduction -> `github:superconductivity_electron_liquids::ab_initio_workflow`; infer -> `github:superconductivity_electron_liquids::ab_initio_workflow`

### downfolded_me_equation

**QID:** `github:superconductivity_electron_liquids::downfolded_me_equation`
**Type:** claim
**Role:** derived
**Content:** At the superconducting critical temperature $T_c$, the downfolded Bethe-Salpeter equation reduces to the traditional linearized Migdal-Eliashberg (ME) gap equation: $\Delta_\omega = \pi T_c \sum_{|\omega'|<\omega_c} (\lambda_{\omega\omega'} - \mu^*) \frac{z_{\omega'}^{\mathrm{ph}}}{|\omega'|} \Delta_{\omega'}$. As $T \to T_c$, the anomalous vertex diverges as $\Lambda_{k\omega} \sim \Delta_{k\omega}/(T - T_c)$, causing the source term $\eta$ to become irrelevant. The diverging prefactor $(T - T_c)^{-1}$ cancels between the two sides of the equation, yielding the gap equation with $\mu^* \equiv \mu_{\omega_c}$. This establishes the microscopic foundation for the ME equation with precise definitions of $\mu^*$ and $\lambda$ in terms of electron vertex functions.
**Belief:** 0.66
**Derived from:** deduction
**Premises:** `github:superconductivity_electron_liquids::downfolded_bse`
**gaia:** {'provenance': {'referenced_claims': ['downfolded_bse', 'precursory_cooper_flow']}}

### lambda_microscopic_definition

**QID:** `github:superconductivity_electron_liquids::lambda_microscopic_definition`
**Type:** claim
**Role:** derived
**Content:** The electron-phonon coupling $\lambda(\omega, \omega')$ in the downfolded BSE has a microscopic definition: it is the Fermi-surface average of the phonon-mediated interaction $W^{\mathrm{ph}}$ weighted by quasiparticle renormalization factors $z^e$ and $z_\omega^{\mathrm{ph}}$.

In the standard ME normalization, the static dimensionless coupling follows the Fermi-surface average of $g^2/\omega^2$ over phonon branches $\kappa$ [@Cai2025, Eq. 31]:

$$\lambda = N_F \sum_\kappa \left\langle \frac{g_\kappa^2(\mathbf{k}, \mathbf{q})}{\omega_{\kappa, \mathbf{q}}^2}\right\rangle_{\mathrm{FS}},$$

with $|\mathbf{k}| = |\mathbf{k} + \mathbf{q}| = k_F$, $N_F$ the density of states at the Fermi level, and $g_\kappa(\mathbf{k}, \mathbf{q})$ the physical screened-and-renormalized e-ph vertex (see @eft_eph_vertex). This definition reduces to the standard Eliashberg $\lambda$ in the adiabatic limit but retains dynamical corrections from the electron self-energy.
**Belief:** 0.50
**Derived from:** deduction
**Premises:** `github:superconductivity_electron_liquids::downfolded_bse`
**gaia:** {'provenance': {'cited_refs': ['Cai2025'], 'referenced_claims': ['downfolded_bse', 'eft_eph_vertex', 'electron_phonon_action']}}
**Referenced by:** deduction -> `github:superconductivity_electron_liquids::eft_eph_vertex`

### mu_microscopic_definition

**QID:** `github:superconductivity_electron_liquids::mu_microscopic_definition`
**Type:** claim
**Role:** derived
**Content:** The Coulomb pseudopotential $\mu_{\omega_c}(\omega, \omega')$ in the downfolded BSE has a microscopic definition: it is determined by the purely electronic particle-particle irreducible four-point vertex $\tilde\Gamma^e$ projected onto the Fermi surface, with the high-energy electronic degrees of freedom integrated out above the cutoff $\omega_c$.

Operationally, in a purely electronic theory ($\lambda = 0$, $z^{\mathrm{ph}} = 1$), solving the downfolded equation gives the temperature-dependent effective Cooper-channel repulsion [@Cai2025, Eq. 23]:

$$\gamma_T = \frac{\mu_{\omega_c}}{1 + \mu_{\omega_c} \ln(\omega_c/T)} \quad (T \ll \omega_c),$$

where $\gamma_T$ is computed directly from the four-point vertex [@Cai2025, Eq. 24]:

$$\gamma_T \equiv z_e^2\, N_F^{\ast}\, \bigl\langle \Gamma_4^e(\mathbf{k}_F, \omega_0;\, \mathbf{k}_F', \omega_0)\bigr\rangle_{\mathbf{k}_F, \mathbf{k}_F'},\qquad \omega_0 = \pi T.$$

Here $z_e$ is the electronic quasiparticle weight, $N_F^\ast$ is the quasiparticle density of states, and $\Gamma_4^e$ is the full electronic four-point vertex on the Fermi surface evaluated at the lowest Matsubara frequency $\omega_0 = \pi T$. Inverting Eq. 23 yields $\mu_{\omega_c}$ from the measured $\gamma_T$, providing a precise meaning to the Coulomb pseudopotential as the effective repulsion in the low-energy pairing channel, renormalized by all electronic correlations.
**Belief:** 0.54
**Derived from:** deduction
**Premises:** `github:superconductivity_electron_liquids::downfolded_bse`
**gaia:** {'provenance': {'cited_refs': ['Cai2025'], 'referenced_claims': ['downfolded_bse']}}
**Referenced by:** deduction -> `github:superconductivity_electron_liquids::mu_scale_independence`; deduction -> `github:superconductivity_electron_liquids::ma_pseudopotential_justified`

### mu_scale_independence

**QID:** `github:superconductivity_electron_liquids::mu_scale_independence`
**Type:** claim
**Role:** derived
**Content:** The BTS renormalization relation $\mu_{\omega_c} = \mu_{\omega_c'} / (1 + \mu_{\omega_c'} \ln(\omega_c'/\omega_c))$ emerges as a corollary of the microscopic definition of $\mu_{\omega_c}$: changing the cutoff $\omega_c$ reshuffles contributions between the explicit Coulomb kernel and the Cooper logarithm in the BCS propagator, leaving the physical $T_c$ invariant. This provides a microscopic derivation of the originally phenomenological BTS relation.
**Belief:** 0.98
**Derived from:** deduction
**Premises:** `github:superconductivity_electron_liquids::mu_microscopic_definition`
**gaia:** {'provenance': {'referenced_claims': ['mu_microscopic_definition']}}
**Referenced by:** unknown -> `github:superconductivity_electron_liquids::bts_microscopic_equivalence`

### bts_microscopic_equivalence

**QID:** `github:superconductivity_electron_liquids::bts_microscopic_equivalence`
**Type:** claim
**Role:** structural
**Content:** same_truth(A, B)
**Belief:** 1.00
**helper_kind:** equivalence_result

### ma_pseudopotential_justified

**QID:** `github:superconductivity_electron_liquids::ma_pseudopotential_justified`
**Type:** claim
**Role:** derived
**Content:** The Morel-Anderson constant-pseudopotential ansatz — treating $\mu_{\omega_c}$ as approximately frequency-independent — is microscopically justified: the four-point vertex $\tilde\Gamma^e$ varies on electronic energy scales ($E_F$), which are much larger than the phonon scale ($\omega_D$). Within the low-energy window $|\omega|, |\omega'| < \omega_c \ll E_F$, the Coulomb kernel is effectively constant, validating the traditional constant-$\mu^*$ treatment used in Eliashberg theory.
**Belief:** 0.77
**Derived from:** deduction
**Premises:** `github:superconductivity_electron_liquids::mu_microscopic_definition`
**gaia:** {'provenance': {'referenced_claims': ['mu_microscopic_definition', 'mu_star_phenomenological']}}
