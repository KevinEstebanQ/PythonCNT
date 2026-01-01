import networkx as nx
import matplotlib.pyplot as plt

# Define the adjacency matrix
adj_matrix = [
    [1, 0, 1, 2],
    [0, 0, 1, 0],
    [0, 2, 3, 1],
    [0, 1, 4, 0]
]

# Create a directed graph
G = nx.DiGraph()

# Node labels
nodes = ['v1', 'v2', 'v3', 'v4']

# Add weighted edges
for i in range(len(adj_matrix)):
    for j in range(len(adj_matrix[i])):
        weight = adj_matrix[i][j]
        if weight != 0:
            G.add_edge(nodes[i], nodes[j], weight=weight)

# Set positions for consistent layout
pos = nx.spring_layout(G, seed=42)

# Draw the graph
plt.figure(figsize=(8, 6))
nx.draw_networkx_nodes(G, pos, node_color='skyblue', node_size=1500)
nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')
nx.draw_networkx_edges(G, pos, arrowstyle='->', arrows=True, connectionstyle='arc3,rad=0.2')

# Draw weights as edge labels
edge_labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', font_size=12)

plt.title("Directed Graph with Weighted Edges")
plt.axis('off')
plt.show()

