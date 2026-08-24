# Data

This project uses official Central Statistics Office (CSO) PxStat datasets.

## Source files

Place downloaded CSV files locally in `data/raw/`.

Expected files:

- `HPM09.csv` — Residential Property Price Index, monthly
- `NDQ06.csv` — New Dwelling Completions, quarterly

The raw CSV files are intentionally excluded from Git version control through `.gitignore`. This keeps the repository lightweight and makes the workflow reproducible from the official source data.

## Current downloaded coverage

### HPM09

- January 2005 to June 2026
- 20,640 rows
- Columns:
  - `Statistic Label`
  - `Month`
  - `Type of Residential Property`
  - `UNIT`
  - `VALUE`

### NDQ06

- 2011 Q1 to 2026 Q2
- 7,936 rows
- Columns:
  - `STATISTIC Label`
  - `Quarter`
  - `Type of House`
  - `Local Authority`
  - `UNIT`
  - `VALUE`

Processed outputs created later in the project will be stored under `data/processed/` and will also be excluded from Git unless a small portfolio-ready extract is intentionally added.
