from pathlib import Path
import pandas as pd


RAW_DIR = Path("data/raw")
PROCESSED_DIR = Path("data/processed")

HPM09_PATH = RAW_DIR / "HPM09.csv"
NDQ06_PATH = RAW_DIR / "NDQ06.csv"


def clean_hpm09() -> pd.DataFrame:
    df = pd.read_csv(HPM09_PATH)

    df = df.rename(
        columns={
            "Statistic Label": "statistic",
            "Month": "month",
            "Type of Residential Property": "property_type",
            "UNIT": "unit",
            "VALUE": "value",
        }
    )

    text_columns = ["statistic", "month", "property_type", "unit"]
    for column in text_columns:
        df[column] = df[column].str.strip()

    df["date"] = pd.to_datetime(df["month"], format="%Y %B")
    df["year"] = df["date"].dt.year
    df["month_number"] = df["date"].dt.month
    df["month_name"] = df["date"].dt.month_name()

    duplicate_keys = df.duplicated(
        subset=["statistic", "month", "property_type"]
    ).sum()

    print(f"HPM09 duplicate observation keys: {duplicate_keys}")
    print(f"HPM09 missing values: {df['value'].isna().sum():,}")

    return df


def clean_ndq06() -> pd.DataFrame:
    df = pd.read_csv(NDQ06_PATH)

    df = df.rename(
        columns={
            "STATISTIC Label": "statistic",
            "Quarter": "quarter",
            "Type of House": "house_type",
            "Local Authority": "local_authority",
            "UNIT": "unit",
            "VALUE": "value",
        }
    )

    text_columns = [
        "statistic",
        "quarter",
        "house_type",
        "local_authority",
        "unit",
    ]
    for column in text_columns:
        df[column] = df[column].str.strip()

    df["year"] = df["quarter"].str[:4].astype(int)
    df["quarter_number"] = df["quarter"].str[-1].astype(int)
    df["quarter_start"] = pd.PeriodIndex(df["quarter"], freq="Q").to_timestamp()

    duplicate_keys = df.duplicated(
        subset=["quarter", "house_type", "local_authority"]
    ).sum()

    print(f"NDQ06 duplicate observation keys: {duplicate_keys}")
    print(f"NDQ06 missing values: {df['value'].isna().sum():,}")

    return df


def main() -> None:
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    hpm09 = clean_hpm09()
    ndq06 = clean_ndq06()

    hpm09.to_csv(PROCESSED_DIR / "hpm09_clean.csv", index=False)
    ndq06.to_csv(PROCESSED_DIR / "ndq06_clean.csv", index=False)

    print("\nCleaning complete.")
    print(f"HPM09 cleaned rows: {len(hpm09):,}")
    print(f"NDQ06 cleaned rows: {len(ndq06):,}")
    print("Files saved to data/processed/")


if __name__ == "__main__":
    main()
