import os


class DatasetParser:
    def __init__(self, path):
        self.path = path
        nodes_file = open(os.path.join(self.path, 'nodes.csv'), 'r')
        edges_file = open(os.path.join(self.path, 'edges.csv'), 'r')

        line = nodes_file.readline()
        while line != '':
            self.__nodes_count = int(line.strip())
            line = nodes_file.readline()

        self.__edges_list = []
        line = edges_file.readline()
        while line != '':
            node1, node2 = line.strip().split(',')
            self.__edges_list.append((int(node1), int(node2)))
            line = edges_file.readline()

        nodes_file.close()
        edges_file.close()

    def nodes_count(self):
        return self.__nodes_count

    def edges_list(self):
        return self.__edges_list
