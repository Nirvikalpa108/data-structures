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

class Node(object):
    def __init__(self, key): # key is the identity of the node (like an id), not the value 
        self.key = key
    
    def __str__(self):
        return str(self.key)
    
    def __repr__(self):
        return str(self)
    
# compute extra properties for each node:
    # distance - number edges from start (or source) to given node
    # previous - previous of each node
    # visited boolean/colour - have we visited node already? (max's book uses three colours - do we need three options or is a boolean enough?)
def breadth_first_search(graph, start): # start parameter sometimes called source
    queue = []
    # first loop - graph - go through all nodes in graph and set initial state
    for node in graph.nodes:
        node.distance = None # value that makes it obvious it's not been set
        node.previous = None
        node.visited = False 
    # set special values for start node
    start.distance = 0
    start.previous = None
    start.visited = True 
    queue.append(start) # add start node to the queue
    # second loop - do the search
    # use the visited flag to check if we've already seen them before if already in the queue (so don't add them again)
    while not queue:
        node = queue.pop[0] # get first thing out of queue
        # find nodes connected to given node
        # add them to the queue
        # set their properties
        # what is prev?
        # TODO: add visited property later
        # Amina - use graph object to find all nodes connected to given node
        # chat my findings to Max and then continue step by step

# h/w - in example, instead of Ints, use Kings X/Farringdon example
# h/w - visualise the distance/prev/visited    
# h/w - start looking at depth first search

myNodes = [Node(1), Node(2), Node(3)]
myEdges = [Edge(myNodes[0],myNodes[1]), Edge(myNodes[1],myNodes[2]), Edge(myNodes[2],myNodes[0])]
print(myEdges)
myGraph = Graph(myEdges, myNodes)
print(myGraph)
breadth_first_search(myGraph, 1)