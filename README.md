# Optimisation des déplacements des agents de régulation des stations Vélib' à Paris

## Objectifs
- Minimiser le nombre de déplacements des agents de régulation.
- Équilibrer les stations pour éviter qu'elles soient vides ou pleines.

## Contraintes
- La capacité maximale des stations ne doit pas être dépassée.
- Les camions de régulation ont des capacités variables (6, 13 ou 15 vélos) selon leur type.
- Chaque camion peut transporter un maximum de 3 fois sa capacité en vélos durant sa tournée de régulation.
- Le coût des déplacements des camions est déterminé par la distance parcourue entre les stations.

## Approche
- Utilisation de l'algorithme heuristique A* pour trouver le chemin optimal entre les stations.
- Intégration des contraintes dans l'algorithme pour garantir des solutions réalisables.
- Définition d'une fonction de coût pour évaluer la qualité des solutions générées.

## Données
- Fichier CSV contenant les informations sur les stations Vélib' (identifiants, noms, capacités, coordonnées géographiques).
- Graphe représentant les stations Vélib' et les distances entre elles.

## Structure du projet
|- requirements.txt
|- README.md
|-- graphs
|   |- graph_map.html
|   |- graph.gml
|- main.py
|-- data
|   |- velib-emplacement-des-stations.csv
|   |- velib-emplacement-des-stations.parquet
|- test.ipynb
|-- src
|   |-- visualization
|   |   |- analyze_graph.py
|   |   |- visualize_graph.py
|   |   |- __init__.py
|   |-- data_processing
|   |   |- modify_graph_init.py
|   |   |- __init__.py
|   |   |- generate_graph_random_init.py
|   |- __init__.py

## Étapes
1. Chargement et prétraitement des données des stations Vélib'.
2. Création du graphe représentant les stations et les distances.
3. Implémentation de l'algorithme A* avec intégration des contraintes.
4. Définition de la fonction de coût pour évaluer les solutions.
5. Visualisation des résultats avant et après l'optimisation.
6. Analyse des performances et des améliorations obtenues.


