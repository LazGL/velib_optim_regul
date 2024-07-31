import logging

def choose_end_station(G, start_station_id, imbalances, min_distance=1.5, top_n=50):
    """
    Choose the closest deficit station as the end station, with a minimum distance constraint.
    
    Args:
        G (networkx.Graph): The bike station graph.
        start_station_id (int): The ID of the start station.
        imbalances (dict): A dictionary of station imbalances.
        min_distance (float): The minimum distance required between start and end stations.
        top_n (int): The number of top deficit stations to consider.
    
    Returns:
        tuple: A tuple containing the chosen end station ID and its imbalance.
    """
    # Find the top imbalanced stations with deficit bikes
    top_deficit_stations = sorted(
        [(station_id, imbalance) for station_id, imbalance in imbalances.items() if imbalance < 0],
        key=lambda x: x[1]
    )[:top_n]

    if top_deficit_stations:
        # Filter the top deficit stations based on the minimum distance constraint
        filtered_deficit_stations = [
            (station_id, imbalance)
            for station_id, imbalance in top_deficit_stations
            if G[start_station_id][station_id]['weight'] >= min_distance
        ]

        if filtered_deficit_stations:
            # Choose the closest deficit station among the filtered stations as the end station
            end_station_id, end_imbalance = min(
                filtered_deficit_stations,
                key=lambda x: G[start_station_id][x[0]]['weight']
            )
            logging.info(f"End station chosen: {end_station_id} with imbalance {end_imbalance}")
            logging.info(f"Distance: {G[start_station_id][end_station_id]['weight']}")
            print(f"End station chosen: {end_station_id} with imbalance {end_imbalance}")
            return end_station_id, end_imbalance
        else:
            logging.info("No suitable end station found within the minimum distance.")
            print("No suitable end station found within the minimum distance.")
            return None, None
    else:
        logging.info("No suitable end station found.")
        print("No suitable end station found.")
        return None, None