class UnitTests(unittest.TestCase):

  def test(self):
    g = LinkedDirectedGraph()
    g.addVertex("A")
    g.addVertex("B")
    g.addVertex("C")
    g.addEdge("A", "B", 2.5)
    with self.assertRaises(AttributeError):
        g.addEdge("A", "B", 2.5)

  def test_addVertex(self):
    g = LinkedDirectedGraph()
    g.addVertex("A")
    g.addVertex("B")
    g.addVertex("C")
    g.addEdge("A", "B", 2.5)
    with self.assertRaises(AttributeError):
        g.addVertex("A")

  def test_getVertex(self):
    g = LinkedDirectedGraph()
    g.addVertex("A")
    g.addVertex("B")
    g.addVertex("C")
    g.addEdge("A", "B", 2.5)
    with self.assertRaises(AttributeError):
        g.getVertex("F")

    def test_getEdge(self):
      g = LinkedDirectedGraph()
      g.addVertex("A")
      g.addVertex("B")
      g.addVertex("C")
      g.addEdge("A", "B", 2.5)
      with self.assertRaises(AttributeError):
          g.getEdge("Q", "P")