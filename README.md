# Superconductivity in Electron Liquids

A [Gaia](https://github.com/SiliconEinstein/Gaia) knowledge package formalizing:

> **Superconductivity in Electron Liquids: A Precision Many-Body Treatment**
>
> arXiv: [2512.19382](https://arxiv.org/abs/2512.19382)

## What This Package Contains

A machine-readable formalization of the paper's argument structure:

- **6 settings** — background context (BCS framework, material parameters)
- **22 claims** — propositions from each section of the paper
- **11 reasoning strategies** — how claims support each other (noisy_and, contradiction, abduction)
- **1 operator** — VDiagMC vs RPA contradiction on the sign of $\mu^*$

### Core Argument

The paper establishes that the Coulomb pseudopotential $\mu^*$ can be computed from first principles using Variational Diagrammatic Monte Carlo (VDiagMC), eliminating the key phenomenological parameter in superconductivity theory. Combined with validated DFPT electron-phonon coupling and a precursory Cooper flow method, this yields reliable $T_c$ predictions for simple metals without adjustable parameters.

### Reasoning Structure

```
VDiagMC method + homotopic expansion + UEG vertex challenge
    → μ* values (noisy_and)

Large corrections + cancellation + numerical validation
    → DFPT reliable for simple metals (noisy_and)

BSE kernel decomposition + electron-phonon action + adiabatic approx
    → precursory Cooper flow (noisy_and)

μ* values + DFPT reliable + Cooper flow
    → ab initio workflow (noisy_and)

ab initio workflow + material parameters
    → Tc predictions for Al, Li, Mg, Na (noisy_and)

μ* values ↔ RPA negative μ* → contradiction
```

## Usage

```bash
pip install gaia-lang
git clone https://github.com/kunyuan/SuperconductivityElectronLiquids.gaia.git
cd SuperconductivityElectronLiquids.gaia
gaia compile .
gaia infer .
```

## License

MIT
