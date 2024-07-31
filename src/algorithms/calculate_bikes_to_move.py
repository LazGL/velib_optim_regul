import logging

def calculate_bikes_to_move(start_imbalance, end_imbalance, max_bikes=15):
    """
    Calculate the number of bikes to move from the start station to the end station.
    
    Args:
        start_imbalance (int): The imbalance of the start station.
        end_imbalance (int): The imbalance of the end station.
        max_bikes (int): The maximum number of bikes that can be moved.
    
    Returns:
        int: The number of bikes to move.
    """
    num_bikes_moved = min(start_imbalance, -end_imbalance, max_bikes)
    logging.info(f"Number of bikes to move: {num_bikes_moved}")
    print(f"Number of bikes to move: {num_bikes_moved}")
    return num_bikes_moved