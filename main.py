from src.extract import extract_sales
from src.transform import transform_sales, calculate_summary
from src.load import load_clean_sales, load_summary


def run_pipeline():
    raw_sales = extract_sales("data/raw/sales.csv")

    clean_sales = transform_sales(raw_sales)

    summary = calculate_summary(clean_sales)

    load_clean_sales(
        clean_sales,
        "data/processed/clean_sales.csv",
    )

    load_summary(
        summary,
        "data/processed/summary.json",
    )

    print("ETL pipeline completed successfully.")
    print(summary)


if __name__ == "__main__":
    run_pipeline()
