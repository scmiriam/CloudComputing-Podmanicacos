---
type: concept_note
topic: Standards
owner: OPC Foundation; IEC 62541
latest_version: 1.05.07 (core parts, April 2026)
sources:
  - "[[OPC Foundation - OPC UA Online Reference]]"
tags:
  - digital-twins
  - standards
  - opc-ua
  - industrial-communication
---
# OPC UA (Open Platform Communications Unified Architecture)

> [!summary] Core Takeaway
> The industrial **communication and information-modeling standard** (IEC 62541). It connects PLCs, machines and SCADA systems with the twin. In a digital twin it works at the **physical ↔ digital** boundary: it reads machine state and sends commands back, using a typed and secure information model.

## Key elements
- **Information model**: an *address space* of typed nodes (objects, variables, methods). The machine does not only send numbers: it says what each value means, its unit and its type.
- **Companion specifications**: shared models per sector (robots, machine tools, devices, and one for the AAS), written together with industry associations.
- **Transport**: client/server over TCP or HTTPS, and **PubSub** over MQTT/UDP for cloud and large-scale use.
- **Built-in security**: certificates, encryption and signing (*SecurityPolicies*, with ECC changes in 1.05.07).

## Example: a ventilation unit as an OPC UA address space
```
Objects
└── VentilationUnit_Aula1            (Object, type: VentilationUnitType)
    ├── CO2            = 812  ppm    (Variable, Double, EngineeringUnits = ppm)
    ├── Temperature    = 22.4 °C     (Variable, Double)
    ├── Running        = false       (Variable, Boolean)
    ├── Start()                      (Method)  ← command from the twin
    └── Stop()                       (Method)
```
A twin platform reads the variables (monitoring) and calls the methods (control). This is the same loop as our demo, but with types, units and security from the standard.

## OPC UA vs. MQTT
| | OPC UA | MQTT |
|---|---|---|
| What it is | Information model + communication + security | Only a lightweight message transport |
| Meaning of data | Built in (types, units, structure) | None; the payload is free (JSON, text...) |
| Typical place | Factory floor, PLCs | Sensors, IoT, cloud |
| Weight | Heavy | Very light |
| Combined | **OPC UA PubSub over MQTT** brings the OPC UA model to the cloud |

Our [[Demo - Gemelo digital del aula]] uses plain MQTT with JSON. In a real factory, OPC UA would replace it or run on top of it.

## Current status (Nov 2026)
- Specification **1.05.07** (April 2026) for the core parts. The parts are versioned separately.
- **IEC 62541:2026** editions published (e.g. Part 5, 4th edition).
- The OPC Foundation ends **1.03 certification at the end of 2026**. Vendors must move to 1.05.

## Advantages
- **De facto standard** in industry: supported by nearly all automation vendors.
- Combines transport, semantics and security in one standard.
- Supported by cloud platforms (e.g. AWS IoT SiteWise, Azure IoT Operations), so it connects to them.
- Open-source implementations (e.g. open62541 in C, already updated to 1.05.07).

## Disadvantages
- **Complex**: hundreds of pages of specification, steep learning curve.
- High resource usage on small devices compared to plain MQTT.
- Covers the machine, but not the full lifecycle of the asset (that is what AAS does).

## Linked notes
- [[Digital Twin Platforms and Standards - Comparative Audit (2026)]]
- [[Asset Administration Shell (AAS)]] (complementary: AAS can be exposed through OPC UA)
- [[Bidirectional Data Loop (Closed-Loop Feedback)]]
