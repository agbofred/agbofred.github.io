"""
File: algorithms.py

Project 12.2

Completes the other classes for this application.

Graph processing algorithms
"""

from week16.linkedstack import LinkedStack

def topoSort(g, startLabel = None):  
    stack = LinkedStack()
    g.clearEdgeMarks()
    for v in g.getVertices():
        if not v.isMark():
            dfs(g, v, stack)
    return stack

def dfs(g, v, stack):
    v.setMark()
    for w in g.neighboringVertices(v.getLabel()):
        if not w.isMark():
            dfs(g, w, stack)
    stack.push(v)
    
def shortestPaths(g, startLabel):
    """Returns shortest paths from startLabel to all other vertices using Dijkstra's algorithm."""
    # Initialize data structures
    
def spanTree(g, startLabel):
    """Returns a minimum spanning tree using Prim's algorithm."""
    # Mark all vertices and edges as unvisited
