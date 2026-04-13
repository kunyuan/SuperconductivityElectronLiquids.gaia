# Module: s4_pseudopotential

### ueg_vertex_challenge

**QID:** `github:superconductivity_electron_liquids::ueg_vertex_challenge`
**Type:** claim
**Role:** background
**Content:** Computing the particle-particle irreducible four-point vertex $\tilde\Gamma^e$ of the uniform electron gas (UEG) is a long-standing challenge: perturbation theory in the bare Coulomb interaction diverges for $r_s \gtrsim 1$, and partial resummations (RPA, GW) miss crucial vertex corrections. A controlled, systematically improvable method is needed to evaluate $\tilde\Gamma^e$ in the metallic density range $r_s \in [1, 6]$.
**Belief:** 0.95
**prior:** 0.95
**prior_justification:** Recognized challenge.

### vdiagmc_method

**QID:** `github:superconductivity_electron_liquids::vdiagmc_method`
**Type:** claim
**Role:** independent
**Content:** Variational diagrammatic Monte Carlo (vDiagMC) provides a controlled, systematically improvable method for computing Feynman diagrammatic series to high order: (i) bold-line (self-consistent) resummation avoids infrared divergences in individual diagrams, (ii) stochastic sampling of diagram topologies and internal variables accesses orders unreachable by deterministic methods, (iii) the series can be extrapolated to infinite order with controlled error bars. For the UEG, vDiagMC achieves reliable convergence of the irreducible vertex in the metallic density range.
**Belief:** 0.86
**prior:** 0.9
**prior_justification:** Rigorous Feynman diagram expansion; validated at r_s <= 5.
**Referenced by:** support -> `github:superconductivity_electron_liquids::mu_vdiagmc_values`

### homotopic_expansion

**QID:** `github:superconductivity_electron_liquids::homotopic_expansion`
**Type:** claim
**Role:** independent
**Content:** The homotopic transformation provides a physically motivated reorganization of the diagrammatic series: by continuously deforming the bare Coulomb interaction $v(q)$ into a form that incorporates partial screening at each perturbative order, the series convergence is dramatically improved. This allows the vDiagMC calculation to reach converged results for the four-point vertex at metallic densities with modest diagram orders ($n \lesssim 7$).
**Belief:** 0.84
**figure:** artifacts/images/10_0.jpg
**caption:** Fig. 6 | Diagrammatic contributions to the 4-point vertex at first and second order, with Coulomb interaction re-expanded from Yukawa interaction with screening parameter lambda_R.
**prior:** 0.88
**prior_justification:** Log-divergence cure rigorous; conformal-map relies on analyticity.
**Referenced by:** support -> `github:superconductivity_electron_liquids::mu_vdiagmc_values`

### mu_vdiagmc_values

**QID:** `github:superconductivity_electron_liquids::mu_vdiagmc_values`
**Type:** claim
**Role:** derived
**Content:** vDiagMC calculations of the UEG four-point vertex yield the Coulomb pseudopotential at the Fermi energy scale: $\mu_{E_F}(r_s)$ is positive and monotonically increasing with $r_s$ in the metallic density range, approximately following $\mu_{E_F} \approx 0.27\, r_s$. The complete set of values (Cai et al., TABLE I), computed at $\omega_c = 0.1\, E_F$ and rescaled to $E_F$ via the BTS relation:

| $r_s$              | 1       | 2       | 3       | 4        | 5        | 6      |
|--------------------|---------|---------|---------|----------|----------|--------|
| $\mu_{0.1\,E_F}$ | 0.172(4)| 0.238(4)| 0.278(6)| 0.306(15)| 0.328(12)| 0.35(3)|
| $\mu_{E_F}$       | 0.28(1) | 0.53(2) | 0.77(5) | 1.0(2)   | 1.3(2)   | 1.8(8) |

Numbers in parentheses indicate the systematic uncertainty in the last digit. These results, combined with the BTS relation, yield $\mu^\ast \approx 0.12\text{--}0.18$ at the Debye scale, consistent with the empirical range but now derived from first principles with controlled error bars of a few percent. The values are dramatically larger than the static RPA, Morel-Anderson, and dynamic RPA predictions for $r_s > 0.5$ — by a factor of three at $r_s = 5$ — and resolve the long-standing contradiction between phenomenological and RPA-based treatments of the Coulomb pseudopotential.
**Belief:** 0.60
**Derived from:** support
**Premises:** `github:superconductivity_electron_liquids::vdiagmc_method`, `github:superconductivity_electron_liquids::homotopic_expansion`
**figure:** artifacts/images/8_0.jpg
**caption:** Fig. 4 | Dimensionless bare Coulomb pseudopotential mu_EF as a function of r_s for the 3D UEG from vDiagMC data, compared with static RPA, Morel-Anderson, and dynamic RPA predictions.
**gaia:** {'provenance': {'referenced_claims': ['bts_renormalization', 'homotopic_expansion', 'mu_microscopic_definition', 'ueg_vertex_challenge', 'vdiagmc_method']}}
**Referenced by:** support -> `github:superconductivity_electron_liquids::mu_available_for_simple_metals`; infer -> `github:superconductivity_electron_liquids::ab_initio_workflow`; unknown -> `github:superconductivity_electron_liquids::rpa_vs_vdiagmc`

### rpa_vs_vdiagmc

**QID:** `github:superconductivity_electron_liquids::rpa_vs_vdiagmc`
**Type:** claim
**Role:** structural
**Content:** not_both_true(A, B)
**Belief:** 1.00
**helper_kind:** contradiction_result
**prior:** 0.95
