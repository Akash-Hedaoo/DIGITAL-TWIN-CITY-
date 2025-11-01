import osmnx as ox
import networkx as nx
import time

# --- This is the only part you might need to change ---
CITY_NAME = "Pune, Maharashtra, India"
FILE_NAME = "pune_road_network.graphml"
# -----------------------------------------------------

print(f"Starting to download road network for {CITY_NAME}...")
print("This may take a few minutes...")

# Record the start time
start_time = time.time()

try:
    # Download the 'drive' network for the city
    G = ox.graph_from_place(CITY_NAME, network_type='drive')
    
    # Record the end time
    end_time = time.time()
    
    print("\n--- Download Success! ---")
    print(f"Time taken: {end_time - start_time:.2f} seconds")
    
    # See how big the graph is
    print(f"Graph has {len(G.nodes)} nodes (intersections).")
    print(f"Graph has {len(G.edges)} edges (roads).")

    # Save the graph to a file to use later
    ox.save_graphml(G, filepath=FILE_NAME)
    
    print(f"\nSuccessfully saved the map to: {FILE_NAME}")
    print("--- Task 1 Complete ---")

except Exception as e:
    print(f"\n--- AN ERROR OCCURRED ---")
    print(f"Error: {e}")
    print("Please copy this error message and send it to me.")