---
type: concept_note
topic: Challenges
sources:
  - "[[Digital Twin Enabling Technologies, Challenges and Open Research]]"
  - "[[Digital Twin A Comprehensive Survey of Security Threats]]"
  - "[[Digital Twin Values, Challenges and Enablers From a Modeling Perspective]]"
  - "[[Digital Twin and Digital Thread A Unified Architectural Approach]]"
  - "[[The Digital Twin to enable the vision of precision cardiology]]"
tags:
  - digital-twins
  - challenges
  - cloud-computing
  - cybersecurity
  - latency
  - infrastructure
---
# Technical, Cloud and Security Challenges

> [!summary] Core Takeaway
> Deploying digital twins over cloud and IoT infrastructures faces four primary technical bottlenecks:
> 1. **IT Infrastructure & Compute Cost:** High-fidelity 3D rendering and multiphysics solvers demand expensive HPC and GPU clusters.
> 2. **Latency & Synchronization Constraints:** Cloud round-trip times often conflict with real-time actuation requirements, requiring careful calibration of synchronization frequency and fidelity.
> 3. **Data Volume, Velocity & Quality ("Useful Data"):** Continuous high-frequency sensor streams generate massive storage/bandwidth overhead while suffering from noise, dropouts, and calibration drift.
> 4. **Bidirectional Cybersecurity & Privacy:** Because a true digital twin has an automated downward actuation channel, compromising the cloud platform or message broker can directly damage physical assets or expose regulated data.

---
## Cross-Source Technical Challenge Matrix

| Technical Dimension | Root Problem in Cloud / IoT Architectures | Operational Impact on the Twin | Concrete Example in the Vault | Primary References |
| :-- | :-- | :-- | :-- | :-- |
| **Compute & Infrastructure Cost** | Running coupled CFD/FEA solvers or photorealistic 3D environments continuously in the cloud requires dedicated HPC/GPU instances. | High operational expenditure (OpEx); limits continuous twin deployment to high-value assets. | **Living Heart** (4-chamber FEA simulation) and **BMW Omniverse** (GPU-heavy 3D collaboration). | Fuller et al. (2020); Rasheed et al. (2020); Baillargeon et al. (2014) |
| **Latency & Synchronization** | Network round-trip delay and jitter between physical edge sensors/actuators and centralized cloud regions. | State desynchronization; delayed control commands can destabilize fast physical processes. | DTC specifies synchronization at a *"specified frequency and fidelity"* rather than universal microsecond links. | DTC (2021); Fuller et al. (2020); Alcaraz & Lopez (2022) |
| **Data Quality & Scale ("Useful Data")** | High-frequency IIoT telemetry produces terabytes of raw time-series data containing sensor noise, missing packets, and outliers. | "Garbage in, garbage out": noisy inputs cause state-estimation drift and false predictive alerts. | **Virtual Singapore** requires nationwide geospatial and real-time dynamic ingestion pipelines. | Fuller et al. (2020); Rasheed et al. (2020); Shahat et al. (2021) |
| **Cybersecurity (Closed-Loop Attack Surface)** | Unauthenticated protocols, public brokers, or compromised cloud APIs expose both upward telemetry and downward actuation. | **Upward:** data poisoning corrupts AI models. **Downward:** rogue commands trigger unsafe physical actions. | **Classroom Demo** (`broker.hivemq.com`): any client knowing the topic can spoof CO2 or trigger `ventilar`. | Alcaraz & Lopez (2022); [[Demo - Gemelo digital del aula]] |
| **Data Privacy & Regulatory Compliance** | Centralizing sensitive personal, clinical, or critical-infrastructure telemetry in multi-tenant public clouds. | Legal barriers (e.g., GDPR, health data residency) and loss of stakeholder trust. | **Cardiac Digital Twins** require strict encryption, residency, and access control for patient CT/MRI data. | Fuller et al. (2020); Corral-Acero et al. (2020) |

---
## Conceptual Breakdown

### A. IT Infrastructure, HPC Demands and Cloud Economics
- **The compute bottleneck:** Fuller et al. (2020) identify *IT Infrastructure* as a foundational barrier: running continuous analytics, 3D visualization, and physics simulations requires high-performance GPUs and uninterrupted high-bandwidth networking.
- **Speed vs. fidelity trade-off:** As Rasheed et al. (2020) point out, traditional finite-element (FEA) or computational fluid dynamics (CFD) solvers can take hours or days to compute a single scenario on HPC clusters, making them too slow and costly to run continuously in the cloud for every serialized asset (*Digital Twin Instance*).
- **Legacy brownfield integration:** Industrial plants often run decades-old PLCs and SCADA systems that lack native cloud connectivity, requiring complex retrofitting before any cloud ingestion can begin.

### B. Latency, Jitter and the Synchronization Trade-Off
- **Cloud distance vs. control loops:** Sending telemetry to a distant cloud data center, running an optimization model, and returning an actuation setpoint introduces network latency and jitter. While acceptable for slow processes (e.g., building HVAC or hourly fleet diagnostics), it fails for millisecond-level safety interlocks in robotics or power grids.
- **Fit-for-purpose synchronization:** The Digital Twin Consortium (see [[Digital Twin and Digital Thread A Unified Architectural Approach]]) resolves this by defining synchronization around a **specified frequency and fidelity** matched to the use case, rather than demanding continuous zero-latency streaming for every variable.

### C. From Big Data to "Useful Data"
- **Noise and sparsity:** Rasheed et al. (2020) emphasize that physical sensors are subject to thermal noise, degradation, and communication dropouts, and cannot be placed at every internal point of an asset (such as inside a beating heart or a combustion chamber).
- **Filtering and storage overhead:** Fuller et al. (2020) stress the challenge of *Useful Data*: cloud ingestion pipelines must clean, synchronize, and compress raw telemetry in real time so that storage costs do not explode and predictive models are not poisoned by corrupted readings.

### D. Cybersecurity in the Bidirectional Loop
Alcaraz & Lopez (2022) demonstrate why cybersecurity is substantially more critical for a **Digital Twin** than for a traditional simulation or read-only **Digital Shadow** (see [[Differences (Digital Twin vs. Simulation vs. 3D Model)]]):
- **Physical-to-Virtual Threats (Upward Stream):** Attackers can spoof sensor readings or execute man-in-the-middle (MitM) attacks on IIoT protocols (MQTT, OPC-UA) to blind operators or poison machine-learning training sets.
- **Virtual-to-Physical Threats (Downward Stream):** Because the twin can actuate physical equipment, a compromise of the cloud platform or message broker allows attackers to inject unauthorized control setpoints directly into real machinery.
- **Direct link to our Demo ([[Demo - Gemelo digital del aula]]):** Our classroom demo illustrates this exact vulnerability. Because it uses a public broker (`broker.hivemq.com`) without authentication or per-device TLS client certificates, anyone who discovers the topic `uji-ccdt-podmanicacos/aula1/comandos` can send rogue `ventilar` or `parar` commands. Production cloud deployments (such as AWS IoT Core or Azure IoT Hub) mitigate this with mutual TLS (mTLS), X.509 device certificates, and strict per-topic access control lists (ACLs).
