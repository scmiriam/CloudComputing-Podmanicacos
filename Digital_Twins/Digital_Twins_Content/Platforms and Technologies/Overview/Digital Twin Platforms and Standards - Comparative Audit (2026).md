---
type: concept_note
topic: Overview
audit_date: 2026-11-12
sources:
  - "[[Microsoft Learn - What is Azure Digital Twins]]"
  - "[[Microsoft Learn - Digital twin builder in Microsoft Fabric]]"
  - "[[Microsoft - Azure Digital Twins Pricing]]"
  - "[[AWS - What is AWS IoT TwinMaker]]"
  - "[[AWS - IoT TwinMaker Pricing]]"
  - "[[NVIDIA - Omniverse Launcher Deprecation]]"
  - "[[NVIDIA - Omniverse DSX Blueprint]]"
  - "[[NVIDIA - Omniverse Enterprise]]"
  - "[[Eclipse Ditto - Release 3.9.0]]"
  - "[[Eclipse Ditto - Release 3.9.8]]"
  - "[[Bosch IoT Things - Open Source Basis (Eclipse Ditto)]]"
  - "[[DTDL v4 Specification]]"
  - "[[OPC Foundation - OPC UA Online Reference]]"
  - "[[IDTA - AAS Specification Part 1 Metamodel]]"
  - "[[IDTA and Catena-X - Digital Battery Passport Guideline]]"
tags:
  - digital-twins
  - platforms
  - standards
  - cloud
  - comparison
---
# Digital Twin Platforms and Standards - Comparative Audit (2026)

> [!summary] Core Takeaway
> There is no "one platform" for digital twins. The landscape has three layers:
> - **Cloud twin services (PaaS):** [[Azure Digital Twins]] and [[AWS IoT TwinMaker]]. They model the twin as a **graph of entities** fed by IoT data. Both remain documented as available. Fabric Digital Twin Builder is a separate Microsoft preview; AWS service retirements are a lifecycle risk signal, not evidence that TwinMaker itself is discontinued.
> - **Simulation and visualization:** [[NVIDIA Omniverse]]. It focuses on physically accurate 3D (OpenUSD) and "physical AI", not on IoT state management. Since 2025 it is a **developer SDK** (Kit, libraries, blueprints), not a desktop app suite.
> - **Open source:** [[Eclipse Ditto]]. It is a self-hosted, vendor-neutral backend for twin state, with active releases (3.9.x in 2026). It is the base of a commercial service (Bosch IoT Things).
>
> **Standards** give the twin a common language and decide whether it can be moved between platforms: [[DTDL (Digital Twins Definition Language)]] for modeling, [[OPC UA]] for machine communication, and the [[Asset Administration Shell (AAS)]] for the industrial asset description.

---

## 1. Audit scope and method
- **Date:** status checked on **11 Nov 2026**, using official documentation, release notes and vendor pricing pages (see source notes). Secondary sources are only used for signals and are marked as such.
- **Criteria:** for each technology we look at (1) what it models, (2) how data comes in and goes back to the physical asset, (3) visualization, (4) lifecycle status, (5) cost model, (6) lock-in, and (7) real adopters.
- **Why it matters for Cloud Computing:** a digital twin is a typical cloud workload (event ingestion, storage, compute and visualization). The platform choice decides the **service model** (PaaS vs. self-hosted), the cost and the dependence on one provider.

## 2. Where each technology fits (reference architecture)
The same layers as in [[Key Components of a Digital Twin]], with the technology that covers each one:

```
 ┌─────────────────────────────────────────────────────────────────────┐
 │ 5. Applications / users      Dashboards, Grafana, Power BI, AI      │
 ├─────────────────────────────────────────────────────────────────────┤
 │ 4. Simulation & 3D           NVIDIA Omniverse (OpenUSD)             │
 │                              TwinMaker scenes · ADT 3D Scenes       │
 ├─────────────────────────────────────────────────────────────────────┤
 │ 3. Twin state & model        Azure Digital Twins · AWS IoT TwinMaker│
 │    (the "twin backend")      Eclipse Ditto                          │
 │    model language →          DTDL · AAS · W3C WoT Thing Model       │
 ├─────────────────────────────────────────────────────────────────────┤
 │ 2. Connectivity              MQTT · OPC UA (client/server, PubSub)  │
 │                              IoT Hub · IoT SiteWise · Ditto conn.   │
 ├─────────────────────────────────────────────────────────────────────┤
 │ 1. Physical asset            Sensors, PLCs, machines, buildings     │
 └─────────────────────────────────────────────────────────────────────┘
        ▲  data goes up (monitoring)       │  commands go down (control)
        └───────── bidirectional loop ─────┘
```

Key point: **no single product covers all layers**. Omniverse has no IoT backend; ADT, TwinMaker and Ditto have only basic 3D. Real solutions combine them, for example **Ditto or ADT for the state + Omniverse for the visualization**, connected with **OPC UA or MQTT**.

## 3. Platforms - comparative table

| | [[Azure Digital Twins]] | [[AWS IoT TwinMaker]] | [[NVIDIA Omniverse]] | [[Eclipse Ditto]] |
|---|---|---|---|---|
| **Type** | Managed PaaS (Microsoft) | Managed PaaS (AWS) | SDK, libraries and blueprints (NVIDIA) | Open-source framework (Eclipse Foundation, EPL-2.0) |
| **Main focus** | Twin graph of an environment (building, plant, city) | Operational twin + 3D scene + dashboards | High-fidelity 3D simulation, physical AI | Twin state and API for IoT devices |
| **Twin model** | DTDL v2/v3 (graph of models, twins, relationships) | Entity-component knowledge graph (JSON) | OpenUSD scene description | "Things" (JSON) + W3C WoT Thing Models |
| **Data in** | IoT Hub, REST, Azure Functions | Connectors: IoT SiteWise, Kinesis Video, custom Lambda | Connectors to CAD/BIM tools, sensor data via extensions | MQTT, AMQP, Kafka, HTTP |
| **Back to the asset** | Through IoT Hub / Functions (built by you) | Not native, through other AWS services | Not native | **Native**: desired properties and live messages |
| **Data stays where?** | Copied into the twin graph | **Referenced at the source** (no duplication) | USD stage (Nucleus/files) | Copied into Ditto (MongoDB) |
| **Visualization** | ADT Explorer, 3D Scenes Studio (still preview) | Scene composer (glTF) + Grafana plugin | Native RTX rendering (main strength) | Basic Explorer UI; needs external dashboard |
| **Status 2026** | Active, docs updated Aug 2026. No retirement notice. New Microsoft twin work goes to **Fabric digital twin builder (preview)** | Active in AWS docs. No official end-of-support notice found, but AWS retired sister services (IoT Events, IoT Analytics) | Active and growing. **Launcher deprecated Oct 2025**; DSX Blueprint GA Mar 2026 | Active. **3.9.8 (Oct 2026)**; latest release includes an important UI/SSO security fix |
| **Cost model** | Pay per use: operations, routed messages and query units (per million) | Standard mode: $0.05/entity/month, $1.50 per million API calls, $0.50 per 10,000 queries; or tiered bundle from $220/month | SDK free for development; **Omniverse Enterprise $4,500 per GPU/year** + GPU hardware/cloud | Free license; you pay your own infrastructure (Kubernetes + MongoDB) |
| **Lock-in** | High (Azure ecosystem), DTDL is open | High (AWS ecosystem), proprietary model | Medium: OpenUSD is open, runtime needs NVIDIA GPUs | Low: self-hosted, open APIs |
| **Real adopters** | Smart buildings and campuses on Azure; public DTDL ontologies (RealEstateCore, smart cities, energy grid) | Industrial customers on IoT SiteWise; Mendix partnership | BMW, Siemens, Schneider Electric, PTC, Jacobs, Cadence | **Bosch IoT Things** (commercial SaaS built on Ditto), Aloxy, Othermo |
| **Best for** | Smart buildings, spaces and graph queries on Azure | Industrial ops already on AWS IoT SiteWise | Factory planning, robotics, data centers (e.g. [[01_Manufacturing - BMW Group Virtual Factory]]) | Research, multi-cloud, avoiding vendor dependence |

## 4. Standards - comparative table

| | [[DTDL (Digital Twins Definition Language)]] | [[OPC UA]] | [[Asset Administration Shell (AAS)]] |
|---|---|---|---|
| **Question it answers** | *What* is the twin? (properties, telemetry, commands, relationships) | *How* do we talk to the machine? | *What do we know* about the asset during its whole life? |
| **Owner** | Microsoft (open spec on GitHub, CC BY 4.0) | OPC Foundation; also IEC 62541 | IDTA (Plattform Industrie 4.0); also IEC 63278 |
| **Formal standard?** | No (vendor specification) | Yes (IEC) | Yes (IEC, in progress) |
| **Latest version (Nov 2026)** | **v4** (`dtmi:dtdl:context;4`). Azure Digital Twins still uses v2/v3 | **1.05.07** (Apr 2026) for core parts; IEC 62541 2026 editions | IDTA Part 1 metamodel **v3.2**, Part 2 API v3.2.0; IEC 63278-4:2026 |
| **Format** | JSON-LD | Binary/JSON over TCP, HTTPS, PubSub (MQTT/UDP) | JSON, XML, RDF, AASX package; REST API |
| **Layer in the twin** | Cloud/model layer | Shop-floor/edge layer | Asset/information layer (between them) |
| **Ecosystem** | Mainly Azure (ADT, Azure IoT Operations) | Very broad: almost every PLC and industrial vendor | European industry; Eclipse BaSyx; Catena-X; EU Digital Product Passport |
| **Main weakness** | Single-vendor future | Complexity | Mostly European, many versions |

The three standards **complement each other** rather than compete. A typical industrial chain: the machine exposes its data through **OPC UA**, the asset is described with an **AAS** (which has an official OPC UA mapping), and a cloud twin service models the plant with **DTDL** or its own model.

## 5. Selection guide

| If your project... | Recommended option | Why |
|---|---|---|
| Already runs on Azure and models buildings or spaces | [[Azure Digital Twins]] (watch Fabric digital twin builder) | Graph + ontologies + Azure integration |
| Already uses AWS IoT SiteWise in a plant | [[AWS IoT TwinMaker]] | Uses the data where it is, Grafana dashboards included |
| Needs realistic 3D, physics or robot/AI training | [[NVIDIA Omniverse]] + a backend for the live data | Best simulation; not an IoT platform |
| Must avoid vendor lock-in, or is research/teaching | [[Eclipse Ditto]] | Open source, runs anywhere, native bidirectional control |
| Exchanges asset data between companies (supply chain, EU passport) | [[Asset Administration Shell (AAS)]] on any platform | IEC standard, Catena-X, Digital Product Passport |

## 6. Key findings of the audit
1. **Check lifecycle evidence separately from roadmap signals.** Azure Digital Twins and AWS IoT TwinMaker remain documented services, and this audit found no official retirement notice for either. Microsoft Fabric Digital Twin Builder is still a distinct preview, while AWS has lifecycle changes affecting other IoT services. Those facts justify checking roadmap, support and migration terms before adoption; they do not prove that ADT or TwinMaker is being retired.
2. **NVIDIA is moving from apps to "infrastructure".** Omniverse dropped its Launcher and desktop apps and is now sold as SDK, libraries and reference blueprints (DSX for AI factories). It is the leading option for 3D simulation, but it does not replace an IoT state backend.
3. **Open source reduces vendor dependence but transfers operations to the team.** Eclipse Ditto has an active release stream, a commercial version (Bosch IoT Things) and fits our [[Demo - Gemelo digital del aula]] architecture (MQTT broker → twin state → dashboard). Version 3.9.8 (Oct 2026) fixes a high-severity session-takeover issue affecting the UI/SSO setup and an MQTT reconnection message-loss bug: this is a practical reminder to keep self-hosted deployments patched. The team still operates the infrastructure and security updates.
4. **Standards are the protection against lock-in.** A twin modeled in DTDL, AAS or WoT and fed through OPC UA/MQTT can move between platforms. The industry is converging here: AAS ↔ OPC UA mappings, and AAS for the EU Digital Battery Passport with Catena-X (guideline Feb 2026).
5. **The market moves fast.** Omniverse changed its distribution model, Microsoft introduced a separate Fabric preview, and cloud vendors continue to change IoT product lifecycles. Recheck product status, supported standards, pricing and exit paths before committing.

## 7. Our demo on each platform
How the [[Demo - Gemelo digital del aula]] (CO₂/temperature/humidity sensor + "ventilate" command) would be built on each option:

| Piece of the demo | Azure Digital Twins | AWS IoT TwinMaker | Eclipse Ditto | NVIDIA Omniverse |
|---|---|---|---|---|
| Classroom model | DTDL interface `Classroom` (see example in [[DTDL (Digital Twins Definition Language)]]) | Entity `aula1` + time-series component | Thing `uji.podmanicacos:aula1` (see example in [[Eclipse Ditto]]) | USD model of the room |
| Sensor data in | IoT Hub → Azure Function → twin update | IoT SiteWise → connector | MQTT connection (same broker as the demo) | Extension that reads MQTT |
| "Ventilate" command | Function → IoT Hub cloud-to-device message | Not native | Desired property / live message | Not native |
| Dashboard | Power BI / custom web | Grafana | Our `index.html` | 3D view |
