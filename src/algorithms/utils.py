import networkx as nx
import time

def calculate_imbalance(station_capacity, num_velos):
    target_velos = station_capacity // 2
    imbalance = num_velos - target_velos
    return imbalance
def update_graph(G, station1_id, station2_id, num_velos_moved):
    # Update the number of bikes and docks at the stations
    G.nodes[station1_id]['velos'] -= num_velos_moved
    G.nodes[station1_id]['bornes'] += num_velos_moved
    G.nodes[station2_id]['velos'] += num_velos_moved
    G.nodes[station2_id]['bornes'] -= num_velos_moved

    # Recalculate the imbalance and update the edge cost
    imbalance1 = calculate_imbalance(G.nodes[station1_id]['capacity'], G.nodes[station1_id]['velos'])
    imbalance2 = calculate_imbalance(G.nodes[station2_id]['capacity'], G.nodes[station2_id]['velos'])
    G.edges[station1_id, station2_id]['weight'] += imbalance1 + imbalance2

def load_graph(file_path):
    """
    Load the graph from a GML file.
    
    Parameters:
        file_path (str): Path to the GML file.
    
    Returns:
        networkx.Graph: The loaded graph.
    """
    start_time = time.time() 
    graph = nx.read_gml(file_path)
    end_time = time.time()  
    execution_time = end_time - start_time
    print(f"Graph loaded in {execution_time} seconds.")  # Print the execution time
    return graph