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
    adiabatic_approx["Adiabatic Approximation\n(0.95 → 0.71)"]:::premise
    tc_al_experimental["Tc(Al) Experimental\n(0.99 → 1.00)"]:::premise
    tc_li_experimental["Tc(Li) Experimental\n(0.85 → 0.94)"]:::premise
    tc_zn_experimental["Tc(Zn) Experimental\n(0.99 → 1.00)"]:::premise
    tc_al_phenomenological["Tc(Al) Phenomenological Prediction\n(0.35 → 0.41)"]:::premise
    tc_li_phenomenological["Tc(Li) Phenomenological Prediction\n(0.10 → 0.13)"]:::premise
    tc_zn_phenomenological["Tc(Zn) Phenomenological Prediction\n(0.35 → 0.41)"]:::premise
    cross_term_suppressed["Cross-Channel Terms Suppressed\n(0.90 → 0.50)"]:::premise
    downfolded_bse["★ Downfolded BSE\n(0.50 → 0.33)"]:::exported
    vdiagmc_method["vDiagMC Method\n(0.90 → 0.84)"]:::premise
    homotopic_expansion["Homotopic Expansion\n(0.88 → 0.81)"]:::premise
    mu_vdiagmc_values["★ mu from vDiagMC: Numerical Values\n(0.50 → 0.55)"]:::exported
    ward_identity["Ward Identity at q->0\n(0.98 → 0.99)"]:::premise
    gamma3_vdiagmc["vDiagMC Computation of Gamma_3\n(0.88 → 0.95)"]:::premise
    quasiparticle_mass_near_unity["Quasiparticle Mass Near Unity\n(0.92 → 0.88)"]:::premise
    dfpt_reliable_for_simple_metals["★ DFPT Reliable for Simple Metals\n(0.50 → 0.75)"]:::exported
    ueg_pseudopotential_parameterization["UEG mu#ast; Parameterization and Mapping\n(0.85 → 0.85)"]:::premise
    ab_initio_workflow["★ Ab Initio Tc Prediction Workflow\n(0.50 → 0.96)"]:::exported
    tc_al_predicted["★ Tc(Al) Ab Initio Prediction\n(0.50 → 0.90)"]:::exported
    tc_zn_predicted["★ Tc(Zn) Ab Initio Prediction\n(0.50 → 0.90)"]:::exported
    tc_li_predicted["★ Tc(Li) Ab Initio Prediction\n(0.50 → 0.90)"]:::exported
    al_pressure_transition["★ Al Pressure-Tc Transition\n(0.50 → 0.77)"]:::exported
    tc_mg_na_near_qpt["★ Na and Mg Near Quantum Phase Transition\n(0.50 → 0.77)"]:::exported
    rpa_predicts_attractive_mu["RPA Predicts Attractive mu#ast;\n(0.50 → 0.23)"]:::premise
    rpa_vs_vdiagmc["rpa_vs_vdiagmc\n(0.50 → 1.00)"]:::premise
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

Evidence assessment for each exported conclusion, ordered from highest to lowest belief.

### Ab Initio $T_c$ Prediction Workflow (belief: 0.96)

The complete parameter-free workflow: (1) compute $\mu_{E_F}$ from the UEG four-point vertex via vDiagMC, (2) map to the material's $r_s$ and run down to $\mu^\ast$ via the BTS relation, (3) obtain $\lambda$ from DFPT, (4) solve the downfolded Eliashberg equations to predict $T_c$.

**Evidence chain:** This conclusion sits at the apex of the graph and requires all four components to be valid simultaneously. The composite strategy assigns $P(T_c\text{ workflow} \mid \text{all 4 components true}) = 0.92$, reflecting that if the downfolded BSE is correct, $\mu^\ast$ is known, $\lambda$ is reliable, and the UEG-to-material mapping works, the workflow logically follows. The weakest upstream links are:
- Downfolded BSE (belief 0.33) -- the theoretical foundation
- $\mu^\ast$ from vDiagMC (belief 0.55) -- the key new input
- DFPT reliability (belief 0.75) -- the $\lambda$ computation
- UEG parameterization (belief 0.85) -- the material mapping

Despite the low beliefs on the intermediate nodes (especially the downfolded BSE), the workflow conclusion reaches belief 0.96 because the downstream material predictions are strongly validated by experiment, feeding back through the abductive reasoning chains.

![Fig. 9 | Proposed ab initio framework for electron-phonon superconductivity beyond the weak correlation limit.](artifacts/images/13_0.jpg)

**Verdict:** High confidence. The workflow is validated end-to-end by the material-specific predictions below. The main risk is that the method may not generalize beyond simple metals where the UEG approximation holds.

---

### $T_c$(Al) Ab Initio Prediction (belief: 0.90)

Predicted $T_c^{\mathrm{EFT}} = 0.96$ K for aluminum ($r_s = 2.07$, $\mu^\ast = 0.13$, $\lambda = 0.44$), compared with $T_c^{\mathrm{exp}} = 1.2$ K.

**Evidence chain:** The abductive reasoning combines the ab initio workflow (belief 0.96) with the experimental measurement (belief 1.00) and the phenomenological alternative ($\mu^\ast = 0.1$ gives 1.9 K, belief 0.41). The conditional probability of the prediction given the workflow is 0.85 ("material-specific application"). The weakest link is the UEG-to-Al mapping via the band mass correction ($m_b = 1.05$).

![Fig. 10 | Pressure dependence of the superconducting critical temperature in aluminum, with EFT predictions compared to experimental data.](artifacts/images/14_0.jpg)

**Verdict:** Credible. The 20% underestimate (0.96 vs 1.2 K) is consistent with the few-percent uncertainties in both $\mu^\ast$ and $\lambda$. The phenomenological prediction (1.9 K) is clearly worse, and the abductive structure correctly favors the ab initio explanation.

---

### $T_c$(Zn) Ab Initio Prediction (belief: 0.90)

Predicted $T_c^{\mathrm{EFT}} = 0.874$ K for zinc ($r_s = 2.90$, $\mu^\ast = 0.12$, $\lambda = 0.502$), compared with $T_c^{\mathrm{exp}} = 0.875$ K.

**Evidence chain:** Same abductive structure as aluminum. The conditional probability given the workflow is 0.85. The phenomenological alternative ($\mu^\ast = 0.1$ gives 1.37 K, belief 0.41) overestimates by 57%.

![Fig. 11 | Effective BCS coupling strength for simple metals, showing Al, Zn, Li, Na, Mg on the $\lambda$-$\mu^\ast$ plane.](artifacts/images/15_0.jpg)

**Verdict:** This is the most impressive prediction in the paper -- 0.1% agreement with experiment. The near-exact match is partly fortunate (the method has few-percent uncertainties), but it demonstrates that the workflow produces results in the right ballpark without parameter tuning.

---

### $T_c$(Li) Ab Initio Prediction (belief: 0.90)

Predicted $T_c^{\mathrm{EFT}} = 5 \times 10^{-3}$ K for lithium (9R, $r_s = 3.25$, $\mu^\ast = 0.18$, $\lambda = 0.34$), compared with $T_c^{\mathrm{exp}} \approx 4 \times 10^{-4}$ K.

**Evidence chain:** The key physics is that $\mu^\ast = 0.18$ (not the standard guess of 0.1) nearly cancels $\lambda = 0.34$, making the effective coupling $g = \lambda - \mu^\ast(1 + 0.62\lambda)$ very small. The exponential sensitivity $T_c \propto \exp(-1/g)$ then drives $T_c$ to extremely low temperatures. The conditional probability is lowered to 0.80 due to lithium's structural uncertainty at ultra-low $T$. The phenomenological prediction ($\mu^\ast = 0.1$ gives 0.35 K, belief 0.13) overestimates by three orders of magnitude.

**Verdict:** A dramatic improvement over conventional theory (factor of ~10 remaining error vs factor of ~1000 for McMillan). The residual discrepancy likely reflects the controversial crystal structure of lithium at sub-kelvin temperatures -- the HCP structure gives $T_c = 0.03$ K with $\mu^\ast = 0.17$, and neither structure has been definitively established at these temperatures.

---

### Al Pressure-$T_c$ Transition (belief: 0.77)

Under hydrostatic pressure, the framework predicts monotonically decreasing $T_c$, consistent with experimental data up to 6 GPa, with superconductivity vanishing at approximately 60 GPa.

**Evidence chain:** Direct application of the ab initio workflow to aluminum under varying pressure. As pressure increases, $r_s$ decreases, modifying both $\mu^\ast$ and $\lambda$. The conditional probability is 0.80 ("extrapolation to high pressure"). The single upstream dependency is the ab initio workflow (belief 0.96).

**Verdict:** The prediction agrees with the available experimental data (up to 6 GPa), lending credibility to the trend. However, the 60 GPa extinction prediction is extrapolation -- no experimental data constrain it, and structural phase transitions could intervene at high pressures.

---

### Na and Mg Near Quantum Phase Transition (belief: 0.77)

The framework predicts effectively zero $T_c$ for sodium ($2 \times 10^{-13}$ K) and magnesium ($5 \times 10^{-5}$ K), placing both metals near the quantum phase transition between superconducting and non-superconducting ground states.

**Evidence chain:** For Na ($r_s = 3.96$, $\lambda = 0.2$, $\mu^\ast = 0.15$), the Coulomb repulsion nearly cancels the weak electron-phonon coupling. For Mg ($r_s = 2.66$, $\lambda = 0.24$, $\mu^\ast = 0.14$), the situation is similar but less extreme. The conditional probability is 0.80 ("near quantum critical point"). Both predictions rely solely on the ab initio workflow with no experimental data for validation.

**Verdict:** Physically reasonable -- the near-cancellation of $\lambda$ and $\mu^\ast$ in these metals has long been suspected but never quantified from first principles. However, the predictions are entirely theoretical. The exponential sensitivity of $T_c$ near the quantum phase transition means that even small errors in $\mu^\ast$ or $\lambda$ translate into orders-of-magnitude changes in $T_c$. Experimental confirmation would require sub-nanokelvin measurements.

---

### DFPT Reliable for Simple Metals (belief: 0.75)

For simple metals, the DFPT calculation of $\lambda$ is reliable because the EFT vertex matches the DFPT Kohn-Sham expression at the vertex level, and the quasiparticle density of states $N_F^\ast$ nearly equals the band density of states $N_F^{(0)}$.

**Evidence chain:** This conclusion is supported by a composite strategy with three premises: (1) the Ward identity at $q \to 0$ fixes $\Gamma_3^e = m^\ast/m$ (belief 0.99); (2) vDiagMC computation of $\Gamma_3^e$ at finite $q$ shows smooth, modest 10-20% corrections (belief 0.95); (3) $m^\ast/m \approx 1$ for simple metals (belief 0.88). The downfolded BSE (belief 0.33) also enters as a premise, contributing to the belief reduction.

![Fig. 8 | Comparison between the angle-resolved e-ph vertex correction from vDiagMC (points) and DFPT (lines) for different $r_s$ values.](artifacts/images/12_0.jpg)

**Verdict:** The argument is internally consistent and specific to simple metals -- it does not claim DFPT is universally reliable. The main risk is that the cancellation between $z^e$, $\epsilon_\mathbf{q}$, and $\Gamma_3^e$ demonstrated for the UEG may not transfer perfectly to real materials with crystal fields.

---

### $\mu^\ast$ from vDiagMC: Numerical Values (belief: 0.55)

vDiagMC calculations yield $\mu_{E_F}(r_s) \approx 0.27\, r_s$ -- positive, monotonically increasing, and dramatically larger than all RPA-based predictions.

**Evidence chain:** The vDiagMC method (belief 0.84) and homotopic expansion (belief 0.81) are the two premises. The conditional probability is 0.90 ("systematic uncertainty from truncation/resummation"). The modest belief reflects the formal contradiction with RPA ($\mu^\ast < 0$ at $r_s > 2$), which anchors the contradiction node (belief 1.00 for "not both true") and pulls the vDiagMC values toward 0.50.

| $r_s$ | 1 | 2 | 3 | 4 | 5 | 6 |
|--------|---------|---------|---------|----------|----------|--------|
| $\mu_{0.1\,E_F}$ | 0.172(4)| 0.238(4)| 0.278(6)| 0.306(15)| 0.328(12)| 0.35(3)|
| $\mu_{E_F}$ | 0.28(1) | 0.53(2) | 0.77(5) | 1.0(2) | 1.3(2) | 1.8(8) |

![Fig. 4 | Dimensionless bare Coulomb pseudopotential $\mu_{E_F}$ vs $r_s$ from vDiagMC, compared with static RPA, Morel-Anderson, and dynamic RPA predictions.](artifacts/images/8_0.jpg)

**Verdict:** The moderate belief is a graph artifact of the RPA contradiction, not a reflection of the physics. The vDiagMC method is systematically controlled (bold-line resummation, homotopic transformation, extrapolation to infinite order), while RPA is known to fail for $r_s > 1$ due to missing vertex corrections. The downstream material predictions strongly validate these values. After BTS renormalization, $\mu^\ast \approx 0.12\text{-}0.18$ at the Debye scale, consistent with the empirical range but now derived from first principles.

---

### Downfolded BSE (belief: 0.33)

The full momentum-frequency BSE reduces to a one-dimensional integral equation in Matsubara frequency, with corrections bounded by $\omega_D/E_F$, $\omega_c^2/\omega_p^2$, and $T/\omega_c$.

**Evidence chain:** Two premises: the adiabatic approximation (belief 0.71, down from prior 0.95) and cross-channel term suppression (belief 0.50, down from prior 0.90). The low belief on the cross-term suppression is the bottleneck -- it drops from 0.90 to 0.50 because this claim appears as a premise to the downfolded BSE but also feeds into the ab initio workflow, where the abductive reasoning from experimental data creates complex message-passing dynamics. The conditional probability of the infer strategy is structured so that both premises must hold ($P = 0.90$ when all true, $P = 0.02$ when one fails).

The downfolding is validated numerically: for a toy model with aluminum-like parameters, the full and downfolded BSE give $T_c$ values differing by only 0.2%.

![Fig. 5 | Comparison between the precursory Cooper flow solutions of the full and downfolded BSE, demonstrating 0.2% agreement in $T_c$.](artifacts/images/8_1.jpg)

**Verdict:** The low belief is driven by the graph's conservative handling of the cross-term suppression assumption, not by a genuine weakness in the derivation. The 0.2% numerical validation at one density is compelling but has not been tested at higher $r_s$. The derivation itself is rigorous given the three small-parameter bounds; the real question is whether these bounds hold for all materials of interest.

---

## Key Findings

| Label | Content | Prior | Belief |
|-------|---------|-------|--------|
| ab_initio_workflow | Complete parameter-free workflow: vDiagMC $\mu^\ast$ + DFPT $\lambda$ + downfolded Eliashberg equations | 0.50 | 0.96 |
| tc_al_predicted | $T_c^{\mathrm{EFT}}(\mathrm{Al}) = 0.96$ K vs $T_c^{\mathrm{exp}} = 1.2$ K | 0.50 | 0.90 |
| tc_zn_predicted | $T_c^{\mathrm{EFT}}(\mathrm{Zn}) = 0.874$ K vs $T_c^{\mathrm{exp}} = 0.875$ K | 0.50 | 0.90 |
| tc_li_predicted | $T_c^{\mathrm{EFT}}(\mathrm{Li}) = 5 \times 10^{-3}$ K vs $T_c^{\mathrm{exp}} \approx 4 \times 10^{-4}$ K | 0.50 | 0.90 |
| al_pressure_transition | Al $T_c$ monotonically decreases under pressure, vanishing at ~60 GPa | 0.50 | 0.77 |
| tc_mg_na_near_qpt | Na and Mg near quantum phase transition, effectively non-superconducting | 0.50 | 0.77 |
| dfpt_reliable_for_simple_metals | DFPT $\lambda$ reliable for simple metals: vertex corrections cancel at $m^\ast/m \approx 1$ | 0.50 | 0.75 |
| mu_vdiagmc_values | vDiagMC $\mu_{E_F} \approx 0.27\, r_s$, dramatically exceeding RPA predictions | 0.50 | 0.55 |
| downfolded_bse | Frequency-only downfolded BSE with microscopic $\lambda$ and $\mu_{\omega_c}$ | 0.50 | 0.33 |

<details open>
<summary><strong>Weak Points</strong></summary>

**Cross-channel term suppression is the most vulnerable intermediate node.** The entire downfolding procedure rests on cross-channel mixing being $O(\omega_c^2/\omega_p^2) \leq 1\%$, estimated from a plasmon-pole model for three-dimensional metals. This claim drops from prior 0.90 to belief 0.50 -- the largest relative decline among all intermediate nodes. For systems with softer collective modes (low-density metals, 2D materials) or near structural transitions where phonon frequencies approach electronic scales, this suppression could fail, invalidating the downfolded BSE and all downstream conclusions.

**The UEG-to-material mapping introduces unquantified lattice corrections.** The intermediate node `mu_available_for_simple_metals` (belief 0.41) aggregates the vDiagMC $\mu_{E_F}(r_s)$ values with the material-specific $r_s$ and band mass correction. While simple metals are nearly-free-electron-like, the band mass correction for lithium ($m_b = 1.75$) is substantial and not independently validated. The conditional probability of this mapping step is 0.88 ("UEG-to-material mapping adds uncertainty").

**Intermediate nodes in the EFT vertex chain carry moderate beliefs.** The `eft_vertex_matches_dfpt` node (belief 0.58) and `gamma3_approximation` node (belief 0.62) encode the argument that vertex corrections, quasiparticle renormalization, and dielectric screening cancel to make DFPT $\lambda$ reliable. While the physics of this cancellation is well-motivated ($z^e \cdot \Gamma_3^e \approx (m/m^\ast)(m^\ast/m) = 1$), each factor individually carries significant corrections (10-20%), and the cancellation has only been verified for the homogeneous electron gas, not for real crystal potentials.

**The homotopic expansion has unverified analyticity assumptions.** The homotopic transformation (belief 0.81, down from prior 0.88) reorganizes the diagrammatic series by continuously deforming the bare Coulomb interaction. While the log-divergence cure is rigorous, the conformal-map-based resummation relies on analyticity properties that are assumed rather than proven for the UEG four-point vertex at metallic densities.

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
