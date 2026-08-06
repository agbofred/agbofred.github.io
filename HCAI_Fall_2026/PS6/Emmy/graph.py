from abstractcollection import AbstractCollection

class AbstractStack(AbstractCollection):
    """An abstract stack implementation."""

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        AbstractCollection.__init__(self, sourceCollection)

    # Mutator methods
    def add(self, item):
        """Adds item to self."""
        self.push(item)

class Node(object):
    """Represents a singly linked node."""

    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class LinkedStack(AbstractStack):
    def __init__(self, sourceCollection = None):
        self.items = None
        AbstractStack.__init__(self, sourceCollection)
    def __iter__(self):
        def visitNodes(node):
            if node != None:
                visitNodes(node.next)
                tempList.append(node.data)
        tempList = list()
        visitNodes(self.items)
        return iter(tempList)
    def peek(self):
        if self.isEmpty():
            raise KeyError("The stack is empty.")
        return self.items.data
    def clear(self):
        self.size = 0
        self.items = None
    def push(self, item):
        self.items = Node(item, self.items)
        self.size += 1
    def pop(self):
        if self.isEmpty():
            raise KeyError("The stack is empty.")
        oldItem = self.items.data
        self.items = self.items.next
        self.size -= 1
        return oldItem

class LinkedEdge(object):
    def __init__(self, fromVertex, toVertex, weight = None):
        self.vertex1 = fromVertex
        self.vertex2 = toVertex
        self.weight = weight
        self.mark = False
    def __eq__(self, other):
        if self is other: return True
        if type(self) != type(other): return False
        return self.vertex1 == other.vertex1 and \
        self.vertex2 == other.vertex2 and \
        self.weight == other.weight

class LinkedVertex(object):
    def __init__(self, label):
        self.label = label
        self.edgeList = list()
        self.mark = False
    def setLabel(self, label, g):
        g.vertices.pop(self.label, None)
        g.vertices[label] = self
        self.label = label
    def neighboringVertices(self):
        vertices = list()
        for edge in self.edgeList:
            vertices.append(edge.getOtherVertex(self))
        return iter(vertices)
    def removeEdgeTo(self, toVertex):
        edge = LinkedEdge(self, toVertex)
        if edge in self.edgeList:
            self.edgeList.remove(edge)
            return True
        else:
            return False
    def getEdgeTo(self, toVertex):
        for edge in self.edgeList:
            if edge.vertex2 == toVertex:
                return edge
        return None
    def setMark(self):
        self.mark = True
    def isMarked(self):
        return self.mark

class LinkedDirectedGraph(AbstractCollection):
    def __init__(self, sourceCollection = None):
        self.edgeCount = 0
        self.vertices = dict()
        AbstractCollection.__init__(self, sourceCollection)
    def addVertex(self, label):
        self.vertices[label] = LinkedVertex(label)
        self.size += 1
    def removeVertex(self, label):
        removedVertex = self.vertices.pop(label, None)
        if removedVertex is None:
            return False
        for vertex in self.getVertices():
            if vertex.removeEdgeTo(removedVertex):
                self.edgeCount -= 1
        for edge in removedVertex.incidentEdges():
            self.edgeCount -= 1
        self.size -= 1
        return True
    def addEdge(self, fromLabel, toLabel, weight):
        fromVertex = self.getVertex(fromLabel)
        toVertex = self.getVertex(toLabel)
        fromVertex.addEdgeTo(toVertex, weight)
        self.edgeCount += 1
    def getEdge(self, fromLabel, toLabel):
        fromVertex = self.getVertex(fromLabel)
        toVertex = self.getVertex(fromLabel)
        return fromVertex.getEdgeTo(toVertex)
    def removeEdge(self, fromLabel, toLabel):
        fromVertex = self.getVertex(fromLabel)
        toVertex = self.getVertex(toLabel)
        edgeRemovedFlg = fromVertex.removeEdgeTo(toVertex)
        if edgeRemovedFlg:
            self.edgeCount -= 1
        return edgeRemovedFlg
    def edges(self):
        result = set()
        for vertex in self.getVertices():
            edges = vertex.incidentEdges()
            result = result.union(set(edges))
        return iter(result)
    def containsVertex(self, label):
        return label in self.vertices            
    def containsEdge(self, fromLabel, toLabel):
        fromVertex = self.getVertex(fromLabel)
        return fromVertex and fromVertex.getEdgeTo(self.getVertex(toLabel)) is not None
    def getEdgeTo(self, toVertex):
        for edge in self.edgeList:
            if edge.vertex2 == toVertex:
                return edge
        return None        
    def getVertex(self, label):
        return self.vertices.get(label, None)
    def getVertices(self):
        return self.vertices.values()