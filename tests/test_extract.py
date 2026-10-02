from src.extract import extract_sales


def test_extract_sales_returns_list_of_records(tmp_path):
    test_file = tmp_path / "sales.csv"

    test_file.write_text(
        "order_id,customer,product,quantity,unit_price\n"
        "1,Ali,Keyboard,2,50.00\n"
        "2,Sara,Mouse,1,20.00\n"
    )

    result = extract_sales(test_file)

    assert len(result) == 2
    assert result[0]["customer"] == "Ali"
    assert result[1]["product"] == "Mouse"


def test_extract_sales_returns_empty_list_for_empty_csv(tmp_path):
    test_file = tmp_path / "sales.csv"

    test_file.write_text(
        "order_id,customer,product,quantity,unit_price\n"
    )

    result = extract_sales(test_file)

    assert result == []
