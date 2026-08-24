# Ireland Housing Market Intelligence

**Python | pandas | CSO PxStat | Housing Analytics | Power BI | Data Storytelling**

## Project Overview

This portfolio project analyses the Irish residential housing market using official Central Statistics Office (CSO) datasets. It combines residential property price trends with new dwelling completions to examine how prices and housing supply have evolved over time and across geographic areas.

The project demonstrates an end-to-end analytics workflow:

**Official CSO data → Python profiling and cleaning → analytical datasets → exploratory analysis → Power BI dashboard → business interpretation**

## Business Problem

> How have Irish residential property prices and housing supply changed over time, how do Dublin and the rest of Ireland differ, and which local authorities account for the strongest recent housing delivery?

## Data Sources

### HPM09 — Residential Property Price Index

- Source: Central Statistics Office (CSO) PxStat
- Frequency: Monthly
- Current downloaded coverage: **January 2005 to June 2026**
- Rows: **20,640**
- Measures include:
  - Residential Property Price Index
  - 1-month percentage change
  - 3-month percentage change
  - 12-month percentage change
- Geography/property groupings include National, Dublin, National excluding Dublin, Dublin local-authority house indices and regional house indices.

### NDQ06 — New Dwelling Completions

- Source: Central Statistics Office (CSO) PxStat
- Frequency: Quarterly
- Current downloaded coverage: **2011 Q1 to 2026 Q2**
- Rows: **7,936**
- Housing types:
  - Single house
  - Scheme house
  - Apartment
  - All house types
- Geography: **31 local authorities plus Ireland total**

## Planned Business Questions

1. How has the national Residential Property Price Index changed since 2005?
2. How does price growth differ between Dublin and National excluding Dublin?
3. Which periods recorded the strongest and weakest annual price growth?
4. How have new dwelling completions changed since 2011?
5. Which local authorities currently deliver the most new housing?
6. How has the mix of apartments, scheme houses and single houses changed?
7. How do housing completions differ across Dublin and non-Dublin local authorities?
8. What market-pressure patterns emerge when price growth and housing supply are examined together?

## Important Scope Note

The two source datasets operate at different geographic levels. HPM09 provides national, Dublin, National excluding Dublin and selected regional/property-type price indices, while NDQ06 provides housing completions by local authority. Therefore, this project will **not** present a county-by-county property-price ranking unless an additional official county-level price dataset is added later.

Any combined "market pressure" metric developed in the project will be clearly labelled as a **portfolio-defined analytical indicator**, not an official CSO measure.

## Tools

- **Python** — data profiling, cleaning and exploratory analysis
- **pandas / NumPy** — transformation and validation
- **Matplotlib** — analytical validation charts
- **Power BI** — interactive dashboard and DAX measures
- **GitHub** — reproducible project documentation and version control

## Repository Structure

```text
ireland-housing-market-intelligence/
├── README.md
├── .gitignore
├── requirements.txt
├── data/
│   └── README.md
├── src/
│   └── 01_profile_datasets.py
├── docs/
│   └── project_plan.md
├── dashboard/
│   └── README.md
└── images/
    └── README.md
```

## Project Status

🟡 **In development — source datasets validated and Python profiling stage initialized.**

## Author

**Antony Pereira George**  
Dublin, Ireland  
Data Analyst | SQL | Python | Power BI

---

*This project uses official public CSO datasets and is intended for educational and portfolio purposes.*
