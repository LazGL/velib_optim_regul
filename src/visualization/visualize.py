import folium
import networkx as nx

def visualize_path(G, path, map_name='map_paris.html'):
    """Visualize the path on a map of Paris."""
    # Create a map centered on Paris
    map_paris = folium.Map(location=[48.8566, 2.3522], zoom_start=12)

    # Add markers for each station
    for node, data in G.nodes(data=True):
        folium.Marker(
            location=data['coords'],
            popup=f"Station: {data['name']}<br>Capacity: {data['capacity']}<br>Bikes: {data['velos']}<br>Docks: {data['bornes']}",
            icon=folium.Icon(color='blue', icon='bicycle', prefix='fa')
        ).add_to(map_paris)

    # Add lines for each edge in the path
    if path:
        edges = list(zip(path, path[1:]))
        for edge in edges:
            coords = [G.nodes[edge[0]]['coords'], G.nodes[edge[1]]['coords']]
            folium.PolyLine(locations=coords, color='red', weight=2.5, opacity=1).add_to(map_paris)

    return map_paris