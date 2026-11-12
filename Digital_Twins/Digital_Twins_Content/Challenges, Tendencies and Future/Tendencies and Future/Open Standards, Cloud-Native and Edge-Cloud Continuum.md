---
type: concept_note
topic: Tendencies and Future
sources:
  - "[[ISO 23247-1 Digital twin framework for manufacturing]]"
  - "[[Digital Twin and Digital Thread A Unified Architectural Approach]]"
  - "[[NVIDIA - BMW Group Starts Global Rollout of NVIDIA Omniverse]]"
  - "[[Digital Twin Enabling Technologies, Challenges and Open Research]]"
  - "[[Digital Twin A Comprehensive Survey of Security Threats]]"
  - "[[Singapore Land Authority - Virtual Singapore]]"
tags:
  - digital-twins
  - tendencies
  - cloud-computing
  - edge-computing
  - standards
  - interoperability
---
# Open Standards, Cloud-Native and Edge-Cloud Continuum

> [!summary] Core Takeaway
> From a Cloud Computing and systems architecture perspective, two structural tendencies are resolving the latency, cost, security, and interoperability bottlenecks of first-generation twins:
> 1. **The Edge–Cloud Continuum:** Rather than forcing all telemetry into a centralized cloud or keeping everything on local hardware, modern deployments partition the twin across tiers—running millisecond closed-loop control and privacy filtering at the **Edge**, while leveraging the **Cloud** for elastic GPU simulation, fleet-wide aggregation (*DTA*), and multi-tenant **PaaS** collaboration.
> 2. **Open Standards & Universal Interoperability Fabrics:** Industry and standardization bodies are replacing proprietary silos with open reference architectures (**ISO 23247**, **DTC Interoperability Framework**) and universal scene/data formats (**OpenUSD**), enabling a continuous **Digital Thread** across multi-vendor tools.

---
## Architectural Distribution Across the Edge–Cloud Continuum

| Architectural Tier | Primary Workload in a Digital Twin | Latency & Bandwidth Profile | Security & Governance Role | Representative Examples in the Vault |
| :-- | :-- | :-- | :-- | :-- |
| **Physical & Edge Tier (On-Premise / Gateway)** | High-frequency sensor acquisition, local signal filtering, fast closed-loop actuation, and lightweight ROM inference. | Sub-millisecond to millisecond latency; reduces raw upstream cloud bandwidth. | Local data anonymization/privacy enforcement; hardware root of trust and X.509/mTLS device identity. | Shop-floor PLCs/sensors; local edge pre-processing before cloud broker ingestion. |
| **Cloud Messaging & Ingestion Fabric** | Asynchronous pub/sub telemetry routing, device twin state synchronization, and digital thread lineage logging. | Milliseconds to seconds (*"specified frequency and fidelity"*, DTC 2021). | Mutual TLS (mTLS), topic-level RBAC/ACL, and anomaly detection on incoming streams. | Managed brokers (AWS IoT Core, Azure IoT Hub) vs. public MQTT in [[Demo - Gemelo digital del aula]]. |
| **Cloud Compute, HPC & PaaS Layer** | Heavy multiphysics simulation (FEA/CFD), photorealistic 3D collaboration, AI model training, and fleet-wide aggregation (*DTA*). | Elastic on-demand scaling (seconds to hours); globally accessible across teams. | Multi-tenant isolation, role-based federation across agencies, and sovereign data compliance. | **BMW Factory Explorer** on NVIDIA Omniverse; **Living Heart** HPC; **Virtual Singapore** national PaaS. |

---
## Conceptual Breakdown

### A. The Edge–Cloud Continuum: Workload Partitioning
As Fuller et al. (2020) and Rasheed et al. (2020) note, neither pure cloud computing nor pure local computing satisfies every requirement of a complex digital twin:
- **Why the Edge is needed:** Fast safety loops, high-frequency vibration telemetry, and privacy-sensitive clinical or video streams cannot tolerate wide-area network latency or raw cloud ingestion costs. Edge nodes filter raw telemetry into *Useful Data* and execute immediate routine actuation.
- **Why the Cloud is indispensable:** Local edge hardware cannot host a national 3D geospatial replica like [[03_Smart City - Virtual Singapore]], run multi-site collaborative 3D factories like [[01_Manufacturing - BMW Group Virtual Factory]], or aggregate thousands of individual *Digital Twin Instances (DTIs)* into a fleet-wide *Digital Twin Aggregate (DTA)* (see [[Lifecycle Types (Prototype, Instance, Aggregate)]]).
- **Cloud-native Digital Twins as PaaS:** Virtual Singapore exemplifies the shift toward **Platform-as-a-Service (PaaS)** twin architectures: a single authoritative cloud twin maintained as shared infrastructure on which multiple government agencies, researchers, and private companies build domain-specific simulation apps.

### B. Convergence on Open Standards and Formats
To eliminate the multi-vendor silos identified in [[Interoperability, Modeling and Socio-Technical Challenges]], the industry is consolidating around three complementary standardization layers:
1. **International Reference Architectures ([[ISO 23247-1 Digital twin framework for manufacturing]]):** Published in 2021, the four-part ISO 23247 series establishes a common vocabulary, observable manufacturing elements (OMEs), a layered reference architecture (Part 2), core information attributes (Part 3), and information exchange requirements (Part 4) built on ISO/IEC 30141.
2. **Cross-Industry Interoperability Frameworks ([[Digital Twin and Digital Thread A Unified Architectural Approach]]):** The Digital Twin Consortium (DTC) defines system interoperability rules linking runtime **Digital Twins** (vertical depth) with the enterprise **Digital Thread** (horizontal lifecycle lineage).
3. **Universal 3D & Scene Formats (OpenUSD):** In [[01_Manufacturing - BMW Group Virtual Factory]], BMW and NVIDIA demonstrated how Pixar's open **Universal Scene Description (USD)** acts as a common lingua franca in the cloud, allowing geometry and metadata from Siemens Process Simulate, Autodesk Revit, and Bentley MicroStation to synchronize non-destructively inside a single shared virtual factory.

### C. Hardening the Cloud–Edge Loop (Zero-Trust IIoT)
Addressing the threat taxonomy of Alcaraz & Lopez (2022) (see [[Technical, Cloud and Security Challenges]]), modern cloud digital twin platforms enforce **security-by-design** across the bidirectional loop:
- **Cryptographic Device Identity & mTLS:** Every physical sensor and actuator authenticates with unique certificates before publishing telemetry or subscribing to command topics—closing the open-broker vulnerability illustrated in [[Demo - Gemelo digital del aula]].
- **Privacy-Preserving & Decentralized Learning:** As noted by Fuller et al. (2020), decentralized or federated learning architectures allow multiple hospital or factory twins to train shared predictive AI models in the cloud without exporting raw confidential patient or proprietary production data.
