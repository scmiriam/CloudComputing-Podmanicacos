---
type: use_case
sector: Healthcare
organization: Dassault Systèmes (Living Heart Project), academic cardiology consortium
year: 2014-2020
maturity: Simulation / Predictive (research)
tags:
  - use-case
  - digital-twins
  - healthcare
  - precision-medicine
---
# [Use Case] Healthcare - Living Heart Project and Cardiac Digital Twins

> [!summary] Core Takeaway
> The **Living Heart Project** built a realistic four-chamber simulation of the human heart from CT and MRI images, simulating both its electrical activity and its mechanical motion. The longer-term vision is a **digital twin of each patient's heart** that doctors can use to test treatments virtually before applying them (precision cardiology).

## Context and problem
- Cardiac devices and treatments (for example valve repair) are hard to test safely on real patients, and every heart is different.
- Precision medicine needs not only patient data but computers and algorithms able to learn, reason and build a digital twin of each patient (Corral-Acero et al., 2020).

## How the twin works
| Element | Implementation |
|---|---|
| Physical entity | A human heart (generic in the Living Heart model; patient-specific in the precision-cardiology vision) |
| Virtual entity | Four-chamber finite element heart model built from computed tomography and magnetic resonance images, coupling electrical excitation and mechanical contraction (Baillargeon et al., 2014) |
| Data link (physical → virtual) | Medical imaging and clinical measurements that personalize the model |
| Data link (virtual → physical) | Device design and treatment planning decisions |

## Results
- The simulator reproduces electrical potential and mechanical deformation across the cardiac cycle, and its **pressure-volume relationship agrees well with clinical observations** (Baillargeon et al., 2014).
- Intended uses: guiding device design and treatment planning for stenosis, regurgitation or prolapse of the aortic, pulmonary, tricuspid or mitral valves (Baillargeon et al., 2014).
- Corral-Acero et al. (2020), a position paper by 39 authors in the *European Heart Journal*, review the first steps of cardiac digital twins and stress combining **mechanistic (physics-based) and statistical (data-driven) models**.

## Maturity level (assessment)
**Simulation moving towards predictive.** The Living Heart model is a proof of concept of a generic heart. A full patient twin with continuous data from the patient is still a research goal.

## Relevance for Cloud Computing
- Finite element simulations of a beating heart need **HPC resources**, often consumed on demand.
- Patient data raises strong **privacy and regulatory requirements** (data location, encryption, access control) for any cloud deployment.

## Limitations
- Model validation and regulatory approval for clinical decisions are major open challenges.
- Personalizing a model to each patient requires large amounts of high-quality medical data.

## References
Summaries: [[The Living Heart Project A robust and integrative simulator for human heart function]] · [[The Digital Twin to enable the vision of precision cardiology]]

- Baillargeon, B., Rebelo, N., Fox, D. D., Taylor, R. L., & Kuhl, E. (2014). The Living Heart Project: A robust and integrative simulator for human heart function. *European Journal of Mechanics - A/Solids*, 48, 38–47. https://doi.org/10.1016/j.euromechsol.2014.04.001
- Corral-Acero, J., Margara, F., Marciniak, M., Rodero, C., Loncaric, F., Feng, Y., ... Lamata, P. (2020). The 'Digital Twin' to enable the vision of precision cardiology. *European Heart Journal*, 41(48), 4556–4564. https://doi.org/10.1093/eurheartj/ehaa159
