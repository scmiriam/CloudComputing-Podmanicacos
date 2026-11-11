---
type: concept_note
topic: Types
sources:
  - "[[Digital Twin Mitigating Unpredictable, Undesirable Emergent Behavior in Complex Systems]]"
  - "[[Leveraging Digital Twin Technology in Model-Based Systems Engineering]]"
  - "[[Siemens - Digital Twin of Product, Production and Performance]]"
tags:
  - digital-twins
  - types
  - lifecycle
  - dtp
  - dti
  - dta
  - michael-grieves
---
# Lifecycle Types (Prototype, Instance, Aggregate)

> [!summary] Core Takeaway
> Grieves & Vickers classify twins by their **relationship to the physical product across its lifecycle**:
> - **Digital Twin Prototype (DTP):** describes the prototypical artifact and contains the information needed to produce a physical version. It exists *before* any physical unit.
> - **Digital Twin Instance (DTI):** remains linked to *one specific* physical product throughout that product's life.
> - **Digital Twin Aggregate (DTA):** the aggregation of *all* DTIs. It need not be an independent data structure; it can be a computing construct that queries the instances.
> - **Digital Twin Environment (DTE):** not a twin type, but the integrated, multi-domain physics application space in which twins are operated on for **predictive** and **interrogative** purposes.

---
## Cross-Source Comparative Matrix

| Evaluation Dimension | Digital Twin Prototype (DTP) | Digital Twin Instance (DTI) | Digital Twin Aggregate (DTA) | Digital Twin Environment (DTE) |
| :-- | :-- | :-- | :-- | :-- |
| **When it exists** | Before physical production | From the moment a specific unit is produced | Once multiple instances exist | Throughout the lifecycle |
| **Physical counterpart** | None yet (the design with all its variants) | One specific, serial-numbered unit | The whole population (fleet) of units | Not applicable (it is the workspace) |
| **Typical content** | Requirements, fully annotated 3D model, bills of materials, processes, services and disposal | As-built configuration, service history, and operational states from sensor data (current, past and predicted) | Queries and correlations across all DTIs | Multi-domain physics models and analytics that operate on DTPs, DTIs and DTAs |
| **Typical use** | Design and virtual testing before committing physical resources | Monitoring and interrogating the state and history of one unit | Fleet-level questions (e.g., mean time between failures of a component) and prognostics | Forecasting future behavior; interrogating current and past states |
| **Cardinality** | One per product design | One per physical unit | One per population | Shared |

---
## Conceptual Breakdown

### A. Digital Twin Prototype (DTP)
- **Purpose:** Captures everything needed to describe and *produce* a physical version that duplicates the virtual one.
- **Content:** Grieves & Vickers list requirements, a fully annotated 3D model, and bills of materials, processes, services and disposal.
- **Value:** Behavior can be tested virtually before physical resources are committed, the information-resource substitution principle described in [[History and Origin (Michael Grieves and NASA)]].

### B. Digital Twin Instance (DTI)
- **One-to-one link:** Each produced unit gets its own DTI, which stays linked to it for the unit's entire life.
- **Content:** Beyond the as-built geometry and configuration (including which components are fitted now and which were fitted before), it stores operational states captured from real sensor data: current, past and predicted.
- **Value:** It reflects the individual unit's manufacturing deviations, operating history and wear, which a generic design model cannot (see [[Differences (Digital Twin vs. Simulation vs. 3D Model)]]).

### C. Digital Twin Aggregate (DTA)
- **Population view:** The DTA aggregates all DTIs of a product.
- **Not necessarily a separate database:** Grieves & Vickers note that, unlike the DTI, the DTA may be a computing construct with access to all instances rather than an independent data structure.
- **Two modes of use:**
  - *Ad hoc:* answering fleet-level questions, such as the mean time between failures of a given component.
  - *Proactive:* continually correlating sensor readings with observed failures to enable prognostics; accumulated failures can supply Bayesian probabilities for prediction.

### D. Digital Twin Environment (DTE)
The DTE is where twins are *used*:
- **Predictive:** forecasting the future behavior and performance of a physical product, either for a single instance or for the population.
- **Interrogative:** querying DTIs for their current and past histories, regardless of where their physical counterparts are located.

### E. Note on the Taxonomy's Evolution
- In the widely circulated 2016 excerpt of the chapter (published in the 2017 Springer book *Transdisciplinary Perspectives on Complex Systems*), Grieves & Vickers state that digital twins are of **two types** (DTP and DTI) operated on in a DTE, yet the same text also defines the **DTA**. This explains why sources cite the chapter as either 2016 or 2017.
- Later texts by Grieves, and most secondary literature, present **three types**: DTP, DTI and DTA.

### F. Relationship to Other Frameworks (Interpretive)
- **Madni et al.:** The *Pre-Digital Twin* (Level 1), a virtual prototype built before the physical system exists, corresponds closely to the DTP (see [[Maturity Levels (Arup and Madni Frameworks)]]).
- **Siemens:** The *product twin* is mostly prototype-centered, while the *performance twin* of products in operation corresponds to DTIs and, across a fleet, to the DTA (see [[Functional Types (Product, Production, Performance)]]).
- **Vault context:** [[What is a Digital Twin]] introduces these archetypes briefly; this note details them.
