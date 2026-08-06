import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import approximation as approx


G = nx.DiGraph()

#G.add_edges_from([('A', 'B'), ('B','C'), ('C','A')])
G.add_edge('A', 'B', weigth=40)
G.add_edge('A', 'C', weigth=20)
G.add_edge('A', 'D', weigth=10)
G.add_edge('B', 'A', weigth=30)
G.add_edge('B', 'C', weigth=5)
G.add_edge('B', 'D', weigth=10)
G.add_edge('C', 'A', weigth=4)
G.add_edge('C', 'B', weigth=16)
G.add_edge('C', 'D', weigth=4)
G.add_edge('D', 'A', weigth=5)
G.add_edge('D', 'B', weigth=12)
G.add_edge('D', 'C', weigth=10)
pos= nx.arf_layout(G)

cycle = approx.greedy_tsp(G, source="A")
cost = sum(G[n][nbr]["weigth"] for n, nbr in nx.utils.pairwise(cycle))

nx.draw_networkx_nodes(G,pos, node_size=500)
nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color="blue")
nx.draw_networkx_labels(G, pos)
label = nx.get_edge_attributes(G, 'weigth')
nx.draw_networkx_edge_labels(G, pos, edge_labels=label)

print("Cycle Path: ", cycle)
print("Cost: ", cost)

plt.show()
