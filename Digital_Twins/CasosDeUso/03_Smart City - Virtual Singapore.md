---
type: use_case
sector: Smart Cities / Urban Planning
organization: National Research Foundation, Singapore Land Authority, GovTech (Singapore)
year: Ongoing national programme
maturity: Descriptive / Simulation
tags:
  - use-case
  - digital-twins
  - smart-city
  - urban-planning
---
# [Use Case] Smart City - Virtual Singapore

> [!summary] Core Takeaway
> **Virtual Singapore** is a 3D digital replica of the whole country built on topographical and real-time, dynamic data. The government uses it as an authoritative platform to **simulate and test solutions to urban planning problems** before applying them in the real city. It is the reference example of a national-scale city digital twin.

## Context and problem
- Dense cities must plan housing, transport, energy and green space with little room for error.
- Decisions involve many agencies, companies and citizens, who need a shared, trusted view of the city.

## How the twin works
| Element | Implementation |
|---|---|
| Physical entity | The city-state of Singapore |
| Virtual entity | "A 3D digital replica of Singapore built on topographical as well as real-time, dynamic data" (Singapore Land Authority, n.d.) |
| Data link (physical → virtual) | Geospatial and topographical data plus real-time, dynamic data feeds |
| Data link (virtual → physical) | Simulations and virtual tests that inform planning and policy decisions |

## Goals and users (Singapore Land Authority, n.d.)
- Be "the country's authoritative platform that can be used in simulations and virtual tests of new solutions to urban planning problems".
- Act as a "critical enabler" of the Smart Nation initiative.
- Provide 3D city information to the public and a public-private innovation space for researchers.
- Co-led by the National Research Foundation, the Singapore Land Authority and the Government Technology Agency.

## Academic framing
- Batty (2018), in an editorial in *Environment and Planning B*, discusses what distinguishes a digital twin of a city from traditional urban models.
- Shahat et al. (2021) review city digital twins and propose a research agenda: more efficient data processing, including the city's **socio-economic components**, and tighter integration between the physical city and its digital counterpart.

## Maturity level (assessment)
**Descriptive and simulation-based:** the strength is a shared, accurate model for planning and "what-if" tests. Automatic control of city systems is not part of the public description.

## Relevance for Cloud Computing
- A national 3D model with real-time feeds requires **large-scale geospatial storage, data pipelines and access control** for many agencies and external users.
- A good example of a **platform (PaaS-like) model**: one shared twin on which many organizations build their own applications.

## Limitations
- Cities are socio-technical systems: modelling people's behaviour is much harder than modelling buildings (Shahat et al., 2021).
- The official page gives no quantitative results.

## References
Summaries: [[Singapore Land Authority - Virtual Singapore]] · [[Digital twins - Batty]] · [[City Digital Twin Potentials A Review and Research Agenda]]

- Singapore Land Authority. (n.d.). *Virtual Singapore*. Retrieved November 10, 2026, from https://www.sla.gov.sg/geospatial/gw/virtual-singapore
- Batty, M. (2018). Digital twins. *Environment and Planning B: Urban Analytics and City Science*, 45(5), 817–820. https://doi.org/10.1177/2399808318796416
- Shahat, E., Hyun, C. T., & Yeom, C. (2021). City Digital Twin Potentials: A Review and Research Agenda. *Sustainability*, 13(6), 3386. https://doi.org/10.3390/su13063386

## Linked notes
- [[Demo - Gemelo digital del aula]]
- [[00_MOC - Use Cases]]
