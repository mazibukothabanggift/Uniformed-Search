import networkx as nx
import matplotlib.pyplot as plt

from bfs import bfs
from dfs import dfs
from id_dfs import iddfs

# Your graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}


def draw_graph(graph):
    G = nx.DiGraph()
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    plt.figure(figsize=(7, 6))
    pos = {
        'A': (0, 2),
        'B': (-1.5, 1),
        'C': (1.5, 1),
        'D': (-2, 0),
        'E': (-1, 0),
        'F': (2, 0),
        'G': (-1, -1)
    }

    nx.draw(
        G, pos,
        with_labels=True,
        node_color='lightblue',
        node_size=2000,
        font_size=12,
        font_weight='bold',
        arrows=True,
        arrowstyle='-|>',
        arrowsize=20
    )

    plt.title("Graph Representation")
    plt.axis('off')
    plt.show()


if __name__ == '__main__':
    draw_graph(graph)

    start_node = 'A'
    max_depth = 3

    print("BFS:", bfs(graph, start_node))
    print("DFS:", dfs(graph, start_node))
    print("IDDFS:", iddfs(graph, start_node, max_depth))
