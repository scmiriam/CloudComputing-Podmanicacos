---
type: concept_note
topic: Platforms
vendor: Microsoft
category: Cloud PaaS
status_2026: Active (no retirement notice); Fabric digital twin builder in preview
sources:
  - "[[Microsoft Learn - What is Azure Digital Twins]]"
  - "[[Microsoft Learn - Digital twin builder in Microsoft Fabric]]"
  - "[[Microsoft - Azure Digital Twins Pricing]]"
  - "[[DTDL v4 Specification]]"
tags:
  - digital-twins
  - platforms
  - azure
  - dtdl
---
# Azure Digital Twins

> [!summary] Core Takeaway
> A Microsoft PaaS that models an environment as a **graph of twins** described in [[DTDL (Digital Twins Definition Language)]], kept up to date with IoT Hub data and queried with a SQL-like language. It is still active, but Microsoft is putting its new digital twin work into **digital twin builder in Microsoft Fabric** (preview), which is a different product.

## How it works
| Element | Implementation |
|---|---|
| Model | DTDL v2/v3 *models* (e.g. Building, Floor, Elevator); public industry ontologies (RealEstateCore for buildings, smart cities, energy grid) |
| Twin | Instances of models connected by relationships, forming a **twin graph** |
| Data in | IoT Hub (device twins), REST API, Logic Apps, Azure Functions for processing logic |
| Data out | *Event routes* to Event Hubs, Event Grid and Service Bus; *data history* to Azure Data Explorer |
| Query | Query API with a SQL-like language over properties, relationships and models |
| Visualization | Azure Digital Twins Explorer (graph); 3D Scenes Studio (**still preview**) |

## Typical architecture
```
Devices ──► IoT Hub ──► Azure Function ──► Azure Digital Twins (twin graph)
                                                 │
                    ┌────────────────────────────┼───────────────────────┐
                    ▼                            ▼                       ▼
            Event Grid / Event Hubs      Data history → ADX       Explorer / 3D Scenes
            (Logic Apps, apps)           (time series, KQL)        / custom apps
```
The service stores the **current state** and the relationships. History, processing logic and the path back to the device (cloud-to-device messages) are built with other Azure services. ADT is the **center of a solution, not the whole solution**.

## Example: query on the twin graph
"Rooms on floor 1 with CO₂ above 1,000 ppm":
```sql
SELECT room FROM DIGITALTWINS floor
JOIN room RELATED floor.contains
WHERE floor.$dtId = 'Floor1' AND room.co2 > 1000
```
This is the key strength: questions about **structure + state** at the same time, which a time-series database cannot answer easily.

## Cost model
Pay per use, with three meters (Microsoft, 2026):
- **Operations:** each API call, metered in 1 KB steps of the response.
- **Messages:** events routed to Event Grid, Event Hubs or Service Bus, in 1 KB steps.
- **Query units:** cost of each query (returned as `query-charge` in the response).

Exact prices vary by region and must be checked with the Azure pricing calculator. IoT Hub, Functions and Data Explorer are billed separately.

## Current status (Nov 2026)
- The official overview was updated in August 2026 and has no retirement notice (Microsoft Learn, 2026).
- Microsoft points out that ADT is *different* from **digital twin builder (preview)** in Fabric Real-Time Intelligence. That tool is low-code, uses ontologies and stores the data in OneLake. It was first shown at Build 2025 and has no GA date yet (Microsoft Learn, 2026b).
- Signal of change: Microsoft retires Azure IoT Central on 20 Sep 2029 and directs customers to IoT services integrated with Fabric.

| | Azure Digital Twins | Digital twin builder (Fabric) |
|---|---|---|
| Users | Developers (APIs, SDKs) | Business and operations users (low-code) |
| Model | DTDL | Ontology in Fabric |
| Storage | Twin graph in the service | OneLake (lakehouse) |
| Status | GA, mature | Preview |

## Advantages
- Expressive **graph model** with relationships and a query API, good for spaces (buildings, campuses, cities).
- Uses an open modeling language (DTDL) and public ontologies.
- Deep integration with the Azure stack (IoT Hub, Functions, Data Explorer, Event Grid).
- Fully managed: no servers, scaling or patching for the user.

## Disadvantages
- **Vendor lock-in** to Azure; the twin graph cannot be exported directly to other clouds.
- Weak native visualization (3D Scenes Studio has been in preview for years).
- Uncertain long-term roadmap while Fabric becomes the main focus.
- Only supports DTDL v2/v3, even though DTDL v4 exists.
- A complete solution needs several paid services, so the total cost is hard to estimate.

## Linked notes
- [[Digital Twin Platforms and Standards - Comparative Audit (2026)]]
- [[AWS IoT TwinMaker]] (direct competitor)
- [[03_Smart City - Virtual Singapore]] (the kind of space-level twin that ADT targets)
- [[Hierarchical Types (Component, Asset, System, Process)]] (the twin graph naturally represents this hierarchy)
