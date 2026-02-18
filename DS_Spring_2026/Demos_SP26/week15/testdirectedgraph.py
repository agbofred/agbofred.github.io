from graph import LinkedDirectedGraph

g = LinkedDirectedGraph()

g.addVertex("A")
g.addVertex("B")
g.addVertex("C")
g.addVertex("D")
g.addVertex("E")


print('The graph is: '+ str(g))

#adding Edges 

g.addEdge("A", "B", 5)
g.addEdge("A", "C", 2.5)
g.addEdge("C", "D", 4)
g.addEdge("E", "B", 10)

print("Expect same vertices and edges \n" + str(g))

#g.addVertex("A")

g.addEdge("A", "D", 2.5)

#g.addEdge("A", "B", 2.5)

print("Incident edges of A:", list(map(str, g.incidentEdges("A"))))
print(list(map(str, g.incidentEdges("D"))))
print(list(map(str, g.neighboringVertices("E"))))