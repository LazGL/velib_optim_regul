import heapq
import logging

def astar(graph, start_station_id, end_station_id, max_duration, max_nodes=20000):
    """
    Find the optimal path between two stations using the A* algorithm.
    
    :param graph: The graph representing the Velib' stations network.
    :param start_station_id: The ID of the starting station.
    :param end_station_id: The ID of the destination station.
    :param max_duration: The maximum duration allowed for the tour.
    :param max_nodes: The maximum number of nodes to explore.
    :return: The optimal path as a list of station IDs.
    """

    logging.info(f"Starting A* algorithm from station {start_station_id} to station {end_station_id}")
    
    # Initialize the open set and the g_scores dictionary
    open_set = [(0, start_station_id)]
    g_scores = {start_station_id: 0}
    
    # Initialize the came_from dictionary to reconstruct the path
    came_from = {}
    
    explored_nodes = 0
    
    while open_set:
        current_f_score, current_station_id = heapq.heappop(open_set)
        
        if current_station_id == end_station_id:
            logging.info(f"Destination station {end_station_id} reached")
            
            # Reconstruct the path
            path = []
            while current_station_id in came_from:
                path.append(current_station_id)
                current_station_id = came_from[current_station_id]
            path.append(start_station_id)
            path.reverse()
            return path
        
        for neighbor_station_id in graph.neighbors(current_station_id):
            tentative_g_score = g_scores[current_station_id] + graph[current_station_id][neighbor_station_id]['weight']
            
            if tentative_g_score < g_scores.get(neighbor_station_id, float('inf')):
                came_from[neighbor_station_id] = current_station_id
                g_scores[neighbor_station_id] = tentative_g_score
                
                if graph.has_edge(neighbor_station_id, end_station_id):
                    f_score = tentative_g_score + graph[neighbor_station_id][end_station_id]['weight']
                    heapq.heappush(open_set, (f_score, neighbor_station_id))
        
        explored_nodes += 1
        if explored_nodes % 1000 == 0:
            logging.info(f"Explored {explored_nodes} nodes so far")
        if explored_nodes > max_nodes:
            logging.warning(f"A* algorithm reached the maximum number of explored nodes ({max_nodes})")
            return None
    
    if came_from:
        path = []
        current_station_id = end_station_id
        while current_station_id in came_from:
            path.append(current_station_id)
            current_station_id = came_from[current_station_id]
        path.append(start_station_id)
        path.reverse()
        logging.info(f"Optimal path found: {' -> '.join(map(str, path))}")
        return path
    else:
        print(f"ERROR : No path found from {start_station_id} to {end_station_id}")
        logging.info(f"No path found from {start_station_id} to {end_station_id}")
        return None