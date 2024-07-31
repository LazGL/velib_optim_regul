import random
import logging

def choose_start_station(imbalances, top_n=5):
    """
    Choose a random station from the top imbalanced stations with surplus bikes.
    
    Args:
        imbalances (dict): A dictionary of station imbalances.
        top_n (int): The number of top surplus stations to consider.
    
    Returns:
        tuple: A tuple containing the chosen start station ID and its imbalance.
    """
    # Find the top imbalanced stations with surplus bikes
    top_surplus_stations = sorted(
        [(station_id, imbalance) for station_id, imbalance in imbalances.items() if imbalance > 0],
        key=lambda x: x[1],
        reverse=True
    )[:top_n]

    if top_surplus_stations:
        # Choose a random station from the top surplus stations as the start station
        start_station_id, start_imbalance = random.choice(top_surplus_stations)
        logging.info(f"Start station chosen: {start_station_id} with imbalance {start_imbalance}")
        print(f"Start station chosen: {start_station_id} with imbalance {start_imbalance}")
        return start_station_id, start_imbalance
    else:
        logging.info("No suitable start station found.")
        print("No suitable start station found.")
        return None, None