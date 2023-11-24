"""
This is an introductory exercise in series for a Graph Neural Network project
Nishu Choudhary
"""
# Import Required Packages
import networkx as nx
import matplotlib.pyplot as plt
"""
There are four basic types of graphs offered by the NetworkX library
1. Undirected: allows self-loops but no parallel edges
2. Directed: allows self-loops but no parallel edges
3. MultiGraph (undirected): allow self-loops and parallel edges
4. MultiDiGraph (directed): allow self-loops and parallel edges
"""

# Create an undirected graph
G = nx.Graph()
print(f"Is Graph G directed: {G.is_directed()}")

# Create an undirected graph
G_di = nx.DiGraph()
print(f"Is Graph G_di directed: {G_di.is_directed()}")
print(dir(G))
"""
Object attributes
Each graph instance has following attributes: 
1. adj
2. adjaceny
3. degree
4. edge_subgraph
5. edges
6. graph
7. nodes
8. number_of_edges
9. number_of_nodes
10. order
11. size
12. subgraph

print(dir(G))
"""

# Adding graph level attributes:
G.graph['Name'] = 'Undirected_graph1'

"""
Object Methods (from documentation: https://networkx.org/documentation/stable/reference/classes/graph.html#methods)
1. __init__ : instantiation
2. add_node(node_for_adding, **attr): Add a single node node_for_adding and update node attributes
3. add_node_from(nodes_for_adding, **attr): Add multiple nodes.
4. remove_node(n): Remove node n
5. remove_nodes_form(nodes): Remove multiple nodes
6. add_edge(u_of_edge, v_of_edge, **attr): Add an edge between u and v
7. add_edges_from(ebunch_to_add, **attr): Add all the edges in ebunch_to_add
8. add_weighted_edges_from(ebunch_to_add): Add weighted edges in ebunch_to_add with specified weight attr
9. remove_edge(u,v): Remove the edge between u and v
10. remove_edges_from(ebunch): remove all edges specified in ebunch
11. update([edges, nodes]): update the graph using nodes/edges/graphs as input
12. clear(): remove all nodes and edges from the graph
13. clear_edges(): remove all edges from the graph without altering nodes
14. get_edge_data
15. has_edge
16. has_node
"""

# Add a node to the undirected graph object
G.add_node(0, feature=5, label=0)

# Get attributes of node 0
node_0_attributes = G.nodes[0]
print(f"Node 0 has attributes: {node_0_attributes}")

# Add multiple nodes
G.add_nodes_from([
  (1, {"feature": 8, "label": 1}),
  (2, {"feature": 9, "label": 2})
])

# Loop through all the nodes
# Set data=True will return node attributes in data view
for node in G.nodes(data=True):
  print(node)

# View Adjacency list representation of a graph
print(G.adj)

# Get total number of nodes in the graph
print(f"Total number of nodes in the graph are: {G.number_of_nodes()}")

# Add edges between nodes
G.add_edge(0, 1, weight=0.5)
print(f"Edge attributes: {G.edges[(0,1)]}")

# Adding multiple edges
G.add_edges_from([
    (0, 2, {'weight': 0.3}),
    (1, 2, {'weight': 0.1})

])

# Get total number of nodes in the graph
print(f"Total number of edges in the graph are: {G.number_of_edges()}")

# Re-view Adjacency list representation of a graph
print(G.adj)

# Pictorial visualization of the graph
nx.draw(G, with_labels=True)
plt.draw()
plt.savefig('sample.png')
plt.show()

# Node Degree and Neighbors
G.add_node(3, feature =3, label=3)
G.add_edge(1, 3, weight = 0.9)

node_id = 1
# Degree of node_id = 1
print(f"Degree of node {node_id} is {G.degree[node_id]}")

# Get all neighbors for node_id
for node in G.neighbors(node_id):
    print(f"Node {node_id} has neighbor {node}")

# Additional functionalities - converting a path-like graph and converting it to a directed graph
number_of_nodes = G.number_of_nodes()

G_new = nx.DiGraph(nx.path_graph(number_of_nodes))
nx.draw(G_new, with_labels=True)
plt.savefig('sample_2.png')
plt.show()