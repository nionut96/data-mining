from undirected_graph import UndirectedGraph
from cluster import Cluster


def cluster(graph: UndirectedGraph):
    cluster_list = [Cluster(graph, [x]) for x in graph.nodes()]
    while len(cluster_list) != 5:
        print('Iteration ' + str(len(cluster_list)))
        min_dist = 100000000
        left = None
        right = None
        for c1 in range(len(cluster_list)):
            for c2 in range(c1+1,len(cluster_list)):
                if Cluster.neighbour(cluster_list[c1], cluster_list[c2]):
                    dist = Cluster.distance(cluster_list[c1], cluster_list[c2])
                    if min_dist > dist:
                        left = cluster_list[c1]
                        right = cluster_list[c2]
                        min_dist = dist

        #print(left)
        #print(right)

        cluster_list.remove(left)
        cluster_list.remove(right)
        cluster_list.append(Cluster.merge(left, right))

        #print(cluster_list)
    return cluster_list
