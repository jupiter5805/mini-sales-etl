from src.extract import extract_sales
from src.transform import transform_sales


raw_sales = extract_sales("data/raw/sales.csv")
clean_sales = transform_sales(raw_sales)

for sale in clean_sales:
    print(sale)
