from undirected_graph import UndirectedGraph
from dataset_parser import DatasetParser
from kmeans import kmeans

if __name__ == '__main__':
    dataset = DatasetParser('simple_dataset')
    graph = UndirectedGraph(dataset.nodes_count(), dataset.edges_list())
    print(dataset.nodes_count())
    print(dataset.edges_list())
    kmeans(graph, 3)
