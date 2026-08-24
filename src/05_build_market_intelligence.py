from pathlib import Path
import pandas as pd


PRICE_PATH = Path("data/processed/hpm09_clean.csv")
SUPPLY_PATH = Path("data/processed/ndq06_clean.csv")
OUTPUT_PATH = Path("data/processed/market_intelligence_quarterly.csv")

DUBLIN_AUTHORITIES = [
    "Dublin City Council",
    "Fingal County Council",
    "South Dublin County Council",
    "Dún Laoghaire Rathdown County Council",
]


def prepare_price_data() -> pd.DataFrame:
    df = pd.read_csv(PRICE_PATH, parse_dates=["date"])

    annual_growth_stat = (
        "Percentage Change over 12 months for Residential Property Price Index"
    )
    selected_markets = [
        "Dublin - all residential properties",
        "National excluding Dublin - all residential properties",
    ]

    price = df[
        (df["statistic"] == annual_growth_stat)
        & (df["property_type"].isin(selected_markets))
        & (df["date"].dt.month.isin([3, 6, 9, 12]))
    ].copy()

    price["quarter"] = price["date"].dt.to_period("Q").astype(str)

    return (
        price.pivot(index="quarter", columns="property_type", values="value")
        .reset_index()
        .rename(
            columns={
                "Dublin - all residential properties": "dublin_price_growth_pct",
                "National excluding Dublin - all residential properties": "non_dublin_price_growth_pct",
            }
        )
    )


def prepare_supply_data() -> pd.DataFrame:
    df = pd.read_csv(SUPPLY_PATH)
    all_homes = df[df["house_type"] == "All house types"].copy()

    national = all_homes[all_homes["local_authority"] == "Ireland"][["quarter", "value"]].rename(
        columns={"value": "ireland_completions"}
    )

    dublin = (
        all_homes[all_homes["local_authority"].isin(DUBLIN_AUTHORITIES)]
        .groupby("quarter", as_index=False)["value"]
        .sum()
        .rename(columns={"value": "dublin_completions"})
    )

    supply = national.merge(dublin, on="quarter", how="left")
    supply["non_dublin_completions"] = supply["ireland_completions"] - supply["dublin_completions"]
    supply = supply.sort_values("quarter")

    supply["dublin_completions_yoy_pct"] = supply["dublin_completions"].pct_change(4).mul(100).round(2)
    supply["non_dublin_completions_yoy_pct"] = supply["non_dublin_completions"].pct_change(4).mul(100).round(2)
    return supply


def main():
    market = prepare_supply_data().merge(prepare_price_data(), on="quarter", how="inner")
    market.to_csv(OUTPUT_PATH, index=False)

    print("=" * 90)
    print("LATEST QUARTERLY MARKET INTELLIGENCE")
    print("=" * 90)
    print(market.tail(8).to_string(index=False))

    latest = market.iloc[-1]
    print("\n" + "=" * 90)
    print("LATEST QUARTER")
    print("=" * 90)
    print(f"Quarter: {latest['quarter']}")
    print(f"Dublin price growth: {latest['dublin_price_growth_pct']:.2f}%")
    print(f"Non-Dublin price growth: {latest['non_dublin_price_growth_pct']:.2f}%")
    print(f"Dublin completions: {int(latest['dublin_completions']):,}")
    print(f"Non-Dublin completions: {int(latest['non_dublin_completions']):,}")
    print(f"Dublin completions YoY: {latest['dublin_completions_yoy_pct']:.2f}%")
    print(f"Non-Dublin completions YoY: {latest['non_dublin_completions_yoy_pct']:.2f}%")
    print("\nSaved combined dataset to data/processed/market_intelligence_quarterly.csv")


if __name__ == "__main__":
    main()
