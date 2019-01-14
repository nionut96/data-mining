from undirected_graph import UndirectedGraph
from dataset_parser import DatasetParser
from aglomerative_clustering import *

if __name__ == '__main__':
    dataset = DatasetParser('simple_dataset')
    graph = UndirectedGraph(dataset.nodes_count(), dataset.edges_list())
    print(dataset.nodes_count())
    print(dataset.edges_list())
    clusters = cluster(graph)
    print(clusters)
