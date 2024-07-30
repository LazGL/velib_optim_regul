import pandas as pd
import networkx as nx
from haversine import haversine
from tqdm import tqdm

def load_data(file_path):
    """Load the data from a CSV file."""
    return pd.read_csv(file_path)

def create_graph(df):
    """Create a graph from the dataframe."""
    G = nx.Graph()
    
    # Add nodes
    for _, row in tqdm(df.iterrows(), desc="Adding nodes"):
        station_id = str(row['Identifiant station'])  # Convert to string to avoid KeyErrors
        station_name = row['Nom de la station']
        station_capacity = row['Capacité de la station']
        station_coords = tuple(map(float, row['Coordonnées géographiques'].split(',')))
        G.add_node(station_id, name=station_name, capacity=station_capacity, coords=station_coords)
    
    # Add edges with distances
    stations = list(G.nodes(data=True))
    for i, (station1_id, station1_data) in enumerate(tqdm(stations, desc="Adding edges")):
        for j, (station2_id, station2_data) in enumerate(stations):
            if i != j:
                distance = haversine(station1_data['coords'], station2_data['coords'])
                G.add_edge(station1_id, station2_id, weight=distance)
    
    return G

def save_graph(G, file_path):
    """Save the graph to a file."""
    nx.write_gml(G, file_path)

if __name__ == "__main__":
    input_file = 'velib-emplacement-des-stations.csv'
    output_file = 'graph.gml'
    
    df = load_data(input_file)
    G = create_graph(df)
    save_graph(G, output_file)
    print(f"Graph saved to {output_file}")