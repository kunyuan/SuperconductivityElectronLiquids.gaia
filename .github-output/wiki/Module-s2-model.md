# Module: s2_model

### electron_phonon_action

**QID:** `github:superconductivity_electron_liquids::electron_phonon_action`
**Type:** claim
**Role:** background
**Content:** The effective action of the electron-phonon coupled system can be decomposed as $S = S_e + S_{\mathrm{ph}} + S_{e\text{-ph}} + S_{\mathrm{CT}} + O(\sqrt{m/M})$, where $m$ is the electron mass and $M$ is the ion mass. $S_e$ is the complete many-electron action without any approximation, $S_{\mathrm{ph}}$ describes phonons with physical dispersion, $S_{e\text{-ph}}$ is the coupling between electron density and ionic displacement, and $S_{\mathrm{CT}}$ is a counterterm that subtracts the static electron polarization contribution already included in the physical phonon dispersion to prevent double counting.
**Belief:** 0.95
**figure:** artifacts/images/4_1.jpg
**caption:** Fig. 2 | Diagrammatic representation of the phonon-mediated e-e interaction W^ph, composed of phonon propagator D, bare coupling g^(0), vertex function Gamma_3^e, and dielectric function.
**prior:** 0.95
**prior_justification:** Standard EFT decomposition.

### bse_kernel_decomposition

**QID:** `github:superconductivity_electron_liquids::bse_kernel_decomposition`
**Type:** claim
**Role:** derived
**Content:** The kernel of the Bethe-Salpeter equation (BSE) can be decomposed into the purely electronic particle-particle irreducible four-point vertex $\tilde\Gamma^e$ (encoding all non-perturbative Coulomb effects) and the phonon-mediated effective electron-electron interaction $W^{\mathrm{ph}}$: $\tilde\Gamma = \tilde\Gamma^e + W^{\mathrm{ph}} + O(\omega_D/E_F)$. Migdal's theorem ensures that higher-order phonon vertex corrections are suppressed by the adiabatic small parameter.
**Belief:** 0.74
**Derived from:** deduction
**Premises:** `github:superconductivity_electron_liquids::me_framework`
**figure:** artifacts/images/4_2.jpg
**caption:** Fig. 3 | Self-consistent Bethe-Salpeter equation for the anomalous vertex in momentum space, with kernel consisting of the electronic four-point vertex Gamma_e and phonon-mediated interaction W^ph.
**gaia:** {'provenance': {'referenced_claims': ['me_framework']}}
**Referenced by:** support -> `github:superconductivity_electron_liquids::full_bse_toy_model`; deduction -> `github:superconductivity_electron_liquids::downfolded_bse`

### precursory_cooper_flow

**QID:** `github:superconductivity_electron_liquids::precursory_cooper_flow`
**Type:** claim
**Role:** background
**Content:** The low-frequency limit of the anomalous vertex function on the Fermi surface $\Lambda_0$ obeys a universal scaling relation (precursory Cooper flow, PCF): $\Lambda_0 = 1/(1 + g\ln(\omega_\Lambda/T)) + O(T)$, where $g$ is the dimensionless coupling constant ($g < 0$ corresponds to net attraction) and $\omega_\Lambda$ is an effective high-energy cutoff. When $g < 0$, $\Lambda_0$ diverges at $T_c = \omega_\Lambda e^{1/g}$; by computing in the normal state and extrapolating, one can predict $T_c$.
**Belief:** 0.90
**prior:** 0.9
**prior_justification:** Verified in prior work.
