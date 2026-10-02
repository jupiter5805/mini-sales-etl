import csv


def extract_sales(filepath):
    """
    Extract sales records from a CSV file.

    Args:
        filepath (str): Path to the CSV file.

    Returns:
        list[dict]: Sales records as dictionaries.
    """

    with open(filepath, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)
