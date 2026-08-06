import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import approximation as approx

G = nx.DiGraph()
#G.add_edges_from([('A','B'),('B','C'), ('C','A')])

G.add_edge('A','B',weight=7)
G.add_edge('A','C',weight=17)
G.add_edge('A','D',weight=10)
G.add_edge('B','A',weight=20)
G.add_edge('B','C',weight=10)
G.add_edge('B','D',weight=2)
G.add_edge('C','A',weight=5)
G.add_edge('C','B',weight=4)
G.add_edge('C','D',weight=20)
G.add_edge('D','A',weight=6)
G.add_edge('D','B',weight=3)
G.add_edge('D','C',weight=6)

pos = nx.spring_layout(G)

nx.draw_networkx_nodes(G, pos, node_size=500)
nx.draw_networkx_edges(G,pos, edgelist= G.edges(), edge_color='blue')
nx.draw_networkx_labels(G, pos)
label = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=label)
cycle = approx.greedy_tsp(G, source="A")
cost = sum(G[n][nbr]["weight"] for n, nbr in nx.utils.pairwise(cycle))

print("Cycle path: ", cycle)
print("COst for TSA: ", cost)

plt.show()
