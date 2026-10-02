# Mini Sales ETL Pipeline

A small Python Data Engineering project that demonstrates a complete ETL workflow using raw CSV sales data.

## Pipeline

Raw CSV
→ Extract
→ Transform
→ Clean
→ Aggregate
→ Load
→ Processed CSV + JSON Summary

## Features

- Extracts sales records from CSV
- Converts raw string values into appropriate data types
- Cleans customer and product fields
- Calculates order totals
- Aggregates revenue and item metrics
- Writes processed data to CSV
- Writes summary metrics to JSON
- Automated testing with pytest

## Technologies

- Python
- CSV
- JSON
- pytest
- Git

## Project Structure

```text
mini-sales-etl/
├── data/
│   ├── raw/
│   │   └── sales.csv
│   └── processed/
├── src/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
├── tests/
│   ├── test_extract.py
│   └── test_transform.py
├── main.py
├── requirements.txt
└── README.md