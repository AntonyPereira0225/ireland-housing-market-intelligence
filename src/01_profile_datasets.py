from pathlib import Path
import pandas as pd


RAW_DIR = Path("data/raw")
HPM09_PATH = RAW_DIR / "HPM09.csv"
NDQ06_PATH = RAW_DIR / "NDQ06.csv"


def profile_dataframe(name: str, df: pd.DataFrame) -> None:
    print("\n" + "=" * 70)
    print(name)
    print("=" * 70)
    print(f"Rows: {len(df):,}")
    print(f"Columns: {len(df.columns)}")
    print("\nColumn names:")
    for column in df.columns:
        print(f"- {column}")

    print("\nData types:")
    print(df.dtypes)

    print("\nMissing values:")
    print(df.isna().sum())

    print("\nDuplicate rows:")
    print(df.duplicated().sum())

    print("\nFirst 5 rows:")
    print(df.head())


def main() -> None:
    hpm09 = pd.read_csv(HPM09_PATH)
    ndq06 = pd.read_csv(NDQ06_PATH)

    profile_dataframe("HPM09 — Residential Property Price Index", hpm09)
    profile_dataframe("NDQ06 — New Dwelling Completions", ndq06)

    print("\n" + "=" * 70)
    print("Coverage checks")
    print("=" * 70)
    print(f"HPM09 first month: {hpm09['Month'].iloc[0]}")
    print(f"HPM09 last month:  {hpm09['Month'].iloc[-1]}")
    print(f"HPM09 property groups: {hpm09['Type of Residential Property'].nunique()}")
    print(f"HPM09 statistics: {hpm09['Statistic Label'].nunique()}")

    print(f"\nNDQ06 first quarter: {ndq06['Quarter'].iloc[0]}")
    print(f"NDQ06 last quarter:  {ndq06['Quarter'].iloc[-1]}")
    print(f"NDQ06 local authorities/geographies: {ndq06['Local Authority'].nunique()}")
    print(f"NDQ06 house types: {ndq06['Type of House'].nunique()}")


if __name__ == "__main__":
    main()
