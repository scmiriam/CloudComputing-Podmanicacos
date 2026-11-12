---
type: concept_note
topic: Types
sources:
  - "[[IBM -  What is a Digital Twin]]"
  - "[[ISO 23247-1 Digital twin framework for manufacturing]]"
  - "[[Digital Twin Mitigating Unpredictable, Undesirable Emergent Behavior in Complex Systems]]"
  - "[[Arup - Digital Twin Towards a Meaningful Framework]]"
tags:
  - digital-twins
  - types
  - hierarchy
  - granularity
  - iso-23247
---
# Hierarchical Types (Component, Asset, System, Process)

> [!summary] Core Takeaway
> Classifying a twin by **scope** answers the question "how much of the physical world does it represent?". IBM describes four nested layers of magnification (**component/part, asset, system/unit and process** twins) that can coexist in the same environment, each one composed of twins from the layer below. ISO 23247-1 (2021) broadens *what* can be twinned in manufacturing to eight categories of observable manufacturing elements, from equipment and products to personnel and documents, and lists hierarchical modeling among the framework's requirements.

---
## Cross-Source Comparative Matrix

| Evaluation Dimension | Component / Part Twin | Asset Twin | System / Unit Twin | Process Twin |
| :-- | :-- | :-- | :-- | :-- |
| **Scope** | A single individual part | A functional unit made of two or more components | Several assets working together as an integrated system | Several systems working together across a facility, supply chain or operational workflow |
| **Main insight** | Granular behavior of a specific component | How components interact with one another in real time | System-level performance and where it can be improved | End-to-end coordination and efficiency of the whole operation |
| **Oil & gas example (IBM)** | A valve in a pipeline | The pipeline valve system | A pipeline segment | An end-to-end oil distribution network |
| **Wind energy example (IBM)** | A motor in a wind turbine | The turbine's drive train | A whole wind turbine | A wind farm |
| **Automotive example (IBM)** | A turbocharger | The turbocharging system | The vehicle powertrain | The automotive manufacturing process |
| **Typical data** | Dense, high-frequency sensor signals from one part | Combined signals of the interacting components | Aggregated asset states and system KPIs | Flows, throughput, schedules and cross-system KPIs |

*(The "typical data" row is a general characterization added for this note, not a statement from IBM.)*

---
## Conceptual Breakdown

### A. Four Layers of Magnification (IBM)
- **Component twins** are the most granular: they isolate a single part to understand its condition and behavior in detail.
- **Asset twins** combine two or more components into a functional unit and reveal how those components interact.
- **System (unit) twins** show how multiple assets fit together and where system-level performance can be improved.
- **Process twins** offer the broadest view: how whole systems cooperate across a facility, supply chain or workflow.
- **Coexistence:** IBM presents these as layers that can operate at the same time in one production environment. Each layer widens the view rather than replacing the one below.

### B. Composition vs. Aggregation
Two different ways of "grouping" twins are often confused:
- **Composition (hierarchy):** *different* parts are combined into a larger whole (drive train + blades + tower → wind turbine). This is IBM's hierarchy.
- **Aggregation (population):** *many instances of the same* product are combined (100 identical turbines → fleet). This is Grieves & Vickers' *Digital Twin Aggregate* (see [[Lifecycle Types (Prototype, Instance, Aggregate)]]).

Both can exist at the same time: a wind farm is a process twin (composition of turbines), while fleet analytics across all turbines of the same model form an aggregate.

### C. ISO 23247-1: What Can Be Twinned in Manufacturing
The ISO 23247 series calls the things being twinned **observable manufacturing elements (OMEs)** and lists eight categories:

| OME category | Illustrative example |
| :-- | :-- |
| **Personnel** | Operators and their assignments |
| **Equipment** | Machine tools, robots, fixtures |
| **Material** | Raw stock, consumables |
| **Process** | A machining or assembly operation |
| **Facility** | A plant, a cell, its infrastructure |
| **Environment** | Ambient conditions such as temperature or humidity |
| **Product** | Parts and assemblies being produced |
| **Supporting document** | Process plans, work instructions, specifications |

*(Category names are from the ISO 23247-1 table of contents; the examples are illustrative.)*

- **Beyond physical "things":** The list shows that a twin can represent people, processes and documents, not only machines.
- **Hierarchical modeling as a requirement:** Among its requirements for manufacturing digital twins, ISO 23247-1 includes a clause on hierarchical modeling (clause 5.3.15), formalizing the idea that twins are organized in nested levels.

### D. Towards Systems of Systems
- At the top of the hierarchy, a twin becomes a **twin of twins**. Arup's Level 5 explicitly integrates lower-level twins (its example is a smart-city neighborhood model), and the report envisions an ecosystem of twins sharing data and learning from each other across organizational boundaries (see [[Maturity Levels (Arup and Madni Frameworks)]]).
- **Design implication:** Lower-level twins can only feed higher-level ones if interfaces and data models are consistent between layers; this is where the digital thread becomes essential (see [[Digital Twin vs. Digital Thread]]).
- **Scoping rule:** Choose the lowest layer that answers the business question. A process twin is not "better" than a component twin; it answers a different question.
