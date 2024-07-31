import networkx as nx
import matplotlib.pyplot as plt
import os
import folium


def load_graph(file_path):
    """
    Load the graph from a GML file.
    
    Parameters:
        file_path (str): Path to the GML file.
    
    Returns:
        networkx.Graph: The loaded graph.
    """
    return nx.read_gml(file_path)

def create_map(G):
    """
    Create a Folium map with nodes and edges from the graph.
    
    Parameters:
        G (networkx.Graph): The graph to visualize.
    
    Returns:
        folium.Map: The generated map.
    """
    # Get the geographical center of the graph to center the map
    latitudes = [data['coords'][0] for _, data in G.nodes(data=True)]
    longitudes = [data['coords'][1] for _, data in G.nodes(data=True)]
    center_lat = sum(latitudes) / len(latitudes)
    center_lon = sum(longitudes) / len(longitudes)

    # Create a map centered on the geographical center
    m = folium.Map(location=[center_lat, center_lon], zoom_start=14)

    # Add nodes to the map
    for node, data in G.nodes(data=True):
        folium.Marker(
            location=data['coords'],
            popup=f"Station: {data['name']}\nCapacity: {data['capacity']}",
            icon=folium.Icon(color='blue', icon='info-sign')
        ).add_to(m)
    
    # Add edges to the map
    for u, v, data in G.edges(data=True):
        coords_u = G.nodes[u]['coords']
        coords_v = G.nodes[v]['coords']
        folium.PolyLine(
            locations=[coords_u, coords_v],
            weight=1,
            color='black'
        ).add_to(m)
    
    return m

def save_map(m, file_path):
    """
    Save the generated map to an HTML file.
    
    Parameters:
        m (folium.Map): The map to save.
        file_path (str): Path to the output HTML file.
    """
    m.save(file_path)


def display_graph(G):
    """Display the graph."""
    plt.figure(figsize=(12, 8))
    pos = nx.spring_layout(G, seed=42)  # Positions des nœuds
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=10, font_weight='bold')
    plt.title("Graphe des Stations Vélib")
    plt.show()

def print_node_attributes(G, node_id):
    """Print attributes of a specific node."""
    node_attributes = G.nodes[str(node_id)]
    print(f"Attributs du nœud {node_id} :", node_attributes)

def print_edge_attributes(G, node1_id, node2_id):
    """Print attributes of a specific edge."""
    edge_attributes = G.edges[(str(node1_id), str(node2_id))]
    print(f"Attributs de l'arête ({node1_id}, {node2_id}) :", edge_attributes)

if __name__ == "__main__":
    input_file = 'graphs/graph.gml'
    output_file = 'graphs/graph_map.html'

    print("Loading graph...")
    G = load_graph(input_file)
    print("Graph loaded successfully.")

    print("Creating map...")
    m = create_map(G)
    print("Map created successfully.")
    print("Saving map...")
    save_map(m, output_file)
    print(f"Map saved to {output_file}")
    
    # display_graph(G)
    
    # Example usage
    print("Examples:")
    print_node_attributes(G, 32017)
    print_edge_attributes(G, 32017, 17048)