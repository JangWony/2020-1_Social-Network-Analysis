import networkx as nx
import pandas as pd

def politician_graph():
    G = nx.read_gml("Graph/politician.gml")
    return G

def dolphins_graph():
    G = nx.read_gml("Graph/dolphins.gml")
    return G


if __name__ == "__main__":
    pass