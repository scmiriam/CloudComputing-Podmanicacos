---
type: concept_note
topic: Platforms
vendor: Amazon Web Services
category: Cloud PaaS
status_2026: Active in AWS docs; no official lifecycle notice found
sources:
  - "[[AWS - What is AWS IoT TwinMaker]]"
  - "[[AWS - IoT TwinMaker Pricing]]"
tags:
  - digital-twins
  - platforms
  - aws
  - iot
---
# AWS IoT TwinMaker

> [!summary] Core Takeaway
> An AWS service (GA April 2022) for **operational twins** of factories, buildings and plants. It connects an **entity-component knowledge graph** to data that stays where it already is (IoT SiteWise, Kinesis Video, custom connectors), and shows it in **3D scenes in Grafana**. It is still active, but its strategic future is unclear.

## How it works
| Element | Implementation |
|---|---|
| Workspace | Top-level container and security boundary, linked to an S3 bucket |
| Model | **Entities** (equipment, spaces, processes) + **components** (JSON) that add data and context |
| Properties | Static values, time-series references and relationships between entities |
| Data in | Built-in connectors for IoT SiteWise and Kinesis Video Streams; custom connectors through Lambda (e.g. Snowflake). Data is *referenced*, not copied |
| Visualization | Scene composer with glTF/GLB models and data *tags*; plugin for Grafana / Amazon Managed Grafana |

## Typical architecture
```
PLCs / sensors ──► IoT SiteWise (time series) ─┐
IP cameras     ──► Kinesis Video Streams ──────┤
Other sources  ──► Lambda connector ───────────┤
                                               ▼
                         IoT TwinMaker (knowledge graph + unified query)
                                               │
                                               ▼
                         Grafana / Amazon Managed Grafana (3D scene + panels)
```
The main idea is **"connect, don't copy"**. TwinMaker keeps the structure (entities and relationships) and asks each data source when it needs a value. This is different from [[Azure Digital Twins]] and [[Eclipse Ditto]], which store the state in the twin.

## Entity-component model
Based on the *entity component system* pattern from video games:
- **Entity** = a thing (pump, room, production line).
- **Component** = a piece of data or behavior added to it (alarm, temperature series, video feed, document).
- The same component type can be reused on many entities, and the default view is a hierarchy.

## Cost model (AWS, US East)
| Mode | What you pay |
|---|---|
| **Basic** | Only per million data API calls. No knowledge graph |
| **Standard** (recommended for new customers) | $0.05 per entity per month + $1.50 per million API calls + $0.50 per 10,000 queries |
| **Tiered bundle** | Fixed price per entity tier, 3-month commitment. Tier 1 (up to 1,000 entities): $220/month; Tier 2 (up to 5,000): $650/month |

SiteWise, Kinesis Video, S3, Lambda and Grafana are billed separately.

## Current status (Nov 2026)
- The AWS developer guide still lists the service as active, with no *maintenance* or *sunset* notice (AWS, 2026).
- **Risk signal:** AWS has retired related IoT services (IoT Events, IoT Analytics) and moved IoT FleetWise to maintenance in 2026. Some resellers say TwinMaker is discontinued, but there is **no official AWS notice** that confirms it. It should be checked again on AWS's *Lifecycle Changes* page.
- AWS's lifecycle stages: **Maintenance** (no new customers), **Sunset** (about 12 months to migrate) and **Full shutdown**.

## Advantages
- **No data duplication:** it queries data at its source through a unified query interface.
- Quick start for companies that already use IoT SiteWise.
- Built-in 3D visualization and dashboards (Grafana), including video feeds.
- Clear and predictable pricing (per entity or fixed tier).

## Disadvantages
- **Proprietary model** (not DTDL or AAS), so moving to another platform is hard.
- Strong dependence on other AWS services (S3, Lambda, SiteWise, Grafana).
- No native path back to the device: control has to be built with other services.
- Only basic 3D (web glTF), no physics simulation.
- Strategic risk because AWS is cutting back its IoT portfolio.
- AWS says it is not intended for critical or hazardous systems.

## Linked notes
- [[Digital Twin Platforms and Standards - Comparative Audit (2026)]]
- [[Azure Digital Twins]] (direct competitor)
- [[Key Components of a Digital Twin]]
- [[Maturity Levels (Arup and Madni Frameworks)]] (without native control, it stays at monitoring/descriptive levels unless extended)
