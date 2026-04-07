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
**Belief:** 0.69
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
**Belief:** 1.00
**Derived from:** noisy_and
**Premises:** `github:superconductivity_electron_liquids::bse_kernel_decomposition`
**figure:** artifacts/images/8_1.jpg
**caption:** Fig. 5 | Comparison between the precursory Cooper flow solutions of the full and downfolded BSE for a toy model, demonstrating 0.2% agreement in Tc.
**Referenced by:** abduction -> `github:superconductivity_electron_liquids::downfolded_bse_toy_model`

### downfolded_bse_toy_model

**QID:** `github:superconductivity_electron_liquids::downfolded_bse_toy_model`
**Type:** claim
**Role:** derived
**Content:** For the same toy model (aluminum-like parameters $r_s = 1.92$, $\omega_D/E_F = 0.005$), solving the downfolded frequency-only Bethe-Salpeter equation yields $T_c^{\mathrm{approx}}/T_F = 10^{-5.667}$, where $T_F$ is the Fermi temperature.
**Belief:** 0.76
**Derived from:** abduction
**Premises:** `github:superconductivity_electron_liquids::full_bse_toy_model`, `github:superconductivity_electron_liquids::__alternative_explanation_ddfe26b1`
**Derived from:** noisy_and
**Premises:** `github:superconductivity_electron_liquids::downfolded_bse`

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
**Content:** The frequency-only downfolded Bethe-Salpeter equation: the full momentum-frequency BSE kernel reduces to a one-dimensional integral equation in Matsubara frequency, with an effective kernel $K(\omega, \omega') = \lambda(\omega, \omega') - \mu_{\omega_c}(\omega, \omega')$, where the phonon-mediated attraction $\lambda$ and Coulomb pseudopotential $\mu_{\omega_c}$ are microscopically defined. The momentum integration is absorbed into the density of states, and the pair propagator's coherent part generates the BCS logarithm that drives the Cooper instability.
**Belief:** 0.76
**Derived from:** deduction
**Premises:** `github:superconductivity_electron_liquids::cross_term_suppressed`, `github:superconductivity_electron_liquids::bse_kernel_decomposition`
**Referenced by:** noisy_and -> `github:superconductivity_electron_liquids::downfolded_bse_toy_model`; deduction -> `github:superconductivity_electron_liquids::downfolded_me_equation`; deduction -> `github:superconductivity_electron_liquids::lambda_microscopic_definition`; deduction -> `github:superconductivity_electron_liquids::mu_microscopic_definition`; deduction -> `github:superconductivity_electron_liquids::ab_initio_workflow`; infer -> `github:superconductivity_electron_liquids::ab_initio_workflow`

### downfolded_me_equation

**QID:** `github:superconductivity_electron_liquids::downfolded_me_equation`
**Type:** claim
**Role:** derived
**Content:** At the superconducting critical temperature $T_c$, the downfolded Bethe-Salpeter equation reduces to the traditional linearized Migdal-Eliashberg (ME) gap equation: $\Delta_\omega = \pi T_c \sum_{|\omega'|<\omega_c} (\lambda_{\omega\omega'} - \mu^*) \frac{z_{\omega'}^{\mathrm{ph}}}{|\omega'|} \Delta_{\omega'}$. As $T \to T_c$, the anomalous vertex diverges as $\Lambda_{k\omega} \sim \Delta_{k\omega}/(T - T_c)$, causing the source term $\eta$ to become irrelevant. The diverging prefactor $(T - T_c)^{-1}$ cancels between the two sides of the equation, yielding the gap equation with $\mu^* \equiv \mu_{\omega_c}$. This establishes the microscopic foundation for the ME equation with precise definitions of $\mu^*$ and $\lambda$ in terms of electron vertex functions.
**Belief:** 0.88
**Derived from:** deduction
**Premises:** `github:superconductivity_electron_liquids::downfolded_bse`

### lambda_microscopic_definition

**QID:** `github:superconductivity_electron_liquids::lambda_microscopic_definition`
**Type:** claim
**Role:** derived
**Content:** The electron-phonon coupling $\lambda(\omega, \omega')$ in the downfolded BSE has a microscopic definition: it is the Fermi-surface average of the phonon-mediated interaction $W^{\mathrm{ph}}$ weighted by quasiparticle renormalization factors $z^e$ and $z_\omega^{\mathrm{ph}}$. This definition reduces to the standard Eliashberg $\lambda$ in the adiabatic limit but retains dynamical corrections from the electron self-energy.
**Belief:** 0.81
**Derived from:** deduction
**Premises:** `github:superconductivity_electron_liquids::downfolded_bse`
**Referenced by:** deduction -> `github:superconductivity_electron_liquids::eft_eph_vertex`

### mu_microscopic_definition

**QID:** `github:superconductivity_electron_liquids::mu_microscopic_definition`
**Type:** claim
**Role:** derived
**Content:** The Coulomb pseudopotential $\mu_{\omega_c}(\omega, \omega')$ in the downfolded BSE has a microscopic definition: it is determined by the purely electronic particle-particle irreducible four-point vertex $\tilde\Gamma^e$ projected onto the Fermi surface, with the high-energy electronic degrees of freedom integrated out above the cutoff $\omega_c$. This gives $\mu_{\omega_c}$ a precise meaning as the effective Coulomb repulsion in the low-energy pairing channel, renormalized by all electronic correlations.
**Belief:** 0.84
**Derived from:** deduction
**Premises:** `github:superconductivity_electron_liquids::downfolded_bse`
**Referenced by:** deduction -> `github:superconductivity_electron_liquids::mu_scale_independence`; deduction -> `github:superconductivity_electron_liquids::ma_pseudopotential_justified`

### mu_scale_independence

**QID:** `github:superconductivity_electron_liquids::mu_scale_independence`
**Type:** claim
**Role:** derived
**Content:** The BTS renormalization relation $\mu_{\omega_c} = \mu_{\omega_c'} / (1 + \mu_{\omega_c'} \ln(\omega_c'/\omega_c))$ emerges as a corollary of the microscopic definition of $\mu_{\omega_c}$: changing the cutoff $\omega_c$ reshuffles contributions between the explicit Coulomb kernel and the Cooper logarithm in the BCS propagator, leaving the physical $T_c$ invariant. This provides a microscopic derivation of the originally phenomenological BTS relation.
**Belief:** 0.99
**Derived from:** deduction
**Premises:** `github:superconductivity_electron_liquids::mu_microscopic_definition`
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
**Belief:** 0.92
**Derived from:** deduction
**Premises:** `github:superconductivity_electron_liquids::mu_microscopic_definition`
