import pandas as pd
import os

DATA_FOLDER = "data"
print("Starting Task 3: Preprocessing Data...\n")

try:
    # --- 1. Clean Bus Stops ---
    bus_stops_path = os.path.join(DATA_FOLDER, "bus_stops.csv")
    df_bus = pd.read_csv(bus_stops_path)

    # Select only the columns we need
    keep_cols_bus = ['stop_id', 'stop_name', 'stop_lat', 'stop_lon']
    df_bus_clean = df_bus[keep_cols_bus]

    # Save the new clean file
    df_bus_clean.to_csv(os.path.join(DATA_FOLDER, "bus_stops_clean.csv"), index=False)
    print("SUCCESS: Created 'bus_stops_clean.csv'")

except Exception as e:
    print(f"ERROR cleaning bus_stops.csv: {e}")

try:
    # --- 2. Clean Metro Stations ---
    metro_path = os.path.join(DATA_FOLDER, "Metro-Station-Lat-Long.csv")
    df_metro = pd.read_csv(metro_path)

    # Rename the columns with spaces
    rename_cols_metro = {'Lat ': 'latitude', 'Long ': 'longitude', 'Station Name': 'station_name'}
    df_metro_clean = df_metro.rename(columns=rename_cols_metro)

    df_metro_clean.to_csv(os.path.join(DATA_FOLDER, "metro_stations_clean.csv"), index=False)
    print("SUCCESS: Created 'metro_stations_clean.csv'")

except Exception as e:
    print(f"ERROR cleaning Metro-Station-Lat-Long.csv: {e}")

try:
    # --- 3. Clean Air Quality (Filter for Pune) ---
    aqi_path = os.path.join(DATA_FOLDER, "MH_AIR_QUALITY.csv")
    df_aqi = pd.read_csv(aqi_path)

    # Filter the DataFrame to only get rows where city is 'Pune'
    df_aqi_clean = df_aqi[df_aqi['city'] == 'Pune'].copy()

    df_aqi_clean.to_csv(os.path.join(DATA_FOLDER, "aqi_pune_clean.csv"), index=False)
    print(f"SUCCESS: Created 'aqi_pune_clean.csv' (Found {len(df_aqi_clean)} rows for Pune)")

except Exception as e:
    print(f"ERROR cleaning MH_AIR_QUALITY.csv: {e}")

try:
    # --- 4. Clean Population Data (Filter and Select) ---
    pop_path = os.path.join(DATA_FOLDER, "Population_Data.xlsm")
    df_pop = pd.read_excel(pop_path, engine='openpyxl')

    # Filter for Pune District
    df_pop_pune = df_pop[df_pop['District_Name'] == 'Pune'].copy()

    # Select only the columns we need
    keep_cols_pop = ['Level', 'Name', 'Total/Rural/Urban', 'Total Population Person', 'Total Population Male', 'Total Population Female']
    df_pop_clean = df_pop_pune[keep_cols_pop]

    df_pop_clean.to_csv(os.path.join(DATA_FOLDER, "population_pune_clean.csv"), index=False)
    print(f"SUCCESS: Created 'population_pune_clean.csv' (Found {len(df_pop_clean)} rows for Pune)")

except Exception as e:
    print(f"ERROR cleaning Population_Data.xlsm: {e}")

print("\n--- Preprocessing Task 3 Complete ---")