# Project Plan — Ireland Housing Market Intelligence

## Objective

Build a reproducible analytics project that combines Irish residential property price trends with new housing supply data and communicates the results through Python analysis and a Power BI dashboard.

## Phase 1 — Data profiling and cleaning

- Validate source schemas and row counts
- Parse monthly and quarterly time fields
- Standardise column names
- Check missing values and duplicates
- Validate units and categorical values
- Create analysis-ready price and completions tables

## Phase 2 — Price analysis

- National Residential Property Price Index trend
- Dublin vs National excluding Dublin
- Annual growth trend
- Strongest and weakest growth periods
- House vs apartment comparisons where supported

## Phase 3 — Housing supply analysis

- National completion trend
- Local-authority ranking
- Dublin-area completions
- Housing-type mix
- Year-over-year completion growth

## Phase 4 — Combined market view

- Align price and supply series at a suitable time grain
- Compare periods of price growth with housing delivery
- Develop a clearly documented portfolio-defined market-pressure indicator only if the data supports it
- Avoid causal claims from observational data

## Phase 5 — Power BI

Planned dashboard components:

- Latest national RPPI and annual price growth KPIs
- Latest quarterly/new annual dwelling completion KPIs
- Long-run national property-price trend
- Dublin vs National excluding Dublin price-growth comparison
- Housing completions over time
- Local-authority completion ranking
- Housing-type mix
- Interactive time, geography and housing-type filters
- Key Insights panel

## Methodology safeguards

- HPM09 is an index dataset, not transaction-level sale-price data.
- NDQ06 measures completed new dwellings, not total housing stock or housing demand.
- Price and completion datasets have different geographic granularity.
- Observed relationships will be described as associations, not causation.
- Any custom score will be explicitly labelled as portfolio-defined and its formula documented.
