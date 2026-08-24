# Data

The project uses official Central Statistics Office (CSO) PxStat data.

## Raw source files

Place the downloaded CSV files in `data/raw/` using these filenames:

- `HPM09.csv` — Residential Property Price Index
- `NDQ06.csv` — New Dwelling Completions

Raw files are not committed to the repository. This keeps the repository lightweight and encourages reproducible retrieval from the official source.

## Generated folders

The Python workflow creates:

- `data/processed/hpm09_clean.csv`
- `data/processed/ndq06_clean.csv`
- `data/processed/market_intelligence_quarterly.csv`
- `data/power_bi/market_intelligence_quarterly.csv`
- `data/power_bi/local_authority_completions.csv`
- `data/power_bi/national_house_type_completions.csv`

Run the scripts in numerical order from the repository root.
