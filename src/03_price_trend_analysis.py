from pathlib import Path
import pandas as pd


DATA_PATH = Path("data/processed/hpm09_clean.csv")


def main():
    df = pd.read_csv(DATA_PATH, parse_dates=["date"])

    annual_growth = df[
        df["statistic"]
        == "Percentage Change over 12 months for Residential Property Price Index"
    ].copy()

    selected_markets = [
        "National - all residential properties",
        "Dublin - all residential properties",
        "National excluding Dublin - all residential properties",
    ]

    annual_growth = annual_growth[
        annual_growth["property_type"].isin(selected_markets)
    ].dropna(subset=["value"])

    print("=" * 70)
    print("LATEST ANNUAL PROPERTY PRICE GROWTH")
    print("=" * 70)

    latest_date = annual_growth["date"].max()
    latest = annual_growth[
        annual_growth["date"] == latest_date
    ][["property_type", "value"]]

    print(f"\nLatest month: {latest_date.strftime('%B %Y')}\n")
    print(latest.to_string(index=False))

    print("\n" + "=" * 70)
    print("STRONGEST ANNUAL PRICE GROWTH")
    print("=" * 70)
    strongest = annual_growth.sort_values("value", ascending=False)[
        ["date", "property_type", "value"]
    ].head(10)
    print(strongest.to_string(index=False))

    print("\n" + "=" * 70)
    print("WEAKEST ANNUAL PRICE GROWTH")
    print("=" * 70)
    weakest = annual_growth.sort_values("value")[["date", "property_type", "value"]].head(10)
    print(weakest.to_string(index=False))


if __name__ == "__main__":
    main()
