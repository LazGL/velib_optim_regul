import heapq

def astar(graph, start_station_id, end_station_id, max_duration):
    """
    Find the optimal path between two stations using the A* algorithm.
    
    :param graph: The graph representing the Velib' stations network.
    :param start_station_id: The ID of the starting station.
    :param end_station_id: The ID of the destination station.
    :param max_duration: The maximum duration allowed for the tour.
    :return: The optimal path as a list of station IDs.
    """
    # Initialize the open set and the g_scores dictionary
    open_set = [(0, start_station_id)]
    g_scores = {start_station_id: 0}
    
    # Initialize the came_from dictionary to reconstruct the path
    came_from = {}
    
    while open_set:
        current_f_score, current_station_id = heapq.heappop(open_set)
        
        if current_station_id == end_station_id:
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
                f_score = tentative_g_score + graph[neighbor_station_id][end_station_id]['weight']
                heapq.heappush(open_set, (f_score, neighbor_station_id))
    
    # If no path is found, return None
    return None