---
type: concept_note
topic: Platforms
vendor: NVIDIA
category: Simulation and 3D platform (SDK)
status_2026: Active; Launcher deprecated 2025-10-01; moved to Kit SDK, libraries and blueprints
sources:
  - "[[NVIDIA - Omniverse Launcher Deprecation]]"
  - "[[NVIDIA - Omniverse DSX Blueprint]]"
  - "[[NVIDIA - Omniverse Enterprise]]"
  - "[[NVIDIA - BMW Group Starts Global Rollout of NVIDIA Omniverse]]"
tags:
  - digital-twins
  - platforms
  - nvidia
  - omniverse
  - openusd
---
# NVIDIA Omniverse

> [!summary] Core Takeaway
> A platform for building **physically accurate 3D digital twins** based on **OpenUSD** and RTX rendering. In 2025-2026 it changed from an app suite (Launcher, USD Composer) into a **developer platform**: Kit SDK, libraries and reference *blueprints*. It is the leading option for simulation and "physical AI" (robotics, factories, data centers), but it is **not an IoT backend**.

## How it works
| Element | Implementation |
|---|---|
| Scene model | **OpenUSD** (Universal Scene Description), created by Pixar, now managed by the Alliance for OpenUSD (AOUSD) |
| Development | **Omniverse Kit SDK**, apps and templates distributed through GitHub and NGC |
| Data in | Connectors to CAD/BIM tools (Siemens, Autodesk, Bentley); live data through extensions |
| Rendering and physics | RTX real-time ray tracing, physics simulation, sensor simulation |
| Reference designs | Blueprints such as **Omniverse DSX** (AI factory twins, GA March 2026) |

## Why OpenUSD matters
Each engineering tool has its own file format (Revit for buildings, Process Simulate for robots, MicroStation for infrastructure). OpenUSD works as a **common scene language**. Each tool writes its own *layer*, and Omniverse combines them in one live scene without converting the files. This is how BMW combined data from three vendors in its virtual factory ([[01_Manufacturing - BMW Group Virtual Factory]]).

## From apps to platform (2025-2026)
| Before (until 2025) | Now (2026) |
|---|---|
| Omniverse Launcher installs ready-made apps | **Launcher deprecated** (1 Oct 2025) |
| USD Composer, USD Presenter for end users | Developers build their own apps with **Kit SDK** |
| Nucleus Workstation for collaboration | Hub Workstation Cache; Enterprise Nucleus Server via NGC |
| General "metaverse" positioning | **"Physical AI"**: robotics (Isaac), world models (Cosmos), AI factories (DSX) |

## Typical architecture of a twin with Omniverse
```
CAD / BIM tools ──► USD layers ──┐
                                 ▼
IoT backend (ADT, Ditto...) ──► Omniverse Kit app (live USD stage)
                                 │   RTX rendering + physics simulation
                                 ▼
             Streaming to browser / XR / AI training data (synthetic)
```
Omniverse gives the **"what if"** (simulation) and the visualization. The **"what is"** (live state) comes from another platform.

## Cost model
- **SDK and development:** free to download and develop with.
- **Omniverse Enterprise:** NVIDIA lists **$4,500 per GPU per year** (licensed per GPU since NVIDIA moved away from per-user licensing). Academic licenses are much cheaper. Resellers in Europe sell it for about €5,800 per GPU/year, bundled with NVIDIA AI Enterprise.
- **Hardware:** NVIDIA RTX GPUs, on-premise or rented in the cloud. This is usually the largest cost.

## Current status (Nov 2026)
- **Omniverse Launcher deprecated on 1 Oct 2025.** Its installers are no longer downloadable, and Nucleus Workstation is deprecated too. NVIDIA says that *"Omniverse itself is not going away"* (NVIDIA, 2025).
- **Omniverse DSX Blueprint** (GTC Mar 2026): twins of gigawatt-scale AI data centers. The twin is used to simulate heat and power before construction, and to operate the site afterwards. Partners include Siemens, Schneider Electric, PTC, Cadence and Jacobs (NVIDIA, 2026).
- NVIDIA now presents Omniverse as the base for **physical AI**, together with world models (Cosmos) and robotics (Isaac).

## Advantages
- **Best-in-class visual and physical fidelity** (RTX, physics, sensor simulation).
- Open, collaborative format (OpenUSD) that combines data from many engineering tools.
- Large industrial ecosystem (Siemens, PTC, Schneider, BMW).
- Can generate **synthetic data** to train AI models (robots, computer vision).

## Disadvantages
- Needs **NVIDIA GPUs** (hardware lock-in) and an Enterprise license for production use.
- Steep learning curve. Since the Launcher was removed, it is aimed at developers, not end users.
- Does not manage IoT state, devices or bidirectional control on its own. It needs a backend ([[Azure Digital Twins]], [[Eclipse Ditto]], etc.).
- Frequent product changes (apps deprecated in 2025) make it hard to rely on a specific tool.
