import sys
import os
import random
    
print("USAGE: generate_dataset.py <dirName> <nNodes> <nGroups> <method>")
print("       nNodes >= nGroups")
print("       <method> = 'random'")
print("Example: generate_dataset.py large_dataset 100 10 random")

if len(sys.argv) != 5:
    print("EXITING...")
    exit()

dirName = sys.argv[1]
nNodes = int(sys.argv[2])
nGroups = int(sys.argv[3])
method = sys.argv[4]

if not os.path.exists(dirName):
    os.makedirs(dirName)

if nNodes < nGroups:
    print("Invalid data")
    exit()

fNodes = open(dirName + "/nodes.csv", "w")
for i in range(1, nNodes + 1):
    fNodes.write(str(i) + "\n")
fNodes.close()

fGroup = open(dirName + "/group.csv", "w")
for i in range(1, nGroups + 1):
    fGroup.write(str(i) + "\n")
fGroup.close()

edges = [0] * (nNodes + 1)
for i in range(1, nNodes + 1):
    edges[i] = [0] * (nNodes + 1)

nodeGroupMapping = [0] * (nNodes + 1)

if method == "random":
    nMaxEdges = (nNodes * (nNodes - 1)) / 2
    
    nEdges = int(nMaxEdges / 10) # hardcoded (10)
    
    for i in range(nEdges):
        while True:
            x = random.randint(1, nNodes)
            y = random.randint(1, nNodes)
            if x != y and edges[x][y] == 0:
                edges[x][y] = 1
                edges[y][x] = 1
                break

    for i in range(1, nNodes + 1):
        nodeGroupMapping[i] = random.randint(1, nGroups)

fEdges = open(dirName + "/edges.csv", "w")
for i in range(1, nNodes + 1):
    for j in range(i, nNodes + 1):
        if edges[i][j] == 1:
            fEdges.write(str(i) + "," + str(j) + "\n")
fEdges.close()        


fGroupEdges = open(dirName + "/group-edges.csv", "w")
for i in range(1, nNodes + 1):
    fGroupEdges.write(str(i) + "," + str(nodeGroupMapping[i]) + "\n")
fGroupEdges.close()        
