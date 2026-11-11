---
type: source
author: Adil Rasheed, Omer San, Trond Kvamsdal
organization: Norwegian University of Science and Technology (NTNU) / Oklahoma State University / SINTEF Digital
year: 2020
focus: Academic Review / Modeling Challenges / Hybrid AI-Physics & Reduced-Order Modeling
url: https://doi.org/10.1109/ACCESS.2020.2970143
doi: 10.1109/ACCESS.2020.2970143
document_id: Rasheed et al.
tags:
  - source
  - digital-twins
  - challenges
  - hybrid-modeling
  - reduced-order-modeling
  - ai
---

# [Source] - Digital Twin: Values, Challenges and Enablers From a Modeling Perspective (Rasheed et al., 2020)

- **Author/Entity:** Adil Rasheed, Omer San & Trond Kvamsdal (NTNU, Oklahoma State University & SINTEF Digital)
- **Year:** 2020 (*IEEE Access*, Vol. 8, pp. 21980–22012)
- **Focus:** Survey of digital twin values, computational/modeling challenges, and enabling methodologies
- **Key Quote:**
  - *"A digital twin is defined as a virtual representation of a physical asset enabled through data and simulators for real-time prediction, optimization, monitoring, controlling, and improved decision making."*
- **Linked Notes:**
  - [[Challenges and Future Landscape of Digital Twins]]
  - [[Interoperability, Modeling and Socio-Technical Challenges]]
  - [[Hybrid AI-Physics and Reduced-Order Modeling]]

## Source Summary
A widely cited open-access review examining why high-fidelity simulations struggle to operate in real time and how hybrid modeling and reduced-order techniques resolve this bottleneck:

1. **Core Modeling Tension (Physics vs. Data):**
   - **Physics-based (white-box) models:** Governed by conservation laws and partial differential equations (CFD, FEA); offer physical interpretability and generalization to unseen states, but are computationally expensive, slow for real-time loops, and sensitive to incomplete boundary conditions.
   - **Data-driven (black-box) ML models:** Fast at inference once trained and adaptable to complex patterns, but data-hungry, opaque ("black box"), prone to violating physical laws, and unreliable outside their training distribution.
2. **Major Modeling Challenges:**
   - High computational cost incompatible with real-time closed-loop latency requirements.
   - Sensor noise, sparse measurements, and unobservable internal states.
   - Coupled multiphysics and multiscale interactions across long lifecycles.
   - **Verification, Validation, and Uncertainty Quantification (VV&UQ):** Proving that the virtual model remains faithful to the physical asset under changing operating envelopes.
3. **Key Technological Enablers (Tendencies):**
   - **Hybrid Analysis and Modeling (HAM):** Combining physics-based equations with data-driven machine learning (e.g., physics-informed neural networks, residual correction, and data assimilation) to retain physical consistency while running at real-time speeds.
   - **Reduced-Order Modeling (ROM):** Compressing high-dimensional solvers (via Proper Orthogonal Decomposition or deep-learning surrogates) by orders of magnitude so complex simulations can execute online across cloud and edge nodes.
   - **Big Data Cybernetics & Cloud/Edge HPC:** Closing the loop between continuous sensor fusion, scalable cloud training, and low-latency edge execution.
