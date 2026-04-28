from graph import LinkedDirectedGraph


# Instance of graph

g = LinkedDirectedGraph()

g.addVertex("a")
g.addVertex("B")
g.addVertex("C")
g.addVertex("D")
g.addVertex("A")

g.addEdge("A", "B", 4)
g.addEdge("A", "a", 10)
g.addEdge("A", "C", 20)
g.addEdge("B", "A", 20)

for i in g.neighboringVertices("B"):
    print(i)
print("Incident edges of A:", list(map(str, g.incidentEdges("A"))))
# print(g)