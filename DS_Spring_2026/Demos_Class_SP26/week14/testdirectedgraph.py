from graph import LinkedDirectedGraph

g = LinkedDirectedGraph()

g.addVertex("Z")
g.addVertex("U")
g.addVertex("Y")

g.addEdge("Z", "U", 7)
g.addEdge("Z", "Y", 10)
g.addEdge("Y", "U", 20)

print (g.getVertices())