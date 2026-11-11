---
type: concept_note
topic: Types
sources:
  - "[[Siemens - Digital Twin of Product, Production and Performance]]"
  - "[[ISO 23247-1 Digital twin framework for manufacturing]]"
  - "[[Digital Twin Mitigating Unpredictable, Undesirable Emergent Behavior in Complex Systems]]"
tags:
  - digital-twins
  - types
  - product-twin
  - production-twin
  - performance-twin
  - manufacturing
---
# Functional Types (Product, Production, Performance)

> [!summary] Core Takeaway
> Industrial practice often classifies twins by the **stage of the value chain** they support. The model popularized by Siemens distinguishes three connected twins:
> - **Product twin:** the product under design, used to test and optimize its mechanics, electronics, software and system behavior before anything is built.
> - **Production twin:** the machines, controllers and production lines that will make the product, used for planning and virtual commissioning before the plant runs.
> - **Performance twin:** continuously fed with operational data from products and plants, used for monitoring, predictive maintenance and optimization.
>
> The value lies in **connecting** the three, so that operational insight flows back into design and manufacturing.

---
## Cross-Source Comparative Matrix

| Evaluation Dimension | Product Twin | Production Twin | Performance Twin |
| :-- | :-- | :-- | :-- |
| **Lifecycle stage** | Definition and design (product development) | Manufacturing engineering and production operations | Operation / utilization of products and plants |
| **What is twinned** | The product and its properties (e.g., stability, usability, aerodynamics, reliability of electronics) | Machines, plant controllers and entire production lines | Products and plants in service (e.g., machine status, energy consumption) |
| **Key activities** | Virtual testing and design optimization across mechanical, electronic, software and system domains | Production planning, PLC code generation, virtual commissioning to catch errors before start-up | Predictive maintenance, energy optimization, data-driven services and business models |
| **Main data** | Engineering models and simulation results | Plant, process and automation models; production data | Live operational data |
| **Closest Grieves & Vickers type** *(interpretive)* | DTP of the product | DTP of the plant during planning; DTI of the running line | DTI per unit; DTA across the fleet |
| **Closest ISO 23247-1 application** *(interpretive)* | Engineering design | Production control; real-time control | Predictive maintenance; health check; off-line analytics |

---
## Conceptual Breakdown

### A. Product Twin
- **When:** Created as early as the definition and design stage of a planned product.
- **What for:** Mechanical, electronic, software and system behavior can be tested and optimized virtually before a physical prototype exists, reducing late design changes.
- **Role:** Acts as the core model that holds and manages the product's geometry and other attributes (per CIMdata).

### B. Production Twin
- **When:** During manufacturing engineering and before (and during) production operations.
- **What for:** It represents every aspect of production, from individual machines and plant controllers to entire lines, in a virtual environment. Automation code can be generated and the plant virtually commissioned, so errors are found and prevented before the real plant runs.
- **Value:** Siemens links this to customized mass production, because complex production routes can be calculated, tested and programmed virtually at low cost.

### C. Performance Twin
- **When:** During operation of the product or the plant.
- **What for:** It is constantly fed with operational data from products or the production plant and supports predictive maintenance, energy optimization and new data-driven business models.

### D. Closing the Loop
- Siemens describes a **closed decision-making loop** in which knowledge from the performance twin is fed back through the value chain into the product and production twins, enabling continuous optimization.
- CIMdata's analysis of the Siemens approach (2017) describes this "actionable, holistic" combination of functional twins as a way to create a **digital thread** across the product and process lifecycle (see [[Digital Twin vs. Digital Thread]]).
- CIMdata's own definition mirrors the three types: a twin can represent the product itself, its production process, or the way the product is used, and it must be accurate enough to predict real physical performance.

### E. Caveat: A Vendor Taxonomy
- This classification originates in Siemens' strategy and is aligned with its software portfolio (product design, factory engineering, automation and IoT platforms). It is a useful **value-chain lens**, but it is not a standard.
- The standards-based counterpart for manufacturing is ISO 23247-1, which classifies twins by the element they represent (see [[Hierarchical Types (Component, Asset, System, Process)]]) and lists applications such as real-time control, off-line analytics, predictive maintenance, health check, engineering design, production control and video surveillance.
