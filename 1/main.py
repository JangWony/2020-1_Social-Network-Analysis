import networkx as nx
import community as lvcm
import matplotlib.pyplot as plt
from networkx.algorithms import community

G = nx.read_gml("Datasets/karate.gml", label='id')

partition = lvcm.best_partition(graph=G, partition=None, weight='weight',resolution=1., randomize=True)

size = float(len(set(partition.values())))
pos = nx.spring_layout(G)
count = 0.
for com in set(partition.values()) :
    count = count + 1.
    list_nodes = [nodes for nodes in partition.keys()
                                if partition[nodes] == com]
    nx.draw_networkx_nodes(G, pos, list_nodes, node_size = 200,
                                node_color = str(count / size / 1.3))


nx.draw_networkx_edges(G, pos, alpha=0.5)
plt.show()

communities_init = [[i] for i in list(G.nodes())]
modularity = community.modularity(G, communities=communities_init, weight='weight')
print(modularity)