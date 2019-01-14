from undirected_graph import UndirectedGraph


class Cluster:
    def __init__(self, graph: UndirectedGraph, nodes: list):
        self.__graph = graph
        self.__nodes = nodes
        self.__node_set = set(nodes)
        self.__score = self.__score_func()

    def __score_func(self):
        ms = 0
        cs = 0
        for node in self.__nodes:
            for neigh in self.__graph.neighbors(node):
                if neigh in self.__node_set:
                    ms += 1
                else:
                    cs += 1
        return cs / 2 * ms
        #return cs / 2 * ms + cs + cs / 2 * (self.__graph.node_count() - ms) + cs

    def __contains__(self, node):
        return node in self.__node_set

    def __str__(self):
        return self.__nodes.__str__()

    def __repr__(self):
        return self.__str__()

    def nodes(self):
        return self.__nodes

    def score(self):
        return self.__score

    @staticmethod
    def merge(left, right):
        nodes = right.__nodes + left.__nodes
        return Cluster(left.__graph, nodes)

    @staticmethod
    def neighbour(left, right):
        for node in left.__nodes:
            for neigh in left.__graph.neighbors(node):
                if neigh in right:
                    return True
        return False

    @staticmethod
    def distance(left, right):
        return Cluster.merge(left, right).score()
