class Edge(object):
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def __str__(self):
        return "(" + str(self.a) + "," + str(self.b) + ")"

    def __repr__(self):
        return str(self)

# represents all nodes, even unconnected nodes
class Graph(object):
    def __init__(self, edges=[], nodes=[]):
        self.edges = edges
        self.nodes = nodes
        # check that all edges are contained in the nodes list
        # don't want to initialise a nodes list that doesn't contain all nodes
        for edge in edges:
            if edge.a in nodes and edge.b in nodes:
                pass
            else: 
                raise ValueError("graph constructed with an edge that has not been identified as a node. Check your edges are correct.")
    
    def __str__(self):
        return "Nodes = " + str(self.nodes) + " Edges = " + str(self.edges)

    # h/w - complete heaps h/w (max heap and heap sort)
    # h/w - read about the traversals 
    # DONE - h/w - exception should say "graph constructed with edge xx, but no such node found" / or easier - nice exception msg

myEdges = [Edge(1,2), Edge(2,3), Edge(3,1)]
print(myEdges)
myGraph = Graph(myEdges, [1,2,3])
print(myGraph)