# simpler graph representation than graph.py
# dictionary - keys are numbers (nodes), values list nodes you could go to
# 1 -> (2,3) 1 is node and 2 and 3 are the nodes you can get to from 1

# this search can be used in so many ways. this one is just printing the node values in the order visited.
# there are other ways this algo could be used
def depth_first_search(graph, source, visited = []):
    # each node will be printed and put in the visited array
    print(source)
    visited.append(source)
    # recursively visit each node
    neighbours = graph.get(source)
    if neighbours:
        for neighbour in neighbours:
            if neighbour not in visited:
                depth_first_search(graph, neighbour, visited)
    else:
        return 

myGraph = {
  "Bank": ["Waterloo", "Liverpool Street"],
  "Waterloo": ["Bank", "Brixton"],
  "Liverpool Street": ["Bank", "Bethnal Green"]
}

print(myGraph)
depth_first_search(myGraph, "Bank")

