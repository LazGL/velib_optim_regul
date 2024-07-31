import logging
import os
from datetime import datetime
from src.data_processing.generate_graph import load_data, create_graph
from src.algorithms.astar import astar
from src.algorithms.utils import calculate_imbalance, update_graph, load_graph
from src.visualization.visualize import visualize_path
from src.constants import MAX_TOUR_DURATION

def main():
    # Create a logs directory if it doesn't exist
    os.makedirs('logs', exist_ok=True)

    # Create a log file for the current execution
    log_filename = f"logs/execution_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    logging.basicConfig(filename=log_filename, level=logging.INFO, format='%(asctime)s - %(message)s')

    # Load the data and create the graph
    input_file = 'data/velib-emplacement-des-stations.csv'
    logging.info(f"Loading data from {input_file}")
    df = load_data(input_file)
    logging.info("Data loaded")
    logging.info("Loading pre-initialized graph (it might take 35s)")
    G = load_graph('graphs/graph.gml')
    logging.info("Graph loaded")

    # Main loop
    max_iterations = 10
    threshold = 5

    for i in range(max_iterations):
        logging.info(f"Start iteration {i+1}")
        # Calculate the imbalance of each station
        imbalances = {station_id: calculate_imbalance(data['capacity'], data['velos']) for station_id, data in G.nodes(data=True)}

        # Find the most imbalanced station
        start_station_id = max(imbalances, key=lambda x: abs(imbalances[x]))

        # Find neighboring stations that can contribute to rebalancing the start station
        neighbors = [station_id for station_id in G.neighbors(start_station_id) if abs(imbalances[station_id]) < threshold]

        if neighbors:
            # Choose the closest neighboring station
            end_station_id = min(neighbors, key=lambda x: G[start_station_id][x]['weight'])

            # Find the optimal path between the start station and the end station
            path = astar(G, start_station_id, end_station_id, MAX_TOUR_DURATION)

            if path:
                # Move bikes along the optimal path
                num_bikes_moved = min(imbalances[start_station_id], -imbalances[end_station_id])
                update_graph(G, start_station_id, end_station_id, num_bikes_moved)

                # Log the path and the update
                logging.info(f"Iteration {i+1}: Optimal path found:")
                logging.info(f"Path: {' -> '.join(map(str, path))}")
                logging.info(f"Moved {num_bikes_moved} bikes from station {start_station_id} to station {end_station_id}")
            else:
                logging.info(f"Iteration {i+1}: No path found.")
        else:
            logging.info(f"Iteration {i+1}: No suitable neighboring station found.")

if __name__ == "__main__":
    main()