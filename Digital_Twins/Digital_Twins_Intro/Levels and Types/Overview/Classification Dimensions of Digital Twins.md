---
type: concept_note
topic: Overview
sources:
  - "[[Digital Twin in manufacturing A categorical literature review and classification]]"
  - "[[Arup - Digital Twin Towards a Meaningful Framework]]"
  - "[[Leveraging Digital Twin Technology in Model-Based Systems Engineering]]"
  - "[[Digital Twin Where do humans fit in]]"
  - "[[IBM -  What is a Digital Twin]]"
  - "[[Digital Twin Mitigating Unpredictable, Undesirable Emergent Behavior in Complex Systems]]"
  - "[[Siemens - Digital Twin of Product, Production and Performance]]"
  - "[[ISO 23247-1 Digital twin framework for manufacturing]]"
  - "[[Digital Twin and Digital Thread A Unified Architectural Approach]]"
tags:
  - digital-twins
  - taxonomy
  - levels
  - types
  - classification
---
# Classification Dimensions of Digital Twins

> [!summary] Core Takeaway
> There is no single, universally accepted "level" or "type" of digital twin. The literature classifies twins along several **independent dimensions** that fall into two families:
> - **Levels (ordinal: "how capable is it?"):** how automated the data integration is, how mature or sophisticated the twin is, and how autonomous its decisions and actions are.
> - **Types (categorical: "a twin of what, and when?"):** the hierarchical scope of the twinned entity, its relationship to the physical product across the lifecycle, and the value-chain function it serves.
>
> Any real implementation is a point in this multi-dimensional space, so a complete description always combines both families (e.g., *an asset-level performance twin instance at maturity Level 3*).

---
## Cross-Source Classification Matrix

| Dimension | Family | Question it answers | Categories / scale | Reference framework | Detailed note |
| :-- | :-- | :-- | :-- | :-- | :-- |
| **Data integration** | Level | How automated is the data flow between the physical and the digital object? | Digital Model → Digital Shadow → Digital Twin | Kritzinger et al. (2018) | [[Differences (Digital Twin vs. Simulation vs. 3D Model)]] |
| **Maturity / sophistication** | Level | How capable is the twin as a whole? | Arup: Levels 1–5, scored on autonomy, intelligence, learning and fidelity · Madni: Pre-DT → DT → Adaptive DT → Intelligent DT | Arup (2019); Madni et al. (2019) | [[Maturity Levels (Arup and Madni Frameworks)]] |
| **Autonomy** | Level | Which tasks does the twin perform, and with how much human involvement? | 4 roles (Observer, Analyst, Decision Maker, Action Executor) × 5 automation levels | Agrawal et al. (2023) | [[Levels of Autonomy (Roles and Automation)]] |
| **Hierarchical scope** | Type | How large is the twinned entity? | Component → Asset → System/Unit → Process | IBM; ISO 23247-1 (2021) | [[Hierarchical Types (Component, Asset, System, Process)]] |
| **Lifecycle relationship** | Type | Does a physical counterpart exist yet, and does the twin describe one unit or many? | Prototype (DTP), Instance (DTI), Aggregate (DTA), operated within an Environment (DTE) | Grieves & Vickers (2017) | [[Lifecycle Types (Prototype, Instance, Aggregate)]] |
| **Value-chain function** | Type | Which stage of the value chain does the twin support? | Product, Production, Performance | Siemens; CIMdata (2017) | [[Functional Types (Product, Production, Performance)]] |

---
## Conceptual Breakdown

### A. Levels vs. Types
- **Levels are ordinal.** Each framework orders twins from less to more capable (more automation, more prediction, more learning). A higher level demands more data infrastructure, modeling effort and cost, so the appropriate level is the lowest one that satisfies the use case, not the highest one available.
- **Types are categorical.** They describe *what* is being twinned and *when*, without implying that one category is better than another. The only type axis with an internal order is the hierarchical one, and that order expresses containment (components inside assets inside systems), not quality.

### B. The Dimensions Are Independent
- **Different axes, different answers:** A component twin can be highly autonomous (e.g., a closed-loop control twin of a single valve), while a process twin of an entire supply chain may be a descriptive dashboard with no automated feedback at all.
- **Different frameworks, different vocabularies:** The same word can mean different things in different frameworks. Madni et al. call their Level 2 a "Digital Twin" even when it is only refreshed through batch updates, whereas Kritzinger et al. reserve that term for fully automated, bidirectional data exchange. When citing a level, always name the framework it comes from.
- **Multi-metric scoring:** Arup explicitly treats autonomy, intelligence, learning and fidelity as related but independent metrics, so a single twin can score differently on each of them.

### C. Reading a Real Implementation (Illustrative Example)
A wind-farm operator could describe one deployment along every axis at once:
- **Hierarchy:** an asset twin of each turbine's drive train, rolled up into a system twin of each turbine and a process twin of the whole wind farm.
- **Lifecycle:** one DTI per serial-numbered turbine; the fleet analytics that correlate failures across turbines play the role of the DTA.
- **Function:** a performance twin, continuously fed with operational data.
- **Maturity:** Arup Level 3 if it forecasts failures and supports maintenance planning.
- **Integration and autonomy:** if alerts go to engineers who then intervene manually, it is a digital shadow in Kritzinger's terms, with an automated *Analyst* role but a manual *Action Executor* role in the LoDT framework.

*(Example constructed for this note to show how the axes combine; it is not taken from a single source. Component/asset/system/process examples follow IBM's wind-energy examples.)*

### D. The Fit-for-Purpose Principle
The frameworks converge on the same design rule: classification is a **scoping tool**, not a ranking to maximize.
- ISO 23247-1 defines the manufacturing digital twin as a *fit-for-purpose* digital representation of an observable manufacturing element.
- Arup notes that the required fidelity depends on the asset operator's requirements.
- The Digital Twin Consortium ties synchronization to a *specified* frequency and fidelity (see [[Digital Twin and Digital Thread A Unified Architectural Approach]]).

The practical sequence is therefore: define the decision or question the twin must support → choose the hierarchical scope and lifecycle type → set the minimum level of integration, maturity and autonomy that the decision requires.
