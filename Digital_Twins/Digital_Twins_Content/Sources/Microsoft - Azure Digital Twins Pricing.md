---
type: source
author: Microsoft
organization: Microsoft
year: 2026
focus: Pricing / Cost model
document_id: AzureADTPricing
url: https://azure.microsoft.com/en-us/pricing/details/digital-twins/
tags:
  - source
  - digital-twins
  - platforms
  - azure
  - pricing
  - sec-platforms
---

# [Source] - Azure Digital Twins Pricing | Microsoft Azure

- **Author/Entity:** Microsoft Azure
- **Date:** consulted 11 Nov 2026
- **URL:** https://azure.microsoft.com/en-us/pricing/details/digital-twins/
- **Focus:** Cost model
- **Key Points:**
  - Three meters: **operations**, **messages** and **query units**, each priced per million.
  - Operations are metered in 1 KB steps of the response body; messages in 1 KB steps of the payload routed to Event Grid, Event Hubs or Service Bus.
  - Query cost appears as `query-charge` in each Query API response.

## Source Summary
1. **Model:** pure pay per use, with no fixed fee per twin.
2. **Caveat:** the public page loads prices dynamically by region; exact USD values must be taken from the Azure pricing calculator.
