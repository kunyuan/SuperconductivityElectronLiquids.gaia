# superconductivity-electron-liquids-gaia

Gaia knowledge package: Superconductivity in Electron Liquids (arXiv:2512.19382)

[![Interactive Paper](https://img.shields.io/badge/📖_Interactive_Paper-GitHub_Pages-blue)](https://kunyuan.github.io/SuperconductivityElectronLiquids.gaia/)
[![Knowledge Reference](https://img.shields.io/badge/📚_Reference-Wiki-green)](https://github.com/kunyuan/SuperconductivityElectronLiquids.gaia/wiki)

## Summary

This package formalizes the reasoning structure of Cai, Wang, Zhang, Zhang, Millis, Svistunov, Prokof'ev & Chen (2025), which develops a first-principles framework for predicting the superconducting transition temperature $T_c$ of simple metals without adjustable parameters. The central advance is the controlled computation of the Coulomb pseudopotential $\mu^*$ via variational diagrammatic Monte Carlo (vDiagMC) applied to the uniform electron gas, combined with a rigorous downfolding of the Bethe-Salpeter equation that gives microscopic definitions to the quantities traditionally treated as phenomenological inputs. The knowledge graph traces how these theoretical ingredients flow together into an ab initio workflow that reproduces experimental $T_c$ values for aluminum, zinc, and lithium, while predicting that sodium and magnesium sit near a quantum phase transition between superconducting and non-superconducting ground states.

## Overview

> **Reasoning graph information gain: `4.0 bits`**
>
> <sub>Total mutual information between leaf premises and exported conclusions — measures how much the reasoning structure reduces uncertainty about the results.</sub>

```mermaid
---
config:
  flowchart:
    rankSpacing: 80
    nodeSpacing: 30
---
graph TB
    adiabatic_approx["Adiabatic Approximation\n(0.95 → 0.90)"]:::premise
    tc_al_experimental["Tc(Al) Experimental\n(0.99 → 1.00)"]:::premise
    tc_li_experimental["Tc(Li) Experimental\n(0.85 → 1.00)"]:::premise
    tc_zn_experimental["Tc(Zn) Experimental\n(0.99 → 1.00)"]:::premise
    tc_al_phenomenological["Tc(Al) Phenomenological Prediction\n(0.35 → 0.40)"]:::premise
    tc_li_phenomenological["Tc(Li) Phenomenological Prediction\n(0.10 → 0.13)"]:::premise
    tc_zn_phenomenological["Tc(Zn) Phenomenological Prediction\n(0.35 → 0.40)"]:::premise
    cross_term_suppressed["Cross-Channel Terms Suppressed\n(0.90 → 0.69)"]:::premise
    downfolded_bse["★ Downfolded BSE\n(0.50 → 0.76)"]:::exported
    vdiagmc_method["vDiagMC Method\n(0.90 → 0.83)"]:::premise
    homotopic_expansion["Homotopic Expansion\n(0.88 → 0.79)"]:::premise
    mu_vdiagmc_values["★ mu from vDiagMC: Numerical Values\n(0.50 → 0.50)"]:::exported
    ward_identity["Ward Identity at q->0\n(0.98 → 1.00)"]:::premise
    gamma3_vdiagmc["vDiagMC Computation of Gamma_3\n(0.88 → 1.00)"]:::premise
    quasiparticle_mass_near_unity["Quasiparticle Mass Near Unity\n(0.92 → 0.86)"]:::premise
    dfpt_reliable_for_simple_metals["★ DFPT Reliable for Simple Metals\n(0.50 → 0.86)"]:::exported
    ueg_pseudopotential_parameterization["UEG mu#ast; Parameterization and Mapping\n(0.85 → 0.83)"]:::premise
    ab_initio_workflow["★ Ab Initio Tc Prediction Workflow\n(0.50 → 0.99)"]:::exported
    tc_al_predicted["★ Tc(Al) Ab Initio Prediction\n(0.50 → 0.93)"]:::exported
    tc_zn_predicted["★ Tc(Zn) Ab Initio Prediction\n(0.50 → 0.93)"]:::exported
    tc_li_predicted["★ Tc(Li) Ab Initio Prediction\n(0.50 → 0.96)"]:::exported
    al_pressure_transition["★ Al Pressure-Tc Transition\n(0.50 → 0.79)"]:::exported
    tc_mg_na_near_qpt["★ Na and Mg Near Quantum Phase Transition\n(0.50 → 0.79)"]:::exported
    rpa_predicts_attractive_mu["RPA Predicts Attractive mu#ast;\n(0.50 → 0.25)"]:::premise
    rpa_vs_vdiagmc["rpa_vs_vdiagmc\n(0.50 → 1.00)"]:::premise
    strat_0(["infer\n0.60 bits"]):::weak
    ab_initio_workflow --> strat_0
    strat_0 --> al_pressure_transition
    strat_1(["infer\n0.67 bits"]):::weak
    ab_initio_workflow --> strat_1
    tc_al_experimental --> strat_1
    tc_al_phenomenological --> strat_1
    strat_1 --> tc_al_predicted
    strat_2(["infer\n0.60 bits"]):::weak
    ab_initio_workflow --> strat_2
    tc_li_experimental --> strat_2
    tc_li_phenomenological --> strat_2
    strat_2 --> tc_li_predicted
    strat_3(["infer\n0.60 bits"]):::weak
    ab_initio_workflow --> strat_3
    strat_3 --> tc_mg_na_near_qpt
    strat_4(["infer\n0.67 bits"]):::weak
    ab_initio_workflow --> strat_4
    tc_zn_experimental --> strat_4
    tc_zn_phenomenological --> strat_4
    strat_4 --> tc_zn_predicted
    strat_5(["infer\n0.01 bits"]):::weak
    adiabatic_approx --> strat_5
    cross_term_suppressed --> strat_5
    strat_5 --> downfolded_bse
    strat_6(["infer\n0.10 bits"]):::weak
    dfpt_reliable_for_simple_metals --> strat_6
    downfolded_bse --> strat_6
    mu_vdiagmc_values --> strat_6
    ueg_pseudopotential_parameterization --> strat_6
    strat_6 --> ab_initio_workflow
    strat_7(["infer\n0.00 bits"]):::weak
    downfolded_bse --> strat_7
    gamma3_vdiagmc --> strat_7
    quasiparticle_mass_near_unity --> strat_7
    ward_identity --> strat_7
    strat_7 --> dfpt_reliable_for_simple_metals
    strat_8(["infer\n0.74 bits"]):::weak
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

## Reasoning Structure

### Motivation and Phenomenological Baselines

Traditional superconductivity theory relies on the McMillan or Allen-Dynes formula, which takes two inputs: the electron-phonon coupling constant $\lambda$ from DFPT and the Coulomb pseudopotential $\mu^*$ treated as a free parameter in the range 0.1--0.2. For metals where $T_c$ is in the kelvin or sub-kelvin range, the exponential sensitivity $T_c \propto \exp(-1/g)$ amplifies small uncertainties in $\mu^*$ into order-of-magnitude errors in $T_c$. The phenomenological prediction for lithium using $\mu^* = 0.1$ gives $T_c \approx 0.35$ K, three orders of magnitude above the experimental $4 \times 10^{-4}$ K --- the belief in this prediction settles at just 0.13 (prior 0.10), essentially rejected. For aluminum the phenomenological $T_c \approx 1.9$ K overestimates the measured 1.2 K by 58%, and for zinc the predicted 1.37 K exceeds the observed 0.875 K by 57%; both land at belief 0.40 (prior 0.35). Meanwhile the experimental $T_c$ values themselves are firmly established: belief 1.00 for all three metals. The RPA treatment of the dynamically screened Coulomb interaction predicts an attractive $\mu^* < 0$ for $r_s \gtrsim 2$, but this claim is driven down to belief 0.25 (prior 0.50) once confronted with the vDiagMC evidence, confirming that RPA's neglect of vertex corrections produces qualitatively wrong results in the metallic density regime.

### Downfolding the Bethe-Salpeter Equation

The paper's first major theoretical result is a controlled reduction of the full momentum-frequency Bethe-Salpeter equation to a one-dimensional integral equation in Matsubara frequency. This downfolding rests on two pillars: the adiabatic approximation (belief 0.90, prior 0.95) and the suppression of cross-channel terms mixing Coulomb and phonon contributions at order $O(\omega_c^2/\omega_p^2)$ (belief 0.69, prior 0.90). The cross-term suppression experiences the largest belief drop among premises, falling from 0.90 to 0.69, because its quantitative validity depends on maintaining the hierarchy $\omega_c / \omega_p \lesssim 0.1$ which is material-dependent. Despite this softening, the combined inference still lifts the downfolded BSE conclusion from its uninformative prior of 0.50 to belief 0.76, though the edge carries only 0.01 bits of mutual information --- most of the conclusion's credibility comes from the strong theoretical derivation rather than from the premises' raw probability mass. A toy-model validation at aluminum-like parameters ($r_s = 1.92$, $\omega_D / E_F = 0.005$) shows the full BSE gives $T_c/T_F = 10^{-5.668}$ while the downfolded version gives $10^{-5.667}$, a 0.2% discrepancy that confirms quantitative accuracy. The downfolding also yields microscopic definitions for both $\lambda$ and $\mu_{\omega_c}$, and recovers the Bogoliubov-Tolmachev-Shirkov renormalization relation as an exact corollary (belief 0.99) rather than a phenomenological ansatz.

### Computing the Coulomb Pseudopotential via vDiagMC

The central computational challenge is evaluating the particle-particle irreducible four-point vertex $\tilde{\Gamma}^e$ of the uniform electron gas in the metallic density range $r_s \in [1, 6]$, where standard perturbation theory diverges and partial resummations like RPA miss crucial vertex corrections. Variational diagrammatic Monte Carlo (belief 0.83, prior 0.90) addresses this by stochastically sampling Feynman diagrams with bold-line propagators, and the homotopic expansion (belief 0.79, prior 0.88) dramatically accelerates convergence by continuously deforming the bare Coulomb interaction to incorporate partial screening at each order. Together these techniques produce the highest-MI edge in the graph at 0.74 bits, feeding into the numerical values of $\mu_{E_F}(r_s)$. However, the conclusion $\mu_{\text{vDiagMC}}$ itself remains at belief 0.50 (prior 0.50) --- the graph's most conspicuous stall point --- because the two premise beliefs (0.83 and 0.79) are not strong enough under the noisy-AND model to lift a conclusion that demands both to hold simultaneously. The computed values ($\mu_{E_F} \approx 0.21$ at $r_s = 2$, $\approx 0.33$ at $r_s = 3.3$) directly contradict the RPA prediction of attractive $\mu^*$, driving the contradiction node to belief 1.00 and the RPA claim down to 0.25.

### Validating DFPT for the Electron-Phonon Coupling

The second ingredient for ab initio $T_c$ prediction is the electron-phonon coupling $\lambda$, standardly computed via DFPT. The paper justifies this by showing that the EFT vertex $g(k,q) = z^e \cdot \Gamma_3^e \cdot g_0$ reduces to the DFPT expression when vertex corrections and mass renormalization approximately cancel. Three premises support this: the exact Ward identity at $q \to 0$ (belief 1.00, prior 0.98), the vDiagMC computation of $\Gamma_3^e$ showing modest 10-20% corrections at finite $q$ (belief 1.00, prior 0.88), and the near-unity quasiparticle mass at metallic densities (belief 0.86, prior 0.92). Together with the downfolded BSE, these drive the DFPT reliability conclusion from prior 0.50 to belief 0.86, though the edge carries essentially 0.00 bits of MI because the premises are already so strong that the conclusion's uncertainty reduction is dominated by its own prior-to-posterior shift rather than by marginal premise information.

### The Ab Initio Workflow and Material Predictions

All theoretical threads converge into the parameter-free ab initio workflow: (1) compute $\mu_{E_F}$ from vDiagMC, (2) map to material $r_s$ and scale down via BTS, (3) obtain $\lambda$ from DFPT, (4) solve the downfolded Eliashberg equations. This composite conclusion reaches belief 0.99 (prior 0.50) with 0.10 bits MI, drawing on four premises: the downfolded BSE (0.76), the vDiagMC $\mu$ values (0.50), DFPT reliability (0.86), and the UEG parameterization mapping (0.83). The workflow's near-certainty despite the weak $\mu_{\text{vDiagMC}}$ premise reflects the redundancy in the reasoning graph --- experimental validation via abduction provides additional support. For aluminum, the ab initio $T_c = 1.1 \pm 0.3$ K matches the experimental 1.2 K, lifting the prediction to belief 0.93 (0.67 bits MI). Zinc follows the same pattern: $T_c^{\text{th}} = 0.7 \pm 0.3$ K versus $T_c^{\text{exp}} = 0.875$ K, belief 0.93. The most dramatic success is lithium, where the first-principles $\mu^* \approx 0.16$ nearly cancels $\lambda \approx 0.41$, correctly predicting the sub-millikelvin $T_c$ that phenomenological approaches miss by three orders of magnitude, reaching belief 0.96 (0.60 bits MI).

### Predictions Near the Quantum Phase Transition

The framework makes testable predictions beyond the calibrated metals. Under hydrostatic pressure, aluminum's $T_c$ is predicted to first increase as phonon stiffening raises $\omega_{\text{log}}$ while $\mu^*$ changes modestly, then decrease at high pressures when $\lambda$ is suppressed --- a non-monotonic behavior consistent with experimental pressure studies (belief 0.79, prior 0.50, 0.60 bits MI). Sodium ($r_s = 3.93$, $\lambda \approx 0.18$) is predicted to have its large $\mu^*$ exceed the weak electron-phonon coupling, placing it in the net-repulsive regime with no Cooper instability. Magnesium ($r_s = 2.66$, $\lambda \approx 0.26$) sits in the sub-nanokelvin $T_c$ regime. Both materials are near the quantum phase transition between superconducting and non-superconducting ground states, where $T_c = \omega_\Lambda e^{1/g}$ is exponentially sensitive to the coupling $g \to 0$ (belief 0.79, prior 0.50). These predictions highlight both the power of the ab initio approach --- it can distinguish superconductors from non-superconductors without fitting --- and its fragility near the phase boundary, where small errors in $\mu^*$ or $\lambda$ can toggle the qualitative outcome.

## Conclusions

| Label | Content | Prior | Belief |
|-------|---------|-------|--------|
| ab_initio_workflow | The complete ab initio workflow for predicting $T_c$ of simple metals: (1) co... | 0.50 | 0.99 |
| al_pressure_transition | Under hydrostatic pressure, the ab initio framework predicts that aluminum's ... | 0.50 | 0.79 |
| dfpt_reliable_for_simple_metals | For simple metals, the DFPT calculation of the electron-phonon coupling const... | 0.50 | 0.86 |
| downfolded_bse | The frequency-only downfolded Bethe-Salpeter equation: the full momentum-freq... | 0.50 | 0.76 |
| mu_vdiagmc_values | vDiagMC calculations of the UEG four-point vertex yield the Coulomb pseudopot... | 0.50 | 0.50 |
| tc_al_predicted | The ab initio predicted superconducting transition temperature of aluminum is... | 0.50 | 0.93 |
| tc_li_predicted | The ab initio predicted superconducting transition temperature of lithium is ... | 0.50 | 0.96 |
| tc_mg_na_near_qpt | The ab initio framework predicts that sodium and magnesium have extremely low... | 0.50 | 0.79 |
| tc_zn_predicted | The ab initio predicted superconducting transition temperature of zinc is $T_... | 0.50 | 0.93 |

## Weak Points

### Cross-Channel Term Suppression (belief 0.69, prior 0.90)

The largest belief drop in the entire graph occurs at this premise. The suppression relies on the hierarchy $\omega_c / \omega_p \lesssim 0.1$, which is well satisfied for high-density metals like aluminum but becomes increasingly marginal as $r_s$ grows. For materials with lower plasma frequencies or more complex electronic structures, the $O(\omega_c^2 / \omega_p^2)$ estimate may undercount contributions from intermediate-energy excitations that do not cleanly separate into Coulomb and phonon channels. The downfolded BSE inherits this uncertainty directly, which is why its belief plateaus at 0.76 rather than climbing higher.

### vDiagMC Numerical Values of $\mu$ (belief 0.50, prior 0.50)

The most striking stall point in the graph: despite being the central computational result of the paper, $\mu_{\text{vDiagMC}}$ fails to rise above its uninformative prior. Under the noisy-AND inference model, the conclusion requires both the vDiagMC method (0.83) and the homotopic expansion (0.79) to hold simultaneously, and the product of these probabilities minus noise penalties cannot overcome the prior. This reflects a genuine epistemic gap --- the convergence of the homotopic series at metallic densities, while dramatically better than bare perturbation theory, has not been independently validated by an alternative controlled method.

### Homotopic Expansion Convergence (belief 0.79, prior 0.88)

The homotopic transformation reorganizes the diagrammatic series by continuously deforming the bare Coulomb interaction, and the paper reports convergence at modest diagram orders ($n \lesssim 7$). The belief drops from 0.88 to 0.79 because the convergence guarantee is empirical rather than proven: the series is asymptotic, and convergence at order 7 does not preclude significant contributions from higher orders that happen to cancel at the computed densities but might not at others. The 0.74 bits of MI on the edge to $\mu_{\text{vDiagMC}}$ reflects how much the graph's uncertainty about the final $T_c$ predictions depends on this single methodological claim.

### Quasiparticle Mass Near Unity (belief 0.86, prior 0.92)

The DFPT validation chain assumes $m^*/m \approx 1$ for simple metals, so that the quasiparticle density of states $N_F^*$ matches the band density of states $N_F^{(0)}$. At $r_s \approx 4$ (near sodium), mass enhancements of 10-15% start to matter, and the cancellation between $z^e$ and $\Gamma_3^e$ that makes the EFT vertex equal the DFPT expression becomes less precise. For metals at the boundary of the "simple" classification, this assumption is the weakest link in the $\lambda$ validation.

## Evidence Gaps

### No Independent Validation of vDiagMC Four-Point Vertex

The $\mu_{E_F}(r_s)$ values are computed entirely within the vDiagMC framework using the homotopic expansion. No independent method --- such as auxiliary-field quantum Monte Carlo, coupled-cluster theory, or a fundamentally different diagrammatic resummation --- has verified these values at metallic densities. The belief stall at 0.50 for $\mu_{\text{vDiagMC}}$ directly reflects this single-method dependence. An independent calculation confirming $\mu_{E_F} \approx 0.21$ at $r_s = 2$ would substantially raise the belief throughout the downstream graph.

### Missing Experimental Tests for Na and Mg Predictions

The predictions that sodium has no Cooper instability and magnesium has sub-nanokelvin $T_c$ are untested at the required temperature scales. Both materials are predicted to sit near a quantum phase transition where $T_c$ varies exponentially with small parameter changes, making them ideal discriminators of the theory's accuracy --- but the experiments to reach nanokelvin temperatures in these materials with sufficient purity have not been performed. The belief for both predictions (0.79) would be strongly constrained by such measurements.

### Lattice Effects Beyond the Uniform Electron Gas

The entire $\mu^*$ pipeline assumes that the UEG four-point vertex, parameterized as a function of $r_s$, can be mapped to real crystalline metals with only minor corrections from lattice effects. For nearly-free-electron metals this is well motivated, but the claim (belief 0.90 for simple_metals_weak_lattice) has not been tested for metals with partially filled $d$-bands or complex Fermi surfaces. Extending the framework beyond simple $sp$-metals would require either direct crystalline vDiagMC calculations or a controlled estimate of lattice corrections to the UEG vertex, neither of which exists.
