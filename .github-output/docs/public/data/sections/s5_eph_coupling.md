# Module: s5_eph_coupling

### ward_identity

**QID:** `github:superconductivity_electron_liquids::ward_identity`
**Type:** claim
**Role:** independent
**Content:** An exact Ward identity relates the three-point electron-phonon vertex $\Gamma_3^e(k, q)$ to the electron self-energy in the long-wavelength limit $q \to 0$: $\lim_{q \to 0} \Gamma_3^e(k, q) = 1 - \partial\Sigma(k)/\partial\epsilon_k$. This identity is a consequence of charge conservation and provides an exact constraint on vertex corrections at zero momentum transfer.
**Prior:** 0.98
**Belief:** 0.97
**prior_records:** [{'value': 0.98, 'source_id': 'qft_exact_identity', 'justification': "The Ward identity is an exact consequence of charge conservation in QED/QFT; the 2% reserve accounts for the package's framework assumptions (linearizable e-ion coupling, single-band approximation) rather than the identity itself."}]
**prior:** 0.98
**prior_justification:** The Ward identity is an exact consequence of charge conservation in QED/QFT; the 2% reserve accounts for the package's framework assumptions (linearizable e-ion coupling, single-band approximation) rather than the identity itself.
**prior_source_id:** qft_exact_identity
**Referenced by:** deduction -> `github:superconductivity_electron_liquids::gamma3_approximation`

### gamma3_vdiagmc

**QID:** `github:superconductivity_electron_liquids::gamma3_vdiagmc`
**Type:** claim
**Role:** derived
**Content:** vDiagMC computation of the three-point vertex $\Gamma_3^e(k, q)$ of the UEG at finite momentum transfer $q$ shows that vertex corrections are modest (10--20% level) for momenta within the Fermi sphere ($|k|, |k+q| \lesssim k_F$) at metallic densities $r_s \in [2, 4]$. The corrections vary smoothly with $q$ and can be accurately interpolated between the Ward-identity limit ($q \to 0$) and the large-$q$ asymptotic behavior.
**Belief:** 0.65
**Derived from:** deduction
**Premises:** `github:superconductivity_electron_liquids::vdiagmc_method`
**figure:** artifacts/images/12_0.jpg
**caption:** Fig. 8 | Comparison between the angle-resolved e-ph vertex correction in the UEG from vDiagMC (points) and DFPT (lines) for different r_s values.
**Referenced by:** deduction -> `github:superconductivity_electron_liquids::gamma3_approximation`

### github:superconductivity_electron_liquids::_anon_017

**QID:** `github:superconductivity_electron_liquids::_anon_017`
**Type:** claim
**Role:** orphaned
**Content:** observe warrants vDiagMC computation of the three-point vertex $\Gamma_3^e(k, q)$ of the UEG at finite momentum transfer $q$ shows that vertex corrections are modest (10--20% level) for momenta within the Fermi sphere ($|k|, |k+q| \lesssim k_F$) at metallic densities $r_s \in [2, 4]$. The corrections vary smoothly with $q$ and can be accurately interpolated between the Ward-identity limit ($q \to 0$) and the large-$q$ asymptotic behavior.
**Belief:** 0.50
**generated:** True
**helper_kind:** implication_warrant
**review:** True
**relation:** {'type': 'observe', 'given': ['github:superconductivity_electron_liquids::vdiagmc_method'], 'conclusion': 'github:superconductivity_electron_liquids::gamma3_vdiagmc'}
**warrant:** The reported 10-20% vertex correction at finite $q$ is the numerical output of the vDiagMC sampling; the result is pinned as a measurement event conditional on the vDiagMC series convergence assumption captured by @vdiagmc_method.
**action_label:** github:superconductivity_electron_liquids::action::_anon_action_020
**pattern:** observation
**gaia:** {'provenance': {'referenced_claims': ['vdiagmc_method']}}

### dfpt_eph_ansatz

**QID:** `github:superconductivity_electron_liquids::dfpt_eph_ansatz`
**Type:** claim
**Role:** background
**Content:** The DFPT expression for the electron-phonon coupling $g^{\mathrm{DFPT}}(k, q) = \sqrt{\omega_q / 2} \, \langle k+q | \delta V_{\mathrm{KS}} / \delta u_q | k \rangle$ implicitly assumes that vertex corrections to the electron-phonon coupling beyond the Kohn-Sham mean-field level are absorbed into the exchange-correlation functional. The accuracy of this ansatz depends on how well DFT captures the relevant vertex corrections.
**Belief:** 0.50

### quasiparticle_mass_near_unity

**QID:** `github:superconductivity_electron_liquids::quasiparticle_mass_near_unity`
**Type:** claim
**Role:** independent
**Content:** For simple metals at metallic densities ($r_s \in [2, 4]$), the quasiparticle effective mass ratio $m^*/m \approx 1$ (deviations less than 5--10%). This near-unity mass ratio means that the quasiparticle renormalization factor $z^e \approx 1/(1 + \lambda_e)$ primarily reflects the frequency-dependent self-energy rather than momentum-dependent mass enhancement, simplifying the mapping between microscopic and DFPT-level electron-phonon coupling.
**Prior:** 0.92
**Belief:** 0.88
**prior_records:** [{'value': 0.92, 'source_id': 'qmc_numerical_data', 'justification': 'High-precision QMC and DiagMC calculations consistently show |m*/m - 1| < 5-10% for r_s in [2,5]; uncertainty reflects the spread across independent computations and material-specific band corrections.'}]
**prior:** 0.92
**prior_justification:** High-precision QMC and DiagMC calculations consistently show |m*/m - 1| < 5-10% for r_s in [2,5]; uncertainty reflects the spread across independent computations and material-specific band corrections.
**prior_source_id:** qmc_numerical_data
**Referenced by:** deduction -> `github:superconductivity_electron_liquids::dfpt_reliable_for_simple_metals`

### eft_eph_vertex

**QID:** `github:superconductivity_electron_liquids::eft_eph_vertex`
**Type:** claim
**Role:** derived
**Content:** The EFT expression for the physical electron-phonon coupling vertex factorizes the bare coupling into a screening factor and vertex/quasiparticle renormalizations (Cai et al., Eq. 32):

$$g_\kappa(\mathbf{k}, \mathbf{q}) = g_{\kappa\mathbf{q}}^{(0)}\, \frac{z^e}{\epsilon_\mathbf{q}}\, \Gamma_3^e(\mathbf{k}, \mathbf{q}),$$

where $g_{\kappa\mathbf{q}}^{(0)}$ is the bare e-ph matrix element, $\epsilon_\mathbf{q}$ is the electronic dielectric function, $z^e$ is the electronic quasiparticle weight, and $\Gamma_3^e(\mathbf{k}, \mathbf{q})$ is the electronic three-point vertex correction. The combination $z^e \Gamma_3^e(\mathbf{k}, \mathbf{q})$ can be interpreted as the quasiparticle vertex correction to the screened interaction. The corresponding $\lambda$ in the downfolded BSE is the Fermi-surface average of $|g_\kappa(\mathbf{k}, \mathbf{q})|^2 / \omega_{\kappa,\mathbf{q}}^2$ over phonon branches (see @lambda_microscopic_definition).
**Belief:** 0.43
**Derived from:** deduction
**Premises:** `github:superconductivity_electron_liquids::lambda_microscopic_definition`
**gaia:** {'provenance': {'referenced_claims': ['lambda_microscopic_definition']}}
**Referenced by:** deduction -> `github:superconductivity_electron_liquids::eft_vertex_matches_dfpt`

### github:superconductivity_electron_liquids::_anon_018

**QID:** `github:superconductivity_electron_liquids::_anon_018`
**Type:** claim
**Role:** orphaned
**Content:** derive warrants The EFT expression for the physical electron-phonon coupling vertex factorizes the bare coupling into a screening factor and vertex/quasiparticle renormalizations (Cai et al., Eq. 32):

$$g_\kappa(\mathbf{k}, \mathbf{q}) = g_{\kappa\mathbf{q}}^{(0)}\, \frac{z^e}{\epsilon_\mathbf{q}}\, \Gamma_3^e(\mathbf{k}, \mathbf{q}),$$

where $g_{\kappa\mathbf{q}}^{(0)}$ is the bare e-ph matrix element, $\epsilon_\mathbf{q}$ is the electronic dielectric function, $z^e$ is the electronic quasiparticle weight, and $\Gamma_3^e(\mathbf{k}, \mathbf{q})$ is the electronic three-point vertex correction. The combination $z^e \Gamma_3^e(\mathbf{k}, \mathbf{q})$ can be interpreted as the quasiparticle vertex correction to the screened interaction. The corresponding $\lambda$ in the downfolded BSE is the Fermi-surface average of $|g_\kappa(\mathbf{k}, \mathbf{q})|^2 / \omega_{\kappa,\mathbf{q}}^2$ over phonon branches (see @lambda_microscopic_definition).
**Belief:** 0.50
**generated:** True
**helper_kind:** implication_warrant
**review:** True
**relation:** {'type': 'derive', 'given': ['github:superconductivity_electron_liquids::lambda_microscopic_definition'], 'conclusion': 'github:superconductivity_electron_liquids::eft_eph_vertex'}
**warrant:** The microscopic definition of $\lambda$ (@lambda_microscopic_definition) involves the Fermi-surface average of $W^{\mathrm{ph}}$ weighted by quasiparticle factors. Expanding $W^{\mathrm{ph}}$ in terms of the phonon propagator and electron-phonon vertices, and factoring out the quasiparticle weight $z^e$ from the pair propagator coherent part, yields the EFT vertex $g(k,q) = z^e \cdot \Gamma_3^e(k,q) \cdot g_0(k,q)$.
**action_label:** github:superconductivity_electron_liquids::action::_anon_action_021
**pattern:** derivation
**gaia:** {'provenance': {'referenced_claims': ['lambda_microscopic_definition']}}

### gamma3_approximation

**QID:** `github:superconductivity_electron_liquids::gamma3_approximation`
**Type:** claim
**Role:** derived
**Content:** The three-point vertex $\Gamma_3^e(k, q)$ for states within the Fermi sphere can be accurately approximated by interpolation between two controlled limits: (i) the exact Ward identity at $q \to 0$ giving $\Gamma_3^e = 1 - \partial\Sigma/\partial\epsilon_k = m^*/m$, and (ii) the vDiagMC results at finite $q$ showing smooth, modest variations. For simple metals, this yields $\Gamma_3^e \approx m^*/m$ to within 10--15% across the relevant momentum range.
**Belief:** 0.99
**Derived from:** deduction
**Premises:** `github:superconductivity_electron_liquids::ward_identity`
**Derived from:** deduction
**Premises:** `github:superconductivity_electron_liquids::gamma3_vdiagmc`
**Referenced by:** deduction -> `github:superconductivity_electron_liquids::eft_vertex_matches_dfpt`

### github:superconductivity_electron_liquids::_anon_019

**QID:** `github:superconductivity_electron_liquids::_anon_019`
**Type:** claim
**Role:** orphaned
**Content:** derive warrants The three-point vertex $\Gamma_3^e(k, q)$ for states within the Fermi sphere can be accurately approximated by interpolation between two controlled limits: (i) the exact Ward identity at $q \to 0$ giving $\Gamma_3^e = 1 - \partial\Sigma/\partial\epsilon_k = m^*/m$, and (ii) the vDiagMC results at finite $q$ showing smooth, modest variations. For simple metals, this yields $\Gamma_3^e \approx m^*/m$ to within 10--15% across the relevant momentum range.
**Belief:** 0.50
**generated:** True
**helper_kind:** implication_warrant
**review:** True
**relation:** {'type': 'derive', 'given': ['github:superconductivity_electron_liquids::ward_identity'], 'conclusion': 'github:superconductivity_electron_liquids::gamma3_approximation'}
**warrant:** The Ward identity (@ward_identity) provides the exact value of $\Gamma_3^e$ at $q = 0$: $\Gamma_3^e(k, 0) = m^*/m$. This exact constraint anchors the approximation at zero momentum transfer.
**action_label:** github:superconductivity_electron_liquids::action::_anon_action_022
**pattern:** derivation
**gaia:** {'provenance': {'referenced_claims': ['ward_identity']}}

### github:superconductivity_electron_liquids::_anon_020

**QID:** `github:superconductivity_electron_liquids::_anon_020`
**Type:** claim
**Role:** orphaned
**Content:** derive warrants The three-point vertex $\Gamma_3^e(k, q)$ for states within the Fermi sphere can be accurately approximated by interpolation between two controlled limits: (i) the exact Ward identity at $q \to 0$ giving $\Gamma_3^e = 1 - \partial\Sigma/\partial\epsilon_k = m^*/m$, and (ii) the vDiagMC results at finite $q$ showing smooth, modest variations. For simple metals, this yields $\Gamma_3^e \approx m^*/m$ to within 10--15% across the relevant momentum range.
**Belief:** 0.50
**generated:** True
**helper_kind:** implication_warrant
**review:** True
**relation:** {'type': 'derive', 'given': ['github:superconductivity_electron_liquids::gamma3_vdiagmc'], 'conclusion': 'github:superconductivity_electron_liquids::gamma3_approximation'}
**warrant:** The vDiagMC computation (@gamma3_vdiagmc) shows that at finite $q$ within the Fermi sphere, vertex corrections remain modest (10--20%) and vary smoothly with momentum, supporting the approximation $\Gamma_3^e \approx m^*/m$ across the relevant momentum range.
**action_label:** github:superconductivity_electron_liquids::action::_anon_action_023
**pattern:** derivation
**gaia:** {'provenance': {'referenced_claims': ['gamma3_vdiagmc']}}

### eft_vertex_matches_dfpt

**QID:** `github:superconductivity_electron_liquids::eft_vertex_matches_dfpt`
**Type:** claim
**Role:** derived
**Content:** In the uniform electron gas at densities $r_s \in [1,5]$, the EFT electron-phonon vertex $g(\mathbf{k},\mathbf{q}) = g^{(0)}_{\mathbf{q}} \cdot (z^e/\epsilon_{\mathbf{q}}) \cdot \Gamma_3^e(\mathbf{k};\mathbf{q})$ is numerically well approximated by the DFPT Kohn-Sham screened potential $g^{\mathrm{KS}}(\mathbf{q}) = g^{(0)}_{\mathbf{q}} / [1 - (v_{\mathbf{q}} + f_{xc})\chi_0^e(\mathbf{q})]$ for Fermi-surface-relevant momentum transfers $|\mathbf{q}| \leq 2k_F$, with weak residual $\mathbf{k}$-dependence.
**Belief:** 0.62
**Derived from:** deduction
**Premises:** `github:superconductivity_electron_liquids::eft_eph_vertex`, `github:superconductivity_electron_liquids::gamma3_approximation`
**Referenced by:** deduction -> `github:superconductivity_electron_liquids::dfpt_reliable_for_simple_metals`

### github:superconductivity_electron_liquids::_anon_021

**QID:** `github:superconductivity_electron_liquids::_anon_021`
**Type:** claim
**Role:** orphaned
**Content:** derive warrants In the uniform electron gas at densities $r_s \in [1,5]$, the EFT electron-phonon vertex $g(\mathbf{k},\mathbf{q}) = g^{(0)}_{\mathbf{q}} \cdot (z^e/\epsilon_{\mathbf{q}}) \cdot \Gamma_3^e(\mathbf{k};\mathbf{q})$ is numerically well approximated by the DFPT Kohn-Sham screened potential $g^{\mathrm{KS}}(\mathbf{q}) = g^{(0)}_{\mathbf{q}} / [1 - (v_{\mathbf{q}} + f_{xc})\chi_0^e(\mathbf{q})]$ for Fermi-surface-relevant momentum transfers $|\mathbf{q}| \leq 2k_F$, with weak residual $\mathbf{k}$-dependence.
**Belief:** 0.50
**generated:** True
**helper_kind:** implication_warrant
**review:** True
**relation:** {'type': 'derive', 'given': ['github:superconductivity_electron_liquids::eft_eph_vertex', 'github:superconductivity_electron_liquids::gamma3_approximation'], 'conclusion': 'github:superconductivity_electron_liquids::eft_vertex_matches_dfpt'}
**warrant:** Substituting the approximate $\Gamma_3^e \approx m^*/m$ (@gamma3_approximation) into the EFT vertex expression (@eft_eph_vertex) $g = z^e \cdot \Gamma_3^e \cdot g_0$, and using the Migdal relation $z^e \approx m/m^*$, the product $z^e \cdot \Gamma_3^e \approx (m/m^*)(m^*/m) = 1$. This means $g(k,q) \approx g_0(k,q)$, which after screening gives exactly the DFPT Kohn-Sham expression (@dfpt_eph_ansatz) $g^{\mathrm{KS}}(q)$. The vertex-level agreement holds for $|q| \leq 2k_F$ with weak residual $k$-dependence.
**action_label:** github:superconductivity_electron_liquids::action::_anon_action_024
**pattern:** derivation
**gaia:** {'provenance': {'referenced_claims': ['dfpt_eph_ansatz', 'eft_eph_vertex', 'gamma3_approximation']}}

### dfpt_reliable_for_simple_metals

**QID:** `github:superconductivity_electron_liquids::dfpt_reliable_for_simple_metals`
**Type:** claim
**Role:** derived
**Content:** For simple metals, the DFPT calculation of the electron-phonon coupling constant $\lambda$ is reliable: the EFT vertex matches the DFPT expression at the vertex level, and the quasiparticle density of states $N_F^*$ nearly equals the band density of states $N_F^{(0)}$, so $\lambda_{\mathrm{EFT}} \approx \lambda_{\mathrm{DFPT}}$ with corrections at the few-percent level.
**Belief:** 0.76
**Derived from:** deduction
**Premises:** `github:superconductivity_electron_liquids::eft_vertex_matches_dfpt`, `github:superconductivity_electron_liquids::quasiparticle_mass_near_unity`
**Referenced by:** deduction -> `github:superconductivity_electron_liquids::ab_initio_workflow`

### github:superconductivity_electron_liquids::_anon_022

**QID:** `github:superconductivity_electron_liquids::_anon_022`
**Type:** claim
**Role:** orphaned
**Content:** derive warrants For simple metals, the DFPT calculation of the electron-phonon coupling constant $\lambda$ is reliable: the EFT vertex matches the DFPT expression at the vertex level, and the quasiparticle density of states $N_F^*$ nearly equals the band density of states $N_F^{(0)}$, so $\lambda_{\mathrm{EFT}} \approx \lambda_{\mathrm{DFPT}}$ with corrections at the few-percent level.
**Belief:** 0.50
**generated:** True
**helper_kind:** implication_warrant
**review:** True
**relation:** {'type': 'derive', 'given': ['github:superconductivity_electron_liquids::eft_vertex_matches_dfpt', 'github:superconductivity_electron_liquids::quasiparticle_mass_near_unity'], 'conclusion': 'github:superconductivity_electron_liquids::dfpt_reliable_for_simple_metals'}
**warrant:** The vertex-level agreement $g \approx g^{\mathrm{KS}}$ (@eft_vertex_matches_dfpt) ensures the electron-phonon matrix elements match. To obtain $\lambda$, these must be combined with the density of states: EFT uses the quasiparticle $N_F^*$ while DFPT (@dfpt_computes_lambda) uses the band $N_F^{(0)}$. Since $m^*/m \approx 1$ (@quasiparticle_mass_near_unity), we have $N_F^* \approx N_F^{(0)}$, and therefore $\lambda_{\mathrm{EFT}} \approx \lambda_{\mathrm{DFPT}}$.
**action_label:** github:superconductivity_electron_liquids::action::_anon_action_025
**pattern:** derivation
**gaia:** {'provenance': {'referenced_claims': ['dfpt_computes_lambda', 'eft_vertex_matches_dfpt', 'quasiparticle_mass_near_unity']}}
