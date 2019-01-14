from undirected_graph import UndirectedGraph

import random


def max_cl(cluster: dict):
    keys = [x for x in cluster.keys()]
    maximum = cluster[keys[0]]
    value = keys[0]
    for c in keys:
        if cluster[c] > maximum:
            maximum = cluster[c]
            value = c
    return value


def kmeans(graph: UndirectedGraph, cluster_count: int):
    initial_clusters = [n for n in graph.nodes()]
    random.shuffle(initial_clusters)
    initial_clusters = initial_clusters[0:cluster_count]
    new_clust = initial_clusters
    clust = [0]

    while len(set(clust) & set(new_clust)) != cluster_count:
        clust = new_clust[:]
        nodes = set(graph.nodes())
        for node in clust:
            nodes.remove(node)
        clusters = {x: [x] for x in clust}
        neigh = {x: [x] for x in clust}
        while len(nodes) != 0:
            for cl in neigh.keys():
                next_nodes = []
                for node in neigh[cl]:
                    for n in graph.neighbors(node):
                        if n in nodes:
                            clusters[cl].append(n)
                            next_nodes.append(n)
                            nodes.remove(n)
                neigh[cl] = next_nodes

        new_clust = []
        for cl in clusters.keys():
            cluster = {x: 0 for x in clusters[cl]}
            for node in clusters[cl]:
                for n in graph.neighbors(node):
                    if n in cluster:
                        cluster[n] += 1
                    else:
                        cluster[node] -= 0.5
            new_clust.append(max_cl(cluster))

        print(clusters)
        print(clust)
