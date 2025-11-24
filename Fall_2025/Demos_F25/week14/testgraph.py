from graph import LinkedDirectedGraph

gr = LinkedDirectedGraph()

gr.addVertex("A")
gr.addVertex("B")
gr.addVertex("C")
gr.addVertex("D")
gr.addVertex("E")
gr.addVertex("F")

print("The graph Vertex is: "+ str(gr))

gr.addEdge("A", "B", 3)
gr.addEdge("A", "C", 5)
gr.addEdge("A", "D", 6)
gr.addEdge("D", "E", 10)
gr.addEdge("D", "F", 2)


print("Expect Edges:" + str(gr))
print("Neihboring vertex")
print(list(map(str, gr.neighboringVertices("D"))))
print(list(map(str, gr.incidentEdges("D"))))

