import networkx as nx
import community as lvcm
from networkx.algorithms import community
import helper, Graph
import timeit

if __name__ == "__main__":
    
    G = nx.karate_club_graph()
    #G = Graph.dolphins_graph()
    #G = Graph.politician_graph()

    G = nx.convert_node_labels_to_integers(G, first_label=0)

    #first compute the best partition

    start = timeit.default_timer()
    partition = lvcm.best_partition(graph=G, partition=None, resolution=1, randomize=True)
    end = timeit.default_timer()
    runtime = end-start
    print("Time : ", runtime)

    best_partition_tuple = helper.dict_to_tuple(partition)
    best_partition_dict = partition

    partition_coverage = community.coverage(G, best_partition_tuple)
    partition_performance = community.performance(G, best_partition_tuple)
    partition_modularity = community.modularity(G, best_partition_tuple)

    print(
            f"{0:2d} time :: Coverage: {partition_coverage:.4f}, Performance: {partition_performance:.4f}, Modularity: {partition_modularity:.4f}"
        )

    
    helper.draw_graph(G, best_partition_dict, best_partition_tuple)
    
