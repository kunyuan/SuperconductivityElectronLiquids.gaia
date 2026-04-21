# superconductivity-electron-liquids-gaia

Gaia knowledge package: Superconductivity in Electron Liquids (arXiv:2512.19382)

## Overview

```mermaid
graph LR
    downfolded_bse["Downfolded BSE (0.96)"]:::derived
    mu_vdiagmc_values["mu from vDiagMC: Numerical Values (0.75)"]:::derived
    dfpt_reliable_for_simple_metals["DFPT Reliable for Simple Metals (0.87)"]:::derived
    ab_initio_workflow["Ab Initio Tc Prediction Workflow (0.80)"]:::derived
    tc_al_predicted["Tc(Al) Ab Initio Prediction (0.84)"]:::derived
    tc_zn_predicted["Tc(Zn) Ab Initio Prediction (0.84)"]:::derived
    tc_li_predicted["Tc(Li) Ab Initio Prediction (0.82)"]:::derived
    al_pressure_transition["Al Pressure-Tc Transition (0.82)"]:::derived
    tc_mg_na_near_qpt["Na and Mg Near Quantum Phase Transition (0.82)"]:::derived
    ab_initio_workflow --> al_pressure_transition
    ab_initio_workflow --> tc_al_predicted
    ab_initio_workflow --> tc_li_predicted
    ab_initio_workflow --> tc_mg_na_near_qpt
    ab_initio_workflow --> tc_zn_predicted
    dfpt_reliable_for_simple_metals --> ab_initio_workflow
    downfolded_bse --> ab_initio_workflow
    downfolded_bse --> dfpt_reliable_for_simple_metals
    mu_vdiagmc_values --> ab_initio_workflow

    classDef setting fill:#f0f0f0,stroke:#999,color:#333
    classDef premise fill:#ddeeff,stroke:#4488bb,color:#333
    classDef derived fill:#ddffdd,stroke:#44bb44,color:#333
    classDef question fill:#fff3dd,stroke:#cc9944,color:#333
    classDef background fill:#f5f5f5,stroke:#bbb,stroke-dasharray: 5 5,color:#333
    classDef orphan fill:#fff,stroke:#ccc,stroke-dasharray: 5 5,color:#333
    classDef external fill:#fff,stroke:#aaa,stroke-dasharray: 3 3,color:#333
    classDef weak fill:#fff9c4,stroke:#f9a825,stroke-dasharray: 5 5,color:#333
    classDef contra fill:#ffebee,stroke:#c62828,color:#333
```

## Introduction: Motivation and Background

<a id="bcs_theory"></a>

#### BCS Theory

📋 `bcs_theory`

> Bardeen-Cooper-Schrieffer (BCS) theory: phonon-mediated electron-electron attraction leads to Cooper pairing instability at the Fermi surface, providing the fundamental framework for understanding conventional superconductors.


<a id="adiabatic_approx"></a>

#### Adiabatic Approximation

📌 `adiabatic_approx`   |   Prior: 0.95   |   Belief: **0.96**

> In conventional metals, the typical phonon frequency (Debye frequency $\omega_D$) is much smaller than the electron Fermi energy $E_F$, i.e. $\omega_D / E_F \ll 1$ (adiabatic approximation). This energy-scale separation has three key consequences: (i) electrons adiabatically adjust to ionic motion, (ii) the electron-ion coupling can be linearized, and (iii) the space-time scale separation between electron and phonon physics permits a controlled effective field theory (EFT) treatment.


<a id="me_framework"></a>

#### Migdal-Eliashberg Framework

📌 `me_framework`   |   Belief: **0.97**

> Migdal-Eliashberg (ME) theory provides a rigorous treatment of the dynamic electron-phonon interaction. Under the adiabatic condition $\omega_D / E_F \ll 1$, Migdal's theorem guarantees that phonon vertex corrections are suppressed at $O(\omega_D/E_F)$, allowing the electron-phonon self-energy to be truncated at the self-consistent Fock diagram level. This justifies the ME formalism as a controlled low-energy theory for electron-phonon superconductors.

🔗 **deduction**([Adiabatic Approximation](#adiabatic_approx))

<details><summary>Reasoning</summary>

The adiabatic condition $\omega_D/E_F \ll 1$ (@adiabatic_approx) ensures that the ratio of ionic to electronic energy scales is small. Migdal's theorem then proves that phonon vertex corrections beyond the self-consistent Fock level are suppressed by $O(\omega_D/E_F)$, establishing the Migdal-Eliashberg formalism as a controlled approximation built on the BCS pairing mechanism (@bcs_theory).

</details>


<a id="bts_renormalization"></a>

#### BTS Renormalization Relation

📌 `bts_renormalization`   |   Prior: 0.95   |   Belief: **1.00**

> The Bogoliubov-Tolmachev-Shirkov (BTS) renormalization relation connects the Coulomb pseudopotential $\mu_{\omega_c}$ (a dimensionless parameter describing the effective electron-electron repulsion strength in the pairing channel) defined at different energy cutoff scales $\omega_c$: $\mu_{\omega_c} = \mu_{\omega_c'} / (1 + \mu_{\omega_c'} \ln(\omega_c'/\omega_c))$. This relation ensures that physical observables do not depend on the choice of the arbitrary cutoff scale.


<a id="me_downfolding_is_phenomenological"></a>

#### ME Downfolding is Phenomenological

📌 `me_downfolding_is_phenomenological`   |   Prior: 0.95   |   Belief: **0.95**

> The downfolding procedure (integrating out high-energy degrees of freedom to obtain a low-energy effective theory) in traditional Migdal-Eliashberg (ME) theory is phenomenological: the Coulomb effect is replaced by a static pseudopotential $\mu^*$, ignoring corrections from Coulomb fluctuations to quasiparticle renormalization and electron-phonon coupling, as well as non-local effects of screening.


<a id="phenomenological_me_theory"></a>

#### Phenomenological ME Theory Limitations

📌 `phenomenological_me_theory`   |   Prior: 0.95   |   Belief: **0.95**

> Traditional electron-phonon superconductivity theory uses the McMillan (or Allen-Dynes) formula, with the electron-phonon coupling constant $\lambda$ and Coulomb pseudopotential $\mu^*$ as inputs to predict the superconducting transition temperature $T_c$. Since $\mu^*$ cannot be reliably computed from first principles, it is typically assigned an empirical value $\mu^* \in [0.1, 0.2]$. For materials with $T_c$ in the sub-kelvin range, the exponential sensitivity $T_c \propto \exp(-1/g)$ to $\mu^*$ causes this uncertainty to span several orders of magnitude in the predicted $T_c$, destroying predictive power.


<a id="mu_star_phenomenological"></a>

#### mu* as Phenomenological Parameter

📌 `mu_star_phenomenological`   |   Prior: 0.95   |   Belief: **0.99**

> Due to the lack of a reliable microscopic calculation, the Coulomb pseudopotential $\mu^*$ (a dimensionless parameter describing the effective Coulomb repulsion strength in the low-energy pairing channel) is typically treated as an adjustable parameter with empirical values in the range 0.1--0.2.


<a id="rpa_predicts_attractive_mu"></a>

#### RPA Predicts Attractive mu*

📌 `rpa_predicts_attractive_mu`   |   Prior: 0.50   |   Belief: **0.13**

> When treating the dynamically screened Coulomb interaction within the random phase approximation (RPA), the predicted $\mu^* < 0$ (i.e. the Coulomb effect becomes net attractive in the Cooper channel) for Wigner-Seitz radius $r_s \gtrsim 2$ ($r_s$ is proportional to the ratio of electron spacing to Bohr radius, measuring the ratio of Coulomb interaction to kinetic energy). However, RPA neglects beyond-RPA effects such as vertex corrections and self-energy renormalization for $r_s \gtrsim 1$, making its predictions unreliable in this density regime and inconsistent with extensive experimental evidence.


<a id="dfpt_computes_lambda"></a>

#### DFPT Computes lambda

📌 `dfpt_computes_lambda`   |   Prior: 0.92   |   Belief: **0.99**

> Density functional perturbation theory (DFPT) computes the electron-phonon coupling constant $\lambda$ (a dimensionless parameter quantifying the phonon-mediated attraction strength at the Fermi surface) via the linear response of the Kohn-Sham ground-state energy to lattice distortions. DFPT has been validated for weakly correlated superconductors but its accuracy for strongly correlated systems is unknown.


<a id="tc_al_experimental"></a>

#### Tc(Al) Experimental

📌 `tc_al_experimental`   |   Prior: 0.99   |   Belief: **0.99**

> The experimental superconducting transition temperature of aluminum (Al) is 1.2 K. This value is the experimental target used in the Al comparison.


<a id="tc_li_experimental"></a>

#### Tc(Li) Experimental

📌 `tc_li_experimental`   |   Prior: 0.85   |   Belief: **0.85**

> The experimental superconducting transition temperature of lithium (Li) is 0.0004 K. This value is approximately 0.4 mK and corresponds to the 9R crystal structure; the crystal structure of lithium at ultra-low temperatures remains controversial.


<a id="tc_zn_experimental"></a>

#### Tc(Zn) Experimental

📌 `tc_zn_experimental`   |   Prior: 0.99   |   Belief: **0.99**

> The experimental superconducting transition temperature of zinc (Zn) is 0.875 K. This value is the experimental target used in the Zn comparison.


<a id="tc_al_phenomenological"></a>

#### Tc(Al) Phenomenological Prediction

📌 `tc_al_phenomenological`   |   Prior: 0.95   |   Belief: **1.00**

> The phenomenological McMillan predicted superconducting transition temperature of aluminum (Al) is 1.9 K. This uses the standard empirical value mu* = 0.1; the experimental value is 1.2 K, giving a deviation of approximately 58%.

🔗 **support**([DFPT Computes lambda](#dfpt_computes_lambda), [mu* as Phenomenological Parameter](#mu_star_phenomenological))

<details><summary>Reasoning</summary>

The phenomenological McMillan prediction for aluminum uses DFPT-computed $\lambda$ (@dfpt_computes_lambda) and the standard empirical value $\mu^* = 0.1$ (@mu_star_phenomenological) to predict $T_c \approx 1.9$ K.

</details>


<a id="tc_li_phenomenological"></a>

#### Tc(Li) Phenomenological Prediction

📌 `tc_li_phenomenological`   |   Prior: 0.95   |   Belief: **1.00**

> The phenomenological McMillan predicted superconducting transition temperature of lithium (Li) is 0.35 K. This uses mu* = 0.1; the experimental value is approximately 4e-4 K, so the theory overestimates by about three orders of magnitude.

🔗 **support**([DFPT Computes lambda](#dfpt_computes_lambda), [mu* as Phenomenological Parameter](#mu_star_phenomenological))

<details><summary>Reasoning</summary>

The phenomenological McMillan prediction for lithium uses DFPT-computed $\lambda$ (@dfpt_computes_lambda) and the standard empirical value $\mu^* = 0.1$ (@mu_star_phenomenological) to predict $T_c \approx 0.35$ K.

</details>


<a id="tc_zn_phenomenological"></a>

#### Tc(Zn) Phenomenological Prediction

📌 `tc_zn_phenomenological`   |   Prior: 0.95   |   Belief: **1.00**

> The phenomenological McMillan predicted superconducting transition temperature of zinc (Zn) is 1.37 K. This uses the standard empirical value mu* = 0.1; the experimental value is 0.875 K, giving a deviation of approximately 57%.

🔗 **support**([DFPT Computes lambda](#dfpt_computes_lambda), [mu* as Phenomenological Parameter](#mu_star_phenomenological))

<details><summary>Reasoning</summary>

The phenomenological McMillan prediction for zinc uses DFPT-computed $\lambda$ (@dfpt_computes_lambda) and the standard empirical value $\mu^* = 0.1$ (@mu_star_phenomenological) to predict $T_c \approx 1.37$ K.

</details>


<a id="main_question"></a>

#### Main Question: First-Principles mu* and Tc

❓ `main_question`

> Can the Coulomb pseudopotential $\mu^*$ (the parameter quantifying effective electron-electron repulsion in the Cooper pairing channel) be computed from first principles with controlled accuracy, and can this yield quantitative predictions of the superconducting transition temperature $T_c$ for simple metals (e.g. Al, Li, Na, Mg)?


## The Model and Basic Relations

```mermaid
graph TD
    me_framework["Migdal-Eliashberg Framework (0.97)"]:::external
    electron_phonon_action["Electron-Phonon Action Decomposition (0.95)"]:::background
    bse_kernel_decomposition["BSE Kernel Decomposition (0.98)"]:::derived
    precursory_cooper_flow["Precursory Cooper Flow (0.90)"]:::background
    strat_1(["deduction"])
    me_framework --> strat_1
    strat_1 --> bse_kernel_decomposition

    classDef setting fill:#f0f0f0,stroke:#999,color:#333
    classDef premise fill:#ddeeff,stroke:#4488bb,color:#333
    classDef derived fill:#ddffdd,stroke:#44bb44,color:#333
    classDef question fill:#fff3dd,stroke:#cc9944,color:#333
    classDef background fill:#f5f5f5,stroke:#bbb,stroke-dasharray: 5 5,color:#333
    classDef orphan fill:#fff,stroke:#ccc,stroke-dasharray: 5 5,color:#333
    classDef external fill:#fff,stroke:#aaa,stroke-dasharray: 3 3,color:#333
    classDef weak fill:#fff9c4,stroke:#f9a825,stroke-dasharray: 5 5,color:#333
    classDef contra fill:#ffebee,stroke:#c62828,color:#333
```

<a id="electron_phonon_action"></a>

#### Electron-Phonon Action Decomposition

📌 `electron_phonon_action`   |   Prior: 0.95   |   Belief: **0.95**

> The effective action of the electron-phonon coupled system can be decomposed as $S = S_e + S_{\mathrm{ph}} + S_{e\text{-ph}} + S_{\mathrm{CT}} + O(\sqrt{m/M})$, where $m$ is the electron mass and $M$ is the ion mass. $S_e$ is the complete many-electron action without any approximation, $S_{\mathrm{ph}}$ describes phonons with physical dispersion, $S_{e\text{-ph}}$ is the coupling between electron density and ionic displacement, and $S_{\mathrm{CT}}$ is a counterterm that subtracts the static electron polarization contribution already included in the physical phonon dispersion to prevent double counting.


<a id="bse_kernel_decomposition"></a>

#### BSE Kernel Decomposition

📌 `bse_kernel_decomposition`   |   Belief: **0.98**

> The kernel of the Bethe-Salpeter equation (BSE) can be decomposed into the purely electronic particle-particle irreducible four-point vertex $\tilde\Gamma^e$ (encoding all non-perturbative Coulomb effects) and the phonon-mediated effective electron-electron interaction $W^{\mathrm{ph}}$: $\tilde\Gamma = \tilde\Gamma^e + W^{\mathrm{ph}} + O(\omega_D/E_F)$. Migdal's theorem ensures that higher-order phonon vertex corrections are suppressed by the adiabatic small parameter.

🔗 **deduction**([Migdal-Eliashberg Framework](#me_framework))

<details><summary>Reasoning</summary>

Migdal's theorem (@me_framework) guarantees that phonon vertex corrections to the BSE kernel are suppressed at $O(\omega_D/E_F)$. This allows the full particle-particle irreducible kernel to be separated into a purely electronic four-point vertex $\tilde\Gamma^e$ (which encodes all non-perturbative Coulomb correlations and is independent of phonon details) and the phonon-mediated interaction $W^{\mathrm{ph}}$ (which includes the dressed phonon propagator, bare coupling, electronic screening, and vertex corrections). Cross terms between these two contributions are higher order in $\omega_D/E_F$ and can be neglected.

</details>


<a id="precursory_cooper_flow"></a>

#### Precursory Cooper Flow

📌 `precursory_cooper_flow`   |   Prior: 0.90   |   Belief: **0.90**

> The low-frequency limit of the anomalous vertex function on the Fermi surface $\Lambda_0$ obeys a universal scaling relation (precursory Cooper flow, PCF): $\Lambda_0 = 1/(1 + g\ln(\omega_\Lambda/T)) + O(T)$, where $g$ is the dimensionless coupling constant ($g < 0$ corresponds to net attraction) and $\omega_\Lambda$ is an effective high-energy cutoff. When $g < 0$, $\Lambda_0$ diverges at $T_c = \omega_\Lambda e^{1/g}$; by computing in the normal state and extrapolating, one can predict $T_c$.


## Downfolding the Bethe-Salpeter Equation

```mermaid
graph TD
    adiabatic_approx["Adiabatic Approximation (0.96)"]:::external
    bts_renormalization["BTS Renormalization Relation (1.00)"]:::external
    mu_star_phenomenological["mu#ast; as Phenomenological Parameter (0.99)"]:::external
    electron_phonon_action["Electron-Phonon Action Decomposition (0.95)"]:::external
    bse_kernel_decomposition["BSE Kernel Decomposition (0.98)"]:::external
    precursory_cooper_flow["Precursory Cooper Flow (0.90)"]:::external
    pair_propagator_decomposition["Pair Propagator Decomposition"]:::setting
    cross_term_suppressed["Cross-Channel Terms Suppressed (0.93)"]:::premise
    rpa_dynamic_screening["RPA Dynamic Screening"]:::setting
    full_bse_toy_model["Full BSE Toy Model Result (0.99)"]:::derived
    downfolded_bse_toy_model["Downfolded BSE Toy Model Result (0.99)"]:::derived
    downfolding_validity_limits["Downfolding Validity Limits (0.92)"]:::orphan
    downfolded_bse["Downfolded BSE (0.96)"]:::derived
    downfolded_me_equation["Downfolded ME Gap Equation (0.97)"]:::derived
    lambda_microscopic_definition["Microscopic Definition of lambda (0.96)"]:::derived
    mu_microscopic_definition["Microscopic Definition of mu (0.98)"]:::derived
    mu_scale_independence["BTS Relation as Corollary (1.00)"]:::derived
    bts_microscopic_equivalence["bts_microscopic_equivalence (1.00)"]:::derived
    ma_pseudopotential_justified["Morel-Anderson Ansatz Justified (0.96)"]:::derived
    strat_2(["support"]):::weak
    bse_kernel_decomposition --> strat_2
    rpa_dynamic_screening -.-> strat_2
    strat_2 --> full_bse_toy_model
    strat_3(["deduction"])
    cross_term_suppressed --> strat_3
    bse_kernel_decomposition --> strat_3
    pair_propagator_decomposition -.-> strat_3
    adiabatic_approx -.-> strat_3
    strat_3 --> downfolded_bse
    strat_4(["deduction"])
    downfolded_bse --> strat_4
    rpa_dynamic_screening -.-> strat_4
    strat_4 --> downfolded_bse_toy_model
    strat_5(["deduction"])
    downfolded_bse --> strat_5
    precursory_cooper_flow -.-> strat_5
    strat_5 --> downfolded_me_equation
    strat_6(["deduction"])
    downfolded_bse --> strat_6
    electron_phonon_action -.-> strat_6
    strat_6 --> lambda_microscopic_definition
    strat_7(["deduction"])
    downfolded_bse --> strat_7
    strat_7 --> mu_microscopic_definition
    strat_8(["deduction"])
    mu_microscopic_definition --> strat_8
    strat_8 --> mu_scale_independence
    strat_9(["deduction"])
    mu_microscopic_definition --> strat_9
    mu_star_phenomenological -.-> strat_9
    strat_9 --> ma_pseudopotential_justified
    oper_0{{"≡"}}
    downfolded_bse_toy_model --- oper_0
    full_bse_toy_model --- oper_0
    oper_1{{"≡"}}
    mu_scale_independence --- oper_1
    bts_renormalization --- oper_1
    oper_1 --- bts_microscopic_equivalence

    classDef setting fill:#f0f0f0,stroke:#999,color:#333
    classDef premise fill:#ddeeff,stroke:#4488bb,color:#333
    classDef derived fill:#ddffdd,stroke:#44bb44,color:#333
    classDef question fill:#fff3dd,stroke:#cc9944,color:#333
    classDef background fill:#f5f5f5,stroke:#bbb,stroke-dasharray: 5 5,color:#333
    classDef orphan fill:#fff,stroke:#ccc,stroke-dasharray: 5 5,color:#333
    classDef external fill:#fff,stroke:#aaa,stroke-dasharray: 3 3,color:#333
    classDef weak fill:#fff9c4,stroke:#f9a825,stroke-dasharray: 5 5,color:#333
    classDef contra fill:#ffebee,stroke:#c62828,color:#333
```

<a id="pair_propagator_decomposition"></a>

#### Pair Propagator Decomposition

📋 `pair_propagator_decomposition`

> The pair propagator (product of two single-particle Green's functions $G_{k\omega}G_{-k,-\omega}$) can be exactly decomposed into a low-energy coherent part $\Pi_{\mathrm{BCS}}$ and a high-energy incoherent remainder $\phi_{k\omega}$: $G_{k\omega}G_{-k,-\omega} = \Pi_{\mathrm{BCS}} + \phi_{k\omega}$. The coherent part is expressed in terms of the quasiparticle weight $z^e$, frequency-dependent quasiparticle weight $z_\omega^{\mathrm{ph}}$, and renormalized dispersion $\epsilon_k$. This is an exact mathematical identity introducing energy-scale separation in the two-electron channel.


<a id="cross_term_suppressed"></a>

#### Cross-Channel Terms Suppressed

📌 `cross_term_suppressed`   |   Prior: 0.90   |   Belief: **0.93**

> Cross terms mixing Coulomb and phonon channels are suppressed by the plasma frequency $\omega_p$, at order $O(\omega_c^2/\omega_p^2)$, where $\omega_c$ is an intermediate energy cutoff satisfying $\omega_D \ll \omega_c \ll E_F$. For most three-dimensional metals $\omega_c/\omega_p \lesssim 0.1$, so cross terms contribute no more than 1%.


<a id="rpa_dynamic_screening"></a>

#### RPA Dynamic Screening

📋 `rpa_dynamic_screening`

> Random Phase Approximation (RPA) dynamically screened Coulomb interaction: $W_{\mathrm{RPA}}(\mathbf{q},\nu) = v_q / (1 - v_q \Pi^0_{\mathbf{q}\nu})$, where $v_q = 4\pi e^2/q^2$ is the bare Coulomb potential and $\Pi^0$ is the non-interacting polarization function. This is a standard approximation that becomes exact in the weak-coupling limit ($r_s \lesssim 1$).


<a id="full_bse_toy_model"></a>

#### Full BSE Toy Model Result

📌 `full_bse_toy_model`   |   Belief: **0.99**

> For a toy model with aluminum-like parameters (Wigner-Seitz radius $r_s = 1.92$, adiabatic ratio $\omega_D/E_F = 0.005$), numerically solving the full frequency-momentum dependent Bethe-Salpeter equation (BSE) — using RPA dynamically screened Coulomb interaction as the electron irreducible vertex plus a model phonon interaction, without any downfolding approximation — yields a superconducting transition temperature $T_c^{\mathrm{full}}/T_F = 10^{-5.668}$, where $T_F$ is the Fermi temperature.

🔗 **support**([BSE Kernel Decomposition](#bse_kernel_decomposition))

<details><summary>Reasoning</summary>

Using the Bethe-Salpeter equation with the kernel decomposition (@bse_kernel_decomposition) into the electronic four-point vertex (approximated by RPA dynamically screened Coulomb interaction, @rpa_dynamic_screening) and a model phonon-mediated interaction, numerically solve the full frequency-momentum BSE for a toy model at $r_s = 1.92$, $\omega_D/E_F = 0.005$. The precursory Cooper flow analysis of the solution yields $T_c^{\mathrm{full}}/T_F = 10^{-5.668}$.

</details>


<a id="downfolded_bse_toy_model"></a>

#### Downfolded BSE Toy Model Result

📌 `downfolded_bse_toy_model`   |   Belief: **0.99**

> For the same toy model (aluminum-like parameters $r_s = 1.92$, $\omega_D/E_F = 0.005$), solving the downfolded frequency-only Bethe-Salpeter equation yields $T_c^{\mathrm{approx}}/T_F = 10^{-5.667}$, where $T_F$ is the Fermi temperature.

🔗 **deduction**([Downfolded BSE](#downfolded_bse))

<details><summary>Reasoning</summary>

Apply the downfolded frequency-only BSE (@downfolded_bse) to the same toy model (RPA dynamically screened Coulomb interaction @rpa_dynamic_screening, $r_s = 1.92$, $\omega_D/E_F = 0.005$). Solving the frequency-only equation yields $T_c^{\mathrm{approx}}/T_F = 10^{-5.667}$.

</details>


<a id="downfolding_validity_limits"></a>

#### Downfolding Validity Limits

📌 `downfolding_validity_limits`   |   Prior: 0.92   |   Belief: **0.92**

> The downfolded EFT-ME framework's applicability conditions and failure modes: (i) the adiabatic parameter $\omega_D/E_F \ll 1$ must hold, (ii) the intermediate cutoff $\omega_c$ must satisfy $\omega_D \ll \omega_c \ll E_F$ with $\omega_c/\omega_p \ll 1$, and (iii) the framework breaks down for strongly non-adiabatic systems (e.g. high-$T_c$ hydrides where $\omega_D/E_F \sim 0.1$) and for strongly correlated materials where the quasiparticle picture fails.


<a id="downfolded_bse"></a>

#### Downfolded BSE ★

📌 `downfolded_bse`   |   Belief: **0.96**

> The frequency-only downfolded Bethe-Salpeter equation: the full momentum-frequency BSE kernel reduces to a one-dimensional integral equation in Matsubara frequency for the Fermi-surface-averaged anomalous vertex $\Lambda_\omega$ (Cai et al., Eq. 20):
> 
> $$\Lambda_\omega = \eta_\omega + \pi T \sum_{|\omega'|<\omega_c} \bigl(\lambda_{\omega\omega'} - \mu_{\omega_c}\bigr) \frac{z_{\omega'}^{\mathrm{ph}}}{|\omega'|}\, \Lambda_{\omega'}.$$
> 
> Here $\eta_\omega$ is the symmetry-breaking pair source (set to unity for numerical convenience without affecting $T_c$), $z_\omega^{\mathrm{ph}}$ is the e-ph quasiparticle weight (Cai et al., Eq. 21), and the kernel decomposes into the phonon-mediated attraction $\lambda_{\omega\omega'}$ and the Coulomb pseudopotential $\mu_{\omega_c}$, both with microscopic definitions in terms of electron vertex functions. Corrections are bounded by three small parameters: $\omega_D/E_F$, $\omega_c^2/\omega_p^2$, and $T/\omega_c$. The momentum integration is absorbed into the density of states, and the pair propagator's coherent part generates the BCS logarithm that drives the Cooper instability.

🔗 **deduction**([Cross-Channel Terms Suppressed](#cross_term_suppressed), [BSE Kernel Decomposition](#bse_kernel_decomposition))

<details><summary>Reasoning</summary>

Starting from the full BSE with kernel decomposed into $\tilde\Gamma^e + W^{\mathrm{ph}}$ (@bse_kernel_decomposition), we substitute the exact pair propagator decomposition (@pair_propagator_decomposition) which splits $GG$ into a BCS-like coherent piece $\Pi_{\mathrm{BCS}}$ and an incoherent remainder $\phi$. The coherent piece carries the Cooper logarithm and defines the low-energy pairing channel. Momentum summation over the coherent part yields a frequency-only kernel. The cross terms mixing Coulomb and phonon channels are suppressed at $O(\omega_c^2/\omega_p^2)$ (@cross_term_suppressed), justifying their neglect. Under the adiabatic condition (@adiabatic_approx), residual phonon vertex corrections are negligible. The result is a one-dimensional integral equation in Matsubara frequency with microscopically defined $\lambda$ and $\mu_{\omega_c}$ kernels.

</details>


<a id="downfolded_me_equation"></a>

#### Downfolded ME Gap Equation

📌 `downfolded_me_equation`   |   Belief: **0.97**

> At the superconducting critical temperature $T_c$, the downfolded Bethe-Salpeter equation reduces to the traditional linearized Migdal-Eliashberg (ME) gap equation: $\Delta_\omega = \pi T_c \sum_{|\omega'|<\omega_c} (\lambda_{\omega\omega'} - \mu^*) \frac{z_{\omega'}^{\mathrm{ph}}}{|\omega'|} \Delta_{\omega'}$. As $T \to T_c$, the anomalous vertex diverges as $\Lambda_{k\omega} \sim \Delta_{k\omega}/(T - T_c)$, causing the source term $\eta$ to become irrelevant. The diverging prefactor $(T - T_c)^{-1}$ cancels between the two sides of the equation, yielding the gap equation with $\mu^* \equiv \mu_{\omega_c}$. This establishes the microscopic foundation for the ME equation with precise definitions of $\mu^*$ and $\lambda$ in terms of electron vertex functions.

🔗 **deduction**([Downfolded BSE](#downfolded_bse))

<details><summary>Reasoning</summary>

Starting from the downfolded BSE (@downfolded_bse), consider the behavior near the Cooper instability. The precursory Cooper flow (@precursory_cooper_flow) shows that the anomalous vertex diverges as $\Lambda \sim \Delta/(T - T_c)$ when $T \to T_c$. Substituting this scaling into the downfolded BSE, the source term $\eta$ becomes negligible compared to the diverging vertex, and the $(T - T_c)^{-1}$ prefactor cancels on both sides. The result is the linearized gap equation — identical in form to the traditional ME equation, but now with $\mu^*$ and $\lambda$ having precise microscopic definitions from the downfolding.

</details>


<a id="lambda_microscopic_definition"></a>

#### Microscopic Definition of lambda

📌 `lambda_microscopic_definition`   |   Belief: **0.96**

> The electron-phonon coupling $\lambda(\omega, \omega')$ in the downfolded BSE has a microscopic definition: it is the Fermi-surface average of the phonon-mediated interaction $W^{\mathrm{ph}}$ weighted by quasiparticle renormalization factors $z^e$ and $z_\omega^{\mathrm{ph}}$.
> 
> In the standard ME normalization, the static dimensionless coupling follows the Fermi-surface average of $g^2/\omega^2$ over phonon branches $\kappa$ (Cai et al., Eq. 31):
> 
> $$\lambda = N_F \sum_\kappa \left\langle \frac{g_\kappa^2(\mathbf{k}, \mathbf{q})}{\omega_{\kappa, \mathbf{q}}^2}\right\rangle_{\mathrm{FS}},$$
> 
> with $|\mathbf{k}| = |\mathbf{k} + \mathbf{q}| = k_F$, $N_F$ the density of states at the Fermi level, and $g_\kappa(\mathbf{k}, \mathbf{q})$ the physical screened-and-renormalized e-ph vertex (see @eft_eph_vertex). This definition reduces to the standard Eliashberg $\lambda$ in the adiabatic limit but retains dynamical corrections from the electron self-energy.

🔗 **deduction**([Downfolded BSE](#downfolded_bse))

<details><summary>Reasoning</summary>

The downfolded BSE (@downfolded_bse) expresses the pairing kernel as $K = \lambda - \mu_{\omega_c}$. The phonon-mediated part $\lambda(\omega, \omega')$ arises from projecting $W^{\mathrm{ph}}$ (the phonon-mediated interaction from the electron-phonon action decomposition, @electron_phonon_action) onto the Fermi surface using the coherent part of the pair propagator. The counterterm $S_{\mathrm{CT}}$ in the action ensures no double-counting of the static screening already included in the physical phonon dispersion. The resulting expression for $\lambda$ involves the Fermi-surface average of $W^{\mathrm{ph}}$ weighted by quasiparticle factors, providing a controlled microscopic definition that generalizes the standard Eliashberg coupling constant.

</details>


<a id="mu_microscopic_definition"></a>

#### Microscopic Definition of mu

📌 `mu_microscopic_definition`   |   Belief: **0.98**

> The Coulomb pseudopotential $\mu_{\omega_c}(\omega, \omega')$ in the downfolded BSE has a microscopic definition: it is determined by the purely electronic particle-particle irreducible four-point vertex $\tilde\Gamma^e$ projected onto the Fermi surface, with the high-energy electronic degrees of freedom integrated out above the cutoff $\omega_c$.
> 
> Operationally, in a purely electronic theory ($\lambda = 0$, $z^{\mathrm{ph}} = 1$), solving the downfolded equation gives the temperature-dependent effective Cooper-channel repulsion (Cai et al., Eq. 23):
> 
> $$\gamma_T = \frac{\mu_{\omega_c}}{1 + \mu_{\omega_c} \ln(\omega_c/T)} \quad (T \ll \omega_c),$$
> 
> where $\gamma_T$ is computed directly from the four-point vertex (Cai et al., Eq. 24):
> 
> $$\gamma_T \equiv z_e^2\, N_F^{\ast}\, \bigl\langle \Gamma_4^e(\mathbf{k}_F, \omega_0;\, \mathbf{k}_F', \omega_0)\bigr\rangle_{\mathbf{k}_F, \mathbf{k}_F'},\qquad \omega_0 = \pi T.$$
> 
> Here $z_e$ is the electronic quasiparticle weight, $N_F^\ast$ is the quasiparticle density of states, and $\Gamma_4^e$ is the full electronic four-point vertex on the Fermi surface evaluated at the lowest Matsubara frequency $\omega_0 = \pi T$. Inverting Eq. 23 yields $\mu_{\omega_c}$ from the measured $\gamma_T$, providing a precise meaning to the Coulomb pseudopotential as the effective repulsion in the low-energy pairing channel, renormalized by all electronic correlations.

🔗 **deduction**([Downfolded BSE](#downfolded_bse))

<details><summary>Reasoning</summary>

The downfolded BSE (@downfolded_bse) separates the pairing kernel into phonon ($\lambda$) and Coulomb ($\mu_{\omega_c}$) contributions. The Coulomb part is obtained by projecting the purely electronic irreducible four-point vertex $\tilde\Gamma^e$ from the BSE kernel onto the Fermi surface, with frequency integration restricted to the range above $\omega_c$ handled by the incoherent part of the pair propagator. This construction defines $\mu_{\omega_c}$ as a functional of $\tilde\Gamma^e$ — the quantity that encodes all non-perturbative Coulomb correlations — evaluated at a specific energy scale, without any phenomenological input.

</details>


<a id="mu_scale_independence"></a>

#### BTS Relation as Corollary

📌 `mu_scale_independence`   |   Belief: **1.00**

> The BTS renormalization relation $\mu_{\omega_c} = \mu_{\omega_c'} / (1 + \mu_{\omega_c'} \ln(\omega_c'/\omega_c))$ emerges as a corollary of the microscopic definition of $\mu_{\omega_c}$: changing the cutoff $\omega_c$ reshuffles contributions between the explicit Coulomb kernel and the Cooper logarithm in the BCS propagator, leaving the physical $T_c$ invariant. This provides a microscopic derivation of the originally phenomenological BTS relation.

🔗 **deduction**([Microscopic Definition of mu](#mu_microscopic_definition))

<details><summary>Reasoning</summary>

Given the microscopic definition of $\mu_{\omega_c}$ (@mu_microscopic_definition) as a Fermi-surface projection of $\tilde\Gamma^e$ with a cutoff at $\omega_c$, we can examine how $\mu$ transforms when $\omega_c$ is varied. Shifting the cutoff from $\omega_c'$ to $\omega_c$ transfers spectral weight between the explicit Coulomb kernel and the BCS Cooper logarithm $\ln(\omega_c'/T)$ in the coherent pair propagator. Requiring that the physical observable ($T_c$) remain invariant under this reshuffling yields the BTS relation $\mu_{\omega_c} = \mu_{\omega_c'} / (1 + \mu_{\omega_c'} \ln(\omega_c'/\omega_c))$ as an exact consequence of the downfolded theory's structure, rather than an ad hoc ansatz.

</details>


<a id="bts_microscopic_equivalence"></a>

#### bts_microscopic_equivalence

📌 `bts_microscopic_equivalence`   |   Prior: 0.98   |   Belief: **1.00**

> same_truth(A, B)


<a id="ma_pseudopotential_justified"></a>

#### Morel-Anderson Ansatz Justified

📌 `ma_pseudopotential_justified`   |   Belief: **0.96**

> The Morel-Anderson constant-pseudopotential ansatz — treating $\mu_{\omega_c}$ as approximately frequency-independent — is microscopically justified: the four-point vertex $\tilde\Gamma^e$ varies on electronic energy scales ($E_F$), which are much larger than the phonon scale ($\omega_D$). Within the low-energy window $|\omega|, |\omega'| < \omega_c \ll E_F$, the Coulomb kernel is effectively constant, validating the traditional constant-$\mu^*$ treatment used in Eliashberg theory.

🔗 **deduction**([Microscopic Definition of mu](#mu_microscopic_definition))

<details><summary>Reasoning</summary>

The microscopic definition of $\mu_{\omega_c}$ (@mu_microscopic_definition) shows it is determined by the electronic four-point vertex $\tilde\Gamma^e$, which varies on the scale of $E_F$. Within the low-energy window $|\omega|, |\omega'| < \omega_c$ where $\omega_c \ll E_F$, the frequency dependence of $\tilde\Gamma^e$ is negligible, so $\mu_{\omega_c}(\omega, \omega') \approx \mu_{\omega_c}$ becomes effectively a constant. This provides a first-principles justification for the phenomenological Morel-Anderson ansatz (@mu_star_phenomenological) that treats $\mu^*$ as a single number rather than a frequency-dependent kernel. The justification holds precisely because the energy-scale hierarchy $\omega_c \ll E_F$ is maintained.

</details>


## Coulomb Pseudopotential

```mermaid
graph TD
    bts_renormalization["BTS Renormalization Relation (1.00)"]:::external
    rpa_predicts_attractive_mu["RPA Predicts Attractive mu#ast; (0.13)"]:::external
    mu_microscopic_definition["Microscopic Definition of mu (0.98)"]:::external
    ueg_vertex_challenge["UEG Four-Point Vertex Challenge (0.95)"]:::background
    vdiagmc_method["vDiagMC Method (0.87)"]:::premise
    homotopic_expansion["Homotopic Expansion (0.84)"]:::premise
    mu_vdiagmc_values["mu from vDiagMC: Numerical Values (0.75)"]:::derived
    rpa_vs_vdiagmc["rpa_vs_vdiagmc (1.00)"]:::derived
    strat_10(["support"]):::weak
    vdiagmc_method --> strat_10
    homotopic_expansion --> strat_10
    ueg_vertex_challenge -.-> strat_10
    mu_microscopic_definition -.-> strat_10
    bts_renormalization -.-> strat_10
    strat_10 --> mu_vdiagmc_values
    oper_1{{"≡"}}
    bts_renormalization --- oper_1
    oper_2{{"⊗"}}:::contra
    rpa_predicts_attractive_mu --- oper_2
    mu_vdiagmc_values --- oper_2
    oper_2 --- rpa_vs_vdiagmc

    classDef setting fill:#f0f0f0,stroke:#999,color:#333
    classDef premise fill:#ddeeff,stroke:#4488bb,color:#333
    classDef derived fill:#ddffdd,stroke:#44bb44,color:#333
    classDef question fill:#fff3dd,stroke:#cc9944,color:#333
    classDef background fill:#f5f5f5,stroke:#bbb,stroke-dasharray: 5 5,color:#333
    classDef orphan fill:#fff,stroke:#ccc,stroke-dasharray: 5 5,color:#333
    classDef external fill:#fff,stroke:#aaa,stroke-dasharray: 3 3,color:#333
    classDef weak fill:#fff9c4,stroke:#f9a825,stroke-dasharray: 5 5,color:#333
    classDef contra fill:#ffebee,stroke:#c62828,color:#333
```

<a id="ueg_vertex_challenge"></a>

#### UEG Four-Point Vertex Challenge

📌 `ueg_vertex_challenge`   |   Prior: 0.95   |   Belief: **0.95**

> Computing the particle-particle irreducible four-point vertex $\tilde\Gamma^e$ of the uniform electron gas (UEG) is a long-standing challenge: perturbation theory in the bare Coulomb interaction diverges for $r_s \gtrsim 1$, and partial resummations (RPA, GW) miss crucial vertex corrections. A controlled, systematically improvable method is needed to evaluate $\tilde\Gamma^e$ in the metallic density range $r_s \in [1, 6]$.


<a id="vdiagmc_method"></a>

#### vDiagMC Method

📌 `vdiagmc_method`   |   Prior: 0.90   |   Belief: **0.87**

> Variational diagrammatic Monte Carlo (vDiagMC) provides a controlled, systematically improvable method for computing Feynman diagrammatic series to high order: (i) bold-line (self-consistent) resummation avoids infrared divergences in individual diagrams, (ii) stochastic sampling of diagram topologies and internal variables accesses orders unreachable by deterministic methods, (iii) the series can be extrapolated to infinite order with controlled error bars. For the UEG, vDiagMC achieves reliable convergence of the irreducible vertex in the metallic density range.


<a id="homotopic_expansion"></a>

#### Homotopic Expansion

📌 `homotopic_expansion`   |   Prior: 0.88   |   Belief: **0.84**

> The homotopic transformation provides a physically motivated reorganization of the diagrammatic series: by continuously deforming the bare Coulomb interaction $v(q)$ into a form that incorporates partial screening at each perturbative order, the series convergence is dramatically improved. This allows the vDiagMC calculation to reach converged results for the four-point vertex at metallic densities with modest diagram orders ($n \lesssim 7$).


<a id="mu_vdiagmc_values"></a>

#### mu from vDiagMC: Numerical Values ★

📌 `mu_vdiagmc_values`   |   Belief: **0.75**

> vDiagMC calculations of the UEG four-point vertex yield the Coulomb pseudopotential at the Fermi energy scale: $\mu_{E_F}(r_s)$ is positive and monotonically increasing with $r_s$ in the metallic density range, approximately following $\mu_{E_F} \approx 0.27\, r_s$. The complete set of values (Cai et al., TABLE I), computed at $\omega_c = 0.1\, E_F$ and rescaled to $E_F$ via the BTS relation:
> 
> | $r_s$              | 1       | 2       | 3       | 4        | 5        | 6      |
> |--------------------|---------|---------|---------|----------|----------|--------|
> | $\mu_{0.1\,E_F}$ | 0.172(4)| 0.238(4)| 0.278(6)| 0.306(15)| 0.328(12)| 0.35(3)|
> | $\mu_{E_F}$       | 0.28(1) | 0.53(2) | 0.77(5) | 1.0(2)   | 1.3(2)   | 1.8(8) |
> 
> Numbers in parentheses indicate the systematic uncertainty in the last digit. These results, combined with the BTS relation, yield $\mu^\ast \approx 0.12\text{--}0.18$ at the Debye scale, consistent with the empirical range but now derived from first principles with controlled error bars of a few percent. The values are dramatically larger than the static RPA, Morel-Anderson, and dynamic RPA predictions for $r_s > 0.5$ — by a factor of three at $r_s = 5$ — and resolve the long-standing contradiction between phenomenological and RPA-based treatments of the Coulomb pseudopotential.

🔗 **support**([vDiagMC Method](#vdiagmc_method), [Homotopic Expansion](#homotopic_expansion))

<details><summary>Reasoning</summary>

The microscopic definition of $\mu_{\omega_c}$ (@mu_microscopic_definition) reduces, for the uniform electron gas, to evaluating the particle-particle irreducible four-point vertex $\tilde\Gamma^e$ — a notoriously difficult quantity (@ueg_vertex_challenge). The vDiagMC method (@vdiagmc_method) provides a controlled, systematically improvable approach by stochastically sampling Feynman diagrams with bold-line propagators. The homotopic expansion (@homotopic_expansion) dramatically improves convergence by reorganizing the series through a continuous deformation of the bare interaction, enabling convergence at modest diagram orders. Together, these yield numerically exact values of $\mu_{E_F}(r_s)$ with controlled error bars (e.g. $\mu_{E_F} = 0.53(2)$ at $r_s = 2$). The BTS renormalization relation (@bts_renormalization) then maps $\mu_{E_F}$ down to $\mu^*$ at the Debye scale, producing values in the range 0.12--0.18 that are consistent with the empirical range but now microscopically grounded.

</details>


<a id="rpa_vs_vdiagmc"></a>

#### rpa_vs_vdiagmc

📌 `rpa_vs_vdiagmc`   |   Prior: 0.95   |   Belief: **1.00**

> not_both_true(A, B)


## Electron-Phonon Coupling

```mermaid
graph TD
    dfpt_computes_lambda["DFPT Computes lambda (0.99)"]:::external
    lambda_microscopic_definition["Microscopic Definition of lambda (0.96)"]:::external
    ward_identity["Ward Identity at q->0 (0.98)"]:::premise
    gamma3_vdiagmc["vDiagMC Computation of Gamma_3 (0.88)"]:::premise
    dfpt_eph_ansatz["DFPT Expression for e-ph Coupling (0.90)"]:::background
    quasiparticle_mass_near_unity["Quasiparticle Mass Near Unity (0.92)"]:::premise
    eft_eph_vertex["EFT Electron-Phonon Vertex (0.97)"]:::derived
    gamma3_approximation["Approximate Gamma_3 within Fermi Sphere (0.86)"]:::derived
    gamma3_interpolation_test_valid["Gamma_3 Interpolation Test Valid (0.90)"]:::premise
    gamma3_evidence_independent["Gamma_3 Evidence Independence (0.93)"]:::premise
    eft_vertex_matches_dfpt["EFT Vertex Matches DFPT (0.88)"]:::derived
    dfpt_reliable_for_simple_metals["DFPT Reliable for Simple Metals (0.87)"]:::derived
    strat_11(["deduction"])
    lambda_microscopic_definition --> strat_11
    strat_11 --> eft_eph_vertex
    strat_12(["deduction"])
    ward_identity --> strat_12
    gamma3_vdiagmc --> strat_12
    gamma3_interpolation_test_valid --> strat_12
    gamma3_evidence_independent --> strat_12
    strat_12 --> gamma3_approximation
    strat_13(["deduction"])
    eft_eph_vertex --> strat_13
    gamma3_approximation --> strat_13
    dfpt_eph_ansatz -.-> strat_13
    strat_13 --> eft_vertex_matches_dfpt
    strat_14(["deduction"])
    eft_vertex_matches_dfpt --> strat_14
    quasiparticle_mass_near_unity --> strat_14
    dfpt_computes_lambda -.-> strat_14
    strat_14 --> dfpt_reliable_for_simple_metals
    strat_15(["infer"]):::weak
    eft_eph_vertex --> strat_15
    gamma3_approximation --> strat_15
    quasiparticle_mass_near_unity --> strat_15
    strat_15 --> dfpt_reliable_for_simple_metals

    classDef setting fill:#f0f0f0,stroke:#999,color:#333
    classDef premise fill:#ddeeff,stroke:#4488bb,color:#333
    classDef derived fill:#ddffdd,stroke:#44bb44,color:#333
    classDef question fill:#fff3dd,stroke:#cc9944,color:#333
    classDef background fill:#f5f5f5,stroke:#bbb,stroke-dasharray: 5 5,color:#333
    classDef orphan fill:#fff,stroke:#ccc,stroke-dasharray: 5 5,color:#333
    classDef external fill:#fff,stroke:#aaa,stroke-dasharray: 3 3,color:#333
    classDef weak fill:#fff9c4,stroke:#f9a825,stroke-dasharray: 5 5,color:#333
    classDef contra fill:#ffebee,stroke:#c62828,color:#333
```

<a id="ward_identity"></a>

#### Ward Identity at q->0

📌 `ward_identity`   |   Prior: 0.98   |   Belief: **0.98**

> An exact Ward identity relates the three-point electron-phonon vertex $\Gamma_3^e(k, q)$ to the electron self-energy in the long-wavelength limit $q \to 0$: $\lim_{q \to 0} \Gamma_3^e(k, q) = 1 - \partial\Sigma(k)/\partial\epsilon_k$. This identity is a consequence of charge conservation and provides an exact constraint on vertex corrections at zero momentum transfer.


<a id="gamma3_vdiagmc"></a>

#### vDiagMC Computation of Gamma_3

📌 `gamma3_vdiagmc`   |   Prior: 0.88   |   Belief: **0.88**

> vDiagMC computation of the three-point vertex $\Gamma_3^e(k, q)$ of the UEG at finite momentum transfer $q$ shows that vertex corrections are modest (10--20% level) for momenta within the Fermi sphere ($|k|, |k+q| \lesssim k_F$) at metallic densities $r_s \in [2, 4]$. The corrections vary smoothly with $q$ and can be accurately interpolated between the Ward-identity limit ($q \to 0$) and the large-$q$ asymptotic behavior.


<a id="dfpt_eph_ansatz"></a>

#### DFPT Expression for e-ph Coupling

📌 `dfpt_eph_ansatz`   |   Prior: 0.90   |   Belief: **0.90**

> The DFPT expression for the electron-phonon coupling $g^{\mathrm{DFPT}}(k, q) = \sqrt{\omega_q / 2} \, \langle k+q | \delta V_{\mathrm{KS}} / \delta u_q | k \rangle$ implicitly assumes that vertex corrections to the electron-phonon coupling beyond the Kohn-Sham mean-field level are absorbed into the exchange-correlation functional. The accuracy of this ansatz depends on how well DFT captures the relevant vertex corrections.


<a id="quasiparticle_mass_near_unity"></a>

#### Quasiparticle Mass Near Unity

📌 `quasiparticle_mass_near_unity`   |   Prior: 0.92   |   Belief: **0.92**

> For simple metals at metallic densities ($r_s \in [2, 4]$), the quasiparticle effective mass ratio $m^*/m \approx 1$ (deviations less than 5--10%). This near-unity mass ratio means that the quasiparticle renormalization factor $z^e \approx 1/(1 + \lambda_e)$ primarily reflects the frequency-dependent self-energy rather than momentum-dependent mass enhancement, simplifying the mapping between microscopic and DFPT-level electron-phonon coupling.


<a id="eft_eph_vertex"></a>

#### EFT Electron-Phonon Vertex

📌 `eft_eph_vertex`   |   Belief: **0.97**

> The EFT expression for the physical electron-phonon coupling vertex factorizes the bare coupling into a screening factor and vertex/quasiparticle renormalizations (Cai et al., Eq. 32):
> 
> $$g_\kappa(\mathbf{k}, \mathbf{q}) = g_{\kappa\mathbf{q}}^{(0)}\, \frac{z^e}{\epsilon_\mathbf{q}}\, \Gamma_3^e(\mathbf{k}, \mathbf{q}),$$
> 
> where $g_{\kappa\mathbf{q}}^{(0)}$ is the bare e-ph matrix element, $\epsilon_\mathbf{q}$ is the electronic dielectric function, $z^e$ is the electronic quasiparticle weight, and $\Gamma_3^e(\mathbf{k}, \mathbf{q})$ is the electronic three-point vertex correction. The combination $z^e \Gamma_3^e(\mathbf{k}, \mathbf{q})$ can be interpreted as the quasiparticle vertex correction to the screened interaction. The corresponding $\lambda$ in the downfolded BSE is the Fermi-surface average of $|g_\kappa(\mathbf{k}, \mathbf{q})|^2 / \omega_{\kappa,\mathbf{q}}^2$ over phonon branches (see @lambda_microscopic_definition).

🔗 **deduction**([Microscopic Definition of lambda](#lambda_microscopic_definition))

<details><summary>Reasoning</summary>

The microscopic definition of $\lambda$ (@lambda_microscopic_definition) involves the Fermi-surface average of $W^{\mathrm{ph}}$ weighted by quasiparticle factors. Expanding $W^{\mathrm{ph}}$ in terms of the phonon propagator and electron-phonon vertices, and factoring out the quasiparticle weight $z^e$ from the pair propagator coherent part, yields the EFT vertex $g(k,q) = z^e \cdot \Gamma_3^e(k,q) \cdot g_0(k,q)$.

</details>


<a id="gamma3_approximation"></a>

#### Approximate Gamma_3 within Fermi Sphere

📌 `gamma3_approximation`   |   Belief: **0.86**

> The three-point vertex $\Gamma_3^e(k, q)$ for states within the Fermi sphere can be accurately approximated by interpolation between two controlled limits: (i) the exact Ward identity at $q \to 0$ giving $\Gamma_3^e = 1 - \partial\Sigma/\partial\epsilon_k = m^*/m$, and (ii) the vDiagMC results at finite $q$ showing smooth, modest variations. For simple metals, this yields $\Gamma_3^e \approx m^*/m$ to within 10--15% across the relevant momentum range.

🔗 **deduction**([Ward Identity at q->0](#ward_identity), [vDiagMC Computation of Gamma_3](#gamma3_vdiagmc), [Gamma_3 Interpolation Test Valid](#gamma3_interpolation_test_valid), [Gamma_3 Evidence Independence](#gamma3_evidence_independent))

<details><summary>Reasoning</summary>

The Ward identity provides the exact value at $q = 0$ (@ward_identity), while the vDiagMC calculation confirms smooth, modest finite-$q$ variations (@gamma3_vdiagmc). Given that these are valid and independent tests of the same interpolation claim (@gamma3_interpolation_test_valid, @gamma3_evidence_independent), they jointly support the approximation $\Gamma_3^e \approx m^*/m$ with bounded momentum-dependence error.

</details>

<details><summary>Method</summary>

- method: deduction

</details>


<a id="gamma3_interpolation_test_valid"></a>

#### Gamma_3 Interpolation Test Valid

📌 `gamma3_interpolation_test_valid`   |   Prior: 0.90   |   Belief: **0.90**

> The Ward-identity limit and the finite-$q$ vDiagMC vertex calculation are valid tests of the same interpolation approximation for $\Gamma_3^e(k,q)$ within the Fermi sphere. Passing both tests licenses using the approximation $\Gamma_3^e \approx m^*/m$ across the relevant momentum range.


<a id="gamma3_evidence_independent"></a>

#### Gamma_3 Evidence Independence

📌 `gamma3_evidence_independent`   |   Prior: 0.93   |   Belief: **0.93**

> The Ward-identity constraint at $q \to 0$ and the finite-$q$ vDiagMC calculation probe independent aspects of the three-point vertex: one is an exact conservation-law limit, while the other is a numerical many-body calculation away from that limit.


<a id="eft_vertex_matches_dfpt"></a>

#### EFT Vertex Matches DFPT

📌 `eft_vertex_matches_dfpt`   |   Belief: **0.88**

> In the uniform electron gas at densities $r_s \in [1,5]$, the EFT electron-phonon vertex $g(\mathbf{k},\mathbf{q}) = g^{(0)}_{\mathbf{q}} \cdot (z^e/\epsilon_{\mathbf{q}}) \cdot \Gamma_3^e(\mathbf{k};\mathbf{q})$ is numerically well approximated by the DFPT Kohn-Sham screened potential $g^{\mathrm{KS}}(\mathbf{q}) = g^{(0)}_{\mathbf{q}} / [1 - (v_{\mathbf{q}} + f_{xc})\chi_0^e(\mathbf{q})]$ for Fermi-surface-relevant momentum transfers $|\mathbf{q}| \leq 2k_F$, with weak residual $\mathbf{k}$-dependence.

🔗 **deduction**([EFT Electron-Phonon Vertex](#eft_eph_vertex), [Approximate Gamma_3 within Fermi Sphere](#gamma3_approximation))

<details><summary>Reasoning</summary>

Substituting the approximate $\Gamma_3^e \approx m^*/m$ (@gamma3_approximation) into the EFT vertex expression (@eft_eph_vertex) $g = z^e \cdot \Gamma_3^e \cdot g_0$, and using the Migdal relation $z^e \approx m/m^*$, the product $z^e \cdot \Gamma_3^e \approx (m/m^*)(m^*/m) = 1$. This means $g(k,q) \approx g_0(k,q)$, which after screening gives exactly the DFPT Kohn-Sham expression (@dfpt_eph_ansatz) $g^{\mathrm{KS}}(q)$. The vertex-level agreement holds for $|q| \leq 2k_F$ with weak residual $k$-dependence.

</details>


<a id="dfpt_reliable_for_simple_metals"></a>

#### DFPT Reliable for Simple Metals ★

📌 `dfpt_reliable_for_simple_metals`   |   Belief: **0.87**

> For simple metals, the DFPT calculation of the electron-phonon coupling constant $\lambda$ is reliable: the EFT vertex matches the DFPT expression at the vertex level, and the quasiparticle density of states $N_F^*$ nearly equals the band density of states $N_F^{(0)}$, so $\lambda_{\mathrm{EFT}} \approx \lambda_{\mathrm{DFPT}}$ with corrections at the few-percent level.

🔗 **infer**([EFT Electron-Phonon Vertex](#eft_eph_vertex), [Approximate Gamma_3 within Fermi Sphere](#gamma3_approximation), [Quasiparticle Mass Near Unity](#quasiparticle_mass_near_unity))


## Conventional Superconductors

```mermaid
graph TD
    bts_renormalization["BTS Renormalization Relation (1.00)"]:::external
    tc_al_experimental["Tc(Al) Experimental (0.99)"]:::external
    tc_li_experimental["Tc(Li) Experimental (0.85)"]:::external
    tc_zn_experimental["Tc(Zn) Experimental (0.99)"]:::external
    tc_al_phenomenological["Tc(Al) Phenomenological Prediction (1.00)"]:::external
    tc_li_phenomenological["Tc(Li) Phenomenological Prediction (1.00)"]:::external
    tc_zn_phenomenological["Tc(Zn) Phenomenological Prediction (1.00)"]:::external
    precursory_cooper_flow["Precursory Cooper Flow (0.90)"]:::external
    downfolded_bse["Downfolded BSE (0.96)"]:::external
    mu_vdiagmc_values["mu from vDiagMC: Numerical Values (0.75)"]:::external
    dfpt_reliable_for_simple_metals["DFPT Reliable for Simple Metals (0.87)"]:::external
    aluminum_parameters["Aluminum Material Parameters"]:::setting
    lithium_parameters["Lithium Material Parameters"]:::setting
    sodium_parameters["Sodium Material Parameters"]:::setting
    magnesium_parameters["Magnesium Material Parameters"]:::setting
    zinc_parameters["Zinc Material Parameters"]:::setting
    simple_metals_weak_lattice["Simple Metals Have Weak Lattice Effects (0.90)"]:::background
    ueg_pseudopotential_parameterization["UEG mu#ast; Parameterization and Mapping (0.85)"]:::premise
    ab_initio_workflow["Ab Initio Tc Prediction Workflow (0.80)"]:::derived
    mu_available_for_simple_metals["mu#ast; Available for Simple Metals (0.78)"]:::derived
    tc_al_predicted["Tc(Al) Ab Initio Prediction (0.84)"]:::derived
    tc_zn_predicted["Tc(Zn) Ab Initio Prediction (0.84)"]:::derived
    tc_li_predicted["Tc(Li) Ab Initio Prediction (0.82)"]:::derived
    al_pressure_transition["Al Pressure-Tc Transition (0.82)"]:::derived
    tc_mg_na_near_qpt["Na and Mg Near Quantum Phase Transition (0.82)"]:::derived
    tc_al_abinitio_outperforms_phenomenological["Al Ab Initio Prediction Outperforms Phenomenological (0.83)"]:::derived
    tc_al_comparison_valid["Al Tc Comparison Valid (0.95)"]:::premise
    tc_zn_abinitio_outperforms_phenomenological["Zn Ab Initio Prediction Outperforms Phenomenological (0.86)"]:::derived
    tc_zn_comparison_valid["Zn Tc Comparison Valid (0.97)"]:::premise
    tc_li_abinitio_outperforms_phenomenological["Li Ab Initio Prediction Outperforms Phenomenological (0.79)"]:::derived
    tc_li_comparison_valid["Li Tc Comparison Valid (0.88)"]:::premise
    strat_10(["support"]):::weak
    bts_renormalization -.-> strat_10
    strat_10 --> mu_vdiagmc_values
    strat_16(["support"]):::weak
    ueg_pseudopotential_parameterization --> strat_16
    mu_vdiagmc_values --> strat_16
    simple_metals_weak_lattice -.-> strat_16
    bts_renormalization -.-> strat_16
    strat_16 --> mu_available_for_simple_metals
    strat_17(["deduction"])
    downfolded_bse --> strat_17
    mu_available_for_simple_metals --> strat_17
    dfpt_reliable_for_simple_metals --> strat_17
    strat_17 --> ab_initio_workflow
    strat_18(["infer"]):::weak
    downfolded_bse --> strat_18
    mu_vdiagmc_values --> strat_18
    dfpt_reliable_for_simple_metals --> strat_18
    ueg_pseudopotential_parameterization --> strat_18
    simple_metals_weak_lattice -.-> strat_18
    bts_renormalization -.-> strat_18
    strat_18 --> ab_initio_workflow
    strat_19(["support"]):::weak
    ab_initio_workflow --> strat_19
    aluminum_parameters -.-> strat_19
    strat_19 --> tc_al_predicted
    strat_20(["support"]):::weak
    ab_initio_workflow --> strat_20
    zinc_parameters -.-> strat_20
    strat_20 --> tc_zn_predicted
    strat_21(["support"]):::weak
    ab_initio_workflow --> strat_21
    lithium_parameters -.-> strat_21
    strat_21 --> tc_li_predicted
    strat_22(["support"]):::weak
    ab_initio_workflow --> strat_22
    aluminum_parameters -.-> strat_22
    strat_22 --> al_pressure_transition
    strat_23(["support"]):::weak
    ab_initio_workflow --> strat_23
    magnesium_parameters -.-> strat_23
    sodium_parameters -.-> strat_23
    precursory_cooper_flow -.-> strat_23
    strat_23 --> tc_mg_na_near_qpt
    strat_26(["likelihood"]):::weak
    tc_al_experimental --> strat_26
    tc_al_predicted --> strat_26
    tc_al_phenomenological --> strat_26
    tc_al_comparison_valid --> strat_26
    strat_26 --> tc_al_abinitio_outperforms_phenomenological
    strat_29(["likelihood"]):::weak
    tc_zn_experimental --> strat_29
    tc_zn_predicted --> strat_29
    tc_zn_phenomenological --> strat_29
    tc_zn_comparison_valid --> strat_29
    strat_29 --> tc_zn_abinitio_outperforms_phenomenological
    strat_32(["likelihood"]):::weak
    tc_li_experimental --> strat_32
    tc_li_predicted --> strat_32
    tc_li_phenomenological --> strat_32
    tc_li_comparison_valid --> strat_32
    strat_32 --> tc_li_abinitio_outperforms_phenomenological
    oper_1{{"≡"}}
    bts_renormalization --- oper_1
    oper_2{{"⊗"}}:::contra
    mu_vdiagmc_values --- oper_2

    classDef setting fill:#f0f0f0,stroke:#999,color:#333
    classDef premise fill:#ddeeff,stroke:#4488bb,color:#333
    classDef derived fill:#ddffdd,stroke:#44bb44,color:#333
    classDef question fill:#fff3dd,stroke:#cc9944,color:#333
    classDef background fill:#f5f5f5,stroke:#bbb,stroke-dasharray: 5 5,color:#333
    classDef orphan fill:#fff,stroke:#ccc,stroke-dasharray: 5 5,color:#333
    classDef external fill:#fff,stroke:#aaa,stroke-dasharray: 3 3,color:#333
    classDef weak fill:#fff9c4,stroke:#f9a825,stroke-dasharray: 5 5,color:#333
    classDef contra fill:#ffebee,stroke:#c62828,color:#333
```

<a id="aluminum_parameters"></a>

#### Aluminum Material Parameters

📋 `aluminum_parameters`

> Aluminum (Al): FCC crystal structure, $r_s = 2.07$, band mass $m_b = 1.05$, DFPT electron-phonon coupling $\lambda = 0.44$, logarithmic phonon frequency $\omega_{\mathrm{log}} = 320$ K, Fermi temperature $T_F = 1.3 \times 10^5$ K.


<a id="lithium_parameters"></a>

#### Lithium Material Parameters

📋 `lithium_parameters`

> Lithium (Li): 9R crystal structure at low $T$ (also studied in HCP). 9R parameters: $r_s = 3.25$, $m_b = 1.75$, $\lambda = 0.34$, $\omega_{\mathrm{log}} = 242$ K, $T_F = 4.0 \times 10^4$ K. HCP parameters: $r_s = 3.19$, $m_b = 1.4$, $\lambda = 0.37$, $\omega_{\mathrm{log}} = 243$ K, $T_F = 4.1 \times 10^4$ K. Crystal structure at sub-kelvin temperatures remains debated.


<a id="sodium_parameters"></a>

#### Sodium Material Parameters

📋 `sodium_parameters`

> Sodium (Na): BCC crystal structure, $r_s = 3.96$, band mass $m_b = 1.0$, DFPT electron-phonon coupling $\lambda = 0.2$, logarithmic phonon frequency $\omega_{\mathrm{log}} = 127$ K, Fermi temperature $T_F = 4.2 \times 10^4$ K. No superconductivity observed down to mK temperatures.


<a id="magnesium_parameters"></a>

#### Magnesium Material Parameters

📋 `magnesium_parameters`

> Magnesium (Mg): HCP crystal structure, $r_s = 2.66$, band mass $m_b = 1.02$, DFPT electron-phonon coupling $\lambda = 0.24$, logarithmic phonon frequency $\omega_{\mathrm{log}} = 269$ K, Fermi temperature $T_F = 8.0 \times 10^4$ K. No superconductivity observed down to mK temperatures.


<a id="zinc_parameters"></a>

#### Zinc Material Parameters

📋 `zinc_parameters`

> Zinc (Zn): HCP crystal structure, $r_s = 2.90$, band mass $m_b = 1.0$, DFPT electron-phonon coupling $\lambda = 0.502$, logarithmic phonon frequency $\omega_{\mathrm{log}} = 111$ K, Fermi temperature $T_F = 1.21 \times 10^5$ K.


<a id="simple_metals_weak_lattice"></a>

#### Simple Metals Have Weak Lattice Effects

📌 `simple_metals_weak_lattice`   |   Prior: 0.90   |   Belief: **0.90**

> Simple metals (Al, Li, Na, Mg, Zn) have weak lattice effects in the Coulomb pseudopotential: the difference between the crystalline $\mu^*$ and the UEG $\mu^*$ at the same $r_s$ is small (a few percent) because the nearly-free-electron character of these metals means the Fermi surface is approximately spherical and the electronic structure is well described by the homogeneous electron gas with minor crystal-field perturbations.


<a id="ueg_pseudopotential_parameterization"></a>

#### UEG mu* Parameterization and Mapping

📌 `ueg_pseudopotential_parameterization`   |   Prior: 0.85   |   Belief: **0.85**

> The UEG Coulomb pseudopotential $\mu_{E_F}(r_s)$ computed by vDiagMC can be parameterized as a smooth function of $r_s$ and mapped onto real materials by using the material's effective $r_s$ (determined from the valence electron density). Combined with the BTS relation to run $\mu_{E_F}$ down to the Debye scale, this provides $\mu^*(r_s)$ for any simple metal without additional adjustable parameters.


<a id="ab_initio_workflow"></a>

#### Ab Initio Tc Prediction Workflow ★

📌 `ab_initio_workflow`   |   Belief: **0.80**

> The complete ab initio workflow for predicting $T_c$ of simple metals: (1) compute $\mu_{E_F}$ from the UEG four-point vertex via vDiagMC, (2) map to the material's $r_s$ and run down to $\mu^*$ via the BTS relation, (3) obtain $\lambda$ from DFPT, (4) solve the downfolded Eliashberg equations (or use the PCF extrapolation) to predict $T_c$. All inputs are from first principles; no adjustable parameters remain.

🔗 **infer**([Downfolded BSE](#downfolded_bse), [mu from vDiagMC: Numerical Values](#mu_vdiagmc_values), [DFPT Reliable for Simple Metals](#dfpt_reliable_for_simple_metals), [UEG mu* Parameterization and Mapping](#ueg_pseudopotential_parameterization))


<a id="mu_available_for_simple_metals"></a>

#### mu* Available for Simple Metals

📌 `mu_available_for_simple_metals`   |   Belief: **0.78**

> For simple metals, the Coulomb pseudopotential $\mu^*$ can be obtained from first principles without adjustable parameters: the vDiagMC-computed $\mu_{E_F}(r_s)$ for the uniform electron gas is mapped to real materials via material-specific $r_s$ and band mass, then scaled to the Debye frequency via the BTS renormalization relation.

🔗 **support**([UEG mu* Parameterization and Mapping](#ueg_pseudopotential_parameterization), [mu from vDiagMC: Numerical Values](#mu_vdiagmc_values))

<details><summary>Reasoning</summary>

The vDiagMC results provide $\mu_{E_F}(r_s)$ for the UEG (@mu_vdiagmc_values). The parameterization procedure (@ueg_pseudopotential_parameterization) maps these to real materials using material-specific $r_s$ and band mass, justified by the weak lattice effects in simple metals (@simple_metals_weak_lattice). The BTS relation (@bts_renormalization) scales $\mu_{E_F}$ down to $\mu^*$ at the Debye frequency.

</details>


<a id="tc_al_predicted"></a>

#### Tc(Al) Ab Initio Prediction ★

📌 `tc_al_predicted`   |   Belief: **0.84**

> The ab initio EFT predicted superconducting transition temperature of aluminum (Al) is 0.96 K. The first-principles mu*(Al) = 0.13 is obtained from the vDiagMC mu_EF at r_s = 2.07 with band mass m_b = 1.05 via BTS renormalization.

🔗 **support**([Ab Initio Tc Prediction Workflow](#ab_initio_workflow))

<details><summary>Reasoning</summary>

Applying the ab initio workflow (@ab_initio_workflow) to aluminum with its material parameters (@aluminum_parameters): $r_s = 2.07$ with band mass $m_b = 1.05$ gives $\mu^* = 0.13$ from the vDiagMC parameterization via BTS renormalization. Combined with the DFPT $\lambda = 0.44$ and $\omega_{\mathrm{log}} = 320$ K, solving the Eliashberg equations yields $T_c^{\mathrm{EFT}} = 0.96$ K, in good agreement with the experimental value of 1.2 K.

</details>


<a id="tc_zn_predicted"></a>

#### Tc(Zn) Ab Initio Prediction ★

📌 `tc_zn_predicted`   |   Belief: **0.84**

> The ab initio EFT predicted superconducting transition temperature of zinc (Zn) is 0.874 K. The first-principles mu*(Zn) = 0.12 is obtained from the vDiagMC mu_EF at r_s = 2.90 with band mass m_b = 1.0 via BTS renormalization.

🔗 **support**([Ab Initio Tc Prediction Workflow](#ab_initio_workflow))

<details><summary>Reasoning</summary>

Applying the ab initio workflow (@ab_initio_workflow) to zinc with its material parameters (@zinc_parameters): $r_s = 2.90$ with band mass $m_b = 1.0$ gives $\mu^* = 0.12$ via BTS. Combined with $\lambda = 0.502$ and $\omega_{\mathrm{log}} = 111$ K from DFPT, the predicted $T_c^{\mathrm{EFT}} = 0.874$ K is in excellent agreement with the experimental value of 0.875 K.

</details>


<a id="tc_li_predicted"></a>

#### Tc(Li) Ab Initio Prediction ★

📌 `tc_li_predicted`   |   Belief: **0.82**

> The ab initio EFT predicted superconducting transition temperature of lithium (Li) (9R structure) is 0.005 K. The large mu*(Li) = 0.18 from r_s = 3.25 with band mass m_b = 1.75 almost completely cancels lambda = 0.34, pushing Tc to extremely low temperatures. The HCP structure gives Tc = 0.03 K with mu* = 0.17 and lambda = 0.37.

🔗 **support**([Ab Initio Tc Prediction Workflow](#ab_initio_workflow))

<details><summary>Reasoning</summary>

Applying the ab initio workflow (@ab_initio_workflow) to lithium (9R structure) with its material parameters (@lithium_parameters): $r_s = 3.25$ with band mass $m_b = 1.75$ gives $\mu^* = 0.18$ via BTS. Despite a moderate $\lambda = 0.34$ from DFPT, the large $\mu^*$ nearly cancels the effective pairing interaction, making the dimensionless coupling $g = \lambda - \mu^*(1+0.62\lambda)$ very small. The exponential sensitivity $T_c \propto \exp(-1/g)$ drives $T_c$ to $5 \times 10^{-3}$ K, within an order of magnitude of the experimental value $4 \times 10^{-4}$ K.

</details>


<a id="al_pressure_transition"></a>

#### Al Pressure-Tc Transition ★

📌 `al_pressure_transition`   |   Belief: **0.82**

> Under hydrostatic pressure, the ab initio framework predicts that aluminum's superconducting $T_c$ monotonically decreases, consistent with experimental data up to 6 GPa. The framework predicts that superconductivity in Al vanishes at approximately 60 GPa; at 20 GPa, $T_c$ is already suppressed below 1 mK.

🔗 **support**([Ab Initio Tc Prediction Workflow](#ab_initio_workflow))

<details><summary>Reasoning</summary>

Applying the ab initio workflow (@ab_initio_workflow) to aluminum under varying hydrostatic pressure (@aluminum_parameters): as pressure increases, $r_s$ decreases (higher electron density), modifying both $\mu^*$ and $\lambda$. The net effect is a monotonic decrease in $T_c$, accurately capturing the experimental trend from ambient to 6 GPa. Extrapolating beyond experimental data, the framework predicts SC vanishes at ~60 GPa, with $T_c < 1$ mK already at 20 GPa.

</details>


<a id="tc_mg_na_near_qpt"></a>

#### Na and Mg Near Quantum Phase Transition ★

📌 `tc_mg_na_near_qpt`   |   Belief: **0.82**

> The ab initio framework predicts that sodium and magnesium have extremely low or vanishing $T_c$: for Na ($r_s = 3.96$, $\lambda = 0.2$, $\mu^* = 0.15$), the Coulomb repulsion nearly cancels the weak electron-phonon coupling, giving $T_c^{\mathrm{EFT}} = 2 \times 10^{-13}$ K (effectively no superconductivity). For Mg ($r_s = 2.66$, $\lambda = 0.24$, $\mu^* = 0.14$), $T_c^{\mathrm{EFT}} = 5 \times 10^{-5}$ K. Both materials are near the quantum phase transition between superconducting and non-superconducting ground states, where $T_c$ varies exponentially with small parameter changes.

🔗 **support**([Ab Initio Tc Prediction Workflow](#ab_initio_workflow))

<details><summary>Reasoning</summary>

Applying the ab initio workflow (@ab_initio_workflow) to sodium (@sodium_parameters) and magnesium (@magnesium_parameters): Na has $r_s = 3.96$, yielding $\mu^* = 0.15$ which nearly cancels its weak $\lambda = 0.2$, giving $T_c^{\mathrm{EFT}} = 2 \times 10^{-13}$ K (effectively no superconductivity). Mg has $r_s = 2.66$, yielding $\mu^* = 0.14$ which nearly cancels $\lambda = 0.24$, giving $T_c^{\mathrm{EFT}} = 5 \times 10^{-5}$ K. The precursory Cooper flow formalism (@precursory_cooper_flow) shows that near the quantum phase transition ($g \to 0$), $T_c = \omega_\Lambda e^{1/g}$ is exponentially sensitive to the coupling, explaining why small parameter variations can toggle between superconducting and non-superconducting ground states.

</details>


<a id="tc_al_abinitio_outperforms_phenomenological"></a>

#### Al Ab Initio Prediction Outperforms Phenomenological

📌 `tc_al_abinitio_outperforms_phenomenological`   |   Belief: **0.83**

> For aluminum, the ab initio EFT prediction explains the observed transition temperature better than the phenomenological McMillan prediction: $T_c^{\mathrm{EFT}} = 0.96$ K is closer to $T_c^{\mathrm{exp}} = 1.2$ K than the phenomenological value $T_c \approx 1.9$ K.

🔗 **likelihood**([Tc(Al) Experimental](#tc_al_experimental), [Tc(Al) Ab Initio Prediction](#tc_al_predicted), [Tc(Al) Phenomenological Prediction](#tc_al_phenomenological), [Al Tc Comparison Valid](#tc_al_comparison_valid))

<details><summary>Reasoning</summary>

Use the SciPy-backed Gaussian model-comparison likelihood score.

</details>

<details><summary>Method</summary>

- method: gaia.std.likelihood.gaussian_model_comparison@v1
- score: log_lr=2.40222
- query: {"baseline": "phenomenological_mcmillan", "candidate": "ab_initio_eft", "criterion": "higher Gaussian predictive likelihood for observed Tc", "material": "Al", "quantity": "Tc", "unit": "K"}
- rationale: The Gaussian model-comparison log-likelihood ratio is 2.402222222222223 for observed value 1.2, candidate mean 0.96, baseline mean 1.9, and sigma 0.3.

</details>


<a id="tc_al_comparison_valid"></a>

#### Al Tc Comparison Valid

📌 `tc_al_comparison_valid`   |   Prior: 0.95   |   Belief: **0.95**

> The aluminum comparison uses the same material, the same experimental $T_c$ target, and the same absolute-error criterion for the ab initio and phenomenological predictions.


<a id="tc_zn_abinitio_outperforms_phenomenological"></a>

#### Zn Ab Initio Prediction Outperforms Phenomenological

📌 `tc_zn_abinitio_outperforms_phenomenological`   |   Belief: **0.86**

> For zinc, the ab initio EFT prediction explains the observed transition temperature better than the phenomenological McMillan prediction: $T_c^{\mathrm{EFT}} = 0.874$ K is nearly identical to $T_c^{\mathrm{exp}} = 0.875$ K, while the phenomenological value $T_c \approx 1.37$ K overestimates the measurement.

🔗 **likelihood**([Tc(Zn) Experimental](#tc_zn_experimental), [Tc(Zn) Ab Initio Prediction](#tc_zn_predicted), [Tc(Zn) Phenomenological Prediction](#tc_zn_phenomenological), [Zn Tc Comparison Valid](#tc_zn_comparison_valid))

<details><summary>Reasoning</summary>

Use the SciPy-backed Gaussian model-comparison likelihood score.

</details>

<details><summary>Method</summary>

- method: gaia.std.likelihood.gaussian_model_comparison@v1
- score: log_lr=3.0628
- query: {"baseline": "phenomenological_mcmillan", "candidate": "ab_initio_eft", "criterion": "higher Gaussian predictive likelihood for observed Tc", "material": "Zn", "quantity": "Tc", "unit": "K"}
- rationale: The Gaussian model-comparison log-likelihood ratio is 3.062800000000002 for observed value 0.875, candidate mean 0.874, baseline mean 1.37, and sigma 0.2.

</details>


<a id="tc_zn_comparison_valid"></a>

#### Zn Tc Comparison Valid

📌 `tc_zn_comparison_valid`   |   Prior: 0.97   |   Belief: **0.97**

> The zinc comparison uses the same material, the same experimental $T_c$ target, and the same absolute-error criterion for the ab initio and phenomenological predictions.


<a id="tc_li_abinitio_outperforms_phenomenological"></a>

#### Li Ab Initio Prediction Outperforms Phenomenological

📌 `tc_li_abinitio_outperforms_phenomenological`   |   Belief: **0.79**

> For lithium, the ab initio EFT prediction explains the observed ultra-low transition temperature better than the phenomenological McMillan prediction: the ab initio value is within an order of magnitude of $T_c^{\mathrm{exp}} \approx 4 \times 10^{-4}$ K, while the phenomenological value $T_c \approx 0.35$ K is too high by roughly three orders of magnitude.

🔗 **likelihood**([Tc(Li) Experimental](#tc_li_experimental), [Tc(Li) Ab Initio Prediction](#tc_li_predicted), [Tc(Li) Phenomenological Prediction](#tc_li_phenomenological), [Li Tc Comparison Valid](#tc_li_comparison_valid))

<details><summary>Reasoning</summary>

Use the SciPy-backed Gaussian model-comparison likelihood score.

</details>

<details><summary>Method</summary>

- method: gaia.std.likelihood.gaussian_model_comparison@v1
- score: log_lr=3.7261
- query: {"baseline": "phenomenological_mcmillan", "candidate": "ab_initio_eft_9R", "criterion": "higher Gaussian predictive likelihood for observed log Tc", "material": "Li", "quantity": "log10(Tc/K)"}
- rationale: The Gaussian model-comparison log-likelihood ratio is 3.7260999037054043 for observed value -3.3979400086720375, candidate mean -2.3010299956639813, baseline mean -0.4559319556497244, and sigma 1.0.

</details>


<a id="tc_li_comparison_valid"></a>

#### Li Tc Comparison Valid

📌 `tc_li_comparison_valid`   |   Prior: 0.88   |   Belief: **0.88**

> The lithium comparison uses the same 9R low-temperature structure target where applicable, the same experimental $T_c$ reference, and an order-of-magnitude error criterion appropriate for the ultra-low transition temperature regime.


## Inference Results

**BP converged:** True (2 iterations)

| Label | Type | Prior | Belief | Role |
|-------|------|-------|--------|------|
| [rpa_predicts_attractive_mu](#rpa_predicts_attractive_mu) | claim | 0.50 | 0.1276 | independent |
| [mu_vdiagmc_values](#mu_vdiagmc_values) | claim | — | 0.7478 | derived |
| [mu_available_for_simple_metals](#mu_available_for_simple_metals) | claim | — | 0.7790 | derived |
| [tc_li_abinitio_outperforms_phenomenological](#tc_li_abinitio_outperforms_phenomenological) | claim | — | 0.7904 | derived |
| [ab_initio_workflow](#ab_initio_workflow) | claim | — | 0.8012 | derived |
| [al_pressure_transition](#al_pressure_transition) | claim | — | 0.8199 | derived |
| [tc_li_predicted](#tc_li_predicted) | claim | — | 0.8199 | derived |
| [tc_mg_na_near_qpt](#tc_mg_na_near_qpt) | claim | — | 0.8199 | derived |
| [tc_al_abinitio_outperforms_phenomenological](#tc_al_abinitio_outperforms_phenomenological) | claim | — | 0.8272 | derived |
| [tc_al_predicted](#tc_al_predicted) | claim | — | 0.8398 | derived |
| [tc_zn_predicted](#tc_zn_predicted) | claim | — | 0.8398 | derived |
| [homotopic_expansion](#homotopic_expansion) | claim | 0.88 | 0.8429 | independent |
| [tc_li_experimental](#tc_li_experimental) | claim | 0.85 | 0.8500 | independent |
| [ueg_pseudopotential_parameterization](#ueg_pseudopotential_parameterization) | claim | 0.85 | 0.8500 | independent |
| [gamma3_approximation](#gamma3_approximation) | claim | — | 0.8596 | derived |
| [tc_zn_abinitio_outperforms_phenomenological](#tc_zn_abinitio_outperforms_phenomenological) | claim | — | 0.8648 | derived |
| [vdiagmc_method](#vdiagmc_method) | claim | 0.90 | 0.8691 | independent |
| [dfpt_reliable_for_simple_metals](#dfpt_reliable_for_simple_metals) | claim | — | 0.8734 | derived |
| [gamma3_vdiagmc](#gamma3_vdiagmc) | claim | 0.88 | 0.8800 | independent |
| [tc_li_comparison_valid](#tc_li_comparison_valid) | claim | 0.88 | 0.8800 | independent |
| [eft_vertex_matches_dfpt](#eft_vertex_matches_dfpt) | claim | — | 0.8848 | derived |
| [gamma3_interpolation_test_valid](#gamma3_interpolation_test_valid) | claim | 0.90 | 0.9000 | independent |
| [dfpt_eph_ansatz](#dfpt_eph_ansatz) | claim | 0.90 | 0.9000 | background |
| [precursory_cooper_flow](#precursory_cooper_flow) | claim | 0.90 | 0.9000 | background |
| [simple_metals_weak_lattice](#simple_metals_weak_lattice) | claim | 0.90 | 0.9000 | background |
| [downfolding_validity_limits](#downfolding_validity_limits) | claim | 0.92 | 0.9200 | orphaned |
| [quasiparticle_mass_near_unity](#quasiparticle_mass_near_unity) | claim | 0.92 | 0.9200 | independent |
| [cross_term_suppressed](#cross_term_suppressed) | claim | 0.90 | 0.9261 | independent |
| [gamma3_evidence_independent](#gamma3_evidence_independent) | claim | 0.93 | 0.9300 | independent |
| [electron_phonon_action](#electron_phonon_action) | claim | 0.95 | 0.9500 | background |
| [me_downfolding_is_phenomenological](#me_downfolding_is_phenomenological) | claim | 0.95 | 0.9500 | orphaned |
| [phenomenological_me_theory](#phenomenological_me_theory) | claim | 0.95 | 0.9500 | orphaned |
| [tc_al_comparison_valid](#tc_al_comparison_valid) | claim | 0.95 | 0.9500 | independent |
| [ueg_vertex_challenge](#ueg_vertex_challenge) | claim | 0.95 | 0.9500 | background |
| [adiabatic_approx](#adiabatic_approx) | claim | 0.95 | 0.9558 | independent |
| [lambda_microscopic_definition](#lambda_microscopic_definition) | claim | — | 0.9615 | derived |
| [ma_pseudopotential_justified](#ma_pseudopotential_justified) | claim | — | 0.9629 | derived |
| [downfolded_bse](#downfolded_bse) | claim | — | 0.9634 | derived |
| [eft_eph_vertex](#eft_eph_vertex) | claim | — | 0.9654 | derived |
| [downfolded_me_equation](#downfolded_me_equation) | claim | — | 0.9663 | derived |
| [me_framework](#me_framework) | claim | — | 0.9696 | derived |
| [tc_zn_comparison_valid](#tc_zn_comparison_valid) | claim | 0.97 | 0.9700 | independent |
| [mu_microscopic_definition](#mu_microscopic_definition) | claim | — | 0.9764 | derived |
| [ward_identity](#ward_identity) | claim | 0.98 | 0.9800 | independent |
| [bse_kernel_decomposition](#bse_kernel_decomposition) | claim | — | 0.9824 | derived |
| [dfpt_computes_lambda](#dfpt_computes_lambda) | claim | 0.92 | 0.9859 | independent |
| [tc_al_experimental](#tc_al_experimental) | claim | 0.99 | 0.9900 | independent |
| [tc_zn_experimental](#tc_zn_experimental) | claim | 0.99 | 0.9900 | independent |
| [mu_star_phenomenological](#mu_star_phenomenological) | claim | 0.95 | 0.9912 | independent |
| [downfolded_bse_toy_model](#downfolded_bse_toy_model) | claim | — | 0.9944 | derived |
| [full_bse_toy_model](#full_bse_toy_model) | claim | — | 0.9944 | derived |
| [tc_al_phenomenological](#tc_al_phenomenological) | claim | 0.95 | 0.9975 | derived |
| [tc_li_phenomenological](#tc_li_phenomenological) | claim | 0.95 | 0.9975 | derived |
| [tc_zn_phenomenological](#tc_zn_phenomenological) | claim | 0.95 | 0.9975 | derived |
| [bts_renormalization](#bts_renormalization) | claim | 0.95 | 0.9981 | independent |
| [mu_scale_independence](#mu_scale_independence) | claim | — | 0.9982 | derived |
| [rpa_vs_vdiagmc](#rpa_vs_vdiagmc) | claim | 0.95 | 0.9993 | structural |
| [bts_microscopic_equivalence](#bts_microscopic_equivalence) | claim | 0.98 | 0.9999 | structural |
