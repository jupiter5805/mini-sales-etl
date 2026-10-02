from src.transform import transform_sales, calculate_summary


def test_transform_sales_converts_types_and_calculates_total():
    records = [
        {
            "order_id": "1",
            "customer": " Ali ",
            "product": " Keyboard ",
            "quantity": "2",
            "unit_price": "50.00",
        }
    ]

    result = transform_sales(records)

    assert result == [
        {
            "order_id": 1,
            "customer": "Ali",
            "product": "Keyboard",
            "quantity": 2,
            "unit_price": 50.0,
            "total": 100.0,
        }
    ]


def test_transform_sales_returns_empty_list():
    assert transform_sales([]) == []


def test_calculate_summary():
    records = [
        {"quantity": 2, "total": 100.0},
        {"quantity": 1, "total": 50.0},
        {"quantity": 3, "total": 75.0},
    ]

    result = calculate_summary(records)

    assert result == {
        "total_orders": 3,
        "total_items_sold": 6,
        "total_revenue": 225.0,
    }


def test_calculate_summary_with_empty_records():
    result = calculate_summary([])

    assert result == {
        "total_orders": 0,
        "total_items_sold": 0,
        "total_revenue": 0,
    }
