class Edge(object):
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def __str__(self):
        return "(" + str(self.a) + "," + str(self.b) + ")"

    def __repr__(self):
        return str(self)

# represents all nodes, even unconnected nodes
# make sure pass in Nodes to the graph
class Graph(object):
    def __init__(self, edges=[], nodes=[]):
        self.edges = edges
        self.nodes = nodes
        # check that all edges are contained in the nodes list - don't want to initialise a nodes list that doesn't contain all nodes
        for edge in edges:
            if edge.a in nodes and edge.b in nodes:
                pass
            else: 
                raise ValueError("graph constructed with an edge that has not been identified as a node. Check your edges are correct.")
    
    def __str__(self):
        return "Nodes = " + str(self.nodes) + " Edges = " + str(self.edges)

    #TODO
    def getNodeByKey(self, key):
        pass

class Node(object):
    def __init__(self, key): # key is the identity of the node (like an id), not the value 
        self.key = key
    
    def __str__(self):
        return str(self.key)
    
    def __repr__(self):
        return str(self)
    
def breadth_first_search(graph, startKey): # start parameter sometimes called source
    queue = []
    # first loop - go through all nodes in graph and set initial state
    for node in graph.nodes:
        node.distance = None # number edges from start (or source) to given node
        node.previous = None # previous node
        node.visited = False # boolean - visited already or not?
    # set values for start node
    start = next(n for n in graph.nodes if n.key == startKey)
    start.distance = 0
    start.previous = None
    start.visited = True 
    queue.append(start) # add start node to the queue
    # second loop - do the search
    # use the visited flag to check if we've already seen them before if already in the queue (so don't add them again)
    while queue: 
        # get first thing out of queue
        currentNode = queue.pop(0)
        print(currentNode)
        # find adjacent nodes to the dequeued node
        neighbours = []
        for edge in graph.edges:
            if edge.a == currentNode:
                neighbours.append(edge.b)
        # an alternative way of writing the for loop above using python's list comprehension:
        # https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
        # neighbours = [b for (a,b) in graph.edges if a == currentNode]
        
        for neighbour in neighbours:
            if not neighbour.visited: # if the node hasn't been visited already, append to queue
                queue.append(neighbour)
                neighbour.visited = True # mark the node as visited
   

myNodes = [Node(1), Node(2), Node(3)]
myEdges = [Edge(myNodes[0],myNodes[1]), Edge(myNodes[1],myNodes[2]), Edge(myNodes[2],myNodes[0])]
print(myEdges)
myGraph = Graph(myEdges, myNodes)
print(myGraph)

stationNodes = [Node("KingsX"), Node("Farringdon"), Node("Euston"), Node("Barbican")]
stationEdges = [Edge(stationNodes[0],stationNodes[1]), Edge(stationNodes[1],stationNodes[2]), Edge(stationNodes[2],stationNodes[0]), Edge(stationNodes[1], stationNodes[3])]
stationGraph = Graph(stationEdges, stationNodes)
print(stationGraph)

breadth_first_search(myGraph, 1)
breadth_first_search(stationGraph, "Barbican")