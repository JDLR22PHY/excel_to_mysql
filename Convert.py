"""
Convert Excel to MySQL Table
Author: Juan David Lamus Rincón

This script reads an Excel file, cleans and renames its columns to be SQL-safe,
and uploads it to a MySQL database using SQLAlchemy.

⚠️ Remember to replace the database credentials and Excel path with your actual values.
"""

import re
import pandas as pd
from sqlalchemy import create_engine

def clean_and_rename_columns(df):
    """
    1. Cleans column names: removes spaces, special characters, and normalizes to uppercase.
    2. Ensures unique names by adding numeric suffixes when needed.
    """
    # Step 1: Basic cleaning
    df.columns = [re.sub(r'[^a-zA-Z0-9_]', '', col.upper().replace(' ', '_')) for col in df.columns]

    # Step 2: Handle duplicates
    counter = {}
    new_columns = []
    
    for col in df.columns:
        base = re.sub(r'_\d+$', '', col)
        counter[base] = counter.get(base, 0) + 1
        new_col = f"{base}_{counter[base]}" if counter[base] > 1 else base
        new_columns.append(new_col)

    df.columns = new_columns
    return df

# --- Load Excel file ---
excel_path = "~/path/to/your/excel_file.xlsx"  # Change this
sheet = "Sheet1"
df = pd.read_excel(excel_path, sheet_name=sheet)
df = clean_and_rename_columns(df)

# --- MySQL Configuration ---
user = "your_mysql_user"
password = "your_mysql_password"
host = "localhost"
database = "your_database_name"

# --- Connect to MySQL ---
engine = create_engine(f"mysql+mysqlconnector://{user}:{password}@{host}/{database}")

# --- Export DataFrame to MySQL ---
df.to_sql(
    name="national_2008",
    con=engine,
    if_exists="replace",
    index=False
)

print("✅ Table exported successfully to MySQL!")
