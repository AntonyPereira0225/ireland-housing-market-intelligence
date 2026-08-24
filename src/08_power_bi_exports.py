from pathlib import Path
import pandas as pd


SUPPLY_PATH = Path("data/processed/ndq06_clean.csv")
MARKET_PATH = Path("data/processed/market_intelligence_quarterly.csv")
OUTPUT_DIR = Path("data/power_bi")


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    supply = pd.read_csv(SUPPLY_PATH)
    market = pd.read_csv(MARKET_PATH)

    market.to_csv(OUTPUT_DIR / "market_intelligence_quarterly.csv", index=False)

    local_authorities = supply[
        (supply["house_type"] == "All house types")
        & (supply["local_authority"] != "Ireland")
    ][
        ["quarter", "year", "quarter_number", "quarter_start", "local_authority", "value"]
    ].copy()
    local_authorities = local_authorities.rename(columns={"value": "completions"})
    local_authorities.to_csv(OUTPUT_DIR / "local_authority_completions.csv", index=False)

    house_type_mix = supply[
        (supply["local_authority"] == "Ireland")
        & (supply["house_type"] != "All house types")
    ][
        ["quarter", "year", "quarter_number", "quarter_start", "house_type", "value"]
    ].copy()
    house_type_mix = house_type_mix.rename(columns={"value": "completions"})
    house_type_mix.to_csv(OUTPUT_DIR / "national_house_type_completions.csv", index=False)

    print("=" * 70)
    print("POWER BI EXPORTS CREATED")
    print("=" * 70)
    print(f"Market intelligence rows: {len(market):,}")
    print(f"Local authority rows: {len(local_authorities):,}")
    print(f"House type rows: {len(house_type_mix):,}")
    print("\nFiles saved to data/power_bi/")


if __name__ == "__main__":
    main()
