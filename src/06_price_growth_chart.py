from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt


DATA_PATH = Path("data/processed/market_intelligence_quarterly.csv")
OUTPUT_DIR = Path("images")


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(DATA_PATH)
    df["quarter_date"] = pd.PeriodIndex(df["quarter"], freq="Q").to_timestamp()

    plt.figure(figsize=(12, 6))
    plt.plot(df["quarter_date"], df["dublin_price_growth_pct"], label="Dublin")
    plt.plot(df["quarter_date"], df["non_dublin_price_growth_pct"], label="National excluding Dublin")
    plt.axhline(0, linewidth=1)
    plt.title("Annual Residential Property Price Growth: Dublin vs Outside Dublin")
    plt.xlabel("Quarter")
    plt.ylabel("Annual price growth (%)")
    plt.legend()
    plt.tight_layout()

    output_path = OUTPUT_DIR / "price_growth_dublin_vs_non_dublin.png"
    plt.savefig(output_path, dpi=200, bbox_inches="tight")
    plt.show()
    print(f"Chart saved to {output_path}")


if __name__ == "__main__":
    main()
