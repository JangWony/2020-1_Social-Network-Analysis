import networkx as nx
import matplotlib.pyplot as plt

#input : dict, output : tuple
def dict_to_tuple(input): 
    max_k_w = []
    for com in set(input.values()):
        list_nodes = [nodes for nodes in input.keys() if input[nodes] == com]
        max_k_w = max_k_w + [list_nodes]
    output = tuple(max_k_w)
    return output 

#input : tuple, output : dict
def tuple_to_dict(input):

    output = dict()
    for i, com in enumerate(input):
        for node in com:
            output[node] = i
    return output

#input : list of frozenset, output : tuple
def frozensetlist_to_tuple(input):
    best_partition_list = []
    for partition in input:
        best_partition_list = best_partition_list + [list(partition)]
    return tuple(best_partition_list)

#input : generator, output : tuple
def set_to_tuple(input):
    partition_list = []
    for partition in input:
        partition_list = partition_list + [list(partition)]
    return tuple(partition_list)

def draw_graph(G, partition_dict, partition_tuple):

    community_num_group = len(partition_tuple)
    color_list_community = [[] for i in range(len(G.nodes()))]
    for i in range(len(G.nodes())):
        for j in range(community_num_group):
            if i in partition_tuple[j]:
                color_list_community[i]=j
    
    pos = nx.spring_layout(G)
    fig = plt.figure()
    edges = G.edges()
    Feature_color_sub = color_list_community
    node_size = 50
    im = nx.draw_networkx_nodes(G, pos, node_size=node_size, node_color=Feature_color_sub, cmap='jet', vmin=0, vmax=community_num_group)
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_labels(G, pos, font_size=5, font_color="black")
    plt.xticks([])
    plt.yticks([])
    plt.colorbar(im)
    plt.show()
    plt.show(block=False)