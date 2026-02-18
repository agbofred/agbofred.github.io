"""
File: algorithms.py

Project 12.2

Completes the other classes for this application.

Graph processing algorithms
"""

from linkedstack import LinkedStack

def topoSort(g, startLabel = None):  
    stack = LinkedStack()
    g.clearVertexMarks()
    for v in g.getVertices():
        if not v.isMarked():
            dfs(g, v, stack)
    return stack

def dfs(g, v, stack):
    v.setMark()
    for w in g.neighboringVertices(v.getLabel()):
        if not w.isMarked():
            dfs(g, w, stack)
    stack.push(v)

def shortestPaths(g, startLabel):
    """Returns shortest paths from startLabel to all other vertices using Dijkstra's algorithm."""
    # Initialize data structures
    distances = {}  # Stores shortest distance from start to each vertex
    parents = {}    # Stores parent vertex in shortest path
    included = {}   # Tracks which vertices are included in final solution
    
    # Get the start vertex
    startVertex = g.getVertex(startLabel)
    
    # Initialization step
    for vertex in g.getVertices():
        label = vertex.getLabel()
        if vertex == startVertex:
            distances[label] = 0
            parents[label] = None
            included[label] = True
        else:
            # Check if there's an edge from start to this vertex
            edge = startVertex.getEdgeTo(vertex)
            if edge:
                distances[label] = edge.getWeight()
                parents[label] = startLabel
            else:
                distances[label] = float('inf')
                parents[label] = None
            included[label] = False
    
    # Computation step - Dijkstra's algorithm
    while not all(included.values()):
        # Find vertex F that is not yet included and has minimal distance
        minDistance = float('inf')
        F = None
        for label in distances:
            if not included[label] and distances[label] < minDistance:
                minDistance = distances[label]
                F = label
        
        # If no vertex found, break (disconnected graph)
        if F is None:
            break
        
        # Mark F as included
        included[F] = True
        
        # Get the vertex object for F
        FVertex = g.getVertex(F)
        
        # For each other vertex T not included
        for vertex in g.getVertices():
            T = vertex.getLabel()
            if not included[T]:
                # Check if there's an edge from F to T
                edge = FVertex.getEdgeTo(vertex)
                if edge:
                    # Calculate new distance
                    newDistance = distances[F] + edge.getWeight()
                    # If new distance is shorter, update it
                    if newDistance < distances[T]:
                        distances[T] = newDistance
                        parents[T] = F
    
    # Format and return results
    results = []
    for label in distances:
        if label != startLabel:
            if distances[label] == float('inf'):
                results.append(f"{label}: No path")
            else:
                # Build the path
                path = []
                current = label
                while current is not None:
                    path.insert(0, current)
                    current = parents[current]
                pathStr = "->".join(path)
                results.append(f"{label}: {pathStr} (distance: {distances[label]})")
    
    return results

def spanTree(g, startLabel):
    """Returns a minimum spanning tree using Prim's algorithm."""
    # Mark all vertices and edges as unvisited
    g.clearVertexMarks()
    g.clearEdgeMarks()
    
    # Get the start vertex and mark it as visited
    startVertex = g.getVertex(startLabel)
    startVertex.setMark()
    
    # List to store the edges in the spanning tree
    spanningTreeEdges = []
    
    # Number of vertices
    numVertices = len(g)
    
    # For all vertices minus the starting one
    count = 0
    while count < numVertices - 1:
        # Find the minimum weight edge from a visited vertex to an unvisited vertex
        minEdge = None
        minWeight = float('inf')
        
        # Check all visited vertices
        for vertex in g.getVertices():
            if vertex.isMarked():
                # Check all incident edges of this visited vertex
                for edge in vertex.incidentEdges():
                    toVertex = edge.getToVertex()
                    # If the edge leads to an unvisited vertex
                    if not toVertex.isMarked():
                        weight = edge.getWeight()
                        if weight < minWeight:
                            minWeight = weight
                            minEdge = edge
        
        # If we found an edge, mark it and the destination vertex
        if minEdge:
            minEdge.setMark()
            minEdge.getToVertex().setMark()
            spanningTreeEdges.append(minEdge)
        
        count += 1
    
    return spanningTreeEdges


