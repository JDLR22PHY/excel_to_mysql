# 📊 Excel to MySQL Converter

This Python script allows you to read a spreadsheet, clean its column names to be compatible with SQL, and export it directly into a MySQL table using SQLAlchemy.

---

## 💡 What it does

- Loads an Excel sheet using `pandas`
- Cleans and standardizes column names:
  - Removes special characters
  - Converts to uppercase
  - Ensures no duplicate column names
- Uploads the data to a specified MySQL table using `to_sql()`

---

## 📦 Requirements

- Python 3.8+
- `pandas`
- `sqlalchemy`
- `mysql-connector-python`

Install dependencies:

```bash
pip install pandas sqlalchemy mysql-connector-python openpyxl
