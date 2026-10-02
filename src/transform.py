def transform_sales(records):
    """
    Clean and transform raw sales records.

    Converts numeric fields from strings and calculates
    the total value of each order.
    """

    transformed_records = []

    for record in records:
        quantity = int(record["quantity"])
        unit_price = float(record["unit_price"])

        transformed_records.append(
            {
                "order_id": int(record["order_id"]),
                "customer": record["customer"].strip(),
                "product": record["product"].strip(),
                "quantity": quantity,
                "unit_price": unit_price,
                "total": round(quantity * unit_price, 2),
            }
        )

    return transformed_records


def calculate_summary(records):
    """
    Calculate summary metrics from transformed sales records.
    """

    total_orders = len(records)
    total_items_sold = sum(record["quantity"] for record in records)
    total_revenue = round(sum(record["total"] for record in records), 2)

    return {
        "total_orders": total_orders,
        "total_items_sold": total_items_sold,
        "total_revenue": total_revenue,
    }
