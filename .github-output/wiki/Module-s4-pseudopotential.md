# Module: s4_pseudopotential

### ueg_vertex_challenge

**QID:** `github:superconductivity_electron_liquids::ueg_vertex_challenge`
**Type:** claim
**Role:** background
**Content:** Computing the particle-particle irreducible four-point vertex $\tilde\Gamma^e$ of the uniform electron gas (UEG) is a long-standing challenge: perturbation theory in the bare Coulomb interaction diverges for $r_s \gtrsim 1$, and partial resummations (RPA, GW) miss crucial vertex corrections. A controlled, systematically improvable method is needed to evaluate $\tilde\Gamma^e$ in the metallic density range $r_s \in [1, 6]$.
**Prior:** 0.95
**Belief:** 0.95

### vdiagmc_method

**QID:** `github:superconductivity_electron_liquids::vdiagmc_method`
**Type:** claim
**Role:** independent
**Content:** Variational diagrammatic Monte Carlo (vDiagMC) provides a controlled, systematically improvable method for computing Feynman diagrammatic series to high order: (i) bold-line (self-consistent) resummation avoids infrared divergences in individual diagrams, (ii) stochastic sampling of diagram topologies and internal variables accesses orders unreachable by deterministic methods, (iii) the series can be extrapolated to infinite order with controlled error bars. For the UEG, vDiagMC achieves reliable convergence of the irreducible vertex in the metallic density range.
**Prior:** 0.90
**Belief:** 0.83
**Referenced by:** noisy_and -> `github:superconductivity_electron_liquids::mu_vdiagmc_values`

### homotopic_expansion

**QID:** `github:superconductivity_electron_liquids::homotopic_expansion`
**Type:** claim
**Role:** independent
**Content:** The homotopic transformation provides a physically motivated reorganization of the diagrammatic series: by continuously deforming the bare Coulomb interaction $v(q)$ into a form that incorporates partial screening at each perturbative order, the series convergence is dramatically improved. This allows the vDiagMC calculation to reach converged results for the four-point vertex at metallic densities with modest diagram orders ($n \lesssim 7$).
**Prior:** 0.88
**Belief:** 0.79
**Referenced by:** noisy_and -> `github:superconductivity_electron_liquids::mu_vdiagmc_values`

### mu_vdiagmc_values

**QID:** `github:superconductivity_electron_liquids::mu_vdiagmc_values`
**Type:** claim
**Role:** derived
**Content:** vDiagMC calculations of the UEG four-point vertex yield the Coulomb pseudopotential at the Fermi energy scale: $\mu_{E_F}(r_s)$ is positive and monotonically increasing with $r_s$ in the metallic density range. Representative values include $\mu_{E_F} \approx 0.21$ at $r_s = 2$ (aluminum-like) and $\mu_{E_F} \approx 0.33$ at $r_s = 3.3$ (lithium-like). These results, combined with the BTS relation, yield $\mu^* \approx 0.10$--$0.15$ at the Debye scale, consistent with the empirical range but now derived from first principles with controlled error bars of a few percent.
**Belief:** 0.50
**Derived from:** noisy_and
**Premises:** `github:superconductivity_electron_liquids::vdiagmc_method`, `github:superconductivity_electron_liquids::homotopic_expansion`
**Referenced by:** noisy_and -> `github:superconductivity_electron_liquids::mu_available_for_simple_metals`; infer -> `github:superconductivity_electron_liquids::ab_initio_workflow`; unknown -> `github:superconductivity_electron_liquids::rpa_vs_vdiagmc`

### rpa_vs_vdiagmc

**QID:** `github:superconductivity_electron_liquids::rpa_vs_vdiagmc`
**Type:** claim
**Role:** structural
**Content:** not_both_true(A, B)
**Belief:** 1.00
**helper_kind:** contradiction_result
