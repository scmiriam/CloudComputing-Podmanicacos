---
type: concept_note
topic: Standards
owner: Industrial Digital Twin Association (IDTA); IEC 63278
latest_version: IDTA Part 1 Metamodel v3.2 / Part 2 API v3.2.0 (2026)
sources:
  - "[[IDTA - AAS Specification Part 1 Metamodel]]"
  - "[[IDTA and Catena-X - Digital Battery Passport Guideline]]"
tags:
  - digital-twins
  - standards
  - aas
  - industry4-0
---
# Asset Administration Shell (AAS)

> [!summary] Core Takeaway
> The **standardized digital twin of Industry 4.0**. Each physical asset gets a "shell" with **submodels** (nameplate, technical data, documentation, carbon footprint...) in an interoperable format. Plattform Industrie 4.0 created it; today the **IDTA** maintains it and it is being standardized as **IEC 63278**. It is also the main candidate for the EU **Digital Product Passport**.

## Key elements
- **AAS** → identifies the asset → contains **Submodels** based on public IDTA templates.
- Formats: JSON, XML, RDF and the **AASX** package. **REST API** (Part 2) for "active" twins.
- Reference open-source implementation: **Eclipse BaSyx**. There is also an official OPC UA mapping.

## Example: structure of an AAS for a ventilation unit
```
AAS  "VentilationUnit_Aula1"          (globalAssetId: unique URI of the asset)
├── Submodel  Digital Nameplate        manufacturer, model, serial number, year
├── Submodel  Technical Data           max. airflow, power, noise level
├── Submodel  Handover Documentation   manual, certificates (PDF)
├── Submodel  Carbon Footprint         kg CO₂e of production and use
└── Submodel  Operational Data         live CO₂, running state (linked to OPC UA / MQTT)
```
Each submodel follows a **public template** with semantic IDs, so another company's software can read it without a custom integration.

## Three types of AAS
| Type | What it is | Example |
|---|---|---|
| **Type 1 - passive** | A file (AASX) exchanged between companies | The manufacturer sends the AASX with the machine |
| **Type 2 - reactive** | Served through the REST API, answers queries | AAS server in the factory |
| **Type 3 - proactive** | Acts by itself, negotiates with other AAS | Research stage (Industry 4.0 agents) |

These types roughly follow the idea of increasing autonomy in [[Levels of Autonomy (Roles and Automation)]].

## Current status (Nov 2026)
- IDTA specifications **v3.2** (Part 1 Metamodel, Part 2 API), published in 2026.
- **IEC 63278-4:2026** (applications of the AAS) published. Other parts of the series are still in progress.
- **Digital Battery Passport:** in Feb 2026, IDTA, Catena-X and the Battery Pass Consortium published a guideline that uses AAS to meet the EU Battery Regulation, with seven submodel templates.
- IDTA presents AAS as the data format for **Catena-X and Factory-X** data spaces and as ready for the EU Digital Product Passport (2026).

## Advantages
- **Vendor-neutral international standard** (IEC), backed by German and European industry.
- Covers the **whole lifecycle** of the asset, not only operation. See [[Digital Twin vs. Digital Thread]].
- Reusable submodel templates make exchange between companies easier.
- **Regulatory driver**: the EU Digital Product Passport will make it necessary in some sectors (batteries first).

## Disadvantages
- Adoption is mostly **European and industrial**; little support in the hyperscalers' native services.
- Complex metamodel. Templates are still growing, and versions change often (3.0 → 3.1 → 3.2).
- It describes the asset, but it does not include real-time communication or simulation (it relies on OPC UA, MQTT, etc.).

## Linked notes
- [[Digital Twin Platforms and Standards - Comparative Audit (2026)]]
- [[OPC UA]] · [[DTDL (Digital Twins Definition Language)]]
- [[ISO 23247-1 Digital twin framework for manufacturing]]
- [[Lifecycle Types (Prototype, Instance, Aggregate)]]
