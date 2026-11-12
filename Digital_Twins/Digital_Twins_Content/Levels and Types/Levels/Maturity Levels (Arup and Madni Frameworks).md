---
type: concept_note
topic: Levels
sources:
  - "[[Arup - Digital Twin Towards a Meaningful Framework]]"
  - "[[Leveraging Digital Twin Technology in Model-Based Systems Engineering]]"
  - "[[Digital Twin in manufacturing A categorical literature review and classification]]"
tags:
  - digital-twins
  - maturity
  - levels
  - arup
  - madni
  - taxonomy
---
# Maturity Levels (Arup and Madni Frameworks)

> [!summary] Core Takeaway
> - **Arup (2019):** Five levels of sophistication, from a digital model that is merely linked to the real-world system (Level 1) to a twin that approaches autonomous reasoning and integrates lower-level twins (Level 5). Each twin is evaluated on four related but independent metrics: **autonomy, intelligence, learning and fidelity**.
> - **Madni et al. (2019):** Four levels defined by whether a physical twin exists, how its data arrives (batch vs. real time) and what the twin learns: **Pre-Digital Twin → Digital Twin → Adaptive Digital Twin → Intelligent Digital Twin**.
> - **Shared trajectory:** Both ladders move from passive representation, through prediction, towards learning and autonomy. Arup observed in 2019 that twins at Levels 4 and 5 were still rare.

---
## Arup: Five Levels of Sophistication (Table 3 of the report)

| Level | Characterization | Typical capability | Example given by Arup |
| :-- | :-- | :-- | :-- |
| **1** | Digital model linked to the real-world system, without intelligence, learning or autonomy | Basic representation with limited functionality | A basic map |
| **2** | Model with some feedback and control, usually for small-scale systems | Reports conditions to a human operator | Building temperature sensors reporting to an operator |
| **3** | Model that provides predictive maintenance, analytics and insights | Forecasting and decision support | Predicting when rail infrastructure will fail |
| **4** | Model that learns efficiently from multiple data sources and makes autonomous decisions within a given domain | Domain-specific autonomy | Real-time route recommendations |
| **5** | Model with broad capabilities that approaches autonomous reasoning, responds to unseen scenarios and integrates lower-level twins | Takes over tasks normally performed by a human operator | A smart-city neighborhood model |

## Arup: Evaluation Metrics (Table 2 of the report)

| Score | **Autonomy** (acting without human input) | **Intelligence** (replicating human cognitive processes) | **Learning** (improving from data without explicit programming) | **Fidelity** (level of detail and closeness to the true value) |
| :-- | :-- | :-- | :-- | :-- |
| **1** | The user controls every aspect | None | No learning component | Low accuracy; conceptual model |
| **2** | User-assisted through prompts and notifications | Reactive: responds only to stimuli | Executes a programmed list of commands | Low to medium accuracy; usable for taking measurements |
| **3** | Partial autonomy: can alert and control some functions | Learns from historical data to inform decisions | Supervised learning on labeled data | Medium accuracy; a reliable representation of the physical world |
| **4** | High autonomy: performs critical tasks with little or no human intervention | Understands the needs of other intelligent systems | Unsupervised learning (finds structure without labels) | Precise measurements |
| **5** | Operates safely with no human intervention | Self-aware, human-like intelligence | Reinforcement learning (feedback and rewards) | High accuracy; suitable for life-safety and critical decisions |

## Madni et al.: Four Levels (Table 1 of the paper)

| Level | Name | Physical twin | Data received from the physical twin | Machine learning |
| :-- | :-- | :-- | :-- | :-- |
| **1** | **Pre-Digital Twin** | Does not exist yet | Not applicable | None |
| **2** | **Digital Twin** | Exists | Performance, health and maintenance data, via **batch** updates | None |
| **3** | **Adaptive Digital Twin** | Exists | Performance, health and maintenance data, via **real-time** updates | Learns **operator preferences** (supervised, neural-network based) |
| **4** | **Intelligent Digital Twin** | Exists | Adds **environment** data; batch and real-time updates | Learns operator preferences **and** system/environment behavior (unsupervised and reinforcement learning) |

---
## Conceptual Breakdown

### A. Arup: A Multi-Metric Framework from the Built Environment
- **Context:** An industry report by the engineering consultancy Arup whose explicit aim is to align terminology and provide a working framework for categorizing how sophisticated a twin is. Its market chapters (cities, energy, property, transport, water) evaluate real case studies with this framework.
- **Levels vs. metrics:** The five levels are an overall characterization, while the four metrics are scored separately. A twin can, for example, have high fidelity but no learning, which is why the metrics are presented as conceptually related but independent.
- **Fidelity is requirement-driven:** Arup stresses that the fidelity a twin needs depends on what the asset operator requires; maximal fidelity is only justified for life-safety or critical decisions.
- **Level 5 as a "twin of twins":** The top level integrates lower-level twins, which connects maturity to the hierarchical axis (see [[Hierarchical Types (Component, Asset, System, Process)]]).

### B. Madni et al.: A Systems-Engineering Ladder
- **Context:** An academic paper on using digital twins within Model-Based Systems Engineering (MBSE). The ladder is driven by two variables: the **data update mode** (batch vs. real time) and the **scope of machine learning** (operator preferences vs. the system and its environment).
- **Level 1 precedes the physical asset:** The Pre-Digital Twin is a virtual prototype created during upfront engineering, before any physical twin exists. This is conceptually close to Grieves & Vickers' *Digital Twin Prototype* (see [[Lifecycle Types (Prototype, Instance, Aggregate)]]).
- **Adaptivity vs. intelligence:** The jump from Level 2 to Level 3 is real-time updating plus learning how the operator prefers to work; the jump to Level 4 is learning about the system and its environment, enabling the twin to cope with situations beyond operator habits.

### C. Side-by-Side Comparison

| Aspect | Arup (2019) | Madni et al. (2019) |
| :-- | :-- | :-- |
| **Origin** | Industry report, built environment | Peer-reviewed paper (*Systems*, MDPI), MBSE |
| **Starting point** | A model already linked to a real-world system | A virtual prototype before the physical system exists |
| **Structure** | 5 levels + 4 independently scored metrics | 4 levels on a single ladder |
| **Main differentiator** | Combined autonomy, intelligence, learning and fidelity | Data update mode and scope of machine learning |
| **Top level** | Approaches autonomous reasoning; integrates other twins | Learns from both the operator and the environment |

### D. Relationship to the Kritzinger Integration Levels
Neither framework uses Kritzinger et al.'s strict criterion (fully automated, bidirectional data exchange) as the entry condition for the word "twin":
- Madni's Level 2 "Digital Twin" receives batch updates and has no automated return path; in Kritzinger's taxonomy it would be a **digital model** (if updates are manual) or a **digital shadow** (if the physical-to-digital flow is automated).
- Arup's Level 2 description mentions "some feedback and control", but its example (sensors reporting to a human operator) would be classified as a **digital shadow** by Kritzinger et al.

This mismatch is why level labels are not interchangeable across frameworks. See [[Differences (Digital Twin vs. Simulation vs. 3D Model)]] and [[Bidirectional Data Loop (Closed-Loop Feedback)]] for the integration criterion.
