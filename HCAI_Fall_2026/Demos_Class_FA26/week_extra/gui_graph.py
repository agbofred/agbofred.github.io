import networkx as nx
import matplotlib.pyplot as plt


G = nx.DiGraph()
G.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'D'), ('D', 'A')])

pos = nx.arf_layout(G)

nx.draw_networkx_nodes(G,pos,node_size=500)
nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color='red' )
nx.draw_networkx_labels(G, pos)

plt.show()