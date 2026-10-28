# The One-Sided Universe: Conformal Bounce, Non-Orientable Spacetime Topology, and Primordial Tensor Suppression

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Journal: Phys. Rev. D](https://img.shields.io/badge/Journal-Phys.%20Rev.%20D%20(Submitted)-blue.svg)](https://journals.aps.org/prd/)

Numerical simulation routines and figure generation scripts supporting the paper:
> **The One-Sided Universe: Conformal Bounce, Non-Orientable Spacetime Topology, and Primordial Tensor Suppression**  
> Zeyu Cheng (程泽雨)  
> *Submitted to Physical Review D*

---

## Overview

This repository contains the standalone, reproducible Python simulation codes for:
1. **`generate_paper_figures.py`**:
   - Generates Figure 1 (Topological comparison: Standard Inflation vs. BFT CPT Universe vs. One-Sided M\"obius Universe $\mathcal{M}_4 = (\mathbb{R} \times S^3)/\mathbb{Z}_2$).
   - Generates Figure 2 (Cosmological parameter constraints in the $(n_s, r)$ plane comparing Planck 2018 + BK18, Starobinsky $R^2$ inflation, LiteBIRD / CMB-S4 sensitivity, and our primary null tensor prediction $r \equiv 0$).
2. **`simulate_cmb_low_l.py`**:
   - Calculates the Sachs-Wolfe angular power spectrum $C_\ell$ on the compact spatial quotient $\mathbb{RP}^3 = S^3/\mathbb{Z}_2$ with discrete Laplacian eigenvalues $k_n^2 = n(n+2)/R_0^2$ ($n$ even).
   - Simulates the large-scale quadrupole ($\ell=2$) and octupole ($\ell=3$) power deficits and performs theoretical consistency assertion checks.

---

## Installation & Requirements

The scripts require standard Python 3.9+ with `numpy` and `matplotlib`. No external complex cosmological Boltzmann solvers are required.

```bash
pip install -r requirements.txt
```

---

## Usage

### 1. Generate Publication Figures
To reproduce Figures 1 and 2:
```bash
python generate_paper_figures.py
```
Outputs:
- `fig1_topology_comparison.pdf` / `.png`
- `fig2_ns_r_constraints.pdf` / `.png`

### 2. Run CMB Low-$\ell$ Suppression Simulation
To evaluate the discrete spectrum and verify theoretical assertions:
```bash
python simulate_cmb_low_l.py
```
Outputs:
- Full numerical metrics for $\ell=2, 3, 5, 10$ across curvature radii $R_0 = 0.85\Delta\eta, 1.00\Delta\eta, 1.25\Delta\eta$.
- Verification of quadrupole suppression ($\sim 40\%$ at $R_0 = 1.0\chi_{\text{rec}}$).
- `cmb_low_l_suppression.pdf` / `.png`.

---

## Citation

If you use these scripts or build upon this theoretical framework, please cite:
```bibtex
@article{Cheng2026OneSided,
  author    = {Cheng, Zeyu},
  title     = {The One-Sided Universe: Conformal Bounce, Non-Orientable Spacetime Topology, and Primordial Tensor Suppression},
  journal   = {Physical Review D (submitted)},
  year      = {2026},
  note      = {https://github.com/changecheng/one-sided-universe}
}
```

## License
MIT License.
