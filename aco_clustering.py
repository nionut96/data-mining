from undirected_graph import UndirectedGraph
from random import randint
from random import random


def cluster(graph: UndirectedGraph):
    edges = {}
    steps = 0
    for node in graph.nodes():
        for neigh in graph.neighbors(node):
            edges[(node, neigh)] = 10
            edges[(neigh, node)] = 10
            steps += 1



    return cluster_list