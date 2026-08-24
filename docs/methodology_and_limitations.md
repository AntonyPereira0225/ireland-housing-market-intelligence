# Methodology and Limitations

## Source data

The project uses two official CSO PxStat datasets:

- **HPM09** — Residential Property Price Index, monthly.
- **NDQ06** — New Dwelling Completions, quarterly.

## Cleaning methodology

Column names were standardised to Python-friendly names. Leading and trailing whitespace was removed from categorical fields. HPM09 month labels were converted to dates, and NDQ06 quarter labels were converted into year, quarter number and quarter-start fields.

HPM09 contained **2,960 missing values** in the numeric observation field. These were retained as missing because a missing price-index observation is not equivalent to a value of zero. NDQ06 contained no missing values. Duplicate rows and duplicate logical observation keys were checked and none were found.

## Quarterly alignment

The integrated market-intelligence table uses quarter-end HPM09 annual price growth for March, June, September and December. This is joined to quarterly NDQ06 completions using the quarter label.

The resulting common analytical period contains **62 quarterly observations**, from **2011 Q1 to 2026 Q2**.

## Dublin definition for supply

Dublin completions are defined as the sum of:

- Dublin City Council
- Fingal County Council
- South Dublin County Council
- Dún Laoghaire Rathdown County Council

Non-Dublin completions are calculated as Ireland total minus the Dublin total.

## Year-on-year supply growth

Completion growth is calculated against the same quarter one year earlier using a four-quarter percentage change. This avoids misleading comparisons caused by normal seasonality across adjacent quarters.

## Complete-year comparisons

Annual national completion totals are shown only where all four quarters are present. Therefore, **2026 is excluded from full-year comparisons** because the downloaded data currently runs only through Q2.

## Geographic limitation

The two source datasets do not provide property prices and completions at the same geographic grain. HPM09 provides national, Dublin, National excluding Dublin and selected regional/property-type indices. NDQ06 provides local-authority completions. The project therefore does not create a county-level property-price ranking or claim a directly matched local-authority price-versus-supply relationship.

## Scale limitation

Local-authority completion charts use absolute dwelling counts. They are not normalised by population, housing stock, land area or household formation. A larger completion total should not automatically be interpreted as better housing performance.

## Causality limitation

The project is descriptive market intelligence. Correlation or co-movement between price growth and completions does not establish causation. Factors such as interest rates, household income, migration, credit conditions, planning constraints and housing demand are outside the scope of the current two-dataset model.

## Dashboard validation

The Power BI dashboard was checked against Python outputs for the latest reporting period, latest housing-type mix, local-authority ranking and Dublin/non-Dublin series before being treated as final.
