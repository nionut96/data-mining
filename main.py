from undirected_graph import UndirectedGraph
from dataset_handler import *
from aglomerative_clustering import *

if __name__ == '__main__':
    dataset = DatasetParser('simple_dataset')
    graph = UndirectedGraph(dataset.nodes_count(), dataset.edges_list())
    clusters = cluster(graph)
    write_output('simple_dataset_out', clusters)
