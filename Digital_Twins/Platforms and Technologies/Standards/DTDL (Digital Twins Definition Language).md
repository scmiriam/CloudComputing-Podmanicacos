---
type: concept_note
topic: Standards
owner: Microsoft (open specification, GitHub)
latest_version: v4
sources:
  - "[[DTDL v4 Specification]]"
  - "[[Microsoft Learn - What is Azure Digital Twins]]"
tags:
  - digital-twins
  - standards
  - dtdl
  - modeling
---
# DTDL (Digital Twins Definition Language)

> [!summary] Core Takeaway
> A **JSON-LD language for describing twin models**: what properties, telemetry, commands and relationships an entity has. Microsoft created it and publishes it as an open specification. The current version is **v4** (`dtmi:dtdl:context;4`), but [[Azure Digital Twins]] still works with v2/v3.

## Key elements
| Element | Meaning | Classroom example |
|---|---|---|
| **Interface** | The model of a twin type, identified by a **DTMI** | `dtmi:uji:podmanicacos:Classroom;1` |
| **Property** | State that is stored (can be writable) | `ventilating` (true/false) |
| **Telemetry** | Stream of measurements, not stored | `co2`, `temperature` |
| **Command** | Action the twin can receive | `ventilate` |
| **Relationship** | Link to another twin | `isInBuilding` → Building |
| **Component** | Reuse of another interface inside this one | A `Thermostat` inside the room |

## Example: our classroom in DTDL
```json
{
  "@context": "dtmi:dtdl:context;3",
  "@id": "dtmi:uji:podmanicacos:Classroom;1",
  "@type": "Interface",
  "displayName": "Classroom",
  "contents": [
    { "@type": "Telemetry", "name": "co2",         "schema": "double" },
    { "@type": "Telemetry", "name": "temperature", "schema": "double" },
    { "@type": "Telemetry", "name": "humidity",    "schema": "double" },
    { "@type": "Property",  "name": "ventilating", "schema": "boolean", "writable": true },
    { "@type": "Command",   "name": "ventilate" },
    { "@type": "Relationship", "name": "isInBuilding",
      "target": "dtmi:uji:podmanicacos:Building;1" }
  ]
}
```
It uses v3 because that is what Azure Digital Twins accepts. With v4, only the `@context` changes (`dtmi:dtdl:context;4`) for a model this simple.

## Versions
| Version | Notes |
|---|---|
| v2 | Used by IoT Plug and Play and Azure Digital Twins |
| v3 | Recommended in Azure Digital Twins; adds extensions and arrays in properties |
| **v4** | Current spec. Max. 8 levels of nested schemas. Extensions: QuantitativeTypes v2 (units), MQTT v3, Overriding v2. Supported by Azure IoT Operations |

## Advantages
- Simple, readable and machine-processable (JSON-LD).
- Public industry ontologies (RealEstateCore for buildings, smart cities, energy grid) save modeling work.
- Covers both structure (graph) and behavior (telemetry/commands).
- Open tools exist outside Azure (e.g. parsers, and the open-source AGE Digital Twins project supports v2 to v4).

## Disadvantages
- Ecosystem **almost limited to Microsoft** (ADT, Azure IoT Operations). AWS and NVIDIA do not use it.
- It is not an ISO/IEC standard, so its future depends on a single vendor.
- Version gap: v4 is published, but ADT still only supports v2/v3.

## DTDL vs. other modeling languages
| | DTDL | [[Asset Administration Shell (AAS)]] | W3C WoT Thing Model ([[Eclipse Ditto]]) |
|---|---|---|---|
| Focus | Cloud twin graph | Industrial asset over its lifecycle | Web interface of a device |
| Body | Vendor (Microsoft) | IDTA / IEC | W3C |
| Format | JSON-LD | JSON / XML / RDF / AASX | JSON-LD |

## Linked notes
- [[Digital Twin Platforms and Standards - Comparative Audit (2026)]]
- [[Asset Administration Shell (AAS)]] (industrial alternative with ISO/IEC status)
