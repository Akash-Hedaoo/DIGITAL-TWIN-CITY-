import osmnx as ox
import geopandas as gpd
import pandas as pd
import os

DATA_FOLDER = "data"
CITY_NAME = "Pune, Maharashtra, India" # The same name from Task 1

print("Starting Task 4: Downloading healthcare locations for Pune...")

try:
    # --- 1. Get the city boundary polygon directly ---
    print(f"Geocoding boundary for {CITY_NAME}...")

    # This downloads the official administrative boundary for Pune
    gdf_city = ox.geocode_to_gdf(CITY_NAME)

    # Get the actual polygon geometry from the GeoDataFrame
    city_boundary = gdf_city.geometry.iloc[0] 
    print("Successfully got city boundary polygon.")

    # --- 2. Define what we're looking for ---
    # These are tags from OpenStreetMap for healthcare
    tags = {'amenity': ['hospital', 'clinic', 'doctors', 'pharmacy']}

    # --- 3. Download the data from OSM ---
    print("Downloading healthcare data from OpenStreetMap (OSM)...")
    # This function searches for all 'tags' within our 'city_boundary'
    gdf_healthcare = ox.features_from_polygon(city_boundary, tags)

    print(f"Found {len(gdf_healthcare)} total healthcare amenities.")

    # --- 4. Clean the data ---
    if gdf_healthcare.empty:
         print("No healthcare amenities found for the given tags in this area.")
         df_final = pd.DataFrame(columns=['name', 'amenity', 'latitude', 'longitude']) # Create empty dataframe
    else:
        # Keep only the columns we care about
        keep_cols = ['name', 'amenity', 'geometry']

        # Keep only columns that were actually found
        final_cols = [col for col in keep_cols if col in gdf_healthcare.columns]
        gdf_clean = gdf_healthcare[final_cols].copy()

        # Ensure we only process valid geometries
        gdf_clean = gdf_clean[gdf_clean.geometry.is_valid]

        # Filter for points or polygons (avoid lines)
        gdf_clean = gdf_clean[gdf_clean.geometry.type.isin(['Point', 'Polygon', 'MultiPolygon'])]

        # Get latitude and longitude from the 'geometry' column
        gdf_clean['latitude'] = gdf_clean.geometry.centroid.y
        gdf_clean['longitude'] = gdf_clean.geometry.centroid.x

        # Drop the complex 'geometry' column, as we have lat/lon now
        df_final = pd.DataFrame(gdf_clean.drop(columns='geometry'))

    # --- 5. Save the clean file ---
    output_path = os.path.join(DATA_FOLDER, "healthcare_pune_clean.csv")
    df_final.to_csv(output_path, index=False)

    print(f"\n--- SUCCESS! ---")
    print(f"Saved all healthcare locations to: {output_path}")
    print(df_final.head())

except Exception as e:
    print(f"\n--- ERROR ---")
    print(f"An error occurred: {e}")
    print("This can sometimes be a network issue. Please try running the script again.")

print("\n--- Task 4 Complete ---")