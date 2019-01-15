from undirected_graph import UndirectedGraph
from cluster import Cluster
from random import randint
from random import uniform


def cluster(graph: UndirectedGraph):
    edges = {}
    steps = 0
    for node in graph.nodes():
        for neigh in graph.neighbors(node):
            edges[(node, neigh)] = 10
            edges[(neigh, node)] = 10
            steps += 1
    steps = int(0.1 * steps / 100) + 1
    nodes = [node for node in graph.nodes()]

    for iteration in range(500):
        print('Iteration ' + str(iteration))

        for i in range(len(nodes)):
            # ant = nodes[randint(0, len(nodes)-1)]
            # print('Node ' + str(nodes[i]))
            ant = nodes[i]
            for step in range(steps):
                next_nodes = graph.neighbors(ant)
                if len(next_nodes) == 0:
                    continue
                # print(next_nodes)
                prob = [edges[(ant, n)] for n in next_nodes]
                # print('prob:',prob)
                total = sum(prob)
                prob = [p / total for p in prob]
                direction = uniform(0, 1)
                while direction > prob[0]:
                    direction -= prob[0]
                    next_nodes = next_nodes[1:]
                    prob = prob[1:]
                next_node = next_nodes[0]
                # print('next_node ', next_node)
                edges[(next_node, ant)] += 0.1
                edges[(ant, next_node)] += 0.1
                ant = next_node

    suma = 0
    for i in range(len(nodes)):
        for j in range(i+1, len(nodes)):
            if (nodes[i], nodes[j]) in edges:
                print(str(nodes[i]) + ',' + str(nodes[j]) + ' : ' + str(edges[(nodes[i], nodes[j])]))
                suma += edges[(nodes[i], nodes[j])]
    suma = 2 * suma / len(edges)
    print(suma)

    cluster_list = []
    while len(nodes) != 0:
        node = nodes.pop()
        clust = Cluster(graph, [node])
        vecini = []
        for neigh in graph.neighbors(node):
            if (node, neigh) in edges and edges[(node, neigh)] > 0.9 * suma:
                vecini.append(neigh)
                clust.add(neigh)
                if neigh in nodes:
                    nodes.remove(neigh)
                del edges[(node, neigh)]
                del edges[(neigh, node)]
        while len(vecini) != 0:
            n = vecini.pop()
            for neigh in graph.neighbors(n):
                if (n, neigh) in edges and edges[(n, neigh)] > 0.9 * suma and neigh not in clust:
                    vecini.append(neigh)
                    clust.add(neigh)
                    if neigh in nodes:
                        nodes.remove(neigh)
                    del edges[(n, neigh)]
                    del edges[(neigh, n)]
        cluster_list.append(clust)

    return cluster_list