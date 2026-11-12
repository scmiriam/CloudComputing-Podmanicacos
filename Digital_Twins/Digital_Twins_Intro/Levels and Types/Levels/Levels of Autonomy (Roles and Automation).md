---
type: concept_note
topic: Levels
sources:
  - "[[Digital Twin Where do humans fit in]]"
  - "[[Arup - Digital Twin Towards a Meaningful Framework]]"
  - "[[Digital Twin in manufacturing A categorical literature review and classification]]"
tags:
  - digital-twins
  - autonomy
  - automation
  - human-in-the-loop
  - levels
---
# Levels of Autonomy (Roles and Automation)

> [!summary] Core Takeaway
> Autonomy describes how much of the **sense → analyze → decide → act** cycle a digital twin performs without people. The *Levels of Digital Twin* (LoDT) framework (Agrawal et al., 2023) makes this two-dimensional:
> - **Four roles** a twin can play: *Observer, Analyst, Decision Maker* and *Action Executor*.
> - **Five automation levels** for each role, from fully manual to non-routine autonomy.
>
> Because each role is graded separately, one twin can be highly automated as an Observer and still fully manual as an Action Executor. Autonomy is therefore a profile, not a single number.

---
## The LoDT Framework

### Dimension 1: Roles

| Role | What the twin does | Typical techniques |
| :-- | :-- | :-- |
| **Observer** | Collects, processes and presents data about the physical world | Sensing, data acquisition, representation and visualization |
| **Analyst** | Interprets the data against the goal to assess the state of the physical world | Pattern recognition, monitoring, prediction |
| **Decision Maker** | Evaluates alternatives and selects a course of action | Simulation, forecasting, optimization |
| **Action Executor** | Carries out the selected decision in the physical environment | Actuators, control systems |

### Dimension 2: Automation Levels (applied to each role)

| Level | Name | What the twin does | Human role |
| :-- | :-- | :-- | :-- |
| **1** | **No automation (manual)** | Nothing; the role is performed without twin support | Performs the role |
| **2** | **Routine support** | Assists with predefined, rule-based tasks | In control; can override the twin |
| **3** | **Routine autonomy** | Completes routine tasks without supervision | Acts as a backup |
| **4** | **Non-routine support** | Uses learning to assist in dynamic or ambiguous situations | Remains involved in the task |
| **5** | **Non-routine autonomy** (full automation) | Handles non-routine tasks independently and improves its performance over time | Not needed for the task |

---
## Conceptual Breakdown

### A. Why Two Dimensions?
- **Piecemeal reality:** The authors start from the observation that digital twins are rarely implemented as a complete package. In practice some functions are automated by the twin while others are still performed by people.
- **Cost of ambiguity:** Not knowing which roles the twin plays, and which remain human, leads to misallocated resources, unrealistic expectations and strategic misalignment. The framework is meant to help practitioners plan deployments, communicate goals and deliverables, and set a strategic vision.
- **Origin:** The paper comes from construction research (Stanford University and the Indian Institute of Science), published in *Automation in Construction*, and is illustrated with a real case study.

### B. Relationship to the Kritzinger Integration Levels (Interpretive Mapping)
Kritzinger et al. grade only the **automation of the data flow**, not the cognitive work in between. Read alongside LoDT:
- An automated **Observer** corresponds to the automated physical-to-digital flow that defines a **digital shadow**.
- Kritzinger's full **digital twin** requires the digital-to-physical flow to be automated as well, which implies an automated **Action Executor**, at least for routine tasks.
- The **Analyst** and **Decision Maker** roles sit between the two flows and have no counterpart in Kritzinger's taxonomy; LoDT makes them explicit and gradable.

*(This mapping is an interpretation made for this note; neither paper defines it.)* See [[Bidirectional Data Loop (Closed-Loop Feedback)]].

### C. Arup's Autonomy Metric: A Single-Axis Alternative
Arup (2019) scores autonomy on one five-step scale: from the user controlling every aspect, through user-assisted prompts, partial autonomy (alerting and controlling some functions) and high autonomy on critical tasks, up to safe operation with no human intervention (see [[Maturity Levels (Arup and Madni Frameworks)]]).
- **Simpler, but coarser:** A single score merges all four LoDT roles into one value.
- **Autonomy ≠ intelligence ≠ learning:** Arup scores these separately, so a twin can learn from data (e.g., supervised models) without being allowed to act on its own.

### D. Design Implications
- **Specify autonomy per role.** A requirement such as "Observer L3, Analyst L3, Decision Maker L2, Action Executor L1" is far more precise than "a fully autonomous twin".
- **Autonomy is a design choice, not only a technical limit.** In safety-critical or regulated settings it is common to keep humans in the Decision Maker and Action Executor roles even when automation is technically feasible; Arup reserves its highest fidelity level for life-safety and critical decisions.
- **Raising automation shifts the human role** from performing the task, to supervising it, to acting as a backup. That shift has organizational consequences (skills, accountability), which is precisely what the LoDT framework was designed to surface.
