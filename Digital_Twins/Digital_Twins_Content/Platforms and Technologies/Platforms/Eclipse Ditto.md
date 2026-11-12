---
type: concept_note
topic: Platforms
vendor: Eclipse Foundation (open source, EPL-2.0)
category: Open-source twin backend
status_2026: Active; latest release 3.9.8 (2026-10-08)
sources:
  - "[[Eclipse Ditto - Release 3.9.0]]"
  - "[[Eclipse Ditto - Release 3.9.8]]"
  - "[[Bosch IoT Things - Open Source Basis (Eclipse Ditto)]]"
tags:
  - digital-twins
  - platforms
  - open-source
  - eclipse
  - iot
---
# Eclipse Ditto

> [!summary] Core Takeaway
> An open-source framework that turns IoT devices into **digital twins reachable through an API**. It stores the state of each *Thing* (reported and desired), controls access with *Policies*, and connects to MQTT, AMQP, Kafka or HTTP. It is **self-hosted and vendor-neutral**, so it can run on any cloud or on-premise. Bosch uses it as the base of its commercial service Bosch IoT Things.

## How it works
| Element | Implementation |
|---|---|
| Twin | **Thing**: a JSON document with *attributes* (static data) and *features* (state), optionally based on a **W3C WoT Thing Model** |
| Reported vs. desired | Each feature has `properties` (what the device reports) and `desiredProperties` (what the cloud wants) |
| Access control | **Policies** (fine-grained, multi-tenant from 3.9) |
| Data in/out | Connectivity service: MQTT, AMQP, Kafka, HTTP; WebSocket and Server-Sent Events for change notifications |
| Search | RQL queries over all twins (index in MongoDB) |
| Deployment | Microservices on Docker / Kubernetes (Helm chart 4.0), MongoDB as persistence |

## Example: our classroom as a Ditto Thing
```json
{
  "thingId": "uji.podmanicacos:aula1",
  "policyId": "uji.podmanicacos:aula1",
  "attributes": { "building": "Example building", "floor": 1 },
  "features": {
    "environment": {
      "properties": { "co2": 812, "temperature": 22.4, "humidity": 41 }
    },
    "ventilation": {
      "properties":        { "active": false },
      "desiredProperties": { "active": true }
    }
  }
}
```
The dashboard writes `desiredProperties.active = true`. Ditto sends the change to the device through the MQTT connection. When the device starts ventilating, it reports `properties.active = true`. This is the [[Bidirectional Data Loop (Closed-Loop Feedback)]] of our [[Demo - Gemelo digital del aula]], but with history, permissions and an API.

## Typical architecture
```
Devices ──MQTT──► Broker ◄──► Ditto Connectivity ──► Things + Policies (MongoDB)
                                                         │
                                         HTTP API / WebSocket / SSE
                                                         ▼
                                     Dashboards, apps, Grafana, Omniverse...
```
It is often used with other Eclipse IoT projects: **Hono** (device connectivity at scale) and **hawkBit** (software updates to devices).

## Current status (Nov 2026)
- **Ditto 3.9.0 (13 May 2026):** focused on *policies, multi-tenancy and reuse*. Added a W3C WoT Discovery **Thing Directory**, *Time Travel* in the Explorer UI and Java 25 support.
- **Latest release found: 3.9.8 (8 Oct 2026).** This security bugfix resolves CVE-2026-107503, a session-takeover vulnerability affecting the Ditto UI and Swagger UI OIDC/SSO configuration under specific conditions. It also fixes MQTT messages being lost immediately after a connection was established or re-established. Operators should upgrade; the release notes provide affected-version details and workarounds.
- **Adopters:** Bosch IoT Things (commercial SaaS powered by Ditto), Aloxy (industrial monitoring, mostly on-premise), Othermo (energy platform). In 2024 the Eclipse IoT working group counted 8 public adopters, and most contributions now come from outside Bosch.

## Operations and security
Ditto is software you operate: deploy its microservices, MongoDB and connectivity layer; configure identity, TLS, network boundaries and backups; monitor availability and apply upgrades. Open source removes a service subscription, but does not remove staffing or infrastructure costs. The 3.9.8 security advisory illustrates why patch management belongs in the total-cost comparison.

## Cost model
- License: free (EPL-2.0).
- Real cost: the infrastructure (Kubernetes cluster, MongoDB, broker) and the team that operates it.
- Alternative: use **Bosch IoT Things** as a managed version, paying for the service.

## Advantages
- **No vendor lock-in**: open source, runs on any infrastructure (multi-cloud, edge, on-premise).
- Built on open standards (W3C WoT, MQTT, JSON) and fits naturally with our demo (MQTT → twin → dashboard).
- Native **bidirectional** link: desired properties and live messages back to the device.
- Fine-grained, multi-tenant access control.

## Disadvantages
- **You run it yourself**: deployment, scaling, security and MongoDB backups are your job.
- No 3D visualization or built-in analytics, so it needs external tools (Grafana, Omniverse...).
- Small community compared to the hyperscalers, and no commercial support SLA by default.
- No graph query over relationships like [[Azure Digital Twins]]; relationships must be modeled with attributes.
