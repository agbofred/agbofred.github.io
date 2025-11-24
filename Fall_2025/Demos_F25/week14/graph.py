"""
File: graph.py
This module complete the class for linked directed graph
"""

from abstractcollection import AbstractCollection

class LinkedEdge:
    # Constructor
    def __init__(self, fromVertex, toVertex, weight =None):
        self.vertex1 = fromVertex
        self.vertex2 = toVertex
        self.weight = weight
        self.mark = False
        
    def clearMark(self):
        pass
    
    def __eq__(self, other):
        """Two edges are equal if they connect
        the same vertices."""
        if self is other: return True
        if type(self) != type(other):
            return False
        return self.vertex1 == other.vertex1 and self.vertex2 == other.vertex2
        
    
    def getOtherVertex(self, thisVertex):
        if thisVertex == None or thisVertex == self.vertex2:
            return self.vertex1
        else:
            return self.vertex2
    
    def getToVertex(self):
        return self.vertex2
    
    def getWeight(self):
        return self.weight
    
    def isMark(self):
        """Returns True if the edge is marked
        or False otherwise."""
        return self.mark

    def setMark(self):
        self.mark = True
    
    def setWeight(self, weight):
        self.weight = weight
        
    def __str__(self):
        return str(self.vertex1) + ">" + str(self.vertex2) + ":" + str(self.weight)
    
    
class LinkedVertex:
    # Constructor
    def __init__(self, label):
        self.label = label
        self.edgeList = []
        self.mark = False
        
          
    def clearMark(self):
        self.mark = False
        
    def isMark(self):
        """Returns True if the vertex is marked
        or False otherwise."""
        return self.mark

    def getLabel(self):
        """ Return the label for the vertex"""
        return self.label
        
    def setLabel(self, label, g):
        g.vertices.pop(self, label, None)
        g.vertices[label] = self
        self.label = label
    
    def setMark(self):
        self.mark = True
        
    def __str__(self):
        return str(self.label)
    
    def __eq__(self, other):
        if self is other: return True
        if type(self) != type(other): return False
        return self.getLabel() == other.getLabel()
    
    # Methods used by LinkedGraph
    
    def addEdgeTo(self, toVertex, weight):
        """Connects the vertices with an edge."""
        edge = LinkedEdge(self, toVertex, weight)
        self.edgeList.append(edge)
        
    def getEdgeTo(self, toVertex):
        """Return the connecting edge if it exists, or None otherwise"""
        edge = LinkedEdge(self, toVertex)
        try:
            return self.edgeList[self.edgeList.index(edge)]
        except:
            return None
        
    def incidentEdges(self):
        """Returns the incident edges of this vertex."""
        return iter(self.edgeList)
    
    def neighboringVertices(self):
        """Returns the neighboring vertices of this vertex."""
        vertices = []
        for edge in self.edgeList:
             vertices.append(edge.getOtherVertex(self))
        return iter(vertices)
    
    def removeEdgeto(self, toVertex):
        """Returns True if the edge exists and is removed,
        or False otherwise."""
        edge = LinkedEdge(self, toVertex)
        if edge in self.edgeList:
            self.edgeList.remove(edge)
            return True
        else:
            return False
    
        
class LinkedDirectedGraph(AbstractCollection):
    """A graph has a count of vertices, a count of edges,
    and a dictionary of label/vertex pairs."""
    def __init__(self, sourceCollection = None):
        self.edgeCount = 0
        self. vertices = {}
        AbstractCollection.__init__(self, sourceCollection)
        
    # Method for clearing, marks, sizes, string rep
    
    def clear(self):
        """clears the graph"""
        self.size = 0
        self.edgeCount = 0
        self.vertices = {}
        
    def clearEdgeMarks(self):
        """Clear all the edge marks"""
        for edge in self.edges():
            edge.clearMark()
            
    def sizeEdges(self):
        """Returns the number of edges """
        return self.edgeCount
    
    def sizeVertices(self):
        """Returns the number of vertices """
        return len(self)
    
    def __str__(self):
        """Returns the string respresentation of the graph """
        result = str(len(self)) + " vertices: "
        for vertex in self.vertices:
            result += " " + str(vertex)
        result += "\n"
        result += str(self.sizeEdges()) + " Edges: "
        for edge in self.edges():
            result += " " + str(edge)
        return result
    
    def add(self, label):
        """For compatibility with other collections."""
        self.addVertex(label)
        
    # Vertex related methods
    
    def addVertex(self, label):
        """Precondition: a vertex with label must not
        already be in the graph.
        Raises: AttibuteError if a vertex with label
        is already in the graph."""
        if self.containsVertex(label):
            raise AttributeError("Label "+ str(label) + " already in graph")
        self.vertices[label] = LinkedVertex(label)
        self.size += 1
    
    def containsVertex(self, label):
        return label in self.vertices
    
    def getVertex(self, label):
        """ pre-condition: a vetext with label must already be in the graph"""
        if not self.containsVertex(label):
            raise AttributeError("Label "+ str(label) + " not in graph.")
        return self.vertices[label]
    
    def removeVertex(self, label):
        """Returns True if the vertex was removed, or False otherwise."""
        removedVertex = self.vertices.pop(label, None)
        if removedVertex is None:
            return False
        # Examine all other vertices to remove edges 
        for vertex in self.getVertices():
            if vertex.removeEdgesTo(removedVertex):
                self.edgeCount -= 1
                
        # Examine all edges from the removed vertex to others
        for edge in removedVertex.incidentEdges():
            self.edgeCount -= 1
        self.size -=1
        return True
    
    # Methods related to edges
    
    def addEdge(self, fromLabel, toLabel, weight):
        fromVertex = self.getVertex(fromLabel)
        toVertex = self.getVertex(toLabel)
        if self.getEdge(fromLabel, toLabel):
            raise AttributeError("An edge already connects " + str(fromLabel) + " and "+ str(toLabel))
        fromVertex.addEdgeTo(toVertex, weight)
        self.edgeCount += 1
        
    def containsEdge(self, fromeLabel, toLabel):
        return self.getEdge(fromeLabel, toLabel) != None
    
    def getEdge(self, fromLabel, toLabel):
        fromVertex = self.getVertex(fromLabel)
        toVertex = self.getVertex(toLabel)
        return fromVertex.getEdgeTo(toVertex)
    
    def removeEdge(self, fromLabel, toLabel):
        fromVertex = self.getVertex(fromLabel)
        toVertex = self.getVertex(toLabel)
        edgeRemovedFlg = fromVertex.removeEdgeTo(toVertex)
        if edgeRemovedFlg:
            self.edgeCount -= 1
        return edgeRemovedFlg
    
    # Iterators 
    
    def __iter__(self):
        """Supports iteration over a view of self (the vertices)."""
        return self.getVertices()
    
    def edges(self):
        """Supports iteration over the edges in the graph."""
        result = []
        for vertex in self.getVertices():
            result += list(vertex.incidentEdges())
        return iter(result)
    
    def getVertices(self):
        """Supports iteration over the vertices in the graph."""
        return iter(self.vertices.values()) 
    
    def incidentEdges(self, label):
        """Supports iteration over the incident edges of the
        given verrtex."""
        return self.getVertex(label).incidentEdges()
    
    def neighboringVertices(self, label):
        return self.getVertex(label).neighboringVertices()
    