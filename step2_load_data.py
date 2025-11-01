import pandas as pd
import os

# --- Define the data folder ---
DATA_FOLDER = "data"

print(f"Looking for data in: {os.path.abspath(DATA_FOLDER)}")
print("Attempting to load your key datasets...\n")

# --- List of your key files to load ---

# 1. CSV Files
csv_files = [
    "bus_stops.csv",
    "bus_routes.csv",
    "Metro-Station-Lat-Long.csv",
    "MH_AIR_QUALITY.csv",
    "Town Amenities for Pune District of Maharashtra.xls - Sheet1.csv"
]

for file in csv_files:
    # Build the full file path (e.g., "data/bus_stops.csv")
    file_path = os.path.join(DATA_FOLDER, file)

    try:
        df = pd.read_csv(file_path)
        print(f"--- SUCCESS: Loaded {file} ---")
        print(f"Columns: {df.columns.to_list()}")
        print(df.head())
        print("-" * 30 + "\n")
    except FileNotFoundError:
        print(f"--- ERROR: File not found: {file_path} ---")
        print("Please check the file name and make sure it's in the 'data' folder.\n")
    except Exception as e:
        print(f"--- ERROR reading {file}: {e} ---")
        print("This file might have encoding issues. We can fix that later.\n")

# 2. Excel File (.xlsm)
excel_file = "Population_Data.xlsm"
excel_path = os.path.join(DATA_FOLDER, excel_file) # Build the full path

try:
    # We must use 'openpyxl' as the engine for .xlsm files
    df_excel = pd.read_excel(excel_path, engine='openpyxl')

    print(f"--- SUCCESS: Loaded {excel_file} ---")
    print(f"Columns: {df_excel.columns.to_list()}")
    print(df_excel.head())
    print("-" * 30 + "\n")
except FileNotFoundError:
    print(f"--- ERROR: File not found: {excel_path} ---")
    print("Please check the file name and make sure it's in the 'data' folder.\n")
except Exception as e:
    print(f"--- ERROR reading {excel_file}: {e} ---")
    print("This file might be password-protected or have other issues.\n")

print("--- Task 2 Complete ---")