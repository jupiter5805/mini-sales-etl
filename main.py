from src.extract import extract_sales
from src.transform import transform_sales, calculate_summary


raw_sales = extract_sales("data/raw/sales.csv")
clean_sales = transform_sales(raw_sales)
summary = calculate_summary(clean_sales)

print("Sales Summary")
print("-------------")
print(f"Total Orders: {summary['total_orders']}")
print(f"Items Sold: {summary['total_items_sold']}")
print(f"Revenue: £{summary['total_revenue']}")
