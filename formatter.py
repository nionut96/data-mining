

if __name__ == '__main__':
    core_file = open('email-Eu-core.txt', 'r')
    core_gr_file = open('email-Eu-core-department-labels.txt', 'r')

    nodes = dict()
    edges = []
    line = core_file.readline().strip()
    while line != '':
        i, j = line.split(' ')
        i = int(i) + 1
        j = int(j) + 1
        nodes[i] = 1
        nodes[j] = 1
        if i != j:
            edges.append((i, j))
        line = core_file.readline()

    groups = dict()
    group_edges = []
    line = core_gr_file.readline().strip()
    while line != '':
        n, g = line.split(' ')
        n = int(n) + 1
        g = int(g) + 1
        groups[g] = 1
        group_edges.append((n, g))
        line = core_gr_file.readline()

    core_file.close()
    core_gr_file.close()

    nodes_file = open('nodes.csv', 'w+')
    edges_file = open('edges.csv', 'w+')
    groups_file = open('groups.csv', 'w+')
    group_edges_file = open('group-edges.csv', 'w+')

    for node in nodes.keys():
        nodes_file.write(str(node) + '\n')

    for i, j in edges:
        edges_file.write(str(i) + ',' + str(j) + '\n')

    for group in groups.keys():
        groups_file.write(str(group) + '\n')

    for n, g in group_edges:
        group_edges_file.write(str(n) + ',' + str(g) + '\n')

    nodes_file.close()
    edges_file.close()
    groups_file.close()
    group_edges_file.close()