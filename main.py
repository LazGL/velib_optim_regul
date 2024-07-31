from src.data_processing.generate_graph import load_data, create_graph
from src.algorithms.astar import astar
from src.algorithms.utils import calculate_imbalance, update_graph
from src.visualization.visualize import visualize_path

def main():
    # ... (chargement des données et création du graphe initial)

    # Boucle principale
    max_iterations = 10  # Nombre maximal d'itérations
    for i in range(max_iterations):
        # Trouve le chemin optimal entre deux stations
        start_station_id = input("Enter the ID of the starting station: ")
        end_station_id = input("Enter the ID of the destination station: ")
        path = astar(G, start_station_id, end_station_id)

        if path:
            print(f"Iteration {i+1}: Optimal path found:")
            print(path)

            # Effectue le mouvement de régulation
            num_velos_moved = 5  # Nombre de vélos à déplacer (exemple)
            update_graph(G, start_station_id, end_station_id, num_velos_moved)

            # Visualise le chemin et l'état actuel du système Velib'
            map_paris = visualize_path(G, path)
            map_paris.save(f'optimal_path_iteration_{i+1}.html')
            print(f"Path visualization saved to optimal_path_iteration_{i+1}.html")
        else:
            print(f"Iteration {i+1}: No path found.")

if __name__ == "__main__":
    main()