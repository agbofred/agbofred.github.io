from week16.graph import LinkedDirectedGraph


g = LinkedDirectedGraph()

g.addVertex("A")
g.addVertex("B")
g.addVertex("C")
g.addVertex("D")
g.addVertex("E")
g.addVertex("F")



g.addEdge("A", "B", 10)
g.addEdge("A", "C", 50)
g.addEdge("A", "D", 20)
g.addEdge("A", "E", 10)
g.addEdge("A", "F", 5)
g.addEdge("B", "C", 1)

print(g)
