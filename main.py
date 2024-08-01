import logging
import os
from datetime import datetime

from src.data_processing.generate_graph import load_data, create_graph, save_graph
from src.algorithms.astar import astar
from src.algorithms.utils import calculate_imbalance, update_graph, load_graph
from src.visualization.visualize import visualize_path
from src.constants import MAX_TOUR_DURATION
from src.algorithms.choose_start_station import choose_start_station
from src.algorithms.choose_end_station import choose_end_station
from src.algorithms.calculate_bikes_to_move import calculate_bikes_to_move

def main():
    # Create a logs directory if it doesn't exist
    os.makedirs('logs', exist_ok=True)

    # Create a log file for the current execution
    log_filename = f"logs/execution_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    logging.basicConfig(filename=log_filename, level=logging.INFO, format='%(asctime)s - %(message)s')

    # Load the data and create the graph
    if not os.path.exists('graphs/graph.gml'):
        input_file = 'data/velib-emplacement-des-stations.csv'
        logging.info(f"Loading data from {input_file}")
        df = load_data(input_file)
        logging.info("Data loaded")
        logging.info("Creating the graph (it might take a few minutes)")
        G = create_graph(df)
        logging.info("Graph created")
        logging.info("Saving the graph")
        save_graph(G, 'graphs/graph.gml')
    else:
        logging.info("Loading pre-initialized graph (it might take 35s)")
        G = load_graph('graphs/graph.gml')
        logging.info("Graph loaded")

    # Main loop
    max_iterations = 10

    for i in range(max_iterations):
        logging.info(f"Start iteration {i+1}")
        # Calculate the imbalance of each station
        imbalances = {station_id: calculate_imbalance(data['capacity'], data['velos']) for station_id, data in G.nodes(data=True)}
    
        # Choose the start station
        start_station_id, start_imbalance = choose_start_station(imbalances)

        if start_station_id is not None:
            # Choose the end station
            end_station_id, end_imbalance = choose_end_station(G, start_station_id, imbalances)

            if end_station_id is not None:
                # Find the optimal path between the start station and the end station
                path = astar(G, start_station_id, end_station_id, MAX_TOUR_DURATION)

                if path:
                    # Calculate the number of bikes to move
                    num_bikes_moved = calculate_bikes_to_move(start_imbalance, end_imbalance)

                    # Update the graph with the number of bikes moved
                    update_graph(G, start_station_id, end_station_id, num_bikes_moved)

                    # Log the path and the update
                    logging.info(f"Iteration {i+1}: Optimal path found:")
                    logging.info(f"Path: {' -> '.join(map(str, path))}")
                    logging.info(f"Moved {num_bikes_moved} bikes from station {start_station_id} to station {end_station_id}")
                else:
                    logging.info(f"Iteration {i+1}: No path found.")
            else:
                logging.info(f"Iteration {i+1}: No suitable end station found.")
        else:
            logging.info(f"Iteration {i+1}: No suitable start station found.")

if __name__ == "__main__":
    main()