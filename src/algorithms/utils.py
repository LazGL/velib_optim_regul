def calculate_imbalance(station_capacity, num_velos):
    equilibrium = station_capacity // 2
    imbalance = abs(num_velos - equilibrium)
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