from graph import LinkedDirectedGraph

l = LinkedDirectedGraph()

for v in ["A", "B", "C", "D"]:
    l.addVertex(v)

l.addEdge("A", "B", 4)
l.addEdge("A", "C", 1)
l.addEdge("B", "D", 2)
l.addEdge("C", "D", 5)


print(f'Spanning Tree Start: ')

tree = l.spanTree("A")
for label in tree.vertices:
    print(label)

print(f'Shortest Path from A: ')
print(l.shortestPaths("A"))
