from pathlib import Path
import pandas as pd


DATA_PATH = Path("data/processed/ndq06_clean.csv")


def main():
    df = pd.read_csv(DATA_PATH, parse_dates=["quarter_start"])
    latest_quarter = df["quarter"].max()

    print("=" * 70)
    print("LATEST NATIONAL HOUSING COMPLETIONS")
    print("=" * 70)

    national = df[
        (df["quarter"] == latest_quarter)
        & (df["local_authority"] == "Ireland")
        & (df["house_type"] == "All house types")
    ]

    print(f"\nLatest quarter: {latest_quarter}")
    print(national[["quarter", "local_authority", "house_type", "value"]].to_string(index=False))

    print("\n" + "=" * 70)
    print("LATEST COMPLETIONS BY HOUSE TYPE")
    print("=" * 70)

    house_type_mix = df[
        (df["quarter"] == latest_quarter)
        & (df["local_authority"] == "Ireland")
        & (df["house_type"] != "All house types")
    ][["house_type", "value"]].copy()

    total_latest = national["value"].iloc[0]
    house_type_mix["share_pct"] = (house_type_mix["value"] / total_latest * 100).round(2)
    print(house_type_mix.to_string(index=False))

    print("\n" + "=" * 70)
    print("TOP LOCAL AUTHORITIES — LATEST QUARTER")
    print("=" * 70)

    top_local_authorities = (
        df[
            (df["quarter"] == latest_quarter)
            & (df["house_type"] == "All house types")
            & (df["local_authority"] != "Ireland")
        ]
        .sort_values("value", ascending=False)[["local_authority", "value"]]
        .head(10)
    )
    print(top_local_authorities.to_string(index=False))

    print("\n" + "=" * 70)
    print("COMPLETE-YEAR NATIONAL COMPLETIONS")
    print("=" * 70)

    national_trend = df[
        (df["local_authority"] == "Ireland")
        & (df["house_type"] == "All house types")
    ][["quarter", "year", "value"]]

    quarters_per_year = national_trend.groupby("year")["quarter"].nunique().reset_index(name="quarter_count")
    complete_years = quarters_per_year[quarters_per_year["quarter_count"] == 4]["year"]
    annual_totals = (
        national_trend[national_trend["year"].isin(complete_years)]
        .groupby("year", as_index=False)["value"]
        .sum()
    )
    print(annual_totals.tail(10).to_string(index=False))

    print("\n" + "=" * 70)
    print("LATEST QUARTER VS SAME QUARTER LAST YEAR")
    print("=" * 70)

    latest_period = pd.Period(latest_quarter, freq="Q")
    prior_year_quarter = str(latest_period - 4)

    comparison = df[
        (df["local_authority"] == "Ireland")
        & (df["house_type"] == "All house types")
        & (df["quarter"].isin([prior_year_quarter, latest_quarter]))
    ][["quarter", "value"]]

    print(comparison.to_string(index=False))

    if len(comparison) == 2:
        previous_value = comparison.loc[comparison["quarter"] == prior_year_quarter, "value"].iloc[0]
        latest_value = comparison.loc[comparison["quarter"] == latest_quarter, "value"].iloc[0]
        yoy_growth = (latest_value - previous_value) / previous_value * 100
        print(f"\nYear-on-year change: {yoy_growth:.2f}%")


if __name__ == "__main__":
    main()
