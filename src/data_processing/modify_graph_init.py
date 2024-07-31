import pandas as pd
import networkx as nx

def load_graph(file_path):
    """
    Load the graph from a GML file.
    
    Parameters:
        file_path (str): Path to the GML file.
    
    Returns:
        networkx.Graph: The loaded graph.
    """
    return nx.read_gml(file_path)

def update_node_attributes(G, data_file):
    """
    Update the 'velos' and 'bornes' attributes of each node in the graph based on the data file.
    
    Parameters:
        G (networkx.Graph): The graph to update.
        data_file (str): Path to the CSV file containing the node data.
    """
    # Load the node data from the CSV file
    df = pd.read_csv(data_file)
    
    # Iterate over each row in the dataframe
    for _, row in df.iterrows():
        node_id = str(row['node_id'])  # Convert to string to match node ID in the graph
        num_velos = row['num_velos']
        num_bornes = row['num_bornes']
        
        # Update the node attributes in the graph
        if node_id in G.nodes:
            G.nodes[node_id]['velos'] = num_velos
            G.nodes[node_id]['bornes'] = num_bornes

def save_graph(G, file_path):
    """Save the graph to a file."""
    nx.write_gml(G, file_path)

if __name__ == "__main__":
    input_graph_file = 'graphs/graph.gml'
    node_data_file = 'data/node_data.csv'
    output_graph_file = 'graphs/updated_graph.gml'
    
    print(f"Loading graph from {input_graph_file}")
    G = load_graph(input_graph_file)
    print("Graph loaded")
    
    print(f"Updating node attributes based on {node_data_file}")
    update_node_attributes(G, node_data_file)
    print("Node attributes updated")
    
    print(f"Saving updated graph to {output_graph_file}")
    save_graph(G, output_graph_file)
    print("Updated graph saved")