---
type: source
author: Eclipse Ditto project team
organization: Eclipse Foundation
year: 2026
focus: Security and maintenance release
document_id: Ditto398
url: https://eclipse.dev/ditto/release_notes_398.html
tags:
  - source
  - digital-twins
  - platforms
  - open-source
  - eclipse
  - security
---

# [Source] - Release notes 3.9.8 | Eclipse Ditto

- **Author/Entity:** Eclipse Ditto project
- **Date:** 8 October 2026
- **URL:** https://eclipse.dev/ditto/release_notes_398.html
- **Focus:** Security and maintenance release
- **Key Points:**
  - Fixes CVE-2026-107503, a session-takeover vulnerability in the Ditto UI and Swagger UI OIDC integration under the conditions described in the advisory.
  - Fixes MQTT messages lost immediately after a connection was (re)established.
  - Updates vulnerable dependencies; the release adds no new user-facing API features compared with 3.9.7.
- **Linked Notes:**
  - [[Eclipse Ditto]]
  - [[Digital Twin Platforms and Standards - Comparative Audit (2026)]]

## Source Summary
This patch is both a security update and a useful operational signal: self-hosting requires a process for tracking advisories and upgrading. The official notes list affected versions, severity, mitigations and the recommended update.
