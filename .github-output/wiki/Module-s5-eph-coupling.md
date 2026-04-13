# Module: s5_eph_coupling

### ward_identity

**QID:** `github:superconductivity_electron_liquids::ward_identity`
**Type:** claim
**Role:** independent
**Content:** An exact Ward identity relates the three-point electron-phonon vertex $\Gamma_3^e(k, q)$ to the electron self-energy in the long-wavelength limit $q \to 0$: $\lim_{q \to 0} \Gamma_3^e(k, q) = 1 - \partial\Sigma(k)/\partial\epsilon_k$. This identity is a consequence of charge conservation and provides an exact constraint on vertex corrections at zero momentum transfer.
**Belief:** 0.99
**prior:** 0.98
**prior_justification:** Exact QFT identity from charge conservation.
**Referenced by:** support -> `github:superconductivity_electron_liquids::gamma3_approximation`; induction -> `github:superconductivity_electron_liquids::gamma3_approximation`

### gamma3_vdiagmc

**QID:** `github:superconductivity_electron_liquids::gamma3_vdiagmc`
**Type:** claim
**Role:** independent
**Content:** vDiagMC computation of the three-point vertex $\Gamma_3^e(k, q)$ of the UEG at finite momentum transfer $q$ shows that vertex corrections are modest (10--20% level) for momenta within the Fermi sphere ($|k|, |k+q| \lesssim k_F$) at metallic densities $r_s \in [2, 4]$. The corrections vary smoothly with $q$ and can be accurately interpolated between the Ward-identity limit ($q \to 0$) and the large-$q$ asymptotic behavior.
**Belief:** 0.98
**figure:** artifacts/images/12_0.jpg
**caption:** Fig. 8 | Comparison between the angle-resolved e-ph vertex correction in the UEG from vDiagMC (points) and DFPT (lines) for different r_s values.
**prior:** 0.88
**prior_justification:** Systematic uncertainty from truncation; method validated elsewhere.
**Referenced by:** support -> `github:superconductivity_electron_liquids::gamma3_approximation`; induction -> `github:superconductivity_electron_liquids::gamma3_approximation`

### dfpt_eph_ansatz

**QID:** `github:superconductivity_electron_liquids::dfpt_eph_ansatz`
**Type:** claim
**Role:** background
**Content:** The DFPT expression for the electron-phonon coupling $g^{\mathrm{DFPT}}(k, q) = \sqrt{\omega_q / 2} \, \langle k+q | \delta V_{\mathrm{KS}} / \delta u_q | k \rangle$ implicitly assumes that vertex corrections to the electron-phonon coupling beyond the Kohn-Sham mean-field level are absorbed into the exchange-correlation functional. The accuracy of this ansatz depends on how well DFT captures the relevant vertex corrections.
**Belief:** 0.90
**prior:** 0.9
**prior_justification:** Standard DFPT expression.

### quasiparticle_mass_near_unity

**QID:** `github:superconductivity_electron_liquids::quasiparticle_mass_near_unity`
**Type:** claim
**Role:** independent
**Content:** For simple metals at metallic densities ($r_s \in [2, 4]$), the quasiparticle effective mass ratio $m^*/m \approx 1$ (deviations less than 5--10%). This near-unity mass ratio means that the quasiparticle renormalization factor $z^e \approx 1/(1 + \lambda_e)$ primarily reflects the frequency-dependent self-energy rather than momentum-dependent mass enhancement, simplifying the mapping between microscopic and DFPT-level electron-phonon coupling.
**Belief:** 0.87
**prior:** 0.92
**prior_justification:** High-precision QMC/DiagMC: m*/m < 1% deviation for r_s <= 5.
**Referenced by:** deduction -> `github:superconductivity_electron_liquids::dfpt_reliable_for_simple_metals`; infer -> `github:superconductivity_electron_liquids::dfpt_reliable_for_simple_metals`

### eft_eph_vertex

**QID:** `github:superconductivity_electron_liquids::eft_eph_vertex`
**Type:** claim
**Role:** derived
**Content:** The EFT expression for the physical electron-phonon coupling vertex factorizes the bare coupling into a screening factor and vertex/quasiparticle renormalizations (Cai et al., Eq. 32):

$$g_\kappa(\mathbf{k}, \mathbf{q}) = g_{\kappa\mathbf{q}}^{(0)}\, \frac{z^e}{\epsilon_\mathbf{q}}\, \Gamma_3^e(\mathbf{k}, \mathbf{q}),$$

where $g_{\kappa\mathbf{q}}^{(0)}$ is the bare e-ph matrix element, $\epsilon_\mathbf{q}$ is the electronic dielectric function, $z^e$ is the electronic quasiparticle weight, and $\Gamma_3^e(\mathbf{k}, \mathbf{q})$ is the electronic three-point vertex correction. The combination $z^e \Gamma_3^e(\mathbf{k}, \mathbf{q})$ can be interpreted as the quasiparticle vertex correction to the screened interaction. The corresponding $\lambda$ in the downfolded BSE is the Fermi-surface average of $|g_\kappa(\mathbf{k}, \mathbf{q})|^2 / \omega_{\kappa,\mathbf{q}}^2$ over phonon branches (see @lambda_microscopic_definition).
**Belief:** 0.52
**Derived from:** deduction
**Premises:** `github:superconductivity_electron_liquids::lambda_microscopic_definition`
**gaia:** {'provenance': {'referenced_claims': ['lambda_microscopic_definition']}}
**Referenced by:** deduction -> `github:superconductivity_electron_liquids::eft_vertex_matches_dfpt`; infer -> `github:superconductivity_electron_liquids::dfpt_reliable_for_simple_metals`

### gamma3_approximation

**QID:** `github:superconductivity_electron_liquids::gamma3_approximation`
**Type:** claim
**Role:** derived
**Content:** The three-point vertex $\Gamma_3^e(k, q)$ for states within the Fermi sphere can be accurately approximated by interpolation between two controlled limits: (i) the exact Ward identity at $q \to 0$ giving $\Gamma_3^e = 1 - \partial\Sigma/\partial\epsilon_k = m^*/m$, and (ii) the vDiagMC results at finite $q$ showing smooth, modest variations. For simple metals, this yields $\Gamma_3^e \approx m^*/m$ to within 10--15% across the relevant momentum range.
**Belief:** 0.96
**Derived from:** support
**Premises:** `github:superconductivity_electron_liquids::ward_identity`
**Derived from:** support
**Premises:** `github:superconductivity_electron_liquids::gamma3_vdiagmc`
**Derived from:** induction
**Premises:** `github:superconductivity_electron_liquids::ward_identity`, `github:superconductivity_electron_liquids::gamma3_vdiagmc`
**gaia:** {'provenance': {'referenced_claims': ['gamma3_vdiagmc', 'ward_identity']}}
**Referenced by:** deduction -> `github:superconductivity_electron_liquids::eft_vertex_matches_dfpt`; infer -> `github:superconductivity_electron_liquids::dfpt_reliable_for_simple_metals`

### github:superconductivity_electron_liquids::_anon_001

**QID:** `github:superconductivity_electron_liquids::_anon_001`
**Type:** claim
**Role:** orphaned
**Content:** Are observations independent? Do they support the same law?
**Belief:** 0.50
**helper_kind:** composition_validity
**generated:** True
**warrant:** The Ward identity provides the exact value at $q = 0$ and the vDiagMC computation confirms smooth, modest variations at finite $q$. By interpolating between these two controlled limits, we obtain a reliable approximation $\Gamma_3^e \approx m^*/m$ that captures the dominant effect (mass renormalization) while bounding the error from momentum dependence at the 10--15% level.

### eft_vertex_matches_dfpt

**QID:** `github:superconductivity_electron_liquids::eft_vertex_matches_dfpt`
**Type:** claim
**Role:** derived
**Content:** In the uniform electron gas at densities $r_s \in [1,5]$, the EFT electron-phonon vertex $g(\mathbf{k},\mathbf{q}) = g^{(0)}_{\mathbf{q}} \cdot (z^e/\epsilon_{\mathbf{q}}) \cdot \Gamma_3^e(\mathbf{k};\mathbf{q})$ is numerically well approximated by the DFPT Kohn-Sham screened potential $g^{\mathrm{KS}}(\mathbf{q}) = g^{(0)}_{\mathbf{q}} / [1 - (v_{\mathbf{q}} + f_{xc})\chi_0^e(\mathbf{q})]$ for Fermi-surface-relevant momentum transfers $|\mathbf{q}| \leq 2k_F$, with weak residual $\mathbf{k}$-dependence.
**Belief:** 0.67
**Derived from:** deduction
**Premises:** `github:superconductivity_electron_liquids::eft_eph_vertex`, `github:superconductivity_electron_liquids::gamma3_approximation`
**gaia:** {'provenance': {'referenced_claims': ['dfpt_eph_ansatz', 'eft_eph_vertex', 'gamma3_approximation']}}
**Referenced by:** deduction -> `github:superconductivity_electron_liquids::dfpt_reliable_for_simple_metals`

### dfpt_reliable_for_simple_metals

**QID:** `github:superconductivity_electron_liquids::dfpt_reliable_for_simple_metals`
**Type:** claim
**Role:** derived
**Content:** For simple metals, the DFPT calculation of the electron-phonon coupling constant $\lambda$ is reliable: the EFT vertex matches the DFPT expression at the vertex level, and the quasiparticle density of states $N_F^*$ nearly equals the band density of states $N_F^{(0)}$, so $\lambda_{\mathrm{EFT}} \approx \lambda_{\mathrm{DFPT}}$ with corrections at the few-percent level.
**Belief:** 0.78
**Derived from:** deduction
**Premises:** `github:superconductivity_electron_liquids::eft_vertex_matches_dfpt`, `github:superconductivity_electron_liquids::quasiparticle_mass_near_unity`
**Derived from:** infer
**Premises:** `github:superconductivity_electron_liquids::eft_eph_vertex`, `github:superconductivity_electron_liquids::gamma3_approximation`, `github:superconductivity_electron_liquids::quasiparticle_mass_near_unity`
**gaia:** {'provenance': {'referenced_claims': ['dfpt_computes_lambda', 'eft_vertex_matches_dfpt', 'quasiparticle_mass_near_unity']}}
**Referenced by:** deduction -> `github:superconductivity_electron_liquids::ab_initio_workflow`; infer -> `github:superconductivity_electron_liquids::ab_initio_workflow`
