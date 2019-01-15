from undirected_graph import UndirectedGraph
from dataset_handler import *
import aglomerative_clustering
import aco_clustering

if __name__ == '__main__':
    dataset = DatasetParser('email_dataset')
    graph = UndirectedGraph(dataset.nodes_count(), dataset.edges_list())
    # clusters = aco_clustering.cluster(graph)
    clusters = aglomerative_clustering.cluster(graph)
    print(clusters)
    write_output('email_dataset_out2', clusters)
