import os


class GroundTruth:
    def __init__(self):
        self.ground_truth_path = "big_cluster_dataset"
        self.clustered_set_path = "big_cluster_dataset_out"
        self.cluster_number = 0
        self.clustered_set = []
        self.ground_truth_number = 0
        self.ground_truth = []
        self.tags = []

        self.initialise_cluster_number()
        self.initialise_clustered_set()
        self.initialise_ground_truth_number()
        self.initialise_ground_truth()
        self.initialise_tags()

    def initialise_ground_truth_number(self):
        group_file = open(os.path.join(self.ground_truth_path, 'groups.csv'), 'r')
        
        line = group_file.readline()
        while line != '':
            self.ground_truth_number = int(line.strip())
            line = group_file.readline()
        
        group_file.close()
            
    def initialise_cluster_number(self):
        group_file = open(os.path.join(self.clustered_set_path, 'groups.csv'), 'r')
        
        line = group_file.readline()
        while line != '':
            self.cluster_number = int(line.strip())
            line = group_file.readline()
        
        group_file.close()
        
    def initialise_ground_truth(self):
        ground_truth_dict = { k: [] for k in range(1, self.ground_truth_number+1) }
        
        group_edges_file = open(os.path.join(self.ground_truth_path, 'group-edges.csv'), 'r')
        
        line = group_edges_file.readline()
        while line != '':
            split_line = line.strip().split(',')
            ground_truth_dict[int(split_line[1])].append(int(split_line[0]))
            line = group_edges_file.readline()
        
        for key, value in ground_truth_dict.items():
            self.ground_truth.append(value)

        group_edges_file.close()
    
    def initialise_clustered_set(self):
        cluster_dict = {k: [] for k in range(1, self.cluster_number+1)}
        
        group_edges_file = open(os.path.join(self.clustered_set_path, 'group-edges.csv'), 'r')
        
        line = group_edges_file.readline()
        while line != '':
            split_line = line.strip().split(',')
            cluster_dict[int(split_line[1])].append(int(split_line[0]))
            line = group_edges_file.readline()

        for key, value in cluster_dict.items():
            self.clustered_set.append(value)

        group_edges_file.close()
    
    def initialise_tags(self):
        self.tags = [[0 for x in range(0,self.ground_truth_number)] for x in range(0,self.cluster_number)]
        print(self.tags)

        for cluster_index in range(0, len(self.clustered_set)):
            for element in self.clustered_set[cluster_index]:
                for ground_truth_index in range(0, len(self.ground_truth)):
                    if element in self.ground_truth[ground_truth_index]:
                        self.tags[cluster_index][ground_truth_index] += 1
                        print('Element: ' + str(element) + ' is in cluster[' + str(cluster_index) + '] and in ground_truth[' + str(ground_truth_index) + ']')
                        print(self.tags)

    def compute_precision(self):
        greatest_appearence_number = 0
        greatest_appearence_index = 0
        total_hits = 0
        maximum_tag_number = self.greatest_tag()
        
        while maximum_tag_number > 0:
            greatest_appearence_number = 0
            for tag_index in range(0, len(self.tags)):
                for element_index in range(0, len(self.tags[tag_index])):
                    if self.tags[tag_index][element_index] >= greatest_appearence_number:
                        greatest_appearence_number = self.tags[tag_index][element_index]
                        greatest_appearence_index = element_index
            print('Greates number: ' + str(greatest_appearence_number) + ' index: ' + str(greatest_appearence_index))
            for tag_index in range(0, len(self.tags)):
                self.tags[tag_index][greatest_appearence_index] = 0
            total_hits += greatest_appearence_number
            maximum_tag_number = self.greatest_tag()

        total_clusters = self.total_clusters()
        return float(total_hits)/total_clusters

    def greatest_tag(self):
        maximum_tag_number = 0

        for tag_index in range(0, len(self.tags)):
            if max(self.tags[tag_index]) >= maximum_tag_number:
                maximum_tag_number = max(self.tags[tag_index])

        return maximum_tag_number

    def total_clusters(self):
        counter = 0

        for cluster_index in range(0, len(self.clustered_set)):
            counter += len(self.clustered_set[cluster_index])

        return counter



ground_truth_object = GroundTruth()
print(ground_truth_object.cluster_number)
print(ground_truth_object.ground_truth_number)
print(ground_truth_object.clustered_set)
print(ground_truth_object.ground_truth)
print(ground_truth_object.tags)
print(ground_truth_object.compute_precision())
