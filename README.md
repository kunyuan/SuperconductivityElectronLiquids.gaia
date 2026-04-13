# Superconductivity in Electron Liquids

> **Original work:** Cai, X., Wang, T., Zhang, S., Zhang, T., Millis, A., Svistunov, B. V., Prokof'ev, N. V., & Chen, K. "Superconductivity in Electron Liquids: Precision Many-Body Treatment of Coulomb Interaction." [arXiv:2512.19382v2](https://arxiv.org/abs/2512.19382) (2025).

[![Gaia Package](https://img.shields.io/badge/Gaia-knowledge--package-blue)](https://github.com/SiliconEinstein/gaia-registry)

> [!NOTE]
> This README is an AI-generated analysis based on a [Gaia](https://github.com/SiliconEinstein/Gaia) reasoning graph formalization of the original work. Belief values reflect the graph's probabilistic assessment of each claim's support, not the original authors' confidence. See [detailed-reasoning.md](docs/detailed-reasoning.md) for per-module reasoning graphs.

## Summary

For decades, predicting the superconducting transition temperature $T_c$ of conventional metals from first principles has been blocked by the inability to compute the Coulomb pseudopotential $\mu^\ast$ -- the parameter encoding how much Coulomb repulsion survives in the Cooper pairing channel. This paper eliminates the guesswork by computing $\mu^\ast$ from the four-point electron vertex of the uniform electron gas via variational diagrammatic Monte Carlo (vDiagMC), deriving a controlled downfolded Bethe-Salpeter equation with microscopically defined $\mu^\ast$ and $\lambda$, and combining these with DFPT phonon calculations to predict $T_c$ with no adjustable parameters. The results are striking: $T_c = 0.874$ K for zinc (experiment: 0.875 K -- a 0.1% match), $T_c = 0.96$ K for aluminum (experiment: 1.2 K), and $T_c = 5 \times 10^{-3}$ K for lithium (experiment: $4 \times 10^{-4}$ K) -- compared to the standard McMillan formula which overestimates lithium by three orders of magnitude. The framework also predicts pressure-induced destruction of superconductivity in aluminum and identifies sodium and magnesium as sitting near a quantum phase transition.

## Reasoning Graph

> [!TIP]
> **Reasoning graph information gain: `3.8 bits`**
>
> Total mutual information between leaf premises and exported conclusions -- measures how much the reasoning structure reduces uncertainty about the results.

```mermaid
---
config:
  flowchart:
    rankSpacing: 80
    nodeSpacing: 30
---
graph TB
    adiabatic_approx["Adiabatic Approximation\n(0.95 → 0.96)"]:::premise
    tc_al_experimental["Tc(Al) Experimental\n(0.99 → 0.99)"]:::premise
    tc_li_experimental["Tc(Li) Experimental\n(0.85 → 0.25)"]:::premise
    tc_zn_experimental["Tc(Zn) Experimental\n(0.99 → 0.99)"]:::premise
    tc_al_phenomenological["Tc(Al) Phenomenological Prediction\n(0.35 → 0.99)"]:::premise
    tc_li_phenomenological["Tc(Li) Phenomenological Prediction\n(0.10 → 0.21)"]:::premise
    tc_zn_phenomenological["Tc(Zn) Phenomenological Prediction\n(0.35 → 0.99)"]:::premise
    cross_term_suppressed["Cross-Channel Terms Suppressed\n(0.90 → 0.93)"]:::premise
    downfolded_bse["★ Downfolded BSE\n(0.50 → 0.98)"]:::exported
    vdiagmc_method["vDiagMC Method\n(0.90 → 0.90)"]:::premise
    homotopic_expansion["Homotopic Expansion\n(0.88 → 0.89)"]:::premise
    mu_vdiagmc_values["★ mu from vDiagMC: Numerical Values\n(0.50 → 0.72)"]:::exported
    ward_identity["Ward Identity at q->0\n(0.98 → 0.99)"]:::premise
    gamma3_vdiagmc["vDiagMC Computation of Gamma_3\n(0.88 → 0.99)"]:::premise
    quasiparticle_mass_near_unity["Quasiparticle Mass Near Unity\n(0.92 → 0.93)"]:::premise
    dfpt_reliable_for_simple_metals["★ DFPT Reliable for Simple Metals\n(0.50 → 0.97)"]:::exported
    ueg_pseudopotential_parameterization["UEG mu#ast; Parameterization and Mapping\n(0.85 → 0.90)"]:::premise
    ab_initio_workflow["★ Ab Initio Tc Prediction Workflow\n(0.50 → 1.00)"]:::exported
    tc_al_predicted["★ Tc(Al) Ab Initio Prediction\n(0.50 → 0.99)"]:::exported
    tc_zn_predicted["★ Tc(Zn) Ab Initio Prediction\n(0.50 → 0.99)"]:::exported
    tc_li_predicted["★ Tc(Li) Ab Initio Prediction\n(0.50 → 0.25)"]:::exported
    al_pressure_transition["★ Al Pressure-Tc Transition\n(0.50 → 0.80)"]:::exported
    tc_mg_na_near_qpt["★ Na and Mg Near Quantum Phase Transition\n(0.50 → 0.80)"]:::exported
    rpa_predicts_attractive_mu["RPA Predicts Attractive mu#ast;\n(0.50 → 0.14)"]:::premise
    rpa_vs_vdiagmc["rpa_vs_vdiagmc\n(0.95 → 1.00)"]:::premise
    strat_0(["infer\n0.60 bits"]):::weak
    ab_initio_workflow --> strat_0
    strat_0 --> al_pressure_transition
    strat_1(["infer\n0.62 bits"]):::weak
    ab_initio_workflow --> strat_1
    tc_al_experimental --> strat_1
    tc_al_phenomenological --> strat_1
    strat_1 --> tc_al_predicted
    strat_2(["infer\n0.64 bits"]):::weak
    ab_initio_workflow --> strat_2
    tc_li_experimental --> strat_2
    tc_li_phenomenological --> strat_2
    strat_2 --> tc_li_predicted
    strat_3(["infer\n0.60 bits"]):::weak
    ab_initio_workflow --> strat_3
    strat_3 --> tc_mg_na_near_qpt
    strat_4(["infer\n0.62 bits"]):::weak
    ab_initio_workflow --> strat_4
    tc_zn_experimental --> strat_4
    tc_zn_phenomenological --> strat_4
    strat_4 --> tc_zn_predicted
    strat_5(["infer\n0.07 bits"]):::weak
    adiabatic_approx --> strat_5
    cross_term_suppressed --> strat_5
    strat_5 --> downfolded_bse
    strat_6(["infer\n0.00 bits"]):::weak
    dfpt_reliable_for_simple_metals --> strat_6
    downfolded_bse --> strat_6
    mu_vdiagmc_values --> strat_6
    ueg_pseudopotential_parameterization --> strat_6
    strat_6 --> ab_initio_workflow
    strat_7(["infer\n0.08 bits"]):::weak
    downfolded_bse --> strat_7
    gamma3_vdiagmc --> strat_7
    quasiparticle_mass_near_unity --> strat_7
    ward_identity --> strat_7
    strat_7 --> dfpt_reliable_for_simple_metals
    strat_8(["infer\n0.55 bits"]):::weak
    homotopic_expansion --> strat_8
    vdiagmc_method --> strat_8
    strat_8 --> mu_vdiagmc_values
    oper_0{{"⊗"}}:::contra
    rpa_predicts_attractive_mu --- oper_0
    mu_vdiagmc_values --- oper_0
    oper_0 --- rpa_vs_vdiagmc

    classDef premise fill:#ddeeff,stroke:#4488bb,color:#333
    classDef exported fill:#d4edda,stroke:#28a745,stroke-width:2px,color:#333
    classDef weak fill:#fff9c4,stroke:#f9a825,stroke-dasharray: 5 5,color:#333
    classDef contra fill:#ffebee,stroke:#c62828,color:#333
```

> [!NOTE]
> **[Per-module reasoning graphs with full claim details](docs/detailed-reasoning.md)**

## Reasoning Structure

Evidence assessment for each exported conclusion, ordered by the paper's argumentative arc: theoretical foundations, computational methods, validation, and predictions.

### The full Bethe-Salpeter equation reduces to a solvable frequency-only form (belief: 0.98)

The central theoretical contribution of the paper is a controlled downfolding of the full momentum-frequency Bethe-Salpeter equation (BSE) into a one-dimensional integral equation in Matsubara frequency. The key physics is energy-scale separation: the pair propagator $G_{k\omega}G_{-k,-\omega}$ is exactly decomposed into a low-energy coherent BCS piece $\Pi_{\mathrm{BCS}}$ (which carries the Cooper logarithm driving the pairing instability) and a high-energy incoherent remainder $\phi_{k\omega}$. After momentum integration over the coherent part, the kernel separates into a phonon-mediated attraction $\lambda_{\omega\omega'}$ and a Coulomb pseudopotential $\mu_{\omega_c}$, both now carrying precise microscopic definitions in terms of the electronic four-point vertex $\tilde\Gamma^e$. Corrections to the downfolded equation are bounded by three small parameters: $\omega_D/E_F$ (adiabatic ratio, ~0.005 for simple metals), $\omega_c^2/\omega_p^2$ (cross-channel mixing, ~1%), and $T/\omega_c$. This is a significant advance over the traditional Migdal-Eliashberg framework, where $\mu^\ast$ and $\lambda$ were phenomenologically defined -- here both emerge from first principles with controlled error bounds. The downfolding is validated numerically: for a toy model with aluminum-like parameters, the full and downfolded BSE give $T_c$ values differing by only 0.2%.

**Evidence chains:**
- Cross-channel term suppression (belief 0.93) -- the $O(\omega_c^2/\omega_p^2) \leq 1\%$ bound rests on a plasmon-pole model for 3D metals; it could fail in low-dimensional systems or near soft collective modes
- Adiabatic approximation (belief 0.96) -- well-established for simple metals ($\omega_D/E_F \sim 0.005$), but not tested at higher $r_s$ where the ratio worsens
- Toy-model validation covers only one density ($r_s = 1.92$); no test at $r_s \sim 4$ where the adiabatic ratio is less favorable

![Fig. 5 | Comparison between the precursory Cooper flow solutions of the full and downfolded BSE, demonstrating 0.2% agreement in $T_c$.](artifacts/images/8_1.jpg)

**Verdict:** With directed factor inference eliminating the fan-out penalty, the belief (0.98) now reflects the strength of the derivation. Both the cross-channel suppression (0.93) and adiabatic approximation (0.96) hold up well, and the 0.2% numerical agreement at aluminum-like parameters is compelling. The remaining uncertainty is the method's validity at higher $r_s$.

---

### Controlled many-body calculations reveal the Coulomb pseudopotential is far larger than RPA predicts (belief: 0.72)

The paper's central computational result is the first controlled evaluation of the Coulomb pseudopotential $\mu_{E_F}$ from the four-point electron vertex of the uniform electron gas (UEG). Using variational diagrammatic Monte Carlo (vDiagMC) -- a method that stochastically samples Feynman diagrams with bold-line (self-consistent) propagators and extrapolates to infinite order -- the authors find $\mu_{E_F}(r_s) \approx 0.27\, r_s$, positive and monotonically increasing throughout the metallic density range. This dramatically exceeds all RPA-based predictions: at $r_s = 5$, the vDiagMC value is three times larger than the dynamic RPA result, and the RPA prediction of attractive $\mu^\ast$ (which would imply purely electronic superconductivity) is firmly ruled out. The convergence of the diagrammatic series is enabled by a homotopic expansion that continuously deforms the bare Coulomb interaction to incorporate partial screening at each perturbative order, curing logarithmic divergences and allowing convergence at modest diagram orders ($n \lesssim 7$). After BTS renormalization to the Debye scale, the resulting $\mu^\ast \approx 0.12\text{-}0.18$ falls within the empirical range but is now derived from first principles with few-percent error bars.

**Evidence chains:**
- vDiagMC method (belief 0.90) -- systematically controlled via bold-line resummation and infinite-order extrapolation, but no independent cross-validation by an alternative many-body method (e.g., auxiliary-field QMC)
- Homotopic expansion (belief 0.89) -- the log-divergence cure is rigorous, but the conformal-map-based resummation assumes analyticity properties not proven for the UEG four-point vertex at metallic densities
- The formal contradiction with RPA ($\mu^\ast < 0$ at $r_s > 2$) anchors the contradiction node (prior 0.95, belief 1.00), pulling down the RPA claim to belief 0.14

| $r_s$ | 1 | 2 | 3 | 4 | 5 | 6 |
|--------|---------|---------|---------|----------|----------|--------|
| $\mu_{0.1\,E_F}$ | 0.172(4)| 0.238(4)| 0.278(6)| 0.306(15)| 0.328(12)| 0.35(3)|
| $\mu_{E_F}$ | 0.28(1) | 0.53(2) | 0.77(5) | 1.0(2) | 1.3(2) | 1.8(8) |

![Fig. 4 | Dimensionless bare Coulomb pseudopotential $\mu_{E_F}$ vs $r_s$ from vDiagMC, compared with static RPA, Morel-Anderson, and dynamic RPA predictions.](artifacts/images/8_0.jpg)

**Verdict:** The belief (0.72) is pulled down by the RPA contradiction -- since the contradiction helper has prior 0.95, it forces competition between vDiagMC and RPA, and the remaining uncertainty reflects that only one controlled method has been used. Independent verification by an alternative many-body method would sharpen confidence further.

---

### DFPT electron-phonon coupling is reliable for simple metals because vertex corrections cancel (belief: 0.97)

A key question for the ab initio workflow is whether the standard DFPT calculation of the electron-phonon coupling $\lambda$ can be trusted when Coulomb correlations are properly included. The paper answers affirmatively for simple metals through a three-step argument. First, the EFT expression for the physical e-ph vertex factorizes as $g(k,q) = g^{(0)} \cdot (z^e / \epsilon_q) \cdot \Gamma_3^e(k,q)$, where $z^e$ is the quasiparticle weight and $\Gamma_3^e$ is the three-point vertex correction. Second, the Ward identity fixes $\Gamma_3^e = m^\ast/m$ at $q \to 0$ (an exact consequence of charge conservation), and vDiagMC calculations at finite $q$ show only smooth, modest 10-20% corrections. Third, because $m^\ast/m \approx 1$ for simple metals at metallic densities (deviations below 5-10%), the product $z^e \cdot \Gamma_3^e \approx (m/m^\ast)(m^\ast/m) = 1$ -- the quasiparticle renormalization and vertex correction cancel to few-percent accuracy. This means the EFT vertex reduces to the DFPT Kohn-Sham expression, and since the quasiparticle density of states $N_F^\ast \approx N_F^{(0)}$, the resulting $\lambda_{\mathrm{EFT}} \approx \lambda_{\mathrm{DFPT}}$. This cancellation is specific to simple metals and does not extend to strongly correlated systems.

**Evidence chains:**
- Ward identity at $q \to 0$ (belief 0.99) -- exact QFT result from charge conservation, essentially bulletproof
- vDiagMC computation of $\Gamma_3^e$ at finite $q$ (belief 0.99) -- well-controlled but only verified for the homogeneous electron gas, not for real crystal potentials
- Quasiparticle mass near unity (belief 0.93) -- high-precision QMC/DiagMC confirms $m^\ast/m < 1\%$ deviation for $r_s \leq 5$, but the cancellation is verified only for the UEG
- Downfolded BSE (belief 0.98) enters as a premise with high confidence

![Fig. 8 | Comparison between the angle-resolved e-ph vertex correction from vDiagMC (points) and DFPT (lines) for different $r_s$ values.](artifacts/images/12_0.jpg)

**Verdict:** The physics of the cancellation is well-motivated and the argument is internally consistent. The main risk is that crystal-field effects in real materials could break the cancellation that works so cleanly in the homogeneous electron gas.

---

### A complete parameter-free workflow predicts $T_c$ from first principles (belief: 1.00)

The paper's culminating result is a complete ab initio workflow for predicting $T_c$ of simple metals with no adjustable parameters: (1) compute $\mu_{E_F}$ from the UEG four-point vertex via vDiagMC, (2) map to the material's $r_s$ and run down to $\mu^\ast$ via the BTS renormalization relation, (3) obtain $\lambda$ from DFPT, and (4) solve the downfolded Eliashberg equations (or use precursory Cooper flow extrapolation) to predict $T_c$. Each component is microscopically grounded: $\mu^\ast$ comes from controlled many-body calculations rather than phenomenological fitting, $\lambda$ comes from DFPT validated against the EFT vertex, and the Eliashberg equations emerge from the controlled downfolding with bounded corrections. The workflow is particularly powerful for low-$T_c$ superconductors near quantum phase transitions, where the exponential sensitivity $T_c \propto \exp(-1/g)$ amplifies small errors in $\mu^\ast$ into orders-of-magnitude discrepancies -- precisely the regime where phenomenological approaches fail most catastrophically.

**Evidence chain:** This conclusion sits at the apex of the graph and requires all four components to be valid simultaneously. The composite strategy assigns $P(T_c\text{ workflow} \mid \text{all 4 components true}) = 0.92$. With directed factor inference, all upstream components now have strong beliefs:
- Downfolded BSE (belief 0.98) -- the theoretical foundation
- $\mu^\ast$ from vDiagMC (belief 0.72) -- the key new input (weakest link, pulled by RPA contradiction)
- DFPT reliability (belief 0.97) -- the $\lambda$ computation
- UEG parameterization (belief 0.90) -- the material mapping

The workflow conclusion reaches belief 1.00 because all components are well-supported and the downstream material predictions for aluminum and zinc are strongly validated by experiment.

![Fig. 9 | Proposed ab initio framework for electron-phonon superconductivity beyond the weak correlation limit.](artifacts/images/13_0.jpg)

**Verdict:** High confidence. The workflow is validated end-to-end by the material-specific predictions below. The main risk is that the method may not generalize beyond simple metals where the UEG approximation holds.

---

### Aluminum's superconductivity is destroyed by pressure above 60 GPa (belief: 0.80)

Applying the ab initio workflow to aluminum under hydrostatic pressure, the framework predicts a monotonic decrease in $T_c$ as pressure increases: higher pressure reduces $r_s$ (compresses the electron gas), which modifies both $\mu^\ast$ and $\lambda$ in a way that weakens the net pairing interaction. The prediction agrees quantitatively with the available experimental data from Levy et al. and Gubser et al. up to 6 GPa. Extrapolating beyond, the framework predicts $T_c$ drops below 1 mK at 20 GPa and superconductivity vanishes entirely at approximately 60 GPa. This represents a pressure-induced quantum phase transition from a superconducting to a non-superconducting ground state -- a testable prediction that diamond anvil cell experiments at 20-60 GPa with sub-millikelvin sensitivity could confirm.

**Evidence chains:**
- Ab initio workflow (belief 1.00) is the sole upstream dependency
- The conditional probability is 0.80 ("extrapolation to high pressure") -- lower than for ambient-pressure predictions because no experimental data constrain the high-pressure regime, and structural phase transitions could intervene

![Fig. 10 | Pressure dependence of the superconducting critical temperature in aluminum, with EFT predictions compared to experimental data.](artifacts/images/14_0.jpg)

**Verdict:** The prediction agrees with available data (up to 6 GPa), lending credibility to the trend. However, the 60 GPa extinction is pure extrapolation -- no experimental data constrain it, and structural phase transitions could intervene at extreme pressures.

---

### Sodium and magnesium sit near a superconducting quantum phase transition (belief: 0.80)

The framework predicts effectively zero $T_c$ for sodium ($2 \times 10^{-13}$ K) and magnesium ($5 \times 10^{-5}$ K), placing both metals near the quantum phase transition between superconducting and non-superconducting ground states. The physics is straightforward: for Na ($r_s = 3.96$, $\lambda = 0.2$, $\mu^\ast = 0.15$), the Coulomb repulsion nearly cancels the weak electron-phonon coupling; for Mg ($r_s = 2.66$, $\lambda = 0.24$, $\mu^\ast = 0.14$), the situation is similar but less extreme. In both cases the effective coupling $g = \lambda - \mu^\ast(1 + 0.62\lambda)$ is nearly zero, and the exponential sensitivity $T_c \propto e^{1/g}$ drives the transition temperature to unobservably low values. This near-cancellation has long been suspected on phenomenological grounds but has never before been quantified from first principles. If confirmed, Na and Mg would offer a unique platform to study quantum critical scaling in the superconducting channel below 10 K -- though confirmation would require sub-nanokelvin transport measurements at the frontier of current cryogenic capabilities.

**Evidence chains:**
- Ab initio workflow (belief 1.00) is the sole upstream dependency
- The conditional probability is 0.80 ("near quantum critical point") -- both predictions are purely theoretical with no experimental validation
- The exponential sensitivity means even small errors in $\mu^\ast$ or $\lambda$ translate into orders-of-magnitude changes in $T_c$

![Fig. 11 | Effective BCS coupling strength for simple metals, showing Al, Zn, Li, Na, Mg on the $\lambda$-$\mu^\ast$ plane.](artifacts/images/15_0.jpg)

**Verdict:** Physically reasonable -- the near-cancellation is a natural consequence of the first-principles $\mu^\ast$ values. But the predictions are entirely theoretical, and the exponential sensitivity makes them inherently fragile near the quantum critical point.

---

### Lithium's anomalously low $T_c$ is explained by a large first-principles $\mu^\ast$ (belief: 0.25)

Lithium has been the most embarrassing failure of conventional superconductivity theory: the standard McMillan formula with $\mu^\ast = 0.1$ predicts $T_c \approx 0.35$ K, overshooting the experimental value $T_c^{\mathrm{exp}} \approx 4 \times 10^{-4}$ K by three orders of magnitude. The ab initio framework resolves this by revealing that lithium's first-principles $\mu^\ast = 0.18$ (from $r_s = 3.25$, $m_b = 1.75$) is nearly twice the standard phenomenological guess. With $\lambda = 0.34$ from DFPT, the effective coupling $g = \lambda - \mu^\ast(1 + 0.62\lambda) \approx 0.12$ is very small, and the exponential sensitivity $T_c \propto \exp(-1/g)$ amplifies the difference between $\mu^\ast = 0.10$ and $\mu^\ast = 0.18$ from a factor of 1.8 into a three-orders-of-magnitude shift in $T_c$. The predicted $T_c^{\mathrm{EFT}} = 5 \times 10^{-3}$ K for the 9R structure (or 0.03 K for HCP with $\mu^\ast = 0.17$) remains about an order of magnitude above experiment, but this residual discrepancy likely reflects the controversial crystal structure of lithium at sub-kelvin temperatures rather than a failure of the electronic theory.

**Evidence chains:**
- Ab initio workflow (belief 1.00) provides the theoretical framework
- Experimental $T_c$(Li) (belief 0.25) -- the order-of-magnitude gap between the EFT prediction ($5 \times 10^{-3}$ K) and experiment ($4 \times 10^{-4}$ K) pulls down beliefs for all three alternatives in the compare
- Phenomenological prediction with $\mu^\ast = 0.1$ (belief 0.21) -- predicts 0.35 K, three orders of magnitude too high

**Verdict:** The low belief (0.25) reflects the graph's honest assessment: while the ab initio prediction ($5 \times 10^{-3}$ K) is a dramatic improvement over McMillan ($0.35$ K), it still overshoots experiment by an order of magnitude. The compare strategy correctly penalizes all three alternatives (EFT, phenomenological, and experimental) because none perfectly reconcile the data. The remaining discrepancy is plausibly attributed to lithium's uncertain low-temperature crystal structure and the sensitivity of $T_c$ to small errors in $\mu^\ast$ near the quantum phase boundary.

---

### Zinc's $T_c$ is predicted to 0.1% accuracy without adjustable parameters (belief: 0.99)

The most striking quantitative success of the framework is the prediction for zinc: $T_c^{\mathrm{EFT}} = 0.874$ K vs. $T_c^{\mathrm{exp}} = 0.875$ K -- agreement to within 0.1%. Zinc has $r_s = 2.90$ and band mass $m_b = 1.0$, giving $\mu^\ast = 0.12$ from the vDiagMC parameterization via BTS renormalization. Combined with $\lambda = 0.502$ from DFPT and $\omega_{\mathrm{log}} = 111$ K, solving the Eliashberg equations yields the near-exact match with experiment. By contrast, the phenomenological prediction using $\mu^\ast = 0.1$ gives 1.37 K, overestimating by 57%. The near-exact agreement is partly fortunate given the method's few-percent uncertainties in both $\mu^\ast$ and $\lambda$, but it demonstrates that the workflow produces results in the right ballpark without any parameter tuning -- precisely the regime where a correct $\mu^\ast$ matters most.

**Evidence chains:**
- Ab initio workflow (belief 1.00) provides the theoretical framework
- Experimental $T_c$(Zn) (belief 0.99) -- well-established, textbook measurement
- Phenomenological prediction with $\mu^\ast = 0.1$ (belief 0.99) -- the abductive structure strongly validates both the ab initio and phenomenological routes, with the 0.1% match dominating

![Fig. 11 | Effective BCS coupling strength for simple metals. E-ph couplings from DFPT; pseudopotentials from vDiagMC.](artifacts/images/15_0.jpg)

**Verdict:** This is the most impressive prediction in the paper. While the 0.1% match is partly fortuitous, the systematic improvement over phenomenological predictions is unambiguous.

---

### Aluminum's $T_c$ is predicted within 20% from first principles (belief: 0.99)

For aluminum ($r_s = 2.07$, $m_b = 1.05$), the ab initio workflow gives $\mu^\ast = 0.13$ and $\lambda = 0.44$ from DFPT, yielding $T_c^{\mathrm{EFT}} = 0.96$ K compared with the experimental value $T_c^{\mathrm{exp}} = 1.2$ K -- a 20% underestimate. The phenomenological prediction using $\mu^\ast = 0.1$ gives 1.9 K, overestimating by 58%. Aluminum is a workhorse of superconducting electronics (transition-edge sensors, qubits), and the long-standing factor-of-two discrepancy between theory and experiment has been a practical obstacle. The ab initio $\mu^\ast = 0.13$ is modestly above the standard guess of 0.1, correctly reducing $T_c$ toward the experimental value. The remaining 20% underestimate is consistent with the few-percent uncertainties in both $\mu^\ast$ and $\lambda$, and the abductive reasoning structure correctly favors the ab initio explanation over the phenomenological one.

**Evidence chains:**
- Ab initio workflow (belief 1.00) provides the theoretical framework
- Experimental $T_c$(Al) (belief 0.99) -- well-established, textbook measurement
- Phenomenological prediction with $\mu^\ast = 0.1$ (belief 0.99) -- the 20% agreement between EFT and experiment validates both approaches
- The weakest link in the material-specific chain is the UEG-to-Al mapping via the band mass correction ($m_b = 1.05$), which is small for Al but unvalidated independently

![Fig. 10 | Pressure dependence of the superconducting critical temperature in aluminum. EFT results (squares) compared with experimental data.](artifacts/images/14_0.jpg)

**Verdict:** Credible. The 20% underestimate is well within the method's expected uncertainty, and the improvement over the phenomenological prediction is clear.

---

## Key Findings

| Label | Content | Prior | Belief |
|-------|---------|-------|--------|
| ab_initio_workflow | Complete parameter-free workflow: vDiagMC $\mu^\ast$ + DFPT $\lambda$ + downfolded Eliashberg equations | 0.50 | 1.00 |
| tc_al_predicted | $T_c^{\mathrm{EFT}}(\mathrm{Al}) = 0.96$ K vs $T_c^{\mathrm{exp}} = 1.2$ K | 0.50 | 0.99 |
| tc_zn_predicted | $T_c^{\mathrm{EFT}}(\mathrm{Zn}) = 0.874$ K vs $T_c^{\mathrm{exp}} = 0.875$ K | 0.50 | 0.99 |
| tc_li_predicted | $T_c^{\mathrm{EFT}}(\mathrm{Li}) = 5 \times 10^{-3}$ K vs $T_c^{\mathrm{exp}} \approx 4 \times 10^{-4}$ K | 0.50 | 0.25 |
| al_pressure_transition | Al $T_c$ monotonically decreases under pressure, vanishing at ~60 GPa | 0.50 | 0.80 |
| tc_mg_na_near_qpt | Na and Mg near quantum phase transition, effectively non-superconducting | 0.50 | 0.80 |
| dfpt_reliable_for_simple_metals | DFPT $\lambda$ reliable for simple metals: vertex corrections cancel at $m^\ast/m \approx 1$ | 0.50 | 0.97 |
| mu_vdiagmc_values | vDiagMC $\mu_{E_F} \approx 0.27\, r_s$, dramatically exceeding RPA predictions | 0.50 | 0.72 |
| downfolded_bse | Frequency-only downfolded BSE with microscopic $\lambda$ and $\mu_{\omega_c}$ | 0.50 | 0.98 |

<details open>
<summary><strong>Weak Points</strong></summary>

**The lithium prediction reveals the sharpest tension in the graph.** With directed factor inference, most nodes now have high beliefs, but $T_c$(Li) (belief 0.25) stands out: the ab initio prediction overshoots experiment by an order of magnitude, and the compare strategy correctly penalizes this mismatch. The exponential sensitivity $T_c \propto \exp(-1/g)$ means even small errors in $\mu^\ast$ translate into order-of-magnitude discrepancies near the quantum phase boundary.

**The UEG-to-material mapping introduces unquantified lattice corrections.** The intermediate node `mu_available_for_simple_metals` (belief 0.62) aggregates the vDiagMC $\mu_{E_F}(r_s)$ values with the material-specific $r_s$ and band mass correction. While simple metals are nearly-free-electron-like, the band mass correction for lithium ($m_b = 1.75$) is substantial and not independently validated. This is the weakest link in the material-specific chain.

**The RPA contradiction limits the vDiagMC belief.** The $\mu^\ast$ from vDiagMC (belief 0.72) is the weakest exported node, pulled down by the contradiction with RPA predictions. While the contradiction is physically correct (RPA predicts attractive $\mu^\ast$ which vDiagMC rules out), the factor graph encodes this as uncertainty in the vDiagMC values themselves. Independent verification by an alternative controlled many-body method would resolve this tension.

**The homotopic expansion relies on unverified analyticity assumptions.** The homotopic transformation (belief 0.89, from prior 0.88) reorganizes the diagrammatic series by continuously deforming the bare Coulomb interaction. While the log-divergence cure is rigorous, the conformal-map-based resummation relies on analyticity properties that are assumed rather than proven for the UEG four-point vertex at metallic densities.

</details>

<details>
<summary><strong>Evidence Gaps</strong></summary>

**Experimental gaps:**
- No experimental $T_c$ measurement exists for Na or Mg at the predicted sub-microkelvin scales. Confirming these metals' proximity to the quantum phase transition would require sub-nanokelvin transport measurements -- technically at the frontier of current cryogenic capabilities. These predictions directly affect the conclusions `tc_mg_na_near_qpt` (belief 0.77).
- No high-pressure $T_c$ data for aluminum beyond 6 GPa. The prediction of superconductivity vanishing at 60 GPa (`al_pressure_transition`, belief 0.77) is pure extrapolation. Diamond anvil cell experiments at 20-60 GPa with sub-millikelvin sensitivity would test this prediction.

**Computational gaps:**
- No independent verification of the vDiagMC $\mu_{E_F}$ values by an alternative controlled many-body method (e.g., auxiliary-field QMC, coupled-cluster theory, or full configuration interaction QMC). The $\mu^\ast$ values (`mu_vdiagmc_values`, belief 0.55) rest entirely on one method. Cross-validation would sharpen confidence in all downstream predictions.
- The downfolding validation was performed at only one electron density ($r_s = 1.92$, aluminum-like). Testing at $r_s \sim 4$ (sodium-relevant) where the adiabatic ratio is less favorable would strengthen confidence in `downfolded_bse` (belief 0.33) and propagate upstream.

**Theoretical gaps:**
- The EFT vertex-DFPT equivalence is established for the homogeneous electron gas, not for real materials with crystal-field splitting, spin-orbit coupling, or multi-band effects. Extending the $\Gamma_3^e$ vDiagMC calculations to include lattice effects would directly test `dfpt_reliable_for_simple_metals` (belief 0.75).
- The framework explicitly excludes strongly correlated systems ($d$- and $f$-electron metals), high-$T_c$ hydrides ($\omega_D/E_F \sim 0.1$), and 2D materials (ungapped plasmons). These boundaries are stated but not probed -- calculations near the validity limits would delineate where the downfolding breaks down.

</details>

---

**[Per-module reasoning graphs with full claim details](docs/detailed-reasoning.md)**
