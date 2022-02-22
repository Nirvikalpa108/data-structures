#myGraph = {
#  "Bank": ["Waterloo", "Liverpool Street"],
#  "Waterloo": ["Bank", "Brixton"],
#  "Liverpool Street": ["Bank", "Bethnal Green"]
#}

myMatrix = [
    [0,1,1,0,0],
    [1,0,0,1,0],
    [1,0,0,0,1],
    [0,1,0,0,0],
    [0,0,1,0,0]
]

myStations = ["Bank", "Waterloo", "Lpool street", "Brixton", "BGreen"]

def addEdge(matrix, nodes, start, end):
    matrix[nodes.index(start)][nodes.index(end)] = 1
    matrix[nodes.index(end)][nodes.index(start)] = 1
    return matrix 

def addEdges(matrix, nodes, start, neighbours):
    print(neighbours)
    s = nodes.index(start)
    for n in neighbours:
        ne = nodes.index(n)
        print(s, ne)
        #matrix[s][ne] = 1 # [0][1] [0][2]
        matrix[ne][s] = 1 # [1][0]
    return matrix 

def hasEdge(matrix, nodes, start, end): 
    return matrix[nodes.index(start)][nodes.index(end)] == 1

def getDestinations(matrix, nodes, start):
    i = nodes.index(start)
    destinations = matrix[i]
    index = 0
    destinationNames = []
    for station in destinations:
        if station == 1:
            destinationNames.append(nodes[index])
        index += 1
    return destinationNames

def createMatrix(length):
    return [[0] * length] * length

def printMatrix(matrix):
    print(" " + str(range(len(matrix))))
    row = 0
    for line in matrix:
        print(str(row) + str(line))
        row += 1

print(hasEdge(myMatrix, myStations, "Lpool street", "BGreen"))
print(hasEdge(myMatrix, myStations, "Brixton", "BGreen"))
print(getDestinations(myMatrix, myStations, "Bank"))
print(getDestinations(myMatrix, myStations, "Brixton"))
printMatrix(addEdge(myMatrix, myStations, "Brixton", "BGreen"))
newMatrix = createMatrix(5)
printMatrix(newMatrix)
printMatrix(addEdges(newMatrix, myStations, "Bank", ["Waterloo", "Lpool street"]))
