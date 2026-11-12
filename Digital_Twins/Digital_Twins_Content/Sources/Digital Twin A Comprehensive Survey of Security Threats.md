---
type: source
author: Cristina Alcaraz, Javier Lopez
organization: NICS Lab, University of Malaga
year: 2022
focus: Academic Survey / Cybersecurity Threats / Cloud-Edge-IIoT Attack Surface
url: https://doi.org/10.1109/COMST.2022.3171465
doi: 10.1109/COMST.2022.3171465
document_id: Alcaraz & Lopez
tags:
  - source
  - digital-twins
  - challenges
  - cybersecurity
  - cloud
  - edge
  - iiot
---

# [Source] - Digital Twin: A Comprehensive Survey of Security Threats (Alcaraz & Lopez, 2022)

- **Author/Entity:** Cristina Alcaraz & Javier Lopez (Network, Information and Computer Security Lab, University of Malaga)
- **Year:** 2022 (*IEEE Communications Surveys & Tutorials*, Vol. 24, No. 3, pp. 1475–1503)
- **Focus:** Threat taxonomy, attack surfaces, and defense mechanisms across the architectural layers of digital twins
- **Key Quote:**
  - *"Because a digital twin maintains a continuous bidirectional connection with its physical counterpart, a compromise in the virtual space can directly propagate to the physical infrastructure, and vice versa."*
- **Linked Notes:**
  - [[Challenges and Future Landscape of Digital Twins]]
  - [[Technical, Cloud and Security Challenges]]
  - [[Open Standards, Cloud-Native and Edge-Cloud Continuum]]

## Source Summary
A comprehensive cybersecurity survey analyzing how the convergence of IIoT, Edge/Cloud virtualization, and bidirectional closed-loop control creates unique security risks for digital twin deployments:

1. **Bidirectional Attack Amplification:**
   - Unlike offline simulations or read-only dashboards, an operational digital twin possesses a downward actuation channel. Poisoned telemetry (*physical-to-virtual*) can corrupt predictive models, while hijacked cloud/broker endpoints (*virtual-to-physical*) enable attackers to issue unauthorized actuation commands to physical machinery.
2. **Layered Threat Taxonomy:**
   - **Physical & Data Acquisition Layer:** Sensor spoofing, tampering, man-in-the-middle (MitM) interception on unauthenticated IIoT protocols (e.g., plaintext or public MQTT/OPC-UA topics), and denial-of-service (DoS) against edge gateways.
   - **Communication & Synchronization Layer:** Desynchronization attacks, packet delay/replay attacks that invalidate real-time state estimation, and unauthorized topic subscription/publication.
   - **Virtualization, Cloud & Storage Layer:** Multi-tenant cloud isolation breaches, unauthorized tampering with simulation parameters or historical digital thread repositories, and intellectual property theft of high-fidelity 3D/physics models.
   - **Analytics & Control Layer:** Adversarial machine learning (data poisoning and evasion attacks against predictive maintenance models) and rogue command injection.
3. **Architectural Countermeasures:**
   - Per-device cryptographic identity and mutual TLS (mTLS), fine-grained topic/API access control (RBAC/ABAC), zero-trust segmentation between edge and cloud tiers, anomaly detection on incoming telemetry, and human-in-the-loop safety interlocks for critical actuation.
