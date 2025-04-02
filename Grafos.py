import networkx as nx
import matplotlib.pyplot as plt
from itertools import permutations, product

G = nx.Graph()

states = ['Aguascalientes', 'Zacatecas', 'San Luis Potosí', 'Jalisco', 'Guanajuato', 'Querétaro', 'Michoacán']
G.add_nodes_from(states)

edges = [
    ('Aguascalientes', 'Zacatecas', 50),
    ('Aguascalientes', 'San Luis Potosí', 70),
    ('Zacatecas', 'San Luis Potosí', 60),
    ('Zacatecas', 'Jalisco', 80),
    ('San Luis Potosí', 'Jalisco', 90),
    ('San Luis Potosí', 'Guanajuato', 100),
    ('Jalisco', 'Guanajuato', 120),
    ('Guanajuato', 'Querétaro', 110),
    ('Querétaro', 'Michoacán', 130),
    ('Michoacán', 'Jalisco', 140)
]
G.add_weighted_edges_from(edges)

def draw_graph(graph):
    plt.figure(figsize=(10, 8))
    pos = nx.spring_layout(graph, seed=42)
    nx.draw(graph, pos, with_labels=True, node_size=3000, node_color='lightblue', font_size=10)
    labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
    plt.title("Graph of Mexican States and Their Relationships")
    plt.show()

def traverse_without_repetition(graph):
    states = list(graph.nodes)
    all_paths = permutations(states)
    min_cost = float('inf')
    best_path = None

    for path in all_paths:
        cost = 0
        valid_path = True
        for i in range(len(path) - 1):
            if graph.has_edge(path[i], path[i + 1]):
                cost += graph[path[i]][path[i + 1]]['weight']
            else:
                valid_path = False
                break
        if valid_path and cost < min_cost:
            min_cost = cost
            best_path = path

    return best_path, min_cost

def traverse_with_repetition(graph):
    states = list(graph.nodes)
    all_paths = product(states, repeat=len(states) + 1)
    min_cost = float('inf')
    best_path = None

    for path in all_paths:
        cost = 0
        valid_path = True
        for i in range(len(path) - 1):
            if graph.has_edge(path[i], path[i + 1]):
                cost += graph[path[i]][path[i + 1]]['weight']
            else:
                valid_path = False
                break
        if valid_path and cost < min_cost:
            min_cost = cost
            best_path = path

    return best_path, min_cost

def display_relationships(edges):
    print("Estados y sus relaciones:")
    for edge in edges:
        print(f"{edge[0]} - {edge[1]}: Costo {edge[2]}")

draw_graph(G)

best_path_no_repeat, total_cost_no_repeat = traverse_without_repetition(G)
print("Recorrido sin repetir estados:", best_path_no_repeat)
print("Costo total sin repetir:", total_cost_no_repeat)

best_path_with_repeat, total_cost_with_repeat = traverse_with_repetition(G)
print("Recorrido con repetición:", best_path_with_repeat)
print("Costo total con repetición:", total_cost_with_repeat)

display_relationships(edges)
