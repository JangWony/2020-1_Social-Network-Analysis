import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import community
import helper, Graph
import timeit


if __name__ == "__main__":
    
    G = nx.karate_club_graph()
    #G = Graph.dolphins_graph()
    #G = Graph.politician_graph()
    
    G = nx.convert_node_labels_to_integers(G, first_label=0)
    
    max_modularity = -1 

    #start = timeit.default_timer()
    community_generator = community.girvan_newman(G=G)

    for i, partition in enumerate(community_generator):

        partition_coverage = community.coverage(G, partition)
        partition_performance = community.performance(G, partition)
        partition_modularity = community.modularity(G, partition)

        
        if partition_modularity > max_modularity:
            max_modularity = partition_modularity
            best_partition = partition
        else:
            break
        
        print(
            f"{i:2d} time :: Coverage: {partition_coverage:.4f}, Performance: {partition_performance:.4f}, Modularity: {partition_modularity:.4f}"
        )
        if False:  #print all communities?
            for j, comm in enumerate(partition):
                print(f"community {j:2d} at time {i:2d} ==> {comm}")
    #print("==" * 20)
    '''
    end = timeit.default_timer()
    runtime = end-start
    print("Time : ", runtime)'''

    print(best_partition, max_modularity)

    best_partition_tuple = best_partition
    best_partition_dict = helper.tuple_to_dict(best_partition)

    helper.draw_graph(G, best_partition_dict, best_partition_tuple)

